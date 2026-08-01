#!/usr/bin/env python3
"""Validate PD-03A approval evidence, hashes, lifecycle, and anti-replay."""

from __future__ import annotations

import base64
import hashlib
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

from validate_pd03a_pilot_prerequisite import (
    BASE_PATHS,
    HEX_SUFFIX,
    ROOT,
    REGISTRY_PATH as FOUNDATION_REGISTRY_PATH,
    ValidationConfigurationError,
    collect_extension_allocations,
    collect_ids,
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
BASELINE_SHA = "dd4d4e9dde59ce652edb5b99d2df3e84b56b8031"
APPROVAL_ID = "papproval:50ba27766106"
EXTENSION_ID = "pdext:ad46d9948af1"
DECISION_ID = "FD-PD03A-001"
REVIEW_ID = "PD03A-TECH-REVIEW-001"
NONCE_BINDING = {
    "decision_id": DECISION_ID,
    "extension_id": EXTENSION_ID,
    "approval_evidence_id": APPROVAL_ID,
    "baseline_sha": BASELINE_SHA,
}
EXPECTED_APPROVAL_CONTRACT = {
    "contract_id": "pd03a-approval-evidence",
    "contract_version": "1.0.0",
    "record_kind": "canonical-pd03a-approval-evidence",
    "schema": {
        "path": "repository/data/schemas/pd03a-approval-evidence.schema.json",
        "draft": "https://json-schema.org/draft/2020-12/schema",
    },
    "registry": {"path": "repository/data/registries/extensions/pd03a/approval-evidence.yaml"},
    "lifecycle_source": "repository/data/contracts/pd03a-pilot-prerequisite.contract.yaml",
    "evidence_policy": {
        "exact_record_count": 1,
        "exact_hash_paths": [
            "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml",
            "repository/data/contracts/measurement.contract.yaml",
            "repository/data/registries/measurement-dimensions.yaml",
            "repository/data/registries/attribute-units.yaml",
        ],
        "failed_review_attempts_preserved": True,
        "failed_review_attempts_never_satisfy_pass": True,
        "independent_technical_pass_required_after_draft": True,
        "technical_review_id": REVIEW_ID,
        "exact_reviewed_head_and_base_sha_required": True,
        "reviewed_commit_object_proof_required": True,
        "reviewed_commit_git_existence_required_when_repository_complete": True,
        "exact_ci_run_and_job_binding_required": True,
        "verdict_artifact_digest_required": True,
        "founder_approval_required_for_approved": True,
        "anti_replay_required": True,
        "anti_replay_binding_fields": [
            "decision_id", "extension_id", "approval_evidence_id", "baseline_sha",
        ],
        "anti_replay_nonce_derivation": "SHA256_FIRST_24_HEX",
        "exact_single_consumption_history_required": True,
        "global_id_collision_check_required": True,
        "network_allowed": False,
        "side_effects_allowed": False,
    },
}


def validate_contract(contract: dict[str, Any]) -> None:
    if contract != EXPECTED_APPROVAL_CONTRACT:
        raise ValidationConfigurationError("PD-03A approval contract differs from exact fail-closed policy")


def technical_artifact(
    reviewed_head_sha: str,
    commit_object_sha256: str,
    ci_run_id: str,
    ci_job_id: str,
) -> str:
    return "|".join((
        REVIEW_ID, "PASS", reviewed_head_sha, BASELINE_SHA,
        commit_object_sha256, ci_run_id, ci_job_id,
    ))


def expected_nonce() -> str:
    material = "|".join((DECISION_ID, EXTENSION_ID, APPROVAL_ID, BASELINE_SHA))
    return hashlib.sha256(material.encode("utf-8")).hexdigest()[:24]


def git_commit_oid(raw_commit: bytes) -> str:
    header = f"commit {len(raw_commit)}\0".encode("ascii")
    return hashlib.sha1(header + raw_commit).hexdigest()  # noqa: S324 - Git object identity is SHA-1 by protocol.


def verify_reviewed_commit(
    reviewed_head: Any,
    object_b64: Any,
    object_sha256: Any,
) -> list[str]:
    issues: list[str] = []
    try:
        if not isinstance(object_b64, str):
            raise ValueError("commit object proof is missing")
        raw_commit = base64.b64decode(object_b64, validate=True)
    except (ValueError, TypeError) as exc:
        return [f"[TECHNICAL_REVIEW_COMMIT] invalid commit object proof: {exc}"]
    actual_sha256 = hashlib.sha256(raw_commit).hexdigest()
    if actual_sha256 != object_sha256:
        issues.append("[TECHNICAL_REVIEW_COMMIT] commit object SHA-256 differs")
    if git_commit_oid(raw_commit) != reviewed_head:
        issues.append("[TECHNICAL_REVIEW_COMMIT] commit object does not produce reviewed head SHA")

    shallow_result = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "--is-shallow-repository"],
        check=False, capture_output=True, text=True,
    )
    is_shallow = shallow_result.returncode == 0 and shallow_result.stdout.strip() == "true"
    object_result = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "commit", str(reviewed_head)],
        check=False, capture_output=True,
    )
    if object_result.returncode == 0:
        if object_result.stdout != raw_commit:
            issues.append("[TECHNICAL_REVIEW_COMMIT] stored Git commit differs from embedded object proof")
        if not is_shallow:
            for ancestor, descendant, label in (
                (BASELINE_SHA, str(reviewed_head), "baseline-to-reviewed-head"),
                (str(reviewed_head), "HEAD", "reviewed-head-to-current-HEAD"),
            ):
                result = subprocess.run(
                    ["git", "-C", str(ROOT), "merge-base", "--is-ancestor", ancestor, descendant],
                    check=False, capture_output=True,
                )
                if result.returncode != 0:
                    issues.append(f"[TECHNICAL_REVIEW_COMMIT] Git ancestry check failed: {label}")
    elif not (is_shallow and os.environ.get("GITHUB_ACTIONS") == "true"):
        issues.append("[TECHNICAL_REVIEW_COMMIT] reviewed head does not exist in the complete local Git repository")
    return issues


