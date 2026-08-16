#!/usr/bin/env python3
"""Positive, negative, and adversarial tests for C002 Product Administration."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
VALIDATION = ROOT / "repository/data/validation"
sys.path.insert(0, str(VALIDATION))

import validate_pd03a_pilot_prerequisite as shared  # noqa: E402
import validate_product_administration_policies as subject  # noqa: E402


FIXTURES = ROOT / "tests/fixtures/c002-product-administration"


class ProductAdministrationPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator, cls.contract = subject.load_validator()
        cls.canonical = shared.load_yaml(subject.REGISTRY_PATH)
        cls.synthetic = shared.load_yaml(FIXTURES / "valid-synthetic.yaml")
        cls.manifest = shared.load_json(FIXTURES / "mutation-cases.json")

    def test_positive_canonical_registry_is_policy_only(self) -> None:
        self.assertEqual(
            subject.validate_package(self.canonical, self.validator, canonical=True), []
        )
        self.assertEqual(self.canonical["instances"], [])
        self.assertEqual(len(self.canonical["policies"]), 8)

    def test_positive_synthetic_exercises_all_eight_kinds(self) -> None:
        self.assertEqual(
            subject.validate_package(self.synthetic, self.validator, canonical=False), []
        )
        self.assertEqual(
            [item["record_kind"] for item in self.synthetic["instances"]],
            [kind for _, _, kind in subject.POLICY_DESCRIPTORS],
        )
        self.assertTrue(all(item["status"] == "CANDIDATE_UNVERIFIED" for item in self.synthetic["instances"]))
        harmony = self._instance(self.synthetic, "INVENTORY_HARMONY")
        self.assertEqual(len(harmony["component_ratios"]), 3)
        commerce = self._instance(self.synthetic, "COMMERCE_ELIGIBILITY")
        self.assertEqual(commerce["state_model"]["states"], subject.COMMERCE_STATES)
        self.assertEqual(len(commerce["evidence_gates"]), 14)
        generic = copy.deepcopy(self.synthetic)
        self._instance(generic, "CONTROLLED_VALUE_PROPOSAL")["proposal_target"] = {
            "target_type": "GENERIC_CONTROLLED_VALUE",
            "attribute_id": "attr:dbf5365ee1e5",
            "value_registry_id": "vreg:302188e2fc8a",
            "proposed_value_term_id": None,
        }
        self.assertEqual(subject.validate_package(generic, self.validator, canonical=False), [])

        lifecycle = copy.deepcopy(self.synthetic)
        proposal = self._instance(lifecycle, "CONTROLLED_VALUE_PROPOSAL")
        proposal["proposal_state"] = "APPROVED"
        proposal["validation_evidence_references"] = ["synthetic:validation-pass"]
        proposal["review_evidence_references"] = ["synthetic:review-pass"]
        proposal["approval_evidence_references"] = ["synthetic:approval-pass"]
        proposal["transition_history"] = [
            {"sequence": 1, "from_state": "DRAFT", "to_state": "VALIDATE", "transitioned_at": "2026-08-16T01:00:00Z", "actor_role": "proposal-author", "reviewer_role": "validation-reviewer", "evidence_references": ["synthetic:validation-pass"]},
            {"sequence": 2, "from_state": "VALIDATE", "to_state": "REVIEW", "transitioned_at": "2026-08-16T02:00:00Z", "actor_role": "validation-reviewer", "reviewer_role": "domain-reviewer", "evidence_references": ["synthetic:review-pass"]},
            {"sequence": 3, "from_state": "REVIEW", "to_state": "APPROVED", "transitioned_at": "2026-08-16T03:00:00Z", "actor_role": "domain-reviewer", "reviewer_role": "approval-authority", "evidence_references": ["synthetic:approval-pass"]},
        ]
        self.assertEqual(subject.validate_package(lifecycle, self.validator, canonical=False), [])

        multi_mass = copy.deepcopy(self.synthetic)
        original = self._instance(multi_mass, "MASS_PROVENANCE")
        successor = copy.deepcopy(original)
        successor["record_id"] = "padm:7b2e0c02a009"
        successor["supersedes_record_ids"] = [original["record_id"]]
        original["conflict_references"] = [successor["record_id"]]
        mass_index = multi_mass["instances"].index(original)
        multi_mass["instances"].insert(mass_index + 1, successor)
        self.assertEqual(subject.validate_package(multi_mass, self.validator, canonical=False), [])

    @staticmethod
    def _instance(value: dict, kind: str) -> dict:
        return next(item for item in value["instances"] if item["record_kind"] == kind)

    def dispatch(self, target: str, mutation: str) -> str:
        if target == "canonical":
            value = copy.deepcopy(self.canonical)
            if mutation == "add_instance":
                value["instances"].append(copy.deepcopy(self.synthetic["instances"][0]))
            else:
                self.fail(f"undispatched canonical mutation: {mutation}")
            return "\n".join(subject.validate_package(value, self.validator, canonical=True))

        if target == "package":
            value = copy.deepcopy(self.synthetic)
            if mutation == "missing_policy":
                value["policies"].pop()
            elif mutation == "duplicate_policy_id":
                value["policies"][1]["policy_id"] = value["policies"][0]["policy_id"]
            elif mutation == "swap_policies":
                value["policies"][0], value["policies"][1] = value["policies"][1], value["policies"][0]
            elif mutation == "policy_runtime":
                value["policies"][0]["runtime_authority"] = True
            elif mutation == "unknown_root":
                value["runtime"] = True
            elif mutation == "duplicate_record_id":
                value["instances"][1]["record_id"] = value["instances"][0]["record_id"]
            elif mutation == "missing_record_kind":
                del value["instances"][0]["record_kind"]
            elif mutation == "builder_cartesian":
                self._instance(value, "PRODUCT_BUILDER")["cartesian_generation_forbidden"] = False
            elif mutation == "builder_sku":
                self._instance(value, "PRODUCT_BUILDER")["sku_derivation_allowed"] = True
            elif mutation == "builder_unknown_family":
                self._instance(value, "PRODUCT_BUILDER")["family_entity_id"] = "prd:family:ffffffffffff"
            elif mutation == "builder_unknown_profile":
                self._instance(value, "PRODUCT_BUILDER")["profile_id"] = "pprof:ffffffffffff"
            elif mutation == "builder_unknown_value":
                self._instance(value, "PRODUCT_BUILDER")["controlled_value_selections"][0]["value_term_id"] = "vterm:ffffffffffff"
            elif mutation == "value_direct_mutation":
                self._instance(value, "CONTROLLED_VALUE_PROPOSAL")["direct_canonical_registry_mutation_allowed"] = True
            elif mutation == "value_normalization":
                self._instance(value, "CONTROLLED_VALUE_PROPOSAL")["normalization"] = ["TRIM"]
            elif mutation == "value_direct_approved":
                self._instance(value, "CONTROLLED_VALUE_PROPOSAL")["proposal_state"] = "APPROVED"
            elif mutation == "value_finish_target":
                target = self._instance(value, "CONTROLLED_VALUE_PROPOSAL")["proposal_target"]
                target["finish_attribute_id"] = "attr:1926e2ad4629"
                target["finish_value_registry_id"] = "vreg:3d37a24e09ea"
            elif mutation in {"value_generic_unknown_attr", "value_generic_mismatch", "value_generic_term"}:
                record = self._instance(value, "CONTROLLED_VALUE_PROPOSAL")
                record["proposal_target"] = {
                    "target_type": "GENERIC_CONTROLLED_VALUE",
                    "attribute_id": "attr:dbf5365ee1e5",
                    "value_registry_id": "vreg:302188e2fc8a",
                    "proposed_value_term_id": None,
                }
                if mutation == "value_generic_unknown_attr":
                    record["proposal_target"]["attribute_id"] = "attr:ffffffffffff"
                elif mutation == "value_generic_mismatch":
                    record["proposal_target"]["value_registry_id"] = "vreg:e1b9dd333df8"
                else:
                    record["proposal_target"]["proposed_value_term_id"] = "vterm:ffffffffffff"
            elif mutation in {"value_exact_duplicate", "value_normalized_duplicate", "value_cyrillic_bypass", "value_unsupported_greek", "value_mixed_persian"}:
                record = self._instance(value, "CONTROLLED_VALUE_PROPOSAL")
                record["proposal_target"] = {
                    "target_type": "GENERIC_CONTROLLED_VALUE", "attribute_id": "attr:dbf5365ee1e5",
                    "value_registry_id": "vreg:302188e2fc8a", "proposed_value_term_id": None,
                }
                if mutation == "value_exact_duplicate":
                    record["value_code"] = "stainless_steel"
                elif mutation == "value_normalized_duplicate":
                    record["aliases"] = [{"locale": "en", "value": "STAINLESS_STEEL"}]
                elif mutation == "value_cyrillic_bypass":
                    record["aliases"] = [{"locale": "en", "value": "ѕtainless_steel"}]
                elif mutation == "value_unsupported_greek":
                    record["aliases"] = [{"locale": "en", "value": "stainless_steεl"}]
                else:
                    record["aliases"] = [{"locale": "fa-IR", "value": "استیلsteel"}]
            elif mutation in {"value_backwards_time", "value_stage_evidence_mismatch"}:
                record = self._instance(value, "CONTROLLED_VALUE_PROPOSAL")
                record["proposal_state"] = "APPROVED"
                record["validation_evidence_references"] = ["synthetic:validation-pass"]
                record["review_evidence_references"] = ["synthetic:review-pass"]
                record["approval_evidence_references"] = ["synthetic:approval-pass"]
                record["transition_history"] = [
                    {"sequence": 1, "from_state": "DRAFT", "to_state": "VALIDATE", "transitioned_at": "2026-08-16T01:00:00Z", "actor_role": "proposal-author", "reviewer_role": "validation-reviewer", "evidence_references": ["synthetic:validation-pass"]},
                    {"sequence": 2, "from_state": "VALIDATE", "to_state": "REVIEW", "transitioned_at": "2026-08-16T02:00:00Z", "actor_role": "validation-reviewer", "reviewer_role": "domain-reviewer", "evidence_references": ["synthetic:review-pass"]},
                    {"sequence": 3, "from_state": "REVIEW", "to_state": "APPROVED", "transitioned_at": "2026-08-16T03:00:00Z", "actor_role": "domain-reviewer", "reviewer_role": "approval-authority", "evidence_references": ["synthetic:approval-pass"]},
                ]
                if mutation == "value_backwards_time":
                    record["transition_history"][1]["transitioned_at"] = "2026-08-16T00:30:00Z"
                else:
                    record["transition_history"][1]["evidence_references"] = ["synthetic:wrong-stage"]
            elif mutation == "brand_inference":
                self._instance(value, "BRAND_PROVENANCE")["inference_forbidden"] = False
            elif mutation == "brand_missing_reference":
                self._instance(value, "BRAND_PROVENANCE")["manufacturer_reference"] = "synthetic:manufacturer"
            elif mutation == "mass_quantity":
                self._instance(value, "MASS_PROVENANCE")["canonical_quantity"] = "WEIGHT"
            elif mutation == "mass_promotion":
                self._instance(value, "MASS_PROVENANCE")["canonical_value_promotion_allowed"] = True
            elif mutation == "mass_method_mismatch":
                self._instance(value, "MASS_PROVENANCE")["mass_method"] = "MEASURED"
            elif mutation == "mass_not_approximate":
                self._instance(value, "MASS_PROVENANCE")["method_evidence"]["approximate"] = False
            elif mutation == "mass_input_provenance":
                del self._instance(value, "MASS_PROVENANCE")["method_evidence"]["inputs"][0]["provenance_reference"]
            elif mutation == "mass_length_unit":
                self._instance(value, "MASS_PROVENANCE")["unit_id"] = "unit:000000000001"
            elif mutation == "mass_reviewer":
                self._instance(value, "MASS_PROVENANCE")["reviewer"] = {"role": "product-data-steward"}
            elif mutation == "mass_unknown_subject":
                self._instance(value, "MASS_PROVENANCE")["subject_reference"] = "prd:series:ffffffffffff"
            elif mutation == "mass_conflict_self":
                record = self._instance(value, "MASS_PROVENANCE")
                record["conflict_references"] = [record["record_id"]]
            elif mutation == "mass_conflict_unknown":
                self._instance(value, "MASS_PROVENANCE")["conflict_references"] = ["padm:ffffffffffff"]
            elif mutation == "mass_supersedes_unknown":
                self._instance(value, "MASS_PROVENANCE")["supersedes_record_ids"] = ["padm:ffffffffffff"]
            elif mutation == "mass_basis_mismatch":
                self._instance(value, "MASS_PROVENANCE")["applicability_scope"]["basis"] = "PER_LENGTH"
            elif mutation == "mass_supersession_cycle":
                original = self._instance(value, "MASS_PROVENANCE")
                successor = copy.deepcopy(original)
                successor["record_id"] = "padm:7b2e0c02a009"
                original["supersedes_record_ids"] = [successor["record_id"]]
                successor["supersedes_record_ids"] = [original["record_id"]]
                value["instances"].insert(value["instances"].index(original) + 1, successor)
            elif mutation == "brand_missing_scope":
                del self._instance(value, "BRAND_PROVENANCE")["applicability_scope"]
            elif mutation == "brand_missing_evidence":
                self._instance(value, "BRAND_PROVENANCE")["evidence_references"] = []
            elif mutation == "brand_reviewer":
                self._instance(value, "BRAND_PROVENANCE")["reviewer"] = {"role": "product-data-steward"}
            elif mutation == "brand_effective_period":
                record = self._instance(value, "BRAND_PROVENANCE")
                record["effective_until"] = "2026-08-15T00:00:00Z"
            elif mutation == "electro_finish":
                self._instance(value, "ELECTROSTATIC_APPEARANCE")["stainless_finish_reference"] = "vterm:1df9a5493546"
            elif mutation == "electro_pvd":
                self._instance(value, "ELECTROSTATIC_APPEARANCE")["pvd_reference"] = "synthetic:pvd"
            elif mutation == "electro_substrate":
                del self._instance(value, "ELECTROSTATIC_APPEARANCE")["substrate_reference"]
            elif mutation == "electro_method":
                self._instance(value, "ELECTROSTATIC_APPEARANCE")["coating_method"] = "PVD"
            elif mutation == "commerce_purchase":
                self._instance(value, "COMMERCE_ELIGIBILITY")["purchase_enabled"] = True
            elif mutation == "commerce_activation":
                self._instance(value, "COMMERCE_ELIGIBILITY")["activation_allowed"] = True
            elif mutation == "commerce_inheritance":
                self._instance(value, "COMMERCE_ELIGIBILITY")["inheritance_forbidden"] = False
            elif mutation == "commerce_missing_gate":
                self._instance(value, "COMMERCE_ELIGIBILITY")["evidence_gates"].pop(2)
            elif mutation == "commerce_nonboolean_gate":
                self._instance(value, "COMMERCE_ELIGIBILITY")["evidence_gates"][4]["status"] = "yes"
            elif mutation == "commerce_target_state":
                self._instance(value, "COMMERCE_ELIGIBILITY")["eligibility_state"] = "PURCHASE_CANDIDATE"
            elif mutation == "commerce_transition_model":
                self._instance(value, "COMMERCE_ELIGIBILITY")["state_model"]["legal_transitions"][0]["to_state"] = "PURCHASE_ENABLED"
            elif mutation == "commerce_expired_pass":
                gate = self._instance(value, "COMMERCE_ELIGIBILITY")["evidence_gates"][0]
                gate.update({
                    "evidence_references": ["synthetic:product-evidence"], "status": "PASS",
                    "valid_from": "2026-08-01T00:00:00Z", "valid_until": "2026-08-15T00:00:00Z",
                    "reviewed_by": "independent-reviewer", "reviewed_at": "2026-08-14T00:00:00Z",
                })
            elif mutation == "commerce_review_before_valid":
                gate = self._instance(value, "COMMERCE_ELIGIBILITY")["evidence_gates"][0]
                gate.update({
                    "evidence_references": ["synthetic:product-evidence"], "status": "PASS",
                    "valid_from": "2026-08-10T00:00:00Z", "valid_until": None,
                    "reviewed_by": "independent-reviewer", "reviewed_at": "2026-08-09T00:00:00Z",
                })
            elif mutation == "harmony_self":
                record = self._instance(value, "INVENTORY_HARMONY")
                record["component_ratios"][1]["component_reference"] = record["component_ratios"][0]["component_reference"]
            elif mutation == "harmony_pricing":
                self._instance(value, "INVENTORY_HARMONY")["pricing_effect_allowed"] = True
            elif mutation == "harmony_stock":
                self._instance(value, "INVENTORY_HARMONY")["stock_or_availability_inference_allowed"] = True
            elif mutation == "harmony_rule_version":
                self._instance(value, "INVENTORY_HARMONY")["rule_version"] = "latest"
            elif mutation == "harmony_zero_ratio":
                self._instance(value, "INVENTORY_HARMONY")["component_ratios"][0]["quantity_lexeme"] = "0"
            elif mutation == "harmony_predicate":
                self._instance(value, "INVENTORY_HARMONY")["dimension_predicates"][0]["component_references"] = ["prd:sku:00000000c002", "prd:sku:00000000c005"]
            elif mutation == "harmony_conflict":
                record = self._instance(value, "INVENTORY_HARMONY")
                record["conflict_references"] = ["synthetic:conflict"]
                record["outcome"] = "ELIGIBLE"
            elif mutation == "harmony_expired":
                record = self._instance(value, "INVENTORY_HARMONY")
                record["effective_until"] = "2026-08-15T00:00:00Z"
                record["outcome"] = "ELIGIBLE"
            elif mutation == "harmony_missing_evidence":
                record = self._instance(value, "INVENTORY_HARMONY")
                record["evidence_entries"] = []
                record["outcome"] = "ELIGIBLE"
            elif mutation == "harmony_reviewer":
                self._instance(value, "INVENTORY_HARMONY")["reviewer"] = {"role": "product-data-steward"}
            elif mutation == "harmony_commerce_effect":
                self._instance(value, "INVENTORY_HARMONY")["commerce_eligibility_effect_allowed"] = True
            elif mutation == "harmony_review_before_valid":
                evidence = self._instance(value, "INVENTORY_HARMONY")["evidence_entries"][0]
                evidence["valid_from"] = "2026-08-16T00:00:00Z"
                evidence["reviewed_at"] = "2026-08-15T00:00:00Z"
            elif mutation == "harmony_evidence_expired":
                evidence = self._instance(value, "INVENTORY_HARMONY")["evidence_entries"][0]
                evidence["valid_until"] = "2026-08-15T00:00:00Z"
            elif mutation == "central_mutation":
                self._instance(value, "DAMAVAND_CENTRAL_BOM_INTERFACE")["central_may_mutate_damavand_truth"] = True
            elif mutation == "central_implementation":
                self._instance(value, "DAMAVAND_CENTRAL_BOM_INTERFACE")["central_implementation_allowed"] = True
            elif mutation == "forged_provenance":
                self._instance(value, "PRODUCT_BUILDER")["provenance"]["source_reference"] = "fabricated"
            elif mutation == "prohibited_price":
                self._instance(value, "PRODUCT_BUILDER")["price"] = "1"
            else:
                self.fail(f"undispatched package mutation: {mutation}")
            return "\n".join(subject.validate_package(value, self.validator, canonical=False))

        if target == "contract":
            value = copy.deepcopy(self.contract)
            if mutation == "authority_tamper":
                value["authority"]["canonical_instance_population_allowed"] = True
            elif mutation == "invariant_tamper":
                value["invariants"]["inventory_harmony"]["component_count_range"] = [2, 2]
            else:
                self.fail(f"undispatched contract mutation: {mutation}")
            try:
                with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", encoding="utf-8") as handle:
                    yaml.safe_dump(value, handle, allow_unicode=True, sort_keys=False)
                    handle.flush()
                    subject.load_validator(contract_path=Path(handle.name))
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
        self.assertEqual(self.manifest["expected_case_count"], 81)
        self.assertEqual(len(cases), 81)
        self.assertEqual(len({case["id"] for case in cases}), 81)
        for case in cases:
            with self.subTest(case=case["id"]):
                message = self.dispatch(case["target"], case["mutation"])
                self.assertTrue(message, f"mutation did not fail closed: {case['id']}")

    def test_duplicate_json_and_nonfinite_json_fail_closed(self) -> None:
        self.assertTrue(self.dispatch("loader", "duplicate_json"))
        self.assertTrue(self.dispatch("loader", "nonfinite_json"))

    def test_issues_are_deterministic_and_sorted(self) -> None:
        value = copy.deepcopy(self.synthetic)
        value["runtime"] = True
        issues = subject.validate_package(value, self.validator, canonical=False)
        self.assertEqual(issues, sorted(set(issues)))

    def test_manifest_is_strict_json(self) -> None:
        parsed = json.loads((FIXTURES / "mutation-cases.json").read_text(encoding="utf-8"))
        self.assertEqual(parsed, self.manifest)


if __name__ == "__main__":
    unittest.main()
