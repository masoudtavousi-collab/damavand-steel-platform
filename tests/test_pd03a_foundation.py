#!/usr/bin/env python3
"""Positive, negative, and adversarial tests for PD-03A."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
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
            else:
                self.fail(f"undispatched pilot mutation: {mutation}")
            messages = rendered_schema_errors(self.pilot_validator, value)
            messages.extend(pilot.validate_fixture(value, mutation, self.pilot_validator))
            return "\n".join(messages)

        if target == "approval":
            value = copy.deepcopy(self.approval_value)
            record = value["evidence"][0]
            verify_hashes = False
            if mutation == "forged_technical_pass":
                record["technical_review"]["verdict"] = "PASS"
                record["technical_review"]["evidence_reference"] = "forged"
                record["technical_review"]["review_date"] = "2026-08-01"
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
            else:
                self.fail(f"undispatched approval mutation: {mutation}")
            return "\n".join(
                approval.validate_registry(value, self.lifecycle, verify_hashes=verify_hashes)
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
            else:
                self.fail(f"undispatched foundation mutation: {mutation}")
            messages = rendered_schema_errors(self.foundation_validator, value)
            messages.extend(foundation.validate_bundle(value, self.contract, self.lifecycle))
            return "\n".join(messages)

        if target == "loader" and mutation == "duplicate_yaml_key":
            try:
                foundation.load_yaml(FIXTURES / "adversarial-duplicate-keys.yaml")
            except foundation.ValidationConfigurationError as exc:
                return str(exc)
            return ""

        if target == "schema":
            path = (
                FIXTURES / "adversarial-remote-ref-schema.json"
                if mutation == "remote_ref"
                else FIXTURES / "adversarial-permissive-schema.json"
            )
            try:
                foundation.validate_schema(
                    foundation.require_mapping(foundation.load_json(path), str(path))
                )
            except foundation.ValidationConfigurationError as exc:
                return str(exc)
            return ""

        self.fail(f"undispatched mutation target={target} mutation={mutation}")
        return ""

    def test_all_mutations_reach_real_validators_and_fail_closed(self) -> None:
        self.assertEqual(len(self.mutations), 25)
        dispatched: set[str] = set()
        for case in self.mutations:
            with self.subTest(case=case["id"]):
                output = self.dispatch(case["mutation"], case["target"])
                self.assertIn(case["expected"].casefold(), output.casefold())
                dispatched.add(case["id"])
        self.assertEqual(dispatched, {case["id"] for case in self.mutations})


if __name__ == "__main__":
    unittest.main()
