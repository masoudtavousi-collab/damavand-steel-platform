# Product SEO Template

## Document Control

- **Document ID:** `repository/engine/product/SEO_TEMPLATE.md`
- **Status:** Review
- **Authority:** Product Engine Template
- **Owner:** Founder
- **Reviewer:** SEO Reviewer, Product Data Owner, Content Reviewer, and Qualified Domain Reviewer
- **Approval Authority:** Founder
- **Version:** 1.0.0
- **Last Updated:** 2026-08-03
- **Last Review:** 2026-08-03
- **Review Cycle:** On entity, intent, canonical, URL, metadata, internal link, schema, content, or template change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise Product Engine](PRODUCT_ENGINE.md), SEO Entity Model, URL Architecture, Internal Linking Model, and generated family data contracts
- **Dependencies:** [Product Family Template](PRODUCT_FAMILY_TEMPLATE.md), [Attribute Template](ATTRIBUTE_TEMPLATE.md), and [Engine Rules](ENGINE_RULES.md)
- **Related Documents:** [Variation Template](VARIATION_TEMPLATE.md), [Import Template](IMPORT_TEMPLATE.md), [Validation Template](VALIDATION_TEMPLATE.md), and [Engine Workflow](ENGINE_WORKFLOW.md)
- **Traceability:** URL-001 through URL-008, LINK-001 through LINK-008, SEOENT-001 through SEOENT-009, CP-005, CP-006, Sprint 03D
- **AI Compatibility:** AI-readable reusable SEO template; no AI content, keyword, metadata, FAQ answer, or schema generation is authorized
- **Approval:** Pending Founder and SEO/domain/content review; no public URL, metadata, schema, or indexation is created

## Purpose

Generate a family-specific SEO entity contract from approved product facts without creating public content, URLs, keywords, schema, or price-bearing search output.

The canonical repository source hierarchy is exactly `Catalog → Platform → Family → Series → Variant Rules → derived SKU`; SKU is not a canonical entity identity.

## Template Identity

| Field | Required generated value |
| --- | --- |
| Engine template ID | `SEO_TEMPLATE` |
| Engine template version | `1.0.0` |
| Required generated provenance | `PRODUCT_ENGINE@1.0.0` and `SEO_TEMPLATE@1.0.0` |
| Generated asset name | `{{FAMILY_KEY}}_SEO_MODEL.md` |
| Generated asset location | `repository/data/seo/` |

## Entity Definition Template

| Property | Placeholder/rule |
| --- | --- |
| Canonical repository source | `{{CATALOG_PLATFORM_FAMILY_SERIES_VARIANT_RULES_REFERENCES}}` |
| Stable Family/Series source IDs | `{{APPROVED_SOURCE_IDS_OR_TBD}}` |
| Persian/English labels | `{{APPROVED_LABELS_OR_TBD}}` |
| Downstream projection type | Legacy Product Family, Variable Parent Product, approved category/public page, or `TBD`; never canonical repository identity |
| Parent/Variation adapter IDs | `{{ADAPTER_IDS_OR_TBD}}`; never canonical repository identity |
| Source product facts | `{{GENERATED_FAMILY_AND_ATTRIBUTE_REFERENCES}}` |
| Public page/URL/search-intent owner | `{{ONE_DOWNSTREAM_OWNER_OR_TBD}}` |
| Public URL/slug | `TBD` until URL/SEO approval |
| Lifecycle/owner/reviewer | `{{VALUES_OR_TBD}}` |

## Search Intent Template

Record only evidence-backed intent classes:

| Intent | Candidate owner | Audience need | Evidence | Competing URL/entity | Status |
| --- | --- | --- | --- | --- | --- |
| `{{INTENT_OR_TBD}}` | `{{ENTITY_OR_TBD}}` | `{{NEED_OR_TBD}}` | `{{SOURCE_OR_TBD}}` | `{{CONFLICT_OR_NONE}}` | Review |

Do not invent keywords, volume, ranking, demand, or language variants. Intent does not approve indexation.

## Category SEO Contract

- Define whether the family category has unique discovery intent.
- Record content owner, inclusion rules, public-page relationship to downstream parent presentations, pagination/facet behavior, and review cycle.
- Block thin, empty, duplicate, filter-only, or unowned category pages.
- Keep category name/slug separate from product/entity identity.

## Product SEO Contract

