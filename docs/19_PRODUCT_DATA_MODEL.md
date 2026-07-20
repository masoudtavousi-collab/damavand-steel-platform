# Enterprise Product Data Model

## Document Control

- **Document ID:** `docs/19_PRODUCT_DATA_MODEL.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.3.0
- **Last Updated:** 2026-07-20
- **Last Review:** 2026-07-20
- **Review Cycle:** On product hierarchy, entity, ownership, lifecycle, taxonomy, attribute, inquiry, CRM, ERP, or Founder-decision change
- **Lifecycle:** Review
- **Source of Truth:** [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles), [ADR 0001](adr/0001-inquiry-first-commerce.md), and [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#founder-constraints-and-decision-sources)
- **Dependencies:** [Business Rules](03_BUSINESS_RULES.md) and [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md)
- **Related Documents:** [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md), [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md), [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md), and [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)
- **Traceability:** CP-001 through CP-010, WP-FC-001, WP-FC-004, WP-FC-005, WP-ARC-007 through WP-ARC-009, and PDM-001 through PDM-008
- **AI Compatibility:** AI-readable with explicit unknown-value and no-implementation boundaries
- **Approval:** Pending Founder approval

## Purpose

Define the logical enterprise Product Repository entities, responsibilities, relationships, identifiers, lifecycle boundaries, and downstream commerce mappings required for a Persian RTL, inquiry-first platform.

## Scope

This model defines product data concepts only. It does not define database tables, WordPress fields, WooCommerce settings, products, taxonomy terms, imports, plugin brands, prices, UI, or code.

## Governing Rules

- Inquiry First and No Public Pricing govern all catalog and inquiry data.
- The canonical repository hierarchy is `Catalog → Platform → Family → Series → Variant Rules → SKU`.
- Variable Parent Product and Variation are downstream commerce/presentation constructs, not canonical repository identity layers.
- Plugin First and Configuration First govern future physical implementation.
- Mobile First and Persian RTL govern labels, editing, filtering, and public presentation.
- WordPress Admin must remain manageable for the non-programmer Founder.
- No Custom Theme, Gravity Forms, LiteSpeed Cache, or Phase 1 AI capability may be introduced.

## Data Model Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| PDM-001 | Use `Catalog → Platform → Family → Series → Variant Rules → SKU` as the canonical repository hierarchy. Product Family → Product Group → Product Type → Variable Parent Product → Variation may exist only as a legacy, presentation, or commerce-adapter mapping. | `APPROVED` by explicit Founder decision dated 2026-07-20 |
| PDM-002 | Give every governed entity a stable internal ID independent of Persian labels, slugs, WooCommerce IDs, Parent IDs, Variation IDs, SKUs, and external system IDs. | Exclusion of those downstream identifiers from canonical identity is `APPROVED`; the stable-ID contract and registry design remain proposed pending separate approval |
| PDM-003 | Govern reusable terms through canonical taxonomy and attribute registries instead of free-text duplication. | Proposed pending Founder approval |
| PDM-004 | Record ownership, lifecycle, visibility, validation, and change evidence for product data. | Proposed pending Founder approval |
| PDM-005 | Reserve versioned external identifiers and mappings for future ERP, CRM, and CentralSteel compatibility without making them current authorities. | Proposed pending Founder approval |
| PDM-006 | Use a product lifecycle that is separate from document lifecycle and explicitly controls review, publication, suspension, discontinuation, restoration, and archival. | Proposed pending Founder/Product approval |
| PDM-007 | Require an assigned accountable owner and reviewer for each governed product-data concern before operational approval. | Proposed pending Founder approval |
| PDM-008 | Treat the Draft Product Data Strategy as non-governing context until its Purpose, Scope, and disposition are approved. | Evidence-based authority clarification; final disposition pending Founder approval |

## Product Hierarchy

```text
Catalog
  -> Platform
      -> Family
          -> Series
              -> Variant Rules
                  -> SKU
