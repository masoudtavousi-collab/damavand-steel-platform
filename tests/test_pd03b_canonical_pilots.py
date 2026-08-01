#!/usr/bin/env python3
"""Positive, negative and adversarial tests for the exact PD-03B scope."""

from __future__ import annotations

import copy
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest
import yaml


ROOT = Path(__file__).resolve().parents[1]
VALIDATION = ROOT / "repository/data/validation"
sys.path.insert(0, str(VALIDATION))

import validate_pd03a_pilot_prerequisite as shared  # noqa: E402
import validate_pd03b_approval_evidence as approval  # noqa: E402
import validate_pd03b_canonical_pilots as pilot  # noqa: E402


FIXTURES = ROOT / "tests/fixtures/pd03b"


class PD03BCanonicalPilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator, cls.contract, cls.lifecycle = pilot.load_validator()
        cls.bundle = shared.load_yaml(pilot.REGISTRY_PATH)
        _, cls.approval_validator = approval.load_contract_and_schema()
        cls.approval_value = shared.load_yaml(approval.REGISTRY_PATH)
        cls.manifest = shared.load_json(FIXTURES / "mutation-cases.json")

    def test_positive_exact_draft(self) -> None:
        self.assertEqual(self.lifecycle, "DRAFT")
        self.assertEqual(pilot.validate_bundle(self.bundle, self.lifecycle, self.validator), [])
        self.assertEqual(
            approval.validate_registry(
                self.approval_value, self.lifecycle, self.approval_validator,
            ),
            [],
        )
        self.assertEqual(len(self.bundle["pilots"]), 3)
        self.assertEqual(
            self.bundle["readiness"],
            {"import_ready": False, "runtime_ready": False, "golden_ready": False},
        )
        self.assertEqual(len(pilot.IDENTITY_REGISTRY_PATHS), 17)
        self.assertTrue(all(path.is_file() for path in pilot.IDENTITY_REGISTRY_PATHS))

    def dispatch(self, target: str, mutation: str) -> str:
        if target == "pilot":
            value = copy.deepcopy(self.bundle)
            first = value["pilots"][0]
            second = value["pilots"][1]
            if mutation == "extra_pilot":
                value["pilots"].append(copy.deepcopy(first))
                value["pilots"][-1]["pilot_id"] = "pilot:abcdef123456"
            elif mutation == "missing_pilot":
                value["pilots"].pop()
            elif mutation == "wrong_tuple":
                first["attribute_values"]["diameter"]["decimal_lexeme"] = "17"
            elif mutation == "duplicate_pilot_id":
                second["pilot_id"] = first["pilot_id"]
            elif mutation == "duplicate_history":
                second["historical_references"] = copy.deepcopy(first["historical_references"])
            elif mutation == "historical_identity":
                first["historical_references"]["references_are_identity"] = True
            elif mutation == "wrong_grade":
                first["attribute_values"]["grade"]["term_id"] = "vterm:000000000430"
            elif mutation == "wrong_finish":
                first["attribute_values"]["finish"]["term_id"] = "vterm:000000000001"
            elif mutation == "wrong_diameter_unit":
                first["attribute_values"]["diameter"]["unit_id"] = "unit:000000000001"
            elif mutation == "wrong_thickness_precision":
                first["attribute_values"]["thickness"]["decimal_lexeme"] = "0.350"
            elif mutation == "length_3m":
                first["attribute_values"]["length"]["decimal_lexeme"] = "3"
            elif mutation == "availability_value":
                first["availability_value"] = "in_stock"
            elif mutation == "availability_status":
                first["availability_status"] = "APPROVED"
            elif mutation == "sku":
                first["sku"] = "FORBIDDEN-SKU"
            elif mutation == "product_id":
                first["product_id"] = "prd:sku:000000000001"
            elif mutation == "golden_package":
                value["golden_package"] = True
            elif mutation == "readiness_import":
                value["readiness"]["import_ready"] = True
            elif mutation == "readiness_runtime":
                value["readiness"]["runtime_ready"] = True
            elif mutation == "readiness_golden":
                value["readiness"]["golden_ready"] = True
            elif mutation == "cartesian":
                value["cartesian_generation_forbidden"] = False
            elif mutation == "unknown_series":
                value["series_entity_id"] = "prd:series:000000000000"
            elif mutation == "unknown_profile":
                value["profile_id"] = "pprof:000000000000"
            elif mutation == "lifecycle_status":
                first["status"] = "APPROVED"
            elif mutation == "owner":
                first["owner"]["role"] = "attacker-controlled"
            elif mutation == "provenance":
                first["provenance"]["source_references"] = ["fabricated"]
            elif mutation == "unicode_confusable":
                first["historical_references"]["golden_reference"] = "GОLD-PIPE-201-16-035-6M"
            elif mutation == "unknown_nested":
                first["owner"]["admin"] = True
            elif mutation == "swapped_pilot_ids":
                first["pilot_id"], second["pilot_id"] = second["pilot_id"], first["pilot_id"]
            elif mutation == "omitted_registry_collision":
                first["pilot_id"] = "pilot:000000000001"
            else:
                self.fail(f"undispatched pilot mutation: {mutation}")
            message = "\n".join(pilot.validate_bundle(value, self.lifecycle, self.validator))
            if mutation == "omitted_registry_collision":
                self.assertIn("GLOBAL_ID_COLLISION", message)
            return message

        if target == "lifecycle":
            contract = copy.deepcopy(self.contract)
            if mutation == "direct_approved":
                contract["lifecycle"]["current_status"] = "APPROVED"
                contract["lifecycle"]["transition_history"] = []
            else:
                self.fail(f"undispatched lifecycle mutation: {mutation}")
            try:
                pilot.lifecycle_status(contract)
            except shared.ValidationConfigurationError as exc:
                return str(exc)
            return ""

        if target == "approval":
            value = copy.deepcopy(self.approval_value)
            record = value["evidence"][0]
            verify_hashes = False
            if mutation == "forged_technical_pass":
                record["technical_review"]["verdict"] = "PASS"
                record["technical_review"]["evidence_reference"] = "forged"
            elif mutation == "premature_approval":
                record["approval"] = {
                    "approved_by": "Founder پروژه Damavand Steel",
                    "approved_at": "2026-08-01T00:00:00Z",
                    "evidence_reference": "FD-PD03B-001",
                }
            elif mutation == "approval_replay":
                record["anti_replay"]["consumed"] = True
            elif mutation == "hash_tamper":
                record["dataset_hashes"][0]["sha256"] = "0" * 64
                verify_hashes = True
            elif mutation == "arbitrary_nonce":
                record["anti_replay"]["nonce"] = "0" * 24
            elif mutation == "approval_id":
                record["approval_evidence_id"] = "papproval:000000000000"
            else:
                self.fail(f"undispatched approval mutation: {mutation}")
            return "\n".join(
                approval.validate_registry(
                    value, self.lifecycle, self.approval_validator,
                    verify_hashes=verify_hashes,
                )
            )

        if target == "contract":
            try:
                if mutation == "pilot_contract_tamper":
                    value = copy.deepcopy(self.contract)
                    value["roles"]["ai_domain_authority"] = True
                    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", encoding="utf-8") as handle:
                        yaml.safe_dump(value, handle, allow_unicode=True, sort_keys=False)
                        handle.flush()
                        pilot.load_validator(contract_path=Path(handle.name))
                elif mutation == "approval_contract_tamper":
                    value = shared.load_yaml(approval.CONTRACT_PATH)
                    value["evidence_policy"]["network_allowed"] = True
                    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", encoding="utf-8") as handle:
                        yaml.safe_dump(value, handle, allow_unicode=True, sort_keys=False)
                        handle.flush()
                        approval.load_contract_and_schema(contract_path=Path(handle.name))
                else:
                    self.fail(f"undispatched contract mutation: {mutation}")
            except shared.ValidationConfigurationError as exc:
                return str(exc)
            return ""

        if target == "loader":
            try:
                if mutation == "duplicate_yaml":
                    shared.load_yaml(FIXTURES / "adversarial-duplicate-keys.yaml")
                elif mutation in {"duplicate_json", "nonfinite_json"}:
                    payload = '{"key":1,"key":2}' if mutation == "duplicate_json" else '{"key":NaN}'
                    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", encoding="utf-8") as handle:
                        handle.write(payload)
                        handle.flush()
                        shared.load_json(Path(handle.name))
                else:
                    self.fail(f"undispatched loader mutation: {mutation}")
            except shared.ValidationConfigurationError as exc:
                return str(exc)
            return ""

        if target == "schema":
            path = (
                FIXTURES / "adversarial-remote-ref-schema.json"
                if mutation == "remote_ref"
                else FIXTURES / "adversarial-permissive-schema.json"
            )
            try:
                shared.validate_schema(shared.require_mapping(shared.load_json(path), str(path)))
            except shared.ValidationConfigurationError as exc:
                return str(exc)
            return ""

        self.fail(f"unknown mutation target: {target}")
        return ""

    def test_all_counted_mutations_dispatch_and_fail_closed(self) -> None:
        cases = self.manifest["cases"]
        self.assertEqual(self.manifest["expected_case_count"], 43)
        self.assertEqual(len(cases), 43)
        self.assertEqual(len({case["id"] for case in cases}), 43)
        for case in cases:
            with self.subTest(case=case["id"]):
                message = self.dispatch(case["target"], case["mutation"])
                self.assertTrue(message, f"mutation did not fail closed: {case['id']}")

    def test_schema_rejects_non_finite_nested_value(self) -> None:
        value = copy.deepcopy(self.bundle)
        value["pilots"][0]["attribute_values"]["diameter"]["decimal_lexeme"] = math.inf
        self.assertTrue(pilot.validate_bundle(value, self.lifecycle, self.validator))

    def test_manifest_is_strict_json(self) -> None:
        parsed = json.loads((FIXTURES / "mutation-cases.json").read_text(encoding="utf-8"))
        self.assertEqual(parsed, self.manifest)


if __name__ == "__main__":
    unittest.main()