- Approved Catalog, Platform, Family, Series, and Variant Rules references remain the source of Product identity and facts.
- A Variable Parent Product may provide the default public product-page, URL, and search-intent presentation when approved; it never owns canonical Product Repository identity.
- Variations are contextual/non-canonical and non-indexable by default.
- Parent and Variation IDs are adapter-only; any projected allowed values, axes, and tuples must resolve to approved Variant Rules.
- Product facts come only from generated/approved family and attribute assets.
- Metadata, content, media, technical documents, and schema remain projections, not fact authority.

## Attribute SEO Contract

For each generated attribute record:

| Attribute | SEO use | Landing/archive | Public page/URL/search-intent owner | Claim evidence | Notes |
| --- | --- | --- | --- | --- | --- |
| `{{ATTRIBUTE}}` | Yes/No | Prohibited/Review/Approved | `{{OWNER_OR_TBD}}` | `{{SOURCE_OR_TBD}}` | `{{BOUNDARY}}` |

Filterability never automatically grants indexation. Category, attribute archive, curated landing, product, and article cannot compete for the same intent.

## Metadata Template

| Field | Placeholder/rule |
| --- | --- |
| SEO title | `TBD` until factual content/intent approval |
| SEO description | `TBD` until factual content/intent approval |
| Canonical slug | `TBD` until namespace/language/collision approval |
| Canonical URL target | `{{ONE_APPROVED_PUBLIC_URL_OR_TBD}}`; never an identity-authority assignment |
| Robots/indexation | `TBD`; non-indexable by default until approved |
| Social metadata | `TBD`; must match approved public facts |

No template default may be published.

## FAQ Topic Template

Record candidate questions only:

| Topic ID | User question/intent | Product evidence required | Owner/reviewer | Answer status |
| --- | --- | --- | --- | --- |
| `{{TOPIC_ID}}` | `{{QUESTION_OR_TBD}}` | `{{SOURCE_OR_TBD}}` | `{{OWNER_OR_TBD}}` | `TBD`; no answer generated |

FAQ schema is prohibited until visible answers are approved, non-duplicative, eligible, and maintained.

## Internal Linking Template

- Higher approved category → family category.
- Family category → approved downstream parent presentations.
- Downstream parent presentation → family/category and approved knowledge/support.
- Approved knowledge/use-case content → relevant family/product.
- No automated links to filter states, unapproved slugs, `TBD` entities, or duplicate intent owners.

Every planned link records source, target stable ID, relationship, anchor intent, owner, lifecycle, and public eligibility.

## Schema Considerations

Document eligibility only for Organization/WebSite/Breadcrumb/Product/Collection/Article/FAQ/Image/Video or future approved types. Do not implement markup. Product schema excludes public price/Offer and unsupported stock, rating, review, brand, certification, warranty, supplier, or availability claims.

## No-Public-Price Boundary

- No price, currency, range, sale, discount, Offer, AggregateOffer, free/zero sentinel, or transaction action.
- No stock/availability promise derived from missing commercial data.
- No price-bearing metadata, structured data, feed, snippet, analytics event, or internal link context.

## SEO Validation Gates

- Stable repository source references and one downstream public page/URL/search-intent owner.
- Approved public slug policy and collision/redirect/reserved-path checks.
- Unique intent and no category/product/attribute/content cannibalization.
- Approved Persian content and Mobile First/RTL/accessibility evidence.
- Visible-content/schema parity and no unsupported claims.
- Internal-link, sitemap, robots, canonical, pagination/facet, and lifecycle review.
- Founder/SEO/domain/content approval before publication.

## Compatibility and Provenance

Version `1.0.0` is a major required-structure and semantic change under Engine Rules. Its compatibility impact is breaking for every Family with a generated 0.x SEO asset. Before use, a separately authorized migration or regeneration task must record the affected-Family/asset inventory, exact engine/template provenance, migration and validation plan, diff review, full validation, and Founder approval. No metadata, slug, URL, schema, or indexation fact is created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.1 | 2026-08-03 | Separated canonical Product Repository sources from downstream public page, URL, search-intent, Parent, and Variation projections. |
| 1.0.0 | 2026-08-03 | Major provenance-compatible template revision: required canonical source references and downstream public-page ownership; existing 0.x outputs require separately authorized review or regeneration. |

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Attribute Template](ATTRIBUTE_TEMPLATE.md)
- [Validation Template](VALIDATION_TEMPLATE.md)
- [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
