# Product Attribute Dictionary

## Document Control

- **Document ID:** `repository/data/attributes/ATTRIBUTE_DICTIONARY.md`
- **Status:** Review
- **Authority:** Product Data Asset
- **Owner:** Founder
- **Reviewer:** Product Data Owner and Qualified Steel-Domain Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On attribute name, label, slug, type, use flag, value set, Product Type profile, CRM/SEO mapping, or validation change
- **Lifecycle:** Review
- **Source of Truth:** Sprint 03A required attribute list and [Product Attribute Model](../../../docs/22_PRODUCT_ATTRIBUTE_MODEL.md)
- **Dependencies:** [Product Attribute Model](../../../docs/22_PRODUCT_ATTRIBUTE_MODEL.md), [Product Data Model](../../../docs/19_PRODUCT_DATA_MODEL.md), and [WooCommerce Product Model](../../../docs/20_WOOCOMMERCE_PRODUCT_MODEL.md)
- **Related Documents:** [Stainless Steel Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md), [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md), [Pipe Import Template](../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv), [Pipe SEO Entity Model](../seo/PIPE_SEO_ENTITY_MODEL.md), and [Validation Rules](../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- **Traceability:** ATT-001 through ATT-007, WCM-004, WCM-007, WCCFG-007, and Sprint 03A
- **AI Compatibility:** AI-readable controlled dictionary; no generated values, inferred claims, or Phase 1 AI feature
- **Approval:** Pending Founder, domain, Product Data, SEO, Sales, CRM, and WooCommerce review; no global attribute is configured

## Purpose

Define the implementation-ready attribute contract for the Stainless Steel Pipe family while keeping exact WooCommerce configuration and unapproved commercial values blocked.

## Flag Semantics

- `Yes` means the attribute is permitted for that use in this Sprint 03A profile after value/combination approval.
- `No` means the attribute must not be used for that purpose in this profile.
- `Required` means a staged row must contain an approved value or an explicitly permitted `TBD` state before review; import may impose a stricter gate.
- SEO `Yes` means supporting factual use only. It does not approve an indexable attribute archive or landing.
- WooCommerce slugs are proposed lowercase ASCII identifiers without the runtime `pa_` prefix; actual IDs remain unconfigured.

## Attribute Dictionary

| English name | Persian label | Slug | Data type | WooCommerce use | Filterable | Variation attribute | SEO use | CRM use | Required | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Material | آلیاژ | `material` | Controlled term | Global shared specification | No | No | Yes | Yes | Yes | Family identity indicates Stainless Steel; supplied codes 201/304/316/430 are stored under Grade. Persian label conflicts with the existing Material/Alloy distinction and requires Founder/domain confirmation. |
| Grade | گرید | `grade` | Controlled technical code | Global attribute | Yes | Yes | Yes | Yes | Yes | Allowed Sprint 03A values: `201`, `304`, `316`, `430`; qualified steel-domain review required. |
| Finish | رنگ و پوشش | `finish` | Controlled term | Global attribute | Yes | Yes | Yes | Yes | Yes | Allowed values: `silver`, `gold-pvd`, `black-pvd`; keep separate from Surface and unverified coating claims. |
| Diameter | قطر | `diameter` | Decimal number, mm context | Global typed/controlled attribute | Yes | Yes | Yes | Yes | Yes | Allowed mm values are defined by the Pipe Variation Matrix; store numeric value without duplicating unit text. |
| Thickness | ضخامت | `thickness` | Decimal number, mm context | Global typed/controlled attribute | Yes | Yes | Yes | Yes | Yes | Allowed mm values are defined by the Pipe Variation Matrix; tolerance remains `TBD`. |
| Length | طول | `length` | Decimal number, m context | Global typed/controlled attribute | Yes | Yes | Yes | Yes | Yes | Allowed meter values: `3`, `6`; display may append `m`, stored value remains numeric. |
| Surface | سطح | `surface` | Controlled term | Global descriptive attribute | No | No | No | Yes | No | Exact surface definitions and relationship to Finish remain `TBD`; no free-text claims. |
| Unit | واحد | `unit` | Controlled enum | Global reference attribute | No | No | No | Yes | Yes | Fixed Sprint 03A value: `meter`; not a variation axis or standalone filter. |
| Brand | برند | `brand` | Controlled relationship/term | Global attribute or approved brand mechanism | No | No | No | Yes | No | Value is `TBD`; do not invent manufacturer/supplier identity or duplicate Brand taxonomy authority. |
| Country | کشور سازنده | `country` | Controlled term | Global descriptive attribute | No | No | No | Yes | No | Value is `TBD`; requires verified legal/operational source and must distinguish manufacturing origin from shipping origin. |
| Quality Level | سطح کیفیت | `quality-level` | Controlled enum | Global descriptive attribute | No | No | No | Yes | No | Value set is `TBD`; must not imply grade, certification, standard, warranty, or origin. |
| Application | کاربرد | `application` | Controlled relationship/term | Global descriptive attribute | No | No | Yes | Yes | No | Value set and taxonomy authority are `TBD`; SEO use requires one canonical intent owner and suitability evidence. |
| Environment | محیط استفاده | `environment` | Controlled term | Global descriptive attribute | No | No | No | Yes | No | Value set is `TBD`; no suitability or safety claim without technical evidence. |
| Installation Use | نوع مصرف | `installation-use` | Controlled term | Global descriptive attribute | No | No | No | Yes | No | Value set is `TBD`; keep distinct from installation instructions and Application taxonomy. |
| Stock Status | وضعیت تأمین | `stock-status` | Controlled enum | Variation operational metadata; future Woo mapping | No | No | No | Yes | Yes | Commercial availability is `TBD`; no public stock, backorder, lead-time, or supply promise. |
| Inquiry Priority | اولویت استعلام | `inquiry-priority` | Controlled internal enum | Not a public WooCommerce attribute | No | No | No | Yes | No | Value/routing rules are `TBD`; protected internal data only and never a public ranking or promise. |

## Controlled Values for Sprint 03A

| Attribute | Allowed stored values | Persian display labels | Approval boundary |
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

## Attribute Use Profile

- Variation axes: Grade, Finish, Diameter, Thickness, Length.
- Required non-axis attributes: Material, Unit, Stock Status.
- Optional descriptive/internal attributes: Surface, Brand, Country, Quality Level, Application, Environment, Installation Use, Inquiry Priority.
- Size is derived from structured dimensions and is not an independent attribute, filter, SKU source, or variation axis.
- New values are rejected or quarantined; imports must never create terms silently.
- Flat controlled registries are the default. No value hierarchy is created by Sprint 03A.

## Known Decisions Still Required

- Confirm Material Persian label and its distinction from Alloy/Grade.
- Confirm Grade/Finish technical semantics and display labels.
- Approve precision, tolerance, unit, range, ordering, and valid combinations.
- Approve Application/Environment/Installation Use boundaries and taxonomy ownership.
- Approve WooCommerce attribute slugs, term IDs, archive/filter settings, and Admin permissions.
- Approve CRM/ERP/CentralSteel mappings.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03A attribute dictionary for Stainless Steel Pipe. |

## Navigation

- [Stainless Steel Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md)
- [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md)
- [Pipe Import Template](../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv)
- [Product Data Validation Rules](../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- [Sprint 03A Audit](../../../docs/AUDIT_REPORT_SPRINT03A.md)