```

This hierarchy is canonical and authoritative. Catalog, Platform, Family, Series, and Variant Rules are repository concepts. SKU is derived only after governed product modeling; it is not the canonical identity of a preceding entity. Exact Family/Series values, Variant Rules, valid combinations, and derived SKUs still require evidence and approval.

### Downstream Commerce and Legacy Mapping

```text
Canonical Family / Series / Variant Rules
  -> optional Product Family / Product Group / Product Type presentation mapping
      -> Variable Parent Product
          -> Variation
```

This mapping supports WooCommerce and other presentation surfaces only. It may be shallower, relabeled, or implementation-specific, but it must preserve stable canonical references and cannot replace, reorder, or redefine the repository hierarchy.

## Core Entity Definitions

| Entity | Definition | Required relationships and boundaries |
| --- | --- | --- |
| Catalog | Root governed product-domain container | Contains approved Platforms; not a menu, WordPress category, or public URL by definition |
| Platform | Governed product-platform context within a Catalog | Contains approved Families and preserves ecosystem ownership across consumers |
| Family | Canonical grouping for a coherent product family | Belongs to one Platform; has a stable repository identity independent of presentation labels and commerce IDs |
| Series | Canonical structured subdivision of a Family | Belongs to one Family; controls the applicable modeling context without becoming a WooCommerce product type |
| Variant Rules | Governed axes, constraints, evidence, and valid-combination rules for a Series | Belongs to one Series; Cartesian possibility never proves validity or availability |
| SKU | Derived commercial/operational identifier after governed modeling | Requires an approved SKU policy and valid governed product record; never substitutes for canonical entity identity |
| Product Family / Product Group / Product Type | Legacy or presentation grouping labels | May map to canonical Family/Series concepts only through an explicit versioned mapping; not canonical repository layers |
| Variable Parent Product / Parent Product | Downstream commerce or presentation entity holding shared display and inquiry context | References canonical Family/Series/Variant Rules; never owns canonical Product truth or public price authority |
| Variation | Downstream selectable commerce/presentation projection | References one approved governed combination; its ID and SKU are not canonical Product entity identities |
| Attribute | Controlled property used for specification, variation, filtering, integration, or presentation | Defined by the Product Attribute Model; free-text use requires explicit exception |
| Material | Canonical material classification applicable to product specification and discovery | References one controlled Material term; does not duplicate Material Category authority |
| Alloy | Canonical alloy designation or family within an approved Material context | Requires qualified technical review and stable mapping; no alloy values are approved here |
| Finish | Controlled surface-finish specification | Uses the canonical Finish registry; exact terms require domain review |
| Color | Controlled appearance value only where meaningful and approved | Must not substitute for Finish or coating specification |
| Size | Human-facing composite size representation derived from structured dimensions where possible | Must not be the sole source when Diameter, Thickness, Length, or other dimensions apply |
| Diameter | Structured dimensional value with unit and dimensional context | Numeric/value policy and applicable product types require approval |
| Thickness | Structured dimensional value with unit and tolerance context when applicable | Numeric/value policy and applicable product types require approval |
| Length | Structured dimensional value with unit and supply-form context | Numeric/value policy and applicable product types require approval |
| Unit | Controlled unit of measure associated with a value, quantity, stock representation, or inquiry line | Unit vocabulary and conversion authority require approval; labels are not conversion logic |
| Brand | Canonical brand/manufacturer identity when approved for catalog use | Uses one Brand registry shared with taxonomy and SEO landing references |
| Quality Level | Controlled commercial or quality classification with an explicit definition and reviewer | Must not imply an unverified standard, grade, certification, or warranty |
| Stock State | Governed availability representation independent of public pricing | Uses the proposed stock-state policy below; no delivery promise is implied |
| Inquiry State | Governed lifecycle of a non-transactional request | Defined by the Inquiry Data Model; not a WooCommerce order status |
| Media Set | Governed collection of product images and visual assets | Has owner, rights, accessibility metadata, role, order, and parent/variation applicability |
| Technical Documents | Versioned datasheets, certificates, drawings, guides, or approved technical files | Has document type, version, owner, review status, access class, and product relationship |
| SEO Data | Approved search metadata and indexation references for a product entity | SEO owner governs titles, descriptions, canonicals, schema, and landing ownership; no price schema |
| CRM Data | Future inquiry/customer/routing references required for CRM handoff | CRM is not selected; product master content is not duplicated into CRM authority |
| ERP Compatibility | Future external IDs, attribute codes, units, stock mappings, and synchronization metadata | ERP is not selected; mappings are versioned and inactive until approved |

## Entity Identity

Every governed entity must support:

- Stable internal ID.
- Persian display label where applicable.
- English internal key where required by integration or administration.
- Lifecycle and visibility status.
- Owner, reviewer, approval source, and last review.
- Created/updated evidence without treating timestamps as authority.
- Optional external-system identifiers scoped by system and mapping version.

Labels, slugs, WooCommerce IDs, Parent IDs, Variation IDs, SKUs, and external IDs may change under governance; the stable internal ID must not be repurposed.

## Relationship Model

| Relationship | Direction | Rule |
| --- | --- | --- |
| Contains | Catalog/Platform/Family/Series to canonical child | Child has one approved structural parent unless an explicit multi-classification decision exists |
| Governed By | Series to Variant Rules | Axes, constraints, evidence, and valid combinations are explicit and versioned |
| Derives | Governed Product record to SKU | Derivation occurs only after approved modeling and SKU policy |
| Maps To | Canonical entity/rule to commerce or presentation entity | Mapping is downstream, versioned, and cannot transfer canonical ownership |
| Varies By | Commerce Parent to global Attribute | Axis must map to approved canonical Variant Rules |
| Has Variation | Commerce Parent to Variation | Only governed, evidence-backed combinations may be exposed for inquiry |
| Classified By | Product to taxonomy term | One canonical term registry per classification concept |
| Described By | Product/Variation to attribute value | Value conforms to type, unit, source, and allowed-value policy |
| Uses Media | Product/Variation/Content to Media Set item | Applicability and ordering are explicit |
| Supported By | Product/Variation to Technical Document | Document version, access, and applicability are explicit |
| Related To | Product to Product | Relationship type such as alternative or accessory must be named; compatibility is never inferred |
| Referenced By | Product/Variation to Inquiry line | Inquiry stores stable IDs plus a submission-time label/specification snapshot |
| Mapped To | Internal entity to ERP/CRM/CentralSteel identity | Mapping is system-specific, versioned, and inactive until approved |

## Proposed Product Lifecycle

Product lifecycle is independent of the document lifecycle in [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md) and independent of Stock State. The following state machine is proposed for product records only:

| Product state | Meaning | Allowed next states | Public boundary |
| --- | --- | --- | --- |
| `draft` | Product data is incomplete or being prepared | `review` | Admin-only |
| `review` | Product data awaits authorized product/domain review | `draft`, `approved` | Not public or indexable |
| `approved` | Required product evidence and approvals are recorded | `review`, `suspended`, `discontinued` | May be public only when visibility, inquiry eligibility, stock, and SEO rules also permit |
| `suspended` | Publication or inquiry eligibility is temporarily withdrawn without ending the product identity | `review`, `approved`, `discontinued` | Hidden or informational behavior requires approved Product/SEO policy |
| `discontinued` | The product is no longer actively supplied | `review`, `archived` | Historical, replacement, redirect, and inquiry behavior require approved Product/Sales/SEO policy |
| `archived` | The record is retained for history and integration references but is not operational | `review` only through an approved restoration record | Not public unless a separately approved historical-content policy applies |

Every transition records the prior state, next state, reason, actor, approval source, and timestamp. Restoration always returns a product to `review`; it never restores public visibility automatically. Exact transition owners, required evidence, public behavior, and whether all states are needed remain Founder/Product/Sales/SEO decisions.

Stock State describes availability and does not change product lifecycle automatically. Inquiry State describes a request and must never be used as product lifecycle.

## Proposed Stock State Model

| Internal state | Meaning | Public/inquiry boundary |
| --- | --- | --- |
| `in_stock` | Availability is currently represented as available by the approved catalog authority | May permit inquiry; no price or delivery promise |
| `limited` | Availability is constrained or requires confirmation | Inquiry remains available with confirmation language |
| `supply_after_order` | Not held as immediately available but may be sourced or produced after an accepted commercial request | Inquiry remains available; must not display as in stock, backorder purchase, or guaranteed lead time |
| `temporarily_unavailable` | Currently unavailable for supply inquiry unless Sales authorizes an exception | Public inquiry behavior requires approved policy |
| `discontinued` | No longer actively supplied | Hidden or informational behavior and alternatives require approval |

These are proposed internal states. Persian labels, WooCommerce mapping, visibility, inventory source, and transition authority require Founder and Sales/Operations approval.

## Proposed Inquiry State Reference

Product data may expose only a summarized inquiry eligibility indicator. The authoritative inquiry lifecycle belongs to [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md); product records must not store duplicated inquiry case status.

## Media Set Model

Each Media Set item identifies:

- Stable media ID and role: primary, gallery, detail, diagram, application, packaging, or document preview.
- Parent/variation applicability.
- Persian alt text and optional caption.
- Rights, source, owner, approval, accessibility review, and expiry when applicable.
- Original and derivative relationship without naming an implementation storage schema.
- Public/protected access class.
- Sort order and replacement history.

## Technical Document Model

Each Technical Document identifies document ID, type, Persian and English title as applicable, version, issue date, owner, reviewer, approval status, access class, language, applicable products/variations, standards reference, replacement relationship, and checksum or integrity evidence when later implemented.

No certificate, standard, warranty, guarantee, or compliance claim is approved by this model.

## SEO Data Boundary

- SEO Data references the canonical product and taxonomy entities; it does not copy product authority.
- One approved landing owner exists per search intent.
- Canonical, indexation, schema, breadcrumb, and redirect ownership follow WordPress Enterprise Architecture.
- Public structured data must not contain price, offer, cart, checkout, payment, or unsupported availability claims.
- Exact URLs, Persian/English slug policy, titles, descriptions, and indexation remain SEO/Founder decisions.

## CRM and Future ERP Compatibility

- CRM receives inquiry and product references, not product-master ownership by default.
- ERP compatibility reserves stable IDs, system-specific external IDs, units, attribute codes, stock states, mapping versions, and synchronization evidence.
- Source-of-truth direction is decided per field before any integration.
- Integrations require conflict policy, idempotency, retries, reconciliation, access control, and audit evidence.
- No ERP, CRM, API, connector, provider, database mapping, or synchronization is implemented here.

## Operational Ownership Matrix

The following roles must be assigned before the corresponding data can receive operational approval. This matrix records accountability requirements; it does not assign people or invent organizational roles.

| Governed concern | Accountable owner | Required reviewer or approval context |
| --- | --- | --- |
| Canonical Product hierarchy | Founder | Hierarchy settled on 2026-07-20; Family/Series values and Variant Rules still require qualified product/domain review |
| Commerce parent/variation mapping and lifecycle | TODO (Founder Decision Required) | Founder, product/domain, and commerce-adapter review |
| Taxonomy terms, Collections, Product Tags, and mappings | TODO (Founder Decision Required) | Founder, domain, and SEO review as applicable |
| Attribute definitions, values, units, profiles, and Size derivation | TODO (Founder Decision Required) | Founder and qualified steel-domain review |
| Media Sets and rights/access metadata | TODO (Founder Decision Required) | Content/accessibility/security review as applicable |
| Technical Documents and technical claims | TODO (Founder Decision Required) | Qualified technical reviewer and approval authority |
| SEO Data and landing ownership | TODO (Founder Decision Required) | Founder and SEO review |
| Inquiry data and workflow | TODO (Founder Decision Required) | Founder, Sales, security, and privacy/legal review |
| Sales follow-up and routing | TODO (Founder Decision Required) | Founder and Sales review |
| CRM mapping and synchronization | TODO (Founder Decision Required) | Founder, Sales, security, and integration review |
| ERP mapping, stock authority, and reconciliation | TODO (Founder Decision Required) | Founder, Operations, security, and integration review |
| CentralSteel mapping | TODO (Founder Decision Required) | Founder, domain, SEO, and integration review as applicable |

No implementation role, WordPress role, or repository author inherits these accountabilities automatically.

## Relationship to Product Data Strategy

[Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md) is a Draft placeholder with unresolved Purpose, Scope, and content. It is related context, not a governing dependency or authority source for this model. The Founder must decide whether that document will be completed, superseded, deprecated, or archived; this model does not make that decision.

## Administration and Data Quality

- Routine entity, relationship, label, media, and document maintenance must be manageable through supported WordPress Admin capabilities after an approved implementation design.
- Admin interfaces must use Persian-capable labels, clear help text, controlled selections, validation, preview, bulk review, and reversible workflows.
- Free-text duplication is rejected when a controlled value exists.
- Required fields and valid combinations vary by canonical Series and approved Variant Rules. A downstream Product Type/profile may project those rules but cannot own or invent them.
- Bulk operations require dry-run, validation report, stable-ID preservation, and approval before mutation.

## Founder Decisions

- PDM-001 and the downstream-ID exclusions in PDM-002 are settled by the explicit Founder decision dated 2026-07-20; the stable-ID contract and remaining proposal scope still require separate review.
- Approve exact canonical Family/Series values, Variant Rules, and any explicit mapping to Product Family/Product Group/Product Type/Parent/Variation constructs.
- Assign every role in the Operational Ownership Matrix.
- Approve product lifecycle, stock states, Persian labels, public messages, and transition authority.
- Approve the stable-ID, SKU, unit, external-ID, and data-retention policies.
- Decide the disposition of the Draft Product Data Strategy through the existing FD-PDS-01 through FD-PDS-03 decisions.

## Open Questions

- Which canonical Families and Series are approved, and which legacy/commerce labels map to them?
- Which dimensions, units, materials, alloys, finishes, colors, standards, brands, and quality levels apply through each Series' Variant Rules?
- Which stock source and state transitions are authoritative before ERP integration?
- Which product lifecycle states, transition owners, evidence, public behaviors, restoration rules, and archival rules are approved?
- Which documents and media may be public, protected, expired, or version-replaced?
- Which CRM, ERP, and CentralSteel mappings will be required in future phases?
- Who owns and reviews each concern in the Operational Ownership Matrix?
- Will Product Data Strategy be completed, superseded, deprecated, or archived?

## Approval Status

Review. The canonical hierarchy and identity distinction are Founder-approved within their exact scope. The remaining data-model proposals are not approved and this document does not authorize contracts, schemas, registries, Product records, WooCommerce configuration, database design, import, or implementation.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.3.0 | 2026-07-20 | Reconciled the Founder-approved canonical repository hierarchy and separated canonical identities from legacy/commerce Parent and Variation mappings; documentation only. |
| 0.2.0 | 2026-07-03 | Batch 05B remediation: explicit product lifecycle, ownership requirements, and Draft Product Data Strategy authority boundary; documentation only. |
| 0.1.0 | 2026-07-03 | Initial Batch 05 enterprise product data model; documentation only. |

## References

- [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md)
- [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md)
- [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md)
- [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md)
- [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Product Data Reading Path](READING_ORDER.md#product-data-and-woocommerce-reading-path)
