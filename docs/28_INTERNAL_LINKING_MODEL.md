# Enterprise Internal Linking Model

## Document Control

- **Document ID:** `docs/28_INTERNAL_LINKING_MODEL.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Information Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On canonical owner, site hierarchy, URL, product, taxonomy, knowledge, representative, landing, inquiry, SEO, or content-lifecycle change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [Site Structure](25_SITE_STRUCTURE.md), [URL Architecture](26_URL_ARCHITECTURE.md), and [Search and Discovery](27_SEARCH_AND_DISCOVERY.md)
- **Dependencies:** [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [Site Structure](25_SITE_STRUCTURE.md), [URL Architecture](26_URL_ARCHITECTURE.md), and [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md)
- **Related Documents:** [Search and Discovery](27_SEARCH_AND_DISCOVERY.md), [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md), and [SEO Strategy](11_SEO_STRATEGY.md)
- **Traceability:** CP-003 through CP-006, IA-001 through IA-007, SITE-001 through SITE-007, URL-001 through URL-008, SRCH-001 through SRCH-008, and LINK-001 through LINK-007
- **AI Compatibility:** AI-readable with explicit relationship meaning, canonical ownership, access, and no-automation boundaries
- **Approval:** Pending Founder/content/SEO approval; no links, templates, widgets, or automation authorized

## Purpose

Define how canonical products, categories, knowledge, representatives, landings, support, documents, and inquiry paths connect without creating duplicate authority, unsupported relationships, public pricing, or uncontrolled SEO structures.

## Scope and Boundary

This model defines logical link responsibilities. It does not add links, create content, choose anchor text, set link counts, configure menus/templates/widgets, select a plugin, automate recommendations, or change public URLs.

## Internal Linking Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| LINK-001 | Build internal links from explicit governed relationships and canonical ownership, not keyword similarity or co-occurrence alone. | Proposed pending Founder/content/SEO approval |
| LINK-002 | Preserve a navigable hierarchy from platform/domain hubs to canonical entities and back to meaningful parents. | Proposed pending Founder/UX/SEO approval |
| LINK-003 | Use products, categories, knowledge, representatives, landings, and support as distinct link roles; a link does not transfer data authority. | Proposed pending Founder approval |
| LINK-004 | Link every public commercial journey to contextual inquiry without price, cart, checkout, payment, or transaction actions. | Required by CP-005, CP-006, and ADR-0001 |
| LINK-005 | Exclude protected/internal data and prevent links from implying compatibility, certification, warranty, availability, representative scope, or commercial claims without evidence. | Proposed pending Founder/domain/security approval |
| LINK-006 | Keep navigation, breadcrumbs, contextual links, related-item links, document links, and inquiry links independently governed and non-duplicative. | Proposed pending Founder/UX/SEO approval |
| LINK-007 | Require link ownership, lifecycle, canonical/redirect validation, and expansion review so future content growth does not create orphan or competing structures. | Proposed pending Founder approval |

## Link Hierarchy

```text
Home / Platform Entry
  -> Domain Hub
      -> Canonical Category, Product, Knowledge, Representative, Support, or Landing
          -> Explicitly Related Canonical Nodes
              -> Contextual Inquiry

Every public node
  -> Meaningful parent or hub
  -> Its canonical URL
  -> Relevant next action
