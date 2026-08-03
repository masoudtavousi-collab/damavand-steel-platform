# Product Import Template

## Document Control

- **Document ID:** `repository/engine/product/IMPORT_TEMPLATE.md`
- **Status:** Review
- **Authority:** Product Engine Template
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Quality Reviewer, Security Reviewer, Operations Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 1.0.0
- **Last Updated:** 2026-08-03
- **Last Review:** 2026-08-03
- **Review Cycle:** On source schema, mapping, validation, target capability, recovery, reconciliation, or template change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Engine](PRODUCT_ENGINE.md), approved canonical Family/Series/Variant Rules sources, and generated Family/Attribute/Variation references; the WooCommerce Product Model constrains downstream target mapping only
- **Dependencies:** [Product Family Template](PRODUCT_FAMILY_TEMPLATE.md), [Attribute Template](ATTRIBUTE_TEMPLATE.md), [Variation Template](VARIATION_TEMPLATE.md), and [Engine Rules](ENGINE_RULES.md)
- **Related Documents:** [Validation Template](VALIDATION_TEMPLATE.md), [Engine Workflow](ENGINE_WORKFLOW.md), and [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
- **Traceability:** PDM-001 through PDM-008, WCM-001 through WCM-008, ATT-001 through ATT-007, INQ-001 through INQ-008, Sprint 03D
- **AI Compatibility:** AI-readable reusable import-contract template; no import execution, value inference, or autonomous mapping approval
- **Approval:** Pending Founder review; no CSV, importer, runtime, or mutation is authorized

## Purpose

Generate a Family-specific, deterministic downstream import contract from approved `Catalog → Platform → Family → Series → Variant Rules → derived SKU` sources without creating product rows, commercial data, or a live WooCommerce import.

## Template Identity

| Field | Required generated value |
| --- | --- |
| Engine template ID | `IMPORT_TEMPLATE` |
| Engine template version | `1.0.0` |
| Required generated provenance | `PRODUCT_ENGINE@1.0.0` and `IMPORT_TEMPLATE@1.0.0` |
| Generated asset name | `{{FAMILY_KEY}}_IMPORT_MODEL.md` |
| Optional future staging file | `{{FAMILY_KEY}}_IMPORT_TEMPLATE.csv` only after schema approval |
| Generated asset location | `repository/data/imports/woocommerce/` |

## Core Staging Contract

Every generated schema defines these logical concerns without assuming exact runtime importer headers:

| Concern | Required mapping rule |
| --- | --- |
| Canonical repository source | Approved Catalog/Platform/Family/Series/Variant Rule Set references |
| Downstream Parent mapping | Adapter-only Parent reference; never canonical identity |
| Downstream Variation mapping | Adapter-only Variation reference mapped to one governed tuple |
| Derived SKU | Later-approved derived Parent/Variation SKU where applicable; never canonical entity identity |
| Row role | Downstream Parent/Variation role consistent with an approved commerce mapping |
| Persian names | Normalized approved family/parent/variation labels |
| Category | Resolve one approved downstream navigation/category mapping; never auto-create or redefine hierarchy |
| Attributes | One downstream column/reference per generated Family/Series attribute contract |
| Variation tuple | Resolve allowed values and one evidence-backed valid tuple from the referenced Variant Rules |
| Inquiry-only control | Exact required affirmative value |
| Public-price control | Empty-only validation; no price destination |
| SEO projection | Downstream public page/URL/search-intent metadata only after SEO approval; no identity transfer |
| Internal review | Protected notes/errors; never public product content |

Family-specific columns are generated from the approved Attribute Template output. Another family's columns cannot be copied as defaults.

## Column Mapping Template

| # | Source column | Family field ID | Row scope | Primary classification | Logical destination | Status | Transformation | Blocker |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{ORDER}}` | `{{COLUMN_KEY}}` | `{{FIELD_ID}}` | Parent/Variation/Both | `{{CLASS}}` | `{{DESTINATION_OR_NONE}}` | MAP/TRANSFORM/REFERENCE/HOLD/PROHIBITED | `{{RULE}}` | `{{FAIL_CONDITION}}` |

Every source column must map exactly once. `PROHIBITED` is required for any public-price field/control; it has no WooCommerce price target.

## Required Mapping Statuses

- `MAP`: deterministic destination after all gates.
- `TRANSFORM`: deterministic normalized output; no inference.
- `REFERENCE`: resolves approved stable identity/relationship.
- `HOLD`: remains staged until evidence/approval exists.
- `PROHIBITED`: no destination and any populated value fails.

## Schema Rules

- UTF-8, one header row, unique stable ASCII column names, consistent row width.
- Exact schema/version/checksum recorded before any future dry run.
- Persian text normalized without altering technical tokens.
- Typed decimals, units, enums, relationships, and null/TBD rules follow family contracts.
- Formula-leading cells, macros, executable content, secrets, personal data, and uncontrolled markup are rejected.
- `TBD`, placeholder IDs, and placeholder SKUs block execution where final values are required.
- No stock, supplier, price, availability, or technical claim is created to satisfy schema completeness.

## Parent and Variation Ordering

1. Validate schema and rows without mutation.
2. Resolve canonical Family/Series/Variant Rules and approved attribute/term source references.
3. Validate downstream Parent/Variation adapter references without treating them as canonical identities.
4. Validate that every projected allowed value, axis, and tuple resolves to the referenced Variant Rules.
5. Validate inquiry-only/no-price constraints.
6. Produce a non-mutating mapping preview and exception report.
7. Stop until the generated Validation asset and separate runtime authorization pass.

Ordering is a dependency contract, not import execution.

## Import Safety Gates

- Verified target versions/capabilities and approved exact runtime mapping.
- No auto-created category, attribute, term, slug, ID, SKU, or commercial state.
- Stable collision checks across canonical source references and separate downstream adapter-ID/SKU namespaces.
- Isolated staging, least-privilege operator, backup/restore proof, dry-run preview, expected counts, reconciliation, rollback triggers, and post-checks.
- Exhaustive no-public-price and no-transaction validation.
- Separate Founder authorization for dry run/import/release.

## Rejection Rules

Reject malformed schema, missing/duplicate columns, unknown values, mixed units, duplicate identities/tuples, orphan variations, unapproved combinations, populated price control, `TBD` execution fields, unsupported claims, public internal data, missing target evidence, or unavailable recovery.

## Output Contract

The generated Import Model must contain:

- Schema/version and source ownership.
- Complete column mapping.
- Canonical source references and downstream Parent/Variation row mappings.
- Normalization and allowed-value references.
- Rejection/quarantine rules.
- Preview/reconciliation expectations.
- Runtime-dependent unknowns and Founder gates.
- Explicit `NO-GO` until every hard gate passes.

## Compatibility and Provenance

Version `1.0.0` is a major required-structure and semantic change. Its compatibility impact is breaking for every Family with a generated 0.x Import asset. Before use, a separately authorized migration or regeneration task must record the affected-Family/asset inventory, exact engine/template provenance, migration and validation plan, diff review, full validation, and Founder approval. No CSV, runtime ID, SKU, tuple, or import action is created by this change.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03D Import template; no import authorized. |
| 1.0.0 | 2026-08-03 | Major canonical-source reconciliation: separated repository source references from adapter IDs and required all projected allowed values, axes, and valid tuples to resolve from Variant Rules. |

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Variation Template](VARIATION_TEMPLATE.md)
- [Validation Template](VALIDATION_TEMPLATE.md)
- [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
