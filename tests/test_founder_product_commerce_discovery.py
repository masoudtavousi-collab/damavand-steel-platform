from __future__ import annotations

from collections import Counter
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_DIR = ROOT / "repository/data/validation"
VALIDATOR_PATH = VALIDATION_DIR / "validate_founder_product_commerce_discovery.py"
FIXTURES = ROOT / "tests/fixtures/c003-founder-discovery"

sys.path.insert(0, str(VALIDATION_DIR))
spec = importlib.util.spec_from_file_location("c003_discovery", VALIDATOR_PATH)
assert spec and spec.loader
subject = importlib.util.module_from_spec(spec)
spec.loader.exec_module(subject)


class FounderProductCommerceDiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator, cls.contract = subject.load_validator()
        cls.canonical = subject.load_yaml(subject.REGISTRY_PATH)
        cls.mutations = json.loads((FIXTURES / "mutation-cases.json").read_text(encoding="utf-8"))

    def render(self, value: object) -> str:
        return "\n".join(subject.validate_registry(value, self.validator, self.contract))

    def test_positive_canonical_package(self) -> None:
        self.assertEqual(subject.validate_registry(self.canonical, self.validator, self.contract), [])

    def test_positive_exact_counts_and_source_order(self) -> None:
        records = self.canonical["evidence_records"]
        self.assertEqual(len(records), 115)
        self.assertEqual(
            Counter(item["evidence_classification"] for item in records),
            Counter(subject.EXPECTED_CLASSIFICATION_COUNTS),
        )
        self.assertEqual(
            Counter(item["temporal_role"] for item in records),
            Counter(subject.EXPECTED_TEMPORAL_COUNTS),
        )
        self.assertEqual([item["sequence"] for item in records], list(range(1, 116)))
        self.assertEqual(subject._render_sources(self.canonical["mission_sources"]), subject.EXPECTED_MISSION_SOURCES)
        self.assertEqual(subject._render_sources(self.canonical["discovery_sources"]), subject.EXPECTED_DISCOVERY_SOURCES)

    def test_positive_supplier_stated_is_proposal_only(self) -> None:
        record = self.canonical["evidence_records"][34]
        self.assertEqual(record["evidence_classification"], "ARCHITECTURE_PROPOSAL")
        self.assertEqual(
            record["proposed_extension_state"],
            "PROPOSED_EXTENSION_REQUIRING_SEPARATE_REVIEW",
        )
        self.assertTrue(record["requires_separate_contract_version"])
        self.assertTrue(record["requires_separate_promotion_authority"])
        c002 = subject.load_yaml(subject.C002_ADMIN_CONTRACT_PATH)
        self.assertEqual(
            c002["invariants"]["mass_provenance"]["methods"],
            subject.EXPECTED_C002_MASS_METHODS,
        )

    def test_positive_future_role_is_independent_from_founder_classification(self) -> None:
        records = self.canonical["evidence_records"]
        founder_future = {30, 46, 50, 52, 60, 101, 102, 104, 107, 111}
        accepted_candidate_future = {93}
        for record in records:
            if record["sequence"] in founder_future:
                self.assertEqual(record["ledger_class"], "FCF")
                self.assertEqual(record["evidence_classification"], "FOUNDER_CONFIRMED")
                self.assertEqual(record["temporal_role"], "FUTURE_CONCEPT")
            elif record["sequence"] in accepted_candidate_future:
                self.assertEqual(record["ledger_class"], "FACF")
                self.assertEqual(record["evidence_classification"], "FOUNDER_ACCEPTED_CANDIDATE")
                self.assertEqual(record["temporal_role"], "FUTURE_CONCEPT")
        self.assertIn("freight receipts in their account", records[110]["statement"])
        self.assertIn("loyalty club", records[100]["statement"])
        self.assertIn("Points Ledger", records[104]["statement"])
        self.assertIn("Tuesday special", records[51]["statement"])

    def test_positive_protected_price_record_contains_no_amount(self) -> None:
        record = self.canonical["evidence_records"][38]
        self.assertEqual(
            record["protected_source_locator"],
            "slack:C0BNHRRTE9F:1786929285.156489:record:039",
        )
        serialized = json.dumps(record, ensure_ascii=False)
        self.assertFalse(subject._contains_protected_price_value(serialized))
        self.assertFalse(record["authority_effects"]["current_price"])
        self.assertFalse(record["authority_effects"]["public_price"])
        self.assertFalse(record["authority_effects"]["pricing_authority"])

    def test_positive_synthetic_control_manifest(self) -> None:
        control = subject.load_yaml(FIXTURES / "valid-synthetic.yaml")
        self.assertEqual(control["data_classification"], "SYNTHETIC_FIXTURE")
        self.assertEqual(control["expected_record_count"], 115)
        self.assertEqual((ROOT / control["subject_path"]).resolve(), subject.REGISTRY_PATH.resolve())
        self.assertEqual(subject.validate_file(ROOT / control["subject_path"]), [])

    def test_contract_digest_is_fail_closed(self) -> None:
        self.assertEqual(subject._semantic_digest(self.contract), subject.EXPECTED_CONTRACT_DIGEST)
        drift = copy.deepcopy(self.contract)
        drift["authority"]["runtime_allowed"] = True
        self.assertNotEqual(subject._semantic_digest(drift), subject.EXPECTED_CONTRACT_DIGEST)

    def dispatch_mutation(self, mutation_id: str) -> str:
        value = copy.deepcopy(self.canonical)
        records = value["evidence_records"]
        if mutation_id == "M01_SOURCE_MISSING":
            value["discovery_sources"].pop()
        elif mutation_id == "M02_SOURCE_TIMESTAMP":
            value["discovery_sources"][0]["timestamp"] = "1786929259.000000"
        elif mutation_id == "M03_PART6_CONTRIBUTES":
            value["discovery_sources"][6]["contributes_new_records"] = True
        elif mutation_id == "M04_RECORD_MISSING":
            records.pop()
        elif mutation_id == "M05_SEQUENCE":
            records[0]["sequence"] = 2
        elif mutation_id == "M06_EVIDENCE_ID":
            records[0]["evidence_id"] = "fdisc:ffffffffffff"
        elif mutation_id == "M07_DECISION_CODE":
            records[0]["decision_code"] = "C003-DISC-002"
        elif mutation_id == "M08_SOURCE_ORDER":
            records[0]["source_order"] = 2
        elif mutation_id == "M09_LEDGER_CLASS":
            records[0]["ledger_class"] = "AP"
        elif mutation_id == "M10_CLASSIFICATION":
            records[0]["evidence_classification"] = "ARCHITECTURE_PROPOSAL"
        elif mutation_id == "M11_TEMPORAL_ROLE":
            records[0]["temporal_role"] = "FUTURE_CONCEPT"
        elif mutation_id == "M12_AUTHORITY_TRUE":
            records[0]["authority_effects"]["runtime"] = True
        elif mutation_id == "M13_SOURCE_SCOPE":
            records[0]["source_scope"] = "PARTIAL"
        elif mutation_id == "M14_SUPPLIER_STATE_MISSING":
            del records[34]["proposed_extension_state"]
        elif mutation_id == "M15_SUPPLIER_OWNER":
            records[34]["canonical_owner"] = "DISCOVERY_BACKLOG_ONLY"
        elif mutation_id == "M16_SUPPLIER_FIELD_OUTSIDE_035":
            records[35]["proposed_extension_state"] = "PROPOSED_EXTENSION_REQUIRING_SEPARATE_REVIEW"
        elif mutation_id == "M17_PROTECTED_LOCATOR_MISSING":
            records[38]["protected_source_locator"] = None
        elif mutation_id == "M18_PROTECTED_PRICE_VALUE":
            records[38]["statement"] += " " + "".join(("57", "0", ",", "0" * 3))
        elif mutation_id == "M19_TOPIC_MISSING":
            for record in records:
                if record["topic_code"] == "SMART_HISTORY":
                    record["topic_code"] = "PRODUCT_ADMIN"
        elif mutation_id == "M20_SUMMARY_COUNT":
            value["evidence_summary"]["record_count"] = 114
        elif mutation_id == "M21_BOUNDARY_TRUE":
            value["boundary"]["commerce_activation"] = True
        elif mutation_id == "M22_ADDITIONAL_PROPERTY":
            records[0]["unexpected"] = True
        elif mutation_id == "M23_DUPLICATE_ID":
            records[1]["evidence_id"] = records[0]["evidence_id"]
        elif mutation_id == "M24_STATUS":
            value["status"] = "RUNTIME_READY"
        elif mutation_id == "M25_AVAILABILITY_OWNER":
            records[60]["canonical_owner"] = "C002_COMMERCE_ELIGIBILITY"
        elif mutation_id == "M26_PRODUCT_CLASS_INHERITANCE":
            records[71]["statement"] = "Direct-purchase eligibility may be inherited from Product class."
        elif mutation_id == "M27_FOUNDER_FUTURE_DOWNGRADE":
            records[29]["ledger_class"] = "FUT"
            records[29]["evidence_classification"] = "ARCHITECTURE_PROPOSAL"
        elif mutation_id == "M28_CANDIDATE_FUTURE_DOWNGRADE":
            records[92]["ledger_class"] = "FUT"
            records[92]["evidence_classification"] = "ARCHITECTURE_PROPOSAL"
        elif mutation_id == "M29_FOUNDER_FUTURE_LEDGER_MISMATCH":
            records[100]["ledger_class"] = "FUT"
        else:
            self.fail(f"undispatched mutation: {mutation_id}")
        return self.render(value)

    def test_negative_mutation_manifest_is_complete_and_fail_closed(self) -> None:
        self.assertEqual(len(self.mutations), 29)
        seen: set[str] = set()
        for mutation in self.mutations:
            mutation_id = mutation["id"]
            with self.subTest(mutation=mutation_id):
                self.assertNotIn(mutation_id, seen)
                seen.add(mutation_id)
                self.assertTrue(self.dispatch_mutation(mutation_id))

    def test_adversarial_duplicate_yaml_keys_rejected(self) -> None:
        with self.assertRaises(subject.ValidationConfigurationError):
            subject.load_yaml(FIXTURES / "adversarial-duplicate-keys.yaml")

    def test_adversarial_permissive_and_remote_schemas_rejected(self) -> None:
        for name in ("adversarial-permissive-schema.json", "adversarial-remote-ref-schema.json"):
            with self.subTest(schema=name), self.assertRaises(subject.ValidationConfigurationError):
                subject.load_validator(schema_path=FIXTURES / name)

    def test_adversarial_non_finite_and_unsafe_paths_rejected(self) -> None:
        value = copy.deepcopy(self.canonical)
        value["evidence_records"][0]["sequence"] = float("nan")
        self.assertTrue(self.render(value))
        with self.assertRaises(subject.ValidationConfigurationError):
            subject.validate_file(Path("/etc/hosts"))
        with tempfile.TemporaryDirectory(prefix="c003-symlink-") as directory:
            symlink = Path(directory) / "registry.yaml"
            symlink.symlink_to(subject.REGISTRY_PATH)
            with self.assertRaises(subject.ValidationConfigurationError):
                subject.validate_file(symlink)

    def test_deterministic_errors_and_cli(self) -> None:
        value = copy.deepcopy(self.canonical)
        value["evidence_records"][0]["authority_effects"]["runtime"] = True
        first = subject.validate_registry(value, self.validator, self.contract)
        second = subject.validate_registry(value, self.validator, self.contract)
        self.assertEqual(first, second)
        self.assertEqual(first, sorted(set(first)))
        result = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH)], cwd=ROOT, text=True,
            capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        synthetic = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), str(FIXTURES / "valid-synthetic.yaml"), "--synthetic"],
            cwd=ROOT, text=True, capture_output=True, check=False,
        )
        self.assertEqual(synthetic.returncode, 0, synthetic.stdout + synthetic.stderr)


if __name__ == "__main__":
    unittest.main()
