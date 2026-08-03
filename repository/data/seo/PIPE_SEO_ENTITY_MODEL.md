# Stainless Steel Pipe SEO Entity Model

## Document Control

- **Document ID:** `repository/data/seo/PIPE_SEO_ENTITY_MODEL.md`
- **Status:** Review
- **Authority:** Product Data Asset
- **Owner:** Founder
- **Reviewer:** SEO Reviewer, Product Data Owner, and Qualified Steel-Domain Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.1
- **Last Updated:** 2026-08-03
- **Last Review:** 2026-08-03
- **Review Cycle:** On entity identity, search intent, canonical, indexation, attribute use, FAQ, schema, internal linking, or public-data boundary change
- **Lifecycle:** Review
- **Source of Truth:** [Enterprise SEO Entity Model](../../../docs/34_SEO_ENTITY_MODEL.md), [URL Architecture](../../../docs/26_URL_ARCHITECTURE.md), and [Stainless Steel Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md)
- **Dependencies:** [Product Data Model](../../../docs/19_PRODUCT_DATA_MODEL.md), [Product Taxonomy Model](../../../docs/21_PRODUCT_TAXONOMY_MODEL.md), and [Attribute Dictionary](../attributes/ATTRIBUTE_DICTIONARY.md)
- **Related Documents:** [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md), [Pipe Import Template](../imports/woocommerce/PIPE_IMPORT_TEMPLATE.csv), and [Product Data Validation Rules](../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- **Traceability:** CP-005, CP-006, URL-001 through URL-008, SEOENT-001 through SEOENT-009, WCM-005, and Sprint 03A
- **AI Compatibility:** AI-readable SEO entity contract; future retrieval compatibility only and no Phase 1 AI implementation
- **Approval:** Pending Founder, SEO, Product Data, content, UX, and steel-domain review; no URL, metadata, schema, or landing is published

## Entity Definition

The canonical Repository source follows `Catalog → Platform → Family → Series → Variant Rules → SKU`. This SEO asset defines only downstream public-page, URL, and search-intent projections; it cannot create or own Product truth.

| Field | Value |
| --- | --- |
| Canonical Repository source | Approved Family/Series/Variant Rules references; no Product record is created here |
| Public SEO projection type | Legacy Product Family landing and candidate Variable Parent Product page |
| Persian label | لوله استیل |
| English label | Stainless Steel Pipe |
| Stable public SEO/mapping ID | `TBD`; not a canonical Repository entity identity |
| Candidate public page/URL owner | Variable Parent Product page for product intent; family/category landing ownership requires SEO decision |
| Canonical URL/slug | `TBD` |
| Indexation | `TBD`; not approved by this asset |
| Public price | Prohibited |
| Inquiry action | Required contextual relationship |

The family, category landing, Variable Parent Product, attribute archives, and knowledge content must not compete for the same search intent.

## Search Intent

| Intent class | Candidate public page/intent owner | Boundary |
| --- | --- | --- |
| Family discovery | Approved downstream Family/category landing projection | Exact landing/URL/indexation `TBD`; no Repository identity ownership |
| Product specification | Variable Parent Product page | Grade/Finish/Dimensions are projected from approved sources; variation URLs are not canonical by default |
| Grade comparison | Approved knowledge/FAQ content or parent guidance | No unsupported metallurgy/suitability claim |
| Finish selection | Parent or approved explanatory content | Finish/color/coating distinctions require domain evidence |
| Dimension discovery | Parent plus structured attributes | Filter combinations are non-canonical by default |
| Application/use | Approved Application taxonomy/landing or knowledge content | Suitability evidence and one canonical public page/intent owner required |
| Commercial intent | Contextual inquiry destination | No public price, quote result, cart, checkout, or payment intent |

Keywords, search volume, ranking opportunity, content owner, and landing assignments remain `TBD`.

## Category SEO

- A legacy Product Family/category presentation may summarize Stainless Steel Pipe and link to its approved public Parent-page set after approval; it does not own canonical Family or Product identity.
- Category content must provide unique user value and must not merely duplicate the parent description.
- Category, Material, Grade, Finish, Application, and Brand classifications require distinct authority and cannibalization review.
- Filter-generated combinations remain non-indexable/non-canonical by default.
- Category title, description, slug, canonical, breadcrumb, schema, and indexation are `TBD`.
- No price, supplier, stock promise, certification, or unsupported suitability claim is permitted.

## Product SEO

- The Variable Parent Product page owns shared public presentation/search-intent context and may own the default canonical public URL; it never owns canonical Repository Product identity or truth.
- Variation selections remain contextual parameters/state and do not create independent canonical pages by default.
- Parent-page metadata may project only approved canonical Family/Series/Variant Rules facts and separately verified attributes.
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
| Application | Supporting relationship after verified suitability | `TBD`; one canonical public page/intent owner required |
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

- Family/category presentation links to the canonical public Parent-page URL and approved knowledge/FAQ resources.
- Parent links to contextual inquiry and approved supporting documents/content.
- Knowledge content links back to the approved canonical public Family/Parent-page URL only when contextually relevant; the link target does not become Repository authority.
- Attribute/filter states link to the canonical public Parent-page URL rather than creating uncontrolled landing pages.
- Anchor text is accurate Persian RTL and does not promise price, stock, delivery, certification, or suitability.
- Links never expose private inquiry, CRM, supplier, price, or internal availability data.
- Redirects, parameters, search results, and duplicate archives are not internal-link targets.

## Schema Considerations

| Schema type | Eligibility | Boundary |
| --- | --- | --- |
| Product | Candidate semantic projection on an approved Variable Parent Product page | Projection must reference approved Repository sources; no Offer, price, currency, sale, aggregate offer, or purchase action |
| BreadcrumbList | Candidate after hierarchy/URL approval | Must reflect canonical navigation, not every mutable classification |
| FAQPage | Conditional | Only visible, reviewed, non-duplicated FAQ content |
| Organization | Site-level publisher relationship | Governed by Organization authority, not product data |
| ImageObject | Conditional | Rights, alt text, identity, and product relationship required |
| CollectionPage | Conditional family/category landing | Requires unique intent and approved canonical public page/intent owner |

No schema output is implemented. Stock/availability schema is prohibited until public eligibility, semantics, and no-promise behavior are explicitly approved.

## Canonical Rules

- One approved public page/URL owner per search intent; this SEO rule does not define canonical Repository entity ownership.
- A Variable Parent Product page may own the default public product-page canonical URL only; it never becomes the owner of shared Product identity and never writes back Product truth.
- Variations, filters, sorting, search, tracking parameters, and attribute selections are non-canonical by default.
- SKU, internal ID, attribute key, and external mapping are not public slugs.
- Slug is `TBD`; do not mix Persian and Latin scripts without an approved namespace rule.
- Canonical-URL changes require redirect, sitemap, breadcrumb, internal-link, inquiry-source, analytics, and external-mapping review.
- Canonical-URL and indexation decisions are separate.

## No Public Pricing Constraints

- No price, range, discount, currency, Offer, AggregateOffer, sale, cart, checkout, payment, shipping purchase, or price-derived statement.
- No price in HTML, structured data, metadata, Open Graph, feeds, APIs, caches, analytics, images, PDFs, filenames, or public exports.
- Inquiry content may invite a commercial request but cannot calculate or return public pricing.
- Empty price is required; `0`, `free`, `TBD`, `hidden`, and sentinel numbers are not substitute prices.

## SEO Readiness Gates

- Canonical Family/Series/Variant Rules source references and separate downstream page/Parent mapping IDs approved.
- Canonical public-URL namespace and slug approved.
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
| 0.1.1 | 2026-08-03 | Separated canonical Repository identity from downstream page, URL, search-intent, Schema.org, and Variable Parent projections under `FD-W2G-001`; no URL, SEO fact, Product, mapping, schema output, or runtime object was created. |

## Navigation

- [Stainless Steel Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md)
- [Attribute Dictionary](../attributes/ATTRIBUTE_DICTIONARY.md)
- [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md)
- [Product Data Validation Rules](../validation/PRODUCT_DATA_VALIDATION_RULES.md)
- [Sprint 03A Audit](../../../docs/AUDIT_REPORT_SPRINT03A.md)
