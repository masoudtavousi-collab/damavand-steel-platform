# Product SEO Template

## Document Control

- **Document ID:** `repository/engine/product/SEO_TEMPLATE.md`
- **Status:** Review
- **Authority:** Product Engine Template
- **Owner:** Founder
- **Reviewer:** SEO Reviewer, Product Data Owner, Content Reviewer, and Qualified Domain Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
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

## Template Identity

| Field | Required generated value |
| --- | --- |
| Engine template ID | `SEO_TEMPLATE` |
| Engine template version | `0.1.0` |
| Generated asset name | `{{FAMILY_KEY}}_SEO_MODEL.md` |
| Generated asset location | `repository/data/seo/` |

## Entity Definition Template

| Property | Placeholder/rule |
| --- | --- |
| Stable entity/family ID | `{{ID_OR_TBD}}` |
| Persian/English labels | `{{APPROVED_LABELS_OR_TBD}}` |
| Entity type | Product Family, Variable Parent Product, approved category, or `TBD` |
| Source product facts | `{{GENERATED_FAMILY_AND_ATTRIBUTE_REFERENCES}}` |
| Canonical owner | `{{ONE_OWNER_OR_TBD}}` |
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
- Record content owner, inclusion rules, canonical relationship to parent products, pagination/facet behavior, and review cycle.
- Block thin, empty, duplicate, filter-only, or unowned category pages.
- Keep category name/slug separate from product/entity identity.

## Product SEO Contract

- Variable Parent Product is canonical by default unless an approved exception exists.
- Variations are contextual/non-canonical and non-indexable by default.
- Product facts come only from generated/approved family and attribute assets.
- Metadata, content, media, technical documents, and schema remain projections, not fact authority.

## Attribute SEO Contract

For each generated attribute record:

| Attribute | SEO use | Landing/archive | Canonical owner | Claim evidence | Notes |
| --- | --- | --- | --- | --- | --- |
| `{{ATTRIBUTE}}` | Yes/No | Prohibited/Review/Approved | `{{OWNER_OR_TBD}}` | `{{SOURCE_OR_TBD}}` | `{{BOUNDARY}}` |

Filterability never automatically grants indexation. Category, attribute archive, curated landing, product, and article cannot compete for the same intent.

## Metadata Template

| Field | Placeholder/rule |
| --- | --- |
| SEO title | `TBD` until factual content/intent approval |
| SEO description | `TBD` until factual content/intent approval |
| Canonical slug | `TBD` until namespace/language/collision approval |
| Canonical target | `{{ONE_APPROVED_ENTITY_OR_TBD}}` |
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
- Family category → approved parent products.
- Parent product → family/category and approved knowledge/support.
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

- Stable entity and one canonical owner.
- Approved public slug policy and collision/redirect/reserved-path checks.
- Unique intent and no category/product/attribute/content cannibalization.
- Approved Persian content and Mobile First/RTL/accessibility evidence.
- Visible-content/schema parity and no unsupported claims.
- Internal-link, sitemap, robots, canonical, pagination/facet, and lifecycle review.
- Founder/SEO/domain/content approval before publication.

## Navigation

- [Enterprise Product Engine](PRODUCT_ENGINE.md)
- [Attribute Template](ATTRIBUTE_TEMPLATE.md)
- [Validation Template](VALIDATION_TEMPLATE.md)
- [Engine Generation Guide](ENGINE_GENERATION_GUIDE.md)
