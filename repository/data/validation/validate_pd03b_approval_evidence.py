#!/usr/bin/env python3
"""Validate PD-03B lifecycle evidence, hashes, technical binding and anti-replay."""

from __future__ import annotations

import argparse
import base64
import hashlib
import os
from pathlib import Path
import subprocess
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
from validate_pd03b_canonical_pilots import (
    IDENTITY_REGISTRY_PATHS,
    collect_reference_ids,
    lifecycle_status,
)


CONTRACT_PATH = ROOT / "repository/data/contracts/pd03b-approval-evidence.contract.yaml"
LIFECYCLE_PATH = ROOT / "repository/data/contracts/pd03b-canonical-pilot.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/pd03b-approval-evidence.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/pd03b/approval-evidence.yaml"
BASELINE_SHA = "e72c32bdb041448d34c925c969fe01a2156f9e1d"
DECISION_ID = "FD-PD03B-001"
REVIEW_ID = "PD03B-TECH-REVIEW-001"
BUNDLE_ID = "pilotset:36c1085ffbe9"
APPROVAL_ID = "papproval:d9d7811dd4f5"
HASH_PATHS = [
    "repository/data/registries/extensions/pd03b/canonical-pilots.yaml",
    "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml",
    "repository/data/registries/product-entities.yaml",
    "repository/data/registries/product-attribute-value-registries.yaml",
    "repository/data/registries/attribute-units.yaml",
]
def expected_nonce() -> str:
    material = "|".join((DECISION_ID, BUNDLE_ID, APPROVAL_ID, BASELINE_SHA))
    return hashlib.sha256(material.encode("utf-8")).hexdigest()[:24]


def technical_artifact(head: str, object_sha256: str, run_id: str, job_id: str) -> str:
    return "|".join((REVIEW_ID, "PASS", head, BASELINE_SHA, object_sha256, run_id, job_id))


def git_commit_oid(raw_commit: bytes) -> str:
    header = f"commit {len(raw_commit)}\0".encode("ascii")
    return hashlib.sha1(header + raw_commit).hexdigest()  # noqa: S324 - Git protocol identity.


def verify_reviewed_commit(technical: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    try:
        encoded = technical.get("reviewed_commit_object_b64")
        if not isinstance(encoded, str):
            raise ValueError("commit object proof is missing")
        raw = base64.b64decode(encoded, validate=True)
    except (TypeError, ValueError) as exc:
        return [f"[TECHNICAL_REVIEW_COMMIT] invalid commit object proof: {exc}"]
    head = str(technical.get("reviewed_head_sha"))
    object_sha = hashlib.sha256(raw).hexdigest()
    if object_sha != technical.get("reviewed_commit_object_sha256"):
        issues.append("[TECHNICAL_REVIEW_COMMIT] commit object SHA-256 differs")
    if git_commit_oid(raw) != head:
        issues.append("[TECHNICAL_REVIEW_COMMIT] commit object does not produce reviewed head SHA")
    is_shallow = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "--is-shallow-repository"],
        check=False, capture_output=True, text=True,
    ).stdout.strip() == "true"
    stored = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "commit", head],
        check=False, capture_output=True,
    )
    if stored.returncode == 0:
        if stored.stdout != raw:
            issues.append("[TECHNICAL_REVIEW_COMMIT] stored Git commit differs from proof")
        for ancestor, descendant, label in (
            (BASELINE_SHA, head, "baseline-to-reviewed-head"),
            (head, "HEAD", "reviewed-head-to-current-HEAD"),
        ):
            result = subprocess.run(
                ["git", "-C", str(ROOT), "merge-base", "--is-ancestor", ancestor, descendant],
                check=False, capture_output=True,
            )
            if result.returncode != 0:
                issues.append(f"[TECHNICAL_REVIEW_COMMIT] Git ancestry failed: {label}")
    elif not (is_shallow and os.environ.get("GITHUB_ACTIONS") == "true"):
        issues.append("[TECHNICAL_REVIEW_COMMIT] reviewed commit is absent from complete repository")
    return issues


