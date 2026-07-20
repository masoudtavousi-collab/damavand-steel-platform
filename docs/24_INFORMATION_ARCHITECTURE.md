# Enterprise Information Architecture

## Document Control

- **Document ID:** `docs/24_INFORMATION_ARCHITECTURE.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Information Architect
- **Approval Authority:** Founder
- **Version:** 0.2.0
- **Last Updated:** 2026-07-20
- **Last Review:** 2026-07-20
- **Review Cycle:** On business-information layer, content type, product, inquiry, representative, support, navigation, URL, search, ownership, or expansion change
- **Lifecycle:** Review
- **Source of Truth:** [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles), [ADR 0001](adr/0001-inquiry-first-commerce.md), [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md), and the Batch 05 product, taxonomy, attribute, and inquiry models
- **Dependencies:** [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md), [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), and [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)
- **Related Documents:** [Site Structure](25_SITE_STRUCTURE.md), [URL Architecture](26_URL_ARCHITECTURE.md), [Search and Discovery](27_SEARCH_AND_DISCOVERY.md), [Internal Linking Model](28_INTERNAL_LINKING_MODEL.md), [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md), and [SEO Strategy](11_SEO_STRATEGY.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, WP-FC-001 through WP-FC-005, PDM-001 through PDM-008, TAX-001 through TAX-008, INQ-001 through INQ-008, and IA-001 through IA-007
- **AI Compatibility:** AI-readable with explicit logical/physical, public/protected, approved/proposed, and no-implementation boundaries
- **Approval:** Pending Founder approval; no implementation authorization

## Purpose

Define the permanent logical organization of business information across products, knowledge, inquiry, representatives, support, landings, navigation, ownership, and future expansion without selecting a physical WordPress implementation.

## Scope and Boundary

This document defines information domains, layers, relationships, authority, and expansion rules. It does not create pages, menus, taxonomies, URLs, search indexes, representative profiles, forms, settings, schemas, plugins, templates, or code.

Exact Persian labels, public section names, taxonomy terms, menu order, URL slugs, page inventory, representative publication, and search behavior remain explicit Founder/domain/SEO/UX decisions.

## Information Architecture Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| IA-001 | Organize the platform as a graph of governed information objects with one canonical owner per fact and multiple controlled discovery paths. | Proposed pending Founder approval |
| IA-002 | Separate business, content, product, inquiry, representative, support, and landing layers while linking them through stable identities. | Proposed pending Founder approval |
| IA-003 | Keep entity identity independent of label, navigation placement, public URL, language, and external-system ID. | Proposed pending Founder approval |
| IA-004 | Assign one canonical public owner per search intent or information purpose; navigation and filters reference that owner rather than duplicate it. | Proposed pending Founder/SEO approval |
| IA-005 | Preserve contextual inquiry as the terminal commercial interaction across product, knowledge, landing, representative, and support journeys without public pricing. | Required by CP-005, CP-006, and ADR-0001 |
| IA-006 | Define logical information requirements before selecting WordPress storage, plugin, theme, menu, search, or URL configuration. | Required by CP-001 and CP-002 |
| IA-007 | Permit future languages, countries, business units, integrations, and information types only through registered ownership, relationships, lifecycle, navigation, URL, search, and migration review. | Proposed pending Founder approval |

## Architecture Principles

- One fact has one canonical authority; other surfaces reference it.
- Stable IDs outlive labels, slugs, hierarchy moves, and external mappings.
- Persian RTL and mobile use are structural constraints for navigation, labels, filters, search, inquiry, and support.
- Inquiry context survives movement between product, knowledge, landing, representative, and support content.
- Public information excludes price, price-derived claims, cart, checkout, payment, and transaction behavior.
- Navigation, URLs, search, filters, and internal links are separate views of the same governed information graph.
- Public, protected, and internal information are explicitly separated.
- Logical IA does not select a plugin, custom theme, database model, or implementation mechanism.
- Growth extends registered node and relationship types; it does not create parallel uncontrolled structures.

## Knowledge-Driven IA

The platform is modeled as governed nodes connected by explicit relationships:

| Node family | Examples from approved reference models | Canonical authority |
| --- | --- | --- |
| Business identity | Company information, policies, contact context | Approved business/content owner |
| Product | Canonical Catalog, Platform, Family, Series, Variant Rules, and derived SKU; downstream Parent Product and Variation presentation constructs | Product Repository authority with versioned commerce mappings |
| Classification | Taxonomy term, attribute definition/value, Collection, Product Tag | Taxonomy and Attribute models |
| Knowledge | Knowledge Page, Article, FAQ, guide-like educational content | Approved content owner; exact types pending |
| Landing | Product, taxonomy, application/use-case, industry, brand, campaign, or curated SEO landing | Single approved landing owner per intent |
| Inquiry | General, Product, Multi-product, or Project Inquiry and Inquiry Line | Inquiry Data Model |
| Customer | Governed Customer identity and submission snapshots | Inquiry Data Model |
| Representative | Governed representative identity, scope, contact/routing context | Exact public model pending Founder decision |
| Support | Inquiry help, support guidance, approved technical-document access, policy guidance | Support/content owner pending assignment |
| Document and media | Media Set item and Technical Document | Product Data Model and access classification |

Allowed relationship vocabulary includes `contains`, `classifies`, `describes`, `varies by`, `supports`, `applies to`, `represented by`, `links to`, `inquiry for`, `related to`, `replaces`, and `mapped to`. Compatibility, suitability, authority, and representation must never be inferred from proximity or shared labels.

## Business Information Layers

| Layer | Responsibility | Boundary |
| --- | --- | --- |
| Identity and trust | Company identity, policies, governance-visible public commitments, contact context | Does not duplicate product or technical authority |
| Catalog and capability | Products, governed specifications, availability context, documents, related entities | WooCommerce/product authority; no public pricing |
| Context and demand | Application/Use Case, Industry, Material, Brand, curated landing, and approved campaign context | References canonical terms and products; one SEO owner |
| Knowledge and education | Durable explanations, articles, FAQs, guides, and supporting technical knowledge | Educational; no unsupported technical or commercial claims |
| Inquiry and engagement | General, Product, Multi-product, and Project inquiry entry and confirmation context | Non-transactional; protected customer data |
| Representation and service | Representative discovery/routing context and support pathways | Public scope, ownership, privacy, and routing pending approval |
| Operational and integration | Internal lifecycle, ownership, CRM/ERP/CentralSteel mappings, audit evidence | Not a public navigation layer |

## Content Layers

1. **Foundation content:** stable company, contact, policy, and support-entry information.
2. **Catalog content:** canonical Family/Series context plus downstream parent/variation presentation, approved specifications, media, and documents.
3. **Context content:** application/use-case, industry, material, finish, brand, Collection, and approved SEO landing context.
4. **Knowledge content:** educational/reference content that links back to canonical products and classifications.
5. **Engagement content:** inquiry guidance and contextual inquiry entry without pricing or purchase language.
6. **Operational content:** protected/internal routing, ownership, review, integration, and audit information.

The layers describe responsibility, not WordPress post types or page-builder templates.

## Product Layers

```text
Product discovery
  -> Catalog
      -> Platform
          -> Family
              -> Series
                  -> Variant Rules
                      -> governed product selection
                          -> optional Parent Product / Variation commerce presentation
                              -> Contextual Inquiry
