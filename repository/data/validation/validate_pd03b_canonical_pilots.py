#!/usr/bin/env python3
"""Validate the exact PD-03B canonical pilot set offline and fail closed."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from typing import Any

from validate_pd03a_pilot_prerequisite import (
    ROOT,
    ValidationConfigurationError,
    collect_ids,
    load_json,
    load_yaml,
    require_mapping,
    validate_schema,
    walk,
)


CONTRACT_PATH = ROOT / "repository/data/contracts/pd03b-canonical-pilot.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/pd03b-canonical-pilot.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/pd03b/canonical-pilots.yaml"
IDENTITY_REGISTRY_PATHS = tuple(
    ROOT / path
    for path in (
        "repository/data/registries/attribute-categories.yaml",
        "repository/data/registries/attribute-data-types.yaml",
        "repository/data/registries/attribute-requirement-levels.yaml",
        "repository/data/registries/attribute-units.yaml",
        "repository/data/registries/extensions/pd03a/approval-evidence.yaml",
        "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml",
        "repository/data/registries/extensions/pd03b/approval-evidence.yaml",
        "repository/data/registries/extensions/pd03b/canonical-pilots.yaml",
        "repository/data/registries/measurement-dimensions.yaml",
        "repository/data/registries/product-attribute-profiles.yaml",
        "repository/data/registries/product-attribute-value-registries.yaml",
        "repository/data/registries/product-attributes.yaml",
        "repository/data/registries/product-data-approval-evidence.yaml",
        "repository/data/registries/product-data-localized-labels.yaml",
        "repository/data/registries/product-entities.yaml",
        "repository/data/registries/product-entity-types.yaml",
        "repository/data/registries/product-statuses.yaml",
    )
)
EXPECTED_IDS = {
    "pilot:b12aa359af76",
    "pilot:8a1546edb732",
    "pilot:f5922666261e",
}
EXPECTED_REFERENCES = {
    ("GOLD-PIPE-201-16-035-6M", "PIPE-COMB-0001", "16", "0.35", "6"),
    ("GOLD-PIPE-201-38-050-6M", "PIPE-COMB-0016", "38", "0.50", "6"),
    ("GOLD-PIPE-201-51-050-6M", "PIPE-COMB-0023", "51", "0.50", "6"),
}
EXPECTED_RECORD_BY_ID = {
    "pilot:b12aa359af76": ("GOLD-PIPE-201-16-035-6M", "PIPE-COMB-0001", "16", "0.35", "6"),
    "pilot:8a1546edb732": ("GOLD-PIPE-201-38-050-6M", "PIPE-COMB-0016", "38", "0.50", "6"),
    "pilot:f5922666261e": ("GOLD-PIPE-201-51-050-6M", "PIPE-COMB-0023", "51", "0.50", "6"),
}
PROHIBITED_FIELDS = {
    "product", "product_id", "sku", "commercial_sku", "slug", "availability",
    "availability_value", "supply_status", "stock", "inventory", "price", "offer",
    "master_data", "golden_package", "wordpress_id", "woocommerce_id", "import",
    "runtime", "deploy", "deployment", "production",
}
EXPECTED_PROVENANCE = {
    "source_type": "FOUNDER_DECISION",
    "source_references": [
        "FD-PILOT-001", "FD-PD03A-001",
        "task:019fa05e-1889-79b3-8e83-9477cd1648c6",
    ],
    "captured_by": "role:product-data-steward",
    "captured_at": "2026-08-01T00:00:00Z",
    "evidence_status": "FOUNDER_APPROVED_EXACT_NO_CLAIM_TUPLES",
}


def collect_reference_ids(value: Any) -> set[str]:
    """Collect stable identifier values from every governed registry shape."""
    ids = collect_ids(value)
    for node in walk(value):
        if not isinstance(node, dict):
            continue
        for key, item in node.items():
            if (
                isinstance(item, str)
                and (key.endswith("_id") or key in {"value_id", "entity_id"})
                and re.search(r":[0-9a-f]{12}$", item)
            ):
                ids.add(item)
    return ids


def lifecycle_status(contract: dict[str, Any]) -> str:
    lifecycle = require_mapping(contract.get("lifecycle"), "PD-03B lifecycle")
    history = {
        "DRAFT": [],
        "REVIEW": [{"from": "DRAFT", "to": "REVIEW", "evidence_reference": "PD03B-TECH-REVIEW-001"}],
        "APPROVED": [
            {"from": "DRAFT", "to": "REVIEW", "evidence_reference": "PD03B-TECH-REVIEW-001"},
            {"from": "REVIEW", "to": "APPROVED", "evidence_reference": "FD-PD03B-001"},
        ],
    }
    status = lifecycle.get("current_status")
    required_keys = {
        "decision_id", "current_status", "allowed_transition_sequence", "transition_history",
        "direct_draft_to_approved_forbidden", "approval_evidence_required",
        "technical_reviewed_sha", "technical_review_artifact_sha256",
    }
    if (
        set(lifecycle) != required_keys
        or lifecycle.get("decision_id") != "FD-PD03B-001"
        or lifecycle.get("allowed_transition_sequence") != ["DRAFT", "REVIEW", "APPROVED"]
        or lifecycle.get("direct_draft_to_approved_forbidden") is not True
        or lifecycle.get("approval_evidence_required") is not True
        or status not in history
        or lifecycle.get("transition_history") != history[status]
    ):
        raise ValidationConfigurationError("PD-03B lifecycle is invalid")
    reviewed_sha = lifecycle.get("technical_reviewed_sha")
    artifact_sha = lifecycle.get("technical_review_artifact_sha256")
    if status == "DRAFT" and (reviewed_sha is not None or artifact_sha is not None):
        raise ValidationConfigurationError("DRAFT cannot contain technical PASS binding")
    if status in {"REVIEW", "APPROVED"} and (
        re.fullmatch(r"[0-9a-f]{40}", str(reviewed_sha)) is None
        or re.fullmatch(r"[0-9a-f]{64}", str(artifact_sha)) is None
    ):
        raise ValidationConfigurationError("REVIEW/APPROVED requires exact technical PASS binding")
    return str(status)


def load_validator(
    contract_path: Path = CONTRACT_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> tuple[Any, dict[str, Any], str]:
    contract = require_mapping(load_yaml(contract_path), "PD-03B contract")
    expected_keys = {
        "contract_id", "contract_version", "record_kind", "schema", "registry", "baseline",
        "lifecycle", "identity_policy", "exact_scope", "attribute_references",
        "measurement_policy", "status_policy", "provenance_policy", "roles", "validation",
        "prohibited",
    }
    if set(contract) != expected_keys:
        raise ValidationConfigurationError("PD-03B contract keys differ from exact policy")
    if contract.get("contract_id") != "pd03b-canonical-pilot" or contract.get("contract_version") != "1.0.0":
        raise ValidationConfigurationError("PD-03B contract identity differs")
    if contract.get("record_kind") != "canonical-pilot-record-set":
        raise ValidationConfigurationError("PD-03B record kind differs")
    if contract.get("baseline") != {
        "repository": "masoudtavousi-collab/damavand-steel-platform",
        "main_sha": "e72c32bdb041448d34c925c969fe01a2156f9e1d",
        "immutable_prerequisite_decision": "FD-PD03A-001",
    }:
        raise ValidationConfigurationError("PD-03B baseline differs")
    if contract.get("schema") != {
        "path": "repository/data/schemas/pd03b-canonical-pilot.schema.json",
        "draft": "https://json-schema.org/draft/2020-12/schema",
    } or contract.get("registry") != {
        "path": "repository/data/registries/extensions/pd03b/canonical-pilots.yaml",
    }:
        raise ValidationConfigurationError("PD-03B path policy differs")
    exact = require_mapping(contract.get("exact_scope"), "PD-03B exact scope")
    if exact.get("pilot_record_count") != 3 or exact.get("canonical_set_id") != "pilotset:36c1085ffbe9":
        raise ValidationConfigurationError("PD-03B exact count or set identity differs")
    if exact.get("tuple_lexemes") != [
        ["201", "silver", "16", "0.35", "6"],
        ["201", "silver", "38", "0.50", "6"],
        ["201", "silver", "51", "0.50", "6"],
    ]:
        raise ValidationConfigurationError("PD-03B exact tuples differ")
    if contract.get("status_policy") != {
        "record_status_by_lifecycle": {
            "DRAFT": "CANDIDATE_UNVERIFIED", "REVIEW": "CANDIDATE_UNVERIFIED", "APPROVED": "APPROVED",
        },
        "availability_status": "MISSING_DATA_VALUE",
        "cartesian_generation_forbidden": True,
        "import_ready": False, "runtime_ready": False, "golden_ready": False,
    }:
        raise ValidationConfigurationError("PD-03B status/readiness policy differs")
    if contract.get("provenance_policy") != EXPECTED_PROVENANCE:
        raise ValidationConfigurationError("PD-03B provenance policy differs")
    expected_sections = {
        "identity_policy": {
            "set_id_pattern": "^pilotset:[0-9a-f]{12}$",
            "pilot_id_pattern": "^pilot:[0-9a-f]{12}$",
            "allocation": "CSPRNG_12_HEX_WITH_GLOBAL_COLLISION_CHECK",
            "immutable": True,
            "historical_references_are_identity": False,
            "labels_slugs_skus_are_identity": False,
        },
        "attribute_references": {
            "material": "attr:dbf5365ee1e5", "grade": "attr:28565665c910",
            "finish": "attr:1926e2ad4629", "diameter": "attr:252ab175be12",
            "thickness": "attr:d1890e85f84c", "length": "attr:d782d47eae7f",
        },
        "measurement_policy": {
            "diameter": {"unit_id": "unit:000000000002", "precision": 0},
            "thickness": {"unit_id": "unit:000000000002", "precision": 2},
            "length": {"unit_id": "unit:000000000001", "precision": 0},
        },
        "roles": {
            "decision_authority": "Founder پروژه Damavand Steel",
            "data_steward": "product-data-steward", "executor": "codex-build-engine",
            "technical_reviewer": "repository-guardian-independent",
            "qa_and_rollback_owner": "repository-guardian", "ai_domain_authority": False,
        },
        "validation": {
            "offline_only": True, "network_allowed": False, "side_effects_allowed": False,
            "exact_contract_required": True, "exact_three_records_required": True,
            "cross_file_reference_resolution_required": True,
            "duplicate_json_or_yaml_keys_rejected": True,
            "non_finite_numbers_rejected": True,
            "remote_or_permissive_schema_rejected": True,
            "mutation_manifest_dispatch_required": True,
        },
        "prohibited": [
            "product", "sku", "commercial_sku", "slug", "availability_value",
            "supply_status", "stock", "inventory", "price", "offer", "master_data",
            "golden_package", "additional_candidate_rows", "cartesian_generation",
            "wordpress", "woocommerce", "import", "runtime", "deploy", "production",
            "branch_deletion", "technical_standard_claim", "tolerance_claim",
            "quality_claim", "application_claim",
        ],
    }
    for section, expected in expected_sections.items():
        if contract.get(section) != expected:
            raise ValidationConfigurationError(f"PD-03B contract section differs: {section}")
    expected_exact = {
        "pilot_record_count": 3, "canonical_set_id": "pilotset:36c1085ffbe9",
        "series_entity_id": "prd:series:e1657d35ac35",
        "variant_rule_set_entity_id": "prd:variant-rule-set:eb255662accc",
        "profile_id": "pprof:4c556c63c1a9",
        "fixed_material_term_id": "vterm:5ff9c0ceca39",
        "grade_term_id": "vterm:a891bfdfdd6b", "finish_term_id": "vterm:1df9a5493546",
        "axes": ["grade", "finish", "diameter", "thickness", "length"],
        "fixed_non_axis": ["material"],
        "tuple_lexemes": [
            ["201", "silver", "16", "0.35", "6"],
            ["201", "silver", "38", "0.50", "6"],
            ["201", "silver", "51", "0.50", "6"],
        ],
        "historical_references": [
            {"golden_reference": "GOLD-PIPE-201-16-035-6M", "combination_reference": "PIPE-COMB-0001"},
            {"golden_reference": "GOLD-PIPE-201-38-050-6M", "combination_reference": "PIPE-COMB-0016"},
            {"golden_reference": "GOLD-PIPE-201-51-050-6M", "combination_reference": "PIPE-COMB-0023"},
        ],
    }
    if exact != expected_exact:
        raise ValidationConfigurationError("PD-03B exact scope differs")
    schema = require_mapping(load_json(schema_path), "PD-03B schema")
    return validate_schema(schema), contract, lifecycle_status(contract)


def validate_bundle(value: Any, lifecycle: str, validator: Any) -> list[str]:
    issues: list[str] = []

    def add(code: str, message: str) -> None:
        issues.append(f"[{code}] {message}")

    for error in validator.iter_errors(value):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        add("SCHEMA_VALIDATION", f"{location}: {error.message}")
    if not isinstance(value, dict):
        return sorted(set(issues))
    expected_status = "APPROVED" if lifecycle == "APPROVED" else "CANDIDATE_UNVERIFIED"
    expected_root = {
        "registry_id": "pd03b-canonical-pilots", "registry_version": "1.0.0",
        "contract_version": "1.0.0", "bundle_id": "pilotset:36c1085ffbe9",
        "data_classification": "CANONICAL_PD03B_PILOT_SET",
        "baseline_sha": "e72c32bdb041448d34c925c969fe01a2156f9e1d",
        "series_entity_id": "prd:series:e1657d35ac35",
        "variant_rule_set_entity_id": "prd:variant-rule-set:eb255662accc",
        "profile_id": "pprof:4c556c63c1a9",
        "axes": ["grade", "finish", "diameter", "thickness", "length"],
        "fixed_non_axis": ["material"], "cartesian_generation_forbidden": True,
        "readiness": {"import_ready": False, "runtime_ready": False, "golden_ready": False},
        "status": expected_status,
    }
    for key, expected in expected_root.items():
        if value.get(key) != expected:
            add("EXACT_ROOT", f"exact root field differs: {key}")

    available_ids: set[str] = set()
    for path in IDENTITY_REGISTRY_PATHS:
        if path == REGISTRY_PATH:
            continue
        available_ids.update(collect_reference_ids(load_yaml(path)))
    references = {
        value.get("series_entity_id"), value.get("variant_rule_set_entity_id"), value.get("profile_id")
    }
    actual_refs: set[tuple[str, str, str, str, str]] = set()
    pilot_ids: set[str] = set()
    golden_refs: set[str] = set()
    combination_refs: set[str] = set()
    expected_attribute_terms = {
        "material": ("attr:dbf5365ee1e5", "vterm:5ff9c0ceca39"),
        "grade": ("attr:28565665c910", "vterm:a891bfdfdd6b"),
        "finish": ("attr:1926e2ad4629", "vterm:1df9a5493546"),
    }
    expected_measure_attributes = {
        "diameter": ("attr:252ab175be12", "unit:000000000002"),
        "thickness": ("attr:d1890e85f84c", "unit:000000000002"),
        "length": ("attr:d782d47eae7f", "unit:000000000001"),
    }
    pilots = value.get("pilots", [])
    if not isinstance(pilots, list) or len(pilots) != 3:
        add("EXACT_PILOT_COUNT", "exactly three pilot records are required")
    for pilot in pilots if isinstance(pilots, list) else []:
        if not isinstance(pilot, dict):
            continue
        pilot_id = pilot.get("pilot_id")
        if pilot_id in pilot_ids:
            add("DUPLICATE_PILOT_ID", str(pilot_id))
        if isinstance(pilot_id, str):
            pilot_ids.add(pilot_id)
        history = pilot.get("historical_references", {})
        if not isinstance(history, dict):
            history = {}
        golden = history.get("golden_reference")
        combination = history.get("combination_reference")
        if golden in golden_refs or combination in combination_refs:
            add("DUPLICATE_HISTORICAL_REFERENCE", f"{golden}/{combination}")
        if isinstance(golden, str):
            golden_refs.add(golden)
        if isinstance(combination, str):
            combination_refs.add(combination)
        if history.get("references_are_identity") is not False:
            add("HISTORICAL_REFERENCE_IDENTITY", "historical references must never be identity")
        values = pilot.get("attribute_values", {})
        if not isinstance(values, dict):
            values = {}
        for key, (attribute_id, term_id) in expected_attribute_terms.items():
            term = values.get(key, {})
            if term != {"attribute_id": attribute_id, "term_id": term_id}:
                add("EXACT_TERM_VALUE", f"exact {key} value differs")
            references.update((attribute_id, term_id))
        for key, (attribute_id, unit_id) in expected_measure_attributes.items():
            measure = values.get(key, {})
            if not isinstance(measure, dict) or measure.get("attribute_id") != attribute_id or measure.get("unit_id") != unit_id:
                add("EXACT_MEASUREMENT_REFERENCE", f"exact {key} attribute/unit differs")
            references.update((attribute_id, unit_id))
        diameter = str(values.get("diameter", {}).get("decimal_lexeme"))
        thickness = str(values.get("thickness", {}).get("decimal_lexeme"))
        length = str(values.get("length", {}).get("decimal_lexeme"))
        actual_refs.add((str(golden), str(combination), diameter, thickness, length))
        if EXPECTED_RECORD_BY_ID.get(str(pilot_id)) != (
            str(golden), str(combination), diameter, thickness, length,
        ):
            add("PILOT_ID_TUPLE_BINDING", "each stable Pilot ID must remain bound to its exact tuple")
        if pilot.get("availability_status") != "MISSING_DATA_VALUE":
            add("AVAILABILITY_STATUS", "availability must remain MISSING_DATA_VALUE")
        if pilot.get("status") != expected_status:
            add("LIFECYCLE_STATUS", "pilot status differs from lifecycle")
        if pilot.get("owner") != {"role": "product-data-steward"}:
            add("OWNER", "exact Product Data Steward role is required")
        if pilot.get("provenance") != EXPECTED_PROVENANCE:
            add("PROVENANCE", "exact decision provenance is required")
        if pilot.get("record_version") != "1.0.0":
            add("RECORD_VERSION", "record version differs")
    if pilot_ids != EXPECTED_IDS:
        add("EXACT_PILOT_IDS", "exact three fresh stable pilot IDs are required")
    allocations = {str(value.get("bundle_id")), *pilot_ids}
    suffixes = [item.rsplit(":", 1)[-1] for item in allocations]
    cross_namespace_collision = any(
        allocated != existing
        and allocated.rsplit(":", 1)[-1] == existing.rsplit(":", 1)[-1]
        for allocated in allocations
        for existing in available_ids
    )
    if len(suffixes) != len(set(suffixes)) or cross_namespace_collision:
        add("GLOBAL_ID_COLLISION", "Pilot set/record suffix collides internally or with approved prerequisites")
    if actual_refs != EXPECTED_REFERENCES:
        add("EXACT_PILOT_TUPLES", "exact three approved historical reference/measurement tuples are required")
    if not all(isinstance(item, str) and item in available_ids for item in references):
        add("CROSS_FILE_REFERENCE", "every prerequisite entity, Profile, Attribute, Term, and Unit must resolve")
    for node in walk(value):
        if isinstance(node, dict):
            overlap = PROHIBITED_FIELDS.intersection(node)
            if overlap:
                add("PROHIBITED_FIELD", f"prohibited field(s): {sorted(overlap)}")
    return sorted(set(issues))


def validate_file(path: Path = REGISTRY_PATH) -> list[str]:
    validator, _, lifecycle = load_validator()
    return validate_bundle(load_yaml(path), lifecycle, validator)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", nargs="?", default=str(REGISTRY_PATH))
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        issues = validate_file(Path(args.registry))
    except (OSError, TypeError, ValueError, ValidationConfigurationError) as exc:
        print(f"PD03B_CONFIGURATION: {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print("PD-03B canonical pilot validation PASS: exact 3 records; availability=MISSING_DATA_VALUE; readiness=false; no Product/SKU/Golden/runtime authority.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
