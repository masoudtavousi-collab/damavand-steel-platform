#!/usr/bin/env python3
"""Fail-closed offline validation for PD-02A standalone Attribute Profiles."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

from validate_product_attributes import (
    DefinitionError,
    load_definitions as load_attribute_definitions,
    load_json,
    load_yaml,
    reject_nonlocal_schema_references,
    require_mapping,
    rfc3339_utc,
    validate_fixture as validate_attribute_fixture,
)
from validate_product_attribute_values import (
    REGISTRY_PATH as VALUE_REGISTRY_PATH,
    Definitions as ValueDefinitions,
    load_definitions as load_value_definitions,
    validate_registry as validate_value_registry,
)
import validate_product_core as product_core_validator


ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = ROOT / "repository/data/contracts/product-attribute-profile.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/product-attribute-profile.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/product-attribute-profiles.yaml"
CANONICAL_ATTRIBUTES = ROOT / "repository/data/registries/product-attributes.yaml"
CANONICAL_VALUES = (
    ROOT / "repository/data/registries/product-attribute-value-registries.yaml"
)
CANONICAL_ENTITIES = ROOT / "repository/data/registries/product-entities.yaml"
DEFAULT_ATTRIBUTES = ROOT / "tests/fixtures/product-attributes/valid-foundation.yaml"
DEFAULT_VALUES = ROOT / "tests/fixtures/pd02/valid-synthetic-controlled-values.yaml"
DEFAULT_ENTITIES = ROOT / "tests/fixtures/product-core/valid-minimal.yaml"

SEMVER_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
ROLE_PATTERN = re.compile(r"^[a-z][a-z0-9-]{2,63}$")
CAPTURED_BY_PATTERN = re.compile(r"^role:[a-z][a-z0-9-]{2,63}$")
MACHINE_CODE_PATTERN = re.compile(r"^[A-Z][A-Z0-9_]*$")


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
    profile_id_pattern: re.Pattern[str]
    scope_id_pattern: re.Pattern[str]
    prohibited_fields: set[str]
    schema_validator: Any


@dataclass(frozen=True)
class ScopeDefinitions:
    entities: dict[str, str]
    product_core_validated: bool


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
    pd02b = require_mapping(contract.get("pd02b_lifecycle"), "pd02b_lifecycle")
    pd02b_history = {
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
    pd02b_status = pd02b.get("current_status")
    if (
        pd02b.get("decision_id") != "FD-PD02B-001"
        or pd02b.get("allowed_transition_sequence") != ["DRAFT", "REVIEW", "APPROVED"]
        or pd02b_status not in pd02b_history
        or pd02b.get("transition_history") != pd02b_history[pd02b_status]
        or pd02b.get("direct_draft_to_approved_forbidden") is not True
        or pd02b.get("canonical_population_authority") is not True
        or pd02b.get("exact_profile_count") != 1
        or pd02b.get("scope_entity_type") != "FAMILY"
        or pd02b.get("required_attribute_keys") != ["material", "grade"]
        or pd02b.get("public_visibility") != "INTERNAL"
        or pd02b.get("variation_axis") is not False
        or pd02b.get("filtering") is not False
        or pd02b.get("inquiry_use") != "NOT_USED"
        or pd02b.get("seo_use") != "PROHIBITED"
        or pd02b.get("approval_evidence_required_for_approved_status") is not True
    ):
        raise DefinitionError("PD-02B Attribute Profile lifecycle or boundary is invalid")


def load_definitions(
    contract_path: Path = CONTRACT_PATH, schema_path: Path = SCHEMA_PATH
) -> Definitions:
    contract, _ = load_yaml(contract_path, "PD-02A Attribute Profile contract")
    contract = require_mapping(contract, "PD-02A Attribute Profile contract")
    if contract.get("contract_id") != "product-attribute-profile":
        raise DefinitionError("Attribute Profile contract_id is invalid")
    if contract.get("contract_version") != "1.0.0":
        raise DefinitionError("Attribute Profile contract_version must be 1.0.0")
    validate_lifecycle(contract)
    policy = require_mapping(contract.get("registry_policy"), "registry_policy")
    if policy != {
        "canonical_registry_must_remain_empty_in_pd02a": True,
        "fixtures_must_be_synthetic": True,
        "scope_references_must_resolve": True,
        "scope_dependencies_must_pass_product_core_validation": True,
        "attribute_references_must_resolve": True,
        "value_registry_references_must_resolve": True,
        "profile_policy_must_not_weaken_attribute_policy": True,
        "network_allowed": False,
        "side_effects_allowed": False,
    }:
        raise DefinitionError("Attribute Profile registry policy differs from PD-02A")
    profile_policy = require_mapping(contract.get("profile_policy"), "profile_policy")
    reconciliation = require_mapping(
        profile_policy.get("reconciliation"), "profile_policy.reconciliation"
    )
    if reconciliation != {
        "controlled_registry_must_match_attribute_reference": True,
        "required_attribute_units_must_remain_nonempty": True,
        "profile_units_must_be_attribute_allowed": True,
        "profile_precision_must_not_exceed_attribute_precision": True,
    }:
        raise DefinitionError("Profile reconciliation policy differs from PD-02A")
    if profile_policy.get("cartesian_generation_forbidden") is not True:
        raise DefinitionError("Cartesian generation must remain forbidden")
    naming = require_mapping(contract.get("stable_identity"), "stable_identity")
    try:
        profile_id_pattern = re.compile(str(naming["profile_id_pattern"]))
        scope_id_pattern = re.compile(str(naming["scope_id_pattern"]))
    except (KeyError, TypeError, re.error) as exc:
        raise DefinitionError("PD-02A profile identity patterns are invalid") from exc
    prohibited = contract.get("prohibited_fields")
    if not isinstance(prohibited, list) or not prohibited:
        raise DefinitionError("PD-02A profile prohibited_fields must be non-empty")

    schema = load_json(schema_path, "PD-02A Attribute Profile schema")
    schema = require_mapping(schema, "PD-02A Attribute Profile schema")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise DefinitionError("PD-02A profile schema must declare Draft 2020-12")
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        raise DefinitionError("PD-02A profile schema must be a closed object")
    reject_nonlocal_schema_references(schema)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise DefinitionError(f"PD-02A Attribute Profile schema is invalid: {exc.message}") from exc
    return Definitions(
        contract_version="1.0.0",
        profile_id_pattern=profile_id_pattern,
        scope_id_pattern=scope_id_pattern,
        prohibited_fields={str(item) for item in prohibited},
        schema_validator=Draft202012Validator(schema, format_checker=FormatChecker()),
    )


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
    value: Any, subject: str, add: Any, *, synthetic: bool
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
    if synthetic and value["evidence_status"] != "SYNTHETIC_TEST_EVIDENCE":
        add(subject, "FORGED_EVIDENCE", "synthetic test evidence is required")


def registry_maps(
    attributes_value: Any,
    values_value: Any,
    value_definitions: ValueDefinitions,
    *,
    canonical: bool = False,
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], list[ValidationIssue]]:
    issues: list[ValidationIssue] = []
    attribute_definitions = load_attribute_definitions()
    attribute_entries = (
        attributes_value.get("attributes")
        if canonical and isinstance(attributes_value, dict)
        else attributes_value
    )
    attribute_issues = validate_attribute_fixture(
        attribute_entries,
        "<canonical-product-attributes>" if canonical else "<synthetic-product-attributes>",
        attribute_definitions,
    )
    for issue in attribute_issues:
        issues.append(
            ValidationIssue(
                issue.source,
                issue.attribute,
                f"PRODUCT_ATTRIBUTE_{issue.code}",
                issue.message,
            )
        )
    value_issues = validate_value_registry(
        values_value,
        "<canonical-value-registries>" if canonical else "<synthetic-value-registries>",
        value_definitions,
        canonical=canonical,
    )
    for issue in value_issues:
        issues.append(ValidationIssue(issue.source, issue.subject, issue.code, issue.message))
    attributes = {
        item["attribute_id"]: item
        for item in (attribute_entries if isinstance(attribute_entries, list) else [])
        if isinstance(item, dict) and isinstance(item.get("attribute_id"), str)
    }
    value_registries = {
        item["value_registry_id"]: item
        for item in values_value.get("value_registries", [])
        if isinstance(item, dict) and isinstance(item.get("value_registry_id"), str)
    }
    return attributes, value_registries, issues


def validated_scope_entities(
    entities_value: Any,
) -> tuple[ScopeDefinitions, list[ValidationIssue]]:
    issues: list[ValidationIssue] = []
    definitions = product_core_validator.load_definitions()
    entity_issues = product_core_validator.validate_dataset(
        entities_value,
        "<synthetic-product-core>",
        definitions,
    )
    for issue in entity_issues:
        issues.append(
            ValidationIssue(
                issue.source,
                issue.entity,
                f"PRODUCT_CORE_{issue.code}",
                issue.message,
            )
        )
    scopes = {
        item["entity_id"]: item["entity_type"]
        for item in (
            entities_value if isinstance(entities_value, list) else []
        )
        if isinstance(item, dict)
        and item.get("entity_type") in {"FAMILY", "SERIES"}
        and isinstance(item.get("entity_id"), str)
    }
    return ScopeDefinitions(scopes, not issues), issues


def validate_registry(
    value: Any,
    source: str,
    definitions: Definitions,
    *,
    canonical: bool,
    attributes: dict[str, dict[str, Any]] | None = None,
    value_registries: dict[str, dict[str, Any]] | None = None,
    scope_entities: ScopeDefinitions | None = None,
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    def add(subject: str, code: str, message: str) -> None:
        issues.append(ValidationIssue(source, subject, code, message))

    expected_envelope = {
        "registry_id",
        "registry_version",
        "contract_version",
        "data_classification",
        "profiles",
    }
    if not isinstance(value, dict):
        add("<registry>", "REGISTRY_TYPE", "profile registry must be a mapping")
        return issues
    if set(value) != expected_envelope:
        add("<registry>", "REGISTRY_STRUCTURE", "profile registry envelope fields differ")
    if value.get("registry_id") != "product-attribute-profiles":
        add("<registry>", "REGISTRY_ID", "registry_id is invalid")
    if not isinstance(value.get("registry_version"), str) or not SEMVER_PATTERN.fullmatch(
        value["registry_version"]
    ):
        add("<registry>", "REGISTRY_VERSION", "registry_version must use X.Y.Z")
    if value.get("contract_version") != definitions.contract_version:
        add("<registry>", "CONTRACT_VERSION", "contract_version is incompatible")
    expected_classification = "CANONICAL_PD02B" if canonical else "SYNTHETIC_FIXTURE"
    if value.get("data_classification") != expected_classification:
        add("<registry>", "DATA_CLASSIFICATION", f"expected {expected_classification}")
    profiles = value.get("profiles")
    if not isinstance(profiles, list):
        add("<registry>", "PROFILE_ENTRIES", "profiles must be a list")
        return sorted(issues, key=lambda item: item.render())
    if not canonical and not profiles:
        add("<registry>", "EMPTY_SYNTHETIC_FIXTURE", "synthetic fixture needs one profile")

    attributes = attributes or {}
    value_registries = value_registries or {}
    if (
        scope_entities is None
        or not isinstance(scope_entities, ScopeDefinitions)
        or not scope_entities.product_core_validated
    ):
        add(
            "<registry>",
            "UNVALIDATED_SCOPE_DEPENDENCIES",
            "Profile scopes require a successfully validated Product Core dataset",
        )
        resolved_scope_entities: dict[str, str] = {}
    else:
        resolved_scope_entities = scope_entities.entities
    profile_ids: set[str] = set()
    scope_ids: set[str] = set()
    for index, raw in enumerate(profiles):
        subject = (
            raw.get("profile_id")
            if isinstance(raw, dict) and isinstance(raw.get("profile_id"), str)
            else f"<profile:{index}>"
        )
        if not isinstance(raw, dict):
            add(str(subject), "PROFILE_TYPE", "profile must be a mapping")
            continue
        for error in sorted(
            definitions.schema_validator.iter_errors(raw),
            key=lambda item: (tuple(str(part) for part in item.absolute_path), item.message),
        ):
            location = "/".join(str(part) for part in error.absolute_path) or "<root>"
            add(str(subject), "SCHEMA_VALIDATION", f"{location}: {error.message}")
        for field in sorted(set(iter_keys(raw)) & definitions.prohibited_fields):
            add(str(subject), "PROHIBITED_FIELD", f"prohibited field: {field}")
        profile_id = raw.get("profile_id")
        if not isinstance(profile_id, str) or not definitions.profile_id_pattern.fullmatch(
            profile_id
        ):
            add(str(subject), "PROFILE_ID", "profile_id format is invalid")
        elif profile_id in profile_ids:
            add(str(subject), "DUPLICATE_PROFILE_ID", f"duplicate profile ID: {profile_id}")
        else:
            profile_ids.add(profile_id)
        scope_id = raw.get("scope_entity_id")
        scope_type = raw.get("scope_entity_type")
        if not isinstance(scope_id, str) or not definitions.scope_id_pattern.fullmatch(scope_id):
            add(str(subject), "SCOPE_ID", "scope_entity_id format is invalid")
        elif scope_id not in resolved_scope_entities:
            add(
                str(subject),
                "ORPHAN_PROFILE_SCOPE",
                f"unknown {'canonical' if canonical else 'synthetic'} scope: {scope_id}",
            )
        elif resolved_scope_entities[scope_id] != scope_type:
            add(str(subject), "SCOPE_TYPE_MISMATCH", "scope type differs from resolved entity")
        elif scope_id in scope_ids:
            add(str(subject), "DUPLICATE_PROFILE_SCOPE", f"duplicate profile scope: {scope_id}")
        else:
            scope_ids.add(scope_id)
        if not canonical and raw.get("status") != "CANDIDATE_UNVERIFIED":
            add(str(subject), "SYNTHETIC_STATUS", "synthetic profile status must be CANDIDATE_UNVERIFIED")
        if not valid_role(raw.get("owner")) or not valid_role(raw.get("reviewer")):
            add(str(subject), "ROLE_STRUCTURE", "owner and reviewer must be stable roles")
        elif raw["owner"]["role"] == raw["reviewer"]["role"]:
            add(str(subject), "SEGREGATION_OF_DUTIES", "owner and reviewer must differ")
        validate_provenance(
            raw.get("provenance"), str(subject), add, synthetic=not canonical
        )

        seen_attributes: set[str] = set()
        for rule in raw.get("attribute_rules", []) if isinstance(raw.get("attribute_rules"), list) else []:
            if not isinstance(rule, dict):
                continue
            attribute_id = rule.get("attribute_id")
            if attribute_id in seen_attributes:
                add(str(subject), "DUPLICATE_PROFILE_ATTRIBUTE", f"duplicate rule: {attribute_id}")
            elif isinstance(attribute_id, str):
                seen_attributes.add(attribute_id)
            attribute = attributes.get(attribute_id)
            if attribute is None:
                add(str(subject), "UNKNOWN_ATTRIBUTE", f"unknown attribute: {attribute_id}")
                continue
            requirement = rule.get("requirement_level")
            if requirement == "PROHIBITED" and (
                rule.get("variation_axis") is not False
                or rule.get("filtering") is not False
                or rule.get("inquiry_use") != "NOT_USED"
                or rule.get("seo_use") != "PROHIBITED"
            ):
                add(str(subject), "PROHIBITED_RULE_BEHAVIOR", "PROHIBITED rule cannot enable use")
            if requirement == "CONDITIONAL" and not rule.get("condition_reference"):
                add(str(subject), "CONDITION_REQUIRED", "CONDITIONAL rule needs condition_reference")
            if requirement != "CONDITIONAL" and rule.get("condition_reference") is not None:
                add(str(subject), "UNEXPECTED_CONDITION", "only CONDITIONAL accepts condition_reference")

            source_kind = rule.get("value_source")
            registry_id = rule.get("value_registry_id")
            data_type = attribute.get("data_type")
            if source_kind == "CONTROLLED_REGISTRY":
                registry = value_registries.get(registry_id)
                if data_type != "CONTROLLED_TERM":
                    add(str(subject), "VALUE_SOURCE_TYPE", "controlled registry requires CONTROLLED_TERM")
                if registry is None:
                    add(str(subject), "UNRESOLVED_VALUE_REGISTRY", f"unknown value registry: {registry_id}")
                elif registry.get("attribute_id") != attribute_id:
                    add(str(subject), "REGISTRY_ATTRIBUTE_MISMATCH", "value registry belongs to another attribute")
                declared_registry = (
                    attribute.get("validation", {})
                    .get("constraints", {})
                    .get("value_registry_reference")
                )
                if registry_id != declared_registry:
                    add(
                        str(subject),
                        "ATTRIBUTE_REGISTRY_POLICY",
                        "Profile registry differs from the Attribute value_registry_reference",
                    )
            elif source_kind == "ENTITY_REFERENCE":
                if data_type != "ENTITY_REFERENCE":
                    add(str(subject), "VALUE_SOURCE_TYPE", "entity source requires ENTITY_REFERENCE")
            elif source_kind == "TYPED_VALIDATION":
                if data_type in {"CONTROLLED_TERM", "ENTITY_REFERENCE"}:
                    add(str(subject), "VALUE_SOURCE_TYPE", f"{data_type} cannot use typed validation")

            allowed_units = rule.get("allowed_unit_ids")
            attribute_unit_policy = attribute.get("unit_policy", {})
            attribute_units = attribute_unit_policy.get("allowed_unit_ids", [])
            if isinstance(allowed_units, list):
                if attribute_unit_policy.get("mode") == "REQUIRED" and not allowed_units:
                    add(
                        str(subject),
                        "REQUIRED_UNITS_EMPTY",
                        "Profile must retain at least one Unit for a REQUIRED-unit Attribute",
                    )
                if attribute_unit_policy.get("mode") == "FORBIDDEN" and allowed_units:
                    add(
                        str(subject),
                        "FORBIDDEN_UNITS_PRESENT",
                        "Profile cannot add Units to a unit-forbidden Attribute",
                    )
                for unit_id in allowed_units:
                    if unit_id not in attribute_units:
                        add(str(subject), "UNIT_NOT_ALLOWED", f"unit is not allowed by attribute: {unit_id}")
            if rule.get("precision") is not None and data_type != "DECIMAL":
                add(str(subject), "PRECISION_TYPE", "precision is allowed only for DECIMAL")
            attribute_precision = (
                attribute.get("validation", {})
                .get("constraints", {})
                .get("decimal_places")
            )
            if (
                isinstance(rule.get("precision"), int)
                and isinstance(attribute_precision, int)
                and rule["precision"] > attribute_precision
            ):
                add(
                    str(subject),
                    "PRECISION_WEAKENS_ATTRIBUTE",
                    "Profile precision exceeds the Attribute decimal_places limit",
                )
    return sorted(issues, key=lambda item: item.render())


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate PD-02A Attribute Profiles offline."
    )
    parser.add_argument("profiles", nargs="?", default=str(REGISTRY_PATH))
    parser.add_argument("--attributes", default=str(DEFAULT_ATTRIBUTES))
    parser.add_argument("--value-registries", default=str(DEFAULT_VALUES))
    parser.add_argument("--entities", default=str(DEFAULT_ENTITIES))
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        definitions = load_definitions()
        profiles, profile_parser = load_yaml(Path(args.profiles), "PD-02A profiles")
        canonical = Path(args.profiles).resolve() == REGISTRY_PATH.resolve()
        if canonical:
            attributes_value, attribute_parser = load_yaml(
                CANONICAL_ATTRIBUTES, "PD-02B canonical attributes"
            )
            values_value, value_parser = load_yaml(
                CANONICAL_VALUES, "PD-02B canonical value registries"
            )
            entities_value, entity_parser = load_yaml(
                CANONICAL_ENTITIES, "PD-02B canonical Product Core"
            )
            value_definitions = load_value_definitions()
            attributes, value_registries, dependency_issues = registry_maps(
                attributes_value,
                values_value,
                value_definitions,
                canonical=True,
            )
            scope_entities, scope_issues = validated_scope_entities(entities_value)
            issues = dependency_issues + scope_issues + validate_registry(
                profiles,
                str(args.profiles),
                definitions,
                canonical=True,
                attributes=attributes,
                value_registries=value_registries,
                scope_entities=scope_entities,
            )
            parser_sources = [
                profile_parser,
                attribute_parser,
                value_parser,
                entity_parser,
            ]
        else:
            attributes_value, attribute_parser = load_yaml(
                Path(args.attributes), "PD-02A synthetic attributes"
            )
            values_value, value_parser = load_yaml(
                Path(args.value_registries), "PD-02A synthetic value registries"
            )
            entities_value, entity_parser = load_yaml(
                Path(args.entities), "PD-02A synthetic Product Core"
            )
            value_definitions = load_value_definitions()
            attributes, value_registries, dependency_issues = registry_maps(
                attributes_value, values_value, value_definitions
            )
            scope_entities, scope_issues = validated_scope_entities(entities_value)
            issues = dependency_issues + validate_registry(
                profiles,
                str(args.profiles),
                definitions,
                canonical=False,
                attributes=attributes,
                value_registries=value_registries,
                scope_entities=scope_entities,
            )
            issues = scope_issues + issues
            parser_sources = [
                profile_parser,
                attribute_parser,
                value_parser,
                entity_parser,
            ]
    except (DefinitionError, product_core_validator.DefinitionError, OSError) as exc:
        print(f"PD02A_PROFILE_CONFIGURATION: {exc}", file=sys.stderr)
        return 2
    issues = sorted(issues, key=lambda item: item.render())
    if issues:
        for issue in issues:
            print(issue.render(), file=sys.stderr)
        return 1
    count = len(profiles["profiles"])
    print(
        f"PD-02A/PD-02B Attribute Profile validation PASS: {count} profile item(s); "
        f"parsers={'; '.join(sorted(set(parser_sources)))}; "
        "Cartesian generation, network, side effects=false."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
