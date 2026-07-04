# Enterprise Content Architecture

## Document Control

- **Document ID:** `docs/29_CONTENT_ARCHITECTURE.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Information Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On content strategy, hierarchy, source, type, block, relationship, owner, lifecycle, validation, approval, localization, or consumer change
- **Lifecycle:** Review
- **Source of Truth:** [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles), [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [Enterprise Site Structure](25_SITE_STRUCTURE.md), and the approved-reference product/taxonomy/inquiry models
- **Dependencies:** [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [Enterprise Site Structure](25_SITE_STRUCTURE.md), [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), and [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md)
- **Related Documents:** [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), [Content Types](32_CONTENT_TYPES.md), [Media Strategy](33_MEDIA_STRATEGY.md), [SEO Entity Model](34_SEO_ENTITY_MODEL.md), [URL Architecture](26_URL_ARCHITECTURE.md), and [Internal Linking Model](28_INTERNAL_LINKING_MODEL.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, IA-001 through IA-007, SITE-001 through SITE-007, LINK-001 through LINK-007, and CONTENT-001 through CONTENT-008
- **AI Compatibility:** AI-readable with canonical-source, ownership, lifecycle, localization, reuse, and no-implementation boundaries
- **Approval:** Pending Founder/content/domain/SEO approval; no content or platform implementation authorized

## Purpose

Define the permanent logical strategy for creating, owning, relating, reusing, validating, versioning, approving, publishing, and retiring enterprise content without selecting WordPress storage, plugins, templates, or page-builder components.

## Scope and Boundary

This document governs content responsibilities and information flow. It does not create content, pages, posts, products, media, taxonomies, reusable WordPress blocks, Elementor templates, schema markup, workflows, fields, databases, or configuration.

Exact content inventory, Persian terminology, editorial roles, service levels, publishing cadence, legal text, topics, and physical platform mappings remain Founder and qualified reviewer decisions.

## Content Architecture Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| CONTENT-001 | Manage content as governed entities with stable identity, canonical source, owner, lifecycle, relationships, language, access class, and review evidence. | Proposed pending Founder approval |
| CONTENT-002 | Separate product-master facts, taxonomy/attribute facts, editorial knowledge, support guidance, representative information, landing content, inquiry content, and repository governance records. | Proposed pending Founder/domain approval |
| CONTENT-003 | Reuse canonical facts by reference or governed reusable block; copied text never becomes a second authority. | Proposed pending Founder/content approval |
| CONTENT-004 | Use a content lifecycle distinct from product, inquiry, customer, taxonomy-term, media-rights, and repository-document lifecycles. | Proposed pending Founder/content approval |
| CONTENT-005 | Require content approval appropriate to claim risk, access class, language, SEO role, product relationship, and intended consumer. | Proposed pending Founder/domain/legal/SEO approval |
| CONTENT-006 | Preserve Persian RTL, Mobile First, accessibility, Inquiry First, and No Public Pricing across every content form and reuse context. | Required by CP-003 through CP-006 and ADR-0001 |
| CONTENT-007 | Keep logical content blocks platform-independent; future physical reuse follows Configuration First and Plugin First. | Required by CP-001 and CP-002 |
| CONTENT-008 | Version substantive content and relationships so consumers can identify the approved current state without erasing prior evidence. | Proposed pending Founder approval |

## Enterprise Content Strategy

- Explain the business, products, applications/use cases, industries, knowledge, support, and inquiry paths using governed entities rather than disconnected pages.
- Publish only information with a named owner, source, audience, lifecycle, access class, and approval evidence.
- Keep product facts in product authority, taxonomy/attribute definitions in their registries, and editorial explanation in content authority.
- Use one canonical owner per intent and one canonical source per fact.
- Design Persian RTL content at mobile scale first; desktop expansion must preserve the same meaning and task completion.
- Lead users toward contextual inquiry without public price, cart, checkout, payment, or transactional promises.
- Treat technical, safety, compatibility, origin, warranty, representative, and project claims as evidence-controlled content.
- Prepare content for future channels through structured identity and relationships without authorizing AI or syndication.

## Content Hierarchy

```text
Enterprise content system
├── Identity and trust content
├── Product and classification content
├── Context and landing content
├── Knowledge and educational content
├── Support and document guidance
├── Representative content [conditional]
├── Inquiry guidance and confirmation content
└── Repository governance and evidence content [not public by default]
```

Within the public platform, the logical path remains Domain Hub → Canonical Entity/Intent → Supporting Content → Contextual Inquiry. Content hierarchy may support navigation but cannot redefine product hierarchy, taxonomy identity, canonical URL ownership, or repository authority.

## Content Ownership

| Content concern | Canonical owner source | Assignment status |
| --- | --- | --- |
| Product and variation facts | Product Data/WooCommerce models | Operational owner pending Founder decision |
| Taxonomy and attribute definitions | Taxonomy/Attribute models | Operational owner pending Founder decision |
| Company identity and policy | Approved business/policy authority | TODO (Founder Decision Required) |
| Knowledge, guide, FAQ, news, and announcement content | Content governance | TODO (Founder Decision Required) |
| Landing intent and SEO presentation | SEO/content governance | TODO (Founder Decision Required) |
| Technical claims and documents | Qualified technical authority | TODO (Founder Decision Required) |
| Representative public information | Representative governance | TODO (Founder Decision Required) |
| Inquiry guidance and confirmation | Inquiry/Sales/privacy governance | TODO (Founder Decision Required) |
| Media rights, accessibility, and derivatives | Media governance | TODO (Founder Decision Required) |
| Repository decisions, ADRs, questions, and audits | Existing repository governance sources | Existing metadata applies |

An author or editor does not become the fact owner solely by writing or publishing content.

## Content Lifecycle

The proposed public/editorial content lifecycle is:

| State | Meaning | Public boundary |
| --- | --- | --- |
| `planned` | Purpose, audience, owner, source, and relationship are proposed | Not public |
| `draft` | Content is being authored from approved sources | Not public |
| `review` | Content awaits required editorial/domain/SEO/legal/accessibility review | Not public |
| `approved` | Required approvals are recorded but publication is separately controlled | Not public by state alone |
| `published` | Approved content is publicly available at its canonical destination | Public within access/indexation rules |
| `suspended` | Public use is temporarily withdrawn pending correction or decision | Not promoted; URL behavior requires review |
| `archived` | Content is retained as evidence/history and is no longer active | Not public unless an approved archival policy applies |

Allowed transitions are `planned → draft → review → approved → published`, with correction returning to `draft` or `review`. Published content may move to `review`, `suspended`, or `archived`. Restoration returns to `review` and never republishes automatically.

This lifecycle does not replace product lifecycle, taxonomy term lifecycle, inquiry state, Customer lifecycle, media license/rights status, or repository Document Lifecycle.

## Content Relationships

| Relationship | Meaning | Constraint |
| --- | --- | --- |
| `about` | Content describes an entity or topic | Does not transfer fact authority |
| `supports` | Content helps users understand or act on a canonical entity | Source and audience required |
| `applies to` | Content is valid for a governed entity/context | Applicability evidence required |
| `classified by` | Content uses an approved taxonomy term | Term remains canonical authority |
| `references` | Content cites another entity/document | Reference is not endorsement or ownership |
| `uses media` | Content includes a governed media asset | Rights/accessibility/language rules apply |
| `leads to inquiry` | Content passes approved source context to inquiry | No price or transaction promise |
| `replaces` | Current content replaces a prior item | Migration/redirect/link evidence required |
| `localized as` | Content has an approved locale-specific expression | Stable identity and translation ownership required |
| `derived from` | A reusable expression comes from canonical source data | Derived copy cannot become authority |

Compatibility, certification, suitability, representative scope, warranty, and safety relationships require explicit qualified evidence and cannot be inferred from shared tags or links.

## Content Consumers

| Consumer | Allowed consumption | Boundary |
| --- | --- | --- |
| Public visitor | Approved public product, knowledge, support, representative, landing, media, and inquiry guidance | No protected/internal/private/pricing content |
| Customer/inquirer | Public content plus approved inquiry confirmation/context | No public transaction or unauthorized account behavior |
| Founder/content owner | Review, approval, inventory, lifecycle, and quality evidence through future supported administration | No implementation is selected here |
| Sales/representative | Approved public content plus authorized operational inquiry context | Does not gain product/content authority automatically |
| Search and navigation | Approved canonical public fields and relationships | Cannot invent facts or expose protected content |
| External integration | Explicit versioned approved subset | No syndication or API is authorized here |
| Future AI/LLM system | No current consumption authorization; compatibility metadata only | Requires separate Founder, security, privacy, source, evaluation, and phase decision |

## Content Governance

Every controlled content item requires:

- Stable ID, type, purpose, audience, language, access class, owner, reviewer, approval authority, lifecycle, version, and review trigger.
- Canonical source facts and related entity IDs.
- SEO role, canonical owner, navigation role, inquiry role, and public/protected/internal boundary.
- Claim/evidence classification for technical, safety, legal, representative, compatibility, origin, warranty, and commercial content.
- Media rights, accessibility, localization, expiry, and replacement evidence where applicable.
- Conflict resolution through repository authority rather than author preference or publication recency.

Unowned, source-less, duplicate, expired, unsupported, inaccessible, confidential, or unauthorized content cannot be published.

## Content Sources

Source priority is scope-specific:

1. Accepted Founder decisions, Core Project Principles, and accepted ADRs.
2. Approved governing business, architecture, legal, security, privacy, product, taxonomy, attribute, inquiry, and content sources within their scope.
3. Qualified domain evidence and approved technical documents.
4. Approved product/taxonomy/attribute records and external mappings.
5. Review-state proposals for review context only.
6. Draft, audit, task, conversation, and external material as non-authoritative context until approved.

External vendor, manufacturer, standards, customer, representative, or third-party content requires source, rights, version, applicability, reviewer, and approval evidence. Importing or quoting a source does not make it repository authority.

## Reusable Content Blocks

Logical reusable blocks may include:

- Canonical entity identity/reference.
- Approved product fact/specification set.
- Approved taxonomy/attribute definition.
- Media asset with rights and accessibility metadata.
- Technical-document reference.
- Evidence-backed claim/citation.
- FAQ question/answer unit.
- Related knowledge/product/support links.
- Contextual inquiry prompt and source context.
- Policy notice, disclaimer, consent, or access notice.
- Author/reviewer/last-reviewed evidence where appropriate.

These are platform-independent content units, not Gutenberg blocks, Elementor widgets, Blocksy components, templates, shortcodes, fields, or database objects.

## Content Reuse Rules

- Reuse by reference to stable identity whenever the consumer can resolve the canonical source.
- If text must be embedded, record the source version and define refresh/review behavior.
- Local adaptation may change presentation, length, language, or audience framing but not the underlying approved fact.
- Product facts, technical claims, policy text, consent, and representative scope cannot be forked without owner approval.
- A reusable block inherits the strictest applicable access, expiry, rights, localization, and review constraint from its sources.
- Reuse does not create an indexable landing, canonical URL, schema entity, or taxonomy term automatically.
- Expired/retracted source content invalidates or suspends dependent reuse until reviewed.

## Content Validation

Validation covers:

- Required metadata, type, stable ID, owner, lifecycle, source, and approval.
- Persian language quality, RTL direction, terminology, Unicode/digit consistency, and mobile readability.
- Factual consistency with product, taxonomy, attribute, inquiry, representative, and policy authorities.
- No public price, Offer, cart, checkout, payment, confidential stock, private inquiry, or unsupported commercial promise.
- Technical claim evidence, product applicability, document version, and qualified review.
- Canonical URL, duplicate intent, internal links, media rights, accessibility, alt text, and protected-data boundaries.
- Reusable-block source/version validity and dependent-content impact.
- No hidden or generated content that users cannot verify.

Validation evidence is required before approval and after material source, relationship, language, or lifecycle change.

## Content Versioning

- Content ID remains stable across versions; a version identifies an approved expression at a review point.
- Editorial corrections, factual changes, relationship changes, translations, media replacements, and policy changes are distinguishable.
- Major semantic changes may require a new content entity when the original intent or subject changes.
- Prior approved versions remain traceable according to retention/access policy; public users receive the current eligible version.
- Product/taxonomy/media/document versions are referenced rather than copied into an independent content version authority.
- Exact version syntax and retention remain pending Founder governance decisions.

## Content Approval Workflow

```text
Purpose and source registration
  -> Authoring
      -> Editorial validation
          -> Applicable domain / SEO / legal / security / privacy / accessibility review
              -> Approval
                  -> Publication authorization
                      -> Monitoring and scheduled/event review
                          -> Correction, suspension, replacement, or archive
