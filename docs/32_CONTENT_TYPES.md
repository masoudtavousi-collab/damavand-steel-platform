# Enterprise Content Types

## Document Control

- **Document ID:** `docs/32_CONTENT_TYPES.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Information Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On content purpose, audience, field, relationship, SEO, navigation, lifecycle, owner, entity, media, or schema change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md), [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), and [Site Structure](25_SITE_STRUCTURE.md)
- **Dependencies:** [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md), [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), and [Site Structure](25_SITE_STRUCTURE.md)
- **Related Documents:** [Schema.org Strategy](31_SCHEMA_ORG_STRATEGY.md), [Media Strategy](33_MEDIA_STRATEGY.md), [SEO Entity Model](34_SEO_ENTITY_MODEL.md), [URL Architecture](26_URL_ARCHITECTURE.md), and [Internal Linking Model](28_INTERNAL_LINKING_MODEL.md)
- **Traceability:** CONTENT-001 through CONTENT-008, ERM-001 through ERM-008, IA-001 through IA-007, SITE-001 through SITE-007, and CTYPE-001 through CTYPE-007
- **AI Compatibility:** AI-readable content-type registry with explicit public/repository, source, lifecycle, SEO, navigation, and no-implementation boundaries
- **Approval:** Pending Founder/content/domain/SEO approval; no content type or platform object authorized

## Purpose

Define every logical content type currently required or explicitly contemplated by the repository, including its purpose, audience, fields, relationships, SEO role, navigation role, lifecycle, and owner source.

## Scope and Boundary

Content types are logical responsibilities, not WordPress post types, WooCommerce product types, taxonomies, database entities, Elementor templates, Blocksy components, Gutenberg blocks, files, or schema markup.

Conditional types remain unavailable until the Founder approves their business purpose, inventory, owner, lifecycle, public status, and required reviews.

## Content Type Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| CTYPE-001 | Use a controlled content-type registry so purpose, fields, lifecycle, audience, SEO, navigation, and ownership remain explicit. | Proposed pending Founder approval |
| CTYPE-002 | Distinguish entity-master content, editorial content, support/policy content, media/document content, and repository-governance records. | Proposed pending Founder approval |
| CTYPE-003 | Require each public content item to reference canonical source entities rather than duplicate their authority. | Proposed pending Founder/domain approval |
| CTYPE-004 | Keep public, protected, internal, and repository-only content roles distinct. | Proposed pending Founder/security/privacy approval |
| CTYPE-005 | Approve SEO and navigation roles independently; a content type is not automatically indexable, searchable, or menu-visible. | Proposed pending Founder/SEO approval |
| CTYPE-006 | Apply Content Lifecycle to editorial/public types and existing repository lifecycle to governance documents; do not merge lifecycles. | Proposed pending Founder approval |
| CTYPE-007 | Defer physical mapping and implementation to future Configuration First/Plugin First review. | Required by CP-001 and CP-002 |

## Common Content Fields

Every content item requires stable ID, content type, purpose, audience, owner, source, lifecycle, language/locale, access class, canonical relationship, and review/approval evidence. Public content additionally requires an approved canonical/indexation decision and Mobile First/Persian RTL validation.

Optional fields remain controlled by type. They cannot be used to bypass product, taxonomy, media, inquiry, privacy, SEO, or repository authority.

## Content Type Registry

| Content type | Purpose | Audience | Required fields | Optional fields | Relationships | SEO role | Navigation role | Lifecycle | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Product | Public/editorial projection of a Variable Parent Product | Product researchers and inquirers | Product ID, approved title/summary, Type, lifecycle/visibility, source owner, inquiry eligibility | Media, documents, related knowledge/products | Parent Product, Variations, taxonomy, attributes, media, inquiry | Canonical product owner when eligible; no Offer/price | Product hierarchy/search/context paths | Product lifecycle plus content approval for narrative | Product owner pending |
| Category | Explain and navigate an approved taxonomy term | Browsers by governed classification | Term ID, taxonomy, label, definition, owner, lifecycle, inclusion rule | Introductory content, media, related knowledge | Products, parent/child terms, landing owner | Conditional canonical landing; one intent owner | Category/browse path only when approved | Taxonomy term lifecycle plus content lifecycle | Taxonomy/content owner pending |
| Landing | Own one approved audience/search/campaign intent | Defined intent audience | ID, intent, audience, owner, source entities, lifecycle, canonical decision, inquiry purpose | Media, campaign dates, related knowledge | Products, categories, knowledge, inquiry | Canonical only after cannibalization review | Not automatically menu-visible | Content lifecycle plus landing start/review/end | Content/SEO owner pending |
| Knowledge Article | Provide durable educational/explanatory knowledge | Buyers, specifiers, support users, content readers | ID, title, purpose, audience, sources, owner, lifecycle, language | Author, summary, media, related entities | Topics, products, categories, documents, inquiry | Indexable only with unique intent/quality approval | Knowledge Center/topic/search | Content lifecycle | Content/domain owner pending |
| FAQ | Provide a reviewed answer to a recurring question | Public/support/inquiry users | ID, question, answer, source, owner, lifecycle, language | Related entity, link, media | Page/article/product/support/inquiry | FAQPage eligibility conditional; no duplicate intent | Embedded or FAQ hub; not automatic menu item | Content lifecycle | Content/domain owner pending |
| Guide | Provide structured instructional or reference guidance | Product, project, installation, or support audience | ID, title, scope, audience, source/evidence, owner, lifecycle | Steps, media, documents, prerequisites | Products, Project/Installation context, FAQ, inquiry | Conditional knowledge intent; schema type review required | Knowledge/support path | Content lifecycle | Content/qualified domain owner pending |
| Policy | Communicate approved legal, privacy, accessibility, business, or governance policy | Public, staff, repository collaborators according to scope | ID, authority/scope, owner, version, effective lifecycle, language/access | Jurisdiction, translations, related notices | Organization, site, inquiry, content, repository | Public policy may be indexable according to purpose | Footer/support/governance path as approved | Content lifecycle or Repository Document Lifecycle by context | Founder/legal/governance owner |
| Decision | Record/index a scoped decision in its authoritative source | Founder, reviewers, developers, AI collaborators | Decision ID, statement, scope, owner, status, source/date | Rationale, consequences, supersession | ADR, documents, rules, entities | Repository-only; no public SEO role by default | Decision Log/repository paths | Decision status plus source-document lifecycle | Decision owner |
| Audit | Record current-state evidence and recommendation | Founder, reviewers, auditors, maintainers | Document ID, evidence scope/date, owner/reviewer, status, findings | Reproducible metrics, risks, recommendation | Audited documents, decisions, health | Repository-only; no public SEO role by default | Audit index/repository paths | Evidence-record Document Lifecycle | Founder/reviewer |
| Representative | Present approved public representative identity/scope | Users seeking authorized local/context assistance | Representative ID, approved public identity, owner, lifecycle, consent/privacy approval | Bio, public contact, language/location/scope, media | Organization, Location, Product/context, inquiry | Conditional entity/profile intent | Conditional directory/context links | Representative lifecycle plus content lifecycle | Founder/Sales/privacy owner pending |
| Project | Present approved public project/case-study content | Defined business/knowledge audience | Project/public-content ID, purpose, consent/rights, owner, lifecycle, sources | Location, products, media, outcomes | Organization, Customer only if permitted, products, documents, installation | Conditional unique case-study intent | Knowledge/landing path; not assumed | Project lifecycle plus content lifecycle | Founder/Project/privacy owner pending |
| Media | Describe and place a governed Media Asset | Public/content/product consumers | Asset ID, type, source, owner, rights/access, lifecycle, relationship | Caption, alt, transcript, locale, derivatives | Product, content, document, organization/person | Supports entity pages; rarely independent intent | Embedded/discovery only when approved | Media lifecycle/rights status | Media owner pending |
| News | Publish time-contextual factual editorial information | Public stakeholders | ID, title, date/context, source, owner, lifecycle, language | Author, media, related entities | Organization, Product/Project/knowledge as applicable | Time-sensitive intent; indexation conditional | News/archive only if approved | Content lifecycle with freshness review | Content owner pending |
| Announcement | Publish an official time-bounded notice | Affected public/internal audience | ID, title, authority/source, owner, effective period, lifecycle | Media, CTA, related entities | Organization, policy, landing, inquiry/support | Usually temporary; canonical/indexation explicit | Home/support/landing placement during approved period | Content lifecycle with expiry | Founder/content owner pending |
| Page | Hold stable institutional, contact, support, or informational content not covered by a more specific type | Public site audience | ID, purpose, title, audience, owner, source, lifecycle | Media, sections, related entities | Organization, policies, support, inquiry | Conditional stable intent owner | Site tree/menu/footer as approved | Content lifecycle | Content owner pending |
| Technical Document | Provide versioned approved technical evidence/download | Product/project/support users with approved access | Document ID, type, title, version, owner/reviewer, access, applicability, lifecycle | Issue date, language, preview, checksum | Products, Variations, Projects, Media | Public document SEO role explicit; protected excluded | Product/support/knowledge links | Technical-document lifecycle | Qualified technical owner pending |

## Content Type Relationships

- Product, Category, Representative, Project, and Media content are projections of canonical entities; their source entities remain authoritative.
- Landing, Knowledge Article, FAQ, Guide, News, Announcement, and Page are editorial entities that reference source entities.
- Policy may be a public content entity or a repository governance document; each instance declares which lifecycle/authority applies.
- Decision and Audit are repository-governance content and are not public business-platform types by default.
- Technical Document has a distinct version/access lifecycle and must not be treated as an ordinary Media file or Knowledge Article.
- One physical page may present several entities, but one main content purpose and canonical owner must be explicit.

## Required Field Rules

- Required fields are lifecycle gates, not optional author guidance.
- A public item cannot reach `published` with missing owner, source, language, access, canonical, or required approval.
- Conditional fields become required when their related feature is used, such as media rights, location privacy, product applicability, project consent, or representative scope.
- Unknown, not applicable, unavailable, and unverified states remain distinct.

## SEO and Navigation Boundaries

- SEO role, indexation, schema eligibility, search eligibility, and navigation placement are separate approvals.
- A content type may exist without a public archive or menu item.
- Search/filter/campaign views do not automatically become content types or canonical pages.
- Internal links point to canonical eligible content and do not create authority.
- No content type may expose public pricing or transaction behavior.

## Founder Decisions

- Approve, revise, or reject CTYPE-001 through CTYPE-007.
- Approve required versus conditional content types and assign owners.
- Approve fields, audiences, SEO/navigation roles, lifecycle gates, and review profiles by type.
- Decide whether Representative, Project, News, Announcement, public Technical Document, and standalone Media content are required.
- Approve physical platform mappings only through a separate implementation task.

## Open Questions

- Which content types are required for initial Phase 2 content operations?
- Which types have public archives, canonical pages, search results, schema projections, or menu entries?
- Which fields/reviews are required by content risk and audience?
- Which conditional types are explicitly out of scope?
- Who owns each content type, inventory, and lifecycle transition?

## Approval Status

Review. No WordPress post type, WooCommerce setting, taxonomy, field group, page, content item, archive, template, Elementor component, plugin, schema, or workflow is approved or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 07 logical content-type registry; documentation only. |

## Related Documents

- [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md)
- [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md)
- [Schema.org Strategy](31_SCHEMA_ORG_STRATEGY.md)
- [Media Strategy](33_MEDIA_STRATEGY.md)
- [SEO Entity Model](34_SEO_ENTITY_MODEL.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| CTYPE-001–CTYPE-007 | CONTENT/ERM/IA/SITE rules and approved reference models | Media and SEO entity models; future content operations | Type inventory, owner, audience, field, relationship, lifecycle, SEO, navigation, access, Persian RTL, mobile, and no-price validation |

Implementation status: `Not authorized`.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Content and Entity Architecture Reading Path](READING_ORDER.md#content-and-entity-architecture-reading-path)
