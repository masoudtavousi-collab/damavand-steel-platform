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
        available = [base for base in MODULE.APPROVED_BASES if MODULE.base_available(base)]
        if available:
            for base in available:
                self.assertEqual(MODULE.base_shape_issues(base), [])
            self.assertEqual(MODULE.approved_base_for_head(), MODULE.APPROVED_SUCCESSOR_BASE)
            self.assertEqual(MODULE.changed_paths(MODULE.APPROVED_SUCCESSOR_BASE), MODULE.ALLOWLIST)
            if MODULE.ORIGINAL_MISSION_BASE in available:
                self.assertEqual(
                    MODULE.changed_paths(MODULE.ORIGINAL_MISSION_BASE),
                    sorted(MODULE.ALLOWLIST + ["tests/test_ft_rb_01_rights_safe_media_readiness.py"]),
                )
        else:
            self.assertEqual((os.environ.get("CI"), os.environ.get("GITHUB_ACTIONS")), ("true", "true"))

        def approved_relation(ancestor: str, descendant: str = "HEAD") -> bool:
            if descendant == "HEAD":
                return ancestor in MODULE.APPROVED_BASES
            return ancestor == MODULE.ORIGINAL_MISSION_BASE and descendant == MODULE.APPROVED_SUCCESSOR_BASE

        with mock.patch.object(MODULE, "base_available", return_value=True), \
             mock.patch.object(MODULE, "is_ancestor", side_effect=approved_relation):
            self.assertEqual(MODULE.approved_base_for_head(), MODULE.APPROVED_SUCCESSOR_BASE)
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

    def _run_ci(
        self,
        event_name: str,
        event: dict,
        checkout: str,
        parents: list[str],
        *,
        tree: str = "d" * 40,
        clean: bool = True,
        tree_issues: list[str] | None = None,
        repair_issues: list[str] | None = None,
        protected_issues: list[str] | None = None,
        regular_issues: list[str] | None = None,
        direct_base_available: bool = True,
        direct_ancestor: bool = True,
    ) -> list[str]:
        def fake_git(*args: str, **_kwargs: object) -> subprocess.CompletedProcess[str]:
            if args == ("rev-parse", "HEAD"):
                return cp(checkout + "\n")
            return cp("")
        with mock.patch.dict(os.environ, {"CI": "true", "GITHUB_ACTIONS": "true", "GITHUB_EVENT_NAME": event_name}, clear=False), \
             mock.patch.object(MODULE, "clean_checkout", return_value=clean), \
             mock.patch.object(MODULE, "load_event", return_value=event), \
             mock.patch.object(MODULE, "git", side_effect=fake_git), \
             mock.patch.object(MODULE, "raw_commit", return_value=(tree, parents)), \
             mock.patch.object(MODULE, "committed_tree_issues", return_value=tree_issues or []), \
             mock.patch.object(MODULE, "repair_delta_issues", return_value=repair_issues or []), \
             mock.patch.object(MODULE, "successor_protected_issues", return_value=protected_issues or []), \
             mock.patch.object(MODULE, "commit_available", return_value=direct_base_available), \
             mock.patch.object(MODULE, "is_ancestor", return_value=direct_ancestor), \
             mock.patch.object(MODULE, "regular_path_issues", return_value=regular_issues or []):
            return MODULE.ci_context_issues()

    def test_36_shallow_direct_and_synthetic_pr_contexts(self) -> None:
        head = "e" * 40
        for base in MODULE.APPROVED_BASES:
            event = self._pr_event(base, head, MODULE.BRANCH, len(MODULE.ALLOWLIST))
            self.assertEqual(self._run_ci("pull_request", event, head, []), [])
            self.assertTrue(self._run_ci("pull_request", event, head, [], direct_base_available=False))
            self.assertTrue(self._run_ci("pull_request", event, head, [], direct_ancestor=False))
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
                  "commits": [{"id": later, "tree_id": tree, "distinct": True, "added": ["repository-index.txt"], "modified": [], "removed": []}],
                  "head_commit": {"id": later, "tree_id": tree}}
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
        current = original(ROOT / "scripts/test.sh").decode("utf-8")
        block = (
            '# FT-RB-02 pre-pin Inquiry/CRM readiness validation and focused/adversarial dispatch.\n'
            'ft_rb_02_inquiry_validator="repository/data/validation/validate_ft_rb_02_inquiry_crm_flow_readiness.py"\n'
            '"$python" "$ft_rb_02_inquiry_validator"\n'
            '"$python" "$ft_rb_02_inquiry_validator" --registry tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/valid-synthetic.yaml --synthetic\n'
            '"$python" -B -m unittest tests.test_ft_rb_02_inquiry_crm_flow_readiness\n\n'
        )
        base_text = current.replace(block, "", 1)
        self.assertNotEqual(base_text, current)

        def injected(path: Path) -> bytes:
            raw = original(path)
            if path == ROOT / "scripts/test.sh":
                return raw + b"# unauthorized extra runner behavior\n"
            return raw

        with mock.patch.object(MODULE, "safe_file", side_effect=injected), \
             mock.patch.object(MODULE, "base_available", side_effect=lambda base: base == MODULE.APPROVED_SUCCESSOR_BASE), \
             mock.patch.object(MODULE, "approved_base_for_head", return_value=MODULE.APPROVED_SUCCESSOR_BASE), \
             mock.patch.object(MODULE, "git", return_value=cp(base_text)):
            issues = MODULE.runner_issues(MODULE.HISTORICAL_CONTEXT)
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
        historical_head = "62f4036fb3fe93edb42b2e8b760507a217b5f295"
        historical_available = MODULE.git("cat-file", "-e", f"{historical_head}^{{commit}}", check=False).returncode == 0
        if historical_available:
            self.assertEqual(MODULE.committed_tree_issues(MODULE.ORIGINAL_MISSION_BASE, historical_head), [])
        else:
            self.assertEqual((os.environ.get("CI"), os.environ.get("GITHUB_ACTIONS")), ("true", "true"))
        self.assertEqual(MODULE.committed_tree_issues(MODULE.APPROVED_SUCCESSOR_BASE), [])
        self.assertEqual(MODULE.committed_tree_issues("a" * 40), ["TREE_PROOF:unapproved_base"])

        entries = {
            path: ("100644", "blob", "a" * 40)
            for path in MODULE.BASE_ABSENT_PATHS
        }
        entries["scripts/test.sh"] = ("100755", "blob", MODULE.PINNED_RUNNER_BLOB)
        for base, expected in MODULE.COMMITTED_TREE_PROOFS.items():
            with mock.patch.object(MODULE, "parse_tree", return_value=(*expected, entries)):
                self.assertEqual(MODULE.committed_tree_issues(base), [])

        expected = MODULE.COMMITTED_TREE_PROOFS[MODULE.APPROVED_SUCCESSOR_BASE]
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

    def test_51_context_classifier_is_generic_and_fail_closed(self) -> None:
        for base in MODULE.APPROVED_BASES:
            self.assertEqual(MODULE.classify_pr_context(base, MODULE.BRANCH), MODULE.HISTORICAL_CONTEXT)
        for base, branch in MODULE.AUTHORIZED_REPAIR_CONTEXTS.items():
            self.assertEqual(MODULE.classify_pr_context(base, branch), MODULE.REPAIR_CONTEXT)
        generic_pairs = [
            ("a" * 40, "codex/repository-index-refresh"),
            ("b" * 40, "automation/quality-ledger-update"),
        ]
        for base, branch in generic_pairs:
            self.assertNotIn(base, MODULE.APPROVED_BASES + tuple(MODULE.AUTHORIZED_REPAIR_CONTEXTS))
            self.assertEqual(MODULE.classify_pr_context(base, branch), MODULE.SUCCESSOR_CONTEXT)
        ambiguous = [
            (MODULE.APPROVED_SUCCESSOR_BASE, "codex/repository-index-refresh"),
            ("a" * 40, MODULE.BRANCH),
            ("not-an-oid", "codex/repository-index-refresh"),
            ("a" * 40, ""),
        ]
        for base, branch in MODULE.AUTHORIZED_REPAIR_CONTEXTS.items():
            ambiguous.extend(
                [
                    (base, "codex/repository-index-refresh"),
                    ("a" * 40, branch),
                    (base, next(other for other in MODULE.REPAIR_BASES_BY_BRANCH if other != branch)),
                ]
            )
        for base, branch in ambiguous:
            with self.assertRaises(RuntimeError):
                MODULE.classify_pr_context(base, branch)
        source = VALIDATOR_PATH.read_text(encoding="utf-8") + Path(__file__).read_text(encoding="utf-8")
        self.assertNotIn("ft-rb-" + "03", source.lower())
        self.assertNotIn("ft_rb_" + "03", source.lower())

    def test_52_generic_successor_protected_artifacts_are_exact(self) -> None:
        raw = subprocess.run(
            ["git", "ls-tree", "-rz", "--full-tree", "HEAD"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        ).stdout
        _, _, _, entries = MODULE.parse_tree(raw)
        validator = VALIDATOR_PATH.read_bytes()
        self.assertEqual(MODULE.protected_entry_issues(entries, validator), [])

        validator_path = "repository/data/validation/validate_ft_rb_02_inquiry_crm_flow_readiness.py"
        for path in MODULE.PROTECTED_PATHS:
            if path == validator_path:
                continue
            attacked = dict(entries)
            attacked[path] = ("100644", "blob", "a" * 40)
            self.assertIn(f"PROTECTED_ARTIFACT:content:{path}", MODULE.protected_entry_issues(attacked, validator))

        self.assertIn(
            f"PROTECTED_ARTIFACT:content:{validator_path}",
            MODULE.protected_entry_issues(entries, validator + b"\n# changed\n"),
        )
        for path in MODULE.PROTECTED_PATHS:
            missing = dict(entries)
            missing.pop(path)
            self.assertIn(
                f"PROTECTED_ARTIFACT:missing:{path}",
                MODULE.protected_entry_issues(missing, validator),
            )
            linked = dict(entries)
            linked[path] = ("120000", "blob", "a" * 40)
            self.assertIn(
                f"PROTECTED_ARTIFACT:shape:{path}",
                MODULE.protected_entry_issues(linked, validator),
            )
        non_executable_runner = dict(entries)
        non_executable_runner["scripts/test.sh"] = ("100644", "blob", "a" * 40)
        self.assertIn("PROTECTED_RUNNER:shape", MODULE.protected_entry_issues(non_executable_runner, validator))
        missing_runner = dict(entries)
        missing_runner.pop("scripts/test.sh")
        self.assertIn("PROTECTED_RUNNER:missing", MODULE.protected_entry_issues(missing_runner, validator))

    def test_53_generic_runner_allows_only_bounded_successor_insertion(self) -> None:
        original = MODULE.safe_file
        current = original(ROOT / "scripts/test.sh").decode("utf-8")

        def check(text: str) -> list[str]:
            def supplied(path: Path) -> bytes:
                if path == ROOT / "scripts/test.sh":
                    return text.encode("utf-8")
                return original(path)

            with mock.patch.object(MODULE, "safe_file", side_effect=supplied):
                return MODULE.runner_issues(MODULE.SUCCESSOR_CONTEXT)

        insertions = [
            'future_validator="repository/data/validation/validate_repository_index.py"\n"$python" "$future_validator"\n\n',
            '"$python" -B -m unittest tests.test_quality_ledger\n\n',
        ]
        for insertion in insertions:
            candidate = current.replace(MODULE.RUNNER_SLOT_START, MODULE.RUNNER_SLOT_START + insertion, 1)
            self.assertEqual(check(candidate), [])
        self.assertTrue(check(current.replace("ft_rb_02_inquiry_validator=", "changed_ft_rb_02_inquiry_validator=", 1)))
        self.assertIn("RUNNER:successor_prefix", check("# changed\n" + current))
        self.assertIn("RUNNER:successor_suffix", check(current + "# changed\n"))
        duplicate = current.replace(
            MODULE.RUNNER_SLOT_START,
            MODULE.RUNNER_SLOT_START + 'ft_rb_02_inquiry_validator="duplicate"\n\n',
            1,
        )
        self.assertIn("RUNNER:successor_insertion", check(duplicate))

    def test_54_repair_and_two_independent_generic_prs_pass(self) -> None:
        for index, (base, branch) in enumerate(MODULE.AUTHORIZED_REPAIR_CONTEXTS.items(), start=3):
            repair_head, repair_merge = str(index) * 40, str(index + 2) * 40
            repair = self._pr_event(base, repair_head, branch, len(MODULE.REPAIR_ALLOWLIST))
            self.assertEqual(self._run_ci("pull_request", repair, repair_head, []), [])
            self.assertEqual(self._run_ci("pull_request", repair, repair_merge, [base, repair_head]), [])

        generic = [
            ("a" * 40, "b" * 40, "codex/repository-index-refresh", 3),
            ("e" * 40, "f" * 40, "automation/quality-ledger-update", 7),
        ]
        for base, head, branch, count in generic:
            event = self._pr_event(base, head, branch, count)
            self.assertEqual(self._run_ci("pull_request", event, head, []), [])
            merge = "9" * 40
            self.assertEqual(self._run_ci("pull_request", event, merge, [base, head]), [])
        first = self._pr_event(*generic[0])
        self.assertTrue(self._run_ci("pull_request", first, generic[0][1], [], protected_issues=["PROTECTED_ARTIFACT:attack"]))
        self.assertTrue(self._run_ci("pull_request", first, generic[0][1], [], direct_base_available=False))
        self.assertTrue(self._run_ci("pull_request", first, generic[0][1], [], direct_ancestor=False))

    def test_55_generic_push_metadata_and_protected_paths_fail_closed(self) -> None:
        before, after, tree = "1" * 40, "2" * 40, "3" * 40
        repo = {"full_name": MODULE.REPOSITORY_FULL_NAME}

        def event_for(path: str) -> dict:
            return {
                "repository": repo,
                "ref": "refs/heads/main",
                "before": before,
                "after": after,
                "created": False,
                "deleted": False,
                "forced": False,
                "commits": [
                    {"id": after, "tree_id": tree, "distinct": True, "added": [path], "modified": [], "removed": []},
                ],
                "head_commit": {"id": after, "tree_id": tree},
            }

        clean = event_for("repository-index.txt")
        self.assertEqual(self._run_ci("push", clean, after, [before], tree=tree), [])
        for protected in (
            "repository/data/contracts/ft-rb-02-inquiry-crm-flow-readiness.contract.yaml",
            "repository/data/schemas/ft-rb-02-inquiry-crm-flow-readiness.schema.json",
            "repository/data/registries/extensions/ftrb02/inquiry-crm-flow-readiness.yaml",
            "repository/data/validation/validate_ft_rb_02_inquiry_crm_flow_readiness.py",
            "tests/test_ft_rb_02_inquiry_crm_flow_readiness.py",
        ):
            self.assertTrue(self._run_ci("push", event_for(protected), after, [before], tree=tree))
        missing = event_for("repository-index.txt")
        for key in ("added", "modified", "removed"):
            missing["commits"][0].pop(key)
        self.assertEqual(self._run_ci("push", missing, after, [before], tree=tree), [])
        self.assertTrue(self._run_ci("push", clean, after, ["4" * 40], tree=tree))
        self.assertTrue(self._run_ci("push", clean, after, [before], tree=tree, protected_issues=["PROTECTED_ARTIFACT:attack"]))
        self.assertTrue(self._run_ci("push", missing, after, [before], tree=tree, regular_issues=["PATH_SHAPE:attack"]))

    def test_56_repair_scope_and_generic_local_dispatch_are_bounded(self) -> None:
        for branch in MODULE.REPAIR_BASES_BY_BRANCH:
            with mock.patch.object(MODULE, "current_branch", return_value=branch), \
                 mock.patch.object(MODULE, "commit_available", return_value=True), \
                 mock.patch.object(MODULE, "is_ancestor", return_value=True):
                self.assertEqual(MODULE.local_context(), MODULE.REPAIR_CONTEXT)
        with mock.patch.object(MODULE, "current_branch", return_value="codex/repository-index-refresh"), \
             mock.patch.object(MODULE, "commit_available", return_value=True), \
             mock.patch.object(MODULE, "is_ancestor", return_value=True):
            self.assertEqual(MODULE.local_context(), MODULE.SUCCESSOR_CONTEXT)
        diff_paths = mock.Mock(return_value=list(MODULE.REPAIR_ALLOWLIST))
        with mock.patch.dict(os.environ, {"CI": "false", "GITHUB_ACTIONS": "false"}, clear=False), \
             mock.patch.object(MODULE, "clean_checkout", return_value=True), \
             mock.patch.object(MODULE, "local_context", return_value=MODULE.REPAIR_CONTEXT), \
             mock.patch.object(MODULE, "current_branch", return_value=MODULE.PATH_PROOF_REPAIR_BRANCH), \
             mock.patch.object(MODULE, "diff_paths", diff_paths), \
             mock.patch.object(MODULE, "repair_delta_issues", return_value=[]), \
             mock.patch.object(MODULE, "committed_tree_issues", return_value=[]), \
             mock.patch.object(MODULE, "successor_protected_issues", return_value=[]), \
             mock.patch.object(MODULE, "regular_path_issues", return_value=[]):
            self.assertEqual(MODULE.git_context_issues(), [])
        diff_paths.assert_called_once_with(MODULE.PATH_PROOF_REPAIR_BASE)
        with mock.patch.dict(os.environ, {"CI": "false", "GITHUB_ACTIONS": "false"}, clear=False), \
             mock.patch.object(MODULE, "clean_checkout", return_value=True), \
             mock.patch.object(MODULE, "local_context", return_value=MODULE.SUCCESSOR_CONTEXT), \
             mock.patch.object(MODULE, "successor_protected_issues", return_value=[]), \
             mock.patch.object(MODULE, "regular_path_issues", return_value=[]):
            self.assertEqual(MODULE.git_context_issues(), [])

    def test_57_realistic_one_row_merge_pushes_are_shallow_safe(self) -> None:
        repo = {"full_name": MODULE.REPOSITORY_FULL_NAME}

        def event_for(
            before: str,
            after: str,
            tree: str,
            paths: tuple[list[str], list[str], list[str]] | None = None,
        ) -> dict:
            row = {"id": after, "tree_id": tree, "distinct": True}
            if paths is not None:
                row.update(zip(("added", "modified", "removed"), paths))
            return {
                "repository": repo,
                "ref": "refs/heads/main",
                "before": before,
                "after": after,
                "created": False,
                "deleted": False,
                "forced": False,
                "commits": [row],
                "head_commit": {"id": after, "tree_id": tree},
            }

        real_after = "bcbc67cbdcb2cbb0757155bb97db0c4acd87d3c7"
        real_source = "1652fad5e079df87b07648e21ebd6cd08f92bd21"
        real_tree = "d2c6c123603fed70ad48bce431c3bbe10264336a"
        real_event = event_for(MODULE.REPAIR_BASE, real_after, real_tree)
        self.assertEqual(
            self._run_ci(
                "push",
                real_event,
                real_after,
                [MODULE.REPAIR_BASE, real_source],
                tree=real_tree,
                direct_base_available=False,
            ),
            [],
        )

        failed_after = "ddea2ffbf209681e7903d76316958f20fb61382f"
        failed_source = "c02b96a8298640477f878c2162335d047308aed4"
        failed_tree = "5017de5ce43be07ce96db336a57c417c055df750"
        failed_actions_event = event_for(
            MODULE.POST_MERGE_REPAIR_BASE,
            failed_after,
            failed_tree,
        )
        self.assertEqual(
            self._run_ci(
                "push",
                failed_actions_event,
                failed_after,
                [MODULE.POST_MERGE_REPAIR_BASE, failed_source],
                tree=failed_tree,
                direct_base_available=False,
            ),
            [],
        )

        future_after, future_source, future_tree = "6" * 40, "7" * 40, "8" * 40
        repair_event = event_for(MODULE.PATH_PROOF_REPAIR_BASE, future_after, future_tree)
        self.assertEqual(
            self._run_ci(
                "push",
                repair_event,
                future_after,
                [MODULE.PATH_PROOF_REPAIR_BASE, future_source],
                tree=future_tree,
                direct_base_available=False,
            ),
            [],
        )
        exact_metadata = event_for(
            MODULE.PATH_PROOF_REPAIR_BASE,
            future_after,
            future_tree,
            ([], list(MODULE.REPAIR_ALLOWLIST), []),
        )
        self.assertEqual(
            self._run_ci("push", exact_metadata, future_after, [MODULE.PATH_PROOF_REPAIR_BASE, future_source], tree=future_tree),
            [],
        )

        historical_after, historical_source = "9" * 40, "a" * 40
        historical = event_for(
            MODULE.APPROVED_SUCCESSOR_BASE,
            historical_after,
            future_tree,
        )
        self.assertEqual(
            self._run_ci(
                "push",
                historical,
                historical_after,
                [MODULE.APPROVED_SUCCESSOR_BASE, historical_source],
                tree=future_tree,
            ),
            [],
        )

        generic_before, generic_after, generic_source = "b" * 40, "c" * 40, "d" * 40
        generic = event_for(generic_before, generic_after, future_tree)
        self.assertEqual(
            self._run_ci(
                "push",
                generic,
                generic_after,
                [generic_before, generic_source],
                tree=future_tree,
                direct_base_available=False,
            ),
            [],
        )
        generic_metadata = event_for(generic_before, generic_after, future_tree, (["repository-index.txt"], [], []))
        self.assertEqual(
            self._run_ci("push", generic_metadata, generic_after, [generic_before, generic_source], tree=future_tree),
            [],
        )

    def test_58_one_row_merge_push_adversaries_fail_closed(self) -> None:
        before = MODULE.PATH_PROOF_REPAIR_BASE
        after, source, tree = "6" * 40, "7" * 40, "8" * 40
        repo = {"full_name": MODULE.REPOSITORY_FULL_NAME}
        exact = {
            "repository": repo,
            "ref": "refs/heads/main",
            "before": before,
            "after": after,
            "created": False,
            "deleted": False,
            "forced": False,
            "commits": [
                {
                    "id": after,
                    "tree_id": tree,
                    "distinct": True,
                    "added": [],
                    "modified": list(MODULE.REPAIR_ALLOWLIST),
                    "removed": [],
                }
            ],
            "head_commit": {"id": after, "tree_id": tree},
        }

        parent_attacks = [
            [],
            [before],
            [source, before],
            [before, before],
            [before, after],
            [before, source, "9" * 40],
        ]
        for parents in parent_attacks:
            self.assertTrue(self._run_ci("push", exact, after, parents, tree=tree), parents)

        event_attacks: list[dict] = []
        for key in ("created", "deleted", "forced"):
            attack = copy.deepcopy(exact); attack[key] = True; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["repository"]["full_name"] = "fork/example"; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["ref"] = "refs/heads/release"; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["before"] = "not-an-oid"; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["after"] = "not-an-oid"; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["head_commit"]["id"] = source; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["head_commit"]["tree_id"] = "9" * 40; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["commits"][0]["id"] = source; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["commits"][0]["tree_id"] = "9" * 40; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["commits"][0]["distinct"] = False; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["commits"][0].pop("removed"); event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["commits"][0]["modified"] = [MODULE.REPAIR_ALLOWLIST[0]]; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["commits"][0]["added"] = ["unexpected.txt"]; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["commits"][0]["removed"] = [MODULE.REPAIR_ALLOWLIST[0]]; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["commits"][0]["modified"] = "not-a-list"; event_attacks.append(attack)
        attack = copy.deepcopy(exact); attack["commits"][0]["added"] = [MODULE.REPAIR_ALLOWLIST[0]]; event_attacks.append(attack)
        for attack in event_attacks:
            self.assertTrue(self._run_ci("push", attack, after, [before, source], tree=tree), attack)

        self.assertTrue(self._run_ci("push", exact, "9" * 40, [before, source], tree=tree))

        actions_without_paths = copy.deepcopy(exact)
        for key in ("added", "modified", "removed"):
            actions_without_paths["commits"][0].pop(key)
        self.assertEqual(self._run_ci("push", actions_without_paths, after, [before, source], tree=tree), [])
        self.assertTrue(
            self._run_ci(
                "push",
                actions_without_paths,
                after,
                [before, source],
                tree=tree,
                repair_issues=["REPAIR_TREE_PROOF:digest_or_count"],
            )
        )
        self.assertTrue(
            self._run_ci(
                "push",
                actions_without_paths,
                after,
                [before, source],
                tree=tree,
                protected_issues=["PROTECTED_ARTIFACT:attack"],
            )
        )
        self.assertTrue(
            self._run_ci(
                "push",
                actions_without_paths,
                after,
                [before, source],
                tree=tree,
                regular_issues=["PATH_SHAPE:attack"],
            )
        )

        multi_row_source_absent = copy.deepcopy(actions_without_paths)
        multi_row_source_absent["commits"].insert(
            0,
            {"id": "a" * 40, "tree_id": "b" * 40, "distinct": True},
        )
        self.assertEqual(self._run_ci("push", multi_row_source_absent, after, [before, source], tree=tree), [])
        inconsistent = copy.deepcopy(multi_row_source_absent)
        inconsistent["commits"][0].update({"added": [], "modified": [], "removed": []})
        self.assertTrue(self._run_ci("push", inconsistent, after, [before, source], tree=tree))

        generic_before = "1" * 40
        direct_with_extra_row = copy.deepcopy(exact)
        direct_with_extra_row["before"] = generic_before
        direct_with_extra_row["commits"][0]["modified"] = []
        direct_with_extra_row["commits"][0]["added"] = ["repository-index.txt"]
        direct_with_extra_row["commits"].insert(
            0,
            {"id": "2" * 40, "tree_id": "3" * 40, "distinct": True, "added": [], "modified": [], "removed": []},
        )
        self.assertTrue(self._run_ci("push", direct_with_extra_row, after, [generic_before], tree=tree))

    def test_59_repair_tree_delta_proof_is_exact_and_depth_one_safe(self) -> None:
        self.assertEqual(MODULE.repair_delta_issues(MODULE.PATH_PROOF_REPAIR_BASE), [])
        self.assertEqual(MODULE.repair_delta_issues("a" * 40), ["REPAIR_TREE_PROOF:unapproved_base"])

        expected_base_blobs = {
            MODULE.REPAIR_BASE: (
                "574faaafcfd78599b9f33de95e8e49a8f4920025",
                "b3db92d5b5ee5e92e32e14d48fd7925cbec3aebc",
            ),
            MODULE.POST_MERGE_REPAIR_BASE: (
                "a64d61a72a044f70628ebea4eaa929016b2f3869",
                "2a455da06fea28de2d11340d6afcdd8b546f6e02",
            ),
            MODULE.PATH_PROOF_REPAIR_BASE: (
                "f74ffcc993f1c502a95331a9cd7268ce700a4828",
                "062d1af57d57dde6c5d96226901dc4c0365f3174",
            ),
        }
        self.assertEqual(set(MODULE.REPAIR_TREE_PROOFS), set(MODULE.AUTHORIZED_REPAIR_CONTEXTS))
        for base, expected in MODULE.REPAIR_TREE_PROOFS.items():
            self.assertEqual(
                expected[:3],
                (
                    "cd207364c54d1af3c1d475a1fed60d1c0720edde27b8210b47a388847279ba64",
                    657,
                    659,
                ),
            )
            self.assertEqual(
                tuple(expected[3][path] for path in MODULE.REPAIR_ALLOWLIST),
                expected_base_blobs[base],
            )

        current_raw = subprocess.run(
            ["git", "ls-tree", "-rz", "--full-tree", "HEAD"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        ).stdout
        completed = subprocess.CompletedProcess(["git"], 0, stdout=current_raw, stderr=b"")
        with mock.patch.object(MODULE.subprocess, "run", return_value=completed) as shallow_run:
            self.assertEqual(MODULE.repair_delta_issues(MODULE.PATH_PROOF_REPAIR_BASE), [])
        shallow_run.assert_called_once_with(
            ["git", "ls-tree", "-rz", "--full-tree", "HEAD"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )

        expected = MODULE.REPAIR_TREE_PROOFS[MODULE.PATH_PROOF_REPAIR_BASE]
        current_entries = MODULE.parse_tree(current_raw, set(MODULE.REPAIR_ALLOWLIST))[3]
        unchanged = dict(current_entries)
        unchanged[MODULE.REPAIR_ALLOWLIST[0]] = ("100644", "blob", expected[3][MODULE.REPAIR_ALLOWLIST[0]])
        with mock.patch.object(MODULE, "parse_tree", return_value=(*expected[:3], unchanged)):
            self.assertIn(
                f"REPAIR_TREE_PROOF:unchanged:{MODULE.REPAIR_ALLOWLIST[0]}",
                MODULE.repair_delta_issues(MODULE.PATH_PROOF_REPAIR_BASE),
            )
        missing = dict(current_entries)
        missing.pop(MODULE.REPAIR_ALLOWLIST[1])
        with mock.patch.object(MODULE, "parse_tree", return_value=(*expected[:3], missing)):
            self.assertIn(
                f"REPAIR_TREE_PROOF:missing:{MODULE.REPAIR_ALLOWLIST[1]}",
                MODULE.repair_delta_issues(MODULE.PATH_PROOF_REPAIR_BASE),
            )
        linked = dict(current_entries)
        linked[MODULE.REPAIR_ALLOWLIST[1]] = ("120000", "blob", "a" * 40)
        with mock.patch.object(MODULE, "parse_tree", return_value=(*expected[:3], linked)):
            self.assertIn(
                f"REPAIR_TREE_PROOF:shape:{MODULE.REPAIR_ALLOWLIST[1]}",
                MODULE.repair_delta_issues(MODULE.PATH_PROOF_REPAIR_BASE),
            )
        with mock.patch.object(
            MODULE,
            "parse_tree",
            return_value=("b" * 64, expected[1] + 1, expected[2] + 1, current_entries),
        ):
            self.assertIn(
                "REPAIR_TREE_PROOF:digest_or_count",
                MODULE.repair_delta_issues(MODULE.PATH_PROOF_REPAIR_BASE),
            )

    def test_60_actions_push_without_paths_uses_real_tree_proof_stack(self) -> None:
        after = MODULE.git("rev-parse", "HEAD").stdout.strip()
        tree = MODULE.git("show", "-s", "--format=%T", "HEAD").stdout.strip()
        source = "7" * 40
        event = {
            "repository": {"full_name": MODULE.REPOSITORY_FULL_NAME},
            "ref": "refs/heads/main",
            "before": MODULE.PATH_PROOF_REPAIR_BASE,
            "after": after,
            "created": False,
            "deleted": False,
            "forced": False,
            "commits": [{"id": after, "tree_id": tree, "distinct": True}],
            "head_commit": {"id": after, "tree_id": tree},
        }
        with mock.patch.dict(
            os.environ,
            {"CI": "true", "GITHUB_ACTIONS": "true", "GITHUB_EVENT_NAME": "push"},
            clear=False,
        ), mock.patch.object(MODULE, "clean_checkout", return_value=True), mock.patch.object(
            MODULE,
            "load_event",
            return_value=event,
        ), mock.patch.object(
            MODULE,
            "raw_commit",
            return_value=(tree, [MODULE.PATH_PROOF_REPAIR_BASE, source]),
        ), mock.patch.object(
            MODULE,
            "commit_available",
            side_effect=AssertionError("parent object access is forbidden"),
        ), mock.patch.object(
            MODULE,
            "is_ancestor",
            side_effect=AssertionError("parent ancestry access is forbidden"),
        ):
            self.assertEqual(MODULE.ci_context_issues(), [])


if __name__ == "__main__":
    unittest.main()
