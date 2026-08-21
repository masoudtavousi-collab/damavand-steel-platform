# Pipe Attribute Model

## Document Control

- **Document ID:** `repository/data/attributes/PIPE_ATTRIBUTE_MODEL.md`
- **Status:** Review
- **Authority:** Product Data Attribute Asset
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Qualified Steel-Domain Reviewer, SEO Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.2.0
- **Last Updated:** 2026-08-21
- **Last Review:** 2026-08-03
- **Review Cycle:** On Pipe attribute, label, slug, scope, variation, filter, product-table, SEO, allowed-value, or validation change
- **Lifecycle:** Review
- **Source of Truth:** [Attribute Dictionary](ATTRIBUTE_DICTIONARY.md), [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md), and [Product Attribute Model](../../../docs/22_PRODUCT_ATTRIBUTE_MODEL.md)
- **Dependencies:** [Pipe Taxonomy and Attribute Classification](../taxonomies/PIPE_TAXONOMY_ATTRIBUTE_CLASSIFICATION.md), [Attribute Dictionary](ATTRIBUTE_DICTIONARY.md), and [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md)
- **Related Documents:** [Pipe Category Model](../taxonomies/PIPE_CATEGORY_MODEL.md), [Pipe WooCommerce Mapping](../products/pipes/PIPE_WOOCOMMERCE_MAPPING.md), and [Pipe Data Governance Checklist](../validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md)
- **Traceability:** CP-001 through CP-010, PDM-001 through PDM-008, ATT-001 through ATT-007, WCM-001 through WCM-008, TAX-001 through TAX-008, Sprint 03A, Sprint 03B, and Sprint 03C
- **AI Compatibility:** AI-readable controlled attribute profile; no inferred values, term generation, or Phase 1 AI feature
- **Approval:** Pending Founder, domain, Product Data, SEO, and WooCommerce review; no global/local attribute or term is configured

## Purpose

Define the logical downstream WooCommerce attribute projection for Stainless Steel Pipe before any attribute, term, filter, variation, product table, or product is created.

## Attribute Policy

- All 14 Pipe product-specification attributes map to system-local global WooCommerce attributes. No WooCommerce local attribute is authorized, and this mapping does not own canonical Product truth.
- Grade, Finish, Diameter, Thickness, and Length are downstream projections of the only candidate variation axes recorded for this Pipe profile; canonical axis and tuple authority remains with the applicable Variant Rules.
- The five variation-attribute mappings are also system-local global attributes; “Variation Attribute” describes downstream use, not canonical ownership.
- `Yes` for Product table or SEO means eligible after value and publication approval. `TBD` and unverified values never render.
- Filterable and SEO flags are independent. A filter does not create an indexable archive or landing.
- Attribute slugs are logical lowercase ASCII identifiers without a runtime `pa_` prefix. Runtime IDs/prefixes remain unconfigured.

## C006 Selector and Semantic Boundary

The current Pipe experience architecture uses a Family-configured dependent
selector. Selector order is projection policy, not an Attribute or Variant Rule,
and no fixed order in this historical profile applies universally. Every option
must resolve to the applicable Variant Rules; `UNKNOWN`, `INCOMPATIBLE`, and
`NEEDS_VERIFICATION` are distinct and none means out of stock.

Finish, Color, Appearance, and Coating Method remain separate. The historical
`finish`/`Silver` pair is preserved only as the immutable PD-03A INTERNAL
appearance designation. Diameter is nominal/market Diameter unless separate
evidence establishes OD; calculated ID is formula-bound and must not be labeled
measured. Brand may become selectable only after canonical identity/provenance
and Variant Rule evidence. Application guidance belongs to Knowledge; cutting
and shipping are services; Mass, Availability, and Pricing are dynamic
commercial concerns outside this attribute model.

## Pipe Attribute Registry

