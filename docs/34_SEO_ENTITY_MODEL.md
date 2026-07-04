# Enterprise SEO Entity Model

## Document Control

- **Document ID:** `docs/34_SEO_ENTITY_MODEL.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Information Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On entity, relationship, canonical, landing, intent, schema, internal link, content, media, search, language, AI/LLM compatibility, or retrieval change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [URL Architecture](26_URL_ARCHITECTURE.md), [Search and Discovery](27_SEARCH_AND_DISCOVERY.md), [Internal Linking Model](28_INTERNAL_LINKING_MODEL.md), [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md), and [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md)
- **Dependencies:** [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [URL Architecture](26_URL_ARCHITECTURE.md), [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md), and [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md)
- **Related Documents:** [Schema.org Strategy](31_SCHEMA_ORG_STRATEGY.md), [Content Types](32_CONTENT_TYPES.md), [Media Strategy](33_MEDIA_STRATEGY.md), [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), and [SEO Strategy](11_SEO_STRATEGY.md)
- **Traceability:** CP-003 through CP-006, CP-010, IA-001 through IA-007, URL-001 through URL-008, SRCH-001 through SRCH-008, LINK-001 through LINK-007, CONTENT-001 through CONTENT-008, ERM-001 through ERM-008, and SEOENT-001 through SEOENT-009
- **AI Compatibility:** AI/LLM compatibility is documentation-only; no AI search, retrieval system, model access, generation, or implementation authorized
- **Approval:** Pending Founder/SEO/domain/content approval; no SEO or semantic implementation authorized

## Purpose

Define an entity-first SEO model that connects canonical business entities, content, media, search intent, internal links, semantic projections, and future retrieval compatibility without creating pages, markup, keywords, schema, or implementation.

## Scope and Boundary

This model defines ownership and semantic relationships. It does not select target keywords, create content, approve indexation, configure SEO plugins, generate Schema.org markup, build knowledge graphs, enable semantic search, or authorize AI/LLM features.

The Draft SEO Strategy remains a related unresolved governance source. This document cannot approve or replace its missing business/operational decisions.

## SEO Entity Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| SEOENT-001 | Organize SEO around canonical entities and explicit relationships rather than isolated keywords or duplicate landing pages. | Proposed pending Founder/SEO approval |
| SEOENT-002 | Assign one canonical public owner to each approved search intent and entity projection. | Proposed pending Founder/SEO approval |
| SEOENT-003 | Preserve product, taxonomy, attribute, content, representative, media, and organization authority while connecting their public projections. | Proposed pending Founder/domain approval |
| SEOENT-004 | Use internal links, navigation, breadcrumbs, schema projections, and search discovery as coordinated references to canonical entities, not competing graphs. | Proposed pending Founder/SEO approval |
| SEOENT-005 | Approve landings only when unique intent, audience, source entities, owner, lifecycle, content value, and non-cannibalization evidence exist. | Proposed pending Founder/SEO approval |
| SEOENT-006 | Exclude public pricing, Offer, transaction, confidential data, unsupported claims, and unauthorized representative/project/customer information from SEO entities. | Required by CP-005, CP-006, privacy/security boundaries, and ADR-0001 |
| SEOENT-007 | Preserve machine-interpretable identity, source, language, lifecycle, and relationships for future semantic retrieval without authorizing AI implementation. | Proposed pending Founder approval |
| SEOENT-008 | Require evidence-backed content and public/protected separation for future AI/LLM compatibility, citations, and knowledge retrieval. | Proposed pending Founder/security/content approval |
| SEOENT-009 | Keep SEO entity policy platform-independent and defer configuration, schema generation, search, and automation to Plugin First/Configuration First review. | Required by CP-001 and CP-002 |

## Entity-First SEO

Entity-first SEO begins with the approved business identity and relationships:

```text
Canonical Organization / WebSite
  -> Canonical Product and Classification Entities
  -> Canonical Content, Media, Representative, Project, and Support Entities
  -> One approved page/landing owner per intent
  -> Internal links, breadcrumbs, search, and semantic projections
  -> Contextual inquiry without public pricing
