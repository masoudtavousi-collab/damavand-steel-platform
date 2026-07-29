#!/usr/bin/env python3
"""Positive, negative, and adversarial tests for PD-02A foundations."""

from __future__ import annotations

import copy
import importlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_DIR = ROOT / "repository/data/validation"
FIXTURES = ROOT / "tests/fixtures/pd02"
VALUE_VALIDATOR = VALIDATION_DIR / "validate_product_attribute_values.py"
PROFILE_VALIDATOR = VALIDATION_DIR / "validate_product_attribute_profiles.py"
VALUE_CONTRACT = (
    ROOT / "repository/data/contracts/product-attribute-value-registry.contract.yaml"
)
PROFILE_CONTRACT = ROOT / "repository/data/contracts/product-attribute-profile.contract.yaml"
VALUE_SCHEMA = (
    ROOT / "repository/data/schemas/product-attribute-value-registry.schema.json"
)
PROFILE_SCHEMA = ROOT / "repository/data/schemas/product-attribute-profile.schema.json"
CANONICAL_VALUES = (
    ROOT / "repository/data/registries/product-attribute-value-registries.yaml"
)
CANONICAL_PROFILES = (
    ROOT / "repository/data/registries/product-attribute-profiles.yaml"
)
ATTRIBUTES = ROOT / "tests/fixtures/product-attributes/valid-foundation.yaml"
VALID_VALUES = FIXTURES / "valid-synthetic-controlled-values.yaml"
VALID_PROFILE = FIXTURES / "valid-synthetic-profile.yaml"
MUTATIONS = FIXTURES / "mutation-cases.json"
SCOPE = {"prd:family:000000000001": "FAMILY"}


def import_modules() -> tuple[object, object]:
    sys.path.insert(0, str(VALIDATION_DIR))
    try:
        values = importlib.import_module("validate_product_attribute_values")
        profiles = importlib.import_module("validate_product_attribute_profiles")
        return values, profiles
    finally:
        sys.path.remove(str(VALIDATION_DIR))


def apply_mutation(document: dict, case: dict) -> None:
    entries_key = "value_registries" if case["document"] == "values" else "profiles"
    entry = document[entries_key][0]
    operation = case["operation"]
    if operation == "inject_prohibited":
        entry[case["field"]] = "synthetic-forbidden"
    elif operation == "delete_entry_field":
        del entry[case["field"]]
    elif operation == "promote_status":
        entry["status"] = "APPROVED"
    elif operation == "same_roles":
        entry["reviewer"] = copy.deepcopy(entry["owner"])
    elif operation == "invalid_classification":
        document["data_classification"] = "CANONICAL_EMPTY"
    elif operation == "duplicate_term":
        entry["values"].append(copy.deepcopy(entry["values"][0]))
    elif operation == "unknown_envelope":
        document["unexpected"] = True
    elif operation == "unknown_scope":
        entry["scope_entity_id"] = "prd:family:ffffffffffff"
    elif operation == "unknown_attribute":
        entry["attribute_rules"][0]["attribute_id"] = "attr:ffffffffffff"
    elif operation == "unresolved_registry":
        rule = entry["attribute_rules"][0]
        rule["value_source"] = "CONTROLLED_REGISTRY"
        rule["value_registry_id"] = "vreg:ffffffffffff"
    elif operation == "prohibited_behavior":
        rule = entry["attribute_rules"][0]
        rule["requirement_level"] = "PROHIBITED"
        rule["variation_axis"] = True
    else:
        raise AssertionError(f"unknown mutation operation: {operation}")