```

Hierarchy links orient users; they do not require the same hierarchy in canonical URL paths. Mobile RTL users must be able to understand the parent, current location, and next action without hover or visual-only cues.

## Authority Distribution

Internal linking distributes discovery and SEO attention, not source authority.

| Link owner | May authoritatively expose | Must reference rather than duplicate |
| --- | --- | --- |
| Product Family/Type hub | Approved membership, navigation context, canonical child links | Product specifications, knowledge narratives, representative claims |
| Variable Parent Product | Shared product facts, variation context, approved media/documents, inquiry action | Taxonomy definitions, independent knowledge ownership, representative routing |
| Taxonomy/landing owner | Definition, inclusion criteria, canonical member references, unique intent content | Product-master facts and attribute values |
| Knowledge item | Approved educational narrative and cited context | Canonical product, taxonomy, technical document, and policy facts |
| Representative profile | Approved public representative identity and explicit scope | Product authority, territory assumptions, routing/workload, customer data |
| Support item | Approved help/process guidance | Product guarantees, commercial terms, private cases |
| Inquiry entry | Required guidance and source context | Public price, quote acceptance, transaction state |

Link prominence, placement, and volume require UX/SEO evidence and do not alter this authority map.

## Category Linking

- Domain/Product hubs link to approved Product Families and high-value governed context paths.
- Product Family links to approved Groups/Types and canonical member products.
- Category/term landings link to canonical products and supporting knowledge whose explicit relationships match inclusion criteria.
- Category cross-links require a named relationship; shared wording is insufficient.
- Material, Alloy, Finish, Brand, Application/Use Case, Industry, Collection, and SEO Landing views preserve one canonical identity and landing owner.
- Product Tags do not create authority, primary navigation, filters, or automatic cross-link networks by default.
- Empty, expired, duplicate, protected, unapproved, or non-canonical categories receive no public internal-link promotion.

## Product Linking

- Product hierarchy, breadcrumbs, and category context link the Variable Parent Product to approved parents.
- Product pages may link to explicit alternatives, accessories, compatible entities, approved documents, knowledge, support, and representative scope.
- Alternatives, related products, accessories, and compatibility are different directed relationship types.
- Variation selection remains within parent context by default and does not create a competing canonical link.
- Links to inquiry preserve parent/variation IDs, selected approved attributes, source context, and language without exposing data in public URLs.
- Product lifecycle, inquiry eligibility, access class, and replacement state govern whether a link is shown, retained, redirected, or removed.
- No product link uses price, discount, cart, checkout, payment, or false availability as anchor/promotion logic.

## Knowledge Linking

- Knowledge items link to their governing topics/content types, canonical products, approved taxonomy owners, public documents, support, and contextual inquiry.
- Product and category pages link back to relevant knowledge only when the relationship and content quality are approved.
- Technical claims link to approved evidence or source documents; a link is not proof by itself.
- Articles, FAQs, guide-like pages, and technical documents do not duplicate one another's canonical intent.
- Related-knowledge links use explicit topic/entity relationships, not uncontrolled keyword matching.
- Superseded, expired, merged, or archived knowledge updates links and redirects according to lifecycle decisions.

## Representative Linking

- Representative links are absent until public profile publication is approved.
- A public profile may link to approved Product, Application/Use Case, Industry, region, language, support, or inquiry context only through explicit governed relationships.
- Product/landing pages may link to a representative only when the relationship owner, scope, lifecycle, and fallback are approved.
- Links must not imply exclusive territory, certification, stock, pricing, availability, response time, or technical suitability without evidence.
- Internal routing, workload, CRM identity, private contact, and customer relationships never become public links.
- Deactivated or changed representatives require privacy, replacement, redirect, inquiry-source, and routing review.

## Landing Linking

- Each landing links to the canonical entities that substantiate its unique intent.
- Product/category/knowledge pages link to a landing only when it adds distinct governed value and is the approved intent owner.
- Campaign links preserve canonical ownership and do not create duplicate pages through parameters or aliases.
- Collections and campaign landings record start, review, end/renewal, owner, and post-expiry link behavior.
- Expired, thin, duplicate, unowned, or non-canonical landings are removed from promotional links and resolved through approved retain/redirect/remove policy.
- Landing inquiry actions retain source intent without exposing price or confidential campaign data.

## Cross-Link Rules

Every cross-domain link requires:

- Source and target stable identities.
- Relationship type and direction.
- Canonical target URL and access eligibility.
- Owner and approval source when the relationship carries a product, technical, representative, legal, or commercial claim.
- Language and mobile RTL-compatible label/anchor context.
- Lifecycle behavior for target change, merge, suspension, discontinuation, expiry, protection, or deletion.
- No conflict with taxonomy/attribute authority, SEO intent ownership, privacy, security, or inquiry boundaries.

Automatic links based only on labels, tags, query text, external IDs, shared attributes, upload proximity, or AI-generated similarity are prohibited without a future approved model and validation.

## SEO Considerations

- Internal links point to canonical URLs, not redirecting, parameterized, filtered, search, preview, duplicate, or private variants.
- Anchor context is descriptive, Persian RTL appropriate, non-deceptive, and consistent with the target's approved purpose.
- Breadcrumbs express information context without forcing mutable hierarchy into URLs.
- Hubs and canonical landing owners receive links from relevant children/supporting items; orphan public content is prohibited.
- Link concentration, sitewide links, repeated anchors, pagination, faceted navigation, nofollow behavior, and link limits require an approved SEO/UX matrix.
- Internal links cannot make thin/duplicate content indexable or transfer authority to an unapproved landing.
- No price, Offer, transaction, compatibility, safety, warranty, or representative claim is introduced through anchor text.

## Future Scalability

- Stable IDs and typed relationships allow links to survive label, slug, menu, taxonomy-parent, and language changes.
- New domains and content types register permitted inbound/outbound relationships before publication.
- Future languages link localized equivalents through approved alternate relationships, not ad hoc cross-language duplicates.
- Future countries/business units preserve shared identity or explicitly document justified divergence.
- Link inventories support owner, source, target, relationship, canonical, language, lifecycle, and validation evidence.
- Merges, splits, migrations, and deprecations include link-impact analysis and orphan detection.
- Future automation remains Configuration First/Plugin First and cannot bypass human approval for high-risk claims or protected data.

## Founder Decisions

- Approve, revise, or reject LINK-001 through LINK-007.
- Approve permitted relationship types and public representative linking.
- Assign linking, content, product, taxonomy, representative, support, and SEO owners.
- Approve anchor, breadcrumb, related-item, sitewide-link, pagination, and lifecycle policies.
- Approve any future automation only after capability, evidence, rollback, privacy, and governance review.

## Open Questions

- Which relationship types may produce public links for each node family?
- Which product relationships require qualified domain evidence?
- Are representative profile links public and from which contexts?
- Which knowledge/product/category links are mandatory versus optional?
- Who owns link review, broken-link correction, redirects, and orphan prevention?
- What mobile RTL, accessibility, and SEO acceptance criteria apply?

## Approval Status

Review. No internal link, anchor, breadcrumb, related-item block, representative link, inquiry link, template, plugin, automation, or configuration is approved or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 06 enterprise internal linking model; documentation only. |

## Related Documents

- [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md)
- [Site Structure](25_SITE_STRUCTURE.md)
- [URL Architecture](26_URL_ARCHITECTURE.md)
- [Search and Discovery](27_SEARCH_AND_DISCOVERY.md)
- [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md)

## Traceability

| Decision range | Origin | Dependent concerns | Future evidence |
| --- | --- | --- | --- |
| LINK-001–LINK-007 | IA/SITE/URL/SRCH decisions, product/taxonomy/inquiry models, CP-003–CP-006 | Future navigation, content, products, landings, representatives, support, inquiry | Link inventory, canonical/redirect checks, relationship evidence, orphan detection, mobile RTL/accessibility, no-price, privacy, and lifecycle validation |

Implementation status: `Not authorized`.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Information Architecture Reading Path](READING_ORDER.md#information-architecture-reading-path)