```

Keywords and queries describe demand; they do not create entities, taxonomies, products, facts, or authority. A page may target an intent only when a canonical entity or governed content entity can satisfy it accurately.

## Knowledge Graph Strategy

The SEO knowledge graph is a public semantic projection of the Entity Relationship Model. It contains only approved public nodes and relationships.

| Node family | SEO function | Authority boundary |
| --- | --- | --- |
| Organization/WebSite | Root identity and publisher/site relationship | Legal/business identity source |
| Product | Canonical catalog subject and inquiry destination | Product Data/WooCommerce authority |
| Taxonomy/Attribute entity | Definition, classification, browse/filter context | Taxonomy/Attribute authority |
| Content | Unique explanatory, support, policy, news, or landing intent | Content owner and approved sources |
| Representative | Conditional public identity/scope | Representative/privacy governance |
| Project | Conditional public case-study entity | Project/consent/content governance |
| Media/Document | Evidence and accessible supporting object | Media/Technical Document authority |
| Inquiry | Public action relationship only | Inquiry data itself remains protected |

The graph never exposes Customer, Inquiry record, routing, CRM/ERP, protected document, internal decision, confidential stock, or pricing data.

## Entity Relationships

SEO-relevant relationships may include `about`, `main entity`, `part of`, `classified by`, `described by`, `has variation`, `brand`, `material`, `supported by`, `uses media`, `related to`, `alternative to`, `compatible with` only when verified, `represented by`, `located at`, `publisher`, `author`, `reviewed by`, `replaces`, and `localized as`.

Every public relationship has source/target IDs, type, direction, owner/source, lifecycle, public eligibility, and evidence where the relationship implies a claim. Shared labels, keywords, tags, links, proximity, or AI similarity do not establish a relationship.

## Internal Entity Linking

- Hubs link to canonical entities that they legitimately contain or classify.
- Entity pages link to explicit supporting/related entities and contextual inquiry.
- Knowledge links to canonical product/taxonomy/document sources; source pages may link back when relevant.
- Representative and Project links are conditional on public approval and evidence.
- Anchor context identifies the entity/purpose accurately in Persian RTL and on mobile.
- Links resolve to canonical eligible URLs, not redirects, search/filter parameters, private views, duplicate archives, or expired landings.
- Internal linking distributes discovery, not source authority.

The detailed rules remain in [Internal Linking Model](28_INTERNAL_LINKING_MODEL.md).

## Authority Flow

```text
Approved business/product/taxonomy/content authority
  -> Canonical entity identity and fields
      -> Canonical public page or landing
          -> Navigation + internal links + breadcrumbs + search
              -> Schema.org semantic projection
                  -> External discovery and future retrieval consumers