class PD02AProductDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.values_module, cls.profiles_module = import_modules()
        cls.value_definitions = cls.values_module.load_definitions()
        cls.profile_definitions = cls.profiles_module.load_definitions()
        cls.values, _ = cls.values_module.load_yaml(VALID_VALUES, "valid PD-02A values")
        cls.profiles, _ = cls.values_module.load_yaml(VALID_PROFILE, "valid PD-02A profiles")
        cls.attributes, _ = cls.values_module.load_yaml(ATTRIBUTES, "synthetic attributes")
        (
            cls.attribute_map,
            cls.value_registry_map,
            cls.dependency_issues,
        ) = cls.profiles_module.registry_maps(
            cls.attributes,
            cls.values,
            cls.value_definitions,
        )
        cls.mutations = json.loads(MUTATIONS.read_text(encoding="utf-8"))

    def value_issues(self, document: dict) -> list:
        return self.values_module.validate_registry(
            document,
            "<test-values>",
            self.value_definitions,
            canonical=False,
        )

    def profile_issues(self, document: dict) -> list:
        return self.profiles_module.validate_registry(
            document,
            "<test-profiles>",
            self.profile_definitions,
            canonical=False,
            attributes=self.attribute_map,
            value_registries=self.value_registry_map,
            scope_entities=SCOPE,
        )

    def test_positive_canonical_registries_are_empty(self) -> None:
        values, _ = self.values_module.load_yaml(CANONICAL_VALUES, "canonical values")
        profiles, _ = self.values_module.load_yaml(CANONICAL_PROFILES, "canonical profiles")
        self.assertEqual(values["value_registries"], [])
        self.assertEqual(profiles["profiles"], [])
        self.assertEqual(
            self.values_module.validate_registry(
                values, "<canonical-values>", self.value_definitions, canonical=True
            ),
            [],
        )
        self.assertEqual(
            self.profiles_module.validate_registry(
                profiles, "<canonical-profiles>", self.profile_definitions, canonical=True
            ),
            [],
        )

    def test_positive_synthetic_fixtures(self) -> None:
        self.assertEqual(self.dependency_issues, [])
        self.assertEqual(self.value_issues(copy.deepcopy(self.values)), [])
        self.assertEqual(self.profile_issues(copy.deepcopy(self.profiles)), [])

    def test_positive_cli_default_and_explicit_paths(self) -> None:
        commands = [
            [sys.executable, str(VALUE_VALIDATOR)],
            [sys.executable, str(PROFILE_VALIDATOR)],
            [sys.executable, str(VALUE_VALIDATOR), str(VALID_VALUES)],
            [sys.executable, str(PROFILE_VALIDATOR), str(VALID_PROFILE)],
        ]
        for command in commands:
            with self.subTest(command=command):
                result = subprocess.run(
                    command, cwd=ROOT, text=True, capture_output=True, check=False
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("PASS", result.stdout)

    def test_positive_validation_has_no_network(self) -> None:
        with patch("socket.socket", side_effect=AssertionError("network forbidden")):
            self.assertEqual(self.value_issues(copy.deepcopy(self.values)), [])
            self.assertEqual(self.profile_issues(copy.deepcopy(self.profiles)), [])

    def test_positive_import_has_no_output_or_side_effect(self) -> None:
        before = {path: path.stat().st_mtime_ns for path in (CANONICAL_VALUES, CANONICAL_PROFILES)}
        out = io.StringIO()
        err = io.StringIO()
        sys.path.insert(0, str(VALIDATION_DIR))
        try:
            with redirect_stdout(out), redirect_stderr(err):
                importlib.reload(self.values_module)
                importlib.reload(self.profiles_module)
        finally:
            sys.path.remove(str(VALIDATION_DIR))
        after = {path: path.stat().st_mtime_ns for path in (CANONICAL_VALUES, CANONICAL_PROFILES)}
        self.assertEqual(out.getvalue(), "")
        self.assertEqual(err.getvalue(), "")
        self.assertEqual(before, after)

    def test_negative_named_fixtures(self) -> None:
        cases = [
            ("invalid-unresolved-registry.yaml", "UNRESOLVED_VALUE_REGISTRY"),
            ("invalid-orphan-profile.yaml", "ORPHAN_PROFILE_SCOPE"),
            ("invalid-term-attribute-mismatch.yaml", "VALUE_SOURCE_TYPE"),
            ("invalid-status-promotion.yaml", "SYNTHETIC_STATUS"),
        ]
        for filename, code in cases:
            document, _ = self.values_module.load_yaml(FIXTURES / filename, filename)
            issues = self.profile_issues(document)
            self.assertTrue(any(issue.code == code for issue in issues), [i.render() for i in issues])
        duplicate, _ = self.values_module.load_yaml(
            FIXTURES / "invalid-duplicate-normalized-term.yaml",
            "invalid normalized term",
        )
        duplicate_issues = self.value_issues(duplicate)
        self.assertTrue(
            any(issue.code == "DUPLICATE_NORMALIZED_TERM" for issue in duplicate_issues)
        )

    def test_negative_direct_draft_to_approved_is_rejected(self) -> None:
        for contract_path, module in (
            (VALUE_CONTRACT, self.values_module),
            (PROFILE_CONTRACT, self.profiles_module),
        ):
            contract, _ = self.values_module.load_yaml(contract_path, "PD-02A contract")
            contract["pd02a_lifecycle"]["current_status"] = "APPROVED"
            contract["pd02a_lifecycle"]["transition_history"] = [
                {
                    "from": "DRAFT",
                    "to": "APPROVED",
                    "evidence_reference": "FORGED",
                }
            ]
            with self.assertRaises(self.values_module.DefinitionError):
                module.validate_lifecycle(contract)

    def test_negative_duplicate_yaml_and_json_keys(self) -> None:
        with self.assertRaises(self.values_module.DefinitionError):
            self.values_module.parse_yaml("a: 1\na: 2\n", "duplicate YAML")
        with self.assertRaises(self.values_module.DefinitionError):
            self.values_module.parse_json('{"a": 1, "a": 2}', "duplicate JSON")
        with self.assertRaises(self.values_module.DefinitionError):
            self.values_module.parse_json('{"a": NaN}', "non-finite JSON")

    def test_adversarial_schemas_are_rejected(self) -> None:
        with self.assertRaises(self.values_module.DefinitionError):
            self.values_module.load_definitions(
                VALUE_CONTRACT, FIXTURES / "adversarial-permissive-schema.json"
            )
        with self.assertRaises(self.values_module.DefinitionError):
            self.values_module.load_definitions(
                VALUE_CONTRACT, FIXTURES / "adversarial-remote-ref-schema.json"
            )

    def test_adversarial_path_escape_and_symlink_are_rejected(self) -> None:
        with self.assertRaises(self.values_module.DefinitionError):
            self.values_module.load_yaml(Path("/etc/hosts"), "escaped path")
        with tempfile.TemporaryDirectory(prefix="pd02a-symlink-") as directory:
            symlink = Path(directory) / "values.yaml"
            symlink.symlink_to(VALID_VALUES)
            with self.assertRaises(self.values_module.DefinitionError):
                self.values_module.load_yaml(symlink, "symbolic input")

    def test_negative_and_adversarial_mutation_depth(self) -> None:
        ids = [case["id"] for case in self.mutations]
        self.assertGreaterEqual(len(ids), 60)
        self.assertEqual(len(ids), len(set(ids)))
        for case in self.mutations:
            with self.subTest(case=case["id"]):
                source = self.values if case["document"] == "values" else self.profiles
                mutated = copy.deepcopy(source)
                apply_mutation(mutated, case)
                issues = (
                    self.value_issues(mutated)
                    if case["document"] == "values"
                    else self.profile_issues(mutated)
                )
                self.assertTrue(issues, case["id"])

    def test_error_output_is_deterministic(self) -> None:
        mutated = copy.deepcopy(self.profiles)
        mutated["profiles"][0]["scope_entity_id"] = "prd:family:ffffffffffff"
        first = [issue.render() for issue in self.profile_issues(mutated)]
        second = [issue.render() for issue in self.profile_issues(copy.deepcopy(mutated))]
        self.assertEqual(first, second)
        self.assertEqual(first, sorted(first))

    def test_fixture_boundary_contains_no_real_product_data(self) -> None:
        combined = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (
                VALID_VALUES,
                VALID_PROFILE,
                FIXTURES / "mutation-cases.json",
            )
        )
        for forbidden in (
            "GOLD-PIPE",
            "PIPE-COMB",
            "لوله استیل دکوراتیو",
            "woocommerce_id:",
            "availability:",
            "sku:",
        ):
            self.assertNotIn(forbidden, combined)


if __name__ == "__main__":
    unittest.main(verbosity=2)