```

- Catalog, Platform, Family, Series, and Variant Rules are canonical repository concepts. SKU is derived only after governed modeling.
- Parent Product and Variation are downstream commerce or presentation constructs. They reference canonical identities and never own canonical Product truth.
- A Variable Parent Product may own one public presentation page, but that page ownership does not make its WooCommerce, Parent, Variation, slug, or SKU identifier canonical repository identity.
- Variations provide selectable context and do not automatically become independent canonical pages or repository entities.
- Categories, attributes, filters, knowledge, landings, and representative scope link to products; they do not duplicate product-master facts.
- Product lifecycle, stock state, inquiry eligibility, SEO eligibility, and public visibility remain separate decisions.

## Inquiry Layers

| Layer | Information responsibility |
| --- | --- |
| Entry context | Source page/entity, inquiry type, language, device class when permitted, and campaign context when approved |
| Requirement context | Free requirements, structured fields, project context, product lines, quantity/unit, and approved attachments |
| Customer context | Submission snapshot, governed Customer relationship, consent evidence, and approved contact channel |
| Routing context | Queue/representative assignment, rule version, reason, and fallback |
| Follow-up context | Inquiry State, Sales Follow-up Status, and CRM Synchronization Status as separate authorities |
| Confirmation context | Human-safe reference and next-step guidance without price, quote, transaction, or delivery promise |

Every public journey may end in an inquiry path, but no content node must fabricate product, customer, routing, or commercial facts to support it.

## Representative Layers

| Layer | Purpose | Boundary |
| --- | --- | --- |
| Representative discovery | Optional public directory or contextual list | Publication is pending Founder/privacy/Sales approval |
| Representative profile | Approved identity, scope, service context, languages/regions when approved, and inquiry action | No personal data, territory, certification, availability, or guarantee may be inferred |
| Representative relationship | Links representative scope to approved product, region, application/use case, industry, or support context | Relationship must be explicit and reviewed |
| Inquiry routing | Protected assignment and fallback information | Not public search or SEO content |
| Operational record | Internal status, workload, notes, permissions, and audit history | Protected; outside public IA |

Representative navigation and search remain conditional until public profile scope, ownership, privacy, lifecycle, and routing authority are approved.

## Support Layers

- Support entry and orientation.
- Inquiry help and submission guidance.
- Approved technical-document discovery and protected-access guidance.
- FAQ and troubleshooting knowledge when approved.
- Contact and escalation context without invented service levels.
- Privacy, consent, accessibility, and other approved policy guidance.
- Representative-assisted support only within approved scope.

Support does not become a transaction, public quote, warranty promise, technical certification, or substitute for product/inquiry authority.

## Landing Page Hierarchy

```text
Platform entry
  -> Domain hub
      -> Canonical entity or intent landing
          -> Supporting product/knowledge/support nodes
              -> Contextual inquiry
