# Stainless Steel Pipe WooCommerce Mapping

## Document Control

- **Document ID:** `repository/data/products/pipes/PIPE_WOOCOMMERCE_MAPPING.md`
- **Status:** Review
- **Authority:** Product Data Mapping Asset
- **Owner:** Founder
- **Reviewer:** Product Data Owner and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.2.0
- **Last Updated:** 2026-08-21
- **Last Review:** 2026-08-21
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

- The canonical Repository source is exactly `Catalog → Platform → Family → Series → Variant Rules → SKU`; WooCommerce consumes a downstream projection and never owns that hierarchy or Product truth.
- This document defines a logical target contract, not a live WooCommerce configuration.
- The staging CSV is not assumed to match a particular importer version directly.
- Exact importer headers, runtime IDs, global attribute IDs, term IDs, plugin behavior, and target-site capabilities require verified runtime evidence and a separately approved execution plan.
- Configuration First and Plugin First remain mandatory. No custom theme or custom business implementation is authorized here.
- Any unresolved hard gate keeps the entire import at `NO-GO`.

## C006 Projection Contract

WooCommerce may only project selectors supplied by approved Family
configuration and Variant Rules; it must not hard-code one universal Pipe order
or infer a Cartesian product. Finish, Color, Appearance, and Coating Method are
separate concepts, and the PD-03A `finish=Silver` value remains only a bounded
legacy appearance designation. Diameter means nominal/market Diameter; OD is a
separate evidence-backed fact and ID is calculated and labeled derived. Brand is
projected only when canonical provenance and Family rules permit it.
Application/suitability content is a governed Knowledge relationship;
cutting/packaging/shipping are services; Mass, Availability, lead time, and
Pricing remain dynamic projections. This section authorizes no object, term,
Product, SKU, commercial data, import, plugin, or runtime change.

## Entity Mapping

| Product-data entity | Future WooCommerce concept | Ownership | Mapping rule | Current state |
| --- | --- | --- | --- | --- |
| Legacy Product Family presentation | Product category or other approved downstream taxonomy view | Taxonomy model | Map to one approved canonical Family source; do not create a duplicate Family identity or term | `TBD`; no term or ID created |
| Variable Parent Product | Variable product | WooCommerce adapter | Own shared commerce presentation, content, category view, projected axes, inquiry-only behavior, and public page/URL context only | Defined logically; no product created and no Repository authority |
| Variation | Product variation | WooCommerce adapter | Belongs to exactly one parent and maps one tuple permitted by canonical Variant Rules and separate commercial evidence | Candidate rows only; commercial validity `TBD` |
| Material | Shared global attribute | Attribute dictionary | Working value `stainless-steel`; non-variation attribute | Terminology approval pending |
| Grade | Shared global attribute | Attribute dictionary | Variation axis using only `201`, `304`, `316`, `430` | Candidate values; no terms created |
| Legacy appearance/finish token | Downstream attribute projection only after canonical mapping | Attribute dictionary | Preserves `silver`, `gold-pvd`, `black-pvd` as historical values without collapsing Finish/Color/Appearance/Coating | Candidate values; no terms created |
| Nominal/market Diameter | Shared global attribute | Attribute dictionary | Family-configured axis; numeric millimetre values are nominal, not OD/ID | Candidate values; no terms created |
| Thickness | Shared global attribute | Attribute dictionary | Variation axis; numeric millimetre values from the matrix | Candidate values; no terms created |
| Length | Shared global attribute | Attribute dictionary | Variation axis; numeric metre values `3` or `6` | Candidate values; no terms created |
| Unit | Shared reference attribute | Attribute dictionary | Fixed value `meter`; not a variation axis | Defined in data contract only |
| Inquiry context | Approved inquiry capability | Inquiry model | Preserve downstream parent mapping ID and selected variation tuple; no transactional substitution | Runtime mechanism `TBD` |
| SEO page projection | Parent public product-page/URL entity | SEO and URL models | Parent may own public page/search intent by default; this does not confer canonical Repository identity | Canonical slug and runtime output `TBD` |

## Variable Parent Mapping

The future parent record must:

