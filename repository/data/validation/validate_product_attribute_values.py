#!/usr/bin/env python3
"""Fail-closed offline validation for PD-02A controlled-value registries."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys
import unicodedata
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

from validate_product_attributes import (
    DefinitionError,
    load_definitions as load_attribute_definitions,
    load_json,
    load_yaml,
    parse_json,
    parse_yaml,
    reject_nonlocal_schema_references,
    require_mapping,
    rfc3339_utc,
    validate_fixture as validate_attribute_fixture,
)


ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = (
    ROOT / "repository/data/contracts/product-attribute-value-registry.contract.yaml"
)
SCHEMA_PATH = (
    ROOT / "repository/data/schemas/product-attribute-value-registry.schema.json"
)
REGISTRY_PATH = (
    ROOT / "repository/data/registries/product-attribute-value-registries.yaml"
)

SEMVER_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
ROLE_PATTERN = re.compile(r"^[a-z][a-z0-9-]{2,63}$")
CAPTURED_BY_PATTERN = re.compile(r"^role:[a-z][a-z0-9-]{2,63}$")
MACHINE_CODE_PATTERN = re.compile(r"^[A-Z][A-Z0-9_]*$")
EXPECTED_STATUSES = {
    "APPROVED",
    "CANDIDATE_UNVERIFIED",
    "MISSING_DATA_VALUE",
    "FOUNDER_INPUT_REQUIRED",
    "DEFERRED",
    "NOT_APPLICABLE",
    "INVALID",
}


@dataclass(frozen=True)
class ValidationIssue:
    source: str
    subject: str
    code: str
    message: str

    def render(self) -> str:
        return f"{self.source}: {self.subject}: [{self.code}] {self.message}"


@dataclass(frozen=True)
class Definitions:
    contract_version: str
    registry_id_pattern: re.Pattern[str]
    value_id_pattern: re.Pattern[str]
    attribute_id_pattern: re.Pattern[str]
    key_pattern: re.Pattern[str]
    prohibited_fields: set[str]
    schema_validator: Any
    attribute_definitions: Any


def validate_lifecycle(contract: dict[str, Any]) -> None:
    lifecycle = require_mapping(contract.get("pd02a_lifecycle"), "pd02a_lifecycle")
    if lifecycle.get("decision_id") != "FD-PD02A-001":
        raise DefinitionError("PD-02A lifecycle decision_id must be FD-PD02A-001")
    if lifecycle.get("allowed_transition_sequence") != [
        "DRAFT",
        "REVIEW",
        "APPROVED",
    ]:
        raise DefinitionError("PD-02A lifecycle must be DRAFT -> REVIEW -> APPROVED")
    expected = {
        "DRAFT": [],
        "REVIEW": [
            {
                "from": "DRAFT",
                "to": "REVIEW",
                "evidence_reference": "PD02A-REVIEW-001",
            }
        ],
        "APPROVED": [
            {
                "from": "DRAFT",
                "to": "REVIEW",
                "evidence_reference": "PD02A-REVIEW-001",
            },
            {
                "from": "REVIEW",
                "to": "APPROVED",
                "evidence_reference": "FD-PD02A-001",
            },
        ],
    }
    status = lifecycle.get("current_status")
    if status not in expected or lifecycle.get("transition_history") != expected[status]:
        raise DefinitionError("PD-02A lifecycle history is invalid or skips REVIEW")
    if lifecycle.get("direct_draft_to_approved_forbidden") is not True:
        raise DefinitionError("direct DRAFT -> APPROVED must remain forbidden")
    if lifecycle.get("canonical_population_authority") is not False:
        raise DefinitionError("PD-02A must not grant canonical population authority")


def load_definitions(
    contract_path: Path = CONTRACT_PATH, schema_path: Path = SCHEMA_PATH
) -> Definitions:
    contract, _ = load_yaml(contract_path, "PD-02A value-registry contract")
    contract = require_mapping(contract, "PD-02A value-registry contract")
    if contract.get("contract_id") != "product-attribute-value-registry":
        raise DefinitionError("value-registry contract_id is invalid")
    if contract.get("contract_version") != "1.0.0":
        raise DefinitionError("value-registry contract_version must be 1.0.0")
    validate_lifecycle(contract)
    policy = require_mapping(contract.get("registry_policy"), "registry_policy")
    if policy != {
        "canonical_registry_must_remain_empty_in_pd02a": True,
        "fixtures_must_be_synthetic": True,
        "network_allowed": False,
        "side_effects_allowed": False,
    }:
        raise DefinitionError("value-registry policy differs from PD-02A")
    synthetic_boundary = require_mapping(
        contract.get("synthetic_boundary"), "synthetic_boundary"
    )
    if synthetic_boundary != {
        "allowed_data_classification": "SYNTHETIC_FIXTURE",
        "allowed_status": "CANDIDATE_UNVERIFIED",
        "approval_evidence_allowed": False,
        "embedded_attribute_dependencies_required": True,
        "embedded_attributes_must_pass_product_attribute_validation": True,
        "registry_attribute_must_exist": True,
        "registry_attribute_data_type": "CONTROLLED_TERM",
        "registry_id_must_match_attribute_reference": True,
    }:
        raise DefinitionError("synthetic dependency boundary differs from PD-02A")
    naming = require_mapping(contract.get("stable_identity"), "stable_identity")
    normalization = require_mapping(contract.get("normalization"), "normalization")
    if normalization.get("unicode_form") != "NFC":
        raise DefinitionError("PD-02A normalization must use NFC")
    try:
        registry_id_pattern = re.compile(str(naming["registry_id"]["pattern"]))
        value_id_pattern = re.compile(str(naming["value_id"]["pattern"]))
        attribute_id_pattern = re.compile(str(naming["attribute_id"]["pattern"]))
        key_pattern = re.compile(str(normalization["key_pattern"]))
    except (KeyError, TypeError, re.error) as exc:
        raise DefinitionError("PD-02A identity patterns are invalid") from exc
    prohibited = contract.get("prohibited_fields")
    if not isinstance(prohibited, list) or not prohibited:
        raise DefinitionError("PD-02A prohibited_fields must be non-empty")

    schema = load_json(schema_path, "PD-02A value-registry schema")
    schema = require_mapping(schema, "PD-02A value-registry schema")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise DefinitionError("PD-02A schema must declare Draft 2020-12")
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        raise DefinitionError("PD-02A schema must be a closed object")
    if schema.get("properties", {}).get("contract_version", {}).get("const") != "1.0.0":
        raise DefinitionError("PD-02A schema contract version differs")
    if set(schema.get("properties", {}).get("status", {}).get("enum", [])) != EXPECTED_STATUSES:
        raise DefinitionError("PD-02A registry statuses differ from the approved vocabulary")
    reject_nonlocal_schema_references(schema)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise DefinitionError(f"PD-02A value-registry schema is invalid: {exc.message}") from exc
    return Definitions(
        contract_version="1.0.0",
        registry_id_pattern=registry_id_pattern,
        value_id_pattern=value_id_pattern,
        attribute_id_pattern=attribute_id_pattern,
        key_pattern=key_pattern,
        prohibited_fields={str(item) for item in prohibited},
        schema_validator=Draft202012Validator(schema, format_checker=FormatChecker()),
        attribute_definitions=load_attribute_definitions(),
    )


def normalized(value: str) -> str:
    return unicodedata.normalize("NFC", value.strip()).casefold()


def iter_keys(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            if isinstance(key, str):
                yield key
            yield from iter_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_keys(child)


def valid_role(value: Any) -> bool:
    return (
        isinstance(value, dict)
        and set(value) == {"role"}
        and isinstance(value.get("role"), str)
        and ROLE_PATTERN.fullmatch(value["role"]) is not None
    )


def validate_provenance(
    value: Any, subject: str, add: Any, synthetic: bool
) -> None:
    expected = {
        "source_type",
        "source_reference",
        "captured_by",
        "captured_at",
        "evidence_status",
    }
    if not isinstance(value, dict) or set(value) != expected:
        add(subject, "PROVENANCE_STRUCTURE", "provenance fields differ from the contract")
        return
    if not isinstance(value["source_type"], str) or not MACHINE_CODE_PATTERN.fullmatch(
        value["source_type"]
    ):
        add(subject, "PROVENANCE_SOURCE_TYPE", "source_type must be a machine code")
    if synthetic and value["source_type"] != "SYNTHETIC_FIXTURE":
        add(subject, "FORGED_CLASSIFICATION", "synthetic provenance is required")
    if not isinstance(value["source_reference"], str) or not value["source_reference"].strip():
        add(subject, "PROVENANCE_SOURCE_REFERENCE", "source_reference is required")
    if not isinstance(value["captured_by"], str) or not CAPTURED_BY_PATTERN.fullmatch(
        value["captured_by"]
    ):
        add(subject, "PROVENANCE_CAPTURED_BY", "captured_by must identify a role")
    if not rfc3339_utc(value["captured_at"]):
        add(subject, "PROVENANCE_CAPTURED_AT", "captured_at must be RFC 3339 UTC")
    if (
        not isinstance(value["evidence_status"], str)
        or not MACHINE_CODE_PATTERN.fullmatch(value["evidence_status"])
    ):
        add(subject, "PROVENANCE_EVIDENCE_STATUS", "evidence_status must be a machine code")
    if synthetic and value["evidence_status"] != "SYNTHETIC_TEST_EVIDENCE":
        add(subject, "FORGED_EVIDENCE", "synthetic test evidence is required")


def validate_registry(
    value: Any,
    source: str,
    definitions: Definitions,
    *,
    canonical: bool,
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    def add(subject: str, code: str, message: str) -> None:
        issues.append(ValidationIssue(source, subject, code, message))

    expected_envelope = {
        "registry_id",
        "registry_version",
        "contract_version",
        "data_classification",
        "value_registries",
    }
    if not canonical:
        expected_envelope.add("synthetic_attribute_dependencies")
    if not isinstance(value, dict):
        add("<registry>", "REGISTRY_TYPE", "registry must be a mapping")
        return issues
    if set(value) != expected_envelope:
        add("<registry>", "REGISTRY_STRUCTURE", "registry envelope fields differ")
    if value.get("registry_id") != "product-attribute-value-registries":
        add("<registry>", "REGISTRY_ID", "registry_id is invalid")
    if not isinstance(value.get("registry_version"), str) or not SEMVER_PATTERN.fullmatch(
        value["registry_version"]
    ):
        add("<registry>", "REGISTRY_VERSION", "registry_version must use X.Y.Z")
    if value.get("contract_version") != definitions.contract_version:
        add("<registry>", "CONTRACT_VERSION", "contract_version is incompatible")
    classification = value.get("data_classification")
    expected_classification = "CANONICAL_EMPTY" if canonical else "SYNTHETIC_FIXTURE"
    if classification != expected_classification:
        add("<registry>", "DATA_CLASSIFICATION", f"expected {expected_classification}")
    entries = value.get("value_registries")
    if not isinstance(entries, list):
        add("<registry>", "REGISTRY_ENTRIES", "value_registries must be a list")
        return sorted(issues, key=lambda item: item.render())
    if canonical:
        if entries:
            add("<registry>", "CANONICAL_REGISTRY_NOT_EMPTY", "PD-02A canonical registry must remain empty")
        return sorted(issues, key=lambda item: item.render())
    if not entries:
        add("<registry>", "EMPTY_SYNTHETIC_FIXTURE", "synthetic fixture needs one registry")
    attribute_dependencies = value.get("synthetic_attribute_dependencies")
    attribute_issues = validate_attribute_fixture(
        attribute_dependencies,
        "<synthetic-value-registry-attributes>",
        definitions.attribute_definitions,
    )
    for issue in attribute_issues:
        add(
            issue.attribute,
            f"PRODUCT_ATTRIBUTE_{issue.code}",
            issue.message,
        )
    attributes = {
        item["attribute_id"]: item
        for item in (
            attribute_dependencies
            if isinstance(attribute_dependencies, list)
            else []
        )
        if isinstance(item, dict)
        and isinstance(item.get("attribute_id"), str)
    }

    registry_ids: set[str] = set()
    registry_keys: set[str] = set()
    registry_labels: set[str] = set()
    global_value_ids: set[str] = set()
    for index, raw in enumerate(entries):
        subject = (
            raw.get("value_registry_id")
            if isinstance(raw, dict) and isinstance(raw.get("value_registry_id"), str)
            else f"<registry:{index}>"
        )
        if not isinstance(raw, dict):
            add(str(subject), "ENTRY_TYPE", "value registry entry must be a mapping")
            continue
        for error in sorted(
            definitions.schema_validator.iter_errors(raw),
            key=lambda item: (tuple(str(part) for part in item.absolute_path), item.message),
        ):
            location = "/".join(str(part) for part in error.absolute_path) or "<root>"
            add(str(subject), "SCHEMA_VALIDATION", f"{location}: {error.message}")
        for field in sorted(set(iter_keys(raw)) & definitions.prohibited_fields):
            add(str(subject), "PROHIBITED_FIELD", f"prohibited field: {field}")

        registry_id = raw.get("value_registry_id")
        if not isinstance(registry_id, str) or not definitions.registry_id_pattern.fullmatch(
            registry_id
        ):
            add(str(subject), "VALUE_REGISTRY_ID", "value_registry_id format is invalid")
        elif registry_id in registry_ids:
            add(str(subject), "DUPLICATE_REGISTRY_ID", f"duplicate registry ID: {registry_id}")
        else:
            registry_ids.add(registry_id)
        registry_key = raw.get("registry_key")
        if not isinstance(registry_key, str) or not definitions.key_pattern.fullmatch(
            registry_key
        ):
            add(str(subject), "REGISTRY_KEY", "registry_key must use lower_snake_case")
        elif registry_key in registry_keys:
            add(str(subject), "DUPLICATE_REGISTRY_KEY", f"duplicate registry key: {registry_key}")
        else:
            registry_keys.add(registry_key)
        attribute_id = raw.get("attribute_id")
        if not isinstance(attribute_id, str) or not definitions.attribute_id_pattern.fullmatch(
            attribute_id
        ):
            add(str(subject), "ATTRIBUTE_ID", "attribute_id format is invalid")
        attribute = attributes.get(attribute_id)
        if attribute is None:
            add(str(subject), "UNKNOWN_ATTRIBUTE", f"unknown synthetic attribute: {attribute_id}")
        else:
            if attribute.get("data_type") != "CONTROLLED_TERM":
                add(
                    str(subject),
                    "ATTRIBUTE_TYPE_MISMATCH",
                    "controlled-value registry requires a CONTROLLED_TERM attribute",
                )
            declared_registry = (
                attribute.get("validation", {})
                .get("constraints", {})
                .get("value_registry_reference")
            )
            if declared_registry != registry_id:
                add(
                    str(subject),
                    "ATTRIBUTE_REGISTRY_MISMATCH",
                    "registry ID differs from the Attribute value_registry_reference",
                )
        label = raw.get("canonical_label")
        if isinstance(label, str) and label.strip():
            normalized_label = normalized(label)
            if normalized_label in registry_labels:
                add(str(subject), "DUPLICATE_NORMALIZED_REGISTRY_LABEL", "normalized registry label collides")
            registry_labels.add(normalized_label)
        if raw.get("status") != "CANDIDATE_UNVERIFIED":
            add(str(subject), "SYNTHETIC_STATUS", "synthetic registry status must be CANDIDATE_UNVERIFIED")
        if not valid_role(raw.get("owner")) or not valid_role(raw.get("reviewer")):
            add(str(subject), "ROLE_STRUCTURE", "owner and reviewer must be stable roles")
        elif raw["owner"]["role"] == raw["reviewer"]["role"]:
            add(str(subject), "SEGREGATION_OF_DUTIES", "owner and reviewer must differ")
        validate_provenance(raw.get("provenance"), str(subject), add, True)

        values = raw.get("values")
        if not isinstance(values, list):
            continue
        codes: set[str] = set()
        labels_and_aliases: set[str] = set()
        for value_index, term in enumerate(values):
            term_subject = (
                term.get("value_id")
                if isinstance(term, dict) and isinstance(term.get("value_id"), str)
                else f"{subject}/<value:{value_index}>"
            )
            if not isinstance(term, dict):
                add(str(term_subject), "VALUE_TYPE", "controlled value must be a mapping")
                continue
            value_id = term.get("value_id")
            if not isinstance(value_id, str) or not definitions.value_id_pattern.fullmatch(
                value_id
            ):
                add(str(term_subject), "VALUE_ID", "value_id format is invalid")
            elif value_id in global_value_ids:
                add(str(term_subject), "DUPLICATE_VALUE_ID", f"duplicate value ID: {value_id}")
            else:
                global_value_ids.add(value_id)
            code = term.get("value_code")
            if not isinstance(code, str) or not definitions.key_pattern.fullmatch(code):
                add(str(term_subject), "VALUE_CODE", "value_code must use lower_snake_case")
            elif code in codes:
                add(str(term_subject), "DUPLICATE_VALUE_CODE", f"duplicate value code: {code}")
            else:
                codes.add(code)
                labels_and_aliases.add(normalized(code))
            names: list[Any] = [term.get("canonical_label")]
            aliases = term.get("aliases")
            if isinstance(aliases, list):
                names.extend(aliases)
            for name in names:
                if not isinstance(name, str) or not name.strip():
                    continue
                normalized_name = normalized(name)
                if normalized_name in labels_and_aliases:
                    add(str(term_subject), "DUPLICATE_NORMALIZED_TERM", f"normalized label or alias collides: {name}")
                else:
                    labels_and_aliases.add(normalized_name)
            if term.get("status") != "CANDIDATE_UNVERIFIED":
                add(str(term_subject), "SYNTHETIC_STATUS", "synthetic value status must be CANDIDATE_UNVERIFIED")
            validate_provenance(term.get("provenance"), str(term_subject), add, True)
    return sorted(issues, key=lambda item: item.render())


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate PD-02A controlled-value registries offline."
    )
    parser.add_argument("registry", nargs="?", default=str(REGISTRY_PATH))
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        definitions = load_definitions()
        registry, parser = load_yaml(Path(args.registry), "PD-02A value registry")
        canonical = Path(args.registry).resolve() == REGISTRY_PATH.resolve()
        issues = validate_registry(
            registry,
            str(args.registry),
            definitions,
            canonical=canonical,
        )
    except (DefinitionError, OSError) as exc:
        print(f"PD02A_VALUE_CONFIGURATION: {exc}", file=sys.stderr)
        return 2
    if issues:
        for issue in issues:
            print(issue.render(), file=sys.stderr)
        return 1
    count = len(registry["value_registries"])
    print(
        f"PD-02A value-registry validation PASS: {count} registry fixture(s); "
        f"parser={parser}; canonical population, network, side effects=false."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
