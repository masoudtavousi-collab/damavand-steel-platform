from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import socket
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_DIR = ROOT / "repository/data/validation"
VALIDATOR_PATH = VALIDATION_DIR / "validate_founder_product_commerce_checkpoint03.py"
sys.path.insert(0, str(VALIDATION_DIR))
SPEC = importlib.util.spec_from_file_location("validate_founder_product_commerce_checkpoint03", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class Checkpoint03ValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema_validator, cls.contract = MODULE.load_validator()
        cls.canonical = MODULE.load_yaml(MODULE.REGISTRY_PATH)
        manifest_path = ROOT / "tests/fixtures/c003r1-checkpoint03/mutation-cases.json"
        cls.mutations = json.loads(manifest_path.read_text(encoding="utf-8"))

    def validate(self, value):
        return MODULE.validate_registry(value, self.schema_validator, self.contract)

    def test_canonical_package_passes_and_is_deterministic(self):
        before = MODULE.semantic_digest(self.canonical)
        with patch.object(socket, "socket", side_effect=AssertionError("network forbidden")):
            first = self.validate(copy.deepcopy(self.canonical))
            second = self.validate(copy.deepcopy(self.canonical))
        self.assertEqual(first, [])
        self.assertEqual(first, second)
        self.assertEqual(before, MODULE.semantic_digest(MODULE.load_yaml(MODULE.REGISTRY_PATH)))

    def test_all_counted_mutations_fail_closed(self):
        self.assertEqual(len(self.mutations), 40)
        self.assertEqual(len({item["name"] for item in self.mutations}), 40)
        for case in self.mutations:
            with self.subTest(case=case["name"]):
                value = copy.deepcopy(self.canonical)
                target = value
                for part in case["path"][:-1]:
                    target = target[part]
                final = case["path"][-1]
                operation = case["operation"]
                if operation == "replace":
                    target[final] = case["value"]
                elif operation == "add":
                    target[final] = case["value"]
                elif operation == "delete":
                    del target[final]
                elif operation == "append":
                    target[final].append(case["value"])
                elif operation == "pop":
                    target[final].pop()
                else:
                    self.fail(f"unknown operation: {operation}")
                rendered = "\n".join(self.validate(value))
                self.assertIn(case["expected"], rendered)

    def test_duplicate_yaml_keys_fail_closed(self):
        path = ROOT / "tests/fixtures/c003r1-checkpoint03/adversarial-duplicate-keys.yaml"
        with self.assertRaises(Exception):
            MODULE.load_yaml(path)

    def test_remote_and_nested_permissive_schemas_fail_closed(self):
        remote = MODULE.load_json(ROOT / "tests/fixtures/c003r1-checkpoint03/adversarial-remote-ref-schema.json")
        permissive = MODULE.load_json(ROOT / "tests/fixtures/c003r1-checkpoint03/adversarial-permissive-schema.json")
        self.assertTrue(any("REMOTE_SCHEMA_REF" in issue for issue in MODULE.audit_schema(remote)))
        self.assertTrue(any("PERMISSIVE_SCHEMA" in issue for issue in MODULE.audit_schema(permissive)))

    def test_nonfinite_and_deep_inputs_fail_closed(self):
        nonfinite = copy.deepcopy(self.canonical)
        nonfinite["pilot_readiness_packet"]["diameter_mm"] = float("nan")
        self.assertTrue(any("NON_FINITE" in issue for issue in self.validate(nonfinite)))
        deep = copy.deepcopy(self.canonical)
        nested = {}
        cursor = nested
        for _ in range(90):
            cursor["nested"] = {}
            cursor = cursor["nested"]
        deep["unexpected"] = nested
        self.assertTrue(any("INPUT_DEPTH" in issue for issue in self.validate(deep)))

    def test_path_escape_and_symlink_fail_closed(self):
        with self.assertRaises(MODULE.ValidationConfigurationError):
            MODULE.safe_path(Path("/etc/passwd"), "escape")
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as temp_dir:
            link = Path(temp_dir) / "link.yaml"
            link.symlink_to(MODULE.REGISTRY_PATH)
            with self.assertRaises(MODULE.ValidationConfigurationError):
                MODULE.safe_path(link, "symlink")

    def test_classification_and_temporal_role_are_independent(self):
        records = self.canonical["evidence_delta"]
        self.assertTrue(any(item["ledger_class"] == "HE" for item in records))
        self.assertTrue(any(item["ledger_class"] == "FCF" for item in records))
        self.assertFalse(any(item["evidence_classification"] == "FOUNDER_ACCEPTED_CANDIDATE" for item in records))
        value_bank = next(item for item in records if item["decision_code"] == "C003R1-CP03-024")
        self.assertEqual(value_bank["evidence_classification"], "FOUNDER_CONFIRMED")
        self.assertEqual(value_bank["disposition"], "CANDIDATE_VALUE_BANK_ONLY")
        self.assertTrue(any(item["ledger_class"] == "AP" for item in records))

    def test_no_cartesian_tuple_or_mass_population_exists(self):
        packet = self.canonical["pilot_readiness_packet"]
        self.assertEqual(packet["combination_evidence"]["evidence_backed_valid_tuples"], [])
        self.assertFalse(packet["combination_evidence"]["cartesian_generation"])
        self.assertEqual(packet["mass_observation_policy"]["observations"], [])
        self.assertFalse(packet["mass_observation_policy"]["variant_identity"])

    def test_no_go_and_c002_regression_anchors_are_live(self):
        self.assertEqual(self.canonical["pilot_readiness_packet"]["c002_readiness"]["coverage"], "0/9")
        self.assertEqual(MODULE.load_yaml(MODULE.C002_CANDIDATE_PATH)["candidates"], [])
        admin = MODULE.load_yaml(MODULE.C002_ADMIN_PATH)
        self.assertEqual(len(admin["policies"]), 8)
        self.assertEqual(admin["instances"], [])
        self.assertEqual(self.canonical["pilot_readiness_packet"]["selection_effects"]["commerce_state"], "INQUIRY_ONLY")


if __name__ == "__main__":
    unittest.main()
