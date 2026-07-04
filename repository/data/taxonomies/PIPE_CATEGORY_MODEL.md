# Pipe Category Model

## Document Control

- **Document ID:** `repository/data/taxonomies/PIPE_CATEGORY_MODEL.md`
- **Status:** Review
- **Authority:** Product Data Taxonomy Asset
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Qualified Steel-Domain Reviewer, SEO Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On Pipe family identity, hierarchy, name, slug, URL, SEO, linking, category, or overlap decision
- **Lifecycle:** Review
- **Source of Truth:** [Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md), [Product Taxonomy Model](../../../docs/21_PRODUCT_TAXONOMY_MODEL.md), and [URL Architecture](../../../docs/26_URL_ARCHITECTURE.md)
- **Dependencies:** [Pipe Taxonomy and Attribute Classification](PIPE_TAXONOMY_ATTRIBUTE_CLASSIFICATION.md) and [Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md)
- **Related Documents:** [Pipe Attribute Model](../attributes/PIPE_ATTRIBUTE_MODEL.md), [Pipe SEO Entity Model](../seo/PIPE_SEO_ENTITY_MODEL.md), and [Pipe Data Governance Checklist](../validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md)
- **Traceability:** CP-001 through CP-010, PDM-001 through PDM-008, TAX-001 through TAX-008, IA-001 through IA-008, SITE-001 through SITE-009, URL-001 through URL-008, SEOENT-001 through SEOENT-009, Sprint 03A, and Sprint 03C
- **AI Compatibility:** AI-readable taxonomy contract; no generated terms, inferred hierarchy, or Phase 1 AI feature
- **Approval:** Pending Founder, domain, Product Data, SEO, and WooCommerce review; no category or term is configured

## Purpose

Define the minimal Pipe Product Family category model without converting technical specifications, commercial fields, SEO projections, or CRM data into categories.

## Main Category

| Property | Value | Approval state |
| --- | --- | --- |
| Logical role | Product Family category | Defined by approved product/taxonomy models |
| Persian name | لوله استیل | Supplied by Sprint 03A; Founder/domain review pending |
| English name | Stainless Steel Pipe | Supplied by Sprint 03A; Founder/domain review pending |
| Stable category ID | `TBD` | Required before implementation |
| English ASCII slug candidate | `stainless-steel-pipe` | Deterministic candidate from approved English name; not a public-slug approval |
| Approved public slug | `TBD` | Blocked by the unresolved Persian-versus-ASCII public slug policy |
| Parent category | `TBD` | Product Group/higher hierarchy is not approved |
| WooCommerce use | One future Product Family product-category term | Logical mapping only; no term created |
| Public display | Yes after approval | No page/category currently created |
| SEO indexation | `TBD` | Requires intent, content, canonical, and cannibalization review |
| Canonical owner | Product Family/category landing if later approved | Must not compete with the Variable Parent Product intent |

The ASCII slug candidate is recorded for review because Sprint 03C requires an English slug. The repository-wide URL policy has not approved English public slugs, so `canonical_slug` remains `TBD` and the candidate must not be imported or published.

## Subcategories

No Pipe subcategory is approved in Sprint 03C.

| Proposed source concept | Subcategory decision | Reason |
| --- | --- | --- |
| Grade | Do not create | Controlled global variation attribute |
| Finish | Do not create | Controlled global variation attribute; prevents finish-category/filter duplication |
| Diameter | Do not create | Typed global variation attribute |
| Thickness | Do not create | Typed global variation attribute |
| Length | Do not create | Typed global variation attribute |
| Material | Do not create | Global attribute in this Pipe profile; broader Material-category hierarchy remains unapproved |
| Brand | Do not create | Canonical global Brand identity; no verified values supplied |
| Country | Do not create | Verified origin specification, not family hierarchy |
| Application | Do not create | Global attribute in this Pipe profile; Use Case taxonomy terms remain unapproved |
| Environment | Do not create | Evidence-backed specification, not family hierarchy |
| Installation Use | Do not create | Evidence-backed specification, not family hierarchy |
| Stock/Inquiry/SEO values | Do not create | Internal behavior, commercial state, or projection—not product hierarchy |

Future subcategories require a separate Founder-approved hierarchy decision with purpose, non-overlap, terms, owner, URL, SEO, migration, and Admin evidence. Absence of subcategories is intentional and prevents unsupported hierarchy invention.

## Parent/Child Structure

