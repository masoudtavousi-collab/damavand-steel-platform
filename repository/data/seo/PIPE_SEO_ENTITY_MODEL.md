# Stainless Steel Pipe SEO Entity Model

## Document Control

- **Document ID:** `repository/data/seo/PIPE_SEO_ENTITY_MODEL.md`
- **Status:** Review
- **Authority:** Product Data Asset
- **Owner:** Founder
- **Reviewer:** SEO Reviewer, Product Data Owner, and Qualified Steel-Domain Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On entity identity, search intent, canonical, indexation, attribute use, FAQ, schema, internal linking, or public-data boundary change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise SEO Entity Model](../../../docs/34_SEO_ENTITY_MODEL.md), [URL Architecture](../../../docs/26_URL_ARCHITECTURE.md), and [Stainless Steel Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md)
- **Dependencies:** [Product Data Model](../../../docs/19_PRODUCT_DATA_MODEL.md), [Product Taxonomy Model](../../../docs/21_PRODUCT_TAXONOMY_MODEL.md), and [Attribute Dictionary](../attributes/ATTRIBUTE_DICTIONARY.md)
- **Related Documents:** [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md), [Pipe Import Template](../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv), and [Product Data Validation Rules](../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- **Traceability:** CP-005, CP-006, URL-001 through URL-008, SEOENT-001 through SEOENT-009, WCM-005, and Sprint 03A
- **AI Compatibility:** AI-readable SEO entity contract; future retrieval compatibility only and no Phase 1 AI implementation
- **Approval:** Pending Founder, SEO, Product Data, content, UX, and steel-domain review; no URL, metadata, schema, or landing is published

## Entity Definition

| Field | Value |
| --- | --- |
| Entity type | Product Family and candidate Variable Parent Product |
| Persian label | لوله استیل |
| English label | Stainless Steel Pipe |
| Stable entity ID | `TBD` |
| Canonical owner | Candidate Variable Parent Product for product intent; family/category landing ownership requires SEO decision |
| Canonical URL/slug | `TBD` |
| Indexation | `TBD`; not approved by this asset |
| Public price | Prohibited |
| Inquiry action | Required contextual relationship |

The family, category landing, Variable Parent Product, attribute archives, and knowledge content must not compete for the same search intent.

## Search Intent

| Intent class | Candidate owner | Boundary |
| --- | --- | --- |
| Family discovery | Approved Product Family/category landing | Exact landing/URL/indexation `TBD` |
| Product specification | Variable Parent Product | Grade/Finish/Dimensions support the parent; variation URLs are not canonical |
| Grade comparison | Approved knowledge/FAQ content or parent guidance | No unsupported metallurgy/suitability claim |
| Finish selection | Parent or approved explanatory content | Finish/color/coating distinctions require domain evidence |
| Dimension discovery | Parent plus structured attributes | Filter combinations are non-canonical by default |
| Application/use | Approved Application taxonomy/landing or knowledge content | Suitability evidence and one canonical owner required |
| Commercial intent | Contextual inquiry destination | No public price, quote result, cart, checkout, or payment intent |

Keywords, search volume, ranking opportunity, content owner, and landing assignments remain `TBD`.

## Category SEO

- Product Family/category identity may summarize Stainless Steel Pipe and link to its canonical parent/product set after approval.
- Category content must provide unique user value and must not merely duplicate the parent description.
- Category, Material, Grade, Finish, Application, and Brand classifications require distinct authority and cannibalization review.
- Filter-generated combinations remain non-indexable/non-canonical by default.
- Category title, description, slug, canonical, breadcrumb, schema, and indexation are `TBD`.
- No price, supplier, stock promise, certification, or unsupported suitability claim is permitted.

## Product SEO

- The Variable Parent Product owns shared product identity and default canonical URL.
- Variation selections remain contextual parameters/state and do not create independent canonical pages by default.
- Parent metadata may use only approved family/type facts and verified attributes.
- Exact `seo_title`, `seo_description`, and `canonical_slug` remain `TBD` in the import template.
- Product publication requires lifecycle, content, media, technical, inquiry, no-price, mobile RTL, and canonical validation.

## Attribute SEO

| Attribute | Permitted role | Indexable archive/landing |
| --- | --- | --- |
| Material | Supporting fact and possible approved material intent | `TBD`; not automatic |
| Grade | Supporting specification and possible approved comparison intent | `TBD`; not automatic |
| Finish | Supporting specification and possible approved finish intent | `TBD`; not automatic |
| Diameter | Structured specification/filter context | No by default |
| Thickness | Structured specification/filter context | No by default |
| Length | Structured specification/filter context | No by default |
| Application | Supporting relationship after verified suitability | `TBD`; one canonical owner required |
| Brand/Country/Quality | Only after verified evidence and authority | No by default |

Attribute values never become keyword pages merely because they exist in WooCommerce.

## FAQ Topics

Candidate topics only; answers and technical claims require qualified review:

- تفاوت گریدهای ارائه‌شده برای لوله استیل چیست؟
- چگونه قطر، ضخامت و طول مورد نیاز برای استعلام مشخص می‌شود؟
- تفاوت Silver، Gold PVD و Black PVD در این کاتالوگ چیست؟
- برای استعلام لوله استیل چه اطلاعاتی باید ارسال شود؟
- آیا همه ترکیب‌های گرید، پرداخت و ابعاد قابل تأمین هستند؟
- واحد ثبت مقدار و طول در استعلام چیست؟
- مدارک فنی و تصاویر هر محصول چگونه بررسی می‌شوند؟

FAQ eligibility requires visible, non-duplicated, user-facing questions and reviewed answers. FAQ schema is not automatic.

## Internal Linking Rules

- Family/category links to the canonical parent and approved knowledge/FAQ resources.
- Parent links to contextual inquiry and approved supporting documents/content.
- Knowledge content links back to the canonical family/parent only when contextually relevant.
- Attribute/filter states link to the parent canonical rather than creating uncontrolled landing pages.
- Anchor text is accurate Persian RTL and does not promise price, stock, delivery, certification, or suitability.
- Links never expose private inquiry, CRM, supplier, price, or internal availability data.
- Redirects, parameters, search results, and duplicate archives are not internal-link targets.

## Schema Considerations

| Schema type | Eligibility | Boundary |
| --- | --- | --- |
| Product | Candidate for approved Variable Parent Product | No Offer, price, currency, sale, aggregate offer, or purchase action |
| BreadcrumbList | Candidate after hierarchy/URL approval | Must reflect canonical navigation, not every mutable classification |
| FAQPage | Conditional | Only visible, reviewed, non-duplicated FAQ content |
| Organization | Site-level publisher relationship | Governed by Organization authority, not product data |
| ImageObject | Conditional | Rights, alt text, identity, and product relationship required |
| CollectionPage | Conditional family/category landing | Requires unique intent and approved canonical owner |

No schema output is implemented. Stock/availability schema is prohibited until public eligibility, semantics, and no-promise behavior are explicitly approved.

## Canonical Rules

- One approved canonical owner per product entity or search intent.
- Variable Parent Product owns the product canonical by default.
- Variations, filters, sorting, search, tracking parameters, and attribute selections are non-canonical by default.
- SKU, internal ID, attribute key, and external mapping are not public slugs.
- Slug is `TBD`; do not mix Persian and Latin scripts without an approved namespace rule.
- Canonical changes require redirect, sitemap, breadcrumb, internal-link, inquiry-source, analytics, and external-mapping review.
- Canonical and indexation decisions are separate.

## No Public Pricing Constraints

- No price, range, discount, currency, Offer, AggregateOffer, sale, cart, checkout, payment, shipping purchase, or price-derived statement.
- No price in HTML, structured data, metadata, Open Graph, feeds, APIs, caches, analytics, images, PDFs, filenames, or public exports.
- Inquiry content may invite a commercial request but cannot calculate or return public pricing.
- Empty price is required; `0`, `free`, `TBD`, `hidden`, and sentinel numbers are not substitute prices.

## SEO Readiness Gates

- Stable entity/family/parent identity approved.
- Canonical namespace and slug approved.
- Search intent and competing-owner analysis approved.
- Persian content and domain claims reviewed.
- Media rights/alt text and technical documents approved.
- Inquiry action works without price/transaction exposure.
- Mobile Persian RTL, accessibility, performance, robots, sitemap, canonical, schema, and internal links validated.
- No-price checks pass every public surface.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03A SEO entity model for Stainless Steel Pipe. |

## Navigation

- [Stainless Steel Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md)
- [Attribute Dictionary](../attributes/ATTRIBUTE_DICTIONARY.md)
- [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md)
- [Product Data Validation Rules](../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- [Sprint 03A Audit](../../../docs/AUDIT_REPORT_SPRINT03A.md)