def load_contract_and_schema(
    contract_path: Path = CONTRACT_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> tuple[dict[str, Any], Any]:
    contract = require_mapping(load_yaml(contract_path), "PD-03B approval contract")
    expected = {
        "contract_id": "pd03b-approval-evidence", "contract_version": "1.0.0",
        "record_kind": "canonical-pd03b-approval-evidence",
        "schema": {
            "path": "repository/data/schemas/pd03b-approval-evidence.schema.json",
            "draft": "https://json-schema.org/draft/2020-12/schema",
        },
        "registry": {"path": "repository/data/registries/extensions/pd03b/approval-evidence.yaml"},
        "lifecycle_source": "repository/data/contracts/pd03b-canonical-pilot.contract.yaml",
        "evidence_policy": {
            "exact_record_count": 1, "exact_hash_paths": HASH_PATHS,
            "founder_scope_and_data_decision_required": True,
            "settled_pilot_decision_reference": "FD-PILOT-001",
            "prerequisite_decision_reference": "FD-PD03A-001",
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
                "decision_id", "bundle_id", "approval_evidence_id", "baseline_sha",
            ],
            "anti_replay_nonce_derivation": "SHA256_FIRST_24_HEX",
            "exact_single_consumption_history_required": True,
            "global_id_collision_check_required": True,
            "network_allowed": False, "side_effects_allowed": False,
        },
    }
    if contract != expected:
        raise ValidationConfigurationError("PD-03B approval contract differs from exact fail-closed policy")
    schema = require_mapping(load_json(schema_path), "PD-03B approval schema")
    return contract, validate_schema(schema)