- Use the row role `variable`.
- Resolve to one approved downstream parent mapping ID and one approved operational parent SKU before execution; neither is a canonical entity identity.
- Own the Persian presentation name, approved category view, Material/Unit display, shared content, and projected axes; it does not own their canonical source definitions.
- Mirror only the Family-configured selector axes and dependency order after canonical Variant Rules and runtime identities/terms are separately approved.
- Preserve `inquiry_only=yes` and an empty public price.
- Expose no cart, checkout, payment, public quotation, price range, or stock promise.
- Own an approved canonical public-page URL only after URL and SEO review; URL ownership does not transfer Product truth.

The parent must not be imported while its operational SKU, canonical public-page slug, category mapping, attribute identities, inquiry mechanism, or valid-combination set remains unresolved.

## Variation Mapping

Each future variation must:

- Use the row role `variation`.
- Resolve `parent_sku` to exactly one approved downstream parent mapping.
- Use one unique approved final variation SKU; every `TBD-*` value is a hard blocker.
- Carry exactly one approved value for each axis permitted by canonical Variant Rules; this Review mapping does not approve the listed axes or values.
- Match an independently approved commercial combination; membership in the candidate value sets alone is insufficient.
- Inherit family/category, Material, Unit, Inquiry First, and No Public Pricing without creating conflicting child authority.
- Keep commercial availability at `TBD` until verified; `TBD` must never be translated to an in-stock, out-of-stock, backorder, or supply-after-order claim.
- Avoid an independent canonical URL unless a later approved exception exists.

## Attribute Mapping

| Source field | Logical attribute | Parent presentation | Variation value | Filter use | Mapping gate |
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

Runtime attribute names must resolve to approved global attributes, and the Parent presentation must mirror canonical Variant Rules rather than define them. This document does not create or approve WordPress/WooCommerce `pa_*` identifiers.

## Identity and SKU Mapping

- CSV `parent_sku` is a downstream staging reference and future operational parent-SKU candidate, not proof that a final SKU or canonical entity identity exists.
- CSV `variation_sku` is a downstream future variation-SKU field and must be globally unique under the approved SKU policy; it is not a canonical entity identity.
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

1. Resolve the already governed canonical Family/Series/Variant Rules sources and approve only the downstream Family/Parent presentation mapping, remaining terminology, and accountable data owners.
2. Approve taxonomy/category destination and global attribute identities/terms.
3. Approve valid commercial combinations without expanding the full Cartesian candidate space.
4. Approve final SKU policy and values.
5. Resolve required commercial and URL fields currently marked `TBD`.
6. Verify target WooCommerce/importer capabilities and approve the exact column mapping.
7. Pass [Pipe Import Precheck](../../validation/PIPE_IMPORT_PRECHECK.md).
8. Prepare separately approved staging, backup, dry-run, reconciliation, and rollback procedures.

This sequence describes dependencies only. It does not authorize or execute any step against WordPress.

## Blocking Unknowns

- Final downstream parent/variation mapping IDs and operational SKUs; none may replace canonical Repository identity.
- Approved valid-combination dataset.
- Category/taxonomy destination and runtime term IDs.
- Runtime global attribute and term IDs.
- Inquiry capability and no-price runtime enforcement.
- Commercial availability and stock mapping.
- Canonical public-page slug and indexation decision.
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
| 0.2.0 | 2026-08-21 | C006 architecture-only reconciliation made the downstream selector Family-configured, separated appearance and dimensional semantics, and excluded Knowledge, service, and dynamic commercial data from Product identity; no WooCommerce or runtime mutation. |
| 0.1.0 | 2026-07-04 | Initial Sprint 03B logical WooCommerce mapping; no configuration or import executed. |
| 0.1.1 | 2026-08-03 | Reclassified every Parent, Variation, taxonomy, SKU, SEO, and WooCommerce reference as a downstream projection of canonical Family/Series/Variant Rules; no object, term, mapping, import, or runtime change was created. |

## Navigation

- [Pipe Product Family](PIPE_PRODUCT_FAMILY.md)
- [Pipe Variation Matrix](PIPE_VARIATION_MATRIX.md)
- [Pipe Import Mapping](../../imports/woocommerce/PIPE_IMPORT_MAPPING.md)
- [Pipe Import Precheck](../../validation/PIPE_IMPORT_PRECHECK.md)
- [Sprint 03B Audit](../../../../docs/AUDIT_REPORT_SPRINT03B.md)
