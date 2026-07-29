#!/usr/bin/env python3
"""Validate the exact PD-02B Minimum Canonical Slice offline and fail closed."""

from __future__ import annotations

from pathlib import Path
import re
import sys
from typing import Any

import validate_product_core
from validate_product_attributes import (
    DefinitionError,
    load_definitions as load_attribute_definitions,
    load_yaml,
    validate_fixture as validate_attributes,
)
from validate_product_attribute_values import (
    load_definitions as load_value_definitions,
    validate_registry as validate_values,
)
from validate_product_attribute_profiles import (
    ScopeDefinitions,
    load_definitions as load_profile_definitions,
    validate_registry as validate_profiles,
)
from validate_product_data_localized_labels import (
    load_validator as load_label_validator,
    validate_registry as validate_labels,
)
from validate_product_data_approval_evidence import (
    load_validator as load_approval_validator,
    validate_registry as validate_approval,
)


ROOT = Path(__file__).resolve().parents[3]
PATHS = {
    "entities": ROOT / "repository/data/registries/product-entities.yaml",
    "attributes": ROOT / "repository/data/registries/product-attributes.yaml",
    "values": ROOT / "repository/data/registries/product-attribute-value-registries.yaml",
    "profiles": ROOT / "repository/data/registries/product-attribute-profiles.yaml",
    "labels": ROOT / "repository/data/registries/product-data-localized-labels.yaml",
    "approval": ROOT / "repository/data/registries/product-data-approval-evidence.yaml",
}
CONTRACTS = {
    "core": ROOT / "repository/data/contracts/product-core.contract.yaml",
    "attributes": ROOT / "repository/data/contracts/product-attribute.contract.yaml",
    "values": ROOT / "repository/data/contracts/product-attribute-value-registry.contract.yaml",
    "profiles": ROOT / "repository/data/contracts/product-attribute-profile.contract.yaml",
    "labels": ROOT / "repository/data/contracts/product-data-localized-labels.contract.yaml",
    "approval": ROOT / "repository/data/contracts/product-data-approval-evidence.contract.yaml",
}
EXPECTED_ENTITY_LABELS = {
    "CATALOG": ("prd:catalog:a3868f6227bb", "Damavand Steel Product Catalog"),
    "PLATFORM": ("prd:platform:603354ec2045", "Stainless Steel Products"),
    "FAMILY": ("prd:family:a10c6d8ceabc", "Stainless Steel Pipe"),
}
EXPECTED_ATTRIBUTES = {
    "material": ("attr:dbf5365ee1e5", "Material", "vreg:302188e2fc8a"),
    "grade": ("attr:28565665c910", "Steel Grade", "vreg:e1b9dd333df8"),
}
EXPECTED_TERMS = {
    "stainless_steel": ("vterm:5ff9c0ceca39", "Stainless Steel"),
    "201": ("vterm:a891bfdfdd6b", "201"),
    "304": ("vterm:9c1a18d4b69b", "304"),
    "316": ("vterm:c62157b97d36", "316"),
}
EXPECTED_LOCALIZED = {
    ("prd:catalog:a3868f6227bb", "fa-IR"): "کاتالوگ محصولات دماوند استیل",
    ("prd:catalog:a3868f6227bb", "en"): "Damavand Steel Product Catalog",
    ("prd:platform:603354ec2045", "fa-IR"): "محصولات فولاد زنگ‌نزن (استنلس استیل)",
    ("prd:platform:603354ec2045", "en"): "Stainless Steel Products",
    ("prd:family:a10c6d8ceabc", "fa-IR"): "لوله استیل",
    ("prd:family:a10c6d8ceabc", "en"): "Stainless Steel Pipe",
    ("attr:dbf5365ee1e5", "fa-IR"): "جنس",
    ("attr:dbf5365ee1e5", "en"): "Material",
    ("attr:28565665c910", "fa-IR"): "گرید فولاد",
    ("attr:28565665c910", "en"): "Steel Grade",
    ("vterm:5ff9c0ceca39", "fa-IR"): "فولاد زنگ‌نزن",
    ("vterm:5ff9c0ceca39", "en"): "Stainless Steel",
    ("vterm:a891bfdfdd6b", "fa-IR"): "201",
    ("vterm:a891bfdfdd6b", "en"): "201",
    ("vterm:9c1a18d4b69b", "fa-IR"): "304",
    ("vterm:9c1a18d4b69b", "en"): "304",
    ("vterm:c62157b97d36", "fa-IR"): "316",
    ("vterm:c62157b97d36", "en"): "316",
}
HEX_SUFFIX = re.compile(r":([0-9a-f]{12})$")


