# Enterprise Entity Relationship Model

## Document Control

- **Document ID:** `docs/30_ENTITY_RELATIONSHIP_MODEL.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Information Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On entity, field, identity, ownership, lifecycle, relationship, content type, schema, integration, or repository-governance change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md), [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md), [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), and [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md)
- **Dependencies:** [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md), [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), and [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md)
- **Related Documents:** [Content Types](32_CONTENT_TYPES.md), [Schema.org Strategy](31_SCHEMA_ORG_STRATEGY.md), [Media Strategy](33_MEDIA_STRATEGY.md), [SEO Entity Model](34_SEO_ENTITY_MODEL.md), and [Repository Metadata Standard](REPOSITORY_METADATA.md)
- **Traceability:** PDM-001 through PDM-008, TAX-001 through TAX-008, ATT-001 through ATT-007, INQ-001 through INQ-008, IA-001 through IA-007, CONTENT-001 through CONTENT-008, and ERM-001 through ERM-008
- **AI Compatibility:** AI-readable entity registry with explicit canonical authority, relationship, lifecycle, optionality, and expansion boundaries
- **Approval:** Pending Founder/domain/governance approval; no storage or implementation authorization

## Purpose

Provide one logical registry of the business-platform and repository-governance entities named by the current architecture, including their purpose, owner source, lifecycle, relationships, required/optional fields, constraints, and future-expansion boundary.

## Scope and Boundary

This is a conceptual relationship model. It does not create database tables, WordPress post types, taxonomies, custom fields, users, records, schema markup, APIs, content, or configuration.

Entity names describe logical responsibilities. A physical platform object may support one or more logical entities only after a separate approved mapping. No unlisted noun becomes an entity merely because it appears in content.

## Entity Model Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| ERM-001 | Give every governed entity a stable type and internal identity independent of labels, URLs, SKUs, language, WordPress IDs, and external IDs. | Proposed pending Founder approval |
| ERM-002 | Assign one canonical authority and lifecycle source per entity type; projections and references cannot become competing masters. | Proposed pending Founder approval |
| ERM-003 | Represent relationships as typed, directional, owned, and evidence-backed records rather than inferred proximity. | Proposed pending Founder/domain approval |
| ERM-004 | Separate business entities, content entities, media/document entities, engagement entities, semantic projections, and repository-governance entities. | Proposed pending Founder approval |
| ERM-005 | Require minimum identity, ownership, lifecycle, source, relationship, access, language, and review fields appropriate to each entity. | Proposed pending Founder approval |
| ERM-006 | Preserve public/protected/internal boundaries and exclude pricing, customer, inquiry, routing, and governance data from unauthorized projections. | Proposed pending Founder/security/privacy approval |
| ERM-007 | Add entity types only through purpose, non-duplication, authority, lifecycle, field, relationship, migration, and consumer review. | Proposed pending Founder approval |
| ERM-008 | Keep the conceptual model platform-independent and defer physical mapping to Configuration First and Plugin First review. | Required by CP-001 and CP-002 |

## Common Entity Contract

Every governed entity requires, as applicable:

- Stable entity ID and entity type.
- Canonical authority/source and accountable owner.
- Lifecycle status, reviewer, approval source, version/revision evidence, and last review.
- Persian display label/title when public or Admin-facing; stable internal key when needed.
- Language/locale and public/protected/internal access class.
- Typed relationships using stable target IDs.
- Canonical URL only when the entity is approved for a public destination.
- External IDs scoped by system/version and never substituted for internal identity.
- Created/updated evidence without treating timestamps as authority.

Optional fields are permitted only when their purpose, source, validation, privacy, and consumer are defined.

## Product and Classification Entities

| Entity | Purpose | Owner | Lifecycle | Relationships | Required fields | Optional fields | Constraints | Future expansion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Product | Abstract governed catalog offering | Product authority | Product lifecycle | Family/Group/Type, parent/variation, taxonomy, attributes, media, documents, inquiry | ID, type, owner, lifecycle, source | External mappings, related products | No public-price or transaction authority; physical form is Variable Parent/Variation | New product forms require superseding product-model decision |
| Product Family | Highest governed catalog grouping | Product/taxonomy owner pending | Taxonomy/product hierarchy lifecycle | Contains Groups/Types/Products | ID, label, key, definition, owner, lifecycle | Parent/external mapping, landing | Exact values/hierarchy unapproved; not automatically a URL | Future mappings/localizations by stable ID |
| Product Group | Optional intermediate grouping | Product owner pending | Product hierarchy lifecycle | Family parent; contains Types | ID, label, definition, parent, owner | External mapping, landing | Optional per approved family; no invented levels | Additional depth requires hierarchy approval |
| Product Type | Structural product class and attribute-profile owner | Product/domain owner pending | Product hierarchy lifecycle | Family/Group parent, products, attribute profile | ID, label, definition, parent, profile, owner | SEO/content relationships | Not WooCommerce product_type by definition | New types require domain/profile/migration review |
| Variable Parent Product | Canonical public/shared product entity | Product owner pending | Product lifecycle | Type, Variations, taxonomy, media, documents, knowledge, inquiry | ID, title, type, lifecycle, owner, valid variation policy | SEO data, external IDs, related products | Canonical product; no public price/cart/checkout | Future channels reference stable ID |
| Variation | Valid selectable supplied configuration | Product/operations owner pending | Product lifecycle subordinate to parent | Exactly one Parent, approved attributes, SKU, stock, inquiry line | ID, parent ID, valid combination, lifecycle | SKU, stock, media/document override, external ID | Non-canonical public entity by default; no price authority | Independent canonical only by approved exception |
| Taxonomy | Governed classification registry | Taxonomy owner pending | Taxonomy governance lifecycle | Contains Terms/Categories; classifies entities | ID, purpose, owner, hierarchy rule, lifecycle | Public mechanism, external mapping | One canonical registry per concept | New taxonomy requires non-duplication/SEO/migration review |
| Category | Navigational/classification term instance | Taxonomy owner pending | Canonical term lifecycle | Taxonomy, parent/children, classified entities, landing | ID, taxonomy ID, label, key, definition, owner, lifecycle | Slug, synonyms, external IDs | Does not duplicate attribute authority; not automatically indexable | Localized labels and mappings by stable ID |
| Taxonomy Term | Generic controlled term instance | Taxonomy owner pending | Canonical term lifecycle | Taxonomy, synonyms, entities, external mappings | ID, taxonomy ID, label, definition, owner, lifecycle | Parent, slug, SEO owner | No silent duplicate or uncontrolled import creation | Versioned mappings and localization |
| Attribute | Reusable governed specification definition | Attribute owner pending | Attribute governance lifecycle | Product Types, values, products/variations | ID, label, key, definition, value type, owner, lifecycle | Unit, variation/filter/SEO flags | Flat by default; no uncontrolled local duplicates | Attribute-specific hierarchy only by approval |
| Attribute Value | Controlled or validated value of an Attribute | Attribute/domain owner pending | Value lifecycle | Attribute, products/variations, synonyms, external mappings | ID/value, attribute ID, source, status | Unit, precision, label, synonyms | Typed/unit-aware; no mixed units or silent synonyms | Localization and external mappings |
| Brand | Canonical manufacturer/brand identity | Brand/taxonomy owner pending | Canonical term lifecycle | Products, category/attribute projection, landing | ID, approved name, definition, owner | Logo, external IDs, landing | One identity across representations; claims require evidence | Organization mapping after review |
| Material | Canonical material specification/classification identity | Qualified domain owner pending | Attribute/term lifecycle | Products, Alloy context, category/attribute projection | ID, approved name, definition, owner | Codes, synonyms, landing | Category and attribute share identity; technical review required | External standards/mappings after approval |
| Alloy | Canonical alloy identity within approved Material context | Qualified domain owner pending | Attribute/term lifecycle | Material, products, external codes | ID, designation, Material context, owner | Synonyms, standard references | Exact notation/evidence required | External mappings after qualified review |
| Finish | Canonical surface-finish identity | Qualified domain owner pending | Attribute/term lifecycle | Products, category/attribute projection | ID, approved label, definition, owner | Synonyms, landing | Must not be confused with Color/coating/quality | Future technical codes/mappings |
| Collection | Time-governed curated grouping | Content/taxonomy owner pending | Start/review/end/renew lifecycle | Products/families/content | ID, purpose, owner, inclusion rule, dates/status | Landing, campaign relation | Not specification/taxonomy authority; non-indexable by default | New channels after intent/lifecycle review |
| Product Tag | Optional editorial discovery term | Editorial owner pending | Term review/deprecation lifecycle | Content/products as approved | ID, label, definition, owner, scope | Synonyms | Not hierarchy, filter, compatibility, specification, or SEO authority by default | Migrate to governed taxonomy/attribute if reuse warrants |

## Engagement and Organizational Entities

| Entity | Purpose | Owner | Lifecycle | Relationships | Required fields | Optional fields | Constraints | Future expansion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Inquiry | Canonical non-transactional request | Inquiry owner pending | Inquiry State | Customer snapshot/link, Lines, Project, source, routing | ID, type, source, requirements, contact/consent evidence, state | Attachments, campaign, project context | No public price, order, checkout, or contract | CRM mapping after approval |
| Inquiry Line | Product requirement within an Inquiry | Inquiry/Product owner pending | Parent Inquiry lifecycle | Inquiry, Parent Product, Variation, attributes | ID/order, inquiry ID, product context, quantity/unit or approved unknown | Notes, alternatives, stock snapshot | Submission snapshot; no price/order data | External line mapping after approval |
| Customer | Governed identity related to inquiries | Customer/privacy owner pending | Customer lifecycle pending | Inquiries, organization/person role, consent, CRM map | ID, party type/status, source, owner | Contacts, organization relationships, external IDs | No public profile; no automatic merge | Approved accounts/CRM later |
| Representative | Governed representative identity and scope | Founder/Sales/privacy owner pending | Representative lifecycle pending | Products, location, use case/industry, inquiries, organization | ID, approved identity, owner, lifecycle/access class | Public bio/contact/scope/languages | Public profile/search conditional; routing/workload private | Additional channels/regions by approval |
| Location | Governed place/service/project context | Location owner pending | Location lifecycle pending | Organization, Representative, Project, Inquiry | ID, type, approved label, jurisdiction/access class, owner | Address/geo/service scope | No public address or service-area claim without approval | Future countries/regions/localization |
| Project | Customer/business requirement context | Project/Sales/privacy owner pending | Project lifecycle pending | Customer, Inquiry, Location, products, documents, Installation | ID, source, owner, access class, status | Name, schedule, stage, specifications | Not a public case study or Schema entity by default | CRM/ERP/public case-study projection by approval |
| Installation | Installation context or governed product relationship | Qualified domain/Project owner pending | Installation lifecycle pending | Project, Location, Product, documents, Representative | ID, purpose/type, owner, source, access class | Schedule, evidence, related products | Not an approved service/content type; no safety/suitability claim inferred | Future service/workflow only by business/architecture decision |
| Organization | Canonical business/legal organization identity | Founder/legal owner pending | Organization lifecycle pending | Brand, Location, Person/Representative, documents | ID, approved name, identity source, owner | Legal identifiers, logo, contacts | Public projection and claims require approval | Future group/subsidiary/external identity mapping |
| Local Business | Conditional semantic/public projection of an approved Organization at an eligible Location | Founder/local/SEO owner pending | Projection lifecycle | Organization, Location, WebSite semantic entity | Source organization/location IDs, eligibility approval | Hours/contact/service area if verified | Not a separate master; no location is assumed | Additional locations only after local governance decision |

## Content, Media, and Document Entities

| Entity | Purpose | Owner | Lifecycle | Relationships | Required fields | Optional fields | Constraints | Future expansion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Content Item | Abstract governed content expression | Content owner pending | Content lifecycle | Type, sources, entities, media, language, canonical | ID, type, title/label, owner, source, lifecycle, language/access | Summary, SEO/navigation role | Does not replace source facts | New content types through CTYPE governance |
| Landing Page | Canonical owner for one approved intent | Content/SEO owner pending | Content/landing lifecycle | Intent, entities, products, knowledge, inquiry | ID, intent, audience, owner, source entities, lifecycle, canonical decision | Campaign dates, media | No duplicate intent; not automatically indexable | New landing types after cannibalization review |
| Knowledge Article | Durable explanatory or educational content | Content/domain owner pending | Content lifecycle | Topics, products, taxonomy, documents, inquiry | ID, title, purpose, audience, source, owner, lifecycle | Author, summary, media | Product/technical facts remain sourced | Future formats/locales by stable ID |
| Guide | Structured instructional/reference content | Content/domain owner pending | Content lifecycle | Products, project/installation context, documents, FAQ | ID, title, scope, audience, owner, sources, lifecycle | Steps/media/download | No unverified safety/installation instruction | Future Guide schema mapping only after eligibility review |
| FAQ | Approved question/answer unit | Content/domain owner pending | Content lifecycle | Topic/entity, answer sources, landing/article | ID, question, answer, owner, source, lifecycle | Related links/media | Must be visible, non-duplicative, factual; no price promise | FAQPage projection only when page eligibility holds |
| Policy | Approved business/legal/governance-facing policy content | Founder/legal/governance owner | Content or Repository Document lifecycle by context | Organization/site/content/inquiry | ID, scope, authority, owner, version, effective status | Jurisdiction, translations | Public and repository policies are distinct authorities | Localized/jurisdiction variants by approval |
| News | Time-contextual factual editorial item | Content owner pending | Content lifecycle | Organization, entities, media | ID, title, date/context, source, owner, lifecycle | Author, related entities | Does not change canonical product/business facts | NewsArticle mapping only after type approval |
| Announcement | Time-bounded official notice | Founder/content owner pending | Content lifecycle with expiry | Organization, affected entities, landing | ID, title, effective period, owner, source, lifecycle | Media, CTA | Must not become permanent fact authority silently | Channel/localization variants by approval |
| Media Asset | Governed visual/audio/file identity | Media owner pending | Media lifecycle plus rights status | Content, Product, Document, derivatives | ID, type, source, owner, rights/access, lifecycle | Caption, alt, focal point, external ID | Public use requires rights/accessibility evidence | CDN/external DAM mapping after approval |
| Media Set | Ordered governed media collection for an entity | Product/media owner pending | Parent/product content lifecycle | Product/Variation/Content, Media Assets | ID, owner, applicability, ordered members | Roles, locale | Set does not duplicate asset authority | Channel-specific renditions by approval |
| Technical Document | Versioned product/project technical evidence | Qualified technical owner pending | Technical-document lifecycle | Products, Variations, Projects, Media preview | ID, type, title, version, owner, reviewer, access, applicability | Issue date, language, checksum | No unsupported certificate/claim; protected access enforced | External document-system mapping |
| Repository Document | Controlled repository knowledge/governance file | Metadata Owner | Repository Document Lifecycle | Decisions, ADRs, audits, dependencies, references | Document ID, status, authority, owner, version, dates, relationships | AI compatibility, approval reference | File does not gain authority by existence | Modular IDs after Founder decision |

## Repository Governance Entities

| Entity | Purpose | Owner | Lifecycle | Relationships | Required fields | Optional fields | Constraints | Future expansion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Decision | Scoped choice with authority/status | Decision owner | Decision status plus source-document lifecycle | Source, affected rules/entities, evidence | ID, statement, scope, owner, status, date/source | Rationale, alternatives, supersession | Log indexes; source remains authority | Classification/approval model after governance approval |
| Founder Decision | Decision requiring/recording Founder authority | Founder | Pending/resolved/superseded as registered | Source question, affected documents, evidence | FD ID, decision required, source, status | Resolution date/reference | Cannot be inferred from task output | New decision families by controlled ID |
| Open Question | Unresolved issue requiring evidence/decision | Source owner | Open/resolved as registered | Source document, decision owner, resolution | OQ ID, question, source, status | Reviewer/deadline | Does not create requirements | Additional domains through register |
| ADR | Immutable architecture decision record after acceptance | Decision Owner/Founder approval | Proposed/Accepted/Superseded plus document lifecycle | Context, decision, consequences, related rules | ADR ID, context, decision, status, date, owner | Alternatives, evidence | Accepted ADR changed only by superseding ADR | New ADRs through ADR process |
| Audit | Evidence record of observed repository state | Founder/reviewer | Evidence-record document lifecycle | Audited sources, findings, evidence, recommendation | Document ID, scope/date, evidence, owner/reviewer, status | Scores only with reproducible method | Does not govern or prove unavailable history | New batch/domain audits |
| Review Record | Evidence of assigned validation and outcome | Review owner | Review lifecycle/event record | Document/entity, reviewer, findings, outcome | Target ID/version, reviewer, date, scope, outcome | Exceptions, evidence links | Review does not equal approval | Domain-specific review profiles |

## Semantic Projection Entities

Schema.org types, search documents, navigation entries, URL records, breadcrumbs, sitemaps, feeds, and external integration payloads are projections of canonical entities. They require stable source IDs, projection purpose, owner, eligibility, source version, lifecycle, access, canonical destination, validation, and refresh behavior. They never become business master entities solely because they are externally visible.

## Relationship Rules

- Relationships are typed, directional, source-owned, lifecycle-aware, and reviewable.
- A relationship record identifies source ID, relationship type, target ID, owner/source, status, applicability, and evidence when needed.
- `contains` is not `classifies`; `related to` is not `compatible with`; `represented by` is not `owned by`; `mentions` is not `applies to`.
- Public projections include only approved relationships and exclude protected/internal fields.
- Deleting, merging, replacing, suspending, or archiving an entity triggers dependent relationship, URL, search, content, schema, media, inquiry, and integration review.
- No relationship is inferred from a common label, tag, URL segment, product family, shared attribute, content co-occurrence, or AI similarity.

## Required and Optional Field Rules

- Required means the entity cannot reach its operational/public lifecycle state without the field and validation.
- Optional means permitted only when an approved source and consumer exist; it does not mean uncontrolled free text.
- Sensitive fields include explicit access, consent, retention, and deletion policy.
- Derived fields identify source fields and regeneration rules.
- Localized fields retain stable identity and translation/review status.
- External fields are system-scoped, versioned mappings.

## Future Expansion

A new entity type requires a stable type ID, purpose, non-duplication analysis, canonical authority, owner, lifecycle, required/optional fields, relationships, access class, content/search/URL/schema consumers, migration impact, and approval. No future entity may bypass Plugin First, Configuration First, Mobile First, Persian RTL, Inquiry First, No Public Pricing, or the existing prohibited-technology boundaries.

## Founder Decisions

- Approve, revise, or reject ERM-001 through ERM-008.
- Approve the entity registry and assign unresolved owners/lifecycles.
- Decide whether Location, Project, Installation, Representative profile, Local Business projection, Review, News, and Announcement become operational/public entities.
- Approve relationship vocabulary, claim evidence, access classes, and expansion review.
- Approve physical mappings only in a separate implementation-authorized phase.

## Open Questions

- Which conditional entities are required for the approved business/content scope?
- Who owns each entity type and relationship type?
- Which lifecycle applies to taxonomy terms, representatives, locations, projects, installations, media rights, and external projections?
- Which fields are public, protected, internal, localized, derived, or integration-only?
- Which relationship types require qualified domain/legal/privacy evidence?

## Approval Status

Review. No entity record, database object, WordPress object, taxonomy, content type, custom field, user, API, schema markup, or integration mapping is approved or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 07 conceptual entity relationship registry; documentation only. |

## Related Documents

- [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md)
- [Schema.org Strategy](31_SCHEMA_ORG_STRATEGY.md)
- [Content Types](32_CONTENT_TYPES.md)
- [Media Strategy](33_MEDIA_STRATEGY.md)
- [SEO Entity Model](34_SEO_ENTITY_MODEL.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| ERM-001–ERM-008 | PDM/TAX/ATT/INQ, IA, CONTENT decisions, repository governance | Documents 31 through 34 | Entity inventory, stable IDs, owners, lifecycles, fields, relationship integrity, public/protected projection, duplicate authority, and expansion validation |

Implementation status: `Not authorized`.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Content and Entity Architecture Reading Path](READING_ORDER.md#content-and-entity-architecture-reading-path)
