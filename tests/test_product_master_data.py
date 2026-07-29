#!/usr/bin/env python3
"""Positive, negative, and adversarial tests for PD-01 Product Master Data."""

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
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_DIR = ROOT / "repository/data/validation"
VALIDATOR = VALIDATION_DIR / "validate_product_master_data.py"
CONTRACT = ROOT / "repository/data/contracts/product-master-data.contract.yaml"
SCHEMA = ROOT / "repository/data/schemas/product-master-data.schema.json"
ATTRIBUTES = ROOT / "tests/fixtures/product-attributes/valid-measured-attribute.yaml"
ENTITIES = ROOT / "tests/fixtures/product-core/valid-minimal.yaml"
CANONICAL_ATTRIBUTE_REGISTRY = (
    ROOT / "repository/data/registries/product-attributes.yaml"
)
FIXTURES = ROOT / "tests/fixtures/product-master-data"
VALID_BUNDLE = FIXTURES / "valid-synthetic-minimal.yaml"
MUTATION_CASES = FIXTURES / "mutation-cases.json"
SUCCESS_MARKER = "PD-01 PRODUCT MASTER DATA VALIDATION PASSED"


def load_validator_module() -> Any:
    sys.path.insert(0, str(VALIDATION_DIR))
    try:
        spec = importlib.util.spec_from_file_location(
            "pd01_product_master_data_validator",
            VALIDATOR,
        )
        if spec is None or spec.loader is None:
            raise AssertionError("unable to load PD-01 validator module")
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(VALIDATION_DIR))


def resolve(document: Any, path: list[Any]) -> Any:
    target = document
    for part in path:
        target = target[part] if isinstance(part, int) else target[part]
    return target


def resolve_parent(document: Any, path: list[Any]) -> tuple[Any, Any]:
    if not path:
        raise AssertionError("root mutation is unsupported")
    return resolve(document, path[:-1]), path[-1]


def apply_mutation(document: Any, case: dict[str, Any]) -> None:
    operation = case["operation"]
    path = case["path"]
    if operation == "append":
        target = resolve(document, path)
        if not isinstance(target, list):
            raise AssertionError(f"append target is not a list: {path}")
        target.append(copy.deepcopy(case["value"]))
        return
    if operation == "append_copy":
        target = resolve(document, path)
        if not isinstance(target, list):
            raise AssertionError(f"append_copy target is not a list: {path}")
        target.append(copy.deepcopy(resolve(document, case["copy_path"])))
        return

    parent, key = resolve_parent(document, path)
    if operation == "set":
        parent[key] = copy.deepcopy(case["value"])
    elif operation == "delete":
        del parent[key]
    else:
        raise AssertionError(f"unsupported mutation operation: {operation}")


class ProductMasterDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_validator_module()
        cls.definitions = cls.module.load_definitions(CONTRACT, SCHEMA)
        cls.entities, _ = cls.module.load_yaml(ENTITIES, "Product Core fixture")
        cls.attributes, _ = cls.module.load_yaml(
            ATTRIBUTES,
            "Product Attribute fixture",
        )
        cls.bundle, _ = cls.module.load_yaml(
            VALID_BUNDLE,
            "Product Master Data fixture",
        )
        cls.mutation_cases = json.loads(
            MUTATION_CASES.read_text(encoding="utf-8")
        )

    def run_validator(
        self,
        *,
        source: Path = VALID_BUNDLE,
        contract: Path = CONTRACT,
        schema: Path = SCHEMA,
        explicit_paths: bool = True,
    ) -> subprocess.CompletedProcess[str]:
        command = [sys.executable, str(VALIDATOR)]
        if explicit_paths:
            command.extend(
                [
                    str(source),
                    "--entities",
                    str(ENTITIES),
                    "--attributes",
                    str(ATTRIBUTES),
                    "--contract",
                    str(contract),
                    "--schema",
                    str(schema),
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
        expected_text: str,
    ) -> None:
        combined = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, combined)
        self.assertIn(expected_text, combined)
        self.assertNotIn("Traceback", combined)
        self.assertNotIn(SUCCESS_MARKER, combined)

    def test_positive_default_paths(self) -> None:
        result = self.run_validator(explicit_paths=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(SUCCESS_MARKER, result.stdout)
        self.assertEqual(result.stderr, "")

    def test_positive_explicit_paths(self) -> None:
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(SUCCESS_MARKER, result.stdout)
        self.assertEqual(result.stderr, "")

    def test_positive_import_has_no_output_or_side_effect(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            module = load_validator_module()
        self.assertIsNotNone(module)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")

    def test_positive_validation_needs_no_network(self) -> None:
        with patch("socket.socket", side_effect=AssertionError("network forbidden")):
            issues = self.module.validate_bundle(
                copy.deepcopy(self.bundle),
                "<offline-test>",
                self.definitions,
                copy.deepcopy(self.entities),
                copy.deepcopy(self.attributes),
            )
        self.assertEqual(issues, [])

    def test_positive_pd02b_attributes_do_not_enable_master_data(self) -> None:
        registry, _ = self.module.load_yaml(
            CANONICAL_ATTRIBUTE_REGISTRY,
            "canonical Product Attribute registry",
        )
        attributes = registry["attributes"]
        self.assertEqual(
            {attribute["attribute_key"] for attribute in attributes},
            {"material", "grade"},
        )
        self.assertTrue(
            all(
                attribute["status"] == "CANDIDATE_UNVERIFIED"
                for attribute in attributes
            )
        )
        self.assertFalse(
            self.definitions.contract["data_boundary"][
                "canonical_population_authority"
            ]
        )

    def test_positive_mutation_matrix_has_negative_and_adversarial_depth(self) -> None:
        identifiers = [case["id"] for case in self.mutation_cases]
        self.assertGreaterEqual(len(identifiers), 50)
        self.assertEqual(len(identifiers), len(set(identifiers)))
        self.assertTrue(any(identifier.startswith("N") for identifier in identifiers))
        self.assertTrue(any(identifier.startswith("A") for identifier in identifiers))

    def test_negative_direct_draft_to_approved_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.definitions.contract)
        mutated["pd01_lifecycle"]["current_status"] = "APPROVED"
        mutated["pd01_lifecycle"]["transition_history"] = [
            {
                "from": "DRAFT",
                "to": "APPROVED",
                "evidence_reference": "FD-PD01-001",
            }
        ]
        with self.assertRaises(self.module.ConfigurationError):
            self.module.validate_lifecycle(mutated)

    def test_negative_duplicate_yaml_key_is_rejected(self) -> None:
        result = self.run_validator(source=FIXTURES / "invalid-duplicate-key.yaml")
        self.assert_rejected(result, "[DUPLICATE_KEY]")

    def test_negative_duplicate_json_key_is_rejected(self) -> None:
        with self.assertRaises(self.module.DuplicateKeyError):
            self.module.strict_json('{"a": 1, "a": 2}', "duplicate JSON")
        attribute_module = sys.modules["validate_product_attributes"]
        with self.assertRaises(attribute_module.DefinitionError):
            attribute_module.parse_json('{"a": 1, "a": 2}', "attribute duplicate JSON")

    def test_negative_non_finite_json_number_is_rejected(self) -> None:
        with self.assertRaises(self.module.ConfigurationError):
            self.module.strict_json('{"value": NaN}', "non-finite JSON")

    def test_adversarial_deep_structure_is_rejected(self) -> None:
        deep: Any = "leaf"
        for _ in range(self.module.MAX_NESTING_DEPTH + 1):
            deep = {"child": deep}
        with self.assertRaises(self.module.ConfigurationError):
            self.module.ensure_bounded_structure(deep, "deep structure")

    def test_adversarial_permissive_schema_is_rejected(self) -> None:
        result = self.run_validator(
            schema=FIXTURES / "adversarial-permissive-schema.json"
        )
        self.assert_rejected(result, "schema root must be closed")

    def test_adversarial_remote_ref_schema_is_rejected(self) -> None:
        result = self.run_validator(
            schema=FIXTURES / "adversarial-remote-ref-schema.json"
        )
        self.assert_rejected(result, "non-local schema reference is forbidden")

    def test_adversarial_path_escape_is_rejected(self) -> None:
        outside = Path("/etc/hosts")
        if not outside.exists():
            self.skipTest("no stable existing path outside repository")
        with self.assertRaises(self.module.ConfigurationError):
            self.module.safe_path(outside, "escaped input")

    def test_adversarial_symlink_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix="pd01-symlink-",
            dir=ROOT / "tests",
        ) as directory:
            symlink = Path(directory) / "bundle.yaml"
            symlink.symlink_to(VALID_BUNDLE)
            with self.assertRaises(self.module.ConfigurationError):
                self.module.safe_path(symlink, "symbolic input")

    def test_negative_and_adversarial_mutations(self) -> None:
        for case in self.mutation_cases:
            with self.subTest(case=case["id"]):
                mutated = copy.deepcopy(self.bundle)
                apply_mutation(mutated, case)
                issues = self.module.validate_bundle(
                    mutated,
                    f"<mutation:{case['id']}>",
                    self.definitions,
                    copy.deepcopy(self.entities),
                    copy.deepcopy(self.attributes),
                )
                codes = {issue.code for issue in issues}
                self.assertIn(
                    case["expected_code"],
                    codes,
                    "\n".join(issue.render() for issue in issues),
                )

    def test_error_output_is_deterministic(self) -> None:
        mutated = copy.deepcopy(self.bundle)
        mutated["readiness"]["runtime_ready"] = True
        mutated["production"] = True
        first = [
            issue.render()
            for issue in self.module.validate_bundle(
                mutated,
                "<determinism>",
                self.definitions,
                self.entities,
                self.attributes,
            )
        ]
        second = [
            issue.render()
            for issue in self.module.validate_bundle(
                mutated,
                "<determinism>",
                self.definitions,
                self.entities,
                self.attributes,
            )
        ]
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main(verbosity=2)
