# Taxonomy Implementation Blueprint

## Document Control

- **Document ID:** `docs/40_TAXONOMY_IMPLEMENTATION.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Solution Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On taxonomy, attribute, term, hierarchy, URL, filtering, SEO, ownership, validation, or integration change
- **Lifecycle:** Review
- **Source of Truth:** [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md), [Information Architecture](24_INFORMATION_ARCHITECTURE.md), and [URL Architecture](26_URL_ARCHITECTURE.md)
- **Dependencies:** [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md), [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md), and [Search and Discovery](27_SEARCH_AND_DISCOVERY.md)
- **Related Documents:** [WooCommerce Configuration](38_WOOCOMMERCE_CONFIGURATION.md), [Custom Post Type Blueprint](39_CUSTOM_POST_TYPES.md), [Custom Fields Model](41_CUSTOM_FIELDS_MODEL.md), and [SEO Entity Model](34_SEO_ENTITY_MODEL.md)
- **Traceability:** CP-001 through CP-006, CP-010, TAX-001 through TAX-008, ATT-001 through ATT-007, WCM-004 through WCM-007, and TAXBP-001 through TAXBP-009
- **AI Compatibility:** AI-readable Blueprint; no AI feature, taxonomy, attribute, or term is authorized
- **Approval:** Pending Founder/domain/SEO/technical approval; no taxonomy configuration is authorized

## Purpose

Define the physical-mapping, ownership, hierarchy, administration, validation, and governance gates for approved taxonomies without creating taxonomies or terms.

## Scope and Boundary

The Product Taxonomy and Attribute models remain semantic authorities. This document proposes implementation mappings only. It does not approve vocabulary, labels, keys, slugs, hierarchy, URLs, filters, landing pages, indexation, terms, or registration mechanisms.

## Taxonomy Blueprint Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| TAXBP-001 | Maintain one canonical registry for each concept and prevent category/attribute/tag duplication. | Derived from TAX-001 through TAX-008 |
| TAXBP-002 | Use WooCommerce global attributes for specification dimensions and variation/filter axes approved by the Attribute Model. | Derived from WCM/ATT rules |
| TAXBP-003 | Use WooCommerce product categories for the approved hierarchical product browse structure only after exact hierarchy approval. | Proposed pending Founder/domain/SEO approval |
| TAXBP-004 | Map classification registries to native or plugin-managed taxonomies only when query, relationship, URL, and Admin requirements justify them. | Proposed pending Founder approval |
| TAXBP-005 | Keep Application and Use Case one logical classification until the governing terminology decision is resolved. | Required by TAX-007 |
| TAXBP-006 | Treat SEO landings as curated canonical projections, not a parallel taxonomy or automatically indexable term archive. | Derived from IA/SEO rules |
| TAXBP-007 | Prohibit uncontrolled Product Tags and mixed-script internal identifiers/slugs. | Derived from TAX governance |
| TAXBP-008 | Require stable term identity, labels/aliases, hierarchy, lifecycle, owner, usage, redirects, and external mappings. | Proposed pending Founder/domain approval |
| TAXBP-009 | Register or modify taxonomies only through an approved Plugin First/Configuration First owner after validation. | Required by CP-001 and CP-002 |

## Taxonomy Ownership Matrix

| Logical registry | Proposed platform mapping | Hierarchy | Variation/filter use | Public archive/SEO |
| --- | --- | --- | --- | --- |
| Product Family / Group / Type | WooCommerce product-category hierarchy or approved governed mapping | Pending exact hierarchy | Browse/filter only as approved | Pending canonical/indexation decision |
| Material | Global WooCommerce attribute and canonical term registry | Flat by default; exceptions require approval | Candidate variation/filter axis | Archive/landing not automatic |
| Alloy | Global WooCommerce attribute and canonical term registry | Relationship to Material; not an invented tree | Candidate variation/filter axis | Archive/landing not automatic |
| Finish | Global WooCommerce attribute and canonical term registry | Flat by default | Candidate variation/filter axis | Archive/landing not automatic |
| Brand | Global attribute or approved Brand taxonomy, one canonical registry | Flat by default | Filtering as approved; variation only if governed | Public Brand landing conditional |
| Use Case / Application | Approved custom/native taxonomy capability after terminology approval | Pending | Discovery filter only if approved | Curated landing conditional |
| Industry | Approved custom/native taxonomy capability | Pending | Discovery filter only if approved | Curated landing conditional |
| Collection | Curated grouping taxonomy only if governance and expiry exist | Pending | Not a product-specification axis | Indexation conditional |
| Product Tag | Disabled/unavailable by default pending explicit controlled use | Flat | Not a variation axis | No automatic archive |
| SEO Landing classification | Internal editorial relationship/metadata, not a duplicate product taxonomy | Not applicable | Not a variation axis | Landing owns approved intent |
| CentralSteel mapping | External mapping fields/relationships on canonical terms | External hierarchy does not replace local authority | Not directly public | Future integration only |

Exact physical mechanisms remain unapproved.

## Hierarchy and Relationships

- Hierarchy exists only where parent/child meaning is stable and approved; facets remain flat unless domain semantics require hierarchy.
- Material–Alloy, Product–Family/Group/Type, term–landing, term–content, and external-system mappings are typed relationships, not implied by names.
- A term belongs to one canonical registry and may have localized labels/aliases without duplicate identity.
- Attribute values do not become categories merely to create archives; categories do not become variation axes merely to create filters.

## Admin Workflow

1. Submit term request with concept, registry, Persian label, English internal key/slug proposal, definition, aliases, parent, owner, usage, evidence, and impact.
2. Search canonical registries and external mappings for duplicates.
3. Obtain domain approval; obtain SEO/URL approval for public or indexable behavior.
4. Validate affected products, variations, filters, URLs, landings, schema, content, imports, and integrations.
5. Create/change only through the future approved configuration owner.
6. Review use, stale/orphan state, aliases, redirects, and replacement evidence.

## Validation

- Unique stable identity and normalized internal key.
- Approved Persian label, definition, aliases, unit/format where relevant, and script policy.
- Correct registry and no category/attribute overlap.
- Valid parent without cycles; valid Product/Variation assignments.
- Approved variation/filter/search/SEO permissions.
- Public archive, canonical, URL, schema, and navigation behavior explicitly decided.
- Mobile/RTL Admin and front-end usability, import/export stability, and rollback evidence.

## Future Governance

Term creation, rename, merge, split, move, deprecate, replace, and archive actions require impact review across products, variations, URLs, redirects, filters, search, landings, content, schema, media/documents, and integrations. CentralSteel/ERP mappings never silently replace local canonical identity.

## Founder Decisions

- Approve, revise, or reject TAXBP-001 through TAXBP-009.
- Approve the physical mapping for each registry and exact Product Family/Group/Type hierarchy.
- Approve labels, keys, slug language, term values, hierarchy, filters, archives, landings, indexation, and external mappings.
- Assign domain, taxonomy, SEO/URL, technical configuration, and review owners.

## Open Questions

- Which registries map to product categories, global attributes, custom taxonomies, or internal relationships?
- What exact hierarchy, term set, label/key/slug policy, and Application/Use-Case name are approved?
- Which term views are public, filterable, searchable, indexable, or landing-backed?
- Which supported capability owns taxonomy registration, validation, term relationships, redirects, and import/export?

## Approval Status

Review. No taxonomy, attribute, term, category, key, slug, hierarchy, filter, archive, URL, landing, or WordPress/WooCommerce configuration is created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 08 taxonomy implementation Blueprint; documentation only. |

## Related Documents

- [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md)
- [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md)
- [Search and Discovery](27_SEARCH_AND_DISCOVERY.md)
- [SEO Entity Model](34_SEO_ENTITY_MODEL.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| TAXBP-001–TAXBP-009 | CP-001–CP-006, CP-010, TAX/ATT/WCM, IA/URL/SRCH/LINK/SEOENT rules | WooCommerce, CPT, fields, search/filter, SEO, import/export, and integration plans | Registry/mapping inventory, duplicate/cycle/link checks, domain/SEO approval, Persian RTL/mobile Admin tests, import/rollback evidence |

Implementation status: `Not authorized`.
