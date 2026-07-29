#!/usr/bin/env python3
"""Fail-closed offline validation for PD-02B approval evidence."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import sys
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

from validate_product_attributes import (
    DefinitionError,
    load_json,
    load_yaml,
    reject_nonlocal_schema_references,
    require_mapping,
)


ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = (
    ROOT / "repository/data/contracts/product-data-approval-evidence.contract.yaml"
)
SCHEMA_PATH = (
    ROOT / "repository/data/schemas/product-data-approval-evidence.schema.json"
)
REGISTRY_PATH = (
    ROOT / "repository/data/registries/product-data-approval-evidence.yaml"
)
EXPECTED_HASH_PATHS = {
    "repository/data/registries/product-entities.yaml",
    "repository/data/registries/product-attributes.yaml",
    "repository/data/registries/product-attribute-value-registries.yaml",
    "repository/data/registries/product-attribute-profiles.yaml",
    "repository/data/registries/product-data-localized-labels.yaml",
}
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def lifecycle_status(contract: dict[str, Any]) -> str:
    lifecycle = require_mapping(contract.get("pd02b_lifecycle"), "pd02b_lifecycle")
    history = {
        "DRAFT": [],
        "REVIEW": [
            {
                "from": "DRAFT",
                "to": "REVIEW",
                "evidence_reference": "PD02B-TECH-REVIEW-001",
            }
        ],
        "APPROVED": [
            {
                "from": "DRAFT",
                "to": "REVIEW",
                "evidence_reference": "PD02B-TECH-REVIEW-001",
            },
            {
                "from": "REVIEW",
                "to": "APPROVED",
                "evidence_reference": "FD-PD02B-001",
            },
        ],
    }
    status = lifecycle.get("current_status")
    if (
        lifecycle.get("decision_id") != "FD-PD02B-001"
        or lifecycle.get("allowed_transition_sequence") != ["DRAFT", "REVIEW", "APPROVED"]
        or status not in history
        or lifecycle.get("transition_history") != history[status]
        or lifecycle.get("direct_draft_to_approved_forbidden") is not True
    ):
        raise DefinitionError("PD-02B approval lifecycle is invalid")
    policy = require_mapping(contract.get("evidence_policy"), "evidence_policy")
    if not all(policy.get(key) is True for key in (
        "founder_decision_required",
        "independent_material_review_required",
        "independent_grade_review_required",
        "independent_technical_review_required_before_approval",
        "dataset_hashes_required",
        "anti_replay_required",
        "approved_status_requires_founder_approval",
    )) or policy.get("exact_evidence_count") != 1:
        raise DefinitionError("PD-02B approval-evidence policy differs")
    return str(status)


def load_validator() -> tuple[Draft202012Validator, str]:
    contract, _ = load_yaml(CONTRACT_PATH, "PD-02B approval-evidence contract")
    contract = require_mapping(contract, "PD-02B approval-evidence contract")
    if (
        contract.get("contract_id") != "product-data-approval-evidence"
        or contract.get("contract_version") != "1.0.0"
    ):
        raise DefinitionError("approval-evidence contract identity differs")
    status = lifecycle_status(contract)
    schema = require_mapping(
        load_json(SCHEMA_PATH, "PD-02B approval-evidence schema"),
        "PD-02B approval-evidence schema",
    )
    if (
        schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema"
        or schema.get("type") != "object"
        or schema.get("additionalProperties") is not False
    ):
        raise DefinitionError("approval-evidence schema must be closed Draft 2020-12")
    reject_nonlocal_schema_references(schema)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise DefinitionError(f"approval-evidence schema is invalid: {exc.message}") from exc
    return Draft202012Validator(schema, format_checker=FormatChecker()), status


def validate_registry(
    value: Any,
    source: str,
    validator: Draft202012Validator,
    lifecycle: str,
    *,
    canonical: bool,
    verify_hashes: bool = True,
) -> list[str]:
    issues: list[str] = []

    def add(code: str, subject: str, message: str) -> None:
        issues.append(f"{source}: {subject}: [{code}] {message}")

    expected_keys = {
        "registry_id",
        "registry_version",
        "contract_version",
        "data_classification",
        "evidence",
    }
    if not isinstance(value, dict):
        return [f"{source}: <registry>: [REGISTRY_TYPE] registry must be a mapping"]
    if set(value) != expected_keys:
        add("REGISTRY_STRUCTURE", "<registry>", "registry envelope fields differ")
    if value.get("registry_id") != "product-data-approval-evidence":
        add("REGISTRY_ID", "<registry>", "registry_id differs")
    if not isinstance(value.get("registry_version"), str) or not SEMVER.fullmatch(
        value["registry_version"]
    ):
        add("REGISTRY_VERSION", "<registry>", "registry_version must be semantic")
    expected_classification = "CANONICAL_PD02B" if canonical else "SYNTHETIC_FIXTURE"
    if value.get("data_classification") != expected_classification:
        add("DATA_CLASSIFICATION", "<registry>", f"expected {expected_classification}")
    evidence = value.get("evidence")
    if not isinstance(evidence, list):
        add("EVIDENCE_TYPE", "<registry>", "evidence must be a list")
        return sorted(issues)
    if len(evidence) != 1:
        add("EXACT_EVIDENCE_COUNT", "<registry>", "exactly one evidence record is required")
        return sorted(issues)
    record = evidence[0]
    if not isinstance(record, dict):
        add("EVIDENCE_RECORD_TYPE", "<evidence>", "evidence record must be a mapping")
        return sorted(issues)
    subject = str(record.get("approval_evidence_id", "<evidence>"))
    for error in validator.iter_errors(record):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        add("SCHEMA_VALIDATION", subject, f"{location}: {error.message}")
    if record.get("lifecycle_status") != lifecycle:
        add("LIFECYCLE_MISMATCH", subject, "evidence lifecycle differs from contract")
    expected_status = "APPROVED" if lifecycle == "APPROVED" else "CANDIDATE_UNVERIFIED"
    if record.get("status") != expected_status:
        add("EVIDENCE_STATUS", subject, "evidence status differs from lifecycle")

    founder = record.get("founder_decision")
    if not isinstance(founder, dict) or (
        founder.get("reviewer_id") != "Founder پروژه Damavand Steel"
        or founder.get("verdict") != "PASS"
        or founder.get("evidence_reference")
        != "task:019faec6-5d14-7da2-909a-450fe030b551"
    ):
        add("MISSING_FOUNDER_DECISION", subject, "exact Founder decision evidence is required")
    reviews = record.get("domain_reviews")
    by_id = {
        review.get("reviewer_id"): review
        for review in reviews
        if isinstance(review, dict)
    } if isinstance(reviews, list) else {}
    expected_reviews = {
        "SS-MATERIAL-REVIEWER-02": "Material taxonomy only",
        "SS-INDEPENDENT-REVIEWER-20Y-01": "Grade identifiers 201, 304 and 316 only",
    }
    if set(by_id) != set(expected_reviews):
        add("MISSING_DOMAIN_APPROVAL", subject, "Material and Grade reviews are both required")
    for reviewer_id, scope in expected_reviews.items():
        review = by_id.get(reviewer_id, {})
        if (
            review.get("scope") != scope
            or review.get("verdict") != "PASS"
            or review.get("independent") is not True
            or not review.get("evidence_reference")
        ):
            add("DOMAIN_APPROVAL_INVALID", subject, f"invalid review: {reviewer_id}")

    technical = record.get("technical_review")
    expected_technical = "PENDING" if lifecycle == "DRAFT" else "PASS"
    if not isinstance(technical, dict) or (
        technical.get("reviewer_id") != "repository-guardian-independent"
        or technical.get("verdict") != expected_technical
        or technical.get("independent") is not True
    ):
        add("TECHNICAL_REVIEW_INVALID", subject, "technical review does not match lifecycle")
    if lifecycle != "DRAFT" and (
        not technical.get("evidence_reference") or not technical.get("review_date")
    ):
        add("TECHNICAL_REVIEW_EVIDENCE", subject, "review evidence is required after DRAFT")

    approval = record.get("approval")
    anti_replay = record.get("anti_replay")
    if lifecycle == "APPROVED":
        if not isinstance(approval, dict) or (
            approval.get("approved_by") != "Founder پروژه Damavand Steel"
            or not approval.get("approved_at")
            or approval.get("evidence_reference") != "FD-PD02B-001"
        ):
            add("FOUNDER_APPROVAL_MISSING", subject, "final Founder approval is required")
        if not isinstance(anti_replay, dict) or anti_replay.get("consumed") is not True:
            add("APPROVAL_NOT_CONSUMED", subject, "approval nonce must be consumed once")
    else:
        if not isinstance(approval, dict) or any(approval.get(key) is not None for key in (
            "approved_by",
            "approved_at",
            "evidence_reference",
        )):
            add("PREMATURE_APPROVAL", subject, "approval fields must remain null before APPROVED")
        if not isinstance(anti_replay, dict) or anti_replay.get("consumed") is not False:
            add("APPROVAL_REPLAY", subject, "nonce cannot be consumed before APPROVED")

    hashes = record.get("dataset_hashes")
    hash_map = {
        item.get("path"): item.get("sha256")
        for item in hashes
        if isinstance(item, dict)
    } if isinstance(hashes, list) else {}
    if set(hash_map) != EXPECTED_HASH_PATHS:
        add("DATASET_HASH_PATHS", subject, "exact five canonical dataset hashes are required")
    elif canonical and verify_hashes:
        for relative_path, expected_hash in sorted(hash_map.items()):
            path = ROOT / relative_path
            actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
            if expected_hash != actual_hash:
                add("DATASET_HASH_MISMATCH", subject, f"hash differs: {relative_path}")
    return sorted(issues)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", nargs="?", default=str(REGISTRY_PATH))
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        validator, lifecycle = load_validator()
        value, parser_name = load_yaml(Path(args.registry), "PD-02B approval evidence")
        canonical = Path(args.registry).resolve() == REGISTRY_PATH.resolve()
        issues = validate_registry(
            value, str(args.registry), validator, lifecycle, canonical=canonical
        )
    except (DefinitionError, OSError) as exc:
        print(f"PD02B_APPROVAL_CONFIGURATION: {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print(
        f"PD-02B approval-evidence validation PASS: {len(value['evidence'])} record; "
        f"parser={parser_name}; anti-replay and hashes verified."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
