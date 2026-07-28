#!/usr/bin/env python3
"""Positive, negative, and adversarial tests for BP2 data administration."""

from __future__ import annotations

import copy
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = (
    ROOT / "repository/data/validation/validate_bp2_data_administration.py"
)
CONTRACT = (
    ROOT / "repository/data/contracts/bp2-data-administration-v1.0.json"
)
SCHEMA = (
    ROOT / "repository/data/schemas/bp2-data-administration-v1.0.schema.json"
)
SOURCE = (
    ROOT / "repository/data/contracts/bp2-pipe-data-blueprint-v0.1.json"
)
FIXTURES = ROOT / "tests/fixtures/bp2-data-administration"
MUTATION_CASES = FIXTURES / "mutation-cases.json"
SUCCESS_MARKER = "BP2 DATA ADMINISTRATION VALIDATION PASSED"


def decode_pointer(path: str) -> list[str]:
    if not path.startswith("/"):
        raise AssertionError(f"invalid JSON Pointer: {path}")
    return [
        part.replace("~1", "/").replace("~0", "~")
        for part in path[1:].split("/")
    ]


def resolve_parent(document: Any, path: str) -> tuple[Any, str]:
    parts = decode_pointer(path)
    if not parts:
        raise AssertionError("root mutation is not supported")
    parent = document
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    return parent, parts[-1]


def apply_mutation(document: Any, case: dict[str, Any]) -> None:
    operation = case["operation"]
    path = case["path"]
    if operation == "append":
        target = document
        for part in decode_pointer(path):
            target = target[int(part)] if isinstance(target, list) else target[part]
        if not isinstance(target, list):
            raise AssertionError(f"append target is not an array: {path}")
        target.append(copy.deepcopy(case["value"]))
        return

    parent, key = resolve_parent(document, path)
    if operation == "set":
        if isinstance(parent, list):
            parent[int(key)] = copy.deepcopy(case["value"])
        else:
            parent[key] = copy.deepcopy(case["value"])
    elif operation == "delete":
        if isinstance(parent, list):
            del parent[int(key)]
        else:
            del parent[key]
    else:
        raise AssertionError(f"unsupported mutation operation: {operation}")


