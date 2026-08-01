#!/usr/bin/env python3
"""Positive, negative, and adversarial tests for PD-03A."""

from __future__ import annotations

import copy
import base64
import hashlib
import json
import math
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
VALIDATION = ROOT / "repository/data/validation"
sys.path.insert(0, str(VALIDATION))

import validate_measurements  # noqa: E402
import validate_pd02b_canonical_slice  # noqa: E402
import validate_pd03a_approval_evidence as approval  # noqa: E402
import validate_pd03a_pilot_prerequisite as foundation  # noqa: E402
import validate_product_pilot_combinations as pilot  # noqa: E402


FIXTURES = ROOT / "tests/fixtures/pd03a"


def rendered_schema_errors(validator, value: object) -> list[str]:
    return [
        f"[SCHEMA_VALIDATION] {'/'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in validator.iter_errors(value)
    ]


class PD03AFoundationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = foundation.require_mapping(
            foundation.load_yaml(foundation.CONTRACT_PATH), "PD-03A contract"
        )
        cls.lifecycle = foundation.lifecycle_status(cls.contract)
        cls.schema = foundation.require_mapping(
            foundation.load_json(foundation.SCHEMA_PATH), "PD-03A schema"
        )
        cls.foundation_validator = foundation.validate_schema(cls.schema)
        cls.bundle = foundation.load_yaml(foundation.REGISTRY_PATH)
        cls.pilot_validator, _ = pilot.load_validator()
        cls.pilot_fixture = foundation.load_yaml(pilot.DEFAULT_FIXTURE)
        cls.approval_value = foundation.load_yaml(approval.REGISTRY_PATH)
        cls.mutations = json.loads(
            (FIXTURES / "mutation-cases.json").read_text(encoding="utf-8")
        )

    def test_positive_canonical_foundation(self) -> None:
        self.assertEqual(foundation.main(), 0)

    def test_positive_approval_evidence(self) -> None:
        self.assertEqual(approval.main(), 0)

    def test_positive_synthetic_pilot_fixture(self) -> None:
        self.assertEqual(pilot.main([]), 0)

    def test_positive_measurement_lifecycle(self) -> None:
        self.assertEqual(validate_measurements.main(["canonical"]), 0)

    def test_positive_pd02b_immutable_regression(self) -> None:
        self.assertEqual(validate_pd02b_canonical_slice.main(), 0)

    def test_positive_synthetic_foundation_manifest(self) -> None:
        manifest = foundation.load_yaml(FIXTURES / "valid-synthetic-foundation.yaml")
        self.assertEqual(manifest["data_classification"], "SYNTHETIC_FIXTURE")
        self.assertFalse(manifest["canonical_population_authority"])
        self.assertEqual(
            manifest["expected_extension_counts"],
            {
                "entities": 2,
                "attributes": 4,
                "value_registries": 1,
                "controlled_terms": 1,
                "profiles": 1,
                "profile_rules": 6,
                "localized_labels": 11,
            },
        )
        self.assertEqual(
            manifest["readiness"],
            {"import_ready": False, "runtime_ready": False, "golden_ready": False},
        )

    def dispatch(self, mutation: str, target: str) -> str:
        if target == "pilot":
            value = copy.deepcopy(self.pilot_fixture)
            first = value["combinations"][0]
            if mutation == "grade_430":
                first["grade_term_id"] = "vterm:000000000430"
            elif mutation == "pvd":
                first["finish_term_id"] = "vterm:000000000001"
            elif mutation == "length_3m":
                first["length"]["decimal_lexeme"] = "3"
            elif mutation == "extra_combination":
                value["combinations"].append(copy.deepcopy(first))
                value["combinations"][-1]["combination_id"] = "pcomb:abcdef123456"
            elif mutation == "wrong_diameter_unit":
                first["diameter"]["unit_id"] = "unit:000000000001"
            elif mutation == "wrong_thickness_precision":
                first["thickness"]["decimal_lexeme"] = "0.350"
            elif mutation == "cartesian_enabled":
                value["cartesian_generation_forbidden"] = False
            elif mutation == "supply_status":
                first["supply_status"] = "SUPPLY_AFTER_INQUIRY"
            elif mutation == "availability_value":
                first["availability_value"] = "in_stock"
            elif mutation == "sku":
                first["sku"] = "FORBIDDEN-SKU"
            elif mutation == "slug":
                first["slug"] = "forbidden-slug"
            elif mutation == "runtime_ready":
                value["readiness"]["runtime_ready"] = True
            elif mutation == "golden_ready":
                value["readiness"]["golden_ready"] = True
            elif mutation == "historical_identity":
                first["historical_reference_is_identity"] = True
            elif mutation == "cross_file_references":
                value["series_entity_id"] = "prd:series:000000000000"
                value["variant_rule_set_entity_id"] = "prd:variant-rule-set:000000000000"
                value["profile_id"] = "pprof:000000000000"
            elif mutation == "wrong_combination_id":
                first["combination_id"] = "pcomb:abcdefabcdef"
            else:
                self.fail(f"undispatched pilot mutation: {mutation}")
            messages = rendered_schema_errors(self.pilot_validator, value)
            messages.extend(pilot.validate_fixture(value, mutation, self.pilot_validator))
            return "\n".join(messages)

        if target == "approval":
            value = copy.deepcopy(self.approval_value)
            record = value["evidence"][0]
            verify_hashes = False
            lifecycle = self.lifecycle
            lifecycle_contract = copy.deepcopy(self.contract)
            if mutation in {"premature_approval", "approval_replay"}:
                lifecycle = "REVIEW"
                lifecycle_contract["lifecycle"].update({
                    "current_status": "REVIEW",
                    "transition_history": [{
                        "from": "DRAFT", "to": "REVIEW",
                        "evidence_reference": "PD03A-TECH-REVIEW-001",
                    }],
                })
                record["lifecycle_status"] = "REVIEW"
                record["status"] = "CANDIDATE_UNVERIFIED"
                record["approval"] = {
                    "approved_by": None, "approved_at": None,
                    "evidence_reference": None,
                }
                record["anti_replay"]["consumed"] = False
                record["anti_replay"]["consumption_history"] = []
            if mutation == "forged_technical_pass":
                record["technical_review"]["verdict"] = "PASS"
                record["technical_review"]["evidence_reference"] = "forged"
                record["technical_review"]["review_date"] = "2026-08-01"
            elif mutation == "forged_technical_pass_review":
                lifecycle = "REVIEW"
                reviewed_head = "a" * 40
                raw_commit = subprocess.check_output([
                    "git", "-C", str(ROOT), "cat-file", "commit", "HEAD",
                ])
                object_b64 = base64.b64encode(raw_commit).decode("ascii")
                object_sha256 = hashlib.sha256(raw_commit).hexdigest()
                ci_run_id = "30695723727"
                ci_job_id = "91358155209"
                artifact = approval.technical_artifact(
                    reviewed_head, object_sha256, ci_run_id, ci_job_id,
                )
                digest = hashlib.sha256(artifact.encode("utf-8")).hexdigest()
                lifecycle_contract["lifecycle"].update({
                    "current_status": "REVIEW",
                    "transition_history": [{
                        "from": "DRAFT", "to": "REVIEW",
                        "evidence_reference": "PD03A-TECH-REVIEW-001",
                    }],
                    "technical_reviewed_sha": reviewed_head,
                    "technical_review_artifact_sha256": digest,
                })
                record["lifecycle_status"] = "REVIEW"
                record["technical_review"].update({
                    "verdict": "PASS", "evidence_reference": "PD03A-TECH-REVIEW-001",
                    "review_date": "2026-08-01", "reviewed_head_sha": reviewed_head,
                    "reviewed_commit_object_b64": object_b64,
                    "reviewed_commit_object_sha256": object_sha256,
                    "ci_run_id": ci_run_id, "ci_job_id": ci_job_id,
                    "verdict_artifact": artifact, "verdict_artifact_sha256": digest,
                })
            elif mutation == "wrong_review_reference_review":
                lifecycle = "REVIEW"
                reviewed_head = subprocess.check_output([
                    "git", "-C", str(ROOT), "rev-parse", "HEAD",
                ], text=True).strip()
                raw_commit = subprocess.check_output([
                    "git", "-C", str(ROOT), "cat-file", "commit", reviewed_head,
                ])
                object_b64 = base64.b64encode(raw_commit).decode("ascii")
                object_sha256 = hashlib.sha256(raw_commit).hexdigest()
                ci_run_id = "30695723727"
                ci_job_id = "91358155209"
                artifact = approval.technical_artifact(
                    reviewed_head, object_sha256, ci_run_id, ci_job_id,
                )
                digest = hashlib.sha256(artifact.encode("utf-8")).hexdigest()
                lifecycle_contract["lifecycle"].update({
                    "current_status": "REVIEW",
                    "transition_history": [{
                        "from": "DRAFT", "to": "REVIEW",
                        "evidence_reference": "PD03A-TECH-REVIEW-001",
                    }],
                    "technical_reviewed_sha": reviewed_head,
                    "technical_review_artifact_sha256": digest,
                })
                record["lifecycle_status"] = "REVIEW"
                record["technical_review"].update({
                    "verdict": "PASS", "evidence_reference": "forged",
                    "review_date": "2026-08-01", "reviewed_head_sha": reviewed_head,
                    "reviewed_commit_object_b64": object_b64,
                    "reviewed_commit_object_sha256": object_sha256,
                    "ci_run_id": ci_run_id, "ci_job_id": ci_job_id,
                    "verdict_artifact": artifact, "verdict_artifact_sha256": digest,
                })
            elif mutation == "premature_approval":
                record["approval"] = {
                    "approved_by": "Founder پروژه Damavand Steel",
                    "approved_at": "2026-08-01T00:00:00Z",
                    "evidence_reference": "FD-PD03A-001",
                }
            elif mutation == "approval_replay":
                record["anti_replay"]["consumed"] = True
            elif mutation == "hash_tampering":
                record["dataset_hashes"][0]["sha256"] = "0" * 64
                verify_hashes = True
            elif mutation == "failed_review_as_pass":
                record["failed_review_attempts"][0]["verdict"] = "PASS"
            elif mutation == "arbitrary_nonce":
                record["anti_replay"]["nonce"] = "0" * 24
            elif mutation == "approval_id_collision":
                record["approval_evidence_id"] = "papproval:f8c559c1228c"
            else:
                self.fail(f"undispatched approval mutation: {mutation}")
            return "\n".join(
                approval.validate_registry(
                    value, lifecycle, verify_hashes=verify_hashes,
                    lifecycle_contract=lifecycle_contract,
                )
            )

        if target == "foundation":
            if mutation == "lifecycle_direct_approved":
                contract = copy.deepcopy(self.contract)
                contract["lifecycle"]["current_status"] = "APPROVED"
                contract["lifecycle"]["transition_history"] = []
                try:
                    foundation.lifecycle_status(contract)
                except foundation.ValidationConfigurationError as exc:
                    return f"LIFECYCLE: {exc}"
                return ""
            value = copy.deepcopy(self.bundle)
            if mutation == "extra_entity":
                value["entities"].append(copy.deepcopy(value["entities"][0]))
            elif mutation == "unicode_confusable":
                for label in value["localized_labels"]:
                    if label["locale"] == "en":
                        label["label"] = "Sіlver"
                        break
            elif mutation == "alias_pvd":
                value["localized_labels"][-1]["aliases"] = ["PVD"]
            elif mutation == "wrong_category":
                value["attributes"][1]["category"] = "SECONDARY"
            elif mutation == "wrong_parent_type":
                value["entities"][0]["parent_entity_type"] = "SERIES"
            elif mutation == "wrong_owner":
                value["entities"][0]["owner"]["role"] = "attacker-controlled"
            elif mutation == "wrong_subject_kind":
                value["localized_labels"][0]["subject_kind"] = "CONTROLLED_TERM"
            elif mutation == "unknown_nested_field":
                value["entities"][0]["owner"]["privilege"] = "admin"
            elif mutation == "malformed_provenance":
                value["attributes"][0]["provenance"] = []
            elif mutation == "non_finite_foundation":
                value["attributes"][1]["validation"]["constraints"]["minimum"] = math.inf
            else:
                self.fail(f"undispatched foundation mutation: {mutation}")
            messages = rendered_schema_errors(self.foundation_validator, value)
            messages.extend(foundation.validate_bundle(value, self.contract, self.lifecycle))
            return "\n".join(messages)

        if target == "loader":
            try:
                if mutation == "duplicate_yaml_key":
                    foundation.load_yaml(FIXTURES / "adversarial-duplicate-keys.yaml")
                elif mutation in {"duplicate_json_key", "nonfinite_json"}:
                    payload = '{"key":1,"key":2}' if mutation == "duplicate_json_key" else '{"key":NaN}'
                    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", encoding="utf-8") as handle:
                        handle.write(payload)
                        handle.flush()
                        foundation.load_json(Path(handle.name))
                else:
                    self.fail(f"undispatched loader mutation: {mutation}")
            except foundation.ValidationConfigurationError as exc:
                return str(exc)
            return ""

        if target == "schema":
            try:
                if mutation in {"remote_ref", "permissive_schema"}:
                    path = (
                        FIXTURES / "adversarial-remote-ref-schema.json"
                        if mutation == "remote_ref"
                        else FIXTURES / "adversarial-permissive-schema.json"
                    )
                    schema = foundation.require_mapping(foundation.load_json(path), str(path))
                elif mutation == "nested_empty_schema":
                    schema = {
                        "$schema": "https://json-schema.org/draft/2020-12/schema",
                        "type": "object", "additionalProperties": False,
                        "properties": {"payload": {}},
                    }
                elif mutation == "nested_true_schema":
                    schema = {
                        "$schema": "https://json-schema.org/draft/2020-12/schema",
                        "type": "object", "additionalProperties": False,
                        "properties": {"payload": {"anyOf": [True, {"type": "string"}]}},
                    }
                elif mutation == "not_false_schema":
                    schema = {
                        "$schema": "https://json-schema.org/draft/2020-12/schema",
                        "type": "object", "additionalProperties": False,
                        "properties": {"payload": {"not": False}},
                    }
                elif mutation == "annotation_only_schema":
                    schema = {
                        "$schema": "https://json-schema.org/draft/2020-12/schema",
                        "type": "object", "additionalProperties": False,
                        "properties": {"payload": {"description": "accepts anything"}},
                    }
                elif mutation == "if_without_branch_schema":
                    schema = {
                        "$schema": "https://json-schema.org/draft/2020-12/schema",
                        "type": "object", "additionalProperties": False,
                        "properties": {"payload": {"if": {"type": "string"}}},
                    }
                else:
                    self.fail(f"undispatched schema mutation: {mutation}")
                foundation.validate_schema(schema)
            except foundation.ValidationConfigurationError as exc:
                return str(exc)
            return ""

        if target == "foundation_contract":
            contract = copy.deepcopy(self.contract)
            if mutation == "role_tampering":
                contract["roles"]["technical_reviewer"] = "attacker-controlled"
            elif mutation == "prohibited_tampering":
                contract["prohibited"].remove("pvd")
            else:
                self.fail(f"undispatched foundation contract mutation: {mutation}")
            try:
                foundation.validate_contract(contract)
            except foundation.ValidationConfigurationError as exc:
                return str(exc)
            return ""

        if target == "approval_contract":
            contract = foundation.load_yaml(approval.CONTRACT_PATH)
            if mutation == "network_enabled":
                contract["evidence_policy"]["network_allowed"] = True
            else:
                self.fail(f"undispatched approval contract mutation: {mutation}")
            try:
                approval.validate_contract(contract)
            except foundation.ValidationConfigurationError as exc:
                return str(exc)
            return ""

        if target == "pilot_contract":
            contract = foundation.load_yaml(pilot.CONTRACT_PATH)
            if mutation == "side_effects_enabled":
                contract["validation"]["side_effects_allowed"] = True
            else:
                self.fail(f"undispatched pilot contract mutation: {mutation}")
            with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", encoding="utf-8") as handle:
                import yaml

                yaml.safe_dump(contract, handle, sort_keys=False, allow_unicode=True)
                handle.flush()
                try:
                    pilot.load_validator(Path(handle.name), pilot.SCHEMA_PATH)
                except foundation.ValidationConfigurationError as exc:
                    return str(exc)
            return ""

        self.fail(f"undispatched mutation target={target} mutation={mutation}")
        return ""

    def test_all_mutations_reach_real_validators_and_fail_closed(self) -> None:
        self.assertEqual(len(self.mutations), 50)
        dispatched: set[str] = set()
        for case in self.mutations:
            with self.subTest(case=case["id"]):
                output = self.dispatch(case["mutation"], case["target"])
                self.assertIn(case["expected"].casefold(), output.casefold())
                dispatched.add(case["id"])
        self.assertEqual(dispatched, {case["id"] for case in self.mutations})


if __name__ == "__main__":
    unittest.main()