```text
Approved higher Product Group/category: TBD
└── لوله استیل / Stainless Steel Pipe
    └── No approved child category
```

- The unresolved parent must not be replaced with an invented category.
- The family category must not be duplicated as a Product Type, tag, landing category, or free-text term.
- The Variable Parent Product belongs to the approved family category when implementation is later authorized; it does not become the category itself.

## Naming and Slug Rules

- Public Persian label: `لوله استیل` after Founder/domain approval.
- English internal display: `Stainless Steel Pipe`.
- ASCII slug candidate: `stainless-steel-pipe`.
- Approved public slug: `TBD` until the URL policy selects Persian or ASCII behavior and collision checks pass.
- Stable internal ID, public slug, and display labels are separate identifiers.
- Before approval, check current/former terms, products, redirects, reserved paths, Persian/Arabic variants, spacing, singular/plural, aliases, and CentralSteel mappings.
- Never mix Persian and Latin scripts in one public slug unless an explicit technical-token exception is approved.

## URL Behavior

- No concrete category URL is authorized in this sprint.
- The future category URL must follow the approved category namespace and public-slug policy in URL Architecture.
- Filter/query combinations do not create canonical category URLs automatically.
- Grade, Finish, Diameter, Thickness, Length, Brand, Country, Application, or other attribute values do not create subcategory URLs.
- Moving or renaming the category requires redirect, canonical, breadcrumb, sitemap, internal-link, analytics, inquiry-source, and external-mapping review.
- The family category and Variable Parent Product must own distinct approved intents or one must support/canonicalize according to SEO review.

## SEO Role

- Candidate role: family discovery and category-level Stainless Steel Pipe intent.
- Indexation remains `TBD`; a category term alone does not justify an indexable landing.
- Approval requires unique intent, sufficient approved Persian content, included-product rules, canonical ownership, maintained internal links, and no competing product/landing/archive.
- Attribute filter pages remain non-indexable/non-canonical by default unless separately approved.
- No price, Offer, stock promise, supplier, unsupported certification, or commercial-availability claim is allowed.

## Internal Linking Role

After separate publication approval, permitted link directions are:

- Higher approved catalog parent → Pipe family category.
- Pipe family category → approved Variable Parent Product(s).
- Approved knowledge/use-case content → Pipe family category when contextually relevant.
- Variable Parent Product → Pipe family category through breadcrumb/category context.

No links are created by this document. Anchor text, placement, and destination require the approved public URL and content state.

## WooCommerce Category Use

- Future logical object: one WooCommerce Product Category for the Pipe family.
- No category term, term ID, parent ID, count, description, image, display mode, menu placement, or SEO plugin metadata is created.
- Import must resolve an approved existing term identity; it must not auto-create a term from CSV text.
- Empty, duplicate, orphan, unowned, or unapproved category terms are rejected.

## Fields That Must Not Become Categories

`material`, `grade`, `finish`, `diameter_mm`, `thickness_mm`, `length_m`, `surface`, `unit`, `brand`, `country`, `quality_level`, `application`, `environment`, `installation_use`, `weight_per_meter`, `stock_status`, `inquiry_priority`, `inquiry_only`, `public_price`, `seo_title`, `seo_description`, `canonical_slug`, SKUs, names, product type, and internal notes must not create Pipe category terms.

The broader enterprise taxonomy model may later authorize a mapped Material, Brand, Use Case, Industry, Finish, or SEO landing representation. Such approval must reuse one canonical identity and cannot silently change this Pipe model.

## Founder Decisions Required

- Approve the family category label and scope.
- Approve the higher parent/Product Group or explicitly approve a root-level family category.
- Approve the repository-wide public slug language policy and the final Pipe category slug.
- Approve family-category versus Variable Parent Product SEO intent/canonical ownership.
- Approve indexation, content owner, internal-link role, and review cycle.
- Approve any future subcategory proposal separately.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03C minimal Pipe category model; no category implementation. |

## Navigation

- [Pipe Taxonomy and Attribute Classification](PIPE_TAXONOMY_ATTRIBUTE_CLASSIFICATION.md)
- [Pipe Attribute Model](../attributes/PIPE_ATTRIBUTE_MODEL.md)
- [Pipe SEO Entity Model](../seo/PIPE_SEO_ENTITY_MODEL.md)
- [Pipe Data Governance Checklist](../validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md)
- [Sprint 03C Audit](../../../docs/AUDIT_REPORT_SPRINT03C.md)
