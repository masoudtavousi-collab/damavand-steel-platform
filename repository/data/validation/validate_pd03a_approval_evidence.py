#!/usr/bin/env python3
"""Validate PD-03A approval evidence, hashes, lifecycle, and anti-replay."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
from typing import Any

from validate_pd03a_pilot_prerequisite import (
    ROOT,
    ValidationConfigurationError,
    lifecycle_status,
    load_json,
    load_yaml,
    require_mapping,
    validate_schema,
)


CONTRACT_PATH = ROOT / "repository/data/contracts/pd03a-approval-evidence.contract.yaml"
LIFECYCLE_PATH = ROOT / "repository/data/contracts/pd03a-pilot-prerequisite.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/pd03a-approval-evidence.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/pd03a/approval-evidence.yaml"
EXPECTED_HASH_PATHS = {
    "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml",
    "repository/data/contracts/measurement.contract.yaml",
    "repository/data/registries/measurement-dimensions.yaml",
    "repository/data/registries/attribute-units.yaml",
}


def validate_registry(value: Any, lifecycle: str, *, verify_hashes: bool = True) -> list[str]:
    issues: list[str] = []

    def add(code: str, message: str) -> None:
        issues.append(f"[{code}] {message}")

    if not isinstance(value, dict):
        return ["[REGISTRY_TYPE] approval evidence must be a mapping"]
    evidence = value.get("evidence", [])
    if not isinstance(evidence, list) or len(evidence) != 1 or not isinstance(evidence[0], dict):
        return ["[EXACT_EVIDENCE_COUNT] exactly one evidence record is required"]
    record = evidence[0]
    if record.get("lifecycle_status") != lifecycle:
        add("LIFECYCLE_MISMATCH", "evidence lifecycle differs")
    expected_status = "APPROVED" if lifecycle == "APPROVED" else "CANDIDATE_UNVERIFIED"
    if record.get("status") != expected_status:
        add("EVIDENCE_STATUS", "record status differs from lifecycle")
    founder = record.get("founder_decision", {})
    if (
        founder.get("reviewer_id") != "Founder پروژه Damavand Steel"
        or founder.get("verdict") != "PASS"
        or founder.get("evidence_reference") != "task:019fa05e-1889-79b3-8e83-9477cd1648c6"
    ):
        add("FOUNDER_DECISION", "exact Founder decision evidence is required")
    failed = record.get("failed_review_attempts", [])
    if not isinstance(failed, list) or len(failed) < 2:
        add("FAILED_REVIEW_HISTORY", "at least two failed review attempts must be preserved")
    elif any(item.get("verdict") == "PASS" for item in failed if isinstance(item, dict)):
        add("FAILED_REVIEW_AS_PASS", "failed review history cannot satisfy PASS")
    domain = record.get("domain_basis", {})
    if domain != {
        "basis": "FOUNDER_APPROVED_NO_CLAIM_PILOT_REFERENCES",
        "human_pass_claimed": False,
        "technical_claims_authorized": False,
        "commercial_claims_authorized": False,
        "source_reference": "FD-PD03A-001",
    }:
        add("DOMAIN_BASIS", "no-claim Founder basis differs")
    technical = record.get("technical_review", {})
    expected_technical = "PENDING" if lifecycle == "DRAFT" else "PASS"
    if (
        technical.get("reviewer_id") != "repository-guardian-independent"
        or technical.get("verdict") != expected_technical
        or technical.get("independent") is not True
    ):
        add("TECHNICAL_REVIEW", "independent technical review differs from lifecycle")
    if lifecycle != "DRAFT" and (not technical.get("evidence_reference") or not technical.get("review_date")):
        add("TECHNICAL_REVIEW_EVIDENCE", "PASS requires evidence reference and date")
    approval = record.get("approval", {})
    anti_replay = record.get("anti_replay", {})
    if lifecycle == "APPROVED":
        if (
            approval.get("approved_by") != "Founder پروژه Damavand Steel"
            or approval.get("evidence_reference") != "FD-PD03A-001"
            or not approval.get("approved_at")
        ):
            add("FINAL_APPROVAL", "final Founder approval is required")
        if anti_replay.get("consumed") is not True:
            add("APPROVAL_NOT_CONSUMED", "approval nonce must be consumed once")
    else:
        if any(approval.get(key) is not None for key in ("approved_by", "approved_at", "evidence_reference")):
            add("PREMATURE_APPROVAL", "approval fields must remain null before APPROVED")
        if anti_replay.get("consumed") is not False:
            add("APPROVAL_REPLAY", "nonce cannot be consumed before APPROVED")
    hashes = record.get("dataset_hashes", [])
    hash_map = {item.get("path"): item.get("sha256") for item in hashes if isinstance(item, dict)}
    if set(hash_map) != EXPECTED_HASH_PATHS:
        add("DATASET_HASH_PATHS", "exact four dataset hash paths are required")
    elif verify_hashes:
        for relative_path, expected_hash in sorted(hash_map.items()):
            actual_hash = hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()
            if actual_hash != expected_hash:
                add("DATASET_HASH_MISMATCH", f"hash differs: {relative_path}")
    return sorted(set(issues))


def main() -> int:
    try:
        contract = require_mapping(load_yaml(CONTRACT_PATH), "PD-03A approval contract")
        if contract.get("contract_id") != "pd03a-approval-evidence":
            raise ValidationConfigurationError("approval contract identity differs")
        lifecycle_contract = require_mapping(load_yaml(LIFECYCLE_PATH), "PD-03A lifecycle contract")
        lifecycle = lifecycle_status(lifecycle_contract)
        schema = require_mapping(load_json(SCHEMA_PATH), "PD-03A approval schema")
        validator = validate_schema(schema)
        value = load_yaml(REGISTRY_PATH)
        issues = [
            f"[SCHEMA_VALIDATION] {'/'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
            for error in validator.iter_errors(value)
        ]
        issues.extend(validate_registry(value, lifecycle))
    except (ValidationConfigurationError, OSError, TypeError, ValueError) as exc:
        print(f"PD03A_APPROVAL_CONFIGURATION: {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(sorted(set(issues))), file=sys.stderr)
        return 1
    print(f"PD-03A approval-evidence validation PASS: lifecycle={lifecycle}; hashes and anti-replay verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