```

Landing types may include Product Family, approved taxonomy, Application/Use Case, Industry, Brand, Collection, campaign, or curated SEO intent only when their source identity, owner, audience, inclusion rule, canonical, lifecycle, maintenance obligation, and inquiry purpose are approved.

No landing type is automatically indexable. SEO Landing Categories do not authorize duplicate pages or taxonomies.

## Category Hierarchy

- Family is the canonical governed product grouping within a Platform.
- Series is the canonical structural subdivision that receives approved Variant Rules.
- Product Family, Product Group, and Product Type may appear only in a documented legacy, navigation, or commerce-adapter mapping.
- Material, Alloy, Application/Use Case, Industry, Finish, Brand, Collection, Product Tag, and SEO Landing classifications retain the purposes and overlap controls in the Taxonomy Model.
- Category navigation never changes canonical product identity or creates new attribute values.
- Exact category terms, depth, labels, and public hierarchy remain unapproved.

## Product Hierarchy

The canonical Product Repository hierarchy is exactly `Catalog → Platform → Family → Series → Variant Rules → SKU`, as settled by PDM-001 and the Founder decision dated 2026-07-20. Information architecture may expose shallower navigation and downstream Parent/Variation views for usability, but it must not delete, reorder, reinterpret, or replace the canonical hierarchy.

## Knowledge Hierarchy

```text
Knowledge Center
  -> Governed topic or audience path (pending approval)
      -> Approved content type
          -> Knowledge item
              -> Canonical classifications/products/support/inquiry
