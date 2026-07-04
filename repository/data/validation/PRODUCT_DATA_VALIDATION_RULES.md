# Product Data Validation Rules

## Document Control

- **Document ID:** `repository/data/validation/PRODUCT_DATA_VALIDATION_RULES.md`
- **Status:** Review
- **Authority:** Product Data Validation Asset
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Qualified Steel-Domain Reviewer, and WooCommerce Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On required field, allowed value, slug, naming, SKU, duplicate, relationship, price, import, or approval-gate change
- **Lifecycle:** Review
- **Source of Truth:** Sprint 03A product-data contract and approved Product/WooCommerce/Attribute/Inquiry models
- **Dependencies:** [Stainless Steel Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md), [Attribute Dictionary](../attributes/ATTRIBUTE_DICTIONARY.md), and [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md)
- **Related Documents:** [Pipe Import Template](../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv), [Pipe SEO Entity Model](../seo/PIPE_SEO_ENTITY_MODEL.md), [WooCommerce Product Model](../../../docs/20_WOOCOMMERCE_PRODUCT_MODEL.md), and [Inquiry Data Model](../../../docs/23_INQUIRY_DATA_MODEL.md)
- **Traceability:** PDM-002 through PDM-007, WCM-002 through WCM-008, ATT-002 through ATT-007, INQ-002, CP-005, CP-006, and Sprint 03A
- **AI Compatibility:** AI-readable deterministic validation contract; no generated commercial data or autonomous approval
- **Approval:** Pending Founder, domain, Product Data, Sales, SEO, security, and WooCommerce review; no validator or import is executed

## Purpose

Define deterministic pre-import rules for Stainless Steel Pipe assets. Passing these rules means a dataset is structurally reviewable; it does not authorize WordPress import or publication.

## Validation Outcomes

| Outcome | Meaning |
| --- | --- |
| `PASS` | Rule satisfied with approved evidence |
| `FAIL` | Invalid value/relationship or prohibited exposure; row cannot proceed |
| `QUARANTINE` | Unknown/unmatched value requires owner/domain review and must not create a term |
| `TBD-BLOCKED` | Required commercial/governance value is intentionally unresolved; asset may remain in staging but cannot import/publish |

## Required Fields

### Parent Row

- `parent_sku`: placeholder permitted only in template; approved final parent reference required before import.
- `product_type`: exactly `variable`.
- `parent_name_fa`: non-empty normalized Persian label.
- `category`: approved canonical Product Family/taxonomy reference.
- `material`: approved controlled value.
- `unit`: exactly `meter` for Sprint 03A.
- `inquiry_only`: exactly `yes`.
- `public_price`: empty.
- `canonical_slug`: approved unique value before publication; `TBD` blocks import/publication.

### Variation Row

- `parent_sku`: must resolve to exactly one parent row.
- `variation_sku`: unique approved final SKU required before import; `TBD-*` blocks import.
- `product_type`: exactly `variation`.
- `parent_name_fa` and `variation_name_fa`: non-empty and consistent with controlled values.
- `category`, `material`, `grade`, `finish`, `diameter_mm`, `thickness_mm`, `length_m`, `unit`.
- `stock_status`: approved controlled state; `TBD` blocks import/publication.
- `inquiry_only`: exactly `yes`.
- `public_price`: empty.

Optional fields remain `TBD` when unresolved: Brand, Country, Weight per Meter, SEO Title, SEO Description, and notes beyond the required staging warning.

## Allowed Values

| Field | Allowed Sprint 03A values |
| --- | --- |
| `product_type` | `variable`, `variation` according to row role |
| `material` | `stainless-steel` working family value; final terminology approval required |
| `grade` | `201`, `304`, `316`, `430` |
| `finish` | `silver`, `gold-pvd`, `black-pvd` |
| `diameter_mm` | `16`, `19`, `22`, `25`, `32`, `38`, `42`, `51`, `63`, `76`, `102` |
| `thickness_mm` | `0.6`, `0.8`, `1`, `1.2`, `1.5`, `2` |
| `length_m` | `3`, `6` |
| `unit` | `meter` |
| `inquiry_only` | `yes` |
| `public_price` | empty only |
| `brand`, `country`, `weight_per_meter` | `TBD` until verified; blocks claim/publication where required |
| `stock_status` | `TBD` in template; later one approved domain state only |

Unlisted values fail or quarantine. They must not be normalized silently into a new canonical term.

## Slug Rules

- Attribute/internal slugs use lowercase ASCII `a-z`, digits, and single hyphens only.
- No leading/trailing hyphen, repeated hyphen, whitespace, underscore, uppercase, or diacritic.
- Public `canonical_slug` is `TBD` until URL namespace/script policy is approved.
- SKU, stable ID, external ID, Persian label, or concatenated attribute tuple is not automatically a public slug.
- Slug uniqueness is scoped to the approved namespace and must be checked against current, former, redirected, and reserved values.
- A slug change requires redirect/canonical/sitemap/internal-link/inquiry-source impact review.

## Persian Naming Rules

