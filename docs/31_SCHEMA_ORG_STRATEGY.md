# Schema.org Semantic Strategy

## Document Control

- **Document ID:** `docs/31_SCHEMA_ORG_STRATEGY.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Information Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On entity, canonical, content type, Schema.org vocabulary/release, eligibility, search-engine policy, language, media, review, or public-claim change
- **Lifecycle:** Review
- **Source of Truth:** [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [URL Architecture](26_URL_ARCHITECTURE.md), [SEO Entity Model](34_SEO_ENTITY_MODEL.md), and the official Schema.org vocabulary
- **Dependencies:** [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md), and [URL Architecture](26_URL_ARCHITECTURE.md)
- **Related Documents:** [Content Types](32_CONTENT_TYPES.md), [Media Strategy](33_MEDIA_STRATEGY.md), [Search and Discovery](27_SEARCH_AND_DISCOVERY.md), [Internal Linking Model](28_INTERNAL_LINKING_MODEL.md), and [SEO Strategy](11_SEO_STRATEGY.md)
- **Traceability:** CP-003 through CP-006, CP-010, IA-001 through IA-007, URL-001 through URL-008, CONTENT-001 through CONTENT-008, ERM-001 through ERM-008, and SCHEMA-001 through SCHEMA-009
- **AI Compatibility:** AI-readable semantic policy; no markup, code, automated generation, or AI implementation authorized
- **Approval:** Pending Founder/SEO/domain/legal review; no structured-data implementation authorized

## Purpose

Define how approved public Damavand Steel entities may later be expressed through Schema.org semantics while preserving canonical identity, visible-content truth, Inquiry First, No Public Pricing, and platform independence.

## Scope and Boundary

This strategy documents semantic eligibility and relationships only. It does not generate JSON-LD, RDFa, Microdata, HTML, schema fields, templates, plugins, product markup, or search-engine configuration.

Schema.org vocabulary existence does not mean a Damavand entity exists, is public, is eligible for markup, or qualifies for a search feature. Search-engine feature eligibility and Schema.org vocabulary are separate concerns and require validation at implementation time.

## Schema Strategy Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| SCHEMA-001 | Generate future semantic projections only from approved canonical public entities and visible validated content. | Proposed pending Founder/SEO approval |
| SCHEMA-002 | Give each projected entity one stable canonical semantic identity aligned with its canonical URL; duplicate pages reference rather than recreate it. | Proposed pending Founder/SEO approval |
| SCHEMA-003 | Use the most specific semantically correct official type only when entity purpose, fields, public visibility, and eligibility are evidenced. | Proposed pending Founder/domain approval |
| SCHEMA-004 | Represent relationships between Organization, WebSite, content, products, media, people, projects, and breadcrumbs as one connected graph without transferring source authority. | Proposed pending Founder/SEO approval |
| SCHEMA-005 | Exclude Offer, price, priceCurrency, public quote, cart, checkout, payment, and unsupported availability semantics under No Public Pricing. | Required by CP-005, CP-006, and ADR-0001 |
| SCHEMA-006 | Publish Person, LocalBusiness, Project, Review, FAQ, Collection, Search, Image, and Video semantics only when the corresponding public entity and required evidence exist. | Proposed pending Founder/domain/legal/privacy approval |
| SCHEMA-007 | Validate language, canonical, access, lifecycle, required fields, visible-content parity, and relationship identity before any semantic publication. | Proposed pending Founder/SEO approval |
| SCHEMA-008 | Keep semantic policy independent of WordPress, WooCommerce, theme, page builder, or SEO plugin implementation. | Required by CP-001 and CP-002 |
| SCHEMA-009 | Review vocabulary version and consumer policies before implementation or material semantic change; this document does not freeze a vendor interpretation. | Proposed pending Founder/SEO approval |

## Semantic Graph Principles

- The semantic graph is a projection of the Entity Relationship Model, not a separate business database.
- Canonical entity IDs, URLs, names, language, ownership, lifecycle, and relationships come from approved sources.
- A page describes its main entity; supporting entities reuse stable identities.
- Public semantic fields match visible public content and do not expose protected/internal information.
- Persian RTL text remains Persian; identifiers and language tags are handled separately.
- Empty, inferred, hidden, stale, contradictory, duplicated, or unsupported fields are omitted rather than fabricated.
- Semantic eligibility is revoked or reviewed when the source entity is suspended, archived, protected, merged, replaced, or materially changed.
- No schema projection authorizes public pricing or AI features.

## Organization Strategy

Potential type: [Organization](https://schema.org/Organization).

- Use for the approved canonical Damavand Steel organization identity only after legal/public identity fields are approved.
- Required strategy fields: stable entity ID, approved name, canonical URL, owner, public lifecycle, and verified identity source.
- Optional fields such as logo, contact, address, identifiers, same-identity references, and policies require verified public sources and rights/privacy review.
- Organization is the preferred root for brand/site/publisher relationships when factually correct.
- Do not create multiple Organization nodes for language, page, department, or campaign variants without an approved distinct legal/business identity.

## Local Business Strategy

Potential type: [LocalBusiness](https://schema.org/LocalBusiness).

- Use only if an approved Organization-at-Location entity meets the semantic definition and has a public local-business presence.
- Required strategy fields include source Organization ID, Location ID, approved public name, canonical local URL, owner, and eligibility approval.
- Address, geo, telephone, hours, service area, images, and branch relationships are optional only when verified and approved for public use.
- Do not infer LocalBusiness from a contact page, representative territory, warehouse mention, project location, or inquiry routing.
- Exact subtype and multi-location identity remain Founder/local/SEO decisions.

## Product Strategy

Potential type: [Product](https://schema.org/Product).

- The Variable Parent Product is the default semantic product owner because it owns the canonical product URL and shared public facts.
- Variation semantics require an approved parent/variation mapping, stable IDs, visible selectable values, canonical behavior, and non-duplication review.
- Candidate public fields include approved name, description, image, brand, material/attributes, identifier, and relationships only when visible and validated.
- Offer, AggregateOffer, price, priceCurrency, priceValidUntil, seller-price, cart, checkout, payment, shipping purchase, and public quote semantics are prohibited.
- Availability semantics require approved public meaning and must not misrepresent `supply_after_order`, inquiry eligibility, lead time, or stock certainty.
- Product ratings/reviews are absent unless an authentic governed Review entity and publication policy are approved.

## Breadcrumb Strategy

Potential type: [BreadcrumbList](https://schema.org/BreadcrumbList).

- Reflect the visible approved navigation/context trail to the current canonical public page.
- Each list item uses a stable canonical public destination, approved label, and correct order.
- Breadcrumb hierarchy may express information context without copying the full path into the URL.
- Exclude protected, search, filter, parameter, redirecting, expired, and non-canonical destinations.
- Product hierarchy, site hierarchy, and URL hierarchy remain distinct; the breadcrumb selects one approved user context.

## Article Strategy

Potential type: [Article](https://schema.org/Article) or a more specific official subtype only after content-type approval.

- Use for an approved public article/knowledge item whose editorial purpose matches the type.
- Required strategy fields: canonical content ID/URL, headline/title, language, owner/publisher, lifecycle/publication evidence, and main entity/topic relationship.
- Author, reviewer, dates, image, section, and related entities require approved sources.
- A product description, landing, FAQ collection, policy, announcement, or technical document is not automatically an Article.
- Material changes preserve version/review evidence and visible-content parity.

## FAQ Strategy

Potential type: [FAQPage](https://schema.org/FAQPage).

- Use only for a public page whose main purpose is to present one or more approved visible frequently asked questions with authoritative answers.
- Each FAQ entity retains a stable question/answer ID, owner, source, lifecycle, language, and applicable entities.
- Do not mark hidden, generated, duplicated, customer-specific, promotional, unreviewed, or user-submitted Q&A as FAQPage.
- FAQ answers do not expose prices, quotes, confidential terms, unsupported compatibility, or warranty promises.
- Search-engine eligibility and display behavior require separate current-policy validation.

## Collection Strategy

Potential types: [CollectionPage](https://schema.org/CollectionPage) for an eligible collection page and [ItemList](https://schema.org/ItemList) when an ordered/list relationship is semantically appropriate.

- A Collection entity must have approved purpose, owner, inclusion rule, lifecycle, canonical URL, and public eligibility.
- CollectionPage describes the page; ItemList describes a governed list. Neither becomes product/taxonomy authority.
- Product Family, category, search results, filters, Product Tags, campaigns, and Collections require distinct eligibility review.
- Expired, unowned, thin, parameter-generated, or non-canonical collections are not projected as independent public semantic entities.

## Search Strategy

Potential relationship: [WebSite](https://schema.org/WebSite) with an eligible [SearchAction](https://schema.org/SearchAction) as a future `potentialAction`.

- Describe site search only if a public search capability exists, works as represented, uses an approved canonical target pattern, and excludes protected data.
- Search result pages and query URLs remain non-canonical/non-indexable by default.
- Do not expose query history, personal data, internal filters, private identifiers, or AI behavior.
- SearchAction does not approve a search plugin, engine, UI, ranking algorithm, or implementation.

## WebSite Strategy

Potential type: [WebSite](https://schema.org/WebSite).

- Use one canonical WebSite entity per approved site identity/domain/language architecture.
- Relate it to the canonical Organization, public publisher identity, language, and approved search capability.
- Do not create duplicate WebSite identities for paths, campaigns, menus, taxonomies, or responsive views.
- Future languages/domains require approved identity, canonical/alternate, ownership, and localization decisions.

## Image Strategy

Potential type: [ImageObject](https://schema.org/ImageObject).

- Project only approved public Media Assets with rights, access, source, content URL, format, dimensions when known, caption/alt context, and entity relationship.
- Keep asset identity separate from derivatives; choose a canonical asset/rendition relationship.
- Alt text remains an accessibility field and must not be fabricated for SEO; schema description/caption may differ by governed purpose.
- Protected/internal/licensed-restricted images are excluded from unauthorized public projections.

## Video Strategy

Potential type: [VideoObject](https://schema.org/VideoObject).

- Require approved public Video entity, title/name, description, thumbnail, content/embed access as applicable, duration/date when verified, owner, rights, language, transcript/captions status, and canonical page relationship.
- Do not publish empty, inaccessible, expired, private, misleading, or unsupported video metadata.
- Product/technical claims in video require the same evidence and review as text.
- Hosting, player, streaming, CDN, and implementation remain outside this strategy.

## Person Strategy

Potential type: [Person](https://schema.org/Person).

- Use only for an approved public person/Representative profile with consent, purpose, owner, lifecycle, canonical identity, and privacy review.
- Candidate public fields are limited to approved business identity and scope; personal contact, private IDs, workload, routing, customer relationships, territory assumptions, and status remain excluded.
- A WordPress user, author account, inquiry contact, Customer, or CRM contact is not automatically a public Person entity.
- Deactivation, role change, deletion, and redirect behavior require privacy and content review.

## Project Strategy

Potential type: [Project](https://schema.org/Project) only when its current official semantics fit the approved public entity.

- The internal Project entity is protected inquiry/business context by default and receives no public schema projection.
- A public project/case-study projection requires separate approval, consent/rights, public canonical content, ownership, lifecycle, participating-entity relationships, and claim evidence.
- Project should not expose Customer identity, location, schedule, commercial data, documents, or installation details without explicit approval.
- If Schema.org Project semantics or consumer support are unsuitable, use a safer approved public content/entity mapping or omit the projection; do not force a type.

## Review Strategy

Potential type: [Review](https://schema.org/Review).

- No review/rating capability, content type, aggregate rating, or customer-review business process is assumed.
- Use only for authentic, attributable, consented/rights-cleared, moderated, publicly visible Review entities with an explicit reviewed item and approved policy.
- Required strategy fields include Review ID, itemReviewed ID, author/source, body, publication lifecycle, owner/moderator, and evidence of authenticity.
- Rating fields are optional only when a governed scale and validation exist.
- No review may contain confidential pricing, private inquiry/customer data, unsupported product claims, incentives not disclosed, or fabricated/generated content.

## Document Relationships

| Source document | Semantic role |
| --- | --- |
| Entity Relationship Model | Canonical entity types, identity, fields, ownership, lifecycle, and relationships |
| Enterprise Content Architecture | Source, approval, reuse, version, and visible-content rules |
| Content Types | Public content purpose, audience, SEO/navigation role, and lifecycle |
| Media Strategy | Asset rights, accessibility, derivatives, localization, and media metadata |
| SEO Entity Model | Search intent, canonical ownership, authority flow, and semantic retrieval boundaries |
| URL Architecture | Canonical public URL and identity behavior |
| Search and Discovery | Public eligibility and search boundaries |

Semantic projections must reference these sources rather than restate independent facts.

## Validation and Change Control

- Confirm current official Schema.org type/property status and current consumer policy before implementation.
- Validate type semantics, required source fields, canonical IDs/URLs, visible-content parity, language, lifecycle, access, and relationships.
- Test duplicate entities, broken references, conflicting owners, stale projections, hidden content, public pricing, protected data, and unsupported claims.
- Schema changes follow entity/content change control and update affected search, canonical, media, URL, and knowledge-graph evidence.
- Automated generation, if ever authorized, must fail closed when source or eligibility is missing.

## Future Schemas

Any future type—such as a more specific Article, Organization, Place, Product grouping, Guide, technical document, event, service, dataset, certification, or other vocabulary—requires an approved repository entity, public purpose, canonical owner, official vocabulary validation, required fields, consumer value, visible evidence, no-price/privacy review, and deprecation path.

Vocabulary availability alone is not a business requirement or implementation authorization.

## Founder Decisions

- Approve, revise, or reject SCHEMA-001 through SCHEMA-009.
- Approve eligible public Organization, LocalBusiness, Product/Variation, Article, FAQ, Collection, Search, Person, Project, and Review projections.
- Approve semantic identity, owner, language, lifecycle, field, and validation policies.
- Assign SEO/domain/legal/privacy/media reviewers.
- Approve implementation only through a separate task after current vocabulary and consumer-policy review.

## Open Questions

- Which organization/location/public-person/project/review entities actually exist and are eligible?
- Which product/variation semantics accurately represent the approved catalog without Offer/pricing data?
- Which content types qualify for Article, FAQPage, CollectionPage, ItemList, or other official types?
- Which fields and relationships are public, visible, verified, and maintained?
- Who owns semantic graph validation and vocabulary/consumer-policy review?

## Approval Status

Review. No Schema.org markup, JSON-LD, RDFa, Microdata, HTML, plugin setting, template, field mapping, Product/Offer schema, SearchAction, or automated generator is approved or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 07 Schema.org semantic strategy; documentation only. |

## Official Vocabulary References

- [Schema.org vocabulary organization](https://schema.org/docs/schemas.html)
- [Organization](https://schema.org/Organization)
- [LocalBusiness](https://schema.org/LocalBusiness)
- [Product](https://schema.org/Product)
- [BreadcrumbList](https://schema.org/BreadcrumbList)
- [Article](https://schema.org/Article)
- [FAQPage](https://schema.org/FAQPage)
- [CollectionPage](https://schema.org/CollectionPage)
- [ItemList](https://schema.org/ItemList)
- [SearchAction](https://schema.org/SearchAction)
- [WebSite](https://schema.org/WebSite)
- [ImageObject](https://schema.org/ImageObject)
- [VideoObject](https://schema.org/VideoObject)
- [Person](https://schema.org/Person)
- [Project](https://schema.org/Project)
- [Review](https://schema.org/Review)

## Related Documents

- [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md)
- [Enterprise Content Architecture](29_CONTENT_ARCHITECTURE.md)
- [Content Types](32_CONTENT_TYPES.md)
- [Media Strategy](33_MEDIA_STRATEGY.md)
- [SEO Entity Model](34_SEO_ENTITY_MODEL.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| SCHEMA-001–SCHEMA-009 | Entity/content/IA/URL/SEO authorities and official Schema.org vocabulary | Content Types, Media Strategy, SEO Entity Model | Entity eligibility, canonical IDs, visible parity, vocabulary version, field validation, no-price, access, language, relationship, and consumer-policy evidence |

Implementation status: `Not authorized`.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Content and Entity Architecture Reading Path](READING_ORDER.md#content-and-entity-architecture-reading-path)
