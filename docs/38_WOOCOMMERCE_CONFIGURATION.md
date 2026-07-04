# WooCommerce Configuration Blueprint

## Document Control

- **Document ID:** `docs/38_WOOCOMMERCE_CONFIGURATION.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Solution Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On catalog, inquiry, product, stock, variation, attribute, customer, shipping, tax, email, quotation, pricing, or Admin-workflow change
- **Lifecycle:** Review
- **Source of Truth:** [Business Rules](03_BUSINESS_RULES.md), [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [Product Data Model](19_PRODUCT_DATA_MODEL.md), [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md), and [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)
- **Dependencies:** [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md), [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md), and [WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md)
- **Related Documents:** [Taxonomy Implementation Blueprint](40_TAXONOMY_IMPLEMENTATION.md), [Custom Fields Model](41_CUSTOM_FIELDS_MODEL.md), [Inquiry Workflow](42_INQUIRY_WORKFLOW.md), [User Roles](43_USER_ROLES.md), and [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md)
- **Traceability:** CP-001 through CP-006, CP-008 through CP-010, ADR-0001, WCM-001 through WCM-008, INQ-001 through INQ-008, WPBP-003 through WPBP-007, and WCCFG-001 through WCCFG-012
- **AI Compatibility:** AI-readable Blueprint; no AI feature or WooCommerce configuration is authorized
- **Approval:** Pending Founder/domain/Sales/technical approval; no WooCommerce setting or data is authorized

## Purpose

Define the future WooCommerce catalog configuration contract for an Inquiry First, No Public Pricing platform without changing WooCommerce.

## Scope and Boundary

This document covers logical store behavior, catalog, inquiry, transaction boundaries, products, stock, attributes, notifications, customers, Admin workflow, and future private pricing/quotation boundaries. It creates no settings, products, variations, terms, prices, orders, emails, shipping, tax, import, or code.

## WooCommerce Configuration Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| WCCFG-001 | Operate WooCommerce as the canonical product catalog, not a public transaction store. | Required by ADR-0001 and WP-FC-001 |
| WCCFG-002 | Use approved Variable Parent Products as the default product structure; exceptions follow WCM-001. | Derived from approved Product/WooCommerce models |
| WCCFG-003 | Prevent all public price, sale price, price range, Offer, cart, checkout, payment, and purchase output. | Required by CP-005, CP-006, and ADR-0001 |
| WCCFG-004 | Route every eligible product and variation context into the canonical Inquiry workflow. | Required by Inquiry First |
| WCCFG-005 | Treat cart, checkout, public order, shipping transaction, tax calculation, coupon, and payment capabilities as inactive. | Required by current business boundary |
| WCCFG-006 | Preserve approved stock states, including `supply_after_order`, without representing them as purchase promises. | Derived from Product Data Model; exact mapping pending |
| WCCFG-007 | Use approved global attributes and valid variation combinations only; local attributes require a governed exception. | Derived from ATT and WCM rules |
| WCCFG-008 | Separate Customer/Inquiry/Sales follow-up from WooCommerce account and order concepts unless a future decision maps them. | Proposed pending Founder/Sales/privacy approval |
| WCCFG-009 | Keep WooCommerce transactional emails inactive for the current public model; inquiry notifications use the approved Inquiry capability. | Proposed pending Founder/Sales/technical approval |
| WCCFG-010 | Use validated, reversible import/export through supported interfaces only after schema and ownership approval. | Derived from WCM-008 |
| WCCFG-011 | A future pricing or quotation capability must remain private, separately authorized, and unable to reactivate public commerce implicitly. | Proposed pending Founder approval |
| WCCFG-012 | Routine catalog administration must be achievable through least-privilege WordPress Admin workflows by trained non-programmers. | Required by WP-FC-005 |

## Store Architecture

```text
WooCommerce catalog
  -> Variable Parent Product
    -> valid Variation and availability context
      -> contextual Inquiry action
        -> canonical Inquiry lifecycle outside public checkout
