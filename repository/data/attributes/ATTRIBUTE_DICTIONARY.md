# Product Attribute Dictionary

## Document Control

- **Document ID:** `repository/data/attributes/ATTRIBUTE_DICTIONARY.md`
- **Status:** Review
- **Authority:** Product Data Asset
- **Owner:** Founder
- **Reviewer:** Product Data Owner and Qualified Steel-Domain Reviewer
- **Approval Authority:** Founder
- **Version:** 0.2.0
- **Last Updated:** 2026-08-21
- **Last Review:** 2026-08-03
- **Review Cycle:** On attribute name, label, slug, type, candidate use flag, registry input, Family/Series scope, Variant Rules resolution, CRM/SEO mapping, or validation change
- **Lifecycle:** Review
- **Source of Truth:** Approved canonical `Catalog → Platform → Family → Series → Variant Rules → derived SKU` sources and [Product Attribute Model](../../../docs/22_PRODUCT_ATTRIBUTE_MODEL.md); Sprint 03A tables are legacy/candidate registry inputs only
- **Dependencies:** [Product Attribute Model](../../../docs/22_PRODUCT_ATTRIBUTE_MODEL.md), [Product Data Model](../../../docs/19_PRODUCT_DATA_MODEL.md), and [WooCommerce Product Model](../../../docs/20_WOOCOMMERCE_PRODUCT_MODEL.md)
- **Related Documents:** [Stainless Steel Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md), [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md), [Pipe Import Template](../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv), [Pipe SEO Entity Model](../seo/PIPE_SEO_ENTITY_MODEL.md), and [Validation Rules](../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- **Traceability:** ATT-001 through ATT-007, WCM-004, WCM-007, WCCFG-007, and Sprint 03A
- **AI Compatibility:** AI-readable controlled dictionary; no generated values, inferred claims, or Phase 1 AI feature
- **Approval:** Pending Founder, domain, Product Data, SEO, Sales, CRM, and WooCommerce review; no global attribute is configured

## Purpose

Define a controlled identity and candidate-evidence dictionary for the Stainless Steel Pipe Family while keeping exact WooCommerce configuration, Product applicability, and unapproved commercial values blocked.

## Authority Boundary

- Canonical Product authority follows exactly `Catalog → Platform → Family → Series → Variant Rules → derived SKU`; SKU is derived and is not canonical entity identity.
- Attribute and value registries provide identity and candidate evidence only. They do not govern Product applicability, variation axes, allowed values, or valid tuples.
- The Sprint 03A dictionary table, candidate value table, and use profile below are legacy/candidate registry inputs. Their rows, values, and flags are non-governing for applicability, axes, allowed values, and valid tuples.
- Applicability, axes, allowed values, and valid tuples resolve only from the applicable Variant Rules for the canonical Family/Series context. Missing resolution remains blocked; no registry row, downstream flag, WooCommerce mapping, or Founder-review item can substitute for it.
- WooCommerce use, filtering, variation, SEO, and CRM columns are candidate downstream projections only. They create no Product, SKU, availability, public claim, or runtime approval.
- The immutable PD-02B and PD-03A facts and exact overrides recorded below remain unchanged and are not generalized into broader Sprint 03A applicability.

## C006 Semantic Reconciliation

The table below preserves Sprint 03A candidate vocabulary, but C006 establishes
the following architecture-only interpretation for every later consumer:

- the legacy `finish` row and PD-03A `finish=Silver` are a bounded appearance
  designation, not a general Finish/Color/coating taxonomy;
- Finish, Color, Appearance, and Coating Method are separate concepts; PVD and
  electrostatic coating remain separate namespaces;
- `diameter` is nominal/market Diameter unless separately sourced as measured OD;
  calculated ID requires evidence-backed OD and Thickness and is labeled
  calculated/nominal, never measured;
- Brand may participate in a Family selector only after canonical identity,
  provenance, applicable Variant Rules, and valid-combination evidence exist;
- Application is Knowledge/use-context input, not immutable Product identity;
- cutting, packaging, and shipping are services; current Mass, Availability, and
  Pricing are dynamic commercial data. None is an attribute axis.

No new Attribute, controlled value, Product, tuple, Mass, Availability, Price, or
runtime mapping is created by this reconciliation.

## Flag Semantics

- `Yes` records a legacy Sprint 03A candidate for that downstream use; it does not establish applicability or axis authority.
- `No` means the attribute must not be used for that purpose in this profile.
- `Required` records a legacy candidate staging expectation and does not require a value unless the applicable Variant Rules resolve that attribute and value for the Family/Series context; import may impose a stricter gate.
- SEO `Yes` means supporting factual use only. It does not approve an indexable attribute archive or landing.
- WooCommerce slugs are proposed system-local adapter identifiers without the runtime `pa_` prefix; they are not canonical identities, and actual IDs remain unconfigured.

## Attribute Dictionary

| English name | Persian label | Slug | Data type | WooCommerce use | Filterable | Variation attribute | SEO use | CRM use | Required | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Material | آلیاژ | `material` | Controlled term | Global shared specification | No | No | Yes | Yes | Yes | Family identity indicates Stainless Steel; supplied codes 201/304/316/430 are stored under Grade. Persian label conflicts with the existing Material/Alloy distinction and requires Founder/domain confirmation. |
| Grade | گرید | `grade` | Controlled technical code | Global attribute | Yes | Yes | Yes | Yes | Yes | Sprint 03A candidate registry values: `201`, `304`, `316`, `430`; applicability and allowed-value status require resolution from the applicable Variant Rules. |
| Finish (legacy bounded appearance designation) | رنگ و پوشش | `finish` | Controlled term | Legacy global-attribute candidate | Yes | Yes | Yes | Yes | Yes | Sprint 03A candidate values are historical inputs only. PD-03A approves only `Silver` as an INTERNAL appearance designation; this row must not collapse Finish, Color, Appearance, PVD, or coating method. |
| Diameter | قطر اسمی / بازاری | `diameter` | Decimal number, mm context | Global typed/controlled attribute | Yes | Yes | Yes | Yes | Yes | Candidate values are nominal/market Diameter unless separate OD evidence says otherwise. Applicable Variant Rules alone authorize values and axes. |
| Thickness | ضخامت | `thickness` | Decimal number, mm context | Global typed/controlled attribute | Yes | Yes | Yes | Yes | Yes | Candidate mm registry inputs are copied from the legacy Pipe Variation Matrix; applicable Variant Rules alone authorize values and axes. Tolerance remains `TBD`. |
| Length | طول | `length` | Decimal number, m context | Global typed/controlled attribute | Yes | Yes | Yes | Yes | Yes | Sprint 03A candidate registry values: `3`, `6`; applicable Variant Rules alone authorize values and axes. Display may append `m`; stored value remains numeric. |
| Surface | سطح | `surface` | Controlled term | Global descriptive attribute | No | No | No | Yes | No | Exact surface definitions and relationship to Finish remain `TBD`; no free-text claims. |
| Unit | واحد | `unit` | Controlled enum | Global reference attribute | No | No | No | Yes | Yes | Sprint 03A candidate registry value: `meter`; not a variation axis or standalone filter, and not applicable without Variant Rules resolution. |
| Brand | برند | `brand` | Controlled relationship/term | Global attribute or approved brand mechanism | Conditional | Conditional | No | Yes | No | Value is `TBD`; selector use requires canonical identity, C002 provenance, and Variant Rule binding. Do not infer Brand from manufacturer or supplier. |
| Country | کشور سازنده | `country` | Controlled term | Global descriptive attribute | No | No | No | Yes | No | Value is `TBD`; requires verified legal/operational source and must distinguish manufacturing origin from shipping origin. |
| Quality Level | سطح کیفیت | `quality-level` | Controlled enum | Global descriptive attribute | No | No | No | Yes | No | Value set is `TBD`; must not imply grade, certification, standard, warranty, or origin. |
| Application | کاربرد | `application` | Governed Knowledge/use-context relationship | No Product-attribute authority | No | No | Yes | Yes | No | Value set and taxonomy authority are `TBD`; application guidance is Knowledge, not Product identity or a Variant axis. |
| Environment | محیط استفاده | `environment` | Controlled term | Global descriptive attribute | No | No | No | Yes | No | Value set is `TBD`; no suitability or safety claim without technical evidence. |
| Installation Use | نوع مصرف | `installation-use` | Controlled term | Global descriptive attribute | No | No | No | Yes | No | Value set is `TBD`; keep distinct from installation instructions and Application taxonomy. |
| Stock Status | وضعیت تأمین | `stock-status` | Controlled enum | Variation operational metadata; future Woo mapping | No | No | No | Yes | Yes | Commercial availability is `TBD`; no public stock, backorder, lead-time, or supply promise. |
| Inquiry Priority | اولویت استعلام | `inquiry-priority` | Controlled internal enum | Not a public WooCommerce attribute | No | No | No | Yes | No | Value/routing rules are `TBD`; protected internal data only and never a public ranking or promise. |

## Legacy/Candidate Registry Inputs from Sprint 03A

The values below are preserved exactly as Sprint 03A candidate evidence. They are not an allowed-value set and do not establish applicability, axes, valid tuples, Product records, or availability; only the applicable Variant Rules may authorize those concerns.

| Attribute | Candidate stored values | Persian display labels | Legacy evidence boundary |
| --- | --- | --- | --- |
| Material | `stainless-steel` | استیل ضدزنگ / لوله استیل | Working family context; final domain label approval required |
| Grade | `201`, `304`, `316`, `430` | ۲۰۱، ۳۰۴، ۳۱۶، ۴۳۰ | Candidate values supplied by Sprint 03A; valid combination/commercial review required |
| Finish | `silver`, `gold-pvd`, `black-pvd` | نقره‌ای، طلایی PVD، مشکی PVD | Candidate values supplied by Sprint 03A; technical terminology review required |
| Diameter | `16`, `19`, `22`, `25`, `32`, `38`, `42`, `51`, `63`, `76`, `102` | Numeric + میلی‌متر | Candidate controlled set; commercial combination review required |
| Thickness | `0.6`, `0.8`, `1`, `1.2`, `1.5`, `2` | Numeric + میلی‌متر | Candidate controlled set; tolerance/commercial review required |
| Length | `3`, `6` | ۳ متر، ۶ متر | Candidate controlled set |
| Unit | `meter` | متر | Fixed for Sprint 03A |
| Stock Status | `TBD` | نیازمند تأیید | Staging-only unresolved commercial state; blocks import/publication |
| All other attributes | `TBD` unless separately approved | نیازمند تأیید | Must not be inferred |

## Legacy/Candidate Attribute Use Profile

- Sprint 03A candidate axis list: Grade, Finish, Diameter, Thickness, Length. This list is non-governing; an axis applies only when resolved from the applicable Variant Rules.
- Sprint 03A candidate required non-axis list: Material, Unit, Stock Status. Requiredness applies only after canonical Family/Series and applicable Variant Rules resolution.
- Sprint 03A candidate optional descriptive/internal list: Surface, Brand, Country, Quality Level, Application, Environment, Installation Use, Inquiry Priority.
- Size is derived from structured dimensions and is not an independent attribute, filter, SKU source, or variation axis.
- New values are rejected or quarantined; imports must never create terms silently.
- Flat controlled registries provide identity and candidate evidence only. No value hierarchy or applicability rule is created by Sprint 03A.
- No candidate row, flag, value, or list in this profile creates an allowed value, axis, or valid tuple.

## Known Decisions Still Required

- Confirm Material Persian label and its distinction from Alloy/Grade.
- Confirm Grade/Finish technical semantics and display labels.
- Approve the applicable Variant Rules resolution for precision, tolerance, unit, range, ordering, allowed values, axes, and valid tuples without treating registry candidates as authority.
- Approve Application/Environment/Installation Use boundaries and taxonomy ownership.
- Approve WooCommerce attribute slugs, term IDs, archive/filter settings, and Admin permissions.
- Approve CRM/ERP/CentralSteel mappings.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.2.0 | 2026-08-21 | Added the C006 architecture-only semantic overlay for legacy Finish/appearance, nominal Diameter versus OD/calculated ID, conditional Brand selection, and Product/Knowledge/service/dynamic-commercial separation; no canonical records changed. |
| 0.1.0 | 2026-07-04 | Initial Sprint 03A attribute dictionary for Stainless Steel Pipe. |
| 0.1.1 | 2026-08-03 | Classified Sprint 03A tables, values, and axes as legacy/candidate registry inputs; applicability, allowed values, axes, and valid tuples now resolve only from applicable Variant Rules. PD-02B and PD-03A facts and overrides remain unchanged; no Product, SKU, availability, or runtime approval. |

## PD-02B Canonical Subset

Only `material` (`attr:dbf5365ee1e5`) and `grade`
(`attr:28565665c910`) are included in the PD-02B APPROVED scope. Their controlled terms
are limited to `stainless_steel`, `201`, `304`, and `316`; Material and Grade
are REQUIRED only in the INTERNAL Family Profile. Every other dictionary row,
Unit, dimension, Finish/Color/PVD field, filter, variation, SEO, inquiry, and
commerce behavior remains outside PD-02B.

## Navigation

## PD-03A Exact Override

PD-03A supersedes legacy candidates only within its immutable extension:

- `finish`: only `silver`, as an INTERNAL appearance designation without PVD,
  coating, quality, standard, application, or availability claim.
- `diameter`: decimal, `mm`, precision 0; synthetic tuples use 16, 38, and 51.
- `thickness`: decimal, `mm`, precision 2; synthetic tuples use 0.35 and 0.50.
- `length`: decimal, `m`, precision 0; synthetic tuples use 6.
- INTERNAL axes: Grade, Finish, Diameter, Thickness, and Length.
- fixed INTERNAL non-axis: Material.

Legacy 430, Gold/Black PVD, 3m, broader dimensions, filtering, SEO, CRM,
WooCommerce, stock-status, and import statements remain outside PD-03A.
Synthetic tuples are not Product or Pilot records.

- [Stainless Steel Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md)
- [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md)
- [Pipe Import Template](../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv)
- [Product Data Validation Rules](../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- [Sprint 03A Audit](../../../docs/AUDIT_REPORT_SPRINT03A.md)
