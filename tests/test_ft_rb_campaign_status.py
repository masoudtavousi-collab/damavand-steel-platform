from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "repository/data/validation/validate_ft_rb_campaign_status.py"
SPEC = importlib.util.spec_from_file_location("ft_rb_campaign_status", VALIDATOR)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

class CampaignStatusTests(unittest.TestCase):
    def setUp(self):
        self.registry = MODULE.load(MODULE.REGISTRY)
        self.contract = MODULE.load(MODULE.CONTRACT)
        self.schema = MODULE.load(MODULE.SCHEMA)

    def test_canonical_passes_with_strict_pins(self):
        self.assertEqual(MODULE.validate(self.contract, self.schema, self.registry, synthetic=False, allow_unpinned=False), [])

    def test_synthetic_passes_with_strict_pins(self):
        fixture = ROOT / "tests/fixtures/ft-rb-campaign-status/valid-synthetic.yaml"
        self.assertEqual(MODULE.validate(self.contract, self.schema, MODULE.load(fixture), synthetic=True, allow_unpinned=False), [])

    def test_live_semantic_digests_match_exact_pins(self):
        fixture = ROOT / "tests/fixtures/ft-rb-campaign-status/valid-synthetic.yaml"
        self.assertEqual(MODULE.digest(self.contract), MODULE.EXPECTED_DIGESTS["contract"])
        self.assertEqual(MODULE.digest(self.schema), MODULE.EXPECTED_DIGESTS["schema"])
        self.assertEqual(MODULE.digest(self.registry), MODULE.EXPECTED_DIGESTS["canonical"])
        self.assertEqual(MODULE.digest(MODULE.load(fixture)), MODULE.EXPECTED_DIGESTS["synthetic"])

    def test_mutation_manifest(self):
        cases = json.loads((ROOT / "tests/fixtures/ft-rb-campaign-status/mutation-cases.json").read_text())
        for case in cases:
            with self.subTest(case=case["name"]):
                value = deepcopy(self.registry); target = value
                for key in case["path"][:-1]: target = target[key]
                target[case["path"][-1]] = case["value"]
                self.assertTrue(any(issue.startswith(case["code"]) for issue in MODULE.validate(self.contract, self.schema, value, synthetic=False, allow_unpinned=False)))

    def test_contract_binding_and_owner_transfer_mutations_fail_closed(self):
        for path, value in [(["record_kind"], "wrong"), (["schema", "path"], "elsewhere"), (["authority", "gate_transition_allowed"], True), (["owner_policy", "product_truth_owner"], "WOOCOMMERCE_ADAPTER"), (["source_policy", "campaign_authorization_reply_count"], 1), (["validation", "network_allowed"], True), (["dependency_pins", "c008_contract"], "0" * 64)]:
            with self.subTest(path=path):
                contract = deepcopy(self.contract); target = contract
                for key in path[:-1]: target = target[key]
                target[path[-1]] = value
                self.assertIn("CONTRACT_EXACTNESS", MODULE.validate(contract, self.schema, self.registry, synthetic=False, allow_unpinned=False))

    def test_schema_boolean_union_prefix_and_annotation_adversaries_fail_closed(self):
        adversaries = [
            {"$schema":"https://json-schema.org/draft/2020-12/schema", "type":"array", "items":True},
            {"$schema":"https://json-schema.org/draft/2020-12/schema", "type":["object","array"], "additionalProperties":False},
            {"$schema":"https://json-schema.org/draft/2020-12/schema", "type":"array", "prefixItems":[True], "items":False},
            {"$schema":"https://json-schema.org/draft/2020-12/schema", "title":"annotation only"},
            {"$schema":"https://json-schema.org/draft/2020-12/schema", "type":"string", "properties":{}},
        ]
        for schema in adversaries:
            with self.subTest(schema=schema): self.assertTrue(MODULE.schema_issues(schema))

    def test_wrong_type_sections_and_lane_mutations_fail_closed_without_exception(self):
        for path, value in [(["effective_gate"], "wrong"), (["lanes"], "wrong"), (["allowlist"], "wrong"), (["blocker_statuses"], "wrong"), (["lanes", 0, "workflow_status"], "MET")]:
            with self.subTest(path=path):
                registry = deepcopy(self.registry); target = registry
                for key in path[:-1]: target = target[key]
                target[path[-1]] = value
                self.assertTrue(MODULE.validate(self.contract, self.schema, registry, synthetic=False, allow_unpinned=False))

    def test_load_rejects_actual_symlink_byte_depth_node_and_nonfinite_inputs(self):
        original_root = MODULE.ROOT
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            try:
                MODULE.ROOT = root
                target = root / "target.yaml"; target.write_text("value: safe\n", encoding="utf-8")
                link = root / "link.yaml"; link.symlink_to(target)
                with self.assertRaises(ValueError): MODULE.load(link)
                too_large = root / "large.yaml"; too_large.write_text("x: " + "a" * (MODULE.MAX_BYTES + 1), encoding="utf-8")
                with self.assertRaises(ValueError): MODULE.load(too_large)
                deep: object = "leaf"
                for _ in range(MODULE.MAX_DEPTH + 2): deep = {"x": deep}
                depth = root / "depth.yaml"; depth.write_text(json.dumps(deep), encoding="utf-8")
                with self.assertRaises(ValueError): MODULE.load(depth)
                nodes = root / "nodes.yaml"; nodes.write_text(json.dumps(list(range(MODULE.MAX_NODES + 1))), encoding="utf-8")
                with self.assertRaises(ValueError): MODULE.load(nodes)
                nonfinite = root / "nonfinite.yaml"; nonfinite.write_text("value: .nan\n", encoding="utf-8")
                with self.assertRaises(ValueError): MODULE.load(nonfinite)
            finally:
                MODULE.ROOT = original_root

    def test_duplicate_yaml_rejected(self):
        with self.assertRaises(ValueError): MODULE.load(ROOT / "tests/fixtures/ft-rb-campaign-status/adversarial-duplicate-keys.yaml")

    def test_duplicate_json_rejected(self):
        with self.assertRaises(ValueError): MODULE.load(ROOT / "tests/fixtures/ft-rb-campaign-status/adversarial-duplicate-keys.json")

    def test_permissive_and_remote_schema_rejected(self):
        self.assertTrue(any(item.startswith("PERMISSIVE_SCHEMA") for item in MODULE.schema_issues(MODULE.load(ROOT / "tests/fixtures/ft-rb-campaign-status/adversarial-permissive-schema.json"))))
        self.assertTrue(any(item.startswith("REMOTE_SCHEMA_REF") for item in MODULE.schema_issues(MODULE.load(ROOT / "tests/fixtures/ft-rb-campaign-status/adversarial-remote-ref-schema.json"))))

    def test_path_escape_rejected(self):
        with self.assertRaises(ValueError): MODULE.load(Path("/etc/hosts"))

if __name__ == "__main__": unittest.main()
