from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import socket
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "repository/data/validation/validate_c005_founder_evidence_readiness.py"
VALIDATION_DIR = VALIDATOR_PATH.parent
import sys
sys.path.insert(0, str(VALIDATION_DIR))
SPEC = importlib.util.spec_from_file_location("validate_c005_founder_evidence_readiness", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class C005FounderEvidenceReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema_validator, cls.contract = MODULE.load_validator()
        cls.canonical = MODULE.load_yaml(MODULE.REGISTRY_PATH)
        cls.mutations = json.loads(
            (ROOT / "tests/fixtures/c005-founder-evidence-readiness/mutation-cases.json").read_text(encoding="utf-8")
        )

    def validate(self, value):
        return MODULE.validate_registry(value, self.schema_validator, self.contract)

    def test_canonical_package_passes_deterministically_without_network(self):
        before = MODULE.semantic_digest(self.canonical)
        with patch.object(socket, "socket", side_effect=AssertionError("network forbidden")):
            first = self.validate(copy.deepcopy(self.canonical))
            second = self.validate(copy.deepcopy(self.canonical))
        self.assertEqual(first, [])
        self.assertEqual(first, second)
        self.assertEqual(before, MODULE.semantic_digest(MODULE.load_yaml(MODULE.REGISTRY_PATH)))

    def test_all_counted_mutations_fail_closed_with_specific_codes(self):
        self.assertEqual(len(self.mutations), 66)
        self.assertEqual(len({case["name"] for case in self.mutations}), 66)
        for case in self.mutations:
            with self.subTest(case=case["name"]):
                value = copy.deepcopy(self.canonical)
                target = value
                for part in case["path"][:-1]:
                    target = target[part]
                final = case["path"][-1]
                operation = case["operation"]
                if operation in {"replace", "add"}:
                    target[final] = case["value"]
                elif operation == "append":
                    target[final].append(case["value"])
                elif operation == "delete":
                    del target[final]
                else:
                    self.fail(f"unknown mutation operation: {operation}")
                rendered = "\n".join(self.validate(value))
                self.assertIn(case["expected"], rendered)

    def test_duplicate_yaml_keys_fail_closed(self):
        path = ROOT / "tests/fixtures/c005-founder-evidence-readiness/adversarial-duplicate-keys.yaml"
        with self.assertRaises(Exception):
            MODULE.load_yaml(path)

    def test_duplicate_json_schema_keys_fail_closed(self):
        path = ROOT / "tests/fixtures/c005-founder-evidence-readiness/adversarial-duplicate-keys.json"
        with self.assertRaises(Exception):
            MODULE.load_validator(schema_path=path)

    def test_remote_and_nested_permissive_schemas_fail_closed(self):
        fixture_dir = ROOT / "tests/fixtures/c005-founder-evidence-readiness"
        for name, expected in [
            ("adversarial-remote-ref-schema.json", "REMOTE_SCHEMA_REF"),
            ("adversarial-permissive-schema.json", "PERMISSIVE_SCHEMA"),
        ]:
            with self.subTest(name=name):
                with self.assertRaisesRegex(Exception, expected):
                    MODULE.load_validator(schema_path=fixture_dir / name)

    def test_path_escape_symlink_and_byte_cap_fail_closed(self):
        with tempfile.NamedTemporaryFile() as outside:
            with self.assertRaisesRegex(Exception, "inside the repository"):
                MODULE.safe_path(Path(outside.name), "outside fixture")
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as temp_dir:
            link = Path(temp_dir) / "registry-link.yaml"
            link.symlink_to(MODULE.REGISTRY_PATH)
            with self.assertRaisesRegex(Exception, "symbolic link"):
                MODULE.safe_path(link, "symlink fixture")
        with tempfile.NamedTemporaryFile(dir=ROOT / "tests", delete=False) as oversized:
            oversized.write(b"x" * 2_000_001)
            oversized_path = Path(oversized.name)
        try:
            with self.assertRaisesRegex(Exception, "2 MB byte cap"):
                MODULE.safe_path(oversized_path, "oversized fixture")
        finally:
            oversized_path.unlink(missing_ok=True)

    def test_depth_and_nonfinite_inputs_fail_closed(self):
        deep_value = {}
        cursor = deep_value
        for index in range(105):
            cursor[str(index)] = {}
            cursor = cursor[str(index)]
        self.assertIn("INPUT_DEPTH", "\n".join(MODULE.audit_value(deep_value)))
        value = copy.deepcopy(self.canonical)
        value["classification_summary"]["total_record_count"] = float("nan")
        self.assertIn("NON_FINITE", "\n".join(self.validate(value)))

    def test_slack_source_and_evidence_classification_are_exact(self):
        manifest = self.canonical["source_manifest"]
        self.assertEqual([item["source_id"] for item in manifest["sources"]], MODULE.EXPECTED_SOURCE_IDS)
        self.assertEqual([item["message_ts"] for item in manifest["sources"]], MODULE.EXPECTED_SOURCE_TS)
        self.assertTrue(all(item["thread_complete"] and item["reply_count"] == 0 for item in manifest["sources"]))
        records = self.canonical["evidence_records"]
        self.assertEqual([item["evidence_classification"] for item in records], MODULE.EXPECTED_CLASSIFICATIONS)
        self.assertEqual([item["temporal_role"] for item in records], MODULE.EXPECTED_TEMPORAL)

    def test_all_nine_criteria_are_reevaluated_without_false_resolution(self):
        readiness = self.canonical["c002_readiness_reevaluation"]
        self.assertEqual([item["criterion_code"] for item in readiness["criteria"]], MODULE.EXPECTED_CRITERIA)
        self.assertEqual([item["evidence_state"] for item in readiness["criteria"]], MODULE.EXPECTED_NEW_STATES)
        self.assertEqual([item["reviewable"] for item in readiness["criteria"]], MODULE.EXPECTED_REVIEWABLE)
        self.assertEqual(readiness["totals"], MODULE.EXPECTED_TOTALS)
        self.assertEqual(readiness["readiness"], "NOT_READY")
        self.assertEqual(readiness["candidate_registry_count"], 0)
        self.assertTrue(all(item["status"] == "OPEN_BLOCKING" for item in readiness["criteria"]))

    def test_mass_supply_pricing_vip_and_order_remain_evidence_only(self):
        mass = self.canonical["mass_and_supply_reconciliation"]
        commercial = self.canonical["commercial_requirements_reconciliation"]
        self.assertEqual(mass["current_numeric_mass_observation_count"], 0)
        self.assertEqual(mass["current_supply_intake_record_count"], 0)
        self.assertFalse(mass["supplier_stated_method_extension_allowed"])
        self.assertEqual(mass["approved_c002_mass_methods"], ["MANUFACTURER_STATED", "MEASURED", "CALCULATED"])
        self.assertEqual(commercial["current_price_value_count"], 0)
        self.assertEqual(commercial["customer_object_count"], 0)
        self.assertEqual(commercial["order_object_count"], 0)
        self.assertEqual(commercial["active_vip_entitlement_count"], 0)
        self.assertEqual(commercial["active_loyalty_ledger_count"], 0)
        self.assertFalse(commercial["implementation_created"])

    def test_direct_c003_and_c003_r1_dependency_pins_fail_closed(self):
        contract = copy.deepcopy(self.contract)
        contract["base_pins"]["c003_base_registry_semantic_sha256"] = "0" * 64
        issues = []
        MODULE.validate_dependency_pins(lambda code, message: issues.append(f"[{code}] {message}"), contract)
        self.assertIn("BASE_PIN_REGRESSION", "\n".join(issues))

    def test_semantic_digests_are_fail_closed_and_fully_pinned(self):
        self.assertNotEqual(MODULE.EXPECTED_CONTRACT_DIGEST, "TO_BE_FINALIZED")
        self.assertNotEqual(MODULE.EXPECTED_SCHEMA_DIGEST, "TO_BE_FINALIZED")
        self.assertNotEqual(MODULE.EXPECTED_REGISTRY_DIGEST, "TO_BE_FINALIZED")
        self.assertEqual(MODULE.semantic_digest(self.contract), MODULE.EXPECTED_CONTRACT_DIGEST)
        self.assertEqual(MODULE.semantic_digest(MODULE.load_json(MODULE.SCHEMA_PATH)), MODULE.EXPECTED_SCHEMA_DIGEST)
        self.assertEqual(MODULE.semantic_digest(self.canonical), MODULE.EXPECTED_REGISTRY_DIGEST)


if __name__ == "__main__":
    unittest.main()
