from __future__ import annotations

from collections import Counter
import copy
import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_DIR = ROOT / "repository/data/validation"
VALIDATOR_PATH = VALIDATION_DIR / "validate_competitive_intelligence.py"
FIXTURES = ROOT / "tests/fixtures/c004-competitive-intelligence"

sys.path.insert(0, str(VALIDATION_DIR))
spec = importlib.util.spec_from_file_location("c004_competitive_intelligence", VALIDATOR_PATH)
assert spec and spec.loader
subject = importlib.util.module_from_spec(spec)
spec.loader.exec_module(subject)


class CompetitiveIntelligenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract, cls.cv, cls.sv, cls.av = subject.load_package()
        cls.competitors = subject.load_yaml(subject.COMPETITOR_PATH)
        cls.scores = subject.load_yaml(subject.SCORE_PATH)
        cls.advantages = subject.load_yaml(subject.ADVANTAGE_PATH)
        cls.mutations = json.loads((FIXTURES / "mutation-cases.json").read_text(encoding="utf-8"))

    def render(self, competitors: object, scores: object, advantages: object) -> str:
        return "\n".join(subject.validate_package(
            competitors, scores, advantages, (self.cv, self.sv, self.av), self.contract
        ))

    def test_positive_canonical_package_and_exact_counts(self) -> None:
        self.assertEqual(self.render(self.competitors, self.scores, self.advantages), "")
        records = self.competitors["competitors"]
        self.assertEqual(len(records), 13)
        self.assertEqual(Counter(item["competitor_tier"] for item in records), Counter({"TIER_1": 6, "TIER_2": 6, "TIER_3": 1}))
        self.assertEqual(Counter(item["verification_status"] for item in records), Counter({"VERIFIED": 8, "PARTIALLY_VERIFIED": 5}))
        self.assertEqual(len(self.scores["dimensions"]), 28)
        self.assertEqual(len(self.scores["scores"]), 364)
        self.assertEqual(len(self.advantages["advantages"]), 10)

    def test_positive_score_and_status_discipline(self) -> None:
        self.assertFalse(self.scores["aggregate_ranking"])
        for item in self.scores["scores"]:
            self.assertTrue(item["rationale"])
            self.assertTrue(item["evidence_refs"])
            if item["score"] is None:
                self.assertEqual((item["evidence_status"], item["confidence"]), ("UNVERIFIED", "LOW"))
            else:
                self.assertIn(item["score"], range(6))
                self.assertIn(item["evidence_status"], {"PARTIALLY_VERIFIED", "STALE"})
        iromart = "comp:00000000000a"
        iromart_scores = [item for item in self.scores["scores"] if item["competitor_id"] == iromart]
        self.assertTrue(all(item["evidence_status"] == "STALE" for item in iromart_scores if item["score"] is not None and item["dimension_code"] != "TRUST_CREDIBILITY"))
        self.assertEqual(next(item for item in iromart_scores if item["dimension_code"] == "TRUST_CREDIBILITY")["score"], 0)

    def test_positive_advantage_dispositions_and_class_separation(self) -> None:
        counts = Counter(item["recommended_status"] for item in self.advantages["advantages"])
        self.assertEqual(counts, Counter({"USE_NOW": 7, "PLAN_NOW_IMPLEMENT_LATER": 3}))
        classes = {basis["evidence_classification"] for item in self.advantages["advantages"] for basis in item["evidence_basis"]}
        self.assertEqual(classes, {"EXTERNAL_OBSERVATION", "FOUNDER_CONFIRMED", "ARCHITECTURE_PROPOSAL"})
        self.assertTrue(all(item["implementation_authority"] is False for item in self.advantages["advantages"]))
        advantage_c = next(item for item in self.advantages["advantages"] if item["advantage_code"] == "C")
        current_source = next(item for item in advantage_c["evidence_basis"] if item["reference"] == "slack:C0BNHRRTE9F:1787056479.144299")
        self.assertEqual((current_source["evidence_classification"], current_source["temporal_role"]), ("FOUNDER_CONFIRMED", "CURRENT_INTENT"))
        advantage_d = next(item for item in self.advantages["advantages"] if item["advantage_code"] == "D")
        self.assertEqual(advantage_d["recommended_status"], "USE_NOW")
        claims = " ".join(basis["claim"] for item in self.advantages["advantages"] for basis in item["evidence_basis"]).casefold()
        self.assertNotIn("does not own a warehouse", claims)
        self.assertNotIn("has no own warehouse", claims)

    def test_positive_exact_authority_map(self) -> None:
        authority = self.contract["authority"]
        self.assertEqual(
            set(authority),
            {"mission_id", "research_reconciliation_allowed", "architecture_planning_allowed"}
            | subject.EXPECTED_FALSE_AUTHORITY_KEYS,
        )
        self.assertTrue(all(authority[key] is False for key in subject.EXPECTED_FALSE_AUTHORITY_KEYS))
        drift = copy.deepcopy(self.contract)
        drift["authority"].pop("hosting_mutation_allowed")
        self.assertIn("CONTRACT_AUTHORITY_KEYS", "\n".join(subject.validate_package(
            self.competitors, self.scores, self.advantages, (self.cv, self.sv, self.av), drift
        )))

    def test_positive_synthetic_pointer(self) -> None:
        control = subject.load_yaml(FIXTURES / "valid-synthetic.yaml")
        self.assertEqual(control["data_classification"], "SYNTHETIC_FIXTURE")
        self.assertEqual(control["expected"], {"competitor_count": 13, "score_count": 364, "advantage_count": 10, "authority_effects": False})
        with mock.patch.object(socket.socket, "connect", side_effect=AssertionError("network call attempted")):
            self.assertEqual(subject.validate_files(), [])

    def test_semantic_digests_are_fail_closed(self) -> None:
        expected = (
            subject.EXPECTED_CONTRACT_DIGEST,
            subject.EXPECTED_COMPETITOR_SCHEMA_DIGEST,
            subject.EXPECTED_SCORE_SCHEMA_DIGEST,
            subject.EXPECTED_ADVANTAGE_SCHEMA_DIGEST,
            subject.EXPECTED_COMPETITOR_DIGEST,
            subject.EXPECTED_SCORE_DIGEST,
            subject.EXPECTED_ADVANTAGE_DIGEST,
        )
        actual = tuple(subject.semantic_digest(item) for item in (
            self.contract,
            subject.load_json(subject.COMPETITOR_SCHEMA_PATH),
            subject.load_json(subject.SCORE_SCHEMA_PATH),
            subject.load_json(subject.ADVANTAGE_SCHEMA_PATH),
            self.competitors,
            self.scores,
            self.advantages,
        ))
        self.assertNotIn("TO_BE_FINALIZED", expected)
        self.assertEqual(actual, expected)
        drift = copy.deepcopy(self.contract)
        drift["authority"]["runtime_allowed"] = True
        self.assertNotEqual(subject.semantic_digest(drift), actual[0])

    def dispatch_mutation(self, mutation_id: str) -> str:
        competitors = copy.deepcopy(self.competitors)
        scores = copy.deepcopy(self.scores)
        advantages = copy.deepcopy(self.advantages)
        cs = competitors["competitors"]
        ss = scores["scores"]
        aa = advantages["advantages"]
        ap = advantages["anti_patterns"]
        leaders = advantages["leadership_map"]
        if mutation_id == "M01_COMPETITOR_MISSING": cs.pop()
        elif mutation_id == "M02_TIER_COUNT": cs[0]["competitor_tier"] = "TIER_2"
        elif mutation_id == "M03_VERIFIED_LOW_CONFIDENCE": cs[0]["observations"][0]["confidence"] = "LOW"
        elif mutation_id == "M04_DUPLICATE_OBSERVATION": cs[1]["observations"][0]["observation_id"] = cs[0]["observations"][0]["observation_id"]
        elif mutation_id == "M05_COPYRIGHT_CAPTURE": cs[0]["observations"][0]["copyright_capture"] = "COPIED_TABLE"
        elif mutation_id == "M06_COMPETITOR_AUTHORITY": competitors["authority_effects"]["runtime"] = True
        elif mutation_id == "M07_COMPETITOR_ADDITIONAL_PROPERTY": cs[0]["unexpected"] = True
        elif mutation_id == "M08_PATTERN_CROSS_REFERENCE": cs[0]["patterns"][0]["observation_refs"] = [cs[1]["observations"][0]["observation_id"]]
        elif mutation_id == "M09_COMPETITOR_ID_ORDER": cs[0]["competitor_id"] = "comp:ffffffffffff"
        elif mutation_id == "M10_SCORE_MISSING": ss.pop()
        elif mutation_id == "M11_DIMENSION_ORDER": scores["dimensions"][0], scores["dimensions"][1] = scores["dimensions"][1], scores["dimensions"][0]
        elif mutation_id == "M12_SCORE_RANGE": ss[0]["score"] = 6
        elif mutation_id == "M13_NULL_PARTIAL": ss[0]["score"] = None
        elif mutation_id == "M14_NUMERIC_UNVERIFIED": ss[0]["evidence_status"] = "UNVERIFIED"
        elif mutation_id == "M15_EMPTY_RATIONALE": ss[0]["rationale"] = ""
        elif mutation_id == "M16_UNKNOWN_EVIDENCE": ss[0]["evidence_refs"] = ["cobs:ffffffffffff"]
        elif mutation_id == "M17_CROSS_COMPETITOR_EVIDENCE": ss[0]["evidence_refs"] = [cs[1]["observations"][0]["observation_id"]]
        elif mutation_id == "M18_AGGREGATE_RANKING": scores["aggregate_ranking"] = True
        elif mutation_id == "M19_SCORE_ORDER": ss[0], ss[1] = ss[1], ss[0]
        elif mutation_id == "M20_DUPLICATE_SCORE_ID": ss[1]["score_id"] = ss[0]["score_id"]
        elif mutation_id == "M21_ADVANTAGE_CODE_ORDER": aa[0]["advantage_code"], aa[1]["advantage_code"] = aa[1]["advantage_code"], aa[0]["advantage_code"]
        elif mutation_id == "M22_ADVANTAGE_SET": aa[0]["title"] = "COPIED COMPETITOR FEATURE"
        elif mutation_id == "M23_FOUNDER_REFERENCE": aa[0]["evidence_basis"][2]["reference"] = "C004-UNSUPPORTED-FOUNDER"
        elif mutation_id == "M24_EXTERNAL_REFERENCE": aa[0]["evidence_basis"][0]["reference"] = "cobs:ffffffffffff"
        elif mutation_id == "M25_IMPLEMENTATION_AUTHORITY": advantages["implementation_authority"] = True
        elif mutation_id == "M26_ANTI_PATTERN_COUNT": del ap[-3:]
        elif mutation_id == "M27_DUPLICATE_ANTI_PATTERN": ap[1]["anti_pattern_id"] = ap[0]["anti_pattern_id"]
        elif mutation_id == "M28_STALE_LEADER": leaders[0]["competitor_id"] = "comp:00000000000a"; leaders[0]["evidence_refs"] = ["cobs:000000000023"]
        elif mutation_id == "M29_LEADER_CROSS_REFERENCE": leaders[0]["evidence_refs"] = ["cobs:00000000000a"]
        elif mutation_id == "M30_ADVANTAGE_ADDITIONAL_PROPERTY": aa[0]["implementation_plan"] = "NOW"
        elif mutation_id == "M31_PATTERN_ID_DUPLICATE": cs[1]["patterns"][0]["pattern_id"] = cs[0]["patterns"][0]["pattern_id"]
        elif mutation_id == "M32_SCORE_PAIR_DUPLICATE": ss[1]["competitor_id"] = ss[0]["competitor_id"]; ss[1]["dimension_code"] = ss[0]["dimension_code"]
        elif mutation_id == "M33_OBSERVATION_IDENTITY": cs[0]["observations"][0]["competitor_name"] = "Wrong owner"
        elif mutation_id == "M34_OBSERVATION_DIMENSION": cs[0]["observations"][0]["score_dimensions"] = ["UNREVIEWED_DIMENSION"]
        elif mutation_id == "M35_SCORE_DIMENSION_EVIDENCE": ss[0]["dimension_code"] = "CRM_VISIBLE_BEHAVIOR"
        elif mutation_id == "M36_NUMERIC_VERIFIED": ss[0]["evidence_status"] = "VERIFIED"; ss[0]["confidence"] = "HIGH"
        elif mutation_id == "M37_SCORE_OBSERVED_AT": ss[0]["observed_at"] = "2026-08-17"
        elif mutation_id == "M38_NULL_STATUS": next(item for item in ss if item["score"] is None)["evidence_status"] = "NOT_APPLICABLE"
        elif mutation_id == "M39_COMPETITOR_SUMMARY": cs[9]["verification_status"] = "VERIFIED"; cs[9]["confidence"] = "HIGH"
        elif mutation_id == "M40_FAKE_FOUNDER_REFERENCE": aa[0]["evidence_basis"][2]["reference"] = "C003-FAKE"
        elif mutation_id == "M41_PROPOSAL_AS_FOUNDER": aa[0]["evidence_basis"][2]["reference"] = "C003-DISC-004"
        elif mutation_id == "M42_SUPPORTED_LEADER_NULL": leaders[0]["competitor_id"] = None
        elif mutation_id == "M43_NO_LEADER_UNKNOWN_REFERENCE": next(item for item in leaders if item["status"] == "NO_RELIABLE_LEADER")["evidence_refs"] = ["cobs:ffffffffffff"]
        elif mutation_id == "M44_DUPLICATE_LEADER_DOMAIN": leaders[1]["domain"] = leaders[0]["domain"]
        elif mutation_id == "M45_ANTI_UNKNOWN_REFERENCE": ap[0]["evidence_refs"] = ["cobs:ffffffffffff"]
        elif mutation_id == "M46_PARTIAL_SUPPORTED_LEADER": next(item for item in leaders if item["competitor_id"] == "comp:000000000006")["status"] = "SUPPORTED_LEADER"
        elif mutation_id == "M47_STALE_CURRENT_REFERENCE": ss[0]["evidence_status"] = "STALE"; ss[0]["confidence"] = "LOW"
        elif mutation_id == "M48_PARTIAL_HIGH_CONFIDENCE": ss[0]["confidence"] = "HIGH"
        elif mutation_id == "M49_DIRECT_FOUNDER_TEMPORAL": next(item for item in aa[2]["evidence_basis"] if item["reference"].startswith("slack:"))["temporal_role"] = "HISTORICAL_EXAMPLE_NONCURRENT"
        elif mutation_id == "M50_WAREHOUSE_OWNERSHIP_CLAIM": aa[3]["evidence_basis"][2]["claim"] = "Damavand does not own a warehouse."
        elif mutation_id == "M51_AVAILABILITY_FOUNDER_ESCALATION": aa[3]["recommended_status"] = "NEEDS_FOUNDER_DECISION"
        elif mutation_id == "M52_AVAILABILITY_ABSOLUTE_STOCK_BAN": next(item for item in ap if item["anti_pattern_id"] == "canti:00000000000a")["damavand_prevention_rule"] = "Never claim stock."
        else: self.fail(f"undispatched mutation: {mutation_id}")
        return self.render(competitors, scores, advantages)

    def test_negative_mutation_manifest_is_complete_and_fail_closed(self) -> None:
        self.assertEqual(len(self.mutations), 52)
        seen: set[str] = set()
        for mutation in self.mutations:
            mutation_id = mutation["id"]
            with self.subTest(mutation=mutation_id):
                self.assertNotIn(mutation_id, seen)
                seen.add(mutation_id)
                output = self.dispatch_mutation(mutation_id)
                self.assertIn(mutation["expected_code"], output)

    def test_adversarial_duplicate_keys_rejected(self) -> None:
        with self.assertRaises(subject.ValidationConfigurationError):
            subject.load_yaml(FIXTURES / "adversarial-duplicate-keys.yaml")

    def test_adversarial_permissive_and_remote_schemas_rejected(self) -> None:
        for name in ("adversarial-permissive-schema.json", "adversarial-remote-ref-schema.json"):
            with self.subTest(schema=name), self.assertRaises(subject.ValidationConfigurationError):
                subject.load_package(competitor_schema_path=FIXTURES / name)

    def test_adversarial_nonfinite_paths_symlinks_and_byte_cap(self) -> None:
        scores = copy.deepcopy(self.scores)
        scores["scores"][0]["score"] = float("nan")
        self.assertIn("SCHEMA_SCORE", self.render(self.competitors, scores, self.advantages))
        with self.assertRaises(subject.ValidationConfigurationError):
            subject.validate_files(competitor_path=Path("/etc/hosts"))
        with tempfile.TemporaryDirectory(dir=ROOT, prefix="c004-test-") as directory:
            directory_path = Path(directory)
            symlink = directory_path / "competitors.yaml"
            symlink.symlink_to(subject.COMPETITOR_PATH)
            with self.assertRaises(subject.ValidationConfigurationError):
                subject.validate_files(competitor_path=symlink)
            oversized = directory_path / "oversized.yaml"
            oversized.write_bytes(b"x" * 2_097_153)
            with self.assertRaises(subject.ValidationConfigurationError):
                subject.safe_path(oversized, "oversized adversary")
            regression_symlink = directory_path / "c002-candidates.yaml"
            regression_symlink.symlink_to(subject.C002_CANDIDATE_PATH)
            with mock.patch.object(subject, "C002_CANDIDATE_PATH", regression_symlink), self.assertRaises(subject.ValidationConfigurationError):
                subject.validate_package(
                    self.competitors, self.scores, self.advantages,
                    (self.cv, self.sv, self.av), self.contract,
                )

    def test_deterministic_errors_and_cli(self) -> None:
        competitors = copy.deepcopy(self.competitors)
        competitors["authority_effects"]["runtime"] = True
        first = self.render(competitors, self.scores, self.advantages)
        second = self.render(competitors, self.scores, self.advantages)
        self.assertEqual(first, second)
        result = subprocess.run([sys.executable, str(VALIDATOR_PATH)], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
