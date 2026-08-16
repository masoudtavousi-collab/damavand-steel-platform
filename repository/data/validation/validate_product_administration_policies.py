#!/usr/bin/env python3
"""Validate C002 Product Administration policies offline and fail closed."""

from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any
import unicodedata

from validate_pd03a_pilot_prerequisite import (
    ROOT,
    ValidationConfigurationError,
    load_json,
    load_yaml,
    require_mapping,
    validate_schema,
    walk,
)


CONTRACT_PATH = ROOT / "repository/data/contracts/product-administration-policy.contract.yaml"
SCHEMA_PATH = ROOT / "repository/data/schemas/product-administration-policy.schema.json"
REGISTRY_PATH = ROOT / "repository/data/registries/extensions/c002/product-administration-policies.yaml"
PRODUCT_ENTITIES_PATH = ROOT / "repository/data/registries/product-entities.yaml"
PD03A_EXTENSION_PATH = ROOT / "repository/data/registries/extensions/pd03a/pilot-prerequisite.yaml"
PRODUCT_ATTRIBUTES_PATH = ROOT / "repository/data/registries/product-attributes.yaml"
CONTROLLED_VALUES_PATH = ROOT / "repository/data/registries/product-attribute-value-registries.yaml"
DIMENSIONS_PATH = ROOT / "repository/data/registries/measurement-dimensions.yaml"
UNITS_PATH = ROOT / "repository/data/registries/attribute-units.yaml"
EXPECTED_CONTRACT_DIGEST = "75b608e67b6ca3c870e6bf0b533310fbb131a75fa576a79e75c4a936659c33ff"
REFERENCE_DATA: dict[str, dict[str, Any]] = {}

COMMERCE_STATES = [
    "INQUIRY_ONLY", "PURCHASE_CANDIDATE", "PURCHASE_ELIGIBLE_INACTIVE",
    "PURCHASE_ENABLED", "SUSPENDED", "REVOKED",
]
COMMERCE_TRANSITIONS = [
    ("INQUIRY_ONLY", "PURCHASE_CANDIDATE"),
    ("PURCHASE_CANDIDATE", "INQUIRY_ONLY"),
    ("PURCHASE_CANDIDATE", "PURCHASE_ELIGIBLE_INACTIVE"),
    ("PURCHASE_ELIGIBLE_INACTIVE", "INQUIRY_ONLY"),
    ("PURCHASE_ELIGIBLE_INACTIVE", "PURCHASE_ENABLED"),
    ("PURCHASE_ENABLED", "SUSPENDED"),
    ("SUSPENDED", "PURCHASE_ENABLED"),
    ("INQUIRY_ONLY", "REVOKED"),
    ("PURCHASE_CANDIDATE", "REVOKED"),
    ("PURCHASE_ELIGIBLE_INACTIVE", "REVOKED"),
    ("PURCHASE_ENABLED", "REVOKED"),
    ("SUSPENDED", "REVOKED"),
]
COMMERCE_GATES = [
    "product", "sku", "configuration", "availability",
    "pricing_authority_boolean_only", "fulfillment", "inventory",
    "legal_commercial", "security_payment", "public_presentation", "runtime",
    "production", "rollback_kill_switch", "founder",
]

POLICY_DESCRIPTORS = [
    ("papolicy:6a1d0c02a001", "product_builder", "PRODUCT_BUILDER"),
    ("papolicy:6a1d0c02a002", "controlled_value_proposal", "CONTROLLED_VALUE_PROPOSAL"),
    ("papolicy:6a1d0c02a003", "brand_provenance", "BRAND_PROVENANCE"),
    ("papolicy:6a1d0c02a004", "mass_provenance", "MASS_PROVENANCE"),
    ("papolicy:6a1d0c02a005", "electrostatic_appearance", "ELECTROSTATIC_APPEARANCE"),
    ("papolicy:6a1d0c02a006", "commerce_eligibility", "COMMERCE_ELIGIBILITY"),
    ("papolicy:6a1d0c02a007", "inventory_harmony", "INVENTORY_HARMONY"),
    ("papolicy:6a1d0c02a008", "damavand_central_bom_interface", "DAMAVAND_CENTRAL_BOM_INTERFACE"),
]
EXPECTED_POLICY_PROVENANCE = {
    "source_type": "C002_MISSION_PACKET",
    "source_reference": "C002",
    "captured_by": "role:product-data-steward",
    "captured_at": "2026-08-16T00:00:00Z",
    "evidence_status": "FOUNDER_AUTHORIZED_POLICY_SCOPE",
}
EXPECTED_SYNTHETIC_PROVENANCE = {
    "source_type": "SYNTHETIC_FIXTURE",
    "source_reference": "fixture:c002-product-administration",
    "captured_by": "role:product-data-steward",
    "captured_at": "2026-08-16T00:00:00Z",
    "evidence_status": "SYNTHETIC_NO_CLAIM",
}
PROHIBITED_FIELDS = {
    "product_population", "sku_population", "availability", "availability_claim",
    "stock", "stock_claim", "price", "pricing", "margin", "discount", "coupon",
    "offer", "cart", "checkout", "payment", "wordpress", "woocommerce", "import",
    "publication", "runtime", "deployment", "production",
    "central_steel_implementation",
}


