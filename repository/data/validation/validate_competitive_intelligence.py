#!/usr/bin/env python3
"""Validate the bounded C004 competitive-intelligence foundation offline."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

from validate_pd03a_pilot_prerequisite import (
    ROOT,
    ValidationConfigurationError,
    load_json,
    load_yaml,
    require_mapping,
    validate_schema,
)


CONTRACT_PATH = ROOT / "repository/data/contracts/competitive-intelligence.contract.yaml"
COMPETITOR_SCHEMA_PATH = ROOT / "repository/data/schemas/competitive-competitor.schema.json"
SCORE_SCHEMA_PATH = ROOT / "repository/data/schemas/competitive-score.schema.json"
ADVANTAGE_SCHEMA_PATH = ROOT / "repository/data/schemas/competitive-advantage.schema.json"
COMPETITOR_PATH = ROOT / "repository/data/registries/extensions/c004/competitors.yaml"
SCORE_PATH = ROOT / "repository/data/registries/extensions/c004/capability-scores.yaml"
ADVANTAGE_PATH = ROOT / "repository/data/registries/extensions/c004/damavand-advantages.yaml"
C002_CANDIDATE_PATH = ROOT / "repository/data/registries/extensions/c002/commercial-pilot-candidates.yaml"
C002_ADMIN_PATH = ROOT / "repository/data/registries/extensions/c002/product-administration-policies.yaml"
C002_ADMIN_CONTRACT_PATH = ROOT / "repository/data/contracts/product-administration-policy.contract.yaml"
C003_BASE_PATH = ROOT / "repository/data/registries/extensions/c003/founder-product-commerce-discovery-session-01.yaml"
C003_R1_PATH = ROOT / "repository/data/registries/extensions/c003r1/checkpoint03-evidence-and-pilot-readiness.yaml"
C003_R3_PATH = ROOT / "repository/data/registries/extensions/c003r2/201-51-founder-evidence-completion.yaml"
PRODUCT_ENTITIES_PATH = ROOT / "repository/data/registries/product-entities.yaml"
PD03A_PATH = ROOT / "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml"
CURRENT_STATE_PATH = ROOT / "docs/CURRENT_PROJECT_STATE.md"

EXPECTED_CONTRACT_DIGEST = "1d920e30a076767e3c30e576fa653cfe01e9769c712b34d5c2488c556b2b83d1"
EXPECTED_COMPETITOR_DIGEST = "c64f79d966f0006d2c3e438d707d834bd1b9cbb74841689d9a489c405ce54309"
EXPECTED_SCORE_DIGEST = "85f66a2baeb54ab28d4c49cffc17dcd5bf73c866381c4e57171b7c094b982207"
EXPECTED_ADVANTAGE_DIGEST = "14f5cf1baae795f017d6a33360a78c3659030c6846cb9295bc3fa8c10aca867e"
EXPECTED_COMPETITOR_SCHEMA_DIGEST = "9082845a7ab29dbe3be70423a8980342d773eeec67e62c7edd5f8842e189d2fd"
EXPECTED_SCORE_SCHEMA_DIGEST = "acc95bf3b0317061d4ca0968ff6acf063456e6ded54a2dc689e4ca93f5a0d1a8"
EXPECTED_ADVANTAGE_SCHEMA_DIGEST = "1ff79810acc5bbb84375b1c42ef7fa9a926de04663f931412194ff8036c365a7"

EXPECTED_COMPETITORS = [
    ("Steel Majlesi", "https://steelmajlesi.com/", "TIER_1"),
    ("Atropat", "https://atropatco.ir/", "TIER_1"),
    ("SteelRokh", "https://steelrokh.com/", "TIER_1"),
    ("Steel Sheet", "https://steel-sheet.ir/", "TIER_1"),
    ("Kia Steel", "https://kiasteel.com/", "TIER_1"),
    ("Sam Steel Shop", "https://shop.sam-steel.ir/", "TIER_1"),
    ("Ahan1", "https://ahan1.com/", "TIER_2"),
    ("MarkazeAhan", "https://www.markazeahan.com/", "TIER_2"),
    ("Pivan", "https://pivan.co/", "TIER_2"),
    ("Iromart", "https://iromart.com/", "TIER_2"),
    ("SteelRonic", "https://steelronic.com/", "TIER_2"),
    ("Saba Profile", "https://sabaprofile.com/", "TIER_2"),
    ("SteelParto", "https://steelparto.com/", "TIER_3"),
]

EXPECTED_DIMENSIONS = [
    "TAXONOMY_BREADTH", "TAXONOMY_CLARITY", "PRODUCT_DATA_RICHNESS", "DATA_CONSISTENCY",
    "PRODUCT_DISCOVERY", "NAVIGATION_SIMPLICITY", "SEARCH_CAPABILITY", "FILTERING_CAPABILITY",
    "VARIANT_SELECTION_UX", "PRODUCT_PAGE_QUALITY", "MOBILE_UX", "PERSIAN_RTL_QUALITY",
    "PRICING_UX", "INQUIRY_UX", "AVAILABILITY_COMMUNICATION", "CHECKOUT_COMMERCE_FLOW",
    "TECHNICAL_CONTENT", "SEO_ARCHITECTURE", "CRAWLABLE_COMMERCIAL_DATA",
    "EDUCATIONAL_CONTENT_DEPTH", "INTERNAL_LINKING", "TRUST_CREDIBILITY",
    "FITTINGS_CATALOG_DEPTH", "CALCULATOR_TOOLING", "RELATED_PRODUCT_SELLING",
    "OPERATOR_SALES_ASSIST_MODEL", "CRM_VISIBLE_BEHAVIOR", "MAINTAINABILITY_FRAGMENTATION_RISK",
]

EXPECTED_ADVANTAGES = [
    "UNIFIED_PRODUCT_FAMILY_UX", "CONTEXT_AWARE_COMMERCIAL_STATE", "SYSTEM_SELLING",
    "AVAILABILITY_TRUST_MODEL", "OPERATOR_CONTROLLED_COMMERCIAL_LAYER",
    "DATA_RICH_SIMPLE_UX", "PRODUCT_KNOWLEDGE_ARCHITECTURE", "TECHNICAL_CONTENT_AUTHORITY",
    "MOBILE_FIRST_PERSIAN_RTL_COMMERCE", "PRODUCT_CALCULATOR_PLATFORM",
]

EXPECTED_FALSE_AUTHORITY_KEYS = {
    "product_population_allowed", "sku_population_allowed", "availability_population_allowed",
    "current_or_public_price_allowed", "commerce_activation_allowed", "checkout_activation_allowed",
    "payment_activation_allowed", "wordpress_woocommerce_mutation_allowed", "hosting_mutation_allowed",
    "seo_page_publishing_allowed", "content_import_allowed", "competitor_image_download_or_reuse_allowed",
    "runtime_allowed", "staging_allowed", "deployment_allowed", "production_allowed",
    "c1_t03_reopen_allowed", "c003_a_start_allowed", "c003_b_start_allowed",
    "successor_mission_allowed", "merge_allowed",
}


def semantic_digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(encoded).hexdigest()


def safe_path(path: Path, label: str) -> Path:
    try:
        if path.is_symlink():
            raise ValidationConfigurationError(f"{label} must not be a symbolic link")
        if path.stat().st_size > 2_097_152:
            raise ValidationConfigurationError(f"{label} exceeds the 2 MiB input cap")
        resolved = path.resolve(strict=True)
    except FileNotFoundError as exc:
        raise ValidationConfigurationError(f"missing {label}: {path}") from exc
    if resolved != ROOT and ROOT not in resolved.parents:
        raise ValidationConfigurationError(f"{label} must remain inside the repository")
    return resolved


def load_package(
    contract_path: Path = CONTRACT_PATH,
    competitor_schema_path: Path = COMPETITOR_SCHEMA_PATH,
    score_schema_path: Path = SCORE_SCHEMA_PATH,
    advantage_schema_path: Path = ADVANTAGE_SCHEMA_PATH,
) -> tuple[dict[str, Any], Any, Any, Any]:
    contract = require_mapping(load_yaml(safe_path(contract_path, "C004 contract")), "C004 contract")
    if EXPECTED_CONTRACT_DIGEST != "TO_BE_FINALIZED" and semantic_digest(contract) != EXPECTED_CONTRACT_DIGEST:
        raise ValidationConfigurationError("C004 contract literal policy differs")
    competitor_schema = require_mapping(load_json(safe_path(competitor_schema_path, "competitor schema")), "competitor schema")
    score_schema = require_mapping(load_json(safe_path(score_schema_path, "score schema")), "score schema")
    advantage_schema = require_mapping(load_json(safe_path(advantage_schema_path, "advantage schema")), "advantage schema")
    for value, expected, label in (
        (competitor_schema, EXPECTED_COMPETITOR_SCHEMA_DIGEST, "competitor schema"),
        (score_schema, EXPECTED_SCORE_SCHEMA_DIGEST, "score schema"),
        (advantage_schema, EXPECTED_ADVANTAGE_SCHEMA_DIGEST, "advantage schema"),
    ):
        if expected != "TO_BE_FINALIZED" and semantic_digest(value) != expected:
            raise ValidationConfigurationError(f"C004 {label} literal policy differs")
    return contract, validate_schema(competitor_schema), validate_schema(score_schema), validate_schema(advantage_schema)


def _schema_issues(value: Any, validator: Any, label: str) -> list[str]:
    issues: list[str] = []
    for error in validator.iter_errors(value):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        issues.append(f"[SCHEMA_{label}] {location}: {error.message}")
    return issues


def _all_false(value: Any) -> bool:
    return isinstance(value, dict) and bool(value) and all(item is False for item in value.values())


def _load_founder_evidence() -> dict[str, dict[str, Any]]:
    base = require_mapping(load_yaml(safe_path(C003_BASE_PATH, "C003 base evidence")), "C003 base evidence")
    r1 = require_mapping(load_yaml(safe_path(C003_R1_PATH, "C003-R1 evidence")), "C003-R1 evidence")
    records = list(base.get("evidence_records", [])) + list(r1.get("evidence_delta", []))
    return {str(item.get("decision_code")): item for item in records if isinstance(item, dict) and item.get("decision_code")}


def _validate_regressions(add: Any) -> None:
    candidates = require_mapping(load_yaml(safe_path(C002_CANDIDATE_PATH, "C002 candidate registry")), "C002 candidate registry")
    admin = require_mapping(load_yaml(safe_path(C002_ADMIN_PATH, "C002 administration registry")), "C002 administration registry")
    admin_contract = require_mapping(load_yaml(safe_path(C002_ADMIN_CONTRACT_PATH, "C002 administration contract")), "C002 administration contract")
    c003 = require_mapping(load_yaml(safe_path(C003_R3_PATH, "C003-R3 evidence registry")), "C003-R3 evidence registry")
    base_entities = load_yaml(safe_path(PRODUCT_ENTITIES_PATH, "Product entity registry"))
    pd03a = require_mapping(load_yaml(safe_path(PD03A_PATH, "PD03A registry")), "PD03A registry")
    if candidates.get("candidates") != []:
        add("REGRESSION_C002_CANDIDATES", "C002 candidate registry must remain empty")
    if not isinstance(admin.get("policies"), list) or len(admin["policies"]) != 8:
        add("REGRESSION_C002_POLICIES", "C002 must retain exactly eight policy definitions")
    if admin.get("instances") != []:
        add("REGRESSION_C002_INSTANCES", "C002 policy-instance registry must remain empty")
    if admin_contract.get("invariants", {}).get("commerce_eligibility", {}).get("default_state") != "INQUIRY_ONLY":
        add("REGRESSION_COMMERCE", "C002 commerce default must remain INQUIRY_ONLY")
    readiness = c003.get("c002_readiness", {})
    if readiness.get("resolved_count") != 0 or readiness.get("unresolved_count") != 9:
        add("REGRESSION_C002_READINESS", "C003-R3 must retain C002 readiness 0/9")
    criterion = next((item for item in c003.get("missing_evidence_register", {}).get("items", []) if item.get("criterion_code") == "PRODUCT_DATA_COMPLETENESS"), {})
    if criterion.get("evidence_state") != "SUBMITTED" or criterion.get("status") != "OPEN_BLOCKING":
        add("REGRESSION_PRODUCT_DATA_COMPLETENESS", "Product Data Completeness must remain SUBMITTED / OPEN_BLOCKING")
    entities = list(base_entities) if isinstance(base_entities, list) else []
    entities.extend(pd03a.get("entities", []) if isinstance(pd03a.get("entities"), list) else [])
    if any(isinstance(item, dict) and item.get("entity_type") == "SKU" for item in entities):
        add("REGRESSION_SKU", "C004 cannot populate canonical SKU entities")
    effects = c003.get("selection_effects", {})
    if effects.get("commerce_state") != "INQUIRY_ONLY" or effects.get("runtime_state") != "NONE" or effects.get("production_state") != "NONE":
        add("REGRESSION_RUNTIME_COMMERCE", "C003-R3 commerce/runtime/production state must remain INQUIRY_ONLY/NONE/NONE")
    state_text = safe_path(CURRENT_STATE_PATH, "Current Project State").read_text(encoding="utf-8")
    if "C1-T03/HF-X0 = FROZEN_AT_PROTECTED_ARCHITECTURE_BOUNDARY" not in state_text:
        add("REGRESSION_C1_T03", "C1-T03 must remain frozen at the protected architecture boundary")


def validate_package(competitors: Any, scores: Any, advantages: Any, validators: tuple[Any, Any, Any], contract: dict[str, Any]) -> list[str]:
    issues: list[str] = []

    def add(code: str, message: str) -> None:
        issues.append(f"[{code}] {message}")

    cv, sv, av = validators
    issues.extend(_schema_issues(competitors, cv, "COMPETITOR"))
    issues.extend(_schema_issues(scores, sv, "SCORE"))
    issues.extend(_schema_issues(advantages, av, "ADVANTAGE"))
    if not all(isinstance(item, dict) for item in (competitors, scores, advantages)):
        return sorted(set(issues))

    digests = [EXPECTED_COMPETITOR_DIGEST, EXPECTED_SCORE_DIGEST, EXPECTED_ADVANTAGE_DIGEST]
    for value, expected, label in zip((competitors, scores, advantages), digests, ("COMPETITOR", "SCORE", "ADVANTAGE")):
        if expected != "TO_BE_FINALIZED" and semantic_digest(value) != expected:
            add(f"{label}_DIGEST", f"C004 {label.lower()} registry differs from the reviewed package")

    authority = contract.get("authority", {})
    if set(authority) != {"mission_id", "research_reconciliation_allowed", "architecture_planning_allowed"} | EXPECTED_FALSE_AUTHORITY_KEYS:
        add("CONTRACT_AUTHORITY_KEYS", "contract authority keys must match the exact reviewed C004 authority map")
    for key, value in authority.items():
        if key in {"mission_id", "research_reconciliation_allowed", "architecture_planning_allowed"}:
            continue
        if value is not False:
            add("CONTRACT_AUTHORITY", f"authority {key} must remain false")
    if authority.get("research_reconciliation_allowed") is not True or authority.get("architecture_planning_allowed") is not True:
        add("CONTRACT_SCOPE", "research reconciliation and architecture planning must be the only enabled mission capabilities")
    if not _all_false(competitors.get("authority_effects")):
        add("REGISTRY_AUTHORITY", "competitor registry authority effects must all be false")
    if advantages.get("implementation_authority") is not False:
        add("ADVANTAGE_AUTHORITY", "advantage planning cannot create implementation authority")

    competitor_records = competitors.get("competitors", [])
    actual_set = [(item.get("competitor_name"), item.get("domain"), item.get("competitor_tier")) for item in competitor_records if isinstance(item, dict)]
    if actual_set != EXPECTED_COMPETITORS:
        add("COMPETITOR_SET", "competitor identity/domain/tier order must match the authorized 13-site set")
    if Counter(item.get("competitor_tier") for item in competitor_records if isinstance(item, dict)) != Counter({"TIER_1": 6, "TIER_2": 6, "TIER_3": 1}):
        add("TIER_COUNTS", "competitor tier counts must be 6/6/1")

    competitor_ids: list[Any] = []
    competitor_by_id: dict[str, dict[str, Any]] = {}
    observations: dict[str, dict[str, Any]] = {}
    competitor_observations: dict[str, set[str]] = {}
    pattern_ids: list[Any] = []
    for index, competitor in enumerate(competitor_records, start=1):
        if not isinstance(competitor, dict):
            continue
        competitor_id = competitor.get("competitor_id")
        competitor_ids.append(competitor_id)
        competitor_by_id[str(competitor_id)] = competitor
        if competitor_id != f"comp:{index:012x}":
            add("COMPETITOR_ID", f"competitor {index} stable ID differs")
        refs: set[str] = set()
        for observation in competitor.get("observations", []):
            if not isinstance(observation, dict):
                continue
            observation_id = observation.get("observation_id")
            if observation_id in observations:
                add("DUPLICATE_OBSERVATION", f"duplicate observation ID {observation_id}")
            observations[observation_id] = observation
            refs.add(observation_id)
            for field in ("competitor_id", "competitor_name", "domain", "competitor_tier"):
                if observation.get(field) != competitor.get(field):
                    add("OBSERVATION_IDENTITY", f"observation {observation_id} {field} must match its competitor")
            unknown_dimensions = set(observation.get("score_dimensions", [])) - set(EXPECTED_DIMENSIONS)
            if unknown_dimensions:
                add("OBSERVATION_DIMENSION", f"observation {observation_id} declares unknown score dimensions")
            if observation.get("copyright_capture") != "ABSTRACTED_FEATURE_PRESENCE_ONLY":
                add("COPYRIGHT_BOUNDARY", f"observation {observation_id} exceeds abstract feature capture")
            if observation.get("evidence_status") == "VERIFIED" and observation.get("confidence") == "LOW":
                add("UNSUPPORTED_VERIFIED", f"observation {observation_id} cannot be VERIFIED with LOW confidence")
        competitor_observations[str(competitor_id)] = refs
        observation_states = [item.get("evidence_status") for item in competitor.get("observations", []) if isinstance(item, dict)]
        verification_status = competitor.get("verification_status")
        competitor_confidence = competitor.get("confidence")
        if verification_status == "UNVERIFIED" and any(state != "UNVERIFIED" for state in observation_states):
            add("UNVERIFIED_COMPETITOR", f"unverified competitor {competitor_id} cannot contain stronger observations")
        if verification_status == "UNVERIFIED" and competitor_confidence != "LOW":
            add("COMPETITOR_SUMMARY", f"unverified competitor {competitor_id} must have LOW confidence")
        if verification_status == "VERIFIED" and (competitor_confidence != "HIGH" or any(state in {"STALE", "UNVERIFIED"} for state in observation_states) or not any(state == "VERIFIED" for state in observation_states)):
            add("COMPETITOR_SUMMARY", f"verified competitor {competitor_id} requires HIGH confidence, verified evidence and no stale or unverified observations")
        if verification_status == "PARTIALLY_VERIFIED" and competitor_confidence == "HIGH" and all(state == "VERIFIED" for state in observation_states):
            add("COMPETITOR_SUMMARY", f"partially verified competitor {competitor_id} needs a visible confidence or observation limitation")
        for pattern in competitor.get("patterns", []):
            if not isinstance(pattern, dict):
                continue
            pattern_ids.append(pattern.get("pattern_id"))
            unknown = set(pattern.get("observation_refs", [])) - refs
            if unknown:
                add("PATTERN_REFERENCE", f"pattern {pattern.get('pattern_id')} has unknown or cross-competitor evidence")
    if len(set(competitor_ids)) != len(competitor_ids):
        add("DUPLICATE_COMPETITOR", "competitor IDs must be unique")
    if len(set(pattern_ids)) != len(pattern_ids):
        add("DUPLICATE_PATTERN", "pattern IDs must be unique")

    dimension_records = scores.get("dimensions", [])
    dimension_codes = [item.get("dimension_code") for item in dimension_records if isinstance(item, dict)]
    if dimension_codes != EXPECTED_DIMENSIONS:
        add("DIMENSION_ORDER", "all 28 score dimensions must be present in exact Mission order")
    score_records = scores.get("scores", [])
    if len(score_records) != 364:
        add("SCORE_COUNT", "C004 requires exactly 13 x 28 = 364 score records")
    score_ids: list[Any] = []
    seen_pairs: list[tuple[Any, Any]] = []
    for sequence, record in enumerate(score_records, start=1):
        if not isinstance(record, dict):
            continue
        score_ids.append(record.get("score_id"))
        expected_competitor = competitor_ids[(sequence - 1) // 28] if competitor_ids and sequence <= len(competitor_ids) * 28 else None
        expected_dimension = EXPECTED_DIMENSIONS[(sequence - 1) % 28]
        pair = (record.get("competitor_id"), record.get("dimension_code"))
        seen_pairs.append(pair)
        if record.get("score_id") != f"cscore:{sequence:012x}":
            add("SCORE_ID", f"score {sequence} stable ID differs")
        if pair != (expected_competitor, expected_dimension):
            add("SCORE_ORDER", f"score {sequence} must follow competitor then Mission dimension order")
        refs = set(record.get("evidence_refs", []))
        if not refs or refs - competitor_observations.get(str(record.get("competitor_id")), set()):
            add("SCORE_EVIDENCE", f"score {sequence} must cite its competitor's observation evidence")
        score = record.get("score")
        evidence_status = record.get("evidence_status")
        confidence = record.get("confidence")
        referenced = [observations.get(ref, {}) for ref in record.get("evidence_refs", [])]
        if record.get("observed_at") != competitors.get("observed_at") or any(item.get("observation_date") != record.get("observed_at") for item in referenced):
            add("SCORE_OBSERVED_AT", f"score {sequence} date must match the registry and all cited observations")
        if score is None and (evidence_status != "UNVERIFIED" or confidence != "LOW"):
            add("NULL_SCORE_STATUS", f"score {sequence} null value requires exactly UNVERIFIED / LOW")
        if score is not None:
            if evidence_status not in {"PARTIALLY_VERIFIED", "STALE"}:
                add("NUMERIC_SCORE_STATUS", f"score {sequence} numeric value requires PARTIALLY_VERIFIED or STALE evidence")
            if evidence_status == "STALE" and (confidence != "LOW" or any(item.get("evidence_status") != "STALE" for item in referenced)):
                add("STALE_SCORE", f"score {sequence} STALE value requires only stale evidence and LOW confidence")
            if evidence_status == "PARTIALLY_VERIFIED" and (confidence != "MEDIUM" or not any(item.get("evidence_status") in {"VERIFIED", "PARTIALLY_VERIFIED"} for item in referenced)):
                add("PARTIAL_SCORE", f"score {sequence} interpretive current value requires current evidence and MEDIUM confidence")
            if any(record.get("dimension_code") not in item.get("score_dimensions", []) for item in referenced):
                add("SCORE_DIMENSION_EVIDENCE", f"score {sequence} cites evidence that does not support its dimension")
        if not str(record.get("rationale", "")).strip():
            add("SCORE_RATIONALE", f"score {sequence} requires a rationale")
    if len(set(score_ids)) != len(score_ids) or len(set(seen_pairs)) != len(seen_pairs):
        add("DUPLICATE_SCORE", "score IDs and competitor/dimension pairs must be unique")
    if scores.get("aggregate_ranking") is not False:
        add("AGGREGATE_RANKING", "fake-precision aggregate ranking is prohibited")

    advantage_records = advantages.get("advantages", [])
    founder_evidence = _load_founder_evidence()
    if [item.get("advantage_code") for item in advantage_records if isinstance(item, dict)] != list("ABCDEFGHIJ"):
        add("ADVANTAGE_ORDER", "advantages A-J must be present in exact order")
    if [str(item.get("title", "")).upper().replace(" ", "_") for item in advantage_records if isinstance(item, dict)] != EXPECTED_ADVANTAGES:
        add("ADVANTAGE_SET", "the exact ten Mission advantages must be represented")
    advantage_ids: list[Any] = []
    for index, advantage in enumerate(advantage_records, start=1):
        if not isinstance(advantage, dict):
            continue
        advantage_ids.append(advantage.get("advantage_id"))
        if advantage.get("advantage_id") != f"cadv:{index:012x}" or advantage.get("implementation_authority") is not False:
            add("ADVANTAGE_ID_AUTHORITY", f"advantage {index} identity or authority differs")
        for basis in advantage.get("evidence_basis", []):
            if not isinstance(basis, dict):
                continue
            kind = basis.get("evidence_classification")
            reference = str(basis.get("reference", ""))
            if kind == "EXTERNAL_OBSERVATION" and reference not in observations:
                add("ADVANTAGE_EXTERNAL_EVIDENCE", f"advantage {index} has unresolved external observation")
            if kind == "FOUNDER_CONFIRMED":
                source = founder_evidence.get(reference)
                if source is None or source.get("evidence_classification") != "FOUNDER_CONFIRMED":
                    add("ADVANTAGE_FOUNDER_EVIDENCE", f"advantage {index} Founder evidence must resolve to canonical FOUNDER_CONFIRMED C003 evidence")
            if kind == "ARCHITECTURE_PROPOSAL" and not (reference.startswith("C004-") or reference.startswith("slack:")):
                add("ADVANTAGE_PROPOSAL_EVIDENCE", f"advantage {index} proposal basis must remain visibly non-Founder authority")
    if len(set(advantage_ids)) != 10:
        add("DUPLICATE_ADVANTAGE", "exactly ten unique advantage IDs are required")

    anti_patterns = advantages.get("anti_patterns", [])
    if len(anti_patterns) < 10 or len({item.get("anti_pattern_id") for item in anti_patterns if isinstance(item, dict)}) != len(anti_patterns):
        add("ANTI_PATTERN_SET", "at least ten unique anti-pattern records are required")
    for anti_pattern in anti_patterns:
        if not isinstance(anti_pattern, dict):
            continue
        if set(anti_pattern.get("evidence_refs", [])) - set(observations):
            add("ANTI_PATTERN_EVIDENCE", f"anti-pattern {anti_pattern.get('anti_pattern_id')} must cite existing observations")
    leadership = advantages.get("leadership_map", [])
    domains = [item.get("domain") for item in leadership if isinstance(item, dict)]
    if len(domains) != len(set(domains)):
        add("LEADER_DOMAIN", "leadership domains must be unique")
    for leader in leadership:
        if not isinstance(leader, dict):
            continue
        refs = set(leader.get("evidence_refs", []))
        leader_id = leader.get("competitor_id")
        status = leader.get("status")
        if refs - set(observations):
            add("LEADER_EVIDENCE", f"leadership record {leader.get('domain')} must cite existing observations")
        if status == "NO_RELIABLE_LEADER" and leader_id is not None:
            add("LEADER_STATUS", "NO_RELIABLE_LEADER must not name a competitor")
        if status in {"SUPPORTED_LEADER", "CANDIDATE_LEADER"} and leader_id is None:
            add("LEADER_STATUS", f"{status} must name a competitor")
        if leader_id is not None and (leader_id not in competitor_ids or refs - competitor_observations.get(str(leader_id), set())):
            add("LEADER_EVIDENCE", f"leadership record {leader.get('domain')} must cite the named competitor's evidence")
        if leader_id is not None:
            leader_competitor = competitor_by_id.get(str(leader_id), {})
            leader_observations = [observations.get(ref, {}) for ref in refs]
            if leader_competitor.get("confidence") == "LOW" or any(item.get("evidence_status") in {"STALE", "UNVERIFIED"} for item in leader_observations):
                add("STALE_OR_UNVERIFIED_LEADER", f"leadership record {leader.get('domain')} cannot be driven by stale, unverified or low-confidence evidence")
            if status == "SUPPORTED_LEADER" and (leader_competitor.get("verification_status") != "VERIFIED" or any(item.get("evidence_status") != "VERIFIED" or item.get("confidence") != "HIGH" for item in leader_observations)):
                add("SUPPORTED_LEADER_EVIDENCE", f"supported leader {leader.get('domain')} requires verified high-confidence current evidence")

    _validate_regressions(add)
    return sorted(set(issues))


def validate_files(
    competitor_path: Path = COMPETITOR_PATH,
    score_path: Path = SCORE_PATH,
    advantage_path: Path = ADVANTAGE_PATH,
    **schema_paths: Any,
) -> list[str]:
    contract, cv, sv, av = load_package(**schema_paths)
    competitors = load_yaml(safe_path(competitor_path, "competitor registry"))
    scores = load_yaml(safe_path(score_path, "score registry"))
    advantages = load_yaml(safe_path(advantage_path, "advantage registry"))
    return validate_package(competitors, scores, advantages, (cv, sv, av), contract)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--competitors", type=Path, default=COMPETITOR_PATH)
    parser.add_argument("--scores", type=Path, default=SCORE_PATH)
    parser.add_argument("--advantages", type=Path, default=ADVANTAGE_PATH)
    args = parser.parse_args()
    try:
        issues = validate_files(args.competitors, args.scores, args.advantages)
    except ValidationConfigurationError as exc:
        print(f"[CONFIGURATION] {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print("C004 competitive intelligence validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
