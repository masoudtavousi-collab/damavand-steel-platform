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
FIXTURES = ROOT / "tests/fixtures/ft-rb-01-rights-safe-media-readiness"
SPEC = importlib.util.spec_from_file_location("ftrb01_validator", ROOT / "repository/data/validation/validate_ft_rb_01_rights_safe_media_readiness.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def mutate(document, case):
    target = document
    for part in case["path"][:-1]:
        target = target[part]
    key = case["path"][-1]
    operation = case["operation"]
    if operation == "replace":
        target[key] = case["value"]
    elif operation == "delete":
        del target[key]
    elif operation == "append":
        target[key].append(case["value"])
    else:
        raise AssertionError(operation)


class RightsSafeMediaReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = MODULE.load(MODULE.CONTRACT)
        cls.schema = MODULE.load(MODULE.SCHEMA)
        cls.canonical = MODULE.load(MODULE.REGISTRY)
        cls.synthetic = MODULE.load(MODULE.SYNTHETIC)
        cls.cases = json.loads((FIXTURES / "mutation-cases.json").read_text(encoding="utf-8"))

    def validate(self, registry, *, synthetic=False, contract=None, schema=None, allow=False, worktree=False):
        return MODULE.validate(contract or self.contract, schema or self.schema, registry, synthetic=synthetic, allow_unpinned=allow, check_worktree=worktree)

    def test_01_strict_pinned_positive_surfaces_are_distinct(self):
        self.assertNotEqual(MODULE.digest(self.canonical), MODULE.digest(self.synthetic))
        self.assertEqual([], self.validate(self.canonical))
        self.assertEqual([], self.validate(self.synthetic, synthetic=True))

    def test_02_semantic_pins_match_and_sentinel_fails_closed(self):
        self.assertEqual(MODULE.DIGESTS["contract"], MODULE.digest(self.contract))
        self.assertEqual(MODULE.DIGESTS["schema"], MODULE.digest(self.schema))
        self.assertEqual(MODULE.DIGESTS["canonical"], MODULE.digest(self.canonical))
        self.assertEqual(MODULE.DIGESTS["synthetic"], MODULE.digest(self.synthetic))
        original = MODULE.DIGESTS["contract"]
        try:
            MODULE.DIGESTS["contract"] = "TO_BE_FINALIZED"
            self.assertIn("SEMANTIC_DIGEST:contract", self.validate(self.canonical))
        finally:
            MODULE.DIGESTS["contract"] = original

    def test_03_all_named_mutations_fail_closed(self):
        names = [case["name"] for case in self.cases]
        self.assertEqual(len(names), len(set(names)))
        for case in self.cases:
            with self.subTest(case=case["name"]):
                value = copy.deepcopy(self.canonical)
                mutate(value, case)
                issues = self.validate(value)
                self.assertTrue(any(issue.startswith(case["code"]) for issue in issues), issues)

    def test_04_contract_source_owner_validation_and_pin_drift(self):
        probes = []
        for path, value in [
            (("authority","media_publication_allowed"), True),
            (("source_policy","campaign_authorized_starting_main"), "bad"),
            (("source_policy","mission_base_main"), "bad"),
            (("owner_policy","media_owner"), "OTHER"),
            (("validation","offline_only"), False),
            (("dependency_pins","c009_registry"), "bad"),
        ]:
            contract = copy.deepcopy(self.contract); target = contract
            for key in path[:-1]: target = target[key]
            target[path[-1]] = value; probes.append(contract)
        extra = copy.deepcopy(self.contract); extra["fast_track_gate"] = True; probes.append(extra)
        for contract in probes:
            self.assertIn("CONTRACT_EXACTNESS", self.validate(self.canonical, contract=contract))

    def test_05_coordinated_schema_registry_identity_drift_rejected(self):
        for key, value in [
            ("registry_version", "9.9.9"),
            ("campaign_authorized_starting_main", "0" * 40),
            ("mission_base_main", "1" * 40),
        ]:
            registry = copy.deepcopy(self.canonical); registry[key] = value
            schema = copy.deepcopy(self.schema); schema["properties"][key] = {"const": value}
            self.assertIn("REGISTRY_EXACTNESS", self.validate(registry, schema=schema))

    def test_06_schema_keyword_and_wrong_instance_bypasses_rejected(self):
        probes = [
            {"uniqueItems": True},
            {"type":"string","minProperties":0},
            {"type":"object","additionalProperties":False,"dependentSchemas":{"x":{}}},
            {"type":"object","additionalProperties":False,"propertyNames":True},
            {"type":"string","contentSchema":{}},
            {"type":"array","prefixItems":[{"type":"string"}]},
            {"type":["object","null"]},
            {"$ref":"https://example.invalid/schema.json"},
            {"description":"annotation only"},
        ]
        for probe in probes:
            schema = copy.deepcopy(self.schema); schema["properties"]["lane_status"] = probe
            self.assertTrue(MODULE.schema_issues(schema), probe)
            self.assertTrue(self.validate(self.canonical, schema=schema), probe)

    def test_07_wrong_type_documents_never_raise(self):
        for value in [None, [], "x", 5, {"registry_id":"x"}]:
            issues = self.validate(value)
            self.assertTrue(issues)
        schema = copy.deepcopy(self.schema); schema["properties"]["lane_status"] = {"$ref":"https://example.invalid/schema.json"}
        self.assertTrue(self.validate(self.canonical, schema=schema))

    def test_08_loader_duplicate_nonfinite_path_symlink_byte_depth_node_guards(self):
        with self.assertRaises(ValueError): MODULE.load(FIXTURES / "adversarial-duplicate-keys.yaml")
        with self.assertRaises(ValueError): MODULE.load(FIXTURES / "adversarial-duplicate-keys.json")
        with self.assertRaises(ValueError): MODULE.bounded(float("inf"))
        deep = []; cursor = deep
        for _ in range(MODULE.MAX_DEPTH + 2):
            child = []; cursor.append(child); cursor = child
        with self.assertRaises(ValueError): MODULE.bounded(deep)
        with self.assertRaises(ValueError): MODULE.bounded([0] * (MODULE.MAX_NODES + 1))
        with self.assertRaises((ValueError, FileNotFoundError)): MODULE.load(Path("/tmp/outside-ftrb01.yaml"))
        byte_path = FIXTURES / ".oversize.tmp"
        symlink_path = FIXTURES / ".symlink.tmp"
        try:
            byte_path.write_bytes(b"x" * (MODULE.MAX_BYTES + 1))
            with self.assertRaises(ValueError): MODULE.load(byte_path)
            os.symlink(FIXTURES / "README.md", symlink_path)
            with self.assertRaises(ValueError): MODULE.load(symlink_path)
        finally:
            byte_path.unlink(missing_ok=True); symlink_path.unlink(missing_ok=True)

    def test_09_exact_allowlist_and_runner_dispatch(self):
        self.assertEqual(MODULE.ALLOWLIST, MODULE.changed_paths())
        self.assertEqual(MODULE.ALLOWLIST, self.contract["validation"]["exact_changed_paths"])
        self.assertEqual(MODULE.ALLOWLIST, self.canonical["exact_changed_paths"])
        runner = (ROOT / "scripts/test.sh").read_text(encoding="utf-8")
        self.assertEqual(1, runner.count('ft_rb_01_media_validator="repository/data/validation/validate_ft_rb_01_rights_safe_media_readiness.py"'))
        self.assertEqual(1, runner.count('ft_rb_campaign_status_validator="repository/data/validation/validate_ft_rb_campaign_status.py"'))

    def test_10_live_archaeology_is_exact_and_temp_symlink_fails(self):
        self.assertEqual([], MODULE.archaeology_issues())
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "repository/assets").mkdir(parents=True)
            (root / "public/wp-content/uploads").mkdir(parents=True)
            os.symlink(root / "repository/assets", root / "assets")
            self.assertTrue(any("symlink" in issue or "root" in issue for issue in MODULE.archaeology_issues(root)))

    def test_11_all_dependency_trios_are_pinned_live(self):
        self.assertEqual(set(MODULE.DEPENDENCIES), set(MODULE.PINS))
        self.assertEqual(24, len(MODULE.PINS))
        for key, path in MODULE.DEPENDENCIES.items():
            self.assertEqual(MODULE.PINS[key], MODULE.digest(MODULE.load(ROOT / path)), key)

    def test_12_mode_crossing_rejected(self):
        self.assertIn("MODE_OR_CHRONOLOGY", self.validate(self.synthetic, synthetic=False))
        self.assertIn("MODE_OR_CHRONOLOGY", self.validate(self.canonical, synthetic=True))

    def test_13_new_package_does_not_persist_c009_stable_ids(self):
        owner = MODULE.load(MODULE.C009)
        leaf = owner["promotion"]["canonical_leaf"]
        prohibited = [leaf["source_pilot_id"], leaf["canonical_combination_id"], leaf["entity"]["entity_id"]]
        paths = [MODULE.CONTRACT, MODULE.SCHEMA, MODULE.REGISTRY, MODULE.SYNTHETIC, ROOT / "docs/FT_RB_01_RIGHTS_SAFE_MEDIA_READINESS_SCOPE_V1.0.md"]
        combined = "\n".join(path.read_text(encoding="utf-8") for path in paths)
        for value in prohibited:
            self.assertNotIn(value, combined)

    def test_14_direct_c009_collision_regression(self):
        path = ROOT / "repository/data/validation/validate_c009_first_commercial_slice_canonical_leaf_promotion.py"
        spec = importlib.util.spec_from_file_location("c009_for_ftrb01", path)
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module)
        contract = module.load_document(module.CONTRACT_PATH, "contract")
        schema = module.load_document(module.SCHEMA_PATH, "schema")
        registry = module.load_document(module.REGISTRY_PATH, "canonical")
        mutated = copy.deepcopy(registry)
        leaf = mutated["promotion"]["canonical_leaf"]
        leaf["entity"]["entity_id"] = leaf["canonical_combination_id"]
        codes = {issue.code for issue in module.validate_all(contract, schema, mutated, synthetic=False, allow_unpinned=True)}
        self.assertIn("STABLE_ID_COLLISION", codes)

    def test_15_validation_is_deterministic_and_offline(self):
        first = self.validate(self.canonical, worktree=True)
        second = self.validate(self.canonical, worktree=True)
        self.assertEqual(first, second)
        self.assertEqual([], first)


if __name__ == "__main__":
    unittest.main()