| Attribute name | Persian label | Slug | Global/local | Variations | Filtering | Product table | SEO | Allowed values | Validation rule | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Material | آلیاژ | `material` | Global | No | No | Yes | Yes | Working value `stainless-steel` | Exact controlled identity; Founder/domain terminology approval required | Keep distinct from Grade and broader Material category authority |
| Grade | گرید | `grade` | Global | Yes | Yes | Yes | Yes | `201`, `304`, `316`, `430` | Exact ASCII token from controlled set and approved valid combination | Technical designation; supplied as “Materials” in Sprint 03A but normalized to Grade pending approval |
| Finish (legacy appearance designation) | رنگ و پوشش | `finish` | Global | Conditional | Conditional | Conditional | Conditional | Historical candidate values only; PD-03A approves only `Silver` internally | Exact governed reference and approved valid combination | Never merge Finish, Color, Appearance, coating method, PVD, or quality |
| Diameter | قطر اسمی / بازاری | `diameter` | Global | Conditional | Conditional | Conditional | Conditional | Historical nominal candidate values in mm | Canonical decimal, explicit nominal context, approved valid combination | Never treat nominal Diameter as measured OD by default |
| Thickness | ضخامت | `thickness` | Global | Yes | Yes | Yes | Yes | `0.6`, `0.8`, `1`, `1.2`, `1.5`, `2` mm | Canonical decimal, allowed set, explicit mm display context, approved valid combination | Tolerance remains `TBD` |
| Length | طول | `length` | Global | Yes | Yes | Yes | Yes | `3`, `6` m | Canonical decimal, allowed set, explicit metre display context, approved valid combination | Fixed lengths only in current candidate profile |
| Surface | سطح | `surface` | Global | No | No | Yes | No | `TBD` | Reject until controlled definition, values, and Finish relationship are approved | Optional; no free text or variation use |
| Unit | واحد | `unit` | Global | No | No | Yes | No | `meter` | Exact token `meter`; consistent on parent and variations | Reference attribute; not a standalone filter or axis |
| Brand | برند | `brand` | Global | Conditional | Conditional | Yes | No | `TBD` | Verified canonical Brand identity, C002 provenance, and Variant Rule binding | No supplier/manufacturer inference or Brand value creation |
| Country | کشور سازنده | `country` | Global | No | No | Yes | No | `TBD` | Verified manufacturing-origin registry; reject shipping-origin substitution | Exact source and definition required |
| Quality Level | سطح کیفیت | `quality-level` | Global | No | No | Yes | No | `TBD` | Controlled definition/evidence required; reject implied grade, certification, warranty, or origin | Optional; not a commercial quality claim by label alone |
| Application | کاربرد | `application` | Knowledge relationship only | No | No | Conditional | Yes | `TBD` | Governed use-context and authoritative Knowledge evidence required | Not Product identity, an Attribute axis, or a Pipe category |
| Environment | محیط استفاده | `environment` | Global | No | No | Yes | No | `TBD` | Controlled evidence-backed values; reject unsupported suitability/safety claims | Not a variation axis |
| Installation Use | نوع مصرف | `installation-use` | Global | No | No | Yes | No | `TBD` | Controlled values and definition required; reject unverified instructions | Not a variation axis or category |

## Legacy Variation Attribute Order

The historical Sprint 03C projection order was:

1. Grade / گرید
2. Finish / رنگ و پوشش
3. Diameter / قطر
4. Thickness / ضخامت
5. Length / طول

This list is not a universal or current hard-coded selector. C006 permits a
Family-configured sequence such as Grade → Brand → nominal Diameter → Thickness
→ Appearance/Finish → Length, but only the governing Variant Rules may supply
axes, values, and valid combinations. No default selection is authorized, and
the 1,584-value Cartesian candidate space must not be expanded automatically.

## Filter Model

| Filter order | Attribute | Filter behavior | Public URL/indexation boundary |
| ---: | --- | --- | --- |
| 1 | Grade | Exact controlled term | Filter state only; no automatic canonical/indexable page |
| 2 | Finish | Exact controlled term | Filter state only; no automatic finish category/archive |
| 3 | Diameter | Exact numeric allowed value with mm display | Filter state only; no dimension category/archive |
| 4 | Thickness | Exact numeric allowed value with mm display | Filter state only; no dimension category/archive |
| 5 | Length | Exact numeric allowed value with metre display | Filter state only; no length category/archive |

Material, Surface, Unit, Brand, Country, Quality Level, Application, Environment, and Installation Use are non-filterable in this Pipe profile. A future change requires user need, value completeness, result-quality, mobile UX, Persian RTL, performance, empty-state, URL, SEO, and governance evidence.

## Product Table Model

