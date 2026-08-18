from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import socket
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "repository/data/validation/validate_valid_combination_evidence_matrix.py"
VALIDATION_DIR = VALIDATOR_PATH.parent
import sys
sys.path.insert(0, str(VALIDATION_DIR))
SPEC = importlib.util.spec_from_file_location("validate_valid_combination_evidence_matrix", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ValidCombinationEvidenceMatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema_validator, cls.contract = MODULE.load_validator()
        cls.canonical = MODULE.load_yaml(MODULE.REGISTRY_PATH)
        cls.mutations = json.loads(
            (ROOT / "tests/fixtures/c003r2-201-51-evidence-completion/mutation-cases.json").read_text(encoding="utf-8")
        )

    def validate(self, value):
        return MODULE.validate_registry(value, self.schema_validator, self.contract)

    def test_canonical_package_passes_deterministically_without_network(self):
        before = MODULE.semantic_digest(self.canonical)
        with patch.object(socket, "socket", side_effect=AssertionError("network forbidden")):
            first = self.validate(copy.deepcopy(self.canonical))
            second = self.validate(copy.deepcopy(self.canonical))
        self.assertEqual(first, [])
        self.assertEqual(first, second)
        self.assertEqual(before, MODULE.semantic_digest(MODULE.load_yaml(MODULE.REGISTRY_PATH)))

    def test_all_counted_mutations_fail_closed(self):
        self.assertEqual(len(self.mutations), 52)
        self.assertEqual(len({case["name"] for case in self.mutations}), 52)
        for case in self.mutations:
            with self.subTest(case=case["name"]):
                value = copy.deepcopy(self.canonical)
                target = value
                for part in case["path"][:-1]:
                    target = target[part]
                final = case["path"][-1]
                operation = case["operation"]
                if operation == "replace":
                    target[final] = case["value"]
                elif operation == "add":
                    target[final] = case["value"]
                elif operation == "delete":
                    del target[final]
                elif operation == "append":
                    target[final].append(case["value"])
                elif operation == "pop":
                    target[final].pop()
                else:
                    self.fail(f"unknown operation: {operation}")
                rendered = "\n".join(self.validate(value))
                self.assertIn(case["expected"], rendered)

    def test_duplicate_yaml_keys_fail_closed(self):
        path = ROOT / "tests/fixtures/c003r2-201-51-evidence-completion/adversarial-duplicate-keys.yaml"
        with self.assertRaises(Exception):
            MODULE.load_yaml(path)

    def test_duplicate_json_keys_fail_closed(self):
        path = ROOT / "tests/fixtures/c003r2-201-51-evidence-completion/adversarial-duplicate-keys.json"
        with self.assertRaises(Exception):
            MODULE.load_json(path)

    def test_remote_and_nested_permissive_schemas_fail_closed(self):
        fixture_dir = ROOT / "tests/fixtures/c003r2-201-51-evidence-completion"
        for name, expected in [
            ("adversarial-remote-ref-schema.json", "REMOTE_SCHEMA_REF"),
            ("adversarial-permissive-schema.json", "PERMISSIVE_SCHEMA"),
        ]:
            with self.subTest(name=name):
                with self.assertRaisesRegex(Exception, expected):
                    MODULE.load_validator(schema_path=fixture_dir / name)

    def test_path_escape_and_symlink_fail_closed(self):
        with tempfile.NamedTemporaryFile() as outside:
            with self.assertRaisesRegex(Exception, "inside the repository"):
                MODULE.safe_path(Path(outside.name), "outside fixture")
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as temp_dir:
            link = Path(temp_dir) / "registry-link.yaml"
            link.symlink_to(MODULE.REGISTRY_PATH)
            with self.assertRaisesRegex(Exception, "symbolic link"):
                MODULE.safe_path(link, "symlink fixture")
        with tempfile.NamedTemporaryFile(dir=ROOT / "tests", delete=False) as oversized:
            oversized.write(b"x" * (2_000_001))
            oversized_path = Path(oversized.name)
        try:
            with self.assertRaisesRegex(Exception, "2 MB byte cap"):
                MODULE.safe_path(oversized_path, "oversized fixture")
        finally:
            oversized_path.unlink(missing_ok=True)

    def test_input_and_schema_depth_caps_fail_closed(self):
        deep_value = {}
        cursor = deep_value
        for index in range(105):
            cursor[str(index)] = {}
            cursor = cursor[str(index)]
        self.assertIn("INPUT_DEPTH", "\n".join(MODULE.audit_value(deep_value)))
        deep_schema = {"type": "object", "additionalProperties": False, "properties": {}}
        cursor = deep_schema["properties"]
        for index in range(105):
            cursor[str(index)] = {"type": "object", "additionalProperties": False, "properties": {}}
            cursor = cursor[str(index)]["properties"]
        self.assertIn("SCHEMA_DEPTH", "\n".join(MODULE.audit_schema(deep_schema)))

    def test_nonfinite_input_fails_closed(self):
        value = copy.deepcopy(self.canonical)
        value["valid_combination_evidence_matrix"]["unknown_count"] = float("nan")
        self.assertIn("NON_FINITE", "\n".join(self.validate(value)))

    def test_compressed_matrix_counts_216_unknown_without_persisted_expansion(self):
        matrix = self.canonical["valid_combination_evidence_matrix"]
        expanded = {
            (brand, thickness, row["appearance"], row["length_m"])
            for row in matrix["rows"]
            for brand in row["brand"]["values"]
            for thickness in row["thickness"]["values_mm"]
        }
        self.assertEqual(len(expanded), 216)
        self.assertEqual(matrix["unknown_count"], 216)
        self.assertEqual(matrix["inferred_tuple_count"], 0)
        self.assertFalse(matrix["persisted_expanded_tuple_rows"])
        self.assertNotIn("expanded_tuples", MODULE.REGISTRY_PATH.read_text(encoding="utf-8"))

    def test_question_plan_is_six_unanswered_brand_items(self):
        plan = self.canonical["founder_question_compression_plan"]
        self.assertEqual([item["brand"] for item in plan["review_items"]], MODULE.EXPECTED_BRANDS)
        self.assertEqual(len(plan["review_items"]), 6)
        for item in plan["review_items"]:
            self.assertEqual(len(item["groups"]), 3)
            self.assertTrue(all(group["answer_mode"] == "UNANSWERED" for group in item["groups"]))
            self.assertTrue(all(group["evidence_state"] == "UNKNOWN" for group in item["groups"]))

    def test_future_question_semantics_are_total_disjoint_and_evidence_bound(self):
        evidence = {
            "source_locator": "founder-evidence:future-authorized-answer",
            "evidence_classification": "FOUNDER_CONFIRMED",
            "temporal_role": "CURRENT_INTENT",
            "founder_confirmed": True,
            "captured_at": "2026-08-18T10:00:00Z",
            "reviewer_reference": "role:repository-guardian",
            "reviewed_at": "2026-08-18T10:05:00Z",
            "review_status": "VERIFIED",
            "promotion_effect": False,
        }
        group = copy.deepcopy(self.canonical["founder_question_compression_plan"]["review_items"][0]["groups"][0])
        group.update({
            "answer_mode": "EXPLICIT_STATE_SETS",
            "supported_thicknesses_mm": ["0.45"],
            "invalid_thicknesses_mm": ["0.50"],
            "not_applicable_thicknesses_mm": ["0.55"],
            "evidence_state": "UNKNOWN",
        })
        self.assertEqual(MODULE.validate_answer_semantics(group, evidence), [])
        overlap = copy.deepcopy(group)
        overlap["invalid_thicknesses_mm"].append("0.45")
        self.assertIn("QUESTION_STATE_OVERLAP", "\n".join(MODULE.validate_answer_semantics(overlap, evidence)))
        reversed_order = copy.deepcopy(group)
        reversed_order["supported_thicknesses_mm"] = ["0.50", "0.45"]
        self.assertIn("QUESTION_STATE_ORDER", "\n".join(MODULE.validate_answer_semantics(reversed_order, evidence)))
        self.assertIn("QUESTION_EVIDENCE_BINDING", "\n".join(MODULE.validate_answer_semantics(group, None)))
        all_valid = copy.deepcopy(group)
        all_valid.update({
            "answer_mode": "ALL_LISTED_CONFIRMED_VALID",
            "supported_thicknesses_mm": MODULE.EXPECTED_THICKNESSES,
            "invalid_thicknesses_mm": [],
            "not_applicable_thicknesses_mm": [],
            "evidence_state": "CONFIRMED_VALID",
        })
        self.assertEqual(MODULE.validate_answer_semantics(all_valid, evidence), [])

    def test_typed_future_mass_and_supply_items_are_closed_and_fail_closed(self):
        mass = {
            "observation_id": "c003r2mass:000000000001",
            "variant_context": {
                "pilot_key": "STAINLESS_ROUND_PIPE__GRADE_201__DIAMETER_51_MM",
                "grade": "201", "diameter_mm": "51", "brand": "Sumwin", "thickness_mm": "0.45",
                "appearance": "STEEL_NATURAL_GLOSSY", "length_m": "6.00", "missing_context_fields": [],
            },
            "observed_mass_decimal": "3.620",
            "unit_reference": "unit:000000000003",
            "unit_status_at_capture": "CANDIDATE_UNVERIFIED",
            "batch_or_load_date": "2026-08-18",
            "supplier_or_source": "protected:supplier:example",
            "operator_reference": "role:operator",
            "source_channel": "MANUFACTURER_DOCUMENT",
            "proposed_c002_mass_method": "MANUFACTURER_STATED",
            "c002_method_validation_state": "UNVALIDATED_C002_INTAKE_ONLY",
            "supplier_stated_method_allowed": False,
            "source_locator": "protected:evidence:example",
            "previous_observation_reference": None,
            "current_suggestion": False,
            "confirmed_by_operator": True,
            "canonical_or_variant_effect": False,
        }
        supply = {
            "supply_evidence_id": "c003r2supply:000000000001",
            "supplier_or_source": "protected:supplier:example",
            "confirmation_channel": "WHATSAPP",
            "confirmation_timestamp": "2026-08-18T10:00:00Z",
            "valid_from": "2026-08-18T10:00:00Z",
            "valid_until": "2026-08-20T10:00:00Z",
            "tuple_scope": {
                "representation": "EXACT_TUPLE_LIST",
                "tuples": [{"brand": "Sumwin", "thickness_mm": "0.45", "appearance": "STEEL_NATURAL_GLOSSY", "length_m": "6.00"}],
                "omitted_tuple_state": "UNKNOWN",
                "cartesian_generation_allowed": False,
            },
            "evidence_source_locator": "protected:supply-evidence:example",
            "evidence_classification": "SUPPLIER_DOCUMENT",
            "temporal_role": "CURRENT_OBSERVATION",
            "reviewer_reference": "role:repository-guardian",
            "reviewed_at": "2026-08-18T10:05:00Z",
            "evidence_status": "VERIFIED",
            "availability_effect": False,
            "stock_effect": False,
        }
        candidate = copy.deepcopy(self.canonical)
        candidate["mass_evidence_intake"]["observations"] = [mass]
        candidate["supply_evidence_intake"]["records"] = [supply]
        self.assertEqual(list(self.schema_validator.iter_errors(candidate)), [])
        self.assertEqual(MODULE.validate_future_mass_observation(mass), [])
        self.assertEqual(MODULE.validate_future_supply_record(supply), [])
        bad_mass = copy.deepcopy(mass)
        bad_mass["variant_context"]["thickness_mm"] = None
        self.assertIn("MASS_CONTEXT_MISSINGNESS", "\n".join(MODULE.validate_future_mass_observation(bad_mass)))
        supplier_method = copy.deepcopy(mass)
        supplier_method["source_channel"] = "SUPPLIER_COMMUNICATION"
        supplier_method["proposed_c002_mass_method"] = "SUPPLIER_STATED"
        supplier_issues = "\n".join(MODULE.validate_future_mass_observation(supplier_method))
        self.assertIn("MASS_METHOD_OWNER", supplier_issues)
        self.assertIn("MASS_SUPPLIER_METHOD_INFERENCE", supplier_issues)
        bad_supply = copy.deepcopy(supply)
        bad_supply["valid_from"] = "2026-08-21T10:00:00Z"
        self.assertIn("SUPPLY_VALIDITY_WINDOW", "\n".join(MODULE.validate_future_supply_record(bad_supply)))
        missing_source = copy.deepcopy(supply)
        missing_source["evidence_source_locator"] = ""
        self.assertIn("SUPPLY_SOURCE_BINDING", "\n".join(MODULE.validate_future_supply_record(missing_source)))
        ambiguous_scope = copy.deepcopy(supply)
        ambiguous_scope["tuple_scope"] = {
            "brands": ["Sumwin", "Sansco"],
            "thicknesses_mm": ["0.45", "0.50"],
            "appearances": ["STEEL_NATURAL_GLOSSY"],
            "lengths_m": ["6.00"],
        }
        self.assertIn("SUPPLY_SCOPE", "\n".join(MODULE.validate_future_supply_record(ambiguous_scope)))
        out_of_universe = copy.deepcopy(supply)
        out_of_universe["tuple_scope"]["tuples"][0]["length_m"] = "3.00"
        self.assertIn("SUPPLY_TUPLE_UNIVERSE", "\n".join(MODULE.validate_future_supply_record(out_of_universe)))
        reverse_order = copy.deepcopy(supply)
        reverse_order["tuple_scope"]["tuples"] = [
            {"brand": "Sumwin", "thickness_mm": "0.50", "appearance": "STEEL_NATURAL_GLOSSY", "length_m": "6.00"},
            {"brand": "Sumwin", "thickness_mm": "0.45", "appearance": "STEEL_NATURAL_GLOSSY", "length_m": "6.00"},
        ]
        self.assertIn("SUPPLY_TUPLE_ORDER", "\n".join(MODULE.validate_future_supply_record(reverse_order)))

    def test_mass_owner_contract_remains_exact_and_supplier_stated_is_not_promoted(self):
        live = MODULE.load_yaml(MODULE.C002_ADMIN_CONTRACT_PATH)
        self.assertEqual(live["invariants"]["mass_provenance"]["methods"], MODULE.EXPECTED_C002_MASS_METHODS)
        self.assertEqual(self.contract["mass_evidence"]["approved_c002_methods"], MODULE.EXPECTED_C002_MASS_METHODS)
        self.assertFalse(self.contract["mass_evidence"]["supplier_stated_method_allowed"])

    def test_c003r1_and_c002_semantic_pins_match_live_owners(self):
        pins = self.contract["base_pins"]
        expected = {
            "c003_r1_contract_semantic_sha256": MODULE.semantic_digest(MODULE.load_yaml(MODULE.c003r1.CONTRACT_PATH)),
            "c003_r1_registry_semantic_sha256": MODULE.semantic_digest(MODULE.load_yaml(MODULE.c003r1.REGISTRY_PATH)),
            "c002_candidate_contract_semantic_sha256": MODULE.semantic_digest(MODULE.load_yaml(MODULE.C002_CANDIDATE_CONTRACT_PATH)),
            "c002_candidate_registry_semantic_sha256": MODULE.semantic_digest(MODULE.load_yaml(MODULE.C002_CANDIDATE_REGISTRY_PATH)),
            "c002_product_administration_contract_semantic_sha256": MODULE.semantic_digest(MODULE.load_yaml(MODULE.C002_ADMIN_CONTRACT_PATH)),
            "c002_product_administration_registry_semantic_sha256": MODULE.semantic_digest(MODULE.load_yaml(MODULE.C002_ADMIN_REGISTRY_PATH)),
        }
        self.assertEqual(pins, expected)

    def test_c002_readiness_mass_supply_and_authority_remain_zero(self):
        self.assertEqual(self.canonical["c002_readiness"]["resolved_count"], 0)
        self.assertEqual(self.canonical["c002_readiness"]["unresolved_count"], 9)
        self.assertEqual(self.canonical["mass_evidence_intake"]["observations"], [])
        self.assertEqual(self.canonical["supply_evidence_intake"]["records"], [])
        self.assertTrue(all(value is False for value in self.canonical["authority_effects"].values()))


if __name__ == "__main__":
    unittest.main()
