from __future__ import annotations

import copy
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

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


def repair_pr_event(head):
    return {
        "repository": {"full_name": MODULE.REPOSITORY_FULL_NAME},
        "pull_request": {
            "changed_files": len(MODULE.REPAIR_ALLOWLIST),
            "base": {"ref": "main", "sha": MODULE.REPAIR_BASE, "repo": {"full_name": MODULE.REPOSITORY_FULL_NAME}},
            "head": {"ref": MODULE.REPAIR_BRANCH, "sha": head, "repo": {"full_name": MODULE.REPOSITORY_FULL_NAME}},
        },
    }


def push_event(before, after, tree, *, added=None, modified=None, removed=None, include_paths=False):
    added = list(added or [])
    modified = list(modified or [])
    removed = list(removed or [])
    commit = {
        "id": after,
        "tree_id": tree,
        "distinct": True,
    }
    if include_paths:
        commit.update({"added": added, "modified": modified, "removed": removed})
    head_commit = dict(commit)
    head_commit.pop("distinct")
    return {
        "repository": {"full_name": MODULE.REPOSITORY_FULL_NAME},
        "ref": MODULE.MAIN_REF,
        "before": before,
        "after": after,
        "created": False,
        "deleted": False,
        "forced": False,
        "commits": [commit],
        "head_commit": head_commit,
    }


