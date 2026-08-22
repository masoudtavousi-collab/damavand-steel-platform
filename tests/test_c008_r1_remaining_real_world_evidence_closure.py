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
VALIDATOR_PATH = ROOT / "repository/data/validation/validate_c008_r1_remaining_real_world_evidence_closure.py"
sys.path.insert(0, str(VALIDATOR_PATH.parent))
SPEC = importlib.util.spec_from_file_location("validate_c008_r1_remaining_real_world_evidence_closure", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
ORIGINAL_DIGESTS = [
    MODULE.EXPECTED_CONTRACT_DIGEST,
    MODULE.EXPECTED_SCHEMA_DIGEST,
    MODULE.EXPECTED_REGISTRY_DIGEST,
    MODULE.EXPECTED_SYNTHETIC_REGISTRY_DIGEST,
]


class C008R1RemainingRealWorldEvidenceClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = MODULE.require_mapping(MODULE.load_yaml(MODULE.CONTRACT_PATH), "contract")
        cls.schema = MODULE.require_mapping(MODULE.load_json(MODULE.SCHEMA_PATH), "schema")
        cls.canonical = MODULE.require_mapping(MODULE.load_yaml(MODULE.REGISTRY_PATH), "registry")
        cls.synthetic = MODULE.require_mapping(MODULE.load_yaml(MODULE.SYNTHETIC_PATH), "synthetic")
        cls.schema_validator, cls.loaded_contract = MODULE.load_validator()
        cls.mutations = json.loads(
            (ROOT / "tests/fixtures/c008-r1-remaining-real-world-evidence-closure/mutation-cases.json").read_text(encoding="utf-8")
        )

    def validate(self, value, *, synthetic_mode=False, contract=None):
        return MODULE.validate_registry(
            value,
            self.schema_validator,
            contract or self.loaded_contract,
            synthetic_mode=synthetic_mode,
        )

    def test_canonical_passes_deterministically_without_network(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network forbidden")):
            first = self.validate(copy.deepcopy(self.canonical))
            second = self.validate(copy.deepcopy(self.canonical))
        self.assertEqual(first, [])
        self.assertEqual(first, second)

    def test_distinct_synthetic_surface_is_mode_isolated(self):
        self.assertNotEqual(MODULE.semantic_digest(self.synthetic), MODULE.semantic_digest(self.canonical))
        self.assertIn("FIXTURE_MODE", "\n".join(self.validate(copy.deepcopy(self.synthetic))))
        self.assertEqual(self.validate(copy.deepcopy(self.synthetic), synthetic_mode=True), [])
        self.assertIn("FIXTURE_MODE", "\n".join(self.validate(copy.deepcopy(self.canonical), synthetic_mode=True)))

    def test_all_counted_mutations_dispatch_and_fail_closed(self):
        self.assertEqual(len(self.mutations), 85)
        self.assertEqual(len({item["name"] for item in self.mutations}), 85)
        for case in self.mutations:
            with self.subTest(case=case["name"]):
                value = copy.deepcopy(self.canonical)
                target = value
                for part in case["path"][:-1]:
                    target = target[part]
                final = case["path"][-1]
                if case["operation"] in {"replace", "add"}:
                    target[final] = case["value"]
                elif case["operation"] == "append":
                    target[final].append(case["value"])
                elif case["operation"] == "delete":
                    del target[final]
                else:
                    self.fail(f"unknown operation {case['operation']}")
                self.assertIn(case["expected"], "\n".join(self.validate(value)))

    def test_duplicate_yaml_and_json_keys_are_rejected(self):
        fixture = ROOT / "tests/fixtures/c008-r1-remaining-real-world-evidence-closure"
        with self.assertRaises(Exception):
            MODULE.load_yaml(fixture / "adversarial-duplicate-keys.yaml")
        with self.assertRaises(Exception):
            MODULE.load_json(fixture / "adversarial-duplicate-keys.json")

    def test_remote_and_permissive_schema_are_rejected(self):
        fixture = ROOT / "tests/fixtures/c008-r1-remaining-real-world-evidence-closure"
        self.assertIn("REMOTE_SCHEMA_REF", "\n".join(MODULE.audit_schema(MODULE.load_json(fixture / "adversarial-remote-ref-schema.json"))))
        self.assertIn("PERMISSIVE_SCHEMA", "\n".join(MODULE.audit_schema(MODULE.load_json(fixture / "adversarial-permissive-schema.json"))))

    def test_path_escape_symlink_and_byte_cap_are_rejected(self):
        with tempfile.NamedTemporaryFile() as outside:
            with self.assertRaisesRegex(Exception, "inside the repository"):
                MODULE.safe_path(Path(outside.name), "outside")
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as temp_dir:
            link = Path(temp_dir) / "link.yaml"
            link.symlink_to(MODULE.REGISTRY_PATH)
            with self.assertRaisesRegex(Exception, "symbolic link"):
                MODULE.safe_path(link, "link")
        with tempfile.NamedTemporaryFile(dir=ROOT / "tests", delete=False) as oversized:
            oversized.write(b"x" * 2_000_001)
            oversized_path = Path(oversized.name)
        try:
            with self.assertRaisesRegex(Exception, "2 MB byte cap"):
                MODULE.safe_path(oversized_path, "oversized")
        finally:
            oversized_path.unlink(missing_ok=True)

    def test_depth_node_and_nonfinite_are_rejected(self):
        deep = {}
        cursor = deep
        for index in range(105):
            cursor[str(index)] = {}
            cursor = cursor[str(index)]
        self.assertIn("INPUT_DEPTH", "\n".join(MODULE.audit_value(deep)))
        value = copy.deepcopy(self.canonical)
        value["readiness_result"]["resolved_count"] = float("nan")
        self.assertIn("NON_FINITE", "\n".join(self.validate(value)))

    def test_zero_new_evidence_and_three_blockers_are_exact(self):
        self.assertEqual(self.canonical["evidence_intake"]["new_evidence_items_total"], 0)
        self.assertEqual(self.canonical["evidence_intake"]["admitted_evidence_items"], [])
        reviews = self.canonical["blocker_reviews"]
        self.assertEqual([item["criterion_code"] for item in reviews], MODULE.EXPECTED_BLOCKERS)
        self.assertEqual([item["final_terminal_state"] for item in reviews], MODULE.EXPECTED_TERMINAL)
        self.assertTrue(all(item["blocking"] and not item["resolved"] for item in reviews))

    def test_c002_readiness_and_g1_are_unchanged(self):
        self.assertEqual(self.canonical["readiness_result"], MODULE.EXPECTED_TOTALS)
        self.assertEqual(self.canonical["g1_decision_surface"], MODULE.EXPECTED_G1)

    def test_founder_input_is_evidence_not_business_decision(self):
        requests = self.canonical["founder_evidence_requests"]
        self.assertEqual(requests["request_count"], 1)
        self.assertEqual(requests["requests"][0]["request_type"], "RIGHTS_SAFE_MEDIA_PACKET")
        self.assertFalse(requests["request_is_founder_decision"])
        self.assertFalse(self.canonical["g1_decision_surface"]["founder_business_decision_required"])
        self.assertTrue(self.canonical["g1_decision_surface"]["founder_evidence_input_required"])

    def test_authority_map_preserves_all_no_go_boundaries(self):
        authority = self.canonical["authority_effects"]
        self.assertEqual({key for key, value in authority.items() if value}, MODULE.ALLOWED_TRUE_AUTHORITY)
        self.assertFalse(authority["product_population"])
        self.assertFalse(authority["availability_or_stock_claim"])
        self.assertFalse(authority["runtime_staging_production"])
        self.assertFalse(authority["c009_or_m4_start"])
        self.assertFalse(authority["merge"])

    def test_dependency_pins_and_protected_owner_state_are_exact(self):
        issues = []
        MODULE.validate_dependency_pins(lambda code, message: issues.append(f"[{code}] {message}"), self.loaded_contract)
        self.assertEqual(issues, [])
        contract = copy.deepcopy(self.loaded_contract)
        contract["base_pins"]["c008_registry_semantic_sha256"] = "0" * 64
        issues = []
        MODULE.validate_dependency_pins(lambda code, message: issues.append(f"[{code}] {message}"), contract)
        self.assertIn("DEPENDENCY_PIN_REGRESSION", "\n".join(issues))

    def test_contract_policy_mutations_fail_closed(self):
        contract = copy.deepcopy(self.loaded_contract)
        contract["evidence_policy"]["exact_new_evidence_item_count"] = 1
        self.assertIn("CONTRACT_EVIDENCE_POLICY", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))
        contract = copy.deepcopy(self.loaded_contract)
        contract["g1_policy"]["m4_authorized"] = True
        self.assertIn("CONTRACT_G1_POLICY", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))
        contract = copy.deepcopy(self.loaded_contract)
        contract["authority"]["product_population_allowed"] = True
        self.assertIn("CONTRACT_AUTHORITY", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))
        contract = copy.deepcopy(self.loaded_contract)
        contract["source_policy"]["public_channel_evidence_search_found_new_items"] = True
        self.assertIn("CONTRACT_SOURCE_POLICY", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))
        contract = copy.deepcopy(self.loaded_contract)
        contract["readiness_policy"]["founder_selection_ready"] = True
        self.assertIn("CONTRACT_READINESS_POLICY", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))
        contract = copy.deepcopy(self.loaded_contract)
        contract["g1_policy"]["founder_decision_required"] = "START_M4"
        self.assertIn("CONTRACT_G1_POLICY", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))
        contract = copy.deepcopy(self.loaded_contract)
        contract["founder_request_policy"]["request_order"].append("SUPPLIER_SUPPLY_FULFILLMENT_PACKET")
        self.assertIn("CONTRACT_REQUEST_POLICY", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))
        contract = copy.deepcopy(self.loaded_contract)
        contract["validation"]["network_allowed"] = True
        self.assertIn("CONTRACT_VALIDATION_POLICY", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))
        contract = copy.deepcopy(self.loaded_contract)
        contract["contract_id"] = "wrong"
        self.assertIn("CONTRACT_EXACTNESS", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))
        contract = copy.deepcopy(self.loaded_contract)
        contract["dependencies"]["c008_registry"] = "redirect.yaml"
        self.assertIn("CONTRACT_EXACTNESS", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))
        contract = copy.deepcopy(self.loaded_contract)
        contract["schema"]["path"] = "redirect-schema.json"
        self.assertIn("CONTRACT_EXACTNESS", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))
        contract = copy.deepcopy(self.loaded_contract)
        contract["schema"]["draft"] = "https://json-schema.org/draft/2019-09/schema"
        self.assertIn("CONTRACT_EXACTNESS", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))
        contract = copy.deepcopy(self.loaded_contract)
        contract["registry"]["path"] = "redirect-registry.yaml"
        self.assertIn("CONTRACT_EXACTNESS", "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))

    def test_semantic_digests_fail_closed_and_are_eventually_pinned(self):
        if "TO_BE_FINALIZED" in ORIGINAL_DIGESTS:
            issues = MODULE.validate_package(allow_unpinned=False)
            self.assertIn("SEMANTIC_DIGEST", "\n".join(issues))
            return
        self.assertEqual(MODULE.semantic_digest(self.contract), ORIGINAL_DIGESTS[0])
        self.assertEqual(MODULE.semantic_digest(self.schema), ORIGINAL_DIGESTS[1])
        self.assertEqual(MODULE.semantic_digest(self.canonical), ORIGINAL_DIGESTS[2])
        self.assertEqual(MODULE.semantic_digest(self.synthetic), ORIGINAL_DIGESTS[3])


if __name__ == "__main__":
    unittest.main()