```

WooCommerce owns catalog records and supported catalog interfaces. Business rules, product taxonomy/values, customer authority, sales qualification, quotation, and external CRM/ERP remain outside its authority unless explicitly mapped later.

## Catalog Behavior

- Publish only approved lifecycle-eligible products and valid variations.
- Show approved specifications, media, technical documents, availability wording, and inquiry action.
- Suppress transactional affordances and price-bearing metadata in every view, search result, feed, API exposure, email, template, schema, cache, and integration.
- Preserve parent canonical ownership unless a governed variation URL exception is approved.
- Exact sorting, pagination, comparison, badges, labels, and catalog visibility settings remain unresolved.

## Inquiry-Only Flow

Product, parent/variation, quantity, selected attributes, source URL, and permitted attachments pass as contextual references to the Inquiry object. The visitor can review and correct context before submission. Submission never creates a public order, checkout session, payment, or public quotation.

## Cart Policy

The cart has no role in the current public journey and must remain inactive and inaccessible. A multi-product inquiry is represented by approved inquiry line references, not by a purchasable cart. Exact implementation mechanism remains unselected.

## Checkout Policy

Checkout, payment, billing, shipping purchase, coupons, tax calculation, and order-confirmation pages are outside the current public platform. No redirect or suppression configuration is specified here.

## Order Lifecycle

WooCommerce public order lifecycle is `Not applicable` for the current architecture. An Inquiry and a future private Quotation are not WooCommerce Orders unless a later approved architecture explicitly defines that mapping, authority, privacy, statuses, migration, and no-public-pricing safeguards.

## Stock Policy

Approved domain stock states remain: `in_stock`, `limited`, `supply_after_order`, `temporarily_unavailable`, and `discontinued`. A future mapping must define WooCommerce stock-management flags, quantities, backorders, visibility, inquiry eligibility, wording, source authority, synchronization, and stale-data behavior. `supply_after_order` means supply may be investigated after inquiry; it is not a backorder sale or delivery promise.

## Variation Strategy

- Parent owns shared identity, canonical content, family/type context, and common media/documents.
- Variation owns valid selectable values, stable identifier/SKU, variation-specific availability, and approved overrides.
- Only approved attribute combinations exist; no Cartesian generation by default.
- Exact variation axes, limits, default selections, image behavior, and invalid-combination messages remain domain decisions.

## Attribute Strategy

The global attribute registry in the Product Attribute Model is canonical. Attribute terms require approved English internal key, Persian label, value policy, unit/normalization, variation/filter/SEO permissions, owner, lifecycle, and migration mapping. Size remains derived unless the governing model is revised.

## Shipping Architecture

Public shipping rates, zones, methods, classes, addresses, estimates, and purchase commitments are inactive because checkout is inactive. Logistics requirements may be collected as protected inquiry data only after field and privacy approval. Future shipping architecture requires a separate business decision.

## Tax Architecture

Public tax calculation and tax-inclusive/exclusive price display are inactive because no public price or checkout exists. Legal/accounting treatment for a future private quotation is outside this Blueprint and requires qualified review.

## Email Architecture

WooCommerce order/customer transaction emails have no current public lifecycle. Inquiry receipt, routing, assignment, escalation, failure, and follow-up notifications belong to the Inquiry Workflow and approved outbound-mail capability. Exact templates, recipients, content, retention, retry, and service levels remain unresolved.

## Customer Lifecycle

Guest inquiry is the current public interaction concept. A Customer is a protected logical entity linked to inquiries under the Inquiry Data Model; it is not automatically a WooCommerce account. Registration, login, account pages, consent, identity matching, data rights, and future CRM authority remain decisions.

## Admin Workflow

1. Create or update catalog data only from approved source values.
2. Validate parent/variation, identifiers, terms, media, documents, lifecycle, availability, and inquiry eligibility.
3. Review no-price/no-transaction output, Persian RTL, mobile, accessibility, SEO, and canonical behavior.
4. Obtain required domain/editorial approval before publication.
5. Monitor inquiry context integrity and stale/broken catalog relations.
6. Suspend or archive through the approved lifecycle with redirects and relationship review.

Exact roles and approval stages remain pending.

## Future Pricing Engine

A future pricing engine is not authorized. Evaluation requires private/public boundary, source authority, currency/unit/tax rules, permissions, expiry, audit, security, integration, cache/schema/email/feed suppression, fallback, and rollback decisions. It cannot weaken CP-005.

## Future Quotation Engine

A future quotation capability may consume an approved Inquiry and create a protected commercial artifact after assignment. It requires quotation identity, statuses, line/version rules, validity, approvals, access, delivery, acceptance/rejection, CRM/ERP/accounting boundaries, retention, and audit decisions. It must not publish prices or become public checkout.

## Founder Decisions

- Approve, revise, or reject WCCFG-001 through WCCFG-012.
- Approve exact WooCommerce versions, catalog visibility, stock mapping, product/variation rules, customer-account policy, and Admin workflow.
- Approve the technical enforcement and validation approach for removing all public transaction and price output.
- Keep private pricing and quotation as separate future decisions.

## Open Questions

- How will every WooCommerce surface, API, feed, email, schema, cache, and extension be verified as price-free and transaction-free?
- What exact stock/availability mapping and wording are approved?
- Which catalog roles, publication gates, import/export schemas, and rollback rules are authorized?
- Are WooCommerce customer accounts excluded or required for any future protected journey?

## Approval Status

Review. No WooCommerce setting, product, variation, attribute, price, stock value, cart, checkout, order, shipping, tax, email, account, import, quotation, or pricing engine is configured or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 08 WooCommerce configuration Blueprint; documentation only. |

## Related Documents

- [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md)
- [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)
- [Inquiry Workflow](42_INQUIRY_WORKFLOW.md)
- [Taxonomy Implementation Blueprint](40_TAXONOMY_IMPLEMENTATION.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| WCCFG-001–WCCFG-012 | CP-001–CP-006, CP-008–CP-010, ADR-0001, PDM/WCM/TAX/ATT/INQ rules | Taxonomy, fields, inquiry, roles, plugins, and future WooCommerce implementation plan | Compatibility/configuration inventory, catalog data fixtures, exhaustive no-price/no-transaction surface checks, inquiry context, RTL/mobile/accessibility, Admin workflow, import/rollback evidence |

Implementation status: `Not authorized`.