def repair_push_event(after, tree, source_parent, *, include_paths=False):
    event = push_event(MODULE.REPAIR_BASE, after, tree, modified=MODULE.REPAIR_ALLOWLIST, include_paths=include_paths)
    source = {
        "id": source_parent,
        "tree_id": "4" * 40,
        "distinct": True,
    }
    if include_paths:
        source.update({"added": [], "modified": list(MODULE.REPAIR_ALLOWLIST), "removed": []})
    event["commits"].insert(0, source)
    event["commits"][-1]["distinct"] = False
    return event


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
        mode, paths = MODULE.git_context()
        if mode == "repair":
            self.assertEqual(MODULE.REPAIR_ALLOWLIST, paths)
            if MODULE.base_available(MODULE.REPAIR_BASE):
                self.assertEqual([], MODULE.repair_shape_issues())
            else:
                self.assertEqual([], MODULE.repair_committed_shape_issues())
        elif mode == "integrated":
            self.assertFalse(set(paths) & set(MODULE.PROTECTED_INTEGRATED_PATHS))
        else:
            self.fail(f"unexpected FT-RB-01 Git context: {mode}")
        self.assertEqual(MODULE.ALLOWLIST, self.contract["validation"]["exact_changed_paths"])
        self.assertEqual(MODULE.ALLOWLIST, self.canonical["exact_changed_paths"])
        runner = (ROOT / "scripts/test.sh").read_text(encoding="utf-8")
        self.assertEqual(1, runner.count('ft_rb_01_media_validator="repository/data/validation/validate_ft_rb_01_rights_safe_media_readiness.py"'))
        self.assertEqual(1, runner.count('ft_rb_campaign_status_validator="repository/data/validation/validate_ft_rb_campaign_status.py"'))
        head = "1" * 40
        event = repair_pr_event(head)
        self.assertEqual(("repair", MODULE.REPAIR_ALLOWLIST), MODULE.pull_request_event_context(event, head, []))
        self.assertEqual(("repair", MODULE.REPAIR_ALLOWLIST), MODULE.pull_request_event_context(event, "2" * 40, [MODULE.REPAIR_BASE, head]))
        raw = f"tree {'3' * 40}\nparent {MODULE.REPAIR_BASE}\nparent {head}\nauthor A <a@example.invalid> 0 +0000\n\nmerge\n"
        self.assertEqual(("3" * 40, [MODULE.REPAIR_BASE, head]), MODULE.parse_raw_commit(raw))
        with self.assertRaises(ValueError):
            MODULE.parse_raw_commit_parents("parent not-an-oid\n\n")
        event["pull_request"]["changed_files"] = 3
        with self.assertRaises(RuntimeError):
            MODULE.pull_request_event_context(event, head, [])
        base_available = subprocess.run(["git","cat-file","-e",MODULE.ORIGINAL_MISSION_BASE], cwd=ROOT, capture_output=True).returncode == 0
        if base_available:
            self.assertEqual([], MODULE.base_shape_issues())

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

    def test_16_shallow_repair_pull_request_direct_and_synthetic(self):
        head = "1" * 40
        event = repair_pr_event(head)
        self.assertEqual(("repair", MODULE.REPAIR_ALLOWLIST), MODULE.pull_request_event_context(event, head, []))
        self.assertEqual(
            ("repair", MODULE.REPAIR_ALLOWLIST),
            MODULE.pull_request_event_context(event, "2" * 40, [MODULE.REPAIR_BASE, head]),
        )
        probes = []
        for path, value in [
            (("repository", "full_name"), "other/repository"),
            (("pull_request", "base", "ref"), "develop"),
            (("pull_request", "base", "sha"), "3" * 40),
            (("pull_request", "base", "repo", "full_name"), "fork/repository"),
            (("pull_request", "head", "ref"), "wrong-branch"),
            (("pull_request", "head", "sha"), "not-an-oid"),
            (("pull_request", "head", "repo", "full_name"), "fork/repository"),
            (("pull_request", "changed_files"), 1),
            (("pull_request", "changed_files"), 3),
        ]:
            probe = copy.deepcopy(event); target = probe
            for key in path[:-1]: target = target[key]
            target[path[-1]] = value; probes.append((probe, head, []))
        probes.extend([(event, "4" * 40, []), (event, "4" * 40, [head, MODULE.REPAIR_BASE])])
        for probe, checkout, parents in probes:
            with self.assertRaises(RuntimeError):
                MODULE.pull_request_event_context(probe, checkout, parents)

    def test_17_shallow_post_merge_push_exact_and_negative(self):
        after, tree, second_parent = "1" * 40, "2" * 40, "3" * 40
        event = repair_push_event(after, tree, second_parent)
        expected = ("repair", MODULE.REPAIR_ALLOWLIST)
        self.assertEqual(expected, MODULE.push_event_context(event, after, tree, [MODULE.REPAIR_BASE, second_parent]))
        event_with_paths = repair_push_event(after, tree, second_parent, include_paths=True)
        self.assertEqual(expected, MODULE.push_event_context(event_with_paths, after, tree, [MODULE.REPAIR_BASE, second_parent]))
        mutations = []
        for path, value in [
            (("repository", "full_name"), "wrong/repo"),
            (("ref",), "refs/heads/other"),
            (("before",), "bad"),
            (("after",), "4" * 40),
            (("created",), True),
            (("deleted",), True),
            (("forced",), True),
            (("head_commit", "tree_id"), "5" * 40),
            (("commits", 0, "id"), after),
            (("commits", 0, "distinct"), "yes"),
            (("commits", 1, "id"), "6" * 40),
            (("commits", 1, "tree_id"), "5" * 40),
        ]:
            probe = copy.deepcopy(event); target = probe
            for key in path[:-1]: target = target[key]
            target[path[-1]] = value; mutations.append((path, probe))
        for path, probe in mutations:
            with self.subTest(path=path):
                with self.assertRaises((RuntimeError, ValueError)):
                    MODULE.push_event_context(probe, after, tree, [MODULE.REPAIR_BASE, second_parent])
        with self.assertRaises(RuntimeError):
            MODULE.push_event_context(event, "4" * 40, tree, [MODULE.REPAIR_BASE, second_parent])
        for parents in [[], [MODULE.REPAIR_BASE], ["4" * 40, second_parent], [MODULE.REPAIR_BASE, second_parent, "5" * 40]]:
            with self.assertRaises(RuntimeError):
                MODULE.push_event_context(event, after, tree, parents)
        partial = repair_push_event(after, tree, second_parent)
        partial["commits"][0]["modified"] = list(MODULE.REPAIR_ALLOWLIST)
        with self.assertRaises(RuntimeError):
            MODULE.push_event_context(partial, after, tree, [MODULE.REPAIR_BASE, second_parent])
        extra = repair_push_event(after, tree, second_parent, include_paths=True)
        extra["commits"][0]["modified"].append("unexpected.txt")
        with self.assertRaises(RuntimeError):
            MODULE.push_event_context(extra, after, tree, [MODULE.REPAIR_BASE, second_parent])
        too_many = repair_push_event(after, tree, second_parent)
        too_many["commits"] = [
            {"id": f"{index:040x}", "tree_id": "4" * 40, "distinct": True}
            for index in range(1, MODULE.MAX_PUSH_COMMITS + 2)
        ]
        too_many["commits"][-1] = {"id": after, "tree_id": tree, "distinct": False}
        with self.assertRaises(RuntimeError):
            MODULE.push_event_context(too_many, after, tree, [MODULE.REPAIR_BASE, second_parent])

    def test_18_future_main_push_ignores_unrelated_lanes_but_protects_ft_rb_01(self):
        before, after, tree = "4" * 40, "5" * 40, "6" * 40
        event = push_event(before, after, tree, added=["docs/FUTURE_SCOPE.md"], modified=["scripts/test.sh"], include_paths=True)
        self.assertEqual(
            ("integrated", ["docs/FUTURE_SCOPE.md", "scripts/test.sh"]),
            MODULE.push_event_context(event, after, tree, [before, "7" * 40]),
        )
        protected = copy.deepcopy(event)
        protected["commits"][0]["modified"] = [MODULE.REPAIR_ALLOWLIST[0]]
        protected["head_commit"]["modified"] = [MODULE.REPAIR_ALLOWLIST[0]]
        with self.assertRaises(RuntimeError):
            MODULE.push_event_context(protected, after, tree, [before, "7" * 40])

    def test_19_event_loader_rejects_malformed_duplicate_nonfinite_and_symlink(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            malformed = root / "malformed.json"; malformed.write_text("{", encoding="utf-8")
            duplicate = root / "duplicate.json"; duplicate.write_text('{"ref":"a","ref":"b"}', encoding="utf-8")
            nonfinite = root / "nonfinite.json"; nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            valid = root / "valid.json"; valid.write_text('{"ref":"refs/heads/main"}', encoding="utf-8")
            link = root / "link.json"; os.symlink(valid, link)
            for path in [malformed, duplicate, nonfinite, link]:
                with self.assertRaises((ValueError, json.JSONDecodeError)):
                    MODULE.load_ci_event(path)

    def test_20_ci_dirty_untracked_and_non_ci_missing_history_fail_closed(self):
        ci_env = {
            "CI": "true",
            "GITHUB_ACTIONS": "true",
            "GITHUB_EVENT_NAME": "pull_request",
            "GITHUB_EVENT_PATH": "/does/not/matter.json",
        }
        with mock.patch.dict(os.environ, ci_env, clear=False), mock.patch.object(MODULE, "working_delta", return_value=(["dirty"], [])):
            with self.assertRaises(RuntimeError): MODULE.git_context()
        with mock.patch.dict(os.environ, ci_env, clear=False), mock.patch.object(MODULE, "working_delta", return_value=([], ["untracked"])):
            with self.assertRaises(RuntimeError): MODULE.git_context()
        with mock.patch.object(MODULE, "base_available", return_value=False):
            with self.assertRaises(RuntimeError): MODULE.local_context("unrelated-branch", [], [])

    def test_21_authorized_path_shape_rejects_missing_and_symlink(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            root = Path(temp)
            first, second = MODULE.REPAIR_ALLOWLIST
            first_path = root / first; first_path.parent.mkdir(parents=True); first_path.write_text("x", encoding="utf-8")
            self.assertIn(f"PATH_SHAPE:missing:{second}", MODULE.regular_path_issues(MODULE.REPAIR_ALLOWLIST, root))
            second_path = root / second; second_path.parent.mkdir(parents=True); os.symlink(first_path, second_path)
            self.assertIn(f"PATH_SHAPE:symlink:{second}", MODULE.regular_path_issues(MODULE.REPAIR_ALLOWLIST, root))

    def test_22_raw_commit_parser_rejects_tree_and_parent_ambiguity(self):
        tree, parent = "8" * 40, "9" * 40
        self.assertEqual((tree, [parent]), MODULE.parse_raw_commit(f"tree {tree}\nparent {parent}\n\nmessage"))
        probes = [
            "parent " + parent + "\n\n",
            "tree bad\n\n",
            f"tree {tree}\ntree {tree}\n\n",
            f"tree {tree}\nparent BAD\n\n",
            f"tree {tree}\nparent {parent}\nparent {parent}\nparent {parent}\n\n",
            f"tree {tree}\nauthor A <a@example.invalid> 0 +0000\nparent {parent}\n\n",
        ]
        for raw in probes:
            with self.assertRaises(ValueError): MODULE.parse_raw_commit(raw)

    def test_23_excluded_full_tree_manifest_exact_and_adversarial(self):
        raw = subprocess.run(
            ["git", "ls-tree", "-rz", "--full-tree", "HEAD"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        ).stdout
        digest, retained, total, entries = MODULE.parse_tree_manifest(raw, MODULE.REPAIR_ALLOWLIST)
        self.assertEqual(MODULE.REPAIR_BASE_EXCLUDED_TREE_DIGEST, digest)
        self.assertEqual(MODULE.REPAIR_BASE_RETAINED_TREE_ENTRIES, retained)
        self.assertEqual(MODULE.REPAIR_BASE_TOTAL_TREE_ENTRIES, total)
        for path, blob in MODULE.REPAIR_BASE_BLOBS.items():
            self.assertEqual(("100644", "blob"), entries[path][:2])
            self.assertNotEqual(blob, entries[path][2])
        if MODULE.base_available(MODULE.REPAIR_BASE):
            base_raw = subprocess.run(
                ["git", "ls-tree", "-rz", "--full-tree", MODULE.REPAIR_BASE],
                cwd=ROOT,
                check=True,
                capture_output=True,
            ).stdout
            _, _, _, base_entries = MODULE.parse_tree_manifest(base_raw, MODULE.REPAIR_ALLOWLIST)
            for path, blob in MODULE.REPAIR_BASE_BLOBS.items():
                self.assertEqual(("100644", "blob", blob), base_entries[path])
        with self.assertRaises(ValueError):
            MODULE.parse_tree_manifest(raw, list(reversed(MODULE.REPAIR_ALLOWLIST)))
        for malformed in [raw[:-1], raw + b"\0", b"bad\0"]:
            with self.assertRaises(ValueError):
                MODULE.parse_tree_manifest(malformed, MODULE.REPAIR_ALLOWLIST)
        first = raw.split(b"\0", 1)[0]
        changed = raw.replace(first, first.replace(b"100644", b"100755", 1), 1)
        changed_digest, _, _, _ = MODULE.parse_tree_manifest(changed, MODULE.REPAIR_ALLOWLIST)
        self.assertNotEqual(MODULE.REPAIR_BASE_EXCLUDED_TREE_DIGEST, changed_digest)

    def test_24_repair_tree_proof_rejects_unchanged_wrong_mode_and_third_path_drift(self):
        entries = {
            path: ("100644", "blob", ("b" if index == 0 else "c") * 40)
            for index, path in enumerate(MODULE.REPAIR_ALLOWLIST)
        }
        exact = (
            MODULE.REPAIR_BASE_EXCLUDED_TREE_DIGEST,
            MODULE.REPAIR_BASE_RETAINED_TREE_ENTRIES,
            MODULE.REPAIR_BASE_TOTAL_TREE_ENTRIES,
            entries,
        )
        with mock.patch.object(MODULE, "tree_manifest", return_value=exact):
            self.assertEqual([], MODULE.repair_excluded_tree_issues(require_changed_entries=True))
        unchanged = copy.deepcopy(entries)
        unchanged[MODULE.REPAIR_ALLOWLIST[0]] = ("100644", "blob", MODULE.REPAIR_BASE_BLOBS[MODULE.REPAIR_ALLOWLIST[0]])
        with mock.patch.object(MODULE, "tree_manifest", return_value=exact[:3] + (unchanged,)):
            self.assertTrue(MODULE.repair_excluded_tree_issues(require_changed_entries=True))
        wrong_mode = copy.deepcopy(entries)
        wrong_mode[MODULE.REPAIR_ALLOWLIST[1]] = ("100755", "blob", "c" * 40)
        with mock.patch.object(MODULE, "tree_manifest", return_value=exact[:3] + (wrong_mode,)):
            self.assertTrue(MODULE.repair_excluded_tree_issues(require_changed_entries=True))
        third_path_drift = ("0" * 64, exact[1], exact[2], entries)
        with mock.patch.object(MODULE, "tree_manifest", return_value=third_path_drift):
            self.assertIn("REPAIR_TREE_PROOF:digest", MODULE.repair_excluded_tree_issues(require_changed_entries=True))

    def test_25_git_context_end_to_end_shallow_pr_synthetic_and_push(self):
        head, checkout, tree, source_parent = "1" * 40, "2" * 40, "3" * 40, "4" * 40
        changed_entries = {
            path: ("100644", "blob", ("b" if index == 0 else "c") * 40)
            for index, path in enumerate(MODULE.REPAIR_ALLOWLIST)
        }
        tree_result = (
            MODULE.REPAIR_BASE_EXCLUDED_TREE_DIGEST,
            MODULE.REPAIR_BASE_RETAINED_TREE_ENTRIES,
            MODULE.REPAIR_BASE_TOTAL_TREE_ENTRIES,
            changed_entries,
        )
        contexts = [
            ("pull_request", repair_pr_event(head), head, tree, []),
            ("pull_request", repair_pr_event(head), checkout, tree, [MODULE.REPAIR_BASE, head]),
            ("push", repair_push_event(head, tree, source_parent), head, tree, [MODULE.REPAIR_BASE, source_parent]),
        ]
        for event_name, event, checkout_oid, tree_oid, parents in contexts:
            with self.subTest(event_name=event_name, checkout=checkout_oid):
                env = {
                    "CI": "true",
                    "GITHUB_ACTIONS": "true",
                    "GITHUB_EVENT_NAME": event_name,
                    "GITHUB_EVENT_PATH": "/absolute/event.json",
                }
                with (
                    mock.patch.dict(os.environ, env, clear=False),
                    mock.patch.object(MODULE, "working_delta", return_value=([], [])),
                    mock.patch.object(MODULE, "load_ci_event", return_value=event),
                    mock.patch.object(MODULE, "head_oid", return_value=checkout_oid),
                    mock.patch.object(MODULE, "raw_commit", return_value=(tree_oid, parents)),
                    mock.patch.object(MODULE, "tree_manifest", return_value=tree_result),
                    mock.patch.object(MODULE, "base_available", return_value=False),
                ):
                    self.assertEqual(("repair", MODULE.REPAIR_ALLOWLIST), MODULE.git_context())

    def test_26_original_integration_and_future_shallow_push_compatibility(self):
        original_event = push_event(
            MODULE.ORIGINAL_MISSION_BASE,
            MODULE.ORIGINAL_MERGE_SHA,
            "7" * 40,
            added=MODULE.BASE_ABSENT_PATHS,
            modified=["scripts/test.sh"],
            include_paths=True,
        )
        self.assertEqual(
            ("original", MODULE.ALLOWLIST),
            MODULE.push_event_context(
                original_event,
                MODULE.ORIGINAL_MERGE_SHA,
                "7" * 40,
                [MODULE.ORIGINAL_MISSION_BASE, MODULE.ORIGINAL_PR_HEAD],
            ),
        )
        original_without_paths = push_event(MODULE.ORIGINAL_MISSION_BASE, MODULE.ORIGINAL_MERGE_SHA, "7" * 40)
        self.assertEqual(
            ("original", MODULE.ALLOWLIST),
            MODULE.push_event_context(
                original_without_paths,
                MODULE.ORIGINAL_MERGE_SHA,
                "7" * 40,
                [MODULE.ORIGINAL_MISSION_BASE, MODULE.ORIGINAL_PR_HEAD],
            ),
        )
        with self.assertRaises(RuntimeError):
            MODULE.push_event_context(
                original_event,
                MODULE.ORIGINAL_MERGE_SHA,
                "7" * 40,
                [MODULE.ORIGINAL_MISSION_BASE, "8" * 40],
            )

        future_before, future_after, future_tree = "9" * 40, "a" * 40, "b" * 40
        future_event = push_event(future_before, future_after, future_tree)
        env = {
            "CI": "true",
            "GITHUB_ACTIONS": "true",
            "GITHUB_EVENT_NAME": "push",
            "GITHUB_EVENT_PATH": "/absolute/event.json",
        }
        with (
            mock.patch.dict(os.environ, env, clear=False),
            mock.patch.object(MODULE, "working_delta", return_value=([], [])),
            mock.patch.object(MODULE, "load_ci_event", return_value=future_event),
            mock.patch.object(MODULE, "head_oid", return_value=future_after),
            mock.patch.object(MODULE, "raw_commit", return_value=(future_tree, [future_before])),
            mock.patch.object(MODULE, "base_available", return_value=False),
        ):
            self.assertEqual(("integrated", []), MODULE.git_context())


if __name__ == "__main__":
    unittest.main()
