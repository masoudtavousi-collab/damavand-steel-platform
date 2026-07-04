# Stainless Steel Pipe WooCommerce Mapping

## Document Control

- **Document ID:** `repository/data/products/pipes/PIPE_WOOCOMMERCE_MAPPING.md`
- **Status:** Review
- **Authority:** Product Data Mapping Asset
- **Owner:** Founder
- **Reviewer:** Product Data Owner and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On pipe product model, attribute contract, import mapping, inquiry behavior, or target WooCommerce capability change
- **Lifecycle:** Review
- **Source of Truth:** Approved repository product and WooCommerce models plus the Sprint 03A Stainless Steel Pipe data contract
- **Dependencies:** [Pipe Product Family](PIPE_PRODUCT_FAMILY.md), [Pipe Variation Matrix](PIPE_VARIATION_MATRIX.md), [Attribute Dictionary](../../attributes/ATTRIBUTE_DICTIONARY.md), [WooCommerce Product Model](../../../../docs/20_WOOCOMMERCE_PRODUCT_MODEL.md), and [WooCommerce Configuration Blueprint](../../../../docs/38_WOOCOMMERCE_CONFIGURATION.md)
- **Related Documents:** [Pipe Import Mapping](../../imports/woocommerce/PIPE_IMPORT_MAPPING.md), [Pipe Import Precheck](../../validation/PIPE_IMPORT_PRECHECK.md), and [Product Data Validation Rules](../../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- **Traceability:** CP-001 through CP-010, PDM-001 through PDM-008, WCM-001 through WCM-008, ATT-001 through ATT-007, WCCFG-001 through WCCFG-013, Sprint 03A, and Sprint 03B
- **AI Compatibility:** AI-readable deterministic mapping; no autonomous product creation, commercial inference, or Phase 1 AI feature
- **Approval:** Pending Founder, Product Data, steel-domain, Sales, SEO, and WooCommerce technical review; not authorized for import

## Purpose

Map the approved Stainless Steel Pipe product-data contract to future WooCommerce concepts without creating products, attributes, terms, configuration, prices, stock records, or final SKUs.

## Mapping Boundary

- This document defines a logical target contract, not a live WooCommerce configuration.
- The staging CSV is not assumed to match a particular importer version directly.
- Exact importer headers, runtime IDs, global attribute IDs, term IDs, plugin behavior, and target-site capabilities require verified runtime evidence and a separately approved execution plan.
- Configuration First and Plugin First remain mandatory. No custom theme or custom business implementation is authorized here.
- Any unresolved hard gate keeps the entire import at `NO-GO`.

## Entity Mapping

| Product-data entity | Future WooCommerce concept | Ownership | Mapping rule | Current state |
| --- | --- | --- | --- | --- |
| Product Family | Product category or other approved canonical taxonomy | Taxonomy model | One approved canonical relationship; do not create a duplicate family term | `TBD`; no term or ID created |
| Variable Parent Product | Variable product | Product model | Own shared identity, content, category, variation declarations, inquiry-only behavior, and canonical ownership | Defined logically; no product created |
| Variation | Product variation | Product model | Belongs to exactly one parent and carries one approved five-axis tuple | Candidate rows only; commercial validity `TBD` |
| Material | Shared global attribute | Attribute dictionary | Working value `stainless-steel`; non-variation attribute | Terminology approval pending |
| Grade | Shared global attribute | Attribute dictionary | Variation axis using only `201`, `304`, `316`, `430` | Candidate values; no terms created |
| Finish | Shared global attribute | Attribute dictionary | Variation axis using only `silver`, `gold-pvd`, `black-pvd` | Candidate values; no terms created |
| Diameter | Shared global attribute | Attribute dictionary | Variation axis; numeric millimetre values from the matrix | Candidate values; no terms created |
| Thickness | Shared global attribute | Attribute dictionary | Variation axis; numeric millimetre values from the matrix | Candidate values; no terms created |
| Length | Shared global attribute | Attribute dictionary | Variation axis; numeric metre values `3` or `6` | Candidate values; no terms created |
| Unit | Shared reference attribute | Attribute dictionary | Fixed value `meter`; not a variation axis | Defined in data contract only |
| Inquiry context | Approved inquiry capability | Inquiry model | Preserve parent identity and selected variation tuple; no transactional substitution | Runtime mechanism `TBD` |
| SEO entity | Parent canonical product entity | SEO and URL models | Parent owns canonical intent by default; variation state is non-canonical by default | Canonical slug and runtime output `TBD` |

## Variable Parent Mapping

The future parent record must:

- Use the row role `variable`.
- Resolve to one approved stable parent identity and one approved final parent SKU before execution.
- Own the Persian parent name, approved category relationship, Material, Unit, shared content, and declared variation axes.
- Declare Grade, Finish, Diameter, Thickness, and Length as variation-capable global attributes only after their runtime identities and terms are approved.
- Preserve `inquiry_only=yes` and an empty public price.
- Expose no cart, checkout, payment, public quotation, price range, or stock promise.
- Own the approved canonical slug only after URL and SEO review.

The parent must not be imported while its SKU, canonical slug, category mapping, attribute identities, inquiry mechanism, or valid-combination set remains unresolved.

## Variation Mapping

Each future variation must:

- Use the row role `variation`.
- Resolve `parent_sku` to exactly one approved parent.
- Use one unique approved final variation SKU; every `TBD-*` value is a hard blocker.
- Carry exactly one approved value for Grade, Finish, Diameter, Thickness, and Length.
- Match an independently approved commercial combination; membership in the candidate value sets alone is insufficient.
- Inherit family/category, Material, Unit, Inquiry First, and No Public Pricing without creating conflicting child authority.
- Keep commercial availability at `TBD` until verified; `TBD` must never be translated to an in-stock, out-of-stock, backorder, or supply-after-order claim.
- Avoid an independent canonical URL unless a later approved exception exists.

## Attribute Mapping

| Source field | Logical attribute | Parent declaration | Variation value | Filter use | Mapping gate |
| --- | --- | --- | --- | --- | --- |
| `material` | Material | Yes | Inherited/shared | No | Founder/domain terminology approval |
| `grade` | Grade | Yes | Yes | Yes | Global attribute/term identity and valid-combination approval |
| `finish` | Finish | Yes | Yes | Yes | Global attribute/term identity and technical terminology approval |
| `diameter_mm` | Diameter | Yes | Yes | Yes | Numeric normalization and approved term representation |
| `thickness_mm` | Thickness | Yes | Yes | Yes | Numeric normalization and approved term representation |
| `length_m` | Length | Yes | Yes | Yes | Numeric normalization and approved term representation |
| `unit` | Unit | Yes | Inherited/shared | No | Must equal `meter` |
| `brand` | Brand | Only after verified | Only after verified | No | `TBD`; do not create a claim |
| `country` | Country | Only after verified | Only after verified | No | `TBD`; do not create a claim |

Runtime attribute names must resolve to approved global attributes. This document does not create or approve WordPress/WooCommerce `pa_*` identifiers.

## Identity and SKU Mapping

- CSV `parent_sku` is a staging parent reference and future parent-SKU candidate, not proof that a final SKU exists.
- CSV `variation_sku` is the future variation SKU field and must be globally unique under the approved SKU policy.
- Placeholder values beginning with `TBD-` must fail precheck.
- Runtime database IDs, taxonomy IDs, attribute IDs, term IDs, and external CRM/ERP IDs must not be derived from row position or invented.
- No SKU may contain price, stock, supplier, mutable URL, customer, or credential information.

## Inquiry and No-Price Mapping

| Source rule | Future target behavior | Required validation |
| --- | --- | --- |
| `inquiry_only=yes` | Product and selected variation remain inquiry-only | Parent and every variation retain inquiry action and context |
| `public_price` empty | No public regular price, sale price, range, Offer, or price feed | Field-level and rendered/API/schema/feed checks must be clean |
| No transaction | No cart, checkout, payment, or public order path | Runtime workflow validation before publication |
| Selected tuple | Inquiry receives approved parent/variation identifiers and attribute snapshot | Field mapping, permissions, and notification flow approved separately |

`public_price` has no permitted price target. Empty input must remain non-price behavior; it must not be converted to zero, free, hidden text, a sentinel, or a generated amount.

## Stock and Commercial Data Boundary

- `stock_status=TBD` is a staging blocker, not a WooCommerce stock value.
- No source row authorizes stock quantity, backorders, supply-after-order, lead time, supplier, minimum order, weight, origin, or availability.
- Commercial fields may be mapped only after verified values, owners, allowed-value rules, and Founder approval exist.
- No default stock state may be selected to make an import pass.

## Import Dependency Order

1. Approve family identity, Material/Grade/Finish terminology, and accountable data owners.
2. Approve taxonomy/category destination and global attribute identities/terms.
3. Approve valid commercial combinations without expanding the full Cartesian candidate space.
4. Approve final SKU policy and values.
5. Resolve required commercial and URL fields currently marked `TBD`.
6. Verify target WooCommerce/importer capabilities and approve the exact column mapping.
7. Pass [Pipe Import Precheck](../../validation/PIPE_IMPORT_PRECHECK.md).
8. Prepare separately approved staging, backup, dry-run, reconciliation, and rollback procedures.

This sequence describes dependencies only. It does not authorize or execute any step against WordPress.

## Blocking Unknowns

- Final parent and variation SKUs and stable IDs.
- Approved valid-combination dataset.
- Category/taxonomy destination and runtime term IDs.
- Runtime global attribute and term IDs.
- Inquiry capability and no-price runtime enforcement.
- Commercial availability and stock mapping.
- Canonical slug and indexation decision.
- Exact target importer/version behavior, staging target, backup, rollback, and reconciliation evidence.

## Approval Gates

| Gate | Required approval/evidence |
| --- | --- |
| Product/domain mapping | Founder, Product Data Owner, and qualified steel-domain reviewer |
| Commercial combinations and availability | Founder and approved Sales/Operations authority |
| Taxonomy/attribute mapping | Founder, Product Data, SEO, and WooCommerce reviewers |
| SKU/identity mapping | Founder and approved Operations/integration reviewers |
| Inquiry/no-price behavior | Founder, Sales, security, and WooCommerce reviewers |
| Import execution | Separate Founder authorization after precheck, staging, backup, dry run, and rollback evidence |

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03B logical WooCommerce mapping; no configuration or import executed. |

## Navigation

- [Pipe Product Family](PIPE_PRODUCT_FAMILY.md)
- [Pipe Variation Matrix](PIPE_VARIATION_MATRIX.md)
- [Pipe Import Mapping](../../imports/woocommerce/PIPE_IMPORT_MAPPING.md)
- [Pipe Import Precheck](../../validation/PIPE_IMPORT_PRECHECK.md)
- [Sprint 03B Audit](../../../../docs/AUDIT_REPORT_SPRINT03B.md)
