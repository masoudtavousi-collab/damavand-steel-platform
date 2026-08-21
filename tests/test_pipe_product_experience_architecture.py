from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import socket
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "repository/data/validation/validate_pipe_product_experience_architecture.py"
VALIDATION_DIR = VALIDATOR_PATH.parent
sys.path.insert(0, str(VALIDATION_DIR))
SPEC = importlib.util.spec_from_file_location("validate_pipe_product_experience_architecture", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class C006PipeProductExperienceArchitectureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema_validator, cls.contract = MODULE.load_validator()
        cls.canonical = MODULE.load_yaml(MODULE.REGISTRY_PATH)
        cls.mutations = json.loads(
            (ROOT / "tests/fixtures/c006-product-experience-architecture/mutation-cases.json").read_text(encoding="utf-8")
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

    def test_seventeen_mandatory_adversaries_and_audit_mutations_fail_closed(self):
        mandatory = {
            "FINISH_COLOR_COLLAPSE", "BRAND_OWNER_DUPLICATION", "DERIVED_ID_AS_MEASURED",
            "MASS_UNAUTHORIZED_PROMOTION", "MASS_IN_PRODUCT_IDENTITY",
            "AVAILABILITY_FROM_SUPPLIER_HABIT", "PRICE_IN_PRODUCT_TRUTH",
            "CARTESIAN_VARIANT_GENERATION", "UNSUPPORTED_SELECTOR_OPTION",
            "FALSE_MEDIA_INHERITANCE", "TUPLE_PAGE_EXPLOSION", "SELECTOR_STATE_INDEXED",
            "WOOCOMMERCE_AS_CANONICAL_OWNER", "PREMATURE_PURCHASE_CTA",
            "SERVICE_AS_PRODUCT_ATTRIBUTE", "UNKNOWN_AS_OUT_OF_STOCK",
            "ORDER_UNIT_PRICING_BASIS_COLLAPSE",
        }
        self.assertEqual(len(self.mutations), 45)
        self.assertEqual(len({case["name"] for case in self.mutations}), 45)
        self.assertTrue(mandatory.issubset({case["expected"] for case in self.mutations}))
        for case in self.mutations:
            with self.subTest(case=case["name"]):
                value = copy.deepcopy(self.canonical)
                target = value
                for part in case["path"][:-1]:
                    target = target[part]
                final = case["path"][-1]
                operation = case["operation"]
                if operation in {"replace", "add"}:
                    target[final] = case["value"]
                elif operation == "append":
                    target[final].append(case["value"])
                elif operation == "delete":
                    del target[final]
                else:
                    self.fail(f"unknown mutation operation: {operation}")
                self.assertIn(case["expected"], "\n".join(self.validate(value)))

    def test_exact_source_manifest_is_complete_and_non_promoting(self):
        manifest = self.canonical["source_manifest"]
        self.assertEqual([MODULE._actual_source(item) for item in manifest["sources"]], MODULE.EXPECTED_SOURCES)
        self.assertTrue(manifest["complete_threads_verified"])
        self.assertTrue(all(item["thread_complete"] for item in manifest["sources"]))
        self.assertTrue(all(item["promotion_effect"] is False for item in manifest["sources"]))

    def test_authority_owner_and_field_maps_are_exact(self):
        expected_authority = {key: True for key in MODULE.ALLOWED_AUTHORITY} | {
            key: False for key in MODULE.DENIED_AUTHORITY
        }
        self.assertEqual(self.canonical["authority_effects"], expected_authority)
        self.assertEqual([item["domain"] for item in self.canonical["owner_bindings"]], MODULE.EXPECTED_DOMAINS)
        self.assertEqual([item["canonical_owner"] for item in self.canonical["owner_bindings"]], MODULE.EXPECTED_OWNERS)
        self.assertEqual([item["field_key"] for item in self.canonical["semantic_fields"]], MODULE.EXPECTED_FIELD_KEYS)
        self.assertEqual(self.canonical["truth_class_vocabulary"], MODULE.EXPECTED_TRUTH_CLASSES)
        self.assertTrue(all(not item["writeback_allowed"] and not item["authority_transfer"] for item in self.canonical["owner_bindings"]))

    def test_four_appearance_semantics_and_separate_owner_links_are_exact(self):
        fields = {item["field_key"]: item for item in self.canonical["semantic_fields"]}
        self.assertEqual(
            [key for key in MODULE.EXPECTED_FIELD_KEYS if key in {"finish", "color", "appearance", "coating_method"}],
            ["finish", "color", "appearance", "coating_method"],
        )
        self.assertEqual(fields["brand"]["owner_domain"], "BRAND_IDENTITY")
        self.assertEqual(fields["brand"]["provenance_owner_domain"], "C002_BRAND_PROVENANCE")
        self.assertEqual(fields["cutting"]["owner_domain"], "SERVICE_POLICY")
        self.assertEqual(fields["customer_order_unit"]["owner_domain"], "CUSTOMER_ORDER_UNIT_POLICY")
        self.assertEqual(fields["pricing_basis"]["owner_domain"], "PRICING_BASIS_POLICY")
        self.assertEqual(self.canonical["variant_resolution"]["owner"], "VARIANT_RULE_SET")
        self.assertEqual(
            self.canonical["media_knowledge"]["media_precedence"],
            ["VARIANT_OVERRIDE", "APPEARANCE_OR_FINISH_OVERRIDE", "FAMILY_DEFAULT"],
        )

    def test_architecture_stays_empty_and_projection_only(self):
        self.assertEqual(self.canonical["mass_lifecycle"]["numeric_observation_count"], 0)
        self.assertEqual(self.canonical["pricing_boundary"]["current_price_value_count"], 0)
        self.assertFalse(self.canonical["woocommerce_projection"]["canonical_product_truth_owner"])
        self.assertFalse(self.canonical["woocommerce_projection"]["canonical_commerce_authority"])
        self.assertEqual(self.canonical["cta_boundary"]["commerce_state"], "INQUIRY_ONLY")
        self.assertFalse(self.canonical["cta_boundary"]["purchase_cta_enabled"])
        self.assertTrue(MODULE.FORBIDDEN_POPULATION_KEYS.isdisjoint(self.canonical))

    def test_duplicate_yaml_and_json_keys_fail_closed(self):
        fixtures = ROOT / "tests/fixtures/c006-product-experience-architecture"
        with self.assertRaises(Exception):
            MODULE.load_yaml(fixtures / "adversarial-duplicate-keys.yaml")
        with self.assertRaises(Exception):
            MODULE.load_validator(schema_path=fixtures / "adversarial-duplicate-keys.json")

    def test_remote_and_recursively_permissive_schemas_fail_closed(self):
        fixtures = ROOT / "tests/fixtures/c006-product-experience-architecture"
        for name, expected in [
            ("adversarial-remote-ref-schema.json", "REMOTE_SCHEMA_REF"),
            ("adversarial-permissive-schema.json", "PERMISSIVE_SCHEMA"),
        ]:
            with self.subTest(name=name):
                with self.assertRaisesRegex(Exception, expected):
                    MODULE.load_validator(schema_path=fixtures / name)

    def test_path_escape_symlink_and_byte_cap_fail_closed(self):
        with tempfile.NamedTemporaryFile() as outside:
            with self.assertRaisesRegex(Exception, "inside the repository"):
                MODULE.safe_path(Path(outside.name), "outside fixture")
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as temp_dir:
            link = Path(temp_dir) / "registry-link.yaml"
            link.symlink_to(MODULE.REGISTRY_PATH)
            with self.assertRaisesRegex(Exception, "symbolic link"):
                MODULE.safe_path(link, "symlink fixture")
        with tempfile.NamedTemporaryFile(dir=ROOT / "tests", delete=False) as oversized:
            oversized.write(b"x" * 2_000_001)
            oversized_path = Path(oversized.name)
        try:
            with self.assertRaisesRegex(Exception, "2 MB byte cap"):
                MODULE.safe_path(oversized_path, "oversized fixture")
        finally:
            oversized_path.unlink(missing_ok=True)

    def test_depth_node_and_nonfinite_inputs_fail_closed(self):
        deep_value = {}
        cursor = deep_value
        for index in range(105):
            cursor[str(index)] = {}
            cursor = cursor[str(index)]
        self.assertIn("INPUT_DEPTH", "\n".join(MODULE.audit_value(deep_value)))
        self.assertIn("INPUT_NODE_CAP", "\n".join(MODULE.audit_value([None] * 50_001)))
        value = copy.deepcopy(self.canonical)
        value["regression_anchors"]["numeric_mass_count"] = float("nan")
        self.assertIn("NON_FINITE", "\n".join(self.validate(value)))

    def test_dependency_pin_corruption_fails_closed(self):
        contract = copy.deepcopy(self.contract)
        contract["base_pins"]["c005_registry_semantic_sha256"] = "0" * 64
        issues = []
        MODULE.validate_dependency_pins(lambda code, message: issues.append(f"[{code}] {message}"), contract)
        self.assertIn("BASE_PIN_REGRESSION", "\n".join(issues))

    def test_semantic_digests_are_fully_pinned_after_independent_review(self):
        self.assertEqual(
            MODULE.EXPECTED_CONTRACT_DIGEST,
            "131b2c79a3d017c65bac896e95e7a638164a77b821546e5217266f6d3829dcc0",
        )
        self.assertEqual(
            MODULE.EXPECTED_SCHEMA_DIGEST,
            "9a9009c4431c097c062dcef81fad03fae51784ff466bb8cc5db6ed14237f79e3",
        )
        self.assertEqual(
            MODULE.EXPECTED_REGISTRY_DIGEST,
            "5b5510af1b521daa7b2539007cab0681885f2bbc3eff4a75dde67cb38857ad8b",
        )
        self.assertEqual(MODULE.semantic_digest(self.contract), MODULE.EXPECTED_CONTRACT_DIGEST)
        self.assertEqual(
            MODULE.semantic_digest(MODULE.load_json(MODULE.SCHEMA_PATH)),
            MODULE.EXPECTED_SCHEMA_DIGEST,
        )
        self.assertEqual(MODULE.semantic_digest(self.canonical), MODULE.EXPECTED_REGISTRY_DIGEST)


if __name__ == "__main__":
    unittest.main()