def load_validator(
    contract_path: Path = CONTRACT_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> tuple[Any, dict[str, Any]]:
    global REFERENCE_DATA
    contract = require_mapping(load_yaml(contract_path), "Product Administration contract")
    semantic = json.dumps(contract, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    if hashlib.sha256(semantic).hexdigest() != EXPECTED_CONTRACT_DIGEST:
        raise ValidationConfigurationError("Product Administration contract literal policy differs")

    base_entities = load_yaml(PRODUCT_ENTITIES_PATH)
    extension = require_mapping(load_yaml(PD03A_EXTENSION_PATH), "PD03A extension")
    base_attributes = require_mapping(load_yaml(PRODUCT_ATTRIBUTES_PATH), "product attributes")
    controlled = require_mapping(load_yaml(CONTROLLED_VALUES_PATH), "controlled values")
    dimensions = require_mapping(load_yaml(DIMENSIONS_PATH), "measurement dimensions")
    units = require_mapping(load_yaml(UNITS_PATH), "attribute units")
    entity_records = list(base_entities) + list(extension.get("entities", []))
    attribute_records = list(base_attributes.get("attributes", [])) + list(extension.get("attributes", []))
    value_registry_records = list(controlled.get("value_registries", [])) + list(extension.get("value_registries", []))
    REFERENCE_DATA = {
        "entities": {item["entity_id"]: item for item in entity_records if isinstance(item, dict)},
        "attributes": {item["attribute_id"]: item for item in attribute_records if isinstance(item, dict)},
        "profiles": {item["profile_id"]: item for item in extension.get("profiles", []) if isinstance(item, dict)},
        "value_registries": {item["value_registry_id"]: item for item in value_registry_records if isinstance(item, dict)},
        "dimensions": {item["dimension_id"]: item for item in dimensions.get("dimensions", []) if isinstance(item, dict)},
        "units": {item["unit_id"]: item for item in units.get("units", []) if isinstance(item, dict)},
    }
    schema = require_mapping(load_json(schema_path), "Product Administration schema")
    return validate_schema(schema), contract


def parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def normalized_text(value: str) -> str:
    return unicodedata.normalize("NFC", value.strip()).casefold()


def allowed_label_script(value: str, locale: str) -> bool:
    if value != value.strip() or value != unicodedata.normalize("NFC", value):
        return False
    ascii_punctuation = set(" .,_+()/'&-")
    if locale == "en":
        return bool(value) and all(
            ord(character) < 128
            and (character.isascii() and character.isalnum() or character in ascii_punctuation)
            for character in value
        )
    if locale != "fa-IR":
        return False
    persian_punctuation = ascii_punctuation | set("،؛؟")
    approved_digit_ranges = set("0123456789۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩")
    for character in value:
        if character in persian_punctuation or character in approved_digit_ranges:
            continue
        codepoint = ord(character)
        in_approved_range = (
            0x0600 <= codepoint <= 0x06FF
            or 0x0750 <= codepoint <= 0x077F
            or 0x08A0 <= codepoint <= 0x08FF
        )
        if not in_approved_range or not unicodedata.name(character, "").startswith("ARABIC"):
            return False
    return bool(value)


def validate_package(value: Any, validator: Any, *, canonical: bool | None = None) -> list[str]:
    issues: list[str] = []

    def add(code: str, message: str) -> None:
        issues.append(f"[{code}] {message}")

    for error in validator.iter_errors(value):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        add("SCHEMA_VALIDATION", f"{location}: {error.message}")
    if not isinstance(value, dict):
        return sorted(set(issues))

    classification = value.get("data_classification")
    if canonical is None:
        canonical = classification == "C002_POLICY_ONLY"
    if canonical and classification != "C002_POLICY_ONLY":
        add("CANONICAL_CLASSIFICATION", "canonical registry must be C002_POLICY_ONLY")
    if not canonical and classification != "SYNTHETIC_FIXTURE":
        add("SYNTHETIC_CLASSIFICATION", "test package must be SYNTHETIC_FIXTURE")
    expected_root = {
        "registry_id": "c002-product-administration-policies",
        "registry_version": "1.0.0",
        "contract_version": "1.0.0",
        "status": "APPROVED",
    }
    for key, expected in expected_root.items():
        if value.get(key) != expected:
            add("EXACT_ROOT", f"exact root field differs: {key}")

    policies = value.get("policies", [])
    if not isinstance(policies, list) or len(policies) != 8:
        add("EXACT_POLICY_COUNT", "exactly eight policy records are required")
        policies = policies if isinstance(policies, list) else []
    policy_ids: set[str] = set()
    policy_keys: set[str] = set()
    policy_kinds: set[str] = set()
    actual_descriptors: list[tuple[Any, Any, Any]] = []
    for policy in policies:
        if not isinstance(policy, dict):
            continue
        actual_descriptors.append((policy.get("policy_id"), policy.get("policy_key"), policy.get("record_kind")))
        policy_ids.add(str(policy.get("policy_id")))
        policy_keys.add(str(policy.get("policy_key")))
        policy_kinds.add(str(policy.get("record_kind")))
        expected_policy = {
            "canonical_instance_population_allowed": False,
            "promotion_requires_separate_authority": True,
            "runtime_authority": False,
            "status": "APPROVED",
            "owner": {"role": "product-data-steward"},
            "provenance": EXPECTED_POLICY_PROVENANCE,
            "record_version": "1.0.0",
        }
        for key, expected in expected_policy.items():
            if policy.get(key) != expected:
                add("POLICY_BOUNDARY", f"{policy.get('record_kind')}: {key} differs")
    if actual_descriptors != POLICY_DESCRIPTORS:
        add("EXACT_POLICY_DESCRIPTORS", "policy identities, keys, kinds, or order differ")
    if len(policy_ids) != len(policies) or len(policy_keys) != len(policies) or len(policy_kinds) != len(policies):
        add("DUPLICATE_POLICY", "policy IDs, keys, and kinds must be unique")

    instances = value.get("instances", [])
    if not isinstance(instances, list):
        instances = []
    if canonical and instances:
        add("CANONICAL_INSTANCE_POPULATION", "canonical registry must keep instances empty")
    if not canonical and not 8 <= len(instances) <= 16:
        add("SYNTHETIC_INSTANCE_COUNT", "synthetic/reference package must contain 8..16 bounded instances")
    record_ids: set[str] = set()
    instance_kinds: list[str] = []
    mass_record_ids = {
        item.get("record_id") for item in instances
        if isinstance(item, dict) and item.get("record_kind") == "MASS_PROVENANCE"
    }
    for instance in instances:
        if not isinstance(instance, dict):
            continue
        record_id = str(instance.get("record_id"))
        if record_id in record_ids:
            add("DUPLICATE_RECORD_ID", record_id)
        record_ids.add(record_id)
        kind = str(instance.get("record_kind"))
        instance_kinds.append(kind)
        if instance.get("status") != "CANDIDATE_UNVERIFIED":
            add("INSTANCE_STATUS", f"{kind} must remain CANDIDATE_UNVERIFIED")
        if instance.get("owner") != {"role": "product-data-steward"}:
            add("INSTANCE_OWNER", f"{kind} owner differs")
        if instance.get("provenance") != EXPECTED_SYNTHETIC_PROVENANCE:
            add("INSTANCE_PROVENANCE", f"{kind} must remain unmistakably synthetic")

        if kind == "PRODUCT_BUILDER":
            if (
                instance.get("output_state") != "DRAFT_CANDIDATE_BUNDLE"
                or instance.get("cartesian_generation_forbidden") is not True
                or instance.get("sku_derivation_allowed") is not False
                or instance.get("canonical_promotion_allowed") is not False
            ):
                add("PRODUCT_BUILDER_BOUNDARY", "builder may emit only a non-promotable draft candidate")
            entities = REFERENCE_DATA.get("entities", {})
            chain = [
                ("catalog_entity_id", "CATALOG", None),
                ("platform_entity_id", "PLATFORM", "catalog_entity_id"),
                ("family_entity_id", "FAMILY", "platform_entity_id"),
                ("series_entity_id", "SERIES", "family_entity_id"),
                ("variant_rule_set_entity_id", "VARIANT_RULE_SET", "series_entity_id"),
            ]
            for field, expected_type, parent_field in chain:
                record = entities.get(instance.get(field))
                if not isinstance(record, dict) or record.get("entity_type") != expected_type or record.get("status") != "APPROVED":
                    add("PRODUCT_BUILDER_REFERENCE", f"{field} must resolve to an APPROVED canonical {expected_type}")
                elif parent_field and record.get("parent_entity_id") != instance.get(parent_field):
                    add("PRODUCT_BUILDER_CHAIN", f"{field} does not belong to the selected canonical chain")
            profile = REFERENCE_DATA.get("profiles", {}).get(instance.get("profile_id"))
            if not isinstance(profile, dict) or profile.get("status") != "APPROVED" or profile.get("scope_entity_id") != instance.get("series_entity_id"):
                add("PRODUCT_BUILDER_PROFILE", "profile must resolve to the APPROVED profile scoped to the selected Series")
                profile_rules = []
            else:
                profile_rules = profile.get("attribute_rules", [])
            seen_attributes: set[Any] = set()
            for selection in instance.get("controlled_value_selections", []):
                if not isinstance(selection, dict):
                    continue
                attribute_id = selection.get("attribute_id")
                registry_id = selection.get("value_registry_id")
                term_id = selection.get("value_term_id")
                if attribute_id in seen_attributes:
                    add("PRODUCT_BUILDER_SELECTION_DUPLICATE", f"duplicate controlled selection for {attribute_id}")
                seen_attributes.add(attribute_id)
                registry = REFERENCE_DATA.get("value_registries", {}).get(registry_id)
                attribute = REFERENCE_DATA.get("attributes", {}).get(attribute_id)
                terms = registry.get("values", []) if isinstance(registry, dict) else []
                if not isinstance(attribute, dict) or attribute.get("status") != "APPROVED":
                    add("PRODUCT_BUILDER_ATTRIBUTE", f"{attribute_id} is not an APPROVED canonical Attribute")
                if not isinstance(registry, dict) or registry.get("status") != "APPROVED" or registry.get("attribute_id") != attribute_id:
                    add("PRODUCT_BUILDER_VALUE_REGISTRY", f"{registry_id} does not bind the selected attribute")
                if not any(isinstance(term, dict) and term.get("value_id") == term_id and term.get("status") == "APPROVED" for term in terms):
                    add("PRODUCT_BUILDER_VALUE_TERM", f"{term_id} is not an APPROVED term in {registry_id}")
                if not any(
                    isinstance(rule, dict)
                    and rule.get("attribute_id") == attribute_id
                    and rule.get("value_source") == "CONTROLLED_REGISTRY"
                    and rule.get("value_registry_id") == registry_id
                    for rule in profile_rules
                ):
                    add("PRODUCT_BUILDER_PROFILE_BINDING", f"{attribute_id}/{registry_id} is not allowed by the selected profile")
        elif kind == "CONTROLLED_VALUE_PROPOSAL":
            target = instance.get("proposal_target", {})
            if (
                instance.get("normalization") != ["NFC", "CASEFOLD", "TRIM"]
                or instance.get("duplicate_check_required") is not True
                or instance.get("domain_review_required") is not True
                or instance.get("direct_canonical_registry_mutation_allowed") is not False
                or instance.get("approved_proposal_requires_separate_promotion_authority") is not True
            ):
                add("CONTROLLED_VALUE_BOUNDARY", "Add Value cannot directly create a term or mutate a canonical registry")
            if re.fullmatch(r"[a-z0-9]+(?:_[a-z0-9]+)*", str(instance.get("value_code", ""))) is None:
                add("CONTROLLED_VALUE_SCRIPT", "value_code must be ASCII lower_snake_case")
            labels = instance.get("labels", {})
            if not isinstance(labels, dict) or not allowed_label_script(str(labels.get("canonical_en", "")), "en"):
                add("CONTROLLED_VALUE_SCRIPT", "English label violates the ASCII Latin/digit/punctuation allowlist")
            if not isinstance(labels, dict) or not allowed_label_script(str(labels.get("fa_ir", "")), "fa-IR"):
                add("CONTROLLED_VALUE_SCRIPT", "Persian label violates the approved Arabic-script allowlist")
            aliases = instance.get("aliases", [])
            for alias in aliases if isinstance(aliases, list) else []:
                if not isinstance(alias, dict) or not allowed_label_script(str(alias.get("value", "")), str(alias.get("locale", ""))):
                    add("CONTROLLED_VALUE_SCRIPT", "alias violates its locale-specific script allowlist")
            if isinstance(target, dict) and target.get("target_type") == "GENERIC_CONTROLLED_VALUE":
                attribute = REFERENCE_DATA.get("attributes", {}).get(target.get("attribute_id"))
                registry = REFERENCE_DATA.get("value_registries", {}).get(target.get("value_registry_id"))
                if not isinstance(attribute, dict) or attribute.get("status") != "APPROVED":
                    add("CONTROLLED_VALUE_TARGET", "generic proposal Attribute must resolve to an APPROVED canonical owner")
                if (
                    not isinstance(registry, dict)
                    or registry.get("status") != "APPROVED"
                    or registry.get("attribute_id") != target.get("attribute_id")
                ):
                    add("CONTROLLED_VALUE_TARGET", "generic proposal registry must resolve and bind the exact Attribute")
                if target.get("proposed_value_term_id") is not None:
                    add("CONTROLLED_VALUE_TARGET", "proposal cannot create or pre-allocate a canonical value term")
                canonical_tokens: list[str] = []
                if isinstance(registry, dict):
                    for term in registry.get("values", []):
                        if not isinstance(term, dict) or term.get("status") != "APPROVED":
                            continue
                        canonical_tokens.extend([str(term.get("value_code", "")), str(term.get("canonical_label", ""))])
                        canonical_tokens.extend(str(alias) for alias in term.get("aliases", []))
                proposed_tokens = [str(instance.get("value_code", ""))]
                if isinstance(labels, dict):
                    proposed_tokens.extend(str(label) for label in labels.values())
                proposed_tokens.extend(
                    str(alias.get("value", "")) for alias in aliases if isinstance(alias, dict)
                )
                canonical_normalized = {normalized_text(token) for token in canonical_tokens if token.strip()}
                for token in proposed_tokens:
                    normalized = normalized_text(token)
                    if normalized in canonical_normalized:
                        add("CONTROLLED_VALUE_DUPLICATE", f"proposed code/label/alias duplicates an approved term: {token}")
            elif isinstance(target, dict) and target.get("target_type") == "ELECTROSTATIC_APPEARANCE":
                if (
                    target.get("proposal_namespace") != "ELECTROSTATIC"
                    or target.get("proposal_owner") != {"role": "electrostatic-appearance-steward"}
                    or target.get("finish_attribute_id") is not None
                    or target.get("finish_value_registry_id") is not None
                    or target.get("pvd_target_reference") is not None
                ):
                    add("CONTROLLED_VALUE_TARGET", "electrostatic proposal must remain isolated from Finish and PVD owners")
            else:
                add("CONTROLLED_VALUE_TARGET", "proposal target must use one supported discriminated branch")
            history = instance.get("transition_history", [])
            legal_edges = [("DRAFT", "VALIDATE"), ("VALIDATE", "REVIEW"), ("REVIEW", "APPROVED"), ("REVIEW", "REJECTED")]
            current = "DRAFT"
            previous_time: datetime | None = None
            for index, transition in enumerate(history if isinstance(history, list) else []):
                if not isinstance(transition, dict):
                    continue
                edge = (transition.get("from_state"), transition.get("to_state"))
                if transition.get("sequence") != index + 1 or edge not in legal_edges or edge[0] != current:
                    add("CONTROLLED_VALUE_TRANSITION", "proposal transition history must be sequential and use only legal edges")
                transition_time = parse_time(transition.get("transitioned_at"))
                if transition_time is None or (previous_time is not None and transition_time <= previous_time):
                    add("CONTROLLED_VALUE_TRANSITION_TIME", "proposal transition timestamps must be strictly increasing")
                previous_time = transition_time or previous_time
                stage_refs = {
                    ("DRAFT", "VALIDATE"): instance.get("validation_evidence_references", []),
                    ("VALIDATE", "REVIEW"): instance.get("review_evidence_references", []),
                    ("REVIEW", "APPROVED"): instance.get("approval_evidence_references", []),
                    ("REVIEW", "REJECTED"): instance.get("approval_evidence_references", []),
                }.get(edge, [])
                if transition.get("evidence_references") != stage_refs or not stage_refs:
                    add("CONTROLLED_VALUE_TRANSITION_EVIDENCE", "each transition must bind its exact stage evidence")
                if transition.get("reviewer_role") == transition.get("actor_role"):
                    add("CONTROLLED_VALUE_TRANSITION_REVIEWER", "transition actor and reviewer must be separate")
                current = str(edge[1])
            if instance.get("proposal_state") != current:
                add("CONTROLLED_VALUE_STATE", "proposal_state must equal the state derived from transition history")
            validation_refs = instance.get("validation_evidence_references", [])
            review_refs = instance.get("review_evidence_references", [])
            approval_refs = instance.get("approval_evidence_references", [])
            if current == "DRAFT" and any((validation_refs, review_refs, approval_refs)):
                add("CONTROLLED_VALUE_EVIDENCE", "DRAFT proposal cannot claim later-stage evidence")
            if current in {"VALIDATE", "REVIEW", "APPROVED", "REJECTED"} and not validation_refs:
                add("CONTROLLED_VALUE_EVIDENCE", "VALIDATE and later states require validation evidence")
            if current in {"REVIEW", "APPROVED", "REJECTED"} and not review_refs:
                add("CONTROLLED_VALUE_EVIDENCE", "REVIEW and later states require review evidence")
            if current in {"APPROVED", "REJECTED"} and not approval_refs:
                add("CONTROLLED_VALUE_EVIDENCE", "terminal proposal states require approval/rejection evidence")
        elif kind == "BRAND_PROVENANCE":
            if instance.get("relationships_are_distinct") is not True or instance.get("inference_forbidden") is not True:
                add("BRAND_BOUNDARY", "brand, manufacturer, supplier, and origin must remain distinct")
            if (
                not isinstance(instance.get("applicability_scope"), dict)
                or not instance.get("evidence_references")
                or instance.get("reviewer") != {"role": "repository-guardian-independent"}
                or instance.get("reviewer") == instance.get("owner")
            ):
                add("BRAND_GOVERNANCE", "brand applicability, evidence, and independent reviewer are required")
            try:
                brand_from = datetime.fromisoformat(str(instance.get("effective_from")).replace("Z", "+00:00"))
                raw_brand_until = instance.get("effective_until")
                brand_until = None if raw_brand_until is None else datetime.fromisoformat(str(raw_brand_until).replace("Z", "+00:00"))
                if brand_until is not None and brand_until < brand_from:
                    add("BRAND_EFFECTIVE_PERIOD", "brand effective_until cannot precede effective_from")
            except ValueError:
                add("BRAND_EFFECTIVE_PERIOD", "brand effective period must contain valid timestamps")
            if instance.get("brand_status") in {"MISSING_DATA_VALUE", "NOT_APPLICABLE"} and any(
                instance.get(key) is not None for key in (
                    "brand_identity_reference", "manufacturer_reference", "supplier_reference", "origin_reference"
                )
            ):
                add("BRAND_MISSINGNESS", "missing/non-applicable brand cannot carry inferred relationships")
        elif kind == "MASS_PROVENANCE":
            if (
                instance.get("canonical_quantity") != "MASS"
                or instance.get("approved_mass_unit_required_for_canonical_value") is not True
                or instance.get("canonical_value_promotion_allowed") is not False
            ):
                add("MASS_BOUNDARY", "mass requires provenance and cannot be promoted by C002")
            subject = REFERENCE_DATA.get("entities", {}).get(instance.get("subject_reference"))
            if not isinstance(subject, dict) or subject.get("status") != "APPROVED":
                add("MASS_SUBJECT_REFERENCE", "mass subject must resolve to an APPROVED canonical Product entity")
            applicability = instance.get("applicability_scope", {})
            if not isinstance(applicability, dict) or applicability.get("basis") != instance.get("basis"):
                add("MASS_BASIS_BINDING", "applicability_scope.basis must equal the top-level Mass basis")
            method = instance.get("mass_method")
            evidence = instance.get("method_evidence")
            if not isinstance(evidence, dict) or evidence.get("method") != method:
                add("MASS_METHOD_BINDING", "mass_method must match exactly one method evidence branch")
            elif method == "MANUFACTURER_STATED" and set(evidence) != {
                "method", "document_reference", "document_revision", "source_locator",
            }:
                add("MASS_MANUFACTURER_EVIDENCE", "manufacturer statement requires document, revision, and locator")
            elif method == "MEASURED" and set(evidence) != {
                "method", "procedure_reference", "instrument_reference", "calibration_reference",
                "sample_reference", "measured_at",
            }:
                add("MASS_MEASURED_EVIDENCE", "measurement requires procedure, instrument, calibration, sample, and time")
            elif method == "CALCULATED":
                inputs = evidence.get("inputs", []) if isinstance(evidence, dict) else []
                if (
                    set(evidence) != {"method", "formula_id", "formula_version", "inputs", "rounding_mode", "approximate"}
                    or evidence.get("approximate") is not True
                    or evidence.get("rounding_mode") != instance.get("rounding_mode")
                    or not inputs
                    or any(
                        not isinstance(item, dict)
                        or set(item) != {"input_reference", "value_lexeme", "unit_id", "provenance_reference"}
                        for item in inputs
                    )
                ):
                    add("MASS_CALCULATION_EVIDENCE", "calculation requires versioned formula, value/unit/provenance inputs, rounding, and approximate=true")
                for item in inputs:
                    if isinstance(item, dict) and item.get("unit_id") not in REFERENCE_DATA.get("units", {}):
                        add("MASS_INPUT_UNIT", f"calculation input unit does not resolve: {item.get('unit_id')}")
            unit = REFERENCE_DATA.get("units", {}).get(instance.get("unit_id"))
            dimension = REFERENCE_DATA.get("dimensions", {}).get(unit.get("dimension_id")) if isinstance(unit, dict) else None
            if not isinstance(unit, dict) or not isinstance(dimension, dict) or dimension.get("dimension_key") != "mass":
                add("MASS_UNIT_DIMENSION", "mass unit must resolve offline to the canonical MASS dimension")
            if instance.get("reviewer") != {"role": "repository-guardian-independent"} or instance.get("reviewer") == instance.get("owner"):
                add("MASS_REVIEWER", "mass provenance requires an independent reviewer")
            effective_from = parse_time(instance.get("effective_from"))
            effective_until = parse_time(instance.get("effective_until")) if instance.get("effective_until") is not None else None
            reviewed_at = parse_time(instance.get("reviewed_at"))
            if effective_from is None or reviewed_at is None or reviewed_at < effective_from or (effective_until is not None and effective_until < effective_from):
                add("MASS_EFFECTIVE_PERIOD", "mass review/effective period is invalid")
            if instance.get("record_id") in instance.get("supersedes_record_ids", []):
                add("MASS_SUPERSESSION", "mass record cannot supersede itself")
            for field in ("conflict_references", "supersedes_record_ids"):
                for reference in instance.get(field, []):
                    if reference == instance.get("record_id"):
                        add("MASS_REFERENCE_SELF", f"{field} cannot reference the current mass record")
                    elif reference not in mass_record_ids:
                        add("MASS_REFERENCE_UNKNOWN", f"{field} must resolve to another Mass provenance record: {reference}")
        elif kind == "ELECTROSTATIC_APPEARANCE":
            if (
                instance.get("appearance_system") != "ELECTROSTATIC"
                or not instance.get("substrate_reference")
                or not instance.get("material_reference")
                or instance.get("coating_method") != "ELECTROSTATIC"
                or "color_reference" not in instance
                or "texture" not in instance
                or "sheen" not in instance
                or instance.get("stainless_finish_reference") is not None
                or instance.get("pvd_reference") is not None
                or instance.get("semantic_isolation_required") is not True
                or instance.get("technical_claim_inference_forbidden") is not True
            ):
                add("ELECTROSTATIC_BOUNDARY", "electrostatic appearance must remain separate from Finish and PVD")
            material_terms = [
                term for registry in REFERENCE_DATA.get("value_registries", {}).values()
                if isinstance(registry, dict) and registry.get("attribute_id") == "attr:dbf5365ee1e5"
                for term in registry.get("values", []) if isinstance(term, dict) and term.get("status") == "APPROVED"
            ]
            if not any(term.get("value_id") == instance.get("material_reference") for term in material_terms):
                add("ELECTROSTATIC_MATERIAL", "electrostatic material must resolve to an approved Material term")
        elif kind == "COMMERCE_ELIGIBILITY":
            model = instance.get("state_model", {})
            model_transitions = [
                (item.get("from_state"), item.get("to_state"))
                for item in model.get("legal_transitions", [])
                if isinstance(item, dict)
            ] if isinstance(model, dict) else []
            gates = instance.get("evidence_gates", [])
            if (
                instance.get("scope") != "PER_SKU_ONLY"
                or model.get("states") != COMMERCE_STATES
                or model_transitions != COMMERCE_TRANSITIONS
                or instance.get("eligibility_state") != "INQUIRY_ONLY"
                or instance.get("transition_history") != []
                or instance.get("purchase_enabled") is not False
                or instance.get("inheritance_forbidden") is not True
                or instance.get("separate_activation_authority_present") is not False
                or instance.get("activation_allowed") is not False
                or instance.get("missing_or_expired_evidence_fallback") != "INQUIRY_ONLY"
            ):
                add("COMMERCE_BOUNDARY", "C002 Commerce must expose the exact future state model while remaining INQUIRY_ONLY and inactive")
            gate_keys = [item.get("gate_key") for item in gates if isinstance(item, dict)] if isinstance(gates, list) else []
            if gate_keys != COMMERCE_GATES:
                add("COMMERCE_GATES", "all fourteen Commerce gates are required in canonical order")
            evaluated_at = parse_time(instance.get("evaluated_at"))
            for gate in gates if isinstance(gates, list) else []:
                if not isinstance(gate, dict):
                    continue
                status = gate.get("status")
                evidence_refs = gate.get("evidence_references", [])
                valid_from = parse_time(gate.get("valid_from")) if gate.get("valid_from") is not None else None
                valid_until = parse_time(gate.get("valid_until")) if gate.get("valid_until") is not None else None
                reviewed_at = parse_time(gate.get("reviewed_at")) if gate.get("reviewed_at") is not None else None
                if status == "MISSING" and any((evidence_refs, valid_from, valid_until, gate.get("reviewed_by"), reviewed_at)):
                    add("COMMERCE_GATE_EVIDENCE", f"MISSING gate must carry no evidence: {gate.get('gate_key')}")
                if status != "MISSING" and (not evidence_refs or valid_from is None or gate.get("reviewed_by") is None or reviewed_at is None):
                    add("COMMERCE_GATE_EVIDENCE", f"non-missing gate requires evidence, validity, and review: {gate.get('gate_key')}")
                if status != "MISSING" and (
                    valid_from is None or reviewed_at is None or evaluated_at is None
                    or not (valid_from <= reviewed_at <= evaluated_at)
                    or (valid_until is not None and (valid_from > valid_until or evaluated_at > valid_until))
                ):
                    add("COMMERCE_GATE_CHRONOLOGY", f"gate validity/review/evaluation chronology is invalid: {gate.get('gate_key')}")
        elif kind == "INVENTORY_HARMONY":
            ratios = instance.get("component_ratios", [])
            component_refs = [item.get("component_reference") for item in ratios if isinstance(item, dict)] if isinstance(ratios, list) else []
            if len(component_refs) != len(set(component_refs)) or not 2 <= len(component_refs) <= 16:
                add("INVENTORY_HARMONY_COMPONENTS", "Harmony requires 2..16 distinct component ratios")
            predicates = instance.get("dimension_predicates", [])
            if not isinstance(predicates, list) or not predicates or any(
                not isinstance(item, dict)
                or not set(item.get("component_references", [])).issubset(set(component_refs))
                or len(item.get("component_references", [])) < 2
                for item in predicates
            ):
                add("INVENTORY_HARMONY_PREDICATE_BINDING", "named predicates must bind only components in the arbitrary ratio set")
            if instance.get("reviewer") != {"role": "repository-guardian-independent"} or instance.get("reviewer") == instance.get("owner"):
                add("INVENTORY_HARMONY_REVIEWER", "Inventory Harmony requires a separate independent reviewer")
            if (
                instance.get("pricing_effect_allowed") is not False
                or instance.get("stock_or_availability_inference_allowed") is not False
                or instance.get("commerce_eligibility_effect_allowed") is not False
            ):
                add("INVENTORY_HARMONY_BOUNDARY", "Inventory Harmony cannot affect price, stock, availability, or Commerce Eligibility")
            effective_from = parse_time(instance.get("effective_from"))
            evaluated_at = parse_time(instance.get("evaluated_at"))
            effective_until = parse_time(instance.get("effective_until")) if instance.get("effective_until") is not None else None
            outside_effective_period = effective_from is None or evaluated_at is None or evaluated_at < effective_from or (
                effective_until is not None and evaluated_at is not None and evaluated_at > effective_until
            ) or (effective_until is not None and effective_from is not None and effective_from > effective_until)
            if effective_from is None or evaluated_at is None:
                add("INVENTORY_HARMONY_TIME", "effective/evaluation timestamps must be valid")
            evidence_entries = instance.get("evidence_entries", [])
            evidence_indeterminate = not evidence_entries or bool(instance.get("conflict_references")) or outside_effective_period
            any_fail = False
            for evidence in evidence_entries if isinstance(evidence_entries, list) else []:
                if not isinstance(evidence, dict):
                    continue
                valid_from = parse_time(evidence.get("valid_from"))
                valid_until = parse_time(evidence.get("valid_until")) if evidence.get("valid_until") is not None else None
                reviewed_at = parse_time(evidence.get("reviewed_at"))
                status = evidence.get("status")
                invalid_chronology = (
                    valid_from is None or reviewed_at is None or evaluated_at is None
                    or not (valid_from <= reviewed_at <= evaluated_at)
                    or (valid_until is not None and (valid_from > valid_until or evaluated_at > valid_until))
                )
                if invalid_chronology:
                    add("INVENTORY_HARMONY_EVIDENCE_TIME", f"evidence chronology is invalid: {evidence.get('evidence_reference')}")
                if status in {"CONFLICT", "MISSING"} or invalid_chronology:
                    evidence_indeterminate = True
                if status == "FAIL":
                    any_fail = True
            expected_outcome = "UNDETERMINED" if evidence_indeterminate else ("INELIGIBLE" if any_fail else "ELIGIBLE")
            if instance.get("outcome") != expected_outcome:
                add("INVENTORY_HARMONY_FAIL_CLOSED", f"evidence state requires outcome {expected_outcome}")
        elif kind == "DAMAVAND_CENTRAL_BOM_INTERFACE" and (
            instance.get("damavand_owns_component_truth") is not True
            or instance.get("central_may_mutate_damavand_truth") is not False
            or instance.get("central_implementation_allowed") is not False
            or instance.get("calculator_project_quote_authority") is not False
            or instance.get("interface_mode") != "VERSIONED_READ_ONLY_REFERENCE"
        ):
            add("BOM_INTERFACE_BOUNDARY", "Central may only consume versioned Damavand component references in the future")

    if not canonical:
        mass_count = instance_kinds.count("MASS_PROVENANCE")
        expected_kinds = [
            "PRODUCT_BUILDER", "CONTROLLED_VALUE_PROPOSAL", "BRAND_PROVENANCE",
            *(["MASS_PROVENANCE"] * mass_count),
            "ELECTROSTATIC_APPEARANCE", "COMMERCE_ELIGIBILITY",
            "INVENTORY_HARMONY", "DAMAVAND_CENTRAL_BOM_INTERFACE",
        ]
        if not 1 <= mass_count <= 8 or instance_kinds != expected_kinds:
            add("EXACT_SYNTHETIC_KINDS", "requires one of every non-Mass kind and 1..8 contiguous Mass records in deterministic order")
        supersession_graph = {
            item.get("record_id"): list(item.get("supersedes_record_ids", []))
            for item in instances if isinstance(item, dict) and item.get("record_kind") == "MASS_PROVENANCE"
        }
        visiting: set[Any] = set()
        visited: set[Any] = set()

        def visit_mass(node: Any) -> bool:
            if node in visiting:
                return True
            if node in visited:
                return False
            visiting.add(node)
            if any(visit_mass(child) for child in supersession_graph.get(node, []) if child in supersession_graph):
                return True
            visiting.remove(node)
            visited.add(node)
            return False

        if any(visit_mass(node) for node in supersession_graph):
            add("MASS_SUPERSESSION_CYCLE", "Mass supersession references must be acyclic")
    for node in walk(value):
        if isinstance(node, dict):
            overlap = PROHIBITED_FIELDS.intersection(node)
            if overlap:
                add("PROHIBITED_FIELD", f"prohibited field(s): {sorted(overlap)}")
    return sorted(set(issues))


def validate_file(path: Path = REGISTRY_PATH) -> list[str]:
    validator, _ = load_validator()
    return validate_package(load_yaml(path), validator, canonical=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", nargs="?", default=str(REGISTRY_PATH))
    parser.add_argument("--synthetic", action="store_true")
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        validator, _ = load_validator()
        issues = validate_package(
            load_yaml(Path(args.registry)), validator, canonical=not args.synthetic,
        )
    except (OSError, TypeError, ValueError, ValidationConfigurationError) as exc:
        print(f"C002_PRODUCT_ADMIN_CONFIGURATION: {exc}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    mode = "synthetic eight-kind fixture" if args.synthetic else "policy-only canonical registry"
    print(f"C002 Product Administration validation PASS: {mode}; no Product/SKU/Availability/runtime authority.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