```

The author cannot self-approve high-risk claims solely by role. Publication authorization is separate from factual approval, and publishing never approves the underlying source entity.

## Founder Decisions

- Approve, revise, or reject CONTENT-001 through CONTENT-008.
- Assign content, knowledge, policy, landing, inquiry-copy, representative, technical-claim, media, localization, and approval owners.
- Approve content lifecycle, version semantics, review triggers, and retention.
- Approve reusable block types and source-refresh behavior.
- Approve required reviews by content/claim risk.

## Open Questions

- Which content domains, inventories, audiences, and Persian labels are approved?
- Which roles author, review, approve, publish, suspend, and archive each content type?
- Which claims require technical, legal, Sales, privacy, security, SEO, or accessibility review?
- What content version, retention, review-cycle, and translation policies apply?
- Which reusable blocks are needed and which facts must always resolve live from canonical sources?

## Approval Status

Review. No content, page, post, product description, block, template, workflow, field, plugin, media, schema, or WordPress/Elementor configuration is approved or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 07 enterprise content architecture; documentation only. |

## Related Documents

- [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md)
- [Content Types](32_CONTENT_TYPES.md)
- [Media Strategy](33_MEDIA_STRATEGY.md)
- [SEO Entity Model](34_SEO_ENTITY_MODEL.md)
- [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| CONTENT-001–CONTENT-008 | CP-001–CP-010, ADR-0001, IA/SITE/LINK decisions, product/taxonomy/inquiry reference models | Documents 30 through 34 | Content inventory, owner, source, lifecycle, reuse, validation, approval, localization, mobile RTL, inquiry, no-price, and access evidence |

Implementation status: `Not authorized`.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Content and Entity Architecture Reading Path](READING_ORDER.md#content-and-entity-architecture-reading-path)