```

Topics and content types require purpose, owner, lifecycle, audience, canonical behavior, and non-duplication review. Product, taxonomy, and technical facts are referenced from their authorities; knowledge content does not become product master data.

## Document Hierarchy

| Access layer | Document purpose | Discovery boundary |
| --- | --- | --- |
| Public | Approved technical/marketing/support documents safe for unrestricted access | May link from canonical product or knowledge owner |
| Protected | Documents available only through approved authenticated or inquiry-assisted access | Excluded from public search, indexation, and open media paths |
| Internal | Review, commercial, operational, personal, integration, or audit documents | Not part of the public site tree |

Document type, version, language, owner, reviewer, product applicability, replacement, access class, and expiry are explicit. Repository governance documents are outside the business-platform document hierarchy.

## Navigation Philosophy

- Offer task-oriented routes: understand, discover, compare governed facts, find support, and inquire.
- Keep primary mobile navigation shallow; deeper structures use progressive disclosure.
- Persian RTL labels and direction are native, not post-processing.
- Preserve location and context across search, filter, product, knowledge, representative, and inquiry transitions.
- Do not expose empty, duplicate, unowned, unapproved, protected, or non-canonical destinations.
- Menus reference governed nodes and never become a second hierarchy authority.

## Information Ownership

| Information concern | Canonical owner source | Assignment status |
| --- | --- | --- |
| Canonical Product identities, hierarchy, and rules | Product Repository models | Operational role pending Founder decision; WooCommerce is a consumer only |
| Parent Product and Variation presentation | Approved commerce-adapter mapping | Operational role pending Founder decision; no canonical Product ownership |
| Taxonomy and attribute facts | Taxonomy/Attribute models | Operational role pending Founder decision |
| Knowledge and editorial content | Content governance | TODO (Founder Decision Required) |
| Landing intent and indexation | SEO governance | TODO (Founder Decision Required) |
| Inquiry and Customer data | Inquiry Data Model | Operational roles pending Founder/privacy/Sales decision |
| Representative identity and public scope | Representative governance | TODO (Founder Decision Required) |
| Support information | Support/content governance | TODO (Founder Decision Required) |
| URLs, redirects, navigation, search, and internal linking | IA/SEO governance | TODO (Founder Decision Required) |

One role may hold multiple assignments, but one concern must not have competing authorities.

## Authority Flow

```text
Core Project Principles + ADR 0001
  -> Canonical Product and Knowledge Repository authority
      -> approved reference and commerce-adapter models
          -> Enterprise Information Architecture
              -> Site Structure + URL Architecture
              -> Search and Discovery + Internal Linking Model
                  -> future configuration and validation evidence
```

The flow transfers constraints, not approval. WordPress, WooCommerce, Parent/Variation presentation, site, URL, search, navigation, or linking documents cannot override Product, Knowledge, taxonomy, inquiry, privacy, SEO, or governance authority.

## Future Expansion Rules

Every new information type, taxonomy, language, country, business unit, representative model, content type, landing type, or integration must document:

- Purpose, audience, owner, reviewer, approval authority, lifecycle, and source of truth.
- Stable identity and relationships to existing nodes.
- Canonical, URL, navigation, search, filter, internal-link, and inquiry behavior.
- Persian RTL, mobile, accessibility, privacy, security, performance, and SEO impact.
- Duplicate-authority and migration analysis.
- Public, protected, or internal access classification.
- Plugin/configuration capability review before custom development.
- Rollback or deprecation path without breaking stable identities.

Expansion must not introduce public pricing, a transaction path, a custom theme, Gravity Forms, LiteSpeed Cache, or unauthorized AI behavior.

## Founder Decisions

- Approve, revise, or reject IA-001 through IA-007.
- Assign owners for knowledge, landing, representative, support, URL, navigation, search, and internal-link governance.
- Approve whether representative discovery and profiles are public.
- Approve knowledge topics/types and landing types without inventing taxonomy terms.
- Approve public/protected/internal document discovery boundaries.

## Open Questions

- Which public business-information domains and top-level labels are approved?
- Which knowledge types and topic paths are needed?
- Are representative directory/profile pages public, and what data and relationships may they expose?
- Which landing types may be indexable and who owns each intent?
- Which support pathways and document access classes are public?
- Who owns cross-domain IA, navigation, URL, search, and internal-link decisions?

## Approval Status

Review. The logical information architecture is proposed for Founder review. It does not authorize WordPress configuration, content creation, page creation, taxonomy creation, URLs, menus, search, plugins, templates, or implementation.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.2.0 | 2026-07-20 | Reconciled Information Architecture with the canonical Product Repository hierarchy and downstream commerce/presentation mappings; documentation only. |
| 0.1.0 | 2026-07-03 | Initial Batch 06 enterprise information architecture; documentation only. |

## Related Documents

- [Site Structure](25_SITE_STRUCTURE.md)
- [URL Architecture](26_URL_ARCHITECTURE.md)
- [Search and Discovery](27_SEARCH_AND_DISCOVERY.md)
- [Internal Linking Model](28_INTERNAL_LINKING_MODEL.md)
- [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md)
- [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md)
- [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md)
- [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| IA-001–IA-007 | This document, CP-001–CP-010, ADR-0001, WP-FC/WP-ARC, PDM/TAX/ATT/INQ reference models | Documents 25 through 28 | Approved inventory, ownership, relationship, navigation, URL, search, linking, mobile RTL, no-price, and inquiry validation |

Implementation status: `Not authorized`.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Information Architecture Reading Path](READING_ORDER.md#information-architecture-reading-path)
