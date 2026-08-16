#!/usr/bin/env python3
"""Positive, negative and adversarial tests for C002 Pilot Candidate intake."""

from __future__ import annotations

import copy
import importlib.util
import io
from contextlib import redirect_stderr, redirect_stdout
import json
from pathlib import Path
import socket
import subprocess
import sys
from unittest.mock import patch
import unittest


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "repository/data/validation/validate_commercial_pilot_candidates.py"
VALIDATION_DIR = VALIDATOR_PATH.parent
FIXTURES = ROOT / "tests/fixtures/c002-commercial-pilot"
VALID_FIXTURE = FIXTURES / "valid-synthetic.yaml"
CANONICAL_REGISTRY = ROOT / "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml"
sys.path.insert(0, str(VALIDATION_DIR))

import validate_commercial_pilot_candidates as candidate  # noqa: E402


class CommercialPilotCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.definitions = candidate.load_definitions()
        cls.canonical = candidate.load_yaml(CANONICAL_REGISTRY, "canonical registry")
        cls.fixture = candidate.load_yaml(VALID_FIXTURE, "valid fixture")
        cls.manifest = candidate.load_json(FIXTURES / "mutation-cases.json", "mutation manifest")

    def render(self, value: object) -> str:
        return "\n".join(
            issue.render()
            for issue in candidate.validate_registry(value, "<mutation>", self.definitions)
        )

    @staticmethod
    def founder_provenance() -> dict[str, object]:
        return {
            "source_type": "FOUNDER_EVIDENCE_PACKET",
            "source_reference": "founder-evidence-packet:c002:protected-intake",
            "captured_by": "role:founder-or-authorized-steward",
            "captured_at": "2000-01-03T00:00:00Z",
            "evidence_status": "PROTECTED_FOUNDER_EVIDENCE",
        }

    def test_positive_canonical_registry_is_empty_and_valid(self) -> None:
        self.assertEqual(self.canonical["candidates"], [])
        self.assertEqual(
            candidate.validate_registry(self.canonical, "<canonical>", self.definitions),
            [],
        )

    def test_positive_synthetic_founder_packet_is_nine_of_nine(self) -> None:
        self.assertEqual(
            candidate.validate_registry(self.fixture, "<fixture>", self.definitions),
            [],
        )
        item = self.fixture["candidates"][0]
        packet = item["founder_evidence_packet"]
        minimum = packet["minimum_data_packet"]
        self.assertEqual(
            tuple(entry["criterion_code"] for entry in packet["criteria"]),
            candidate.CRITERIA,
        )
        self.assertEqual(packet["coverage"]["resolved_count"], 9)
        self.assertEqual(packet["coverage"]["formula"], "resolved_count/9")
        self.assertFalse(packet["coverage"]["weights_used"])
        self.assertFalse(packet["coverage"]["thresholds_used"])
        self.assertEqual(packet["evaluation_as_of"], "2000-01-03T00:00:00Z")
        self.assertEqual(minimum["packet_state"], "COMPLETE")
        self.assertNotIn("UNRESOLVED", tuple(candidate.iter_strings(minimum)))
        self.assertNotEqual(minimum["owner_role"], minimum["reviewer_role"])
        self.assertEqual(item["readiness"]["state"], "FOUNDER_SELECTION_READY")
        self.assertEqual(
            {key: item["selection_effects"][key] for key in candidate.EXPECTED_SELECTION_STATE_POLICY},
            candidate.EXPECTED_SELECTION_STATE_POLICY,
        )

    def test_positive_validation_needs_no_network(self) -> None:
        with patch.object(socket, "socket", side_effect=AssertionError("network forbidden")):
            self.assertEqual(
                candidate.validate_registry(
                    copy.deepcopy(self.fixture), "<offline>", self.definitions
                ),
                [],
            )

    def test_positive_protected_founder_intake_is_noncanonical_and_no_authority(self) -> None:
        value = copy.deepcopy(self.fixture)
        value["data_classification"] = "FOUNDER_INTAKE_PROTECTED"
        value["candidates"][0]["provenance"] = self.founder_provenance()
        self.assertEqual(candidate.validate_registry(value, "<founder-intake>", self.definitions), [])
        self.assertEqual(value["boundary"], candidate.BOUNDARY)
        self.assertFalse(value["candidates"][0]["selection_effects"]["founder_selection_recorded"])

    def test_positive_module_import_has_no_output_or_side_effect(self) -> None:
        spec = importlib.util.spec_from_file_location("c002_import_probe", VALIDATOR_PATH)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        stdout = io.StringIO()
        stderr = io.StringIO()
        try:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                spec.loader.exec_module(module)
        finally:
            sys.modules.pop(spec.name, None)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")

    def dispatch_candidate_mutation(self, mutation: str) -> str:
        value = copy.deepcopy(self.fixture)
        item = value["candidates"][0]
        packet = item["founder_evidence_packet"]
        minimum = packet["minimum_data_packet"]
        criteria = packet["criteria"]
        if mutation == "canonical_population":
            value["data_classification"] = "C002_CONTRACT_FOUNDATION"
        elif mutation == "boundary_product_authority":
            value["boundary"]["product_population_authority"] = True
        elif mutation == "approved_status":
            item["status"] = "APPROVED"
        elif mutation == "sku_scope_reference":
            item["commercial_scope"]["entity_references"] = ["prd:sku:000000000006"]
        elif mutation == "seed_ceiling":
            item["commercial_scope"]["seed_count_is_scope_ceiling"] = True
        elif mutation == "seed_identity":
            item["seed_references"][0]["references_are_identity"] = True
        elif mutation == "seed_auto_select":
            item["seed_references"][0]["automatically_selected"] = True
        elif mutation == "seed_limits_scope":
            item["seed_references"][0]["limits_candidate_scope"] = True
        elif mutation == "unknown_seed":
            item["seed_references"][0]["pilot_id"] = "pilot:ffffffffffff"
        elif mutation == "duplicate_candidate_id":
            value["candidates"].append(copy.deepcopy(item))
        elif mutation == "duplicate_packet_id":
            duplicate = copy.deepcopy(item)
            duplicate["candidate_id"] = "cpcand:000000000002"
            value["candidates"].append(duplicate)
        elif mutation == "duplicate_source_id":
            criteria[1]["sources"][0]["evidence_source_id"] = criteria[0]["sources"][0]["evidence_source_id"]
        elif mutation == "missing_criterion":
            criteria.pop()
        elif mutation == "extra_criterion":
            criteria.append(copy.deepcopy(criteria[-1]))
        elif mutation == "swapped_criteria":
            criteria[0], criteria[1] = criteria[1], criteria[0]
        elif mutation == "unknown_state":
            criteria[0]["state"] = "PASS"
        elif mutation == "gpp_non_founder":
            criteria[2]["sources"][0]["source_type"] = "OPERATIONS_EVIDENCE"
        elif mutation == "missing_with_source":
            criteria[0]["state"] = "MISSING"
        elif mutation == "submitted_without_source":
            criteria[0]["state"] = "SUBMITTED"
            criteria[0]["sources"] = []
        elif mutation == "verified_without_review":
            criteria[0]["review"] = {
                "reviewed_by": None,
                "reviewed_at": None,
                "evidence_reference": None,
            }
        elif mutation == "conflicting_one_source":
            criteria[0]["state"] = "CONFLICTING"
        elif mutation == "na_without_review":
            criteria[0]["state"] = "NOT_APPLICABLE_APPROVED"
            criteria[0]["review"] = {
                "reviewed_by": None,
                "reviewed_at": None,
                "evidence_reference": None,
            }
        elif mutation == "resolved_count_tamper":
            packet["coverage"]["resolved_count"] = 8
        elif mutation == "unresolved_list_tamper":
            packet["coverage"]["unresolved_criteria"] = ["DEMAND_SIGNAL"]
        elif mutation == "weights_enabled":
            packet["coverage"]["weights_used"] = True
        elif mutation == "thresholds_enabled":
            packet["coverage"]["thresholds_used"] = True
        elif mutation == "ready_with_blocker":
            item["readiness"]["blockers"] = ["FOUNDER_DECISION_PENDING"]
        elif mutation == "not_ready_at_nine":
            item["readiness"]["state"] = "NOT_READY"
        elif mutation == "selection_creates_product":
            item["selection_effects"]["creates_product"] = True
        elif mutation == "selection_creates_sku":
            item["selection_effects"]["creates_sku"] = True
        elif mutation == "selection_asserts_availability":
            item["selection_effects"]["asserts_availability"] = True
        elif mutation == "price_injection":
            item["price"] = 1
        elif mutation == "availability_injection":
            item["availability_value"] = "in_stock"
        elif mutation == "registry_version_drift":
            value["registry_version"] = "1.0.1"
        elif mutation == "empty_synthetic":
            value["candidates"] = []
        elif mutation == "evaluation_before_submission":
            packet["evaluation_as_of"] = "1999-12-31T00:00:00Z"
        elif mutation == "review_before_submission":
            criteria[0]["review"]["reviewed_at"] = "1999-12-31T00:00:00Z"
        elif mutation == "review_after_expiry":
            criteria[0]["sources"][0]["expires_at"] = "2000-01-01T12:00:00Z"
        elif mutation == "verified_expired_asof":
            criteria[0]["sources"][0]["expires_at"] = "2000-01-02T12:00:00Z"
        elif mutation == "expired_still_ready":
            criteria[0]["state"] = "EXPIRED"
            criteria[0]["sources"][0]["expires_at"] = "2000-01-02T12:00:00Z"
        elif mutation == "conflicting_still_ready":
            criteria[0]["state"] = "CONFLICTING"
            second = copy.deepcopy(criteria[0]["sources"][0])
            second["evidence_source_id"] = "cpevd:000000000010"
            second["source_reference"] = "fixture:c002:conflicting-demand-signal"
            criteria[0]["sources"].append(second)
        elif mutation == "reviewer_is_submitter":
            criteria[0]["sources"][0]["submitted_by"] = minimum["reviewer_role"]
        elif mutation == "reviewer_is_owner":
            criteria[0]["review"]["reviewed_by"] = minimum["owner_role"]
        elif mutation == "reviewer_role_mismatch":
            minimum["reviewer_role"] = "role:alternate-reviewer"
        elif mutation == "missing_minimum_section":
            del minimum["seo"]
        elif mutation == "unresolved_minimum_complete":
            minimum["seo"]["buyer_intent_reference"] = "UNRESOLVED"
        elif mutation == "incomplete_minimum_ready":
            minimum["seo"]["buyer_intent_reference"] = "UNRESOLVED"
            minimum["packet_state"] = "INCOMPLETE"
        elif mutation == "packet_conflict_ready":
            minimum["conflicts_exclusions_blockers"]["conflicts"] = ["fixture:c002:open-conflict"]
            minimum["packet_state"] = "INCOMPLETE"
        elif mutation == "unknown_packet_canonical":
            minimum["bounded_commercial_context"]["canonical_references"] = [
                "prd:series:ffffffffffff"
            ]
        elif mutation == "unknown_mass_unit":
            minimum["mass"]["unit_reference"] = "unit:ffffffffffff"
        elif mutation == "packet_owner_reviewer_same":
            minimum["owner_role"] = minimum["reviewer_role"]
        elif mutation == "pending_decision_with_ref":
            packet["decision_reference"] = "fixture:c002:unexpected-decision"
        elif mutation == "recorded_decision_without_ref":
            packet["decision_state"] = "FOUNDER_DECISION_RECORDED"
        elif mutation == "product_state_drift":
            item["selection_effects"]["product_state"] = "CREATED"
        elif mutation == "sku_state_drift":
            item["selection_effects"]["sku_state"] = "ASSIGNED"
        elif mutation == "availability_state_drift":
            item["selection_effects"]["availability_state"] = "ASSERTED"
        elif mutation == "projection_state_drift":
            item["selection_effects"]["projection_state"] = "PASS"
        elif mutation == "commerce_state_drift":
            item["selection_effects"]["commerce_state"] = "PURCHASE_ENABLED"
        elif mutation == "founder_provenance_under_synthetic":
            item["provenance"] = self.founder_provenance()
        elif mutation == "founder_classification_with_synthetic":
            value["data_classification"] = "FOUNDER_INTAKE_PROTECTED"
        elif mutation == "founder_invalid_captured_by":
            value["data_classification"] = "FOUNDER_INTAKE_PROTECTED"
            item["provenance"] = self.founder_provenance()
            item["provenance"]["captured_by"] = "role:automated-validation"
        elif mutation == "founder_invalid_evidence_status":
            value["data_classification"] = "FOUNDER_INTAKE_PROTECTED"
            item["provenance"] = self.founder_provenance()
            item["provenance"]["evidence_status"] = "UNPROTECTED"
        elif mutation == "founder_population_authority":
            value["data_classification"] = "FOUNDER_INTAKE_PROTECTED"
            item["provenance"] = self.founder_provenance()
            value["boundary"]["candidate_population_authority"] = True
        elif mutation == "recorded_decision_with_ref":
            packet["decision_state"] = "FOUNDER_DECISION_RECORDED"
            packet["decision_reference"] = "founder-decision:c002:recorded"
        else:
            self.fail(f"undispatched candidate mutation: {mutation}")
        return self.render(value)

    def dispatch(self, target: str, mutation: str) -> str:
        if target == "candidate":
            return self.dispatch_candidate_mutation(mutation)
        if target == "loader":
            try:
                candidate.load_yaml(FIXTURES / "adversarial-duplicate-keys.yaml", "duplicate fixture")
            except candidate.ConfigurationError as exc:
                return str(exc)
            return ""
        if target == "schema":
            path = (
                FIXTURES / "adversarial-remote-ref-schema.json"
                if mutation == "remote_ref"
                else FIXTURES / "adversarial-permissive-schema.json"
            )
            try:
                candidate.load_definitions(schema_path=path)
            except candidate.ConfigurationError as exc:
                return str(exc)
            return ""
        if target == "contract":
            value = copy.deepcopy(self.definitions.contract)
            if mutation == "dependency_drift":
                value["dependencies"]["product_core"] = "docs/incorrect.yaml"
            elif mutation == "classification_drift":
                value["data_classifications"]["canonical"] = "CANONICAL"
            elif mutation == "stable_identity_drift":
                value["stable_identity"]["allocation_policy"] = "SEQUENTIAL"
            elif mutation == "contract_seed_ceiling":
                value["seed_reference_policy"]["seed_count_is_scope_ceiling"] = True
            elif mutation == "evidence_evaluation_drift":
                value["founder_evidence_packet"]["deterministic_evaluation"]["expiry_boundary"] = "unspecified"
            elif mutation == "minimum_packet_drift":
                value["minimum_founder_data_packet"]["ready_requires"]["unresolved_marker_count"] = 1
            elif mutation == "readiness_drift":
                value["readiness_policy"]["founder_selection_ready_requires"]["resolved_count"] = 8
            elif mutation == "selection_state_drift":
                value["selection_state_policy"]["product_state"] = "CREATED"
            elif mutation == "scope_drift":
                value["scope_policy"]["cartesian_generation_forbidden"] = False
            elif mutation == "validation_drift":
                value["validation"]["network_allowed"] = True
            elif mutation == "prohibited_field_drift":
                value["prohibited_fields"].append("new_commercial_field")
            elif mutation == "provenance_policy_drift":
                value["provenance_policy"]["founder_intake_protected"]["canonical_population_authority"] = True
            else:
                self.fail(f"undispatched contract mutation: {mutation}")
            try:
                candidate.validate_contract(value)
            except candidate.ConfigurationError as exc:
                return str(exc)
            return ""
        self.fail(f"unknown mutation target: {target}")
        return ""

    def test_all_manifest_mutations_dispatch_and_fail_closed(self) -> None:
        cases = self.manifest["cases"]
        self.assertEqual(self.manifest["expected_case_count"], 79)
        self.assertEqual(len(cases), 79)
        self.assertEqual(len({case["id"] for case in cases}), 79)
        for case in cases:
            with self.subTest(case=case["id"]):
                message = self.dispatch(case["target"], case["mutation"])
                self.assertTrue(message, f"mutation did not fail closed: {case['id']}")
                self.assertIn(f"[{case['expected_code']}]", message)
                self.assertNotIn("Traceback", message)

    def test_adversarial_non_finite_json_is_rejected(self) -> None:
        with self.assertRaisesRegex(candidate.ConfigurationError, "NON_FINITE_NUMBER"):
            candidate.strict_json('{"value": NaN}', "non-finite")

    def test_adversarial_deep_structure_is_rejected(self) -> None:
        value: object = "leaf"
        for _ in range(candidate.MAX_NESTING_DEPTH + 1):
            value = {"child": value}
        with self.assertRaisesRegex(candidate.ConfigurationError, "STRUCTURE_DEPTH"):
            candidate.bounded(value, "deep")

    def test_adversarial_nested_object_without_required_is_rejected(self) -> None:
        schema = {
            "type": "object",
            "additionalProperties": False,
            "required": ["nested"],
            "properties": {
                "nested": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {"value": {"type": "string"}},
                }
            },
        }
        with self.assertRaisesRegex(candidate.ConfigurationError, "INCOMPLETE_OBJECT_SCHEMA"):
            candidate.audit_schema(schema)

    def test_error_output_is_deterministic(self) -> None:
        value = copy.deepcopy(self.fixture)
        value["candidates"][0]["founder_evidence_packet"]["coverage"]["resolved_count"] = 0
        first = self.render(value)
        second = self.render(value)
        self.assertEqual(first, second)

    def test_cli_positive_canonical_and_fixture(self) -> None:
        for path in (CANONICAL_REGISTRY, VALID_FIXTURE):
            result = subprocess.run(
                [sys.executable, str(VALIDATOR_PATH), str(path)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("validation PASS", result.stdout)
            self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