- Use Persian `ی` (U+06CC) and `ک` (U+06A9), not Arabic variants.
- Normalize Unicode and remove zero-width/control characters unless an approved orthographic rule requires them.
- Trim leading/trailing whitespace and collapse repeated spaces.
- Use Persian RTL-readable order and explicit units.
- Keep technical grade codes and `PVD` tokens stable; do not translate identifiers.
- Variation name values must match the structured attribute tuple exactly.
- Do not add supplier, availability, quality, standard, certification, warranty, price, or lead-time claims.

## SKU Rules

- Parent reference and variation SKU are separate identities.
- Every operational variation requires one unique stable SKU before import.
- Final syntax and segment semantics remain `TBD`; Sprint 03A does not generate final SKUs.
- Template placeholders must begin `TBD-` and must fail the production/import gate.
- SKU is case-policy-controlled ASCII, immutable after integration except through approved migration, and never reused.
- SKU must not contain Persian text, price, stock, supplier, customer, credential, mutable URL, or unapproved commercial meaning.
- Duplicate check covers current, archived, discontinued, legacy, ERP, CRM, and CentralSteel mappings where available.

## Duplicate Prevention

- Parent stable identity, parent reference, canonical slug, and WooCommerce ID must be unique in their own namespaces.
- Variation SKU must be globally unique under the approved policy.
- Variation tuple `(parent, grade, finish, diameter_mm, thickness_mm, length_m)` must be unique.
- Persian/English label duplication does not establish identity; compare normalized values and aliases.
- Imports must check existing parent/variation IDs, SKUs, slugs, taxonomy terms, attribute terms, aliases, and previous mappings.
- Duplicate rows fail; near-duplicates quarantine for review.
- No import may silently merge, overwrite, or create a suffix to bypass a collision.

## Parent/Variation Consistency

- Each variation references exactly one existing staged/approved Variable Parent Product.
- Parent declares every variation axis used by its variations.
- Variations use only parent-approved controlled values and valid combinations.
- Shared parent content is not duplicated as variation authority.
- Variation-specific data does not overwrite parent identity/canonical content.
- All child rows inherit Inquiry First and No Public Pricing.
- Parent and child categories/material/unit must not conflict.
- No orphan variation, empty parent, duplicate tuple, or mixed product family is allowed.

## No Price Exposure

- `public_price` must be empty in parent and variation rows.
- Reject `0`, `0.00`, currency symbols/codes, `free`, `TBD`, `hidden`, dashes, whitespace sentinels, or text in `public_price`.
- Reject price/discount/currency/offer data in names, descriptions, notes, slugs, SKUs, media names, metadata, attributes, or exports intended for public use.
- Import mapping must not populate regular price, sale price, price range, Offer, cart, checkout, payment, or shipping-purchase fields/actions.
- Post-import validation must inspect frontend, source, API, feed, schema, search, cache, email, analytics, and inquiry context for price leakage.
- Any price exposure is a blocking failure and rollback trigger.

## Import Safety Checks

### Before Mapping

- Verify UTF-8 encoding, exact header count/order, CSV parseability, and no embedded formula/macro behavior.
- Validate all required values, controlled sets, decimal formats, and Persian normalization.
- Resolve or explicitly block every `TBD` required for execution.
- Confirm exact WooCommerce version/capability and approved column mapping.
- Confirm approved global attributes/terms exist or use a separately approved term-creation plan.
- Produce row counts, parent/variation counts, duplicate report, invalid-combination report, and no-price report.

### Before Import

- Use staging or an approved isolated safe target; never begin on production without separate authorization.
- Create a complete backup and prove isolated restoration.
- Run a dry-run/preview with no mutation.
- Record exact source file checksum/version, reviewer, mapping, target, expected changes, and rollback point.
- Block on placeholder SKUs, `TBD` stock, unapproved canonical slugs, invalid combinations, missing owners, or unresolved errors.

### After Future Authorized Import

- Reconcile row/product/variation counts and stable IDs.
- Validate parent-child relationships, attributes, names, URLs, inquiry context, visibility, and Admin manageability.
- Run exhaustive no-price/no-transaction checks.
- Verify Persian RTL/mobile/accessibility/SEO behavior.
- Roll back on mismatch, partial import, duplicate, price exposure, invalid public state, or unavailable recovery.

## Founder Review Gates

| Gate | Required approval/evidence |
| --- | --- |
| Family and hierarchy | Founder + Product Data/domain review |
| Attribute dictionary | Founder + qualified steel-domain review |
| Valid combinations | Founder + domain + Sales/Operations evidence |
| SKU policy/final values | Founder + Operations/integration review |
| Taxonomy/category/slugs | Founder + Product Data + SEO review |
| WooCommerce mapping | Founder + WooCommerce/technical review |
| Inquiry/no-price | Founder + Sales + security + exhaustive validation |
| SEO metadata/canonical | Founder + SEO/domain review |
| Backup/rollback/import | Founder + operations/security/quality review |

No gate is satisfied by file creation alone.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03A deterministic product-data validation contract. |

## Navigation

- [Stainless Steel Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md)
- [Attribute Dictionary](../attributes/ATTRIBUTE_DICTIONARY.md)
- [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md)
- [Pipe Import Template](../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv)
- [Sprint 03A Audit](../../../docs/AUDIT_REPORT_SPRINT03A.md)
