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
VALIDATOR_PATH = ROOT / "repository/data/validation/validate_c008_c002_readiness_evidence_closure.py"
VALIDATION_DIR = VALIDATOR_PATH.parent
import sys
sys.path.insert(0, str(VALIDATION_DIR))
SPEC = importlib.util.spec_from_file_location("validate_c008_c002_readiness_evidence_closure", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
ORIGINAL_CONTRACT_DIGEST = MODULE.EXPECTED_CONTRACT_DIGEST
ORIGINAL_SCHEMA_DIGEST = MODULE.EXPECTED_SCHEMA_DIGEST
ORIGINAL_REGISTRY_DIGEST = MODULE.EXPECTED_REGISTRY_DIGEST
ORIGINAL_SYNTHETIC_REGISTRY_DIGEST = MODULE.EXPECTED_SYNTHETIC_REGISTRY_DIGEST


class C008C002ReadinessEvidenceClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = MODULE.require_mapping(MODULE.load_yaml(MODULE.CONTRACT_PATH), "C008 contract")
        cls.schema = MODULE.require_mapping(MODULE.load_json(MODULE.SCHEMA_PATH), "C008 schema")
        cls.canonical = MODULE.require_mapping(MODULE.load_yaml(MODULE.REGISTRY_PATH), "C008 registry")
        cls.synthetic = MODULE.require_mapping(
            MODULE.load_yaml(ROOT / "tests/fixtures/c008-c002-readiness-evidence-closure/valid-synthetic.yaml"),
            "C008 synthetic registry",
        )
        if MODULE.EXPECTED_CONTRACT_DIGEST == "TO_BE_FINALIZED":
            MODULE.EXPECTED_CONTRACT_DIGEST = MODULE.semantic_digest(cls.contract)
        if MODULE.EXPECTED_SCHEMA_DIGEST == "TO_BE_FINALIZED":
            MODULE.EXPECTED_SCHEMA_DIGEST = MODULE.semantic_digest(cls.schema)
        if MODULE.EXPECTED_REGISTRY_DIGEST == "TO_BE_FINALIZED":
            MODULE.EXPECTED_REGISTRY_DIGEST = MODULE.semantic_digest(cls.canonical)
        if MODULE.EXPECTED_SYNTHETIC_REGISTRY_DIGEST == "TO_BE_FINALIZED":
            MODULE.EXPECTED_SYNTHETIC_REGISTRY_DIGEST = MODULE.semantic_digest(cls.synthetic)
        cls.schema_validator, cls.loaded_contract = MODULE.load_validator()
        cls.mutations = json.loads(
            (ROOT / "tests/fixtures/c008-c002-readiness-evidence-closure/mutation-cases.json").read_text(encoding="utf-8")
        )

    def validate(self, value, *, synthetic_mode=False):
        return MODULE.validate_registry(
            value,
            self.schema_validator,
            self.loaded_contract,
            synthetic_mode=synthetic_mode,
        )

    def test_canonical_package_passes_deterministically_without_network(self):
        before = MODULE.semantic_digest(self.canonical)
        with patch.object(socket, "socket", side_effect=AssertionError("network forbidden")):
            first = self.validate(copy.deepcopy(self.canonical))
            second = self.validate(copy.deepcopy(self.canonical))
        self.assertEqual(first, [])
        self.assertEqual(first, second)
        self.assertEqual(before, MODULE.semantic_digest(MODULE.load_yaml(MODULE.REGISTRY_PATH)))

    def test_distinct_synthetic_positive_surface_passes_only_in_synthetic_mode(self):
        self.assertNotEqual(MODULE.semantic_digest(self.synthetic), MODULE.semantic_digest(self.canonical))
        self.assertEqual(self.synthetic["fixture_mode"], "SYNTHETIC")
        self.assertIn("FIXTURE_MODE", "\n".join(self.validate(copy.deepcopy(self.synthetic))))
        self.assertEqual(self.validate(copy.deepcopy(self.synthetic), synthetic_mode=True), [])

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

    def test_duplicate_yaml_and_json_keys_fail_closed(self):
        fixture_dir = ROOT / "tests/fixtures/c008-c002-readiness-evidence-closure"
        with self.assertRaises(Exception):
            MODULE.load_yaml(fixture_dir / "adversarial-duplicate-keys.yaml")
        with self.assertRaises(Exception):
            MODULE.load_json(fixture_dir / "adversarial-duplicate-keys.json")

    def test_remote_and_nested_permissive_schemas_fail_closed(self):
        fixture_dir = ROOT / "tests/fixtures/c008-c002-readiness-evidence-closure"
        for name, expected in [
            ("adversarial-remote-ref-schema.json", "REMOTE_SCHEMA_REF"),
            ("adversarial-permissive-schema.json", "PERMISSIVE_SCHEMA"),
        ]:
            with self.subTest(name=name):
                issues = MODULE.audit_schema(MODULE.load_json(fixture_dir / name))
                self.assertIn(expected, "\n".join(issues))

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

    def test_depth_node_and_nonfinite_inputs_fail_closed(self):
        deep = {}
        cursor = deep
        for index in range(105):
            cursor[str(index)] = {}
            cursor = cursor[str(index)]
        self.assertIn("INPUT_DEPTH", "\n".join(MODULE.audit_value(deep)))
        value = copy.deepcopy(self.canonical)
        value["readiness_result"]["resolved_count"] = float("nan")
        self.assertIn("NON_FINITE", "\n".join(self.validate(value)))

    def test_authorization_packet_and_source_manifest_are_exact(self):
        self.assertEqual(self.canonical["packet"]["packet_id"], "DS-P1-M3-PACKET-01")
        self.assertEqual(self.canonical["packet"]["packet_version"], "1.0")
        self.assertEqual(self.canonical["packet"]["packet_zip_sha256"], "4298addbde0c12cc6f4c4653ab5a33b3f6f17c69c485dd01a7581c98981591e5")
        self.assertEqual([item["source_id"] for item in self.canonical["source_manifest"]["sources"]], [f"C008-SOURCE-{index:03d}" for index in range(1, 3)])

    def test_six_immediate_reviews_and_all_nine_terminal_states_are_exact(self):
        reviews = self.canonical["criterion_reviews"]
        self.assertEqual([item["criterion_code"] for item in reviews], MODULE.EXPECTED_CRITERIA)
        self.assertEqual([item["terminal_state"] for item in reviews], MODULE.EXPECTED_TERMINAL)
        six = [item["criterion_code"] for item in reviews if item["review_lane"] in {"LANE_A_INDEPENDENT_REVIEW", "LANE_D_CONDITIONAL_SEO"}]
        self.assertEqual(six, MODULE.EXPECTED_SIX)
        self.assertEqual(self.canonical["readiness_result"], MODULE.EXPECTED_TOTALS)

    def test_g1_is_hold_not_ready_and_never_selection_or_m4_authority(self):
        g1 = self.canonical["g1_decision_surface"]
        self.assertEqual(g1["result"], "HOLD_NOT_READY_4_OF_9")
        self.assertFalse(g1["founder_selection_ready"])
        self.assertIsNone(g1["m4_promotion_candidate"])
        self.assertFalse(g1["recommendation_is_selection"])
        self.assertFalse(g1["m4_authorized"])

    def test_missing_supply_fulfillment_media_and_seo_research_gate_fail_closed(self):
        by_code = {item["criterion_code"]: item for item in self.canonical["criterion_reviews"]}
        self.assertEqual(by_code["SUPPLY_EVIDENCE"]["terminal_state"], "SUBMITTED_REVIEW_INCOMPLETE")
        self.assertEqual(by_code["FULFILLMENT_RISK"]["terminal_state"], "SUBMITTED_REVIEW_INCOMPLETE")
        self.assertEqual(by_code["PHOTO_CONTENT_READINESS"]["terminal_state"], "MISSING_EVIDENCE")
        self.assertEqual(by_code["SEO_BUYER_INTENT"]["terminal_state"], "SUBMITTED_REVIEW_INCOMPLETE")
        seo = self.canonical["evidence_items"][6]
        self.assertEqual(seo["evidence_class"], "REPOSITORY_CANONICAL_EVIDENCE")
        self.assertIn("prerequisite insufficiency trigger", " ".join(seo["unsupported_claims"]))

    def test_dependency_pins_and_predecessor_owners_fail_closed(self):
        contract = copy.deepcopy(self.loaded_contract)
        contract["base_pins"]["c005_registry_semantic_sha256"] = "0" * 64
        issues = []
        MODULE.validate_dependency_pins(lambda code, message: issues.append(f"[{code}] {message}"), contract)
        self.assertIn("DEPENDENCY_PIN_REGRESSION", "\n".join(issues))

    def test_contract_authority_readiness_and_g1_policy_fail_closed(self):
        contract = copy.deepcopy(self.loaded_contract)
        contract["authority"]["product_population_allowed"] = True
        rendered = "\n".join(MODULE.validate_registry(copy.deepcopy(self.canonical), self.schema_validator, contract))
        self.assertIn("CONTRACT_AUTHORITY", rendered)
        contract = copy.deepcopy(self.loaded_contract)
        contract["c002_readiness_policy"]["exact_terminal_vector"][0] = "SUBMITTED_REVIEW_INCOMPLETE"
        rendered = "\n".join(MODULE.validate_registry(copy.deepcopy(self.canonical), self.schema_validator, contract))
        self.assertIn("CONTRACT_READINESS", rendered)
        contract = copy.deepcopy(self.loaded_contract)
        contract["g1_policy"]["m4_authorized"] = True
        rendered = "\n".join(MODULE.validate_registry(copy.deepcopy(self.canonical), self.schema_validator, contract))
        self.assertIn("CONTRACT_G1", rendered)
        contract = copy.deepcopy(self.loaded_contract)
        contract["source_policy"]["conditional_public_research_triggered"] = True
        rendered = "\n".join(MODULE.validate_registry(copy.deepcopy(self.canonical), self.schema_validator, contract))
        self.assertIn("CONTRACT_SOURCE_POLICY", rendered)

    def test_semantic_digests_are_fail_closed_and_fully_pinned(self):
        self.assertNotEqual(ORIGINAL_CONTRACT_DIGEST, "TO_BE_FINALIZED")
        self.assertNotEqual(ORIGINAL_SCHEMA_DIGEST, "TO_BE_FINALIZED")
        self.assertNotEqual(ORIGINAL_REGISTRY_DIGEST, "TO_BE_FINALIZED")
        self.assertNotEqual(ORIGINAL_SYNTHETIC_REGISTRY_DIGEST, "TO_BE_FINALIZED")
        self.assertEqual(MODULE.semantic_digest(self.contract), ORIGINAL_CONTRACT_DIGEST)
        self.assertEqual(MODULE.semantic_digest(self.schema), ORIGINAL_SCHEMA_DIGEST)
        self.assertEqual(MODULE.semantic_digest(self.canonical), ORIGINAL_REGISTRY_DIGEST)
        self.assertEqual(MODULE.semantic_digest(self.synthetic), ORIGINAL_SYNTHETIC_REGISTRY_DIGEST)


if __name__ == "__main__":
    unittest.main()