def validate_registry(
    value: Any,
    lifecycle: str,
    *,
    verify_hashes: bool = True,
    lifecycle_contract: dict[str, Any] | None = None,
) -> list[str]:
    issues: list[str] = []

    def add(code: str, message: str) -> None:
        issues.append(f"[{code}] {message}")

    if not isinstance(value, dict):
        return ["[REGISTRY_TYPE] approval evidence must be a mapping"]
    evidence = value.get("evidence", [])
    if not isinstance(evidence, list) or len(evidence) != 1 or not isinstance(evidence[0], dict):
        return ["[EXACT_EVIDENCE_COUNT] exactly one evidence record is required"]
    record = evidence[0]
    if lifecycle_contract is None:
        lifecycle_contract = require_mapping(load_yaml(LIFECYCLE_PATH), "PD-03A lifecycle contract")
    lifecycle_fields = require_mapping(lifecycle_contract.get("lifecycle"), "PD-03A lifecycle")
    expected_record_root = {
        "contract_version": "1.0.0", "approval_evidence_id": APPROVAL_ID,
        "decision_id": DECISION_ID,
        "scope_reference": "docs/PD03A_PILOT_PREREQUISITE_FOUNDATION_SCOPE_V1.0.md",
        "record_version": "1.0.0",
    }
    for key, expected in expected_record_root.items():
        if record.get(key) != expected:
            add("EVIDENCE_IDENTITY", f"exact evidence field differs: {key}")
    if record.get("lifecycle_status") != lifecycle:
        add("LIFECYCLE_MISMATCH", "evidence lifecycle differs")
    expected_status = "APPROVED" if lifecycle == "APPROVED" else "CANDIDATE_UNVERIFIED"
    if record.get("status") != expected_status:
        add("EVIDENCE_STATUS", "record status differs from lifecycle")
    founder = record.get("founder_decision", {})
    if founder != {
        "reviewer_id": "Founder پروژه Damavand Steel",
        "scope": "Exact PD-03A Pilot Prerequisite Foundation",
        "verdict": "PASS",
        "evidence_reference": "task:019fa05e-1889-79b3-8e83-9477cd1648c6",
        "independent": False,
        "review_date": "2026-08-01",
    }:
        add("FOUNDER_DECISION", "exact Founder decision evidence is required")
    failed = record.get("failed_review_attempts", [])
    expected_failed = [
        {
            "reviewer_id": "reviewer-id-placeholder", "scope": "PD-03A0 sections A through E",
            "verdict": "BLOCKED_REVIEWER_INCOMPLETE",
            "evidence_reference": "task:019fbc59-74b3-7643-907b-dae234ab871f",
            "independent": True, "review_date": "2026-08-01",
        },
        {
            "reviewer_id": "same-scope-participant", "scope": "PD-03A0 sections B and C",
            "verdict": "BLOCKED_REVIEWER_INELIGIBLE",
            "evidence_reference": "task:019fbc74-4be4-7983-9fbd-5f098cd2a06f",
            "independent": False, "review_date": "2026-08-01",
        },
    ]
    if failed != expected_failed:
        add("FAILED_REVIEW_HISTORY", "exact two failed review attempts must be preserved")
    if isinstance(failed, list) and any(item.get("verdict") == "PASS" for item in failed if isinstance(item, dict)):
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
    common_technical = {
        "review_id": REVIEW_ID,
        "reviewer_id": "repository-guardian-independent",
        "scope": "PD-03A contracts, schemas, validators, tests, extension integrity, lifecycle and exact allowlist",
        "independent": True,
        "reviewed_base_sha": BASELINE_SHA,
    }
    if lifecycle == "DRAFT":
        expected_technical = {
            **common_technical, "verdict": "PENDING", "evidence_reference": None,
            "review_date": None, "reviewed_head_sha": None,
            "reviewed_commit_object_b64": None, "reviewed_commit_object_sha256": None,
            "ci_run_id": None, "ci_job_id": None,
            "verdict_artifact": None, "verdict_artifact_sha256": None,
        }
        if technical != expected_technical:
            add("TECHNICAL_REVIEW", "DRAFT technical review must remain exact PENDING evidence")
    else:
        reviewed_head = technical.get("reviewed_head_sha")
        commit_object_sha256 = str(technical.get("reviewed_commit_object_sha256"))
        ci_run_id = str(technical.get("ci_run_id"))
        ci_job_id = str(technical.get("ci_job_id"))
        artifact = technical_artifact(
            str(reviewed_head), commit_object_sha256, ci_run_id, ci_job_id,
        )
        artifact_digest = hashlib.sha256(artifact.encode("utf-8")).hexdigest()
        expected_technical = {
            **common_technical, "verdict": "PASS", "evidence_reference": REVIEW_ID,
            "review_date": "2026-08-01", "reviewed_head_sha": reviewed_head,
            "reviewed_commit_object_b64": technical.get("reviewed_commit_object_b64"),
            "reviewed_commit_object_sha256": commit_object_sha256,
            "ci_run_id": ci_run_id, "ci_job_id": ci_job_id,
            "verdict_artifact": artifact, "verdict_artifact_sha256": artifact_digest,
        }
        if technical != expected_technical:
            add("TECHNICAL_REVIEW_BINDING", "PASS must bind exact Review ID, head/base SHA, artifact, and digest")
        if (
            reviewed_head is None
            or reviewed_head == BASELINE_SHA
            or lifecycle_fields.get("technical_reviewed_sha") != reviewed_head
            or lifecycle_fields.get("technical_review_artifact_sha256") != artifact_digest
        ):
            add("TECHNICAL_REVIEW_LIFECYCLE_BINDING", "technical PASS differs from lifecycle-bound reviewed SHA or artifact digest")
        issues.extend(verify_reviewed_commit(
            reviewed_head,
            technical.get("reviewed_commit_object_b64"),
            technical.get("reviewed_commit_object_sha256"),
        ))
    approval = record.get("approval", {})
    anti_replay = record.get("anti_replay", {})
    expected_binding = NONCE_BINDING
    if (
        anti_replay.get("nonce_derivation") != "SHA256_FIRST_24_HEX"
        or anti_replay.get("binding") != expected_binding
        or anti_replay.get("nonce") != expected_nonce()
    ):
        add("ANTI_REPLAY_BINDING", "nonce must be uniquely derived from exact decision, extension, approval ID, and baseline SHA")
    history = anti_replay.get("consumption_history")
    if lifecycle == "APPROVED":
        if (
            approval.get("approved_by") != "Founder پروژه Damavand Steel"
            or approval.get("evidence_reference") != "FD-PD03A-001"
            or not approval.get("approved_at")
        ):
            add("FINAL_APPROVAL", "final Founder approval is required")
        if anti_replay.get("consumed") is not True:
            add("APPROVAL_NOT_CONSUMED", "approval nonce must be consumed once")
        expected_history = [{
            "decision_id": DECISION_ID,
            "approval_evidence_id": APPROVAL_ID,
            "evidence_reference": DECISION_ID,
            "consumed_at": approval.get("approved_at"),
        }]
        if history != expected_history:
            add("CONSUMPTION_HISTORY", "APPROVED requires one exact consumption event bound to Founder approval")
    else:
        if any(approval.get(key) is not None for key in ("approved_by", "approved_at", "evidence_reference")):
            add("PREMATURE_APPROVAL", "approval fields must remain null before APPROVED")
        if anti_replay.get("consumed") is not False:
            add("APPROVAL_REPLAY", "nonce cannot be consumed before APPROVED")
        if history != []:
            add("CONSUMPTION_HISTORY", "consumption history must remain empty before APPROVED")

    approval_id = record.get("approval_evidence_id")
    extension_bundle = require_mapping(load_yaml(FOUNDATION_REGISTRY_PATH), "PD-03A extension")
    allocated = collect_extension_allocations(extension_bundle)
    for path in BASE_PATHS:
        allocated.update(collect_ids(load_yaml(path)))
    approval_suffix = HEX_SUFFIX.search(str(approval_id))
    allocated_suffixes = {
        match.group(1)
        for item in allocated
        if (match := HEX_SUFFIX.search(item)) is not None
    }
    if approval_suffix is None or approval_suffix.group(1) in allocated_suffixes:
        add("APPROVAL_ID_COLLISION", "approval evidence ID suffix collides with base or extension allocation")
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
        validate_contract(contract)
        lifecycle_contract = require_mapping(load_yaml(LIFECYCLE_PATH), "PD-03A lifecycle contract")
        lifecycle = lifecycle_status(lifecycle_contract)
        schema = require_mapping(load_json(SCHEMA_PATH), "PD-03A approval schema")
        validator = validate_schema(schema)
        value = load_yaml(REGISTRY_PATH)
        issues = [
            f"[SCHEMA_VALIDATION] {'/'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
            for error in validator.iter_errors(value)
        ]
        issues.extend(validate_registry(value, lifecycle, lifecycle_contract=lifecycle_contract))
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
