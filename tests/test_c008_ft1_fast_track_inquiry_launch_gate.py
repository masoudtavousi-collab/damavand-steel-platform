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
VALIDATOR_PATH = ROOT / "repository/data/validation/validate_c008_ft1_fast_track_inquiry_launch_gate.py"
sys.path.insert(0, str(VALIDATOR_PATH.parent))
SPEC = importlib.util.spec_from_file_location("validate_c008_ft1_fast_track_inquiry_launch_gate", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
ORIGINAL_DIGESTS = [
    MODULE.EXPECTED_CONTRACT_DIGEST,
    MODULE.EXPECTED_SCHEMA_DIGEST,
    MODULE.EXPECTED_REGISTRY_DIGEST,
    MODULE.EXPECTED_SYNTHETIC_REGISTRY_DIGEST,
]


class C008FT1FastTrackInquiryLaunchGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = MODULE.require_mapping(MODULE.load_yaml(MODULE.CONTRACT_PATH), "contract")
        cls.schema = MODULE.require_mapping(MODULE.load_json(MODULE.SCHEMA_PATH), "schema")
        cls.canonical = MODULE.require_mapping(MODULE.load_yaml(MODULE.REGISTRY_PATH), "registry")
        cls.synthetic = MODULE.require_mapping(MODULE.load_yaml(MODULE.SYNTHETIC_PATH), "synthetic")
        cls.schema_validator, cls.loaded_contract = MODULE.load_validator()
        cls.mutations = json.loads(
            (ROOT / "tests/fixtures/c008-ft1-fast-track-inquiry-launch-gate/mutation-cases.json").read_text(encoding="utf-8")
        )

    def validate(self, value, *, synthetic_mode=False, contract=None):
        return MODULE.validate_registry(
            value, self.schema_validator, contract or self.loaded_contract, synthetic_mode=synthetic_mode
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
        self.assertEqual(len(self.mutations), 66)
        self.assertEqual(len({item["name"] for item in self.mutations}), 66)
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
        fixture = ROOT / "tests/fixtures/c008-ft1-fast-track-inquiry-launch-gate"
        with self.assertRaises(Exception):
            MODULE.load_yaml(fixture / "adversarial-duplicate-keys.yaml")
        with self.assertRaises(Exception):
            MODULE.load_json(fixture / "adversarial-duplicate-keys.json")

    def test_remote_and_permissive_schema_are_rejected(self):
        fixture = ROOT / "tests/fixtures/c008-ft1-fast-track-inquiry-launch-gate"
        remote = "\n".join(MODULE.audit_schema(MODULE.load_json(fixture / "adversarial-remote-ref-schema.json")))
        permissive = "\n".join(MODULE.audit_schema(MODULE.load_json(fixture / "adversarial-permissive-schema.json")))
        self.assertIn("REMOTE_SCHEMA_REF", remote)
        self.assertIn("PERMISSIVE_SCHEMA", permissive)

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
        value["gate"]["met_count"] = float("nan")
        self.assertIn("NON_FINITE", "\n".join(self.validate(value)))

    def test_gate_is_false_and_all_prerequisites_are_exact(self):
        gate = self.canonical["gate"]
        self.assertFalse(gate["eligible"])
        self.assertEqual(gate["prerequisite_count"], 12)
        self.assertEqual(gate["met_count"], 4)
        self.assertEqual(gate["unmet_count"], 8)
        self.assertEqual(gate["blockers"], MODULE.EXPECTED_BLOCKERS)
        self.assertEqual(gate["prerequisites"], MODULE.EXPECTED_PREREQUISITES)

    def test_c002_is_preserved_and_not_aliased(self):
        self.assertEqual(self.canonical["c002_snapshot"], MODULE.EXPECTED_C002)
        self.assertEqual(self.canonical["c002_snapshot"]["relationship"], "INDEPENDENT_SIBLING_NOT_ALIAS")
        self.assertFalse(self.canonical["c002_snapshot"]["founder_selection_ready"])
        self.assertEqual(self.canonical["c002_snapshot"]["candidate_registry_count"], 0)

    def test_supplier_media_and_public_claims_fail_closed(self):
        self.assertEqual(self.canonical["supply_fulfillment_deferral"], MODULE.EXPECTED_SUPPLY)
        self.assertEqual(self.canonical["media_boundary"], MODULE.EXPECTED_MEDIA)
        self.assertFalse(self.canonical["commercial_direction"]["public_price"])
        self.assertFalse(self.canonical["commercial_direction"]["public_stock_or_availability"])
        self.assertFalse(self.canonical["commercial_direction"]["public_eta_or_sla"])

    def test_product_selector_and_successor_boundaries_are_exact(self):
        self.assertEqual(self.canonical["commercial_direction"], MODULE.EXPECTED_COMMERCIAL)
        self.assertEqual(self.canonical["selector_boundaries"], MODULE.EXPECTED_SELECTOR)
        self.assertFalse(self.canonical["authority_effects"]["c009_or_m4_start"])
        self.assertFalse(self.canonical["authority_effects"]["runtime_mutation"])
        self.assertFalse(self.canonical["authority_effects"]["merge"])

    def test_dependency_pins_and_protected_owner_state_are_exact(self):
        issues = []
        MODULE.validate_dependency_pins(lambda code, message: issues.append(f"[{code}] {message}"), self.loaded_contract)
        self.assertEqual(issues, [])
        contract = copy.deepcopy(self.loaded_contract)
        contract["base_pins"]["c008_r1_registry_semantic_sha256"] = "0" * 64
        issues = []
        MODULE.validate_dependency_pins(lambda code, message: issues.append(f"[{code}] {message}"), contract)
        self.assertIn("DEPENDENCY_PIN", "\n".join(issues))

    def test_contract_policy_mutations_fail_closed(self):
        cases = [
            (["contract_id"], "wrong", "CONTRACT_EXACTNESS"),
            (["schema", "path"], "wrong.json", "CONTRACT_EXACTNESS"),
            (["registry", "path"], "wrong.yaml", "CONTRACT_EXACTNESS"),
            (["dependencies", "c008_r1_registry"], "redirect.yaml", "CONTRACT_EXACTNESS"),
            (["authority", "product_population_allowed"], True, "CONTRACT_AUTHORITY"),
            (["source_policy", "authorization_ts"], "0", "CONTRACT_SOURCE_POLICY"),
            (["source_policy", "exact_thread_reply_count"], 0, "CONTRACT_SOURCE_POLICY"),
            (["source_policy", "authorization_reply_index"], 16, "CONTRACT_SOURCE_POLICY"),
            (["source_policy", "execution_command_sha256"], "0" * 64, "CONTRACT_SOURCE_POLICY"),
            (["gate_policy", "initial_state"], True, "CONTRACT_GATE_POLICY"),
            (["c002_separation_policy", "founder_selection_ready"], True, "CONTRACT_C002_POLICY"),
            (["supply_fulfillment_policy", "deferred_is_waiver"], True, "CONTRACT_SUPPLY_POLICY"),
            (["media_policy", "publication_without_rights_safe_media_allowed"], True, "CONTRACT_MEDIA_POLICY"),
            (["commercial_direction_policy", "creates_product_variant_value_tuple_or_sku"], True, "CONTRACT_COMMERCIAL_POLICY"),
            (["selector_policy", "finish_and_color_may_be_fused"], True, "CONTRACT_SELECTOR_POLICY"),
            (["validation", "network_allowed"], True, "CONTRACT_VALIDATION_POLICY"),
        ]
        for path, replacement, code in cases:
            with self.subTest(path=path):
                contract = copy.deepcopy(self.loaded_contract)
                target = contract
                for part in path[:-1]:
                    target = target[part]
                target[path[-1]] = replacement
                self.assertIn(code, "\n".join(self.validate(copy.deepcopy(self.canonical), contract=contract)))

    def test_semantic_digests_fail_closed_and_are_eventually_pinned(self):
        if "TO_BE_FINALIZED" in ORIGINAL_DIGESTS:
            self.assertIn("SEMANTIC_DIGEST", "\n".join(MODULE.validate_package(allow_unpinned=False)))
            return
        self.assertEqual(MODULE.semantic_digest(self.contract), ORIGINAL_DIGESTS[0])
        self.assertEqual(MODULE.semantic_digest(self.schema), ORIGINAL_DIGESTS[1])
        self.assertEqual(MODULE.semantic_digest(self.canonical), ORIGINAL_DIGESTS[2])
        self.assertEqual(MODULE.semantic_digest(self.synthetic), ORIGINAL_DIGESTS[3])


if __name__ == "__main__":
    unittest.main()