class BP2DataAdministrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.canonical = {
            "contract": json.loads(CONTRACT.read_text(encoding="utf-8")),
            "schema": json.loads(SCHEMA.read_text(encoding="utf-8")),
            "source": json.loads(SOURCE.read_text(encoding="utf-8")),
        }
        manifest = json.loads(MUTATION_CASES.read_text(encoding="utf-8"))
        cls.mutation_cases = manifest["cases"]

    def run_validator(
        self,
        *,
        contract: Path = CONTRACT,
        schema: Path = SCHEMA,
        source: Path = SOURCE,
        explicit_paths: bool = True,
    ) -> subprocess.CompletedProcess[str]:
        command = [sys.executable, str(VALIDATOR)]
        if explicit_paths:
            command.extend(
                [
                    "--contract",
                    str(contract),
                    "--schema",
                    str(schema),
                    "--source",
                    str(source),
                ]
            )
        return subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def assert_rejected(
        self,
        result: subprocess.CompletedProcess[str],
        expected_code: str,
    ) -> None:
        combined = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, combined)
        self.assertIn(f"[{expected_code}]", combined)
        self.assertNotIn("Traceback", combined)
        self.assertNotIn(SUCCESS_MARKER, combined)

    def test_positive_canonical_default_paths(self) -> None:
        result = self.run_validator(explicit_paths=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(SUCCESS_MARKER, result.stdout)
        self.assertEqual(result.stderr, "")

    def test_positive_canonical_explicit_paths(self) -> None:
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(SUCCESS_MARKER, result.stdout)
        self.assertEqual(result.stderr, "")

    def test_positive_validator_import_has_no_side_effect(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        spec = importlib.util.spec_from_file_location(
            "bp2_data_administration_validator",
            VALIDATOR,
        )
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        with redirect_stdout(stdout), redirect_stderr(stderr):
            spec.loader.exec_module(module)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")

    def test_positive_lifecycle_transition_chain(self) -> None:
        lifecycle = self.canonical["contract"]["lifecycle"]
        current_status = "DRAFT"
        for transition in lifecycle["transition_history"]:
            self.assertEqual(transition["from"], current_status)
            self.assertNotEqual(
                (transition["from"], transition["to"]),
                ("DRAFT", "APPROVED"),
            )
            current_status = transition["to"]
        self.assertEqual(current_status, lifecycle["status"])
        self.assertNotIn("FOUNDER", lifecycle["reviewers"])

    def test_negative_direct_draft_to_approved_transition(self) -> None:
        spec = importlib.util.spec_from_file_location(
            "bp2_data_administration_lifecycle_validator",
            VALIDATOR,
        )
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        mutated = copy.deepcopy(self.canonical["contract"])
        mutated["lifecycle"]["status"] = "APPROVED"
        mutated["lifecycle"]["review_outcome"] = "PASS"
        mutated["lifecycle"]["transition_history"] = [
            {
                "from": "DRAFT",
                "to": "APPROVED",
                "decided_by": "FOUNDER",
                "decided_on": "2026-07-28",
                "decision_id": "FD-BP2-ADM-001",
                "evidence_reference": (
                    "docs/17_FOUNDER_DECISION_LOG.md"
                    "#bp2-data-administration-lifecycle-decision"
                ),
            }
        ]
        with self.assertRaises(module.ValidationFailure) as context:
            module.validate_lifecycle_history(mutated)
        self.assertEqual(context.exception.code, "LIFECYCLE_TRANSITION")

    def test_negative_raw_json_fixtures(self) -> None:
        fixtures = [
            ("invalid-malformed.json", "JSON_INVALID"),
            ("invalid-root-array.json", "ROOT_TYPE"),
            ("adversarial-duplicate-key.json", "JSON_DUPLICATE_KEY"),
        ]
        for target in ("contract", "schema", "source"):
            for filename, expected_code in fixtures:
                with self.subTest(target=target, filename=filename):
                    arguments = {target: FIXTURES / filename}
                    result = self.run_validator(**arguments)
                    self.assert_rejected(result, expected_code)

    def test_negative_missing_inputs(self) -> None:
        missing = FIXTURES / "does-not-exist.json"
        for target in ("contract", "schema", "source"):
            with self.subTest(target=target):
                arguments = {target: missing}
                result = self.run_validator(**arguments)
                self.assert_rejected(result, "FILE_MISSING")

    def test_negative_invalid_schema_keyword(self) -> None:
        result = self.run_validator(
            schema=FIXTURES / "invalid-schema-keyword.json"
        )
        self.assert_rejected(result, "SCHEMA_INVALID")

    def test_negative_invalid_utf8(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix="bp2-data-administration-invalid-utf8-"
        ) as temporary_directory:
            invalid_utf8 = Path(temporary_directory) / "invalid-utf8.json"
            invalid_utf8.write_bytes(b"\xff\xfe")
            result = self.run_validator(contract=invalid_utf8)
        self.assert_rejected(result, "JSON_INVALID")

    def test_adversarial_schema_fixtures(self) -> None:
        cases = [
            (
                "adversarial-permissive-schema.json",
                "SCHEMA_CONTRACT_WEAKENED",
            ),
            (
                "adversarial-remote-ref-schema.json",
                "SCHEMA_CONTRACT_WEAKENED",
            ),
        ]
        for filename, expected_code in cases:
            with self.subTest(filename=filename):
                result = self.run_validator(schema=FIXTURES / filename)
                self.assert_rejected(result, expected_code)

    def test_negative_and_adversarial_mutations(self) -> None:
        for case in self.mutation_cases:
            with self.subTest(case=case["id"]):
                values = copy.deepcopy(self.canonical)
                apply_mutation(values[case["target"]], case)
                with tempfile.TemporaryDirectory(
                    prefix="bp2-data-administration-"
                ) as temporary_directory:
                    temporary = Path(temporary_directory)
                    paths: dict[str, Path] = {}
                    for target, value in values.items():
                        path = temporary / f"{target}.json"
                        path.write_text(
                            json.dumps(value, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8",
                        )
                        paths[target] = path
                    result = self.run_validator(
                        contract=paths["contract"],
                        schema=paths["schema"],
                        source=paths["source"],
                    )
                self.assert_rejected(result, case["expected_code"])

    def test_error_output_is_deterministic(self) -> None:
        first = self.run_validator(
            contract=FIXTURES / "adversarial-duplicate-key.json"
        )
        second = self.run_validator(
            contract=FIXTURES / "adversarial-duplicate-key.json"
        )
        self.assertEqual(first.returncode, second.returncode)
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(first.stderr, second.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
