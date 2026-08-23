from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "repository/data/validation/validate_c009_ft2_post_c009_fast_track_gate_reevaluation.py"
SPEC = importlib.util.spec_from_file_location("validate_c009ft2", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

FIXTURES = ROOT / "tests/fixtures/c009-ft2-post-c009-fast-track-gate-reevaluation"


def mutate(document, case):
    target = document
    for part in case["path"][:-1]:
        target = target[part]
    key = case["path"][-1]
    operation = case["operation"]
    if operation == "replace":
        target[key] = case["value"]
    elif operation == "delete":
        if isinstance(target, list):
            del target[key]
        else:
            target.pop(key)
    elif operation == "append":
        target[key].append(case["value"])
    elif operation == "add":
        target[key] = case["value"]
    else:
        raise AssertionError(f"unknown mutation operation: {operation}")


class C009FT2ValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = MODULE.load_document(MODULE.CONTRACT_PATH, "contract")
        cls.schema = MODULE.load_document(MODULE.SCHEMA_PATH, "schema")
        cls.canonical = MODULE.load_document(MODULE.REGISTRY_PATH, "canonical")
        cls.synthetic = MODULE.load_document(FIXTURES / "valid-synthetic.yaml", "synthetic")
        cls.cases = json.loads((FIXTURES / "mutation-cases.json").read_text(encoding="utf-8"))

    def test_canonical_positive_surface(self):
        self.assertEqual([], MODULE.validate_all(self.contract, self.schema, self.canonical, synthetic=False, allow_unpinned=True))

    def test_distinct_synthetic_positive_surface(self):
        self.assertNotEqual(MODULE.semantic_digest(self.canonical), MODULE.semantic_digest(self.synthetic))
        self.assertEqual([], MODULE.validate_all(self.contract, self.schema, self.synthetic, synthetic=True, allow_unpinned=True))
        self.assertIn("FIXTURE_MODE", {i.code for i in MODULE.validate_registry(self.synthetic, self.schema, synthetic=False)})

    def test_schema_is_closed_assertive_and_local(self):
        self.assertEqual([], MODULE.audit_schema(self.schema))
        permissive = MODULE.load_document(FIXTURES / "adversarial-permissive-schema.json", "permissive")
        remote = MODULE.load_document(FIXTURES / "adversarial-remote-ref-schema.json", "remote")
        self.assertIn("OPEN_SCHEMA", {i.code for i in MODULE.audit_schema(permissive)})
        self.assertIn("REMOTE_SCHEMA_REF", {i.code for i in MODULE.audit_schema(remote)})
        probes = ({}, {"description": "gate"}, {"not": {"type": "null"}}, {"anyOf": [{"type": "object"}, {"type": "null"}]})
        for probe in probes:
            changed = copy.deepcopy(self.schema)
            changed["properties"]["effective_gate"] = probe
            self.assertTrue(MODULE.audit_schema(changed))

    def test_contract_is_exact_and_fail_closed(self):
        self.assertEqual([], MODULE.validate_contract(self.contract))
        probes = [
            ("schema", "path", "wrong.json"), ("registry", "path", "wrong.yaml"),
            ("authority", "gate_true_or_launch_authority_allowed", True),
            ("source_policy", "predecessor_post_merge_ci_run", 1),
            ("owner_policy", "authority_transfer", True),
            ("transition_policy", "changed_prerequisites_count", 2),
            ("c002_policy", "founder_selection_ready", True),
            ("no_claim_policy", "stock", "IN_STOCK"),
            ("validation", "network_allowed", True),
            ("dependencies", "c009_registry", "wrong.yaml"),
            ("dependency_pins", "c009_registry", "0" * 64),
        ]
        for section, key, value in probes:
            changed = copy.deepcopy(self.contract)
            changed[section][key] = value
            self.assertIn("CONTRACT_EXACTNESS", {i.code for i in MODULE.validate_contract(changed)})

    def test_dependency_pins_preserve_c002_ft1_and_c009(self):
        self.assertEqual([], MODULE.validate_dependencies(self.contract))
        c002 = MODULE.load_document(ROOT / MODULE.EXPECTED_DEPENDENCIES["c002_registry"], "c002")
        self.assertEqual([], c002["candidates"])
        ft1 = MODULE.load_document(ROOT / MODULE.EXPECTED_DEPENDENCIES["c008_ft1_registry"], "ft1")
        self.assertEqual((False, 4, 8), (ft1["gate"]["eligible"], ft1["gate"]["met_count"], ft1["gate"]["unmet_count"]))

    def test_only_product_prerequisite_changes(self):
        transition = self.canonical["transition"]
        self.assertEqual(1, transition["changed_prerequisites_count"])
        self.assertEqual("CANONICAL_PRODUCT_PROMOTION_COMPLETE", transition["prerequisite_id"])
        self.assertEqual("NOT_AUTHORIZED", transition["previous"]["state"])
        self.assertEqual("MET", transition["effective"]["state"])
        self.assertFalse(transition["promotion_effect"])

    def test_effective_gate_is_false_five_of_twelve(self):
        gate = self.canonical["effective_gate"]
        self.assertEqual((False, 5, 7, 12), (gate["eligible"], gate["met_count"], gate["unmet_count"], gate["prerequisite_count"]))
        self.assertEqual(MODULE.EXPECTED_BLOCKERS, gate["blockers"])

    def test_c009_evidence_and_no_claims_are_exact(self):
        evidence = self.canonical["c009_evidence"]
        self.assertEqual("pilot:f5922666261e", evidence["target_pilot_id"])
        self.assertEqual("pcomb:829e387ccdcb", evidence["canonical_combination_id"])
        self.assertEqual("prd:sku:66ebd0510693", evidence["canonical_leaf_id"])
        self.assertEqual("MISSING_DATA_VALUE", evidence["availability"])
        self.assertEqual("ABSENT", evidence["price"])
        self.assertEqual("ABSENT", evidence["supplier_truth"])

    def test_c002_state_is_unchanged(self):
        self.assertEqual(MODULE.EXPECTED_C002, self.canonical["c002_snapshot"])
        self.assertFalse(self.canonical["c002_snapshot"]["founder_selection_ready"])
        self.assertEqual(0, self.canonical["c002_snapshot"]["candidate_registry_count"])

    def test_mutation_manifest_is_unique_and_fully_dispatched(self):
        self.assertEqual(76, len(self.cases))
        self.assertEqual(76, len({case["name"] for case in self.cases}))
        for case in self.cases:
            changed = copy.deepcopy(self.canonical)
            mutate(changed, case)
            codes = {issue.code for issue in MODULE.validate_registry(changed, self.schema, synthetic=False)}
            self.assertIn(case["expected"], codes, case["name"])

    def test_duplicate_key_parsers_fail_closed(self):
        for name in ("adversarial-duplicate-keys.yaml", "adversarial-duplicate-keys.json"):
            with self.assertRaises(ValueError):
                MODULE.load_document(FIXTURES / name, name)

    def test_coordinated_laundering_and_extra_population_fail_closed(self):
        changed = copy.deepcopy(self.canonical)
        changed["predecessors"]["c009"]["merge_commit"] = "1" * 40
        changed["c009_evidence"]["evidence_refs"][0] = "git:main:" + "1" * 40
        changed["transition"]["evidence_refs"][0] = "git:main:" + "1" * 40
        codes = {i.code for i in MODULE.validate_registry(changed, self.schema, synthetic=False)}
        self.assertIn("PREDECESSOR_EXACTNESS", codes)
        self.assertIn("C009_EVIDENCE", codes)

        changed = copy.deepcopy(self.canonical)
        changed["products"] = [{"stock": "AVAILABLE", "price": 100}]
        codes = {i.code for i in MODULE.validate_registry(changed, self.schema, synthetic=False)}
        self.assertIn("SCHEMA_VALIDATION", codes)
        self.assertIn("FORBIDDEN_POPULATION", codes)

    def test_path_symlink_byte_depth_and_nonfinite_fail_closed(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as directory:
            temp = Path(directory)
            target = temp / "target.yaml"
            target.write_text("ok: true\n", encoding="utf-8")
            link = temp / "link.yaml"
            link.symlink_to(target)
            with self.assertRaises(ValueError):
                MODULE.load_document(link, "symlink")
            oversized = temp / "oversized.yaml"
            oversized.write_bytes(b"x" * (MODULE.MAX_BYTES + 1))
            with self.assertRaises(ValueError):
                MODULE.load_document(oversized, "oversized")
        deep = value = {}
        for _ in range(MODULE.MAX_DEPTH + 1):
            value["x"] = {}
            value = value["x"]
        with self.assertRaises(ValueError):
            MODULE._bounded_tree(deep)
        with self.assertRaises(ValueError):
            MODULE._bounded_tree(float("nan"))

    def test_validation_is_deterministic_and_offline(self):
        first = MODULE.validate_registry(copy.deepcopy(self.canonical), self.schema, synthetic=False)
        second = MODULE.validate_registry(copy.deepcopy(self.canonical), self.schema, synthetic=False)
        self.assertEqual(first, second)
        self.assertFalse(self.contract["validation"]["network_allowed"])
        self.assertFalse(self.contract["validation"]["side_effects_allowed"])

    def test_semantic_digests_fail_closed_and_can_be_pinned(self):
        pins = [MODULE.EXPECTED_CONTRACT_DIGEST, MODULE.EXPECTED_SCHEMA_DIGEST, MODULE.EXPECTED_REGISTRY_DIGEST, MODULE.EXPECTED_SYNTHETIC_DIGEST]
        if "TO_BE_FINALIZED" in pins:
            codes = {i.code for i in MODULE.validate_all(self.contract, self.schema, self.canonical, synthetic=False, allow_unpinned=False)}
            self.assertIn("SEMANTIC_DIGEST", codes)
        else:
            self.assertEqual(MODULE.semantic_digest(self.contract), pins[0])
            self.assertEqual(MODULE.semantic_digest(self.schema), pins[1])
            self.assertEqual(MODULE.semantic_digest(self.canonical), pins[2])
            self.assertEqual(MODULE.semantic_digest(self.synthetic), pins[3])


if __name__ == "__main__":
    unittest.main()
