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

import yaml

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "repository/data/validation/validate_ft_rb_02_inquiry_crm_flow_readiness.py"
SPEC = importlib.util.spec_from_file_location("ftrb02_validator", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
FIXTURES = ROOT / "tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness"


def documents() -> tuple[dict, dict, dict]:
    return MODULE.load_data(MODULE.CONTRACT), MODULE.load_data(MODULE.SCHEMA), MODULE.load_data(MODULE.REGISTRY)


def set_path(value: object, path: list[object], replacement: object) -> None:
    current = value
    for part in path[:-1]:
        current = current[part]  # type: ignore[index]
    current[path[-1]] = replacement  # type: ignore[index]


def cp(stdout: str = "") -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess(["git"], 0, stdout=stdout, stderr="")


class FTRB02InquiryCRMReadinessTests(unittest.TestCase):
    maxDiff = None

    def test_01_canonical_strict_pinned_positive(self) -> None:
        self.assertEqual(MODULE.validate_all(check_git=False), [])

    def test_02_synthetic_strict_pinned_positive_and_isolation(self) -> None:
        self.assertEqual(MODULE.validate_all(MODULE.SYNTHETIC, synthetic=True, check_git=False), [])
        canonical = MODULE.load_data(MODULE.REGISTRY)
        synthetic = MODULE.load_data(MODULE.SYNTHETIC)
        self.assertNotEqual(canonical["fixture_identity"], synthetic["fixture_identity"])
        self.assertNotEqual(canonical["status_as_of"], synthetic["status_as_of"])

    def test_03_semantic_pins_match_and_sentinel_fails_closed(self) -> None:
        contract, schema, canonical = documents()
        synthetic = MODULE.load_data(MODULE.SYNTHETIC)
        self.assertEqual(MODULE.DIGESTS["contract"], MODULE.digest(contract))
        self.assertEqual(MODULE.DIGESTS["schema"], MODULE.digest(schema))
        self.assertEqual(MODULE.DIGESTS["canonical"], MODULE.digest(canonical))
        self.assertEqual(MODULE.DIGESTS["synthetic"], MODULE.digest(synthetic))
        original = MODULE.DIGESTS["contract"]
        try:
            MODULE.DIGESTS["contract"] = "TO_BE_FINALIZED"
            self.assertIn("DIGEST_UNPINNED:contract", MODULE.validate_all(check_git=False))
        finally:
            MODULE.DIGESTS["contract"] = original

    def test_04_fixture_mode_crossing_rejected(self) -> None:
        contract, schema, registry = documents()
        registry["fixture_mode"] = "SYNTHETIC"
        issues = MODULE.validate_values(contract, schema, registry, allow_unpinned=True)
        self.assertIn("FIXTURE_MODE", issues)

    def test_05_contract_and_registry_key_order_exact(self) -> None:
        contract, schema, registry = documents()
        moved = copy.deepcopy(registry)
        moved["source"] = moved.pop("source")
        self.assertIn("REGISTRY_KEYS_OR_ORDER", MODULE.validate_values(contract, schema, moved, allow_unpinned=True))
        changed = copy.deepcopy(contract)
        changed["extra"] = False
        self.assertIn("CONTRACT_EXACTNESS", MODULE.validate_values(changed, schema, registry, allow_unpinned=True))

    def test_06_schema_is_closed_and_exact(self) -> None:
        _, schema, _ = documents()
        self.assertEqual(MODULE.schema_issues(schema), [])
        self.assertEqual(MODULE.digest(schema), MODULE.EXPECTED_SCHEMA_DIGEST)

    def test_07_schema_permissive_applicator_and_wrong_instance_attacks(self) -> None:
        _, schema, _ = documents()
        attacks = [
            {}, True, {"description": "annotation"}, {"type": ["object", "null"]},
            {"type": "object"}, {"type": "array"}, {"type": "string", "uniqueItems": True},
            {"type": "string", "minProperties": 0}, {"anyOf": [{"type": "object"}]},
            {"dependentSchemas": {"x": {}}}, {"propertyNames": True}, {"contentSchema": {}},
            {"$ref": "https://evil.invalid/schema"}, {"$ref": "#/x", "type": "object"},
        ]
        for attack in attacks:
            candidate = copy.deepcopy(schema)
            candidate["properties"]["source"] = attack
            self.assertTrue(MODULE.schema_issues(candidate), attack)

    def test_08_duplicate_yaml_and_json_rejected(self) -> None:
        for name in ("adversarial-duplicate-keys.yaml", "adversarial-duplicate-keys.json"):
            with self.assertRaises(ValueError):
                MODULE.load_data(FIXTURES / name)

    def test_09_nonfinite_yaml_and_json_rejected(self) -> None:
        with tempfile.TemporaryDirectory(dir=FIXTURES) as directory:
            yaml_path = Path(directory) / "nonfinite.yaml"
            json_path = Path(directory) / "nonfinite.json"
            yaml_path.write_text("value: .nan\n", encoding="utf-8")
            json_path.write_text('{"value": NaN}\n', encoding="utf-8")
            for path in (yaml_path, json_path):
                with self.assertRaises(ValueError):
                    MODULE.load_data(path)

    def test_10_depth_and_node_caps(self) -> None:
        value: dict[str, object] = {}
        cursor = value
        for _ in range(MODULE.MAX_DEPTH + 2):
            cursor["x"] = {}
            cursor = cursor["x"]  # type: ignore[assignment]
        with self.assertRaises(ValueError):
            MODULE.bounded(value)
        with self.assertRaises(ValueError):
            MODULE.bounded([None] * (MODULE.MAX_NODES + 1))

    def test_11_path_symlink_byte_and_utf8_guards(self) -> None:
        with tempfile.TemporaryDirectory(dir=FIXTURES) as directory:
            root = Path(directory)
            target = root / "target.yaml"
            target.write_text("value: ok\n", encoding="utf-8")
            link = root / "link.yaml"
            link.symlink_to(target)
            with self.assertRaises(ValueError):
                MODULE.load_data(link)
            invalid = root / "invalid.yaml"
            invalid.write_bytes(b"\xff")
            with self.assertRaises(UnicodeDecodeError):
                MODULE.load_data(invalid)
            large = root / "large.yaml"
            large.write_bytes(b"x" * (MODULE.MAX_BYTES + 1))
            with self.assertRaises(ValueError):
                MODULE.load_data(large)

    def test_12_remote_ref_fixture_rejected(self) -> None:
        remote = MODULE.load_data(FIXTURES / "adversarial-remote-ref-schema.json")
        permissive = MODULE.load_data(FIXTURES / "adversarial-permissive-schema.json")
        self.assertTrue(any(issue.startswith("REMOTE_SCHEMA_REF") for issue in MODULE.schema_issues(remote)))
        self.assertTrue(MODULE.schema_issues(permissive))

    def test_13_all_27_dependency_pins_match(self) -> None:
        contract, _, _ = documents()
        self.assertEqual(contract["dependencies"], MODULE.DEPENDENCIES)
        self.assertEqual(contract["dependency_pins"], MODULE.PINS)
        self.assertEqual(len(MODULE.PINS), 27)
        for key, relative in MODULE.DEPENDENCIES.items():
            self.assertEqual(MODULE.digest(MODULE.load_data(ROOT / relative)), MODULE.PINS[key])

    def test_14_owner_paths_and_blobs_match(self) -> None:
        contract, _, _ = documents()
        self.assertEqual(contract["owner_documents"], MODULE.OWNER_FILES)
        self.assertEqual(contract["owner_document_pins"], MODULE.OWNER_PINS)
        for key, relative in MODULE.OWNER_FILES.items():
            self.assertEqual(MODULE.git_blob_oid(ROOT / relative), MODULE.OWNER_PINS[key])

    def test_15_execution_and_semantic_sources_are_property_scoped(self) -> None:
        registry = MODULE.load_data(MODULE.REGISTRY)
        policy = registry["source_policy"]
        self.assertFalse(policy["execution_authority_sets_field_semantics"])
        self.assertEqual([row["locator"].rsplit(":", 1)[-1] for row in policy["semantic_sources"]], [
            "1787398832.469889", "1787400933.711809", "1787401091.613509",
            "1787401125.584279", "1787401309.508679",
        ])
        self.assertTrue(all(row["author_id"] == "U0BNFS43TBL" and row["thread_complete"] and row["reply_count"] == 0 for row in policy["semantic_sources"]))

    def test_16_city_reconciliation_is_optional_conditional(self) -> None:
        registry = MODULE.load_data(MODULE.REGISTRY)
        city = next(row for row in registry["customer_form"]["fields"] if row["field_id"] == "city")
        self.assertEqual(city["requiredness"], "OPTIONAL_CONDITIONAL")
        self.assertFalse(city["unconditional_requirement"] or city["absence_blocks_submission"] or city["routing_or_supply_inference_authority"])
        self.assertEqual(registry["city_reconciliation"]["effective_value"], "OPTIONAL_CONDITIONAL")

    def test_17_form_fields_and_source_tokens_are_exact(self) -> None:
        fields = MODULE.load_data(MODULE.REGISTRY)["customer_form"]["fields"]
        by_id = {row["field_id"]: row for row in fields}
        self.assertEqual(list(by_id), ["name", "mobile", "inquiry_type", "city", "quantity_or_approximate_need", "notes", "product_context"])
        self.assertEqual(by_id["inquiry_type"]["values"], ["PRICE", "STOCK_CHECK", "CONSULTATION"])
        self.assertTrue(by_id["inquiry_type"]["intent_only"])

    def test_18_product_context_roles_are_unpopulated_and_read_only(self) -> None:
        fields = MODULE.load_data(MODULE.REGISTRY)["customer_form"]["fields"]
        product = next(row for row in fields if row["field_id"] == "product_context")
        self.assertEqual(product["capture"], "SYSTEM_AUTO_ATTACHED")
        self.assertFalse(product["customer_reentry"] or product["value_population_performed"] or product["absent_or_deferred_values_may_be_inferred"])
        self.assertEqual(len(product["future_role_fields"]), 11)

    def test_19_future_payload_contract_creates_no_record(self) -> None:
        payload = MODULE.load_data(MODULE.REGISTRY)["future_payload_contract"]
        self.assertFalse(payload["record_creation_performed"])
        by_id = {row["field_id"]: row for row in payload["future_fields"]}
        self.assertEqual(by_id["source_channel"]["future_constant"], "website")
        self.assertEqual(by_id["source_page_path"]["capture_rule"], "PATH_ONLY_NO_QUERY_FRAGMENT_OR_PII")
        self.assertIn("consent_timestamp", by_id)
        self.assertEqual(by_id["payload_schema_version_reference"]["current_state"], "MISSING_AUTHORITY_INPUT")
        self.assertTrue(by_id["optional_quantity_unit"]["unknown_unit_must_remain_unknown"])

    def test_20_readiness_ceiling_remains_unmet(self) -> None:
        readiness = MODULE.load_data(MODULE.REGISTRY)["readiness"]
        self.assertEqual(readiness["repository_package_state"], "REPOSITORY_READY")
        self.assertEqual(readiness["readiness_classification"], "REPOSITORY_READY")
        self.assertEqual(readiness["workflow_status"], "BLOCKED_EXTERNAL_INPUT")
        self.assertEqual(readiness["prerequisite_state"], "UNMET")
        self.assertEqual(readiness["gate_transition"], "NONE")

    def test_21_gate_and_c002_snapshots_are_exact(self) -> None:
        registry = MODULE.load_data(MODULE.REGISTRY)
        self.assertEqual(registry["gate_snapshot"], {
            "eligible": False, "met_count": 5, "unmet_count": 7, "total": 12,
            "blockers": ["RIGHTS_SAFE_MEDIA_READY", "INQUIRY_CRM_FLOW_READY", "SECURITY_PRIVACY_GATE_READY", "SEO_INDEXING_GATE_READY", "MOBILE_PERFORMANCE_GATE_READY", "STAGING_ACCEPTANCE_PASS", "PRODUCTION_FOUNDER_GO"],
        })
        self.assertEqual(registry["c002_snapshot"]["readiness"], "6/9 / NOT_READY")
        self.assertFalse(registry["c002_snapshot"]["founder_selection_ready"])
        self.assertEqual(registry["c002_snapshot"]["candidate_count"], 0)

    def test_22_inquiry_and_commerce_planes_are_separate(self) -> None:
        registry = MODULE.load_data(MODULE.REGISTRY)
        self.assertFalse(registry["inquiry_record_policy"]["inquiry_is_quote_reservation_order_or_payment"])
        planes = registry["state_planes"]
        self.assertEqual(len({row["owner"] for row in planes.values()}), len(planes))
        self.assertEqual(planes["quotation"]["implementation_state"], "NOT_AUTHORIZED")

    def test_23_lead_prefix_and_terminal_alternatives(self) -> None:
        lead = MODULE.load_data(MODULE.REGISTRY)["lead_stage_vocabulary"]
        self.assertEqual(lead["ordered_prefix"], ["NEW", "CONTACTED", "QUALIFIED", "SUPPLY_CHECK", "QUOTE_PREPARED"])
        self.assertEqual(lead["terminal_outcomes"], ["WON", "LOST", "CLOSED"])
        self.assertEqual(lead["repository_workflow_direction"], "FOUNDER_APPROVED")
        self.assertFalse(lead["automatic_transition"] or lead["quote_prepared_creates_quote_or_value"] or lead["public_response_sla_created"])
        self.assertTrue(lead["missed_lead_visibility_required"])
        self.assertFalse(lead["qualified_requirements"]["unit_may_be_guessed"])
        self.assertTrue(lead["contacted_requirements"]["customer_provided_corrections_only"])
        self.assertEqual(set(lead["terminal_meanings"]), {"WON", "LOST", "CLOSED"})
        self.assertEqual(len(lead["minimum_operator_screen_roles"]), 12)

    def test_24_supply_check_is_noncanonical(self) -> None:
        supply = MODULE.load_data(MODULE.REGISTRY)["supply_check_policy"]
        self.assertEqual(supply["states"], ["CHECK_REQUIRED", "CHECKED_CAN_PROCEED", "CHECKED_CANNOT_PROCEED"])
        self.assertTrue(supply["internal_operational_context_only"])
        self.assertFalse(supply["canonical_or_public_availability_effect"] or supply["stock_eta_sla_supplier_truth_effect"])

    def test_25_form_security_is_requirement_only(self) -> None:
        security = MODULE.load_data(MODULE.REGISTRY)["form_security_requirements"]
        self.assertEqual((security["implementation_state"], security["verification_state"], security["staging_verification_state"]), ("NOT_IMPLEMENTED", "NOT_VERIFIED", "NOT_RUN"))
        for key in ("https_required", "server_side_validation_authoritative", "csrf_or_nonce_required", "duplicate_submit_suppression_required", "safe_retry_and_contact_fallback_required"):
            self.assertTrue(security[key])

    def test_26_privacy_consent_and_pii_boundary(self) -> None:
        privacy = MODULE.load_data(MODULE.REGISTRY)["consent_privacy"]
        self.assertEqual(privacy["marketing_consent"], "SEPARATE_OPTIONAL_UNPRECHECKED")
        self.assertEqual(privacy["pii_in_url_log_analytics_fixture"], "PROHIBITED")
        self.assertEqual(privacy["exact_approved_text_version_legal_basis_state"], "MISSING_AUTHORITY_INPUT")

    def test_27_candidate_only_dedupe_and_safe_delivery(self) -> None:
        policy = MODULE.load_data(MODULE.REGISTRY)["deduplication_delivery"]
        self.assertTrue(policy["matching_creates_review_candidates_only"] and policy["idempotency_and_replay_control_required"] and policy["safe_retry_required"])
        self.assertEqual(policy["automatic_merge_prohibited_identifiers"], ["name", "mobile", "email", "organization", "cookie", "device", "shared_identifier"])

    def test_28_analytics_owns_no_policy_or_product_truth(self) -> None:
        analytics = MODULE.load_data(MODULE.REGISTRY)["analytics_boundary"]
        self.assertEqual((analytics["state"], analytics["implementation_state"], analytics["events_emitted"]), ("REPOSITORY_REQUIREMENT_ONLY", "NOT_IMPLEMENTED", False))
        self.assertEqual(len(analytics["core_event_vocabulary"]), 16)
        self.assertEqual(len(analytics["primary_kpi_vocabulary"]), 10)
        self.assertEqual(len(analytics["secondary_diagnostic_vocabulary"]), 6)
        self.assertEqual(len(analytics["non_success_alone_metrics"]), 5)
        self.assertEqual(len(analytics["minimum_payload_roles"]), 9)
        self.assertEqual(analytics["review_cadence"], {"first_launch_week": "DAILY_OPERATIONAL_CHECK", "stabilization": "WEEKLY_FUNNEL_REVIEW", "later": "MONTHLY_TREND_REVIEW"})
        self.assertFalse(analytics["analytics_owns_policy_product_or_commercial_truth"])
        self.assertEqual(analytics["sensitive_pii_when_lead_id_suffices"], "PROHIBITED")
        self.assertEqual(analytics["fabricated_benchmark_revenue_or_conversion_result"], "PROHIBITED")

    def test_29_every_no_go_boolean_is_false(self) -> None:
        no_go = MODULE.load_data(MODULE.REGISTRY)["no_claim_boundaries"]
        self.assertEqual(len(no_go), 15)
        self.assertTrue(all(value is False for value in no_go.values()))

    def test_30_c009_owner_and_stable_id_leakage(self) -> None:
        issues, ids = MODULE.c009_owner_issues()
        self.assertEqual(issues, [])
        self.assertEqual(len(ids), 3)
        self.assertEqual(MODULE.leakage_issues(ids), [])

    def test_31_mutation_manifest_has_200_unique_dispatched_cases(self) -> None:
        manifest = MODULE.load_data(FIXTURES / "mutation-cases.json")
        self.assertEqual(manifest["case_count"], 200)
        self.assertEqual(len(manifest["cases"]), 200)
        self.assertEqual(len({row["id"] for row in manifest["cases"]}), 200)
        self.assertEqual([row["id"] for row in manifest["cases"]], [f"M{index:03d}" for index in range(1, 201)])
        self.assertTrue(all(row["op"] == "replace" and isinstance(row["expected_issue"], str) for row in manifest["cases"]))
        contract, schema, registry = documents()
        for row in manifest["cases"]:
            mutated_contract, mutated_schema, mutated_registry = copy.deepcopy(contract), copy.deepcopy(schema), copy.deepcopy(registry)
            targets = {"contract": mutated_contract, "schema": mutated_schema, "registry": mutated_registry}
            target = targets[row["target"]]
            set_path(target, row["path"], row["value"])
            issues = MODULE.validate_values(
                mutated_contract,
                mutated_schema,
                mutated_registry,
                allow_unpinned=True,
                check_protected=False,
                check_surfaces=False,
            )
            self.assertIn(row["expected_issue"], issues, row["id"])

    def test_32_local_allowlist_base_shape_and_path_modes(self) -> None:
        for base in MODULE.APPROVED_BASES:
            self.assertTrue(MODULE.base_available(base))
            self.assertEqual(MODULE.base_shape_issues(base), [])
        self.assertEqual(MODULE.approved_base_for_head(), MODULE.APPROVED_SUCCESSOR_BASE)
        self.assertEqual(MODULE.changed_paths(MODULE.APPROVED_SUCCESSOR_BASE), MODULE.ALLOWLIST)
        self.assertEqual(
            MODULE.changed_paths(MODULE.ORIGINAL_MISSION_BASE),
            sorted(MODULE.ALLOWLIST + ["tests/test_ft_rb_01_rights_safe_media_readiness.py"]),
        )
        self.assertEqual(MODULE.regular_path_issues(), [])

    def test_33_runner_dispatch_is_exact_for_pin_state(self) -> None:
        self.assertEqual(MODULE.runner_issues(), [])
        text = (ROOT / "scripts/test.sh").read_text()
        self.assertEqual(text.count("ft_rb_02_inquiry_validator="), 1)
        self.assertEqual(text.count("tests.test_ft_rb_02_inquiry_crm_flow_readiness"), 1)

    def test_34_deterministic_sorted_offline_validation(self) -> None:
        first = MODULE.validate_all(allow_unpinned=True, check_git=False)
        second = MODULE.validate_all(allow_unpinned=True, check_git=False)
        self.assertEqual(first, second)
        self.assertEqual(first, sorted(set(first)))

    def test_35_raw_commit_parser_rejects_malformed_headers(self) -> None:
        tree, p1, p2 = "a" * 40, "b" * 40, "c" * 40
        self.assertEqual(MODULE.parse_raw_commit(f"tree {tree}\nparent {p1}\nparent {p2}\nauthor x\n\nmsg"), (tree, [p1, p2]))
        for raw in (f"parent {p1}\ntree {tree}\n\nmsg", f"tree {tree}\nauthor x\nparent {p1}\n\nmsg", f"tree {tree}\nparent {p1}\nparent {p2}\nparent {'d'*40}\n\nmsg"):
            with self.assertRaises(ValueError):
                MODULE.parse_raw_commit(raw)

    def _pr_event(self, base: str, head: str, branch: str, count: int) -> dict:
        repo = {"full_name": MODULE.REPOSITORY_FULL_NAME}
        return {"repository": repo, "pull_request": {"changed_files": count, "base": {"sha": base, "ref": "main", "repo": repo}, "head": {"sha": head, "ref": branch, "repo": repo}}}

    def _run_ci(self, event_name: str, event: dict, checkout: str, parents: list[str], *, tree: str = "d" * 40, clean: bool = True) -> list[str]:
        def fake_git(*args: str, **_kwargs: object) -> subprocess.CompletedProcess[str]:
            if args == ("rev-parse", "HEAD"):
                return cp(checkout + "\n")
            return cp("")
        with mock.patch.dict(os.environ, {"CI": "true", "GITHUB_ACTIONS": "true", "GITHUB_EVENT_NAME": event_name}, clear=False), \
             mock.patch.object(MODULE, "clean_checkout", return_value=clean), \
             mock.patch.object(MODULE, "load_event", return_value=event), \
             mock.patch.object(MODULE, "git", side_effect=fake_git), \
             mock.patch.object(MODULE, "raw_commit", return_value=(tree, parents)), \
             mock.patch.object(MODULE, "committed_tree_issues", return_value=[]), \
             mock.patch.object(MODULE, "regular_path_issues", return_value=[]):
            return MODULE.ci_context_issues()

    def test_36_shallow_direct_and_synthetic_pr_contexts(self) -> None:
        head = "e" * 40
        for base in MODULE.APPROVED_BASES:
            event = self._pr_event(base, head, MODULE.BRANCH, len(MODULE.ALLOWLIST))
            self.assertEqual(self._run_ci("pull_request", event, head, []), [])
            merge = "f" * 40
            self.assertEqual(self._run_ci("pull_request", event, merge, [base, head]), [])

    def test_37_exact_merge_push_and_future_integrated_contexts(self) -> None:
        source, merge, tree = "e" * 40, "f" * 40, "d" * 40
        repo = {"full_name": MODULE.REPOSITORY_FULL_NAME}
        for base in MODULE.APPROVED_BASES:
            event = {"repository": repo, "ref": "refs/heads/main", "before": base, "after": merge, "created": False, "deleted": False, "forced": False,
                     "commits": [{"id": source, "tree_id": "c" * 40, "distinct": True}, {"id": merge, "tree_id": tree, "distinct": True}],
                     "head_commit": {"id": merge, "tree_id": tree}}
            self.assertEqual(self._run_ci("push", event, merge, [base, source], tree=tree), [])
        before, later = "1" * 40, "2" * 40
        future = {"repository": repo, "ref": "refs/heads/main", "before": before, "after": later, "created": False, "deleted": False, "forced": False,
                  "commits": [{"id": later, "tree_id": tree, "distinct": True}], "head_commit": {"id": later, "tree_id": tree}}
        self.assertEqual(self._run_ci("push", future, later, [before], tree=tree), [])

    def test_38_ci_event_scope_adversaries_fail(self) -> None:
        head = "e" * 40
        event = self._pr_event(MODULE.APPROVED_SUCCESSOR_BASE, head, MODULE.BRANCH, len(MODULE.ALLOWLIST))
        attacks = []
        wrong_repo = copy.deepcopy(event); wrong_repo["pull_request"]["head"]["repo"]["full_name"] = "fork/example"; attacks.append(wrong_repo)
        wrong_base = copy.deepcopy(event); wrong_base["pull_request"]["base"]["sha"] = "a" * 40; attacks.append(wrong_base)
        malformed_base = copy.deepcopy(event); malformed_base["pull_request"]["base"]["sha"] = "not-an-oid"; attacks.append(malformed_base)
        malformed_head = copy.deepcopy(event); malformed_head["pull_request"]["head"]["sha"] = "not-an-oid"; attacks.append(malformed_head)
        wrong_branch = copy.deepcopy(event); wrong_branch["pull_request"]["head"]["ref"] = "codex/unapproved"; attacks.append(wrong_branch)
        wrong_ref = copy.deepcopy(event); wrong_ref["pull_request"]["base"]["ref"] = "release"; attacks.append(wrong_ref)
        wrong_count = copy.deepcopy(event); wrong_count["pull_request"]["changed_files"] = 13; attacks.append(wrong_count)
        malformed_metadata = copy.deepcopy(event); malformed_metadata["pull_request"]["changed_files"] = "14"; attacks.append(malformed_metadata)
        missing_head = copy.deepcopy(event); del missing_head["pull_request"]["head"]; attacks.append(missing_head)
        for attack in attacks:
            self.assertTrue(self._run_ci("pull_request", attack, head, []), attack)
        merge = "f" * 40
        self.assertTrue(self._run_ci("pull_request", event, merge, [MODULE.ORIGINAL_MISSION_BASE, head]))
        self.assertTrue(self._run_ci("pull_request", event, head, [], clean=False))

    def test_39_cli_has_no_git_bypass_and_binds_registry_mode(self) -> None:
        skipped = subprocess.run([sys.executable, str(MODULE.VALIDATOR_PATH if hasattr(MODULE, "VALIDATOR_PATH") else VALIDATOR_PATH), "--skip-git"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(skipped.returncode, 2)
        with tempfile.TemporaryDirectory(dir=FIXTURES) as directory:
            custom = Path(directory) / "custom.yaml"
            custom.write_text(MODULE.REGISTRY.read_text(encoding="utf-8"), encoding="utf-8")
            result = subprocess.run([sys.executable, str(VALIDATOR_PATH), "--registry", str(custom), "--allow-unpinned"], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout.strip(), "CLI_REGISTRY_PATH")
            link = Path(directory) / "canonical-link.yaml"
            link.symlink_to(MODULE.REGISTRY)
            linked = subprocess.run([sys.executable, str(VALIDATOR_PATH), "--registry", str(link), "--allow-unpinned"], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(linked.returncode, 1)
            self.assertEqual(linked.stdout.strip(), "CLI_REGISTRY_PATH")

    def test_40_runner_rejects_any_unrelated_injection(self) -> None:
        original = MODULE.safe_file

        def injected(path: Path) -> bytes:
            raw = original(path)
            if path == ROOT / "scripts/test.sh":
                return raw + b"# unauthorized extra runner behavior\n"
            return raw

        with mock.patch.object(MODULE, "safe_file", side_effect=injected):
            issues = MODULE.runner_issues()
        self.assertIn("RUNNER:exact_blob", issues)
        self.assertIn("RUNNER:exact_transform", issues)

    def test_41_generic_stable_ids_and_international_mobiles_rejected(self) -> None:
        stable = ("pi" + "lot") + ":aaaaaaaaaaaa"
        combination = ("pc" + "omb") + ":bbbbbbbbbbbb"
        leaf = ("prd" + ":sku") + ":cccccccccccc"
        mobile_a = "+" + "98" + "9121234567"
        mobile_b = "00" + "98" + "9121234567"
        with mock.patch.object(MODULE, "BASE_ABSENT_PATHS", ["synthetic-surface.txt"]), \
             mock.patch.object(MODULE, "safe_file", return_value=(" ".join((stable, combination, leaf, mobile_a, mobile_b))).encode()):
            issues = MODULE.leakage_issues(set())
        self.assertIn("STABLE_ID_PATTERN:synthetic-surface.txt", issues)
        self.assertIn("PII_SURFACE:international_iranian_mobile:synthetic-surface.txt", issues)

    def test_42_source_scope_and_procedural_restart_are_exact(self) -> None:
        policy = MODULE.load_data(MODULE.REGISTRY)["source_policy"]
        self.assertEqual(policy["semantic_sources"][-1]["property_scope"], "PRIVACY_MINIMIZATION_CONSENT_FORM_SECURITY_AND_STAGING_ACCEPTANCE_REQUIREMENTS")
        restart = policy["procedural_restart_evidence"]
        self.assertEqual(
            (restart["predecessor_pr"], restart["predecessor_merge_sha"], restart["post_merge_ci_run"]),
            (53, MODULE.ORIGINAL_MISSION_BASE, 32665124526),
        )
        self.assertFalse(restart["sets_field_semantics"])

    def test_43_privacy_controls_all_optional_and_system_fields(self) -> None:
        registry = MODULE.load_data(MODULE.REGISTRY)
        fields = {row["field_id"]: row for row in registry["customer_form"]["fields"]}
        for field_id in ("quantity_or_approximate_need", "notes", "product_context"):
            self.assertEqual(fields[field_id]["authority_ts"], "1787401309.508679")
        privacy = registry["consent_privacy"]
        self.assertTrue(privacy["privacy_page_link_required"])
        self.assertEqual(privacy["privacy_page_minimum_content_state"], "REPOSITORY_REQUIREMENT_ONLY_EXTERNAL_INPUTS_MISSING")

    def test_44_exact_runner_blobs_are_bound_for_both_pin_states(self) -> None:
        self.assertEqual(MODULE.PROVISIONAL_RUNNER_BLOB, "db7cfa5f44072e43cb7fb0cf8b55d9c0ffa68c91")
        self.assertEqual(MODULE.PINNED_RUNNER_BLOB, "f8ebec998a8fb21e2468e5f5a762a8c122a4af46")
        text = (ROOT / "scripts/test.sh").read_text(encoding="utf-8")
        pinned = text.replace(" --allow-unpinned", "")
        raw = pinned.encode()
        expected = __import__("hashlib").sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
        self.assertEqual(expected, MODULE.PINNED_RUNNER_BLOB)

    def test_45_coordinated_contract_schema_registry_weakening_rejected(self) -> None:
        contract, schema, registry = documents()
        contract["privacy_policy"]["city_required"] = True
        schema["properties"]["customer_form"]["const"]["fields"][3]["requiredness"] = "REQUIRED"
        registry["customer_form"]["fields"][3]["requiredness"] = "REQUIRED"
        issues = MODULE.validate_values(contract, schema, registry, allow_unpinned=True)
        self.assertIn("CONTRACT_EXACTNESS", issues)
        self.assertIn("SCHEMA_EXACTNESS", issues)
        self.assertIn("REGISTRY_EXACTNESS:customer_form", issues)

    def test_46_approved_base_selection_is_exact_and_ambiguous_fails(self) -> None:
        unapproved = "a" * 40
        self.assertFalse(MODULE.base_available(unapproved))
        self.assertEqual(MODULE.base_shape_issues(unapproved), ["BASE_SHAPE:unapproved"])
        with self.assertRaises(ValueError):
            MODULE.changed_paths(unapproved)

        def ambiguous_relation(_ancestor: str, descendant: str = "HEAD") -> bool:
            return descendant == "HEAD"

        with mock.patch.object(MODULE, "base_available", return_value=True), \
             mock.patch.object(MODULE, "is_ancestor", side_effect=ambiguous_relation):
            with self.assertRaises(RuntimeError):
                MODULE.approved_base_for_head()
        with mock.patch.object(MODULE, "base_available", return_value=False):
            with self.assertRaises(RuntimeError):
                MODULE.approved_base_for_head()

    def test_47_historical_and_successor_tree_proofs_are_exact_and_adversarial(self) -> None:
        self.assertEqual(
            MODULE.committed_tree_issues(MODULE.ORIGINAL_MISSION_BASE, "62f4036fb3fe93edb42b2e8b760507a217b5f295"),
            [],
        )
        self.assertEqual(MODULE.committed_tree_issues(MODULE.APPROVED_SUCCESSOR_BASE), [])
        self.assertEqual(MODULE.committed_tree_issues("a" * 40), ["TREE_PROOF:unapproved_base"])

        expected = MODULE.COMMITTED_TREE_PROOFS[MODULE.APPROVED_SUCCESSOR_BASE]
        entries = {
            path: ("100644", "blob", "a" * 40)
            for path in MODULE.BASE_ABSENT_PATHS
        }
        entries["scripts/test.sh"] = ("100755", "blob", MODULE.PINNED_RUNNER_BLOB)
        missing = dict(entries)
        missing.pop(MODULE.BASE_ABSENT_PATHS[0])
        with mock.patch.object(MODULE, "parse_tree", return_value=(*expected, missing)):
            self.assertIn(
                f"TREE_PROOF:new_entry:{MODULE.BASE_ABSENT_PATHS[0]}",
                MODULE.committed_tree_issues(MODULE.APPROVED_SUCCESSOR_BASE),
            )
        unexpected = ("b" * 64, expected[1] + 1, expected[2] + 1, entries)
        with mock.patch.object(MODULE, "parse_tree", return_value=unexpected):
            self.assertIn("TREE_PROOF:digest_or_count", MODULE.committed_tree_issues(MODULE.APPROVED_SUCCESSOR_BASE))

    def test_48_dirty_untracked_and_partial_ci_metadata_fail_closed(self) -> None:
        with mock.patch.object(MODULE, "git", return_value=cp("?? unexpected.txt\n")):
            self.assertFalse(MODULE.clean_checkout())
        head = "e" * 40
        event = self._pr_event(MODULE.APPROVED_SUCCESSOR_BASE, head, MODULE.BRANCH, len(MODULE.ALLOWLIST))
        malformed = copy.deepcopy(event)
        malformed["pull_request"]["base"]["repo"] = {"full_name": 1}
        self.assertTrue(self._run_ci("pull_request", malformed, head, []))
        for flags in (
            {"CI": "true", "GITHUB_ACTIONS": "false"},
            {"CI": "false", "GITHUB_ACTIONS": "true"},
        ):
            with mock.patch.dict(os.environ, flags, clear=False), \
                 mock.patch.object(MODULE, "clean_checkout", return_value=True):
                self.assertEqual(MODULE.git_context_issues(), ["CI_CONTEXT:environment_or_cleanliness"])
            environment = os.environ.copy()
            environment.update(flags)
            result = subprocess.run([sys.executable, str(VALIDATOR_PATH)], cwd=ROOT, capture_output=True, text=True, env=environment)
            self.assertEqual(result.returncode, 1)
            self.assertIn("CI_CONTEXT:environment_or_cleanliness", result.stdout.splitlines())

    def test_49_push_path_parent_and_metadata_adversaries_fail(self) -> None:
        source, merge, tree = "e" * 40, "f" * 40, "d" * 40
        base = MODULE.APPROVED_SUCCESSOR_BASE
        repo = {"full_name": MODULE.REPOSITORY_FULL_NAME}

        def event_with(added: list[str]) -> dict:
            return {
                "repository": repo,
                "ref": "refs/heads/main",
                "before": base,
                "after": merge,
                "created": False,
                "deleted": False,
                "forced": False,
                "commits": [
                    {"id": source, "tree_id": "c" * 40, "distinct": True, "added": added, "modified": [], "removed": []},
                    {"id": merge, "tree_id": tree, "distinct": True, "added": [], "modified": ["scripts/test.sh"], "removed": []},
                ],
                "head_commit": {"id": merge, "tree_id": tree},
            }

        exact = event_with(list(MODULE.BASE_ABSENT_PATHS))
        self.assertEqual(self._run_ci("push", exact, merge, [base, source], tree=tree), [])
        self.assertTrue(self._run_ci("push", exact, merge, [MODULE.ORIGINAL_MISSION_BASE, source], tree=tree))
        self.assertTrue(self._run_ci("push", event_with(list(MODULE.BASE_ABSENT_PATHS[:-1])), merge, [base, source], tree=tree))
        self.assertTrue(self._run_ci("push", event_with(list(MODULE.BASE_ABSENT_PATHS) + ["unexpected.txt"]), merge, [base, source], tree=tree))
        partial = event_with(list(MODULE.BASE_ABSENT_PATHS))
        del partial["commits"][0]["removed"]
        self.assertTrue(self._run_ci("push", partial, merge, [base, source], tree=tree))

    def test_50_successor_adaptation_preserves_semantic_freeze(self) -> None:
        registry = MODULE.load_data(MODULE.REGISTRY)
        self.assertEqual(
            (registry["readiness"]["prerequisite_state"], registry["readiness"]["repository_package_state"], registry["readiness"]["workflow_status"]),
            ("UNMET", "REPOSITORY_READY", "BLOCKED_EXTERNAL_INPUT"),
        )
        gate = registry["gate_snapshot"]
        self.assertEqual((gate["eligible"], gate["met_count"], gate["unmet_count"], gate["total"]), (False, 5, 7, 12))
        self.assertEqual(registry["c002_snapshot"]["readiness"], "6/9 / NOT_READY")
        self.assertFalse(registry["future_payload_contract"]["record_creation_performed"])
        self.assertTrue(all(value is False for value in registry["no_claim_boundaries"].values()))


if __name__ == "__main__":
    unittest.main()
