# Stainless Steel Pipe Variation Matrix

## Document Control

- **Document ID:** `repository/data/products/pipes/PIPE_VARIATION_MATRIX.md`
- **Status:** Review
- **Authority:** Product Data Asset
- **Owner:** Founder
- **Reviewer:** Product Data Owner and Qualified Steel-Domain Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On controlled value, variation axis, valid combination, commercial availability, unit, label, or import change
- **Lifecycle:** Review
- **Source of Truth:** Sprint 03A supplied Grade/Finish/Dimension values and [Attribute Dictionary](../../attributes/ATTRIBUTE_DICTIONARY.md)
- **Dependencies:** [Stainless Steel Pipe Product Family](PIPE_PRODUCT_FAMILY.md), [Attribute Dictionary](../../attributes/ATTRIBUTE_DICTIONARY.md), and [WooCommerce Product Model](../../../../docs/20_WOOCOMMERCE_PRODUCT_MODEL.md)
- **Related Documents:** [Product Data Validation Rules](../../validation/PRODUCT_DATA_VALIDATION_RULES.md), [Pipe Import Template](../../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv), [Pipe SEO Entity Model](../../seo/PIPE_SEO_ENTITY_MODEL.md), and [Inquiry Data Model](../../../../docs/23_INQUIRY_DATA_MODEL.md)
- **Traceability:** WP-FC-004, PDM-001 through PDM-004, WCM-001 through WCM-005, ATT-002 through ATT-007, and Sprint 03A
- **AI Compatibility:** AI-readable candidate matrix; does not infer commercially valid combinations, prices, stock, or final SKUs
- **Approval:** Pending Founder, steel-domain, Product Data, Sales, and WooCommerce review; not authorized for expansion/import

## Purpose

Define finite candidate value sets and combination controls for future Stainless Steel Pipe variations without generating unverified commercial products.

## Normalization Decision

Sprint 03A labels `201`, `304`, `316`, and `430` as Materials. To preserve the existing Product Data Model distinction between Material and technical designation, this asset stores:

- Material: `stainless-steel` as family context.
- Grade: `201`, `304`, `316`, `430` as the variation axis.

This working normalization requires Founder and qualified steel-domain approval before import. It does not redefine repository business rules.

## Controlled Axis Values

### Grade — Source Label: Materials

| Order | Stored value | Persian display | Commercial availability |
| --- | --- | --- | --- |
| 1 | `201` | گرید ۲۰۱ | `TBD` |
| 2 | `304` | گرید ۳۰۴ | `TBD` |
| 3 | `316` | گرید ۳۱۶ | `TBD` |
| 4 | `430` | گرید ۴۳۰ | `TBD` |

### Finish

| Order | Stored value | English display | Persian display | Commercial availability |
| --- | --- | --- | --- | --- |
| 1 | `silver` | Silver | نقره‌ای | `TBD` |
| 2 | `gold-pvd` | Gold PVD | طلایی PVD | `TBD` |
| 3 | `black-pvd` | Black PVD | مشکی PVD | `TBD` |

### Diameter

| Unit | Allowed numeric values | Commercial availability |
| --- | --- | --- |
| mm | `16`, `19`, `22`, `25`, `32`, `38`, `42`, `51`, `63`, `76`, `102` | `TBD` for every combination |

### Thickness

| Unit | Allowed numeric values | Commercial availability |
| --- | --- | --- |
| mm | `0.6`, `0.8`, `1`, `1.2`, `1.5`, `2` | `TBD` for every combination |

### Length

| Unit | Allowed numeric values | Commercial availability |
| --- | --- | --- |
| m | `3`, `6` | `TBD` for every combination |

## Fixed Rules

| Rule | Value |
| --- | --- |
| Unit | `meter` |
| Pricing visibility | Hidden; all public price fields empty |
| Inquiry required | `yes` |
| Commercial availability | `TBD` unless separately verified and approved |
| Parent product type | `variable` |
| Child product type | `variation` |
| Canonical owner | Variable Parent Product |
| Variation canonical/indexation | Not independently canonical/indexable by default |

## Candidate-Space Calculation

The supplied sets produce a theoretical Cartesian candidate space:

```text
4 grades × 3 finishes × 11 diameters × 6 thicknesses × 2 lengths = 1,584 candidate tuples
```

This calculation is a validation warning, not a product count or authorization. No assumption is made that all 1,584 combinations are technically valid, supplied, stocked, useful, or manageable.

## Valid-Combination Rules

- A future approved-combination table is required before import.
- Every tuple must use exactly one value from each variation axis.
- Duplicate tuples under the same parent are rejected.
- Technically invalid, commercially unverified, unsupported, or incomplete tuples are rejected or held in staging.
- `TBD` commercial availability blocks publication and import as an available product.
- Brand, Country, supplier, weight per meter, Quality Level, stock quantity, lead time, and price are never derived from the tuple.
- Grade/Finish/Dimension changes create a different variation identity; they do not silently overwrite an existing variation.
- A valid tuple still requires a stable internal ID, approved unique variation SKU, lifecycle approval, and inquiry eligibility.

## Variation Display Pattern

Working Persian RTL pattern:

```text
لوله استیل | گرید {grade} | {finish_fa} | قطر {diameter} میلی‌متر | ضخامت {thickness} میلی‌متر | طول {length} متر
```

Working English Admin/reference pattern:

```text
Stainless Steel Pipe | Grade {grade} | {finish_en} | Ø {diameter} mm | {thickness} mm | {length} m
```

These are display patterns, not SKU formulas or canonical slugs.

## Sample Candidate Tuples

Samples validate structure only and do not represent available products.

| Sample | Material | Grade | Finish | Diameter mm | Thickness mm | Length m | Unit | Availability | Inquiry | Public price |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SAMPLE-001` | stainless-steel | 304 | silver | 16 | 0.6 | 3 | meter | `TBD` | yes | empty |
| `SAMPLE-002` | stainless-steel | 316 | gold-pvd | 25 | 1.2 | 6 | meter | `TBD` | yes | empty |
| `SAMPLE-003` | stainless-steel | 430 | black-pvd | 51 | 2 | 6 | meter | `TBD` | yes | empty |

Sample identifiers are not SKUs, product IDs, or commercial records.

## Review Gates

- Qualified steel-domain validation of every axis/value and valid combination.
- Founder approval of Material/Grade normalization.
- Sales/Operations approval of commercial availability sources and states.
- Product Data approval of stable IDs, duplicate rules, and SKU policy.
- WooCommerce approval of attribute/term mappings and variation limits.
- UX approval of mobile Persian RTL selection behavior.
- SEO approval of parent canonical and non-indexable variation state.
- Backup, dry-run, error report, and rollback evidence before import.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03A candidate variation matrix; commercial validity remains TBD. |

## Navigation

- [Stainless Steel Pipe Product Family](PIPE_PRODUCT_FAMILY.md)
- [Attribute Dictionary](../../attributes/ATTRIBUTE_DICTIONARY.md)
- [Pipe Import Template](../../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv)
- [Product Data Validation Rules](../../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- [Sprint 03A Audit](../../../../docs/AUDIT_REPORT_SPRINT03A.md)
