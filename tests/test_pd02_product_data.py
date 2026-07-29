#!/usr/bin/env python3
"""Positive, negative, and adversarial tests for PD-02A foundations."""

from __future__ import annotations

import copy
import importlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
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
MEASURED_ATTRIBUTES = ROOT / "tests/fixtures/product-attributes/valid-measured-attribute.yaml"
ENTITIES = ROOT / "tests/fixtures/product-core/valid-minimal.yaml"
VALID_VALUES = FIXTURES / "valid-synthetic-controlled-values.yaml"
VALID_PROFILE = FIXTURES / "valid-synthetic-profile.yaml"
MUTATIONS = FIXTURES / "mutation-cases.json"


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
    elif operation == "alias_equals_code":
        entry["values"][0]["aliases"] = [entry["values"][0]["value_code"]]
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
        cls.measured_attributes, _ = cls.values_module.load_yaml(
            MEASURED_ATTRIBUTES, "synthetic measured attributes"
        )
        cls.entities, _ = cls.values_module.load_yaml(ENTITIES, "synthetic Product Core")
        (
            cls.attribute_map,
            cls.value_registry_map,
            cls.dependency_issues,
        ) = cls.profiles_module.registry_maps(
            cls.attributes,
            cls.values,
            cls.value_definitions,
        )
        cls.scope_definitions, cls.scope_issues = (
            cls.profiles_module.validated_scope_entities(cls.entities)
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
            scope_entities=self.scope_definitions,
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
        self.assertEqual(self.scope_issues, [])
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
        result = subprocess.run(
            [
                sys.executable,
                "-c",
                (
                    "import sys;"
                    f"sys.path.insert(0, {str(VALIDATION_DIR)!r});"
                    "import validate_product_attribute_values;"
                    "import validate_product_attribute_profiles"
                ),
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        after = {path: path.stat().st_mtime_ns for path in (CANONICAL_VALUES, CANONICAL_PROFILES)}
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")
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

    def test_negative_value_registry_attribute_and_alias_reconciliation(self) -> None:
        wrong_type = copy.deepcopy(self.values)
        wrong_type["synthetic_attribute_dependencies"][0]["data_type"] = "TEXT"
        issues = self.value_issues(wrong_type)
        self.assertTrue(
            any(issue.code == "ATTRIBUTE_TYPE_MISMATCH" for issue in issues),
            [issue.render() for issue in issues],
        )
        alias_collision = copy.deepcopy(self.values)
        term = alias_collision["value_registries"][0]["values"][0]
        term["aliases"] = [term["value_code"]]
        issues = self.value_issues(alias_collision)
        self.assertTrue(
            any(issue.code == "DUPLICATE_NORMALIZED_TERM" for issue in issues),
            [issue.render() for issue in issues],
        )

    def test_negative_profile_cannot_weaken_attribute_policy(self) -> None:
        measured_map = {
            self.measured_attributes[0]["attribute_id"]: self.measured_attributes[0]
        }
        weakened = copy.deepcopy(self.profiles)
        rule = weakened["profiles"][0]["attribute_rules"][0]
        rule["attribute_id"] = "attr:000000000002"
        rule["allowed_unit_ids"] = []
        rule["precision"] = 12
        issues = self.profiles_module.validate_registry(
            weakened,
            "<weakened-profile>",
            self.profile_definitions,
            canonical=False,
            attributes=measured_map,
            value_registries={},
            scope_entities=self.scope_definitions,
        )
        codes = {issue.code for issue in issues}
        self.assertIn("REQUIRED_UNITS_EMPTY", codes)
        self.assertIn("PRECISION_WEAKENS_ATTRIBUTE", codes)

        controlled_attribute = self.values["synthetic_attribute_dependencies"][0]
        controlled = copy.deepcopy(self.profiles)
        controlled_rule = controlled["profiles"][0]["attribute_rules"][0]
        controlled_rule["attribute_id"] = controlled_attribute["attribute_id"]
        controlled_rule["value_source"] = "CONTROLLED_REGISTRY"
        controlled_rule["value_registry_id"] = "vreg:000000000099"
        fake_registry = {
            "vreg:000000000099": {
                "value_registry_id": "vreg:000000000099",
                "attribute_id": controlled_attribute["attribute_id"],
            }
        }
        issues = self.profiles_module.validate_registry(
            controlled,
            "<registry-policy-profile>",
            self.profile_definitions,
            canonical=False,
            attributes={controlled_attribute["attribute_id"]: controlled_attribute},
            value_registries=fake_registry,
            scope_entities=self.scope_definitions,
        )
        self.assertTrue(
            any(issue.code == "ATTRIBUTE_REGISTRY_POLICY" for issue in issues),
            [issue.render() for issue in issues],
        )

    def test_adversarial_scope_cli_cannot_assert_unvalidated_identity(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(PROFILE_VALIDATOR),
                str(VALID_PROFILE),
                "--synthetic-scope-id",
                "prd:family:ffffffffffff",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unrecognized arguments", result.stderr)

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