def main() -> int:
    issues: list[str] = []

    def add(code: str, message: str) -> None:
        issues.append(f"[{code}] {message}")

    try:
        datasets = {
            name: load_yaml(path, f"PD-02B {name}")[0]
            for name, path in PATHS.items()
        }
        contracts = {
            name: load_yaml(path, f"PD-02B {name} contract")[0]
            for name, path in CONTRACTS.items()
        }
    except (DefinitionError, OSError) as exc:
        print(f"PD02B_CONFIGURATION: {exc}", file=sys.stderr)
        return 2

    lifecycle_states = {}
    for name, contract in contracts.items():
        section_name = "pd02b_extension" if name == "attributes" else "pd02b_lifecycle"
        if not isinstance(contract, dict) or not isinstance(contract.get(section_name), dict):
            add("LIFECYCLE_MISSING", f"{name} lacks {section_name}")
            continue
        lifecycle_states[name] = contract[section_name].get("current_status")
    if set(lifecycle_states.values()) != {next(iter(lifecycle_states.values()), None)}:
        add("LIFECYCLE_DIVERGENCE", f"contract lifecycle states differ: {lifecycle_states}")
    lifecycle = lifecycle_states.get("core")
    expected_record_status = (
        "APPROVED" if lifecycle == "APPROVED" else "CANDIDATE_UNVERIFIED"
    )

    try:
        core_definitions = validate_product_core.load_definitions()
        for issue in validate_product_core.validate_dataset(
            datasets["entities"], str(PATHS["entities"]), core_definitions
        ):
            add(f"PRODUCT_CORE_{issue.code}", issue.render())
        attribute_definitions = load_attribute_definitions()
        attribute_entries = (
            datasets["attributes"].get("attributes")
            if isinstance(datasets["attributes"], dict)
            else None
        )
        for issue in validate_attributes(
            attribute_entries, str(PATHS["attributes"]), attribute_definitions
        ):
            add(f"PRODUCT_ATTRIBUTE_{issue.code}", issue.render())
        value_definitions = load_value_definitions()
        for issue in validate_values(
            datasets["values"],
            str(PATHS["values"]),
            value_definitions,
            canonical=True,
        ):
            add(f"VALUE_REGISTRY_{issue.code}", issue.render())
        profile_definitions = load_profile_definitions()
        attributes_by_id = {
            item["attribute_id"]: item
            for item in attribute_entries
            if isinstance(item, dict) and isinstance(item.get("attribute_id"), str)
        } if isinstance(attribute_entries, list) else {}
        value_entries = (
            datasets["values"].get("value_registries", [])
            if isinstance(datasets["values"], dict)
            else []
        )
        values_by_id = {
            item["value_registry_id"]: item
            for item in value_entries
            if isinstance(item, dict) and isinstance(item.get("value_registry_id"), str)
        }
        scopes = {
            item["entity_id"]: item["entity_type"]
            for item in datasets["entities"]
            if isinstance(item, dict)
            and isinstance(item.get("entity_id"), str)
            and item.get("entity_type") in {"FAMILY", "SERIES"}
        } if isinstance(datasets["entities"], list) else {}
        for issue in validate_profiles(
            datasets["profiles"],
            str(PATHS["profiles"]),
            profile_definitions,
            canonical=True,
            attributes=attributes_by_id,
            value_registries=values_by_id,
            scope_entities=ScopeDefinitions(scopes, True),
        ):
            add(f"PROFILE_{issue.code}", issue.render())
        label_validator, label_lifecycle = load_label_validator()
        issues.extend(
            validate_labels(
                datasets["labels"],
                str(PATHS["labels"]),
                label_validator,
                label_lifecycle,
                canonical=True,
            )
        )
        approval_validator, approval_lifecycle = load_approval_validator()
        issues.extend(
            validate_approval(
                datasets["approval"],
                str(PATHS["approval"]),
                approval_validator,
                approval_lifecycle,
                canonical=True,
            )
        )
    except (
        DefinitionError,
        validate_product_core.DefinitionError,
        OSError,
        TypeError,
        ValueError,
    ) as exc:
        add("VALIDATOR_CONFIGURATION", str(exc))

    entities = datasets.get("entities")
    if not isinstance(entities, list) or len(entities) != 3:
        add("EXACT_ENTITY_COUNT", "exactly 3 Product Entity records are required")
        entities = []
    entity_by_type = {
        item.get("entity_type"): item for item in entities if isinstance(item, dict)
    }
    if set(entity_by_type) != set(EXPECTED_ENTITY_LABELS):
        add("ENTITY_TYPES", "only CATALOG, PLATFORM and FAMILY are allowed")
    for entity_type, (entity_id, label) in EXPECTED_ENTITY_LABELS.items():
        record = entity_by_type.get(entity_type, {})
        if record.get("entity_id") != entity_id or record.get("canonical_label") != label:
            add("ENTITY_IDENTITY", f"{entity_type} identity/label differs")
        if record.get("status") != expected_record_status:
            add("ENTITY_STATUS", f"{entity_type} status differs from lifecycle")
    if (
        entity_by_type.get("PLATFORM", {}).get("parent_entity_id")
        != EXPECTED_ENTITY_LABELS["CATALOG"][0]
        or entity_by_type.get("FAMILY", {}).get("parent_entity_id")
        != EXPECTED_ENTITY_LABELS["PLATFORM"][0]
    ):
        add("ENTITY_HIERARCHY", "exact Catalog -> Platform -> Family chain is required")

    attributes = (
        datasets.get("attributes", {}).get("attributes", [])
        if isinstance(datasets.get("attributes"), dict)
        else []
    )
    if len(attributes) != 2:
        add("EXACT_ATTRIBUTE_COUNT", "exactly 2 Attributes are required")
    by_key = {
        item.get("attribute_key"): item for item in attributes if isinstance(item, dict)
    }
    if set(by_key) != set(EXPECTED_ATTRIBUTES):
        add("ATTRIBUTE_KEYS", "only material and grade are allowed")
    for key, (attribute_id, label, registry_id) in EXPECTED_ATTRIBUTES.items():
        record = by_key.get(key, {})
        if (
            record.get("attribute_id") != attribute_id
            or record.get("canonical_label") != label
            or record.get("data_type") != "CONTROLLED_TERM"
            or record.get("validation", {}).get("constraints", {}).get(
                "value_registry_reference"
            )
            != registry_id
        ):
            add("ATTRIBUTE_IDENTITY", f"{key} definition differs")
        if record.get("status") != expected_record_status:
            add("ATTRIBUTE_STATUS", f"{key} status differs from lifecycle")

    value_registries = (
        datasets.get("values", {}).get("value_registries", [])
        if isinstance(datasets.get("values"), dict)
        else []
    )
    if len(value_registries) != 2:
        add("EXACT_VALUE_REGISTRY_COUNT", "exactly 2 Value Registries are required")
    terms: dict[str, dict[str, Any]] = {}
    for registry in value_registries:
        if not isinstance(registry, dict):
            continue
        if registry.get("status") != expected_record_status:
            add("VALUE_REGISTRY_STATUS", f"{registry.get('registry_key')} status differs")
        for term in registry.get("values", []):
            if isinstance(term, dict):
                terms[str(term.get("value_code"))] = term
                if term.get("status") != expected_record_status:
                    add("TERM_STATUS", f"{term.get('value_code')} status differs")
    if set(terms) != set(EXPECTED_TERMS):
        add("EXACT_TERMS", "only stainless_steel, 201, 304 and 316 are allowed")
    for code, (value_id, label) in EXPECTED_TERMS.items():
        term = terms.get(code, {})
        if term.get("value_id") != value_id or term.get("canonical_label") != label:
            add("TERM_IDENTITY", f"controlled term differs: {code}")
    if terms.get("stainless_steel", {}).get("aliases") != ["استیل"]:
        add("MATERIAL_ALIAS", "استیل must be the sole Material alias")
    if any(terms.get(code, {}).get("aliases") != [] for code in ("201", "304", "316")):
        add("GRADE_ALIASES", "Grade identifiers cannot have aliases in PD-02B")

    profiles = (
        datasets.get("profiles", {}).get("profiles", [])
        if isinstance(datasets.get("profiles"), dict)
        else []
    )
    if len(profiles) != 1:
        add("EXACT_PROFILE_COUNT", "exactly 1 INTERNAL Family profile is required")
    else:
        profile = profiles[0]
        if (
            profile.get("profile_id") != "pprof:26a474c2e100"
            or profile.get("scope_entity_id") != EXPECTED_ENTITY_LABELS["FAMILY"][0]
            or profile.get("scope_entity_type") != "FAMILY"
            or profile.get("status") != expected_record_status
        ):
            add("PROFILE_IDENTITY", "Family profile identity/status differs")
        rules = profile.get("attribute_rules", [])
        if {rule.get("attribute_id") for rule in rules if isinstance(rule, dict)} != {
            item[0] for item in EXPECTED_ATTRIBUTES.values()
        }:
            add("PROFILE_ATTRIBUTES", "profile must contain only Material and Grade")
        for rule in rules:
            if not isinstance(rule, dict) or any(
                (
                    rule.get("requirement_level") != "REQUIRED",
                    rule.get("public_visibility") != "INTERNAL",
                    rule.get("variation_axis") is not False,
                    rule.get("filtering") is not False,
                    rule.get("inquiry_use") != "NOT_USED",
                    rule.get("seo_use") != "PROHIBITED",
                    rule.get("value_source") != "CONTROLLED_REGISTRY",
                    rule.get("allowed_unit_ids") != [],
                    rule.get("precision") is not None,
                )
            ):
                add("PROFILE_BOUNDARY", "profile rule exceeds INTERNAL-only authority")

    labels = (
        datasets.get("labels", {}).get("labels", [])
        if isinstance(datasets.get("labels"), dict)
        else []
    )
    actual_localized = {
        (record.get("subject_id"), record.get("locale")): record.get("label")
        for record in labels
        if isinstance(record, dict)
    }
    if actual_localized != EXPECTED_LOCALIZED:
        add("EXACT_LOCALIZED_LABELS", "the exact 18 approved localized labels differ")

    all_ids: list[str] = []
    all_ids.extend(record.get("entity_id") for record in entities if isinstance(record, dict))
    all_ids.extend(record.get("attribute_id") for record in attributes if isinstance(record, dict))
    all_ids.extend(
        registry.get("value_registry_id")
        for registry in value_registries
        if isinstance(registry, dict)
    )
    all_ids.extend(term.get("value_id") for term in terms.values())
    all_ids.extend(record.get("profile_id") for record in profiles if isinstance(record, dict))
    all_ids.extend(record.get("label_id") for record in labels if isinstance(record, dict))
    evidence = (
        datasets.get("approval", {}).get("evidence", [])
        if isinstance(datasets.get("approval"), dict)
        else []
    )
    all_ids.extend(
        record.get("approval_evidence_id")
        for record in evidence
        if isinstance(record, dict)
    )
    suffixes = [
        match.group(1)
        for item in all_ids
        if isinstance(item, str) and (match := HEX_SUFFIX.search(item))
    ]
    if len(all_ids) != 31 or len(suffixes) != 31 or len(set(suffixes)) != 31:
        add("STABLE_ID_COLLISION", "31 unique CSPRNG-style 12-hex identifiers are required")

    if issues:
        print(f"PD-02B canonical slice validation FAILED: {len(issues)} issue(s)", file=sys.stderr)
        for issue in sorted(issues):
            print(issue, file=sys.stderr)
        return 1
    print(
        "PD-02B canonical slice validation PASS: "
        "3 entities, 2 attributes, 2 value registries, 4 terms, "
        "1 INTERNAL profile, 18 labels, 1 approval evidence; "
        f"lifecycle={lifecycle}; network, runtime, side effects=false."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