```

Corrections flow from the source authority outward. Search results, schema output, external snippets, analytics, or AI/LLM responses never write back as fact authority without an approved evidence and review process.

## Canonical Ownership

- One canonical URL/entity owner per public entity or unique intent.
- Product canonicals belong to Variable Parent Product by default; variations remain contextual unless an exception is approved.
- Category, attribute archive, curated landing, article, FAQ, page, and campaign cannot each own the same intent.
- Localized expressions share stable entity identity and use approved canonical/alternate relationships.
- Merges, moves, renames, replacements, suspension, and archival update canonical, redirect, internal-link, schema, search, and retrieval references together.
- Canonical ownership does not automatically approve indexation.

## Landing Strategy

Every proposed landing records:

- Stable landing ID and type.
- Approved search intent, audience, journey, and inquiry outcome.
- Source entities and inclusion/exclusion rules.
- Canonical owner and competing URL analysis.
- Content owner, domain reviewer, SEO reviewer, lifecycle, review cadence, and expiry/replacement behavior.
- Required unique value, media/documents, internal links, search eligibility, schema eligibility, and no-price validation.

Thin, duplicate, filter-generated, keyword-only, unowned, unsupported, expired, or uncontrolled combination landings remain non-indexable and do not receive canonical authority.

## Search Intent Mapping

| Intent family | Candidate canonical owner | Boundary |
| --- | --- | --- |
| Organization/brand identity | Organization/Brand page or approved canonical landing | One identity owner; claims verified |
| Product discovery | Product Family/Type/category or Product parent | Exact hierarchy/intent approval required |
| Product specification | Product parent plus governed attributes | Attribute archive not automatic owner |
| Application/Use Case | Approved taxonomy/landing or knowledge item | One logical classification; suitability evidence required |
| Industry | Approved Industry landing/content | No unsupported capability claim |
| Material/Alloy/Finish | Canonical taxonomy/attribute-backed landing | One term identity and one landing owner |
| Knowledge/question | Knowledge Article, Guide, FAQ, or support item | Avoid duplicate answer/intents |
| Representative/location | Conditional approved profile/directory/location landing | Privacy, scope, and local eligibility required |
| Project/case study | Conditional approved Project content | Consent, rights, claims, and privacy required |
| Inquiry/help | Support or inquiry guidance | No public price/quote result/transaction intent |

Actual keywords, demand data, volumes, labels, and landing assignments remain unapproved.

## Future AI Search Compatibility

Compatibility requires:

- Stable entity IDs, types, canonical URLs, labels, aliases, languages, owners, lifecycle, and access classes.
- Typed evidence-backed relationships.
- Clear source authority and last-reviewed/version evidence.
- Structured content types, blocks, media/document metadata, and public/protected separation.
- Query/relevance evaluation data only under approved privacy and retention policy.
- Human-readable canonical pages and fallback discovery paths.

This does not authorize AI search, vector databases, embeddings, reranking, recommendations, generated summaries, chat, agents, or external model access.

## Future LLM Compatibility

- Public facts remain traceable to canonical visible sources.
- High-risk claims identify qualified evidence and review status.
- Content distinguishes fact, interpretation, instruction, policy, marketing, and unresolved proposal.
- Entity aliases do not create duplicate identity.
- Documents expose language, version, owner, lifecycle, access, source, and replacement relationships.
- Citation targets remain stable through canonical/redirect governance.
- Protected/internal/personal/pricing information is excluded from public retrieval sources.

Any future LLM use requires separate purpose, data-source, consent, rights, security, privacy, evaluation, hallucination, citation, human-oversight, retention, vendor, and incident governance.

## Semantic Search

Semantic search is a future compatibility concept only. A future decision would require:

- Approved corpus and access boundaries.
- Entity-aware indexing and canonical deduplication.
- Persian normalization and multilingual behavior.
- Relationship/evidence weighting without inventing facts.
- Query privacy, logging, retention, abuse controls, explainability, evaluation, and fallback.
- No public-price or protected-data leakage.
- Configuration/plugin/vendor selection and rollback evidence.

No semantic search implementation or technology is selected.

## Knowledge Retrieval

Future retrieval must:

- Retrieve from current approved public or authorized protected sources according to the requesting role.
- Preserve entity/source IDs, document version, language, access, lifecycle, and citation target.
- Prefer canonical sources over duplicated excerpts.
- Exclude Draft/Review proposals from factual answers unless clearly presented as proposals to authorized users.
- Refuse or escalate when evidence is missing, conflicting, expired, protected, or outside scope.
- Never treat generated output, search snippets, analytics, or conversation as repository authority.
- Never expose prices, customer/inquiry data, private representative information, credentials, or protected documents without explicit authorization.

No retrieval system is authorized in Batch 07.

## Content and Media Integration

- SEO entities use Content Architecture for source/reuse/approval/version rules.
- Content Types define audience, SEO role, navigation role, lifecycle, and owner.
- Media Strategy defines rights, accessibility, derivatives, localization, and public eligibility.
- Schema.org Strategy defines potential semantic projections after entity eligibility.
- Search/Discovery and Internal Linking consume only approved public entity relationships.

## Validation

- Confirm unique entity ID, canonical owner/URL, intent, owner, lifecycle, public eligibility, language, and source.
- Detect duplicate entities, competing landings, contradictory facts, alias fragmentation, orphan content, broken links, redirect chains, stale schema/search projections, and invalid localized relationships.
- Validate Mobile First, Persian RTL, accessibility, visible-content parity, media rights, claim evidence, and inquiry paths.
- Confirm no public price, Offer, cart, checkout, payment, public quote result, protected data, or unauthorized AI behavior.
- External visibility or ranking is never claimed without measured evidence.

## Founder Decisions

- Approve, revise, or reject SEOENT-001 through SEOENT-009.
- Assign entity SEO, intent, canonical, landing, internal-link, schema, content, media, and retrieval owners.
- Approve intent families, canonical landing owners, public entity graph scope, and validation cadence.
- Approve representative/project/local entity SEO only after privacy/domain review.
- Approve any AI/LLM/semantic-search/retrieval capability only through a separate future architecture and implementation task.

## Open Questions

- Which canonical entities and intent families are in the approved initial SEO scope?
- Which page/landing owns each approved intent?
- Which relationships and claims are public and evidence-backed?
- Which content/media/schema projections are eligible and maintained?
- Who owns entity resolution, canonical conflicts, structured semantics, internal links, and future retrieval governance?
- What explicit phase and evidence would permit future AI/LLM compatibility to become an evaluated capability?

## Approval Status

Review. No keyword map, landing page, canonical tag, indexation, internal link, schema markup, search index, knowledge graph implementation, vector database, embedding, LLM, AI feature, plugin, or configuration is approved or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 07 enterprise SEO entity model; documentation only. |

## Related Documents

- [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md)
- [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md)
- [Schema.org Strategy](31_SCHEMA_ORG_STRATEGY.md)
- [Content Types](32_CONTENT_TYPES.md)
- [Media Strategy](33_MEDIA_STRATEGY.md)
- [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| SEOENT-001–SEOENT-009 | IA/URL/SRCH/LINK, CONTENT/ERM/SCHEMA/CTYPE/MEDIA, product/taxonomy rules, CP-001–CP-006 and CP-010 | Future SEO Strategy and approved content/search/schema operations | Entity resolution, canonical/intent inventory, relationship evidence, landing ownership, internal links, semantic validation, public/protected separation, Persian RTL, mobile, no-price, and no-AI validation |

Implementation status: `Not authorized`.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Content and Entity Architecture Reading Path](READING_ORDER.md#content-and-entity-architecture-reading-path)
