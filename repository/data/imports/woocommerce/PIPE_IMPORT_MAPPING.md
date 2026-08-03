# Stainless Steel Pipe Import Mapping

## Document Control

- **Document ID:** `repository/data/imports/woocommerce/PIPE_IMPORT_MAPPING.md`
- **Status:** Review
- **Authority:** Product Data Import Mapping Asset
- **Owner:** Founder
- **Reviewer:** Product Data Owner and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.1
- **Last Updated:** 2026-08-03
- **Last Review:** 2026-08-03
- **Review Cycle:** On CSV contract, product mapping, target importer, validation, or execution-gate change
- **Lifecycle:** Review
- **Source of Truth:** [Pipe Import Template](PIPE_IMPORT_TEMPLATE.csv), [Pipe WooCommerce Mapping](../../products/pipes/PIPE_WOOCOMMERCE_MAPPING.md), and approved repository product-data models
- **Dependencies:** [Pipe Import Template](PIPE_IMPORT_TEMPLATE.csv), [Pipe WooCommerce Mapping](../../products/pipes/PIPE_WOOCOMMERCE_MAPPING.md), [Attribute Dictionary](../../attributes/ATTRIBUTE_DICTIONARY.md), and [Product Data Validation Rules](../../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- **Related Documents:** [Pipe Product Family](../../products/pipes/PIPE_PRODUCT_FAMILY.md), [Pipe Variation Matrix](../../products/pipes/PIPE_VARIATION_MATRIX.md), and [Pipe Import Precheck](../../validation/PIPE_IMPORT_PRECHECK.md)
- **Traceability:** CP-001 through CP-010, PDM-001 through PDM-008, WCM-001 through WCM-008, ATT-001 through ATT-007, Sprint 03A, and Sprint 03B
- **AI Compatibility:** AI-readable deterministic field mapping; no inferred values, live import, or autonomous approval
- **Approval:** Pending Founder and Product Data, domain, Sales, SEO, and WooCommerce technical review; execution prohibited

## Purpose

Define how each of the 23 staging CSV columns may be transformed into a future downstream WooCommerce import payload while preserving canonical Repository authority, Inquiry First, No Public Pricing, Variable Parent Product presentation mappings, controlled attributes, and all unresolved `TBD` gates.

The canonical source chain is `Catalog → Platform → Family → Series → Variant Rules → derived SKU`. Parent/Variation rows and IDs are downstream adapter mappings only. Their axes and tuple validity must reflect the applicable Variant Rules and cannot originate in this import contract.

## Mapping Status Vocabulary

| Status | Meaning |
| --- | --- |
| `MAP` | Has a logical destination after all row and approval gates pass |
| `TRANSFORM` | Requires deterministic normalization or lookup before mapping |
| `REFERENCE` | Resolves a relationship; it is not copied as uncontrolled text |
| `HOLD` | Must remain staged until verified/approved data exists |
| `PROHIBITED` | Must not populate a WooCommerce/public target |

No status authorizes execution. Exact target importer columns must be verified against the approved runtime before a separate import plan is approved.

## Column Mapping

| # | Staging column | Row scope | Logical WooCommerce destination | Status | Deterministic rule | Blocking condition |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `parent_sku` | Parent and variation | Downstream Parent SKU/reference; Variation-to-Parent adapter relationship | `REFERENCE` | Parent mapping carries one approved derived SKU/reference; child resolves exactly to that system-local mapping | Blank on child, `TBD-*`, duplicate, missing parent mapping, or unapproved SKU policy |
| 2 | `variation_sku` | Variation only | Derived Variation SKU | `MAP` | Blank on parent; unique approved derived value on child; not a canonical entity identity | Present on parent, blank on child, `TBD-*`, duplicate, or unapproved policy |
| 3 | `product_type` | All | Product row type | `MAP` | Exactly `variable` for parent or `variation` for child | Any other value or row-role conflict |
| 4 | `parent_name_fa` | All | Parent Persian display name/shared page reference | `MAP` | Normalized Persian; identical downstream Parent mapping context across its children | Blank, non-normalized, or conflicting child value |
| 5 | `variation_name_fa` | All | Variation Persian display label | `TRANSFORM` | `TBD`/blank on parent; on child must be generated only from approved structured values under approved naming rule | Unapproved naming rule, mismatch, commercial claim, or unresolved value |
| 6 | `category` | All | Approved downstream product-category relationship | `REFERENCE` | Resolve the approved system-local navigation term mapped from canonical Family/Series references; do not create from arbitrary row text | `TBD`, missing/duplicate term, unapproved taxonomy mapping, or mixed family |
| 7 | `material` | All | Global Material attribute | `REFERENCE` | Controlled working value `stainless-steel`; parent/shared consistency required | Terminology not approved or runtime term unresolved |
| 8 | `grade` | Variation; Parent reflection | Global Grade attribute | `REFERENCE` | One of `201`, `304`, `316`, `430`; reflect the governed axis on the Parent mapping only after resolution to Variant Rules | Parent placeholder unresolved, invalid value, missing term, or invalid combination |
| 9 | `finish` | Variation; Parent reflection | Global Finish attribute | `REFERENCE` | One of `silver`, `gold-pvd`, `black-pvd`; reflect the governed axis on the Parent mapping only after resolution to Variant Rules | Parent placeholder unresolved, invalid value, missing term, or invalid combination |
| 10 | `diameter_mm` | Variation; Parent reflection | Global Diameter attribute | `TRANSFORM` | Parse canonical decimal; unit context is mm; reflect the governed axis on the Parent mapping | Invalid value/format, missing term, or invalid combination |
| 11 | `thickness_mm` | Variation; Parent reflection | Global Thickness attribute | `TRANSFORM` | Parse canonical decimal without trailing display unit; reflect the governed axis on the Parent mapping | Invalid value/format, missing term, or invalid combination |
| 12 | `length_m` | Variation; Parent reflection | Global Length attribute | `TRANSFORM` | Parse `3` or `6`; unit context is metre; reflect the governed axis on the Parent mapping | Invalid value/format, missing term, or invalid combination |
| 13 | `unit` | All | Shared Unit reference attribute | `MAP` | Exactly `meter` and consistent across parent/children | Blank or any other value |
| 14 | `brand` | Approved row scope only | Approved Brand relationship/attribute | `HOLD` | Map only a verified controlled identity | `TBD`, unverified source, or unresolved brand authority |
| 15 | `country` | Approved row scope only | Country-of-manufacture attribute | `HOLD` | Map only verified manufacturing-origin data | `TBD`, unverified origin, or shipping-origin substitution |
| 16 | `weight_per_meter` | Variation if verified | Approved technical field/attribute | `HOLD` | Canonical decimal and approved unit only after technical evidence | `TBD`, absent field model, or unsupported calculation |
| 17 | `stock_status` | Variation/commercial | Approved stock/supply state mapping | `HOLD` | No mapping until a verified controlled state and rule exist | `TBD`; no default or inferred WooCommerce stock status allowed |
| 18 | `inquiry_only` | All | Inquiry-only behavior flag/context | `MAP` | Exactly `yes` on parent and every variation | Blank, `no`, inconsistent, or missing approved runtime capability |
| 19 | `public_price` | All | No destination | `PROHIBITED` | Must be byte-empty after trimming; do not map to any price field | Any value, including zero, `TBD`, `hidden`, currency, whitespace sentinel, or formula |
| 20 | `seo_title` | Parent page by default | Approved SEO title | `HOLD` | Map only approved factual Persian metadata for the canonical public-page/search intent; Product facts remain Repository-owned | `TBD`, duplication, keyword claim, price/availability claim, or no SEO approval |
| 21 | `seo_description` | Parent page by default | Approved SEO description | `HOLD` | Map only approved factual Persian metadata for the canonical public-page/search intent; Product facts remain Repository-owned | Same blockers as SEO title |
| 22 | `canonical_slug` | Parent page by default | Approved canonical public-page slug | `HOLD` | Resolve one approved unique lowercase ASCII public-page slug; child blank/non-canonical by default; slug is not Product identity | `TBD`, collision, reserved/legacy conflict, or missing URL/SEO approval |
| 23 | `notes` | Staging/review only | No public product field by default | `HOLD` | Retain as controlled import-review context only | Public mapping, secrets, price, stock promise, supplier claim, or uncontrolled text |

## Parent Row Contract

- Exactly one staged Parent mapping row is permitted per approved downstream Parent adapter reference.
- `product_type` must equal `variable`.
- `parent_sku` requires an approved derived mapping value; `variation_sku` must be empty.
- Parent reflects the approved variation axes resolved from Variant Rules but does not define them or use `TBD` as an attribute term.
- Shared canonical Family/Series references, downstream category mapping, Material, Unit, Persian display name, inquiry-only state, and public-page/URL ownership must be consistent.
- `public_price` must be empty.
- A Parent mapping with unresolved category/attribute mappings, canonical public-page slug, inquiry mechanism, derived SKU, canonical source references, or Variant Rules approval cannot be imported.

## Variation Row Contract

- `product_type` must equal `variation`.
- `parent_sku` must resolve to exactly one downstream Parent mapping row.
- `variation_sku` must be a unique approved derived value and is not canonical entity identity.
- Grade, Finish, Diameter, Thickness, and Length must each contain one allowed canonical value.
- The tuple `(parent_sku, grade, finish, diameter_mm, thickness_mm, length_m)` must be unique and resolve to an approved tuple in the applicable Variant Rules.
- Canonical Family/Series references, downstream category mapping, Material, Unit, inquiry-only state, and no-price behavior must not conflict with the Parent projection.
- `stock_status=TBD` remains a hard blocker and must not be converted to a WooCommerce state.

## Normalization Contract

| Data class | Required normalization |
| --- | --- |
| CSV | UTF-8, parseable, exact 23 headers in the approved order, one header row, no duplicate columns |
| Persian names | Persian `ی` and `ک`, normalized Unicode, no control characters, trimmed/collapsed whitespace, RTL-readable order |
| Internal keys/slugs | Lowercase ASCII; stable allowed tokens; no mixed Persian/English slug form |
| Decimal dimensions | Dot decimal, no grouping separator, no embedded unit, exact allowed-value comparison after canonical parsing |
| Grade | Stable ASCII technical token; no translation or numeric coercion that changes identity |
| Finish | Exact lowercase controlled token |
| Boolean policy | Exact lowercase `yes` for `inquiry_only` |
| Price | Empty only; trimming must not conceal a sentinel/value |
| Placeholder | Any required `TBD` or `TBD-*` remains unresolved and blocks execution |

Normalization must never invent a new controlled value, silently repair an unknown, choose a default, or convert commercial uncertainty into a public claim.

## Import Ordering Contract

1. Validate file structure and all row-level fields without mutation.
2. Resolve approved category/global attribute/term identities through a reviewed lookup table.
3. Validate the single downstream Parent mapping reference and its approved derived SKU/reference.
4. Validate every downstream Variation adapter reference, derived SKU, tuple, and resolution to the applicable Variant Rules.
5. Validate inquiry-only and exhaustive no-price rules.
6. Produce a non-mutating mapping preview and exception report.
7. Stop unless [Pipe Import Precheck](../../validation/PIPE_IMPORT_PRECHECK.md) is fully passed and a separate execution authorization exists.

The existence of this order does not authorize term creation, product creation, or import.

## Rejection and Quarantine Rules

- Reject malformed CSV, missing/duplicate columns, duplicate Parent adapter reference, duplicate derived SKU, duplicate tuple, orphan Variation mapping, or any non-empty public-price value.
- Quarantine unapproved controlled values, near-duplicates, unverified Persian labels, unresolved relationships, and unsupported commercial/technical claims.
- Do not auto-create missing categories, attributes, terms, brands, countries, slugs, SKUs, stock states, or valid combinations.
- Do not overwrite or merge an existing product based only on name, row order, or partial tuple.
- A partial mapping result is not execution-ready.

## Current Template Assessment

| Evidence from `PIPE_IMPORT_TEMPLATE.csv` | Current result |
| --- | --- |
| Header contract | 23 requested columns present |
| Placeholder rows | One parent and three variations |
| Public price | Empty on all four rows |
| Inquiry-only | `yes` on all four rows |
| Final parent/variation SKUs | Not present; all supplied SKU values are `TBD-*` placeholders |
| Stock status | `TBD` on all four rows |
| Canonical slug and SEO metadata | `TBD` |
| Commercial import readiness | Blocked |

The rows demonstrate shape only. They must not be treated as a commercial catalog, valid-combination approval, or import payload.

## Approval Gates

- Founder approval of identity, taxonomy, attribute, SKU, inquiry, no-price, SEO, and commercial boundaries.
- Qualified domain approval of terminology, dimensions, finishes, and valid combinations.
- Sales/Operations approval of verified commercial states.
- WooCommerce technical approval of exact importer mapping against verified runtime capabilities.
- Security/quality approval of no-price tests, staging, backup, rollback, reconciliation, and exception handling.
- Separate explicit authorization before any import execution.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03B field-level staging-to-WooCommerce mapping; no import executed. |
| 0.1.1 | 2026-08-03 | Reclassified Parent/Variation rows, IDs, axes, tuples, category and SEO fields as downstream mappings from canonical Repository and Variant Rules sources; no import or runtime authorization. |

## Navigation

- [Pipe Import Template](PIPE_IMPORT_TEMPLATE.csv)
- [Pipe WooCommerce Mapping](../../products/pipes/PIPE_WOOCOMMERCE_MAPPING.md)
- [Pipe Import Precheck](../../validation/PIPE_IMPORT_PRECHECK.md)
- [Product Data Validation Rules](../../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- [Sprint 03B Audit](../../../../docs/AUDIT_REPORT_SPRINT03B.md)