def validate_registry(
    value: Any,
    lifecycle: str,
    validator: Any,
    *,
    verify_hashes: bool = True,
) -> list[str]:
    issues: list[str] = []

    def add(code: str, message: str) -> None:
        issues.append(f"[{code}] {message}")

    for error in validator.iter_errors(value):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        add("SCHEMA_VALIDATION", f"{location}: {error.message}")
    if not isinstance(value, dict):
        return sorted(set(issues))
    if {key: value.get(key) for key in ("registry_id", "registry_version", "contract_version", "data_classification")} != {
        "registry_id": "pd03b-approval-evidence", "registry_version": "1.0.0",
        "contract_version": "1.0.0", "data_classification": "CANONICAL_PD03B_EVIDENCE",
    }:
        add("EVIDENCE_ROOT", "approval registry identity differs")
    evidence = value.get("evidence", [])
    if not isinstance(evidence, list) or len(evidence) != 1 or not isinstance(evidence[0], dict):
        return sorted(set(issues + ["[EXACT_EVIDENCE_COUNT] exactly one evidence record is required"]))
    record = evidence[0]
    expected_status = "APPROVED" if lifecycle == "APPROVED" else "CANDIDATE_UNVERIFIED"
    expected_identity = {
        "contract_version": "1.0.0", "approval_evidence_id": APPROVAL_ID,
        "decision_id": DECISION_ID, "bundle_id": BUNDLE_ID,
        "lifecycle_status": lifecycle,
        "scope_reference": "docs/PD03B_CANONICAL_PILOT_SCOPE_V1.0.md",
        "status": expected_status, "record_version": "1.0.0",
    }
    for key, expected in expected_identity.items():
        if record.get(key) != expected:
            add("EVIDENCE_IDENTITY", f"exact evidence field differs: {key}")
    existing_ids: set[str] = set()
    for path in IDENTITY_REGISTRY_PATHS:
        if path == REGISTRY_PATH:
            continue
        existing_ids.update(collect_reference_ids(load_yaml(path)))
    approval_suffix = str(record.get("approval_evidence_id")).rsplit(":", 1)[-1]
    if approval_suffix in {item.rsplit(":", 1)[-1] for item in existing_ids}:
        add("GLOBAL_ID_COLLISION", "approval evidence suffix collides with an approved or Pilot identity")
    if record.get("founder_decision") != {
        "reviewer_id": "Founder پروژه Damavand Steel",
        "scope": "Exact PD-03B Canonical Pilot Records", "verdict": "PASS",
        "evidence_reference": "task:019fa05e-1889-79b3-8e83-9477cd1648c6",
        "review_date": "2026-08-01",
    }:
        add("FOUNDER_DECISION", "exact Founder scope/data decision is required")
    if record.get("domain_basis") != {
        "basis": "FOUNDER_APPROVED_EXACT_NO_CLAIM_TUPLES",
        "source_references": ["FD-PILOT-001", "FD-PD03A-001"],
        "new_domain_claims_authorized": False,
        "availability_authorized": False,
        "commercial_identity_authorized": False,
    }:
        add("DOMAIN_BASIS", "exact no-new-claim domain basis differs")
    hashes = record.get("dataset_hashes", [])
    if not isinstance(hashes, list) or [item.get("path") for item in hashes if isinstance(item, dict)] != HASH_PATHS:
        add("DATASET_HASH_PATHS", "exact ordered dataset hash paths are required")
    if verify_hashes and isinstance(hashes, list):
        for item in hashes:
            if not isinstance(item, dict) or item.get("path") not in HASH_PATHS:
                continue
            actual = hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest()
            if item.get("sha256") != actual:
                add("DATASET_HASH", f"hash differs: {item['path']}")

    technical = record.get("technical_review", {})
    common = {
        "review_id": REVIEW_ID, "reviewer_id": "repository-guardian-independent",
        "scope": "PD-03B contracts, schemas, registries, validators, tests, lifecycle, exact records and allowlist",
        "independent": True, "reviewed_base_sha": BASELINE_SHA,
    }
    for key, expected in common.items():
        if technical.get(key) != expected:
            add("TECHNICAL_REVIEW", f"technical review field differs: {key}")
    if lifecycle == "DRAFT":
        expected_pending = {
            "verdict": "PENDING", "evidence_reference": None, "review_date": None,
            "reviewed_head_sha": None, "reviewed_commit_object_b64": None,
            "reviewed_commit_object_sha256": None, "ci_run_id": None, "ci_job_id": None,
            "verdict_artifact": None, "verdict_artifact_sha256": None,
        }
        for key, expected in expected_pending.items():
            if technical.get(key) != expected:
                add("TECHNICAL_REVIEW_PENDING", f"DRAFT technical field differs: {key}")
    else:
        required = ("reviewed_head_sha", "reviewed_commit_object_sha256", "ci_run_id", "ci_job_id")
        if technical.get("verdict") != "PASS" or technical.get("evidence_reference") != REVIEW_ID:
            add("TECHNICAL_REVIEW_PASS", "REVIEW/APPROVED requires exact independent PASS")
        if not all(isinstance(technical.get(key), str) and technical.get(key) for key in required):
            add("TECHNICAL_REVIEW_BINDING", "technical PASS binding is incomplete")
        else:
            artifact = technical_artifact(
                technical["reviewed_head_sha"], technical["reviewed_commit_object_sha256"],
                technical["ci_run_id"], technical["ci_job_id"],
            )
            digest = hashlib.sha256(artifact.encode("utf-8")).hexdigest()
            if technical.get("verdict_artifact") != artifact or technical.get("verdict_artifact_sha256") != digest:
                add("TECHNICAL_REVIEW_ARTIFACT", "technical verdict artifact or digest differs")
            issues.extend(verify_reviewed_commit(technical))

    approval = record.get("approval")
    if lifecycle == "APPROVED":
        if not isinstance(approval, dict) or approval.get("approved_by") != "Founder پروژه Damavand Steel" or approval.get("evidence_reference") != DECISION_ID or not isinstance(approval.get("approved_at"), str):
            add("FOUNDER_APPROVAL", "APPROVED requires exact Founder lifecycle approval")
    elif approval != {"approved_by": None, "approved_at": None, "evidence_reference": None}:
        add("PREMATURE_APPROVAL", "Founder lifecycle approval is forbidden before APPROVED")

    anti = record.get("anti_replay", {})
    expected_binding = {
        "decision_id": DECISION_ID, "bundle_id": BUNDLE_ID,
        "approval_evidence_id": APPROVAL_ID, "baseline_sha": BASELINE_SHA,
    }
    if anti.get("nonce_derivation") != "SHA256_FIRST_24_HEX" or anti.get("binding") != expected_binding or anti.get("nonce") != expected_nonce():
        add("ANTI_REPLAY_BINDING", "anti-replay derivation, binding, or nonce differs")
    history = anti.get("consumption_history")
    if lifecycle == "APPROVED":
        if anti.get("consumed") is not True or not isinstance(history, list) or len(history) != 1:
            add("APPROVAL_NOT_CONSUMED", "APPROVED requires one nonce consumption")
        elif history[0].get("decision_id") != DECISION_ID or history[0].get("approval_evidence_id") != APPROVAL_ID or history[0].get("evidence_reference") != DECISION_ID:
            add("APPROVAL_REPLAY", "nonce consumption event differs")
    elif anti.get("consumed") is not False or history != []:
        add("APPROVAL_REPLAY", "nonce cannot be consumed before APPROVED")
    return sorted(set(issues))


def validate_file(path: Path = REGISTRY_PATH, *, verify_hashes: bool = True) -> list[str]:
    _, validator = load_contract_and_schema()
    lifecycle_contract = require_mapping(load_yaml(LIFECYCLE_PATH), "PD-03B lifecycle contract")
    lifecycle = lifecycle_status(lifecycle_contract)
    return validate_registry(load_yaml(path), lifecycle, validator, verify_hashes=verify_hashes)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", nargs="?", default=str(REGISTRY_PATH))
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        issues = validate_file(Path(args.registry))
    except (OSError, TypeError, ValueError, ValidationConfigurationError) as exc:
        print(f"PD03B_APPROVAL_CONFIGURATION: {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print("PD-03B approval evidence PASS: lifecycle, hashes, technical binding and anti-replay are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
