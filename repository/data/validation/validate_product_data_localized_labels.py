#!/usr/bin/env python3
"""Fail-closed offline validation for PD-02B localized labels."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
import unicodedata
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
    ROOT / "repository/data/contracts/product-data-localized-labels.contract.yaml"
)
SCHEMA_PATH = (
    ROOT / "repository/data/schemas/product-data-localized-labels.schema.json"
)
REGISTRY_PATH = (
    ROOT / "repository/data/registries/product-data-localized-labels.yaml"
)
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
FORBIDDEN_BIDI = {
    "\u202a",
    "\u202b",
    "\u202c",
    "\u202d",
    "\u202e",
    "\u2066",
    "\u2067",
    "\u2068",
    "\u2069",
}


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
        or lifecycle.get("canonical_population_authority") is not True
    ):
        raise DefinitionError("PD-02B localized-label lifecycle is invalid")
    policy = require_mapping(contract.get("label_policy"), "label_policy")
    if policy != {
        "exact_label_count": 18,
        "locales": ["fa-IR", "en"],
        "exact_subject_count": 9,
        "one_label_per_subject_per_locale": True,
        "unicode_form": "NFC",
        "approval_evidence_required_for_approved_status": True,
        "aliases_are_not_additional_labels": True,
    }:
        raise DefinitionError("PD-02B localized-label policy differs")
    return str(status)


def load_validator() -> tuple[Draft202012Validator, str]:
    contract, _ = load_yaml(CONTRACT_PATH, "PD-02B localized-label contract")
    contract = require_mapping(contract, "PD-02B localized-label contract")
    if (
        contract.get("contract_id") != "product-data-localized-labels"
        or contract.get("contract_version") != "1.0.0"
    ):
        raise DefinitionError("localized-label contract identity differs")
    status = lifecycle_status(contract)
    schema = require_mapping(
        load_json(SCHEMA_PATH, "PD-02B localized-label schema"),
        "PD-02B localized-label schema",
    )
    if (
        schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema"
        or schema.get("type") != "object"
        or schema.get("additionalProperties") is not False
    ):
        raise DefinitionError("localized-label schema must be closed Draft 2020-12")
    reject_nonlocal_schema_references(schema)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise DefinitionError(f"localized-label schema is invalid: {exc.message}") from exc
    return Draft202012Validator(schema, format_checker=FormatChecker()), status


def normalized(value: str) -> str:
    return unicodedata.normalize("NFC", value.strip()).casefold()


def validate_registry(
    value: Any,
    source: str,
    validator: Draft202012Validator,
    lifecycle: str,
    *,
    canonical: bool,
) -> list[str]:
    issues: list[str] = []

    def add(code: str, subject: str, message: str) -> None:
        issues.append(f"{source}: {subject}: [{code}] {message}")

    expected_keys = {
        "registry_id",
        "registry_version",
        "contract_version",
        "data_classification",
        "labels",
    }
    if not isinstance(value, dict):
        return [f"{source}: <registry>: [REGISTRY_TYPE] registry must be a mapping"]
    if set(value) != expected_keys:
        add("REGISTRY_STRUCTURE", "<registry>", "registry envelope fields differ")
    if value.get("registry_id") != "product-data-localized-labels":
        add("REGISTRY_ID", "<registry>", "registry_id differs")
    if not isinstance(value.get("registry_version"), str) or not SEMVER.fullmatch(
        value["registry_version"]
    ):
        add("REGISTRY_VERSION", "<registry>", "registry_version must be semantic")
    expected_classification = "CANONICAL_PD02B" if canonical else "SYNTHETIC_FIXTURE"
    if value.get("data_classification") != expected_classification:
        add("DATA_CLASSIFICATION", "<registry>", f"expected {expected_classification}")
    labels = value.get("labels")
    if not isinstance(labels, list):
        add("LABELS_TYPE", "<registry>", "labels must be a list")
        return sorted(issues)
    if canonical and len(labels) != 18:
        add("EXACT_LABEL_COUNT", "<registry>", "canonical slice requires exactly 18 labels")

    ids: set[str] = set()
    pairs: set[tuple[str, str]] = set()
    normalized_labels: set[tuple[str, str]] = set()
    subjects: set[str] = set()
    expected_status = "APPROVED" if lifecycle == "APPROVED" else "CANDIDATE_UNVERIFIED"
    for index, record in enumerate(labels):
        subject = (
            record.get("label_id")
            if isinstance(record, dict) and isinstance(record.get("label_id"), str)
            else f"<label:{index}>"
        )
        if not isinstance(record, dict):
            add("LABEL_TYPE", str(subject), "label record must be a mapping")
            continue
        for error in validator.iter_errors(record):
            location = "/".join(str(part) for part in error.absolute_path) or "<root>"
            add("SCHEMA_VALIDATION", str(subject), f"{location}: {error.message}")
        label_id = record.get("label_id")
        if label_id in ids:
            add("DUPLICATE_LABEL_ID", str(subject), "label_id is duplicated")
        elif isinstance(label_id, str):
            ids.add(label_id)
        subject_id = record.get("subject_id")
        locale = record.get("locale")
        pair = (str(subject_id), str(locale))
        if pair in pairs:
            add("DUPLICATE_SUBJECT_LOCALE", str(subject), "subject/locale pair is duplicated")
        else:
            pairs.add(pair)
        if isinstance(subject_id, str):
            subjects.add(subject_id)
        label = record.get("label")
        if isinstance(label, str):
            if unicodedata.normalize("NFC", label) != label:
                add("UNICODE_NOT_NFC", str(subject), "label must be NFC normalized")
            if any(character in FORBIDDEN_BIDI for character in label):
                add("UNICODE_BIDI_CONTROL", str(subject), "bidi override/isolate controls are forbidden")
            if locale == "en" and not label.isascii():
                add("UNICODE_CONFUSABLE_LABEL", str(subject), "English labels must be ASCII")
            normalized_key = (str(locale), normalized(label))
            if normalized_key in normalized_labels:
                add("DUPLICATE_NORMALIZED_LABEL", str(subject), "normalized locale label collides")
            normalized_labels.add(normalized_key)
        if record.get("status") != (
            expected_status if canonical else "CANDIDATE_UNVERIFIED"
        ):
            add("LIFECYCLE_STATUS", str(subject), "record status does not match lifecycle")
    if canonical and len(subjects) != 9:
        add("EXACT_SUBJECT_COUNT", "<registry>", "canonical slice requires exactly 9 subjects")
    if canonical and any(
        {locale for subject_id, locale in pairs if subject_id == subject} != {"fa-IR", "en"}
        for subject in subjects
    ):
        add("LOCALE_PAIR_MISSING", "<registry>", "every subject requires fa-IR and en")
    return sorted(issues)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", nargs="?", default=str(REGISTRY_PATH))
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        validator, lifecycle = load_validator()
        value, parser_name = load_yaml(Path(args.registry), "PD-02B localized labels")
        canonical = Path(args.registry).resolve() == REGISTRY_PATH.resolve()
        issues = validate_registry(
            value, str(args.registry), validator, lifecycle, canonical=canonical
        )
    except (DefinitionError, OSError) as exc:
        print(f"PD02B_LABEL_CONFIGURATION: {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print(
        f"PD-02B localized-label validation PASS: {len(value['labels'])} label(s); "
        f"parser={parser_name}; network, side effects=false."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
