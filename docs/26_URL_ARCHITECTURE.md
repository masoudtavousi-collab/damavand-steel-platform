# Enterprise URL Architecture

## Document Control

- **Document ID:** `docs/26_URL_ARCHITECTURE.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Information Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On canonical, slug, path, product, taxonomy, content type, language, redirect, search, filter, representative, landing, or reserved-route change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [Site Structure](25_SITE_STRUCTURE.md), [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), and applicable SEO boundaries in [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#seo-architecture)
- **Dependencies:** [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md), [Site Structure](25_SITE_STRUCTURE.md), [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), and [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md)
- **Related Documents:** [Search and Discovery](27_SEARCH_AND_DISCOVERY.md), [Internal Linking Model](28_INTERNAL_LINKING_MODEL.md), [SEO Strategy](11_SEO_STRATEGY.md), and [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)
- **Traceability:** CP-003 through CP-006, CP-010, IA-001 through IA-007, SITE-001 through SITE-007, TAX-001 through TAX-008, and URL-001 through URL-008
- **AI Compatibility:** AI-readable; every literal-looking example uses unresolved placeholder tokens unless explicitly stated otherwise
- **Approval:** Pending Founder/SEO approval; no route, rewrite, redirect, or configuration authorized

## Purpose

Define stable, canonical, language-aware URL rules for the logical site structure without selecting actual public slugs, WordPress permalink settings, redirect tooling, or physical routes.

## Scope and Boundary

This document governs URL semantics and relationships. It does not create a URL, approve a Persian or Latin slug vocabulary, configure WordPress permalinks, enable an archive, publish a page, or select an SEO/redirect plugin.

Tokens in braces—such as `{products-root}`—are placeholders, not approved literal paths.

## URL Architecture Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| URL-001 | Give every indexable public information object one canonical URL owned by its canonical entity or landing. | Proposed pending Founder/SEO approval |
| URL-002 | Keep stable internal identity independent from URL, slug, navigation placement, label, and external-system ID. | Proposed pending Founder approval |
| URL-003 | Use stable type-owned namespaces and avoid embedding the full mutable business hierarchy in canonical paths by default. | Proposed pending Founder/SEO approval |
| URL-004 | Use the Variable Parent Product as the canonical product URL; variation selection is contextual and non-canonical unless a future approved exception defines independent intent. | Proposed pending Founder/domain/SEO approval |
| URL-005 | Require one declared script/language policy per public namespace and prohibit uncontrolled mixed-script slugs. | Proposed pending Founder/SEO approval |
| URL-006 | Keep internal search, filters, sorting, pagination variants, tracking parameters, and temporary states non-canonical and non-indexable unless an explicit SEO matrix approves a specific view. | Proposed pending Founder/SEO approval |
| URL-007 | Preserve changed/moved public identities through reviewed direct redirects and canonical/link updates; chains, loops, and silent reuse are prohibited. | Proposed pending Founder/SEO approval |
| URL-008 | Prohibit public transaction, public-price, protected-data, internal-state, and implementation-detail URLs under current business rules. | Required by CP-005, CP-006, security/privacy boundaries, and ADR-0001 |

## URL Philosophy

- Human-readable without making labels or slugs the entity key.
- Stable across menu changes and routine taxonomy moves.
- Short enough for mobile sharing and Persian RTL comprehension.
- One canonical owner per public intent.
- Explicit by information type rather than dependent on hidden implementation storage.
- Free of price, customer, inquiry-private, session, internal workflow, and infrastructure data.
- Compatible with future localization and migrations through stable identities and redirects.
- Governed before configuration under Plugin First and Configuration First.

## Canonical Rules

- Every eligible public node declares exactly one self-canonical URL.
- Duplicate views point to or redirect to the canonical owner according to an approved SEO matrix.
- Navigation aliases, filters, search results, campaign parameters, print/share views, and language alternates do not create independent canonical authority.
- A taxonomy term, attribute archive, curated landing, page, and knowledge item targeting the same intent cannot each be canonical.
- Product canonicals belong to the Variable Parent Product by default; variation state remains context on that owner.
- Discontinued, replaced, merged, moved, translated, and archived content requires an approved keep, replace, redirect, remove, or restrict decision.
- Canonicals never point to a public-price, cart, checkout, payment, login-protected error, or inaccessible private destination.
- Canonical behavior and indexability are independent: a valid canonical is not automatic permission to index.

## Slug Rules

- Each namespace records approved language/script, digit, case, punctuation, separator, Unicode normalization, transliteration, stop-word, length, and collision policy.
- Persian and Latin scripts must not be mixed within one slug except an explicitly approved technical token.
- Internal English keys, stable IDs, SKUs, taxonomy IDs, and database identifiers are not public slugs by default.
- A slug is unique within its namespace and must not be reused for a different identity.
- Synonyms and former labels map to the canonical identity rather than creating duplicate URLs.
- Slug changes require redirect, canonical, sitemap, breadcrumb, internal-link, search, analytics, inquiry-source, and external-mapping impact review.
- No real slug vocabulary is approved in Batch 06.

## Category URLs

Proposed logical pattern:

```text
/{classification-root}/{classification-type}/{term-slug}/
```

- `{classification-type}` identifies an approved logical taxonomy, not a plugin or database name.
- Product Family, Material, Alloy, Application/Use Case, Industry, Finish, Brand, Collection, and other eligible types use distinct owned namespaces only if public landings are approved.
- Product Tags are non-indexable and non-landing by default; a tag does not receive canonical public authority automatically.
- Attribute values do not automatically receive public archives.
- A category's parent-child navigation may be represented in breadcrumbs without embedding every ancestor in its canonical path.
- Category deletion, merge, move, and rename preserve identity and follow redirect/canonical review.

Exact roots, taxonomy types, term slugs, hierarchy depth, and indexation remain pending.

## Product URLs

Proposed logical pattern:

```text
/{products-root}/{parent-product-slug}/
```

- The Variable Parent Product owns the canonical URL.
- Product Family, Group, and Type are relationships and navigation context, not required canonical path segments.
- Variation selection may use a non-canonical, share-safe state representation only after privacy, validation, canonical, caching, analytics, and inquiry-context review.
- SKU and external IDs are not canonical slugs by default.
- Product replacements and discontinuation follow product lifecycle plus SEO redirect/retention decisions.
- No product URL exposes public price, quote, cart, checkout, payment, or confidential availability data.

## Knowledge URLs

Proposed logical pattern:

```text
/{knowledge-root}/{content-type}/{knowledge-slug}/
```

- `{content-type}` is an approved public content classification, not necessarily a WordPress post type.
- Topic navigation does not have to appear in the canonical path.
- An article, FAQ, guide-like page, product page, and taxonomy landing cannot independently own the same intent.
- Knowledge revisions preserve canonical identity unless a reviewed split, merge, replacement, or archive decision applies.
- Public technical documents use approved document access and URL rules; protected/internal documents never inherit public knowledge paths.

## Representative URLs

Proposed conditional pattern:

```text
/{representatives-root}/{representative-slug}/
```

- The namespace and profile URLs remain disabled/unapproved until public representative identity, privacy, lifecycle, ownership, and SEO purpose are approved.
- Slugs must not expose private contact data, personal identifiers, territory assumptions, employee IDs, CRM IDs, or status.
- A representative move, reassignment, deactivation, or deletion requires retention, replacement, redirect, privacy, and inquiry-routing review.
- Internal representative routing and workload never use public profile URLs as authority.

## Landing URLs

Proposed logical pattern:

```text
/{landing-root}/{landing-slug}/
```

- Only an approved unique intent receives a canonical landing.
- Landing type, source entities, inclusion rule, owner, lifecycle, canonical, indexation, and inquiry purpose are recorded.
- Campaign parameters do not create new canonical pages.
- Expired campaigns use an approved retain, redirect, consolidate, or remove decision.
- SEO Landing Categories organize governance; they do not automatically create URLs.

## Future Language Strategy

- Persian RTL remains the current presentation requirement.
- Stable content/entity IDs are language-neutral.
- Future languages add localized labels, slugs, content, canonicals, and alternate relationships without duplicating the underlying product identity by default.
- Before any additional language, approve locale codes, default-locale behavior, URL prefix/domain strategy, translation ownership, fallback, hreflang/alternate behavior, translated taxonomy, search, redirect, and migration rules.
- A future Latin-script path must not be created merely by transliterating unreviewed Persian content.
- No future-language URL shape is selected here.

## Redirect Rules

- Redirect only after identity and replacement are verified.
- Prefer one direct permanent hop from every approved former public URL to the current canonical owner when the replacement is equivalent.
- Do not redirect unrelated removed content to Home or a broad category solely to preserve traffic.
- Prevent loops, chains, wildcard overreach, cross-language mismatch, and redirects to private/non-indexable/error destinations.
- Record source, destination, reason, owner, approval, effective date, validation, and review/retirement condition.
- Update canonicals, internal links, navigation, sitemaps, breadcrumbs, search references, inquiry-source references, and external mappings with the redirect.
- Temporary redirects require explicit expiry/review evidence.

## Reserved Paths

The following logical namespaces must be reserved before real slugs are approved:

| Logical namespace | Purpose | Public/indexation boundary |
| --- | --- | --- |
| `{products-root}` | Canonical product discovery and product URLs | Public according to product/SEO approval |
| `{classification-root}` | Approved taxonomy/category landings | Conditional and type-governed |
| `{knowledge-root}` | Knowledge Center content | Public according to content/SEO approval |
| `{representatives-root}` | Conditional public representative discovery | Disabled until approved |
| `{support-root}` | Public support/help content | Public subset only |
| `{inquiry-root}` | Approved inquiry entry/confirmation functions | Confirmation/private states non-indexable |
| `{landing-root}` | Approved curated/campaign/SEO landings | Conditional and lifecycle-governed |
| `{search-root}` | Internal search interface | Non-indexable |
| `{system-reserved}` | Platform, authentication, API, asset, operational, and integration paths | Governed separately; not reused for content |

Literal namespace values and collision checks remain TODO (Founder/SEO/technical decision required).

## Forbidden URLs

- Public cart, checkout, payment, shipping-purchase, coupon, price-list, or public quote-result destinations.
- URLs containing public or confidential prices, discount values, customer identifiers, contact data, consent values, inquiry details, CRM/ERP IDs, routing rules, tokens, credentials, or internal statuses.
- Standalone canonical variation URLs without an approved exception.
- Duplicate product URLs created by category, language, brand, material, campaign, filter, or menu placement.
- Mixed-script, uncontrolled transliteration, auto-generated meaningless, date-based product, or raw database-key URLs.
- Indexable internal-search, sort, filter-combination, session, preview, staging, admin, API, feed, attachment, or error URLs unless a specific governing decision permits the public type.
- URLs that imply compatibility, certification, warranty, availability, representative territory, or commercial terms without approved evidence.

## SEO Rules

- URL eligibility, canonical, robots/indexation, sitemap, breadcrumb, pagination, alternate language, and internal-link ownership are approved together.
- No path structure alone earns indexation.
- Filter/facet combinations remain non-indexable until a unique-intent matrix approves an owned landing.
- Product structured data excludes public price and Offer behavior.
- Redirect and 404/410 choices follow semantic equivalence, lifecycle, and user value rather than blanket rules.
- Exact SEO rules remain subordinate to future approved SEO Strategy and must preserve this IA's identity boundaries.

## Examples

All examples are non-literal patterns:

| Information object | Example pattern | Canonical note |
| --- | --- | --- |
| Product hub | `/{products-root}/` | Hub canonical if approved |
| Variable Parent Product | `/{products-root}/{parent-product-slug}/` | Default product canonical |
| Product variation context | `/{products-root}/{parent-product-slug}/{selection-state}` | Non-canonical; representation pending |
| Category/term landing | `/{classification-root}/{classification-type}/{term-slug}/` | Only if the term owns an approved public intent |
| Knowledge item | `/{knowledge-root}/{content-type}/{knowledge-slug}/` | Canonical to the knowledge item |
| Representative profile | `/{representatives-root}/{representative-slug}/` | Conditional; not approved for publication |
| Curated landing | `/{landing-root}/{landing-slug}/` | Requires unique intent and lifecycle |
| Internal search | `/{search-root}/?{query}` | Non-canonical and non-indexable |

These examples approve neither English nor Persian literal roots, slugs, parameters, or permalink settings.

## Founder Decisions

- Approve, revise, or reject URL-001 through URL-008.
- Approve Persian versus transliterated/ASCII slug policy by namespace.
- Approve literal reserved roots, product/category/knowledge/landing patterns, and representative publication.
- Approve variation-state representation, future-language strategy, and redirect authority.
- Assign URL, canonical, redirect, and migration owners.

## Open Questions

- Which script/language and digit policy applies to each namespace?
- What literal reserved roots are approved and collision-free?
- Should any variation own an independent canonical URL?
- Which taxonomy and attribute views receive public URLs?
- Are public representative profiles approved?
- Which language expansion model is preferred when another language is authorized?
- Who approves and maintains redirects and canonical migrations?

## Approval Status

Review. No literal URL, slug, namespace, permalink setting, redirect, canonical tag, indexation rule, sitemap entry, or plugin configuration is approved or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 06 enterprise URL architecture; documentation only. |

## Related Documents

- [Enterprise Information Architecture](24_INFORMATION_ARCHITECTURE.md)
- [Site Structure](25_SITE_STRUCTURE.md)
- [Search and Discovery](27_SEARCH_AND_DISCOVERY.md)
- [Internal Linking Model](28_INTERNAL_LINKING_MODEL.md)
- [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md)

## Traceability

| Decision range | Origin | Dependent concerns | Future evidence |
| --- | --- | --- | --- |
| URL-001–URL-008 | IA-001–IA-007, SITE-001–SITE-007, PDM/TAX rules, CP-003–CP-006 | Site navigation, search, internal linking, SEO, future localization | Canonical inventory, slug registry, redirect map, collision check, mobile RTL, no-price, non-indexable-state, and migration validation |

Implementation status: `Not authorized`.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Information Architecture Reading Path](READING_ORDER.md#information-architecture-reading-path)