- Eligible public specifications may appear in one approved Persian RTL product specification table after value verification.
- Grade, Finish, Diameter, Thickness, and Length display the selected variation values.
- Material and Unit display shared downstream Parent page context sourced from the canonical Repository record.
- Optional attributes render only when a verified non-`TBD` value exists.
- Table labels use the Persian labels in this model; technical tokens remain stable.
- Stock, Inquiry Priority, internal notes, SKUs, import helpers, CRM controls, and `public_price` are not attribute-table rows.
- The table must not imply price, availability, supplier, certification, warranty, safety, or suitability without approved evidence.

## SEO Model

- Material, Grade, Finish, Diameter, Thickness, Length, and Application may support approved factual content.
- Attribute use does not approve indexable archives, generated landing pages, titles, descriptions, or schema.
- The Product Family/category or Variable Parent Product owns canonical intent according to later SEO approval.
- Surface, Unit, Brand, Country, Quality Level, Environment, and Installation Use are non-SEO in this Pipe profile unless a separately reviewed change is approved.
- No attribute may generate price/Offer, stock/availability, supplier, or unsupported technical claims.

## Value and Term Governance

- One system-local WooCommerce global-attribute mapping and one system-local term/value mapping per canonical source concept; these adapter identifiers are not canonical Product identities.
- No local duplicates, free-text synonyms, mixed Persian/English slug forms, silent term creation, or auto-correction into new values.
- Persian labels and English internal keys remain separate controlled representations.
- Dimension values use canonical decimals; units remain explicit context.
- Any allowed-value change requires domain review, duplicate/alias review, matrix impact, filter impact, import impact, SEO impact, CRM impact, and migration evidence.
- Runtime attribute IDs, term IDs, ordering, archive behavior, and plugin/configuration remain `TBD`.

## Founder Decisions Required

- Approve all 14 attributes, labels, slugs, scopes, and use flags.
- Approve Material/Grade/Finish terminology and controlled values.
- Approve the downstream projection and order of the five candidate axes only after the governing Variant Rules and valid tuples are approved.
- Approve optional attribute definitions/value registries.
- Approve filter scope and mobile Persian RTL behavior.
- Approve product-table disclosure and SEO usage.
- Approve physical WooCommerce attribute/term mapping in a later implementation decision.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.2.0 | 2026-08-21 | C006 architecture-only reconciliation replaced universal selector ordering with Family configuration; separated Finish/Color/Appearance/Coating, nominal Diameter/OD/calculated ID, Brand provenance, Knowledge, services, and dynamic commercial context without creating data or runtime mappings. |
| 0.1.0 | 2026-07-04 | Initial Sprint 03C Pipe global attribute profile; no attribute or term implementation. |
| 0.1.1 | 2026-08-03 | Reclassified WooCommerce attributes, terms, axes, and Parent context as downstream projections of canonical Family/Series/Variant Rules sources; no value, tuple, term, or runtime approval. |

## PD-02B Profile Reconciliation

The canonical PD-02B APPROVED Profile is
`pprof:26a474c2e100` for Family `prd:family:a10c6d8ceabc`. It contains only
Material and Grade, both REQUIRED and `INTERNAL`, with variation, filtering,
inquiry, and SEO use disabled. This does not approve the broader Pipe Attribute
model, Units, dimensions, Finish/Color/PVD, combinations, Products, or runtime
mappings.

## Navigation

## PD-03A Exact Prerequisite Boundary

The legacy public/filter/SEO/WooCommerce columns above do not control PD-03A.
The exact extension permits only INTERNAL Grade, Finish, Diameter, Thickness,
and Length axes; required fixed non-axis Material; `finish=Silver` as a
no-claim appearance designation; Diameter in `mm` at precision 0; Thickness in
`mm` at precision 2; and Length in `m` at precision 0.

Synthetic tests exercise only 201/Silver/16/0.35/6,
201/Silver/38/0.50/6, and 201/Silver/51/0.50/6. They create no filter, SEO,
Product table, inquiry, PVD, 430, 3m, WooCommerce, Product, canonical Pilot,
SKU, Slug, availability, import, or runtime authority.

- [Attribute Dictionary](ATTRIBUTE_DICTIONARY.md)
- [Pipe Taxonomy and Attribute Classification](../taxonomies/PIPE_TAXONOMY_ATTRIBUTE_CLASSIFICATION.md)
- [Pipe Category Model](../taxonomies/PIPE_CATEGORY_MODEL.md)
- [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md)
- [Pipe Data Governance Checklist](../validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md)
- [Sprint 03C Audit](../../../docs/AUDIT_REPORT_SPRINT03C.md)
