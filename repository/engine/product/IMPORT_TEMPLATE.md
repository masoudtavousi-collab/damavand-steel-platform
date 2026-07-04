# Product Import Template

## Document Control

- **Document ID:** `repository/engine/product/IMPORT_TEMPLATE.md`
- **Status:** Review
- **Authority:** Product Engine Template
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Quality Reviewer, Security Reviewer, Operations Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On source schema, mapping, validation, target capability, recovery, reconciliation, or template change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Engine](PRODUCT_ENGINE.md), generated family/attribute/variation contracts, and approved WooCommerce Product Model
- **Dependencies:** [Product Family Template](PRODUCT_FAMILY_TEMPLATE.md), [Attribute Template](ATTRIBUTE_TEMPLATE.md), [Variation Template](VARIATION_TEMPLATE.md), and [Engine Rules](ENGINE_RULES.md)
- **Related Documents:** [Validation Template](VALIDATION_TEMPLATE.md), [Engine Workflow](ENGINE_WORKFLOW.md), and [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
- **Traceability:** PDM-001 through PDM-008, WCM-001 through WCM-008, ATT-001 through ATT-007, INQ-001 through INQ-008, Sprint 03D
- **AI Compatibility:** AI-readable reusable import-contract template; no import execution, value inference, or autonomous mapping approval
- **Approval:** Pending Founder review; no CSV, importer, runtime, or mutation is authorized

## Purpose

Generate a family-specific, deterministic import contract and staging schema without creating product rows, commercial data, or a live WooCommerce import.

## Template Identity

| Field | Required generated value |
| --- | --- |
| Engine template ID | `IMPORT_TEMPLATE` |
| Engine template version | `0.1.0` |
| Generated asset name | `{{FAMILY_KEY}}_IMPORT_MODEL.md` |
| Optional future staging file | `{{FAMILY_KEY}}_IMPORT_TEMPLATE.csv` only after schema approval |
| Generated asset location | `repository/data/imports/woocommerce/` |

## Core Staging Contract

Every generated schema defines these logical concerns without assuming exact runtime importer headers:

| Concern | Required mapping rule |
| --- | --- |
| Family identity | Approved stable family reference |
| Parent identity | Approved stable parent reference and later-approved final parent SKU |
| Variation identity | Approved stable variation reference and later-approved final variation SKU |
| Row role | Parent/variation role consistent with Variable Parent Product |
| Persian names | Normalized approved family/parent/variation labels |
| Category | Resolve one approved canonical family category; never auto-create |
| Attributes | One column/reference per generated family attribute contract |
| Variation tuple | One approved value per required variation axis |
| Inquiry-only control | Exact required affirmative value |
| Public-price control | Empty-only validation; no price destination |
| SEO projection | Parent-owned approved metadata/slug only after SEO approval |
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
2. Resolve approved category/global attribute/term identities.
3. Validate parent identity and parent declaration of axes.
4. Validate variations, tuples, identities, and approved combinations.
5. Validate inquiry-only/no-price constraints.
6. Produce a non-mutating mapping preview and exception report.
7. Stop until the generated Validation asset and separate runtime authorization pass.

Ordering is a dependency contract, not import execution.

## Import Safety Gates

- Verified target versions/capabilities and approved exact runtime mapping.
- No auto-created category, attribute, term, slug, ID, SKU, or commercial state.
- Stable collision checks against current, archived, legacy, and integrated identities.
- Isolated staging, least-privilege operator, backup/restore proof, dry-run preview, expected counts, reconciliation, rollback triggers, and post-checks.
- Exhaustive no-public-price and no-transaction validation.
- Separate Founder authorization for dry run/import/release.

## Rejection Rules

Reject malformed schema, missing/duplicate columns, unknown values, mixed units, duplicate identities/tuples, orphan variations, unapproved combinations, populated price control, `TBD` execution fields, unsupported claims, public internal data, missing target evidence, or unavailable recovery.

## Output Contract

The generated Import Model must contain:

- Schema/version and source ownership.
- Complete column mapping.
- Parent/variation row contracts.
- Normalization and allowed-value references.
- Rejection/quarantine rules.
- Preview/reconciliation expectations.
- Runtime-dependent unknowns and Founder gates.
- Explicit `NO-GO` until every hard gate passes.

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Variation Template](VARIATION_TEMPLATE.md)
- [Validation Template](VALIDATION_TEMPLATE.md)
- [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
