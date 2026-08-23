from __future__ import annotations

import copy
import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "repository/data/validation/validate_c009_first_commercial_slice_canonical_leaf_promotion.py"
SPEC = importlib.util.spec_from_file_location("validate_c009", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

FIXTURES = ROOT / "tests/fixtures/c009-first-commercial-slice-canonical-leaf-promotion"


def mutate(document, case):
    target = document
    path = case["path"]
    for part in path[:-1]:
        target = target[part]
    key = path[-1]
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
        raise AssertionError(f"unknown operation: {operation}")


class C009ValidationTests(unittest.TestCase):
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
        codes = {issue.code for issue in MODULE.validate_registry(self.synthetic, self.schema, synthetic=False)}
        self.assertIn("FIXTURE_MODE", codes)

    def test_schema_is_closed_and_local(self):
        self.assertEqual([], MODULE.audit_schema(self.schema))
        self.assertEqual([], sorted({ref for ref in self._refs(self.schema) if not ref.startswith("#/")}))

    def _refs(self, value):
        if isinstance(value, dict):
            for key, child in value.items():
                if key == "$ref" and isinstance(child, str):
                    yield child
                yield from self._refs(child)
        elif isinstance(value, list):
            for child in value:
                yield from self._refs(child)

    def test_contract_policy_is_exact(self):
        self.assertEqual([], MODULE.validate_contract(self.contract))
        probes = [
            ("schema", "path", "wrong.json"),
            ("registry", "path", "wrong.yaml"),
            ("authority", "runtime_staging_production_mutation_allowed", True),
            ("source_policy", "authorization_ts", "0.000000"),
            ("promotion_policy", "exact_leaf_count", 2),
            ("promotion_policy", "product_identity_semantic_owner", "C009_CANONICAL_PROMOTION_EXTENSION"),
            ("promotion_policy", "combination_validity_semantic_owner", "C009_CANONICAL_PROMOTION_EXTENSION"),
            ("promotion_policy", "pilot_evidence_semantic_owner", "C009_CANONICAL_PROMOTION_EXTENSION"),
            ("promotion_policy", "authority_transfer", True),
            ("stable_identity_policy", "label_slug_wordpress_woocommerce_or_commercial_sku_derived", True),
            ("validation", "network_allowed", True),
            ("dependencies", "pd03b_registry", "wrong.yaml"),
            ("dependency_pins", "pd03b_registry", "0" * 64),
        ]
        for section, key, value in probes:
            changed = copy.deepcopy(self.contract)
            changed[section][key] = value
            self.assertIn("CONTRACT_EXACTNESS", {i.code for i in MODULE.validate_contract(changed)})

    def test_dependency_pins_and_protected_owners(self):
        self.assertEqual([], MODULE.validate_dependencies(self.contract))
        self.assertEqual(3, len(MODULE.load_document(ROOT / MODULE.EXPECTED_DEPENDENCIES["product_entities_registry"], "entities")))
        c002 = MODULE.load_document(ROOT / MODULE.EXPECTED_DEPENDENCIES["c002_registry"], "c002")
        self.assertEqual([], c002["candidates"])

    def test_exact_combination_and_leaf_semantics(self):
        promotion = self.canonical["promotion"]
        self.assertEqual("pcomb:829e387ccdcb", promotion["canonical_combination"]["combination_id"])
        self.assertEqual("prd:sku:66ebd0510693", promotion["canonical_leaf"]["entity"]["entity_id"])
        self.assertEqual(MODULE.EXPECTED_AXES, promotion["canonical_combination"]["axes"])
        self.assertEqual("MISSING_DATA_VALUE", promotion["canonical_combination"]["availability_reference"]["state"])
        self.assertEqual(1, promotion["promotion_summary"]["promoted_leaf_count"])
        self.assertEqual(0, promotion["promotion_summary"]["other_pilots_promoted"])

    def test_c002_and_fast_track_gate_are_unchanged(self):
        self.assertEqual(MODULE.EXPECTED_C002, self.canonical["c002_snapshot"])
        self.assertEqual(MODULE.EXPECTED_FT1, self.canonical["c008_ft1_snapshot"])
        self.assertFalse(self.canonical["c008_ft1_snapshot"]["gate_reevaluated"])

    def test_mutation_manifest_is_unique_and_fully_dispatched(self):
        self.assertEqual(81, len(self.cases))
        self.assertEqual(81, len({case["name"] for case in self.cases}))
        for case in self.cases:
            changed = copy.deepcopy(self.canonical)
            mutate(changed, case)
            codes = {issue.code for issue in MODULE.validate_registry(changed, self.schema, synthetic=False)}
            self.assertIn(case["expected"], codes, case["name"])

    def test_duplicate_key_parsers_fail_closed(self):
        for name in ("adversarial-duplicate-keys.yaml", "adversarial-duplicate-keys.json"):
            with self.assertRaises(ValueError):
                MODULE.load_document(FIXTURES / name, name)

    def test_permissive_and_remote_schemas_fail_closed(self):
        permissive = MODULE.load_document(FIXTURES / "adversarial-permissive-schema.json", "permissive")
        remote = MODULE.load_document(FIXTURES / "adversarial-remote-ref-schema.json", "remote")
        self.assertIn("OPEN_SCHEMA", {issue.code for issue in MODULE.audit_schema(permissive)})
        self.assertIn("REMOTE_SCHEMA_REF", {issue.code for issue in MODULE.audit_schema(remote)})
        empty_branch = copy.deepcopy(self.schema)
        empty_branch["properties"]["promotion"] = {}
        self.assertIn("PERMISSIVE_SCHEMA", {issue.code for issue in MODULE.audit_schema(empty_branch)})
        for permissive_type in (["object"], ["object", "null"]):
            union_branch = copy.deepcopy(self.schema)
            union_branch["properties"]["promotion"] = {"type": permissive_type}
            self.assertIn("OPEN_SCHEMA", {issue.code for issue in MODULE.audit_schema(union_branch)})
        applicator_branches = (
            {"not": {"type": "null"}},
            {"anyOf": [{"$ref": "#/$defs/promotion"}, {"not": {"type": "null"}}]},
            {"oneOf": [{"type": "string"}, {"not": {"type": "null"}}]},
        )
        for permissive_branch in applicator_branches:
            changed = copy.deepcopy(self.schema)
            changed["properties"]["promotion"] = permissive_branch
            self.assertIn("PERMISSIVE_APPLICATOR", {issue.code for issue in MODULE.audit_schema(changed)})
        for vacuous_branch in ({"description": "promotion"}, {"format": "uri"}, {"minLength": 0}, {"items": False}):
            changed = copy.deepcopy(self.schema)
            changed["properties"]["promotion"] = vacuous_branch
            self.assertIn("NON_ASSERTIVE_SCHEMA", {issue.code for issue in MODULE.audit_schema(changed)})
        for literal_branch in ({"const": {"supplier_claim": "AVAILABLE NOW"}}, {"enum": [{"price_claim": "100"}]}):
            changed = copy.deepcopy(self.schema)
            changed["properties"]["promotion"] = literal_branch
            self.assertIn("CONTAINER_LITERAL_SCHEMA", {issue.code for issue in MODULE.audit_schema(changed)})

    def test_coordinated_identity_and_claim_creep_fail_closed(self):
        changed = copy.deepcopy(self.canonical)
        changed["promotion"]["canonical_combination"]["combination_id"] = "pcomb:333333333333"
        changed["promotion"]["canonical_leaf"]["canonical_combination_id"] = "pcomb:333333333333"
        changed["promotion"]["immutable_binding"]["combination_id"] = "pcomb:333333333333"
        changed["promotion"]["canonical_leaf"]["entity"]["entity_id"] = "prd:sku:444444444444"
        changed["promotion"]["immutable_binding"]["sku_entity_id"] = "prd:sku:444444444444"
        codes = {issue.code for issue in MODULE.validate_registry(changed, self.schema, synthetic=False)}
        self.assertIn("CANONICAL_IDENTITY", codes)
        self.assertIn("SKU_EXACTNESS", codes)

        changed = copy.deepcopy(self.canonical)
        changed["promotion"]["canonical_leaf"]["entity"]["canonical_label"] = "Available now — guaranteed lowest price"
        self.assertIn("SKU_EXACTNESS", {issue.code for issue in MODULE.validate_registry(changed, self.schema, synthetic=False)})

    def test_path_symlink_and_byte_caps_fail_closed(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as directory:
            temp = Path(directory)
            target = temp / "target.yaml"
            target.write_text("ok: true\n", encoding="utf-8")
            link = temp / "link.yaml"
            link.symlink_to(target)
            with self.assertRaises(ValueError):
                MODULE.load_document(link, "symlink")
            outside = Path("/tmp/c009-outside.yaml")
            outside.write_text("ok: true\n", encoding="utf-8")
            try:
                with self.assertRaises(ValueError):
                    MODULE.load_document(outside, "outside")
            finally:
                outside.unlink(missing_ok=True)
            oversized = temp / "oversized.yaml"
            oversized.write_bytes(b"x" * (MODULE.MAX_BYTES + 1))
            with self.assertRaises(ValueError):
                MODULE.load_document(oversized, "oversized")

    def test_depth_nodes_and_nonfinite_fail_closed(self):
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

    def test_semantic_digests_are_fail_closed_and_fully_pinned(self):
        expected = [MODULE.EXPECTED_CONTRACT_DIGEST, MODULE.EXPECTED_SCHEMA_DIGEST, MODULE.EXPECTED_REGISTRY_DIGEST, MODULE.EXPECTED_SYNTHETIC_DIGEST]
        self.assertNotIn("TO_BE_FINALIZED", expected)
        self.assertEqual(MODULE.semantic_digest(self.contract), expected[0])
        self.assertEqual(MODULE.semantic_digest(self.schema), expected[1])
        self.assertEqual(MODULE.semantic_digest(self.canonical), expected[2])
        self.assertEqual(MODULE.semantic_digest(self.synthetic), expected[3])


if __name__ == "__main__":
    unittest.main()
