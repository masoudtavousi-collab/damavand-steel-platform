# WooCommerce Product Model

## Document Control

- **Document ID:** `docs/20_WOOCOMMERCE_PRODUCT_MODEL.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.2.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On WooCommerce product, variation, SKU, attribute, visibility, price, inquiry, stock, import/export, or Admin-policy change
- **Lifecycle:** Review
- **Source of Truth:** [ADR 0001](adr/0001-inquiry-first-commerce.md), [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#woocommerce-responsibilities), and WP-FC-001/WP-FC-004
- **Dependencies:** [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), and [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md)
- **Related Documents:** [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md), [Business Rules](03_BUSINESS_RULES.md), and [Traceability Matrix](TRACEABILITY_MATRIX.md)
- **Traceability:** CP-001 through CP-006, CP-008 through CP-010, WP-FC-001, WP-FC-004, WP-FC-005, WP-ARC-004, WP-ARC-007, and WCM-001 through WCM-008
- **AI Compatibility:** AI-readable with explicit no-setting, no-price, and no-import boundaries
- **Approval:** Pending Founder approval

## Purpose

Define how the approved logical product model maps to WooCommerce concepts while preserving Variable Parent Product, inquiry-first commerce, hidden pricing, Admin manageability, and future system compatibility.

## Scope

This document defines mapping policy only. It does not create products, fields, settings, templates, buttons, imports, code, database structures, or plugin configuration.

## WooCommerce Model Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| WCM-001 | Variable products are the required governed catalog type; Simple products require a future explicit exception. | Proposed mapping of accepted WP-FC-004 |
| WCM-002 | Parent products own shared catalog content; variations own configuration-specific data. | Proposed pending Founder approval |
| WCM-003 | Operationally distinct variations require unique SKUs; parent identifiers remain separate from variation SKUs. | Proposed pending Founder approval |
| WCM-004 | Reusable specifications and variation axes use approved global attributes. | Proposed pending Founder approval |
| WCM-005 | Public product output omits pricing and transaction actions and exposes contextual inquiry only. | Required by CP-005, CP-006, and ADR-0001 |
| WCM-006 | `supply_after_order` availability may accept inquiry without representing stock, backorder purchase, lead time, or supply guarantee. | Proposed pending Founder/Sales approval |
| WCM-007 | Imports and exports require Admin-reviewable contracts, dry-run validation, stable IDs, and recovery evidence. | Proposed pending Founder approval |
| WCM-008 | A local product attribute requires a governed exception record, duplicate check, owner, review/expiry condition, and migration trigger. | Proposed pending Founder/Product approval |

## Simple vs Variable Product Policy

| WooCommerce concept | Policy |
| --- | --- |
| Variable product | Required for governed Damavand Steel products under WP-FC-004, including parent records with controlled configuration axes |
| Variation | Required representation of an approved configuration or operationally distinct catalog option |
| Simple product | Not approved for the governed product catalog; a future exception requires Founder decision, rationale, traceability, and migration impact |
| Grouped, external/affiliate, subscription, bookable, or other product type | Not approved or assumed by Batch 05 |

A product with only one currently valid configuration still follows the Variable Parent Product policy unless the Founder explicitly changes WP-FC-004. This model does not configure WooCommerce behavior.

## Parent Product Rules

A parent product owns:

- Stable product ID and separate parent reference code when approved.
- Product Family, Product Group, and Product Type relationships.
- Shared Persian title, summary, full narrative, approved shared specifications, and inquiry guidance.
- Approved variation axes and valid-combination policy.
- Shared Media Set and Technical Documents, with variation overrides only when required.
- Shared SEO reference and canonical ownership.
- Related-product relationships with explicit meaning.
- Public visibility and lifecycle state.

A parent product must not:

- Represent a public price, price range, sale, discount, cart action, checkout action, payment, or shipping purchase.
- Publish an empty or invalid variation matrix.
- Duplicate variation-specific SKU, stock state, documents, or specifications as authoritative shared values.
- use free-text attributes when a governed global value exists.

## Variation Rules

Every variation:

- Belongs to exactly one Variable Parent Product.
- Uses an approved combination of parent-declared global variation attributes.
- Has stable internal identity and, when operationally distinct, a unique SKU.
- Carries only configuration-specific data such as dimensions, finish, color, stock state, media, documents, external mapping, or inquiry eligibility.
- Inherits shared content without duplicating it as a second authority.
- Remains unpublished or unavailable when required values, review, media, documents, or mappings are incomplete.
- Never introduces a public price or transaction path.

Invalid, impossible, duplicate, technically incompatible, or unapproved combinations must not be published. The exact combination matrix requires qualified steel-domain approval.

## SKU Policy

- Variation SKU is the operational SKU when a variation is independently referenced, supplied, stocked, quoted, or integrated.
- Parent reference code identifies the family-level catalog entity and must not collide with variation SKUs.
- SKU values are stable, unique, case policy-controlled, and never reused for a different entity.
- SKU is not a public URL key, database key, taxonomy term, or translated label.
- Exact syntax, segment meanings, check rules, legacy mapping, and ERP ownership remain Founder/Operations decisions.
- SKU changes require impact review for inquiries, exports, documents, media, analytics, CRM, ERP, and CentralSteel mappings.

## Attribute Rules

- Use global WooCommerce attributes for reusable controlled values.
- An attribute profile defines which attributes apply to each Product Type.
- Variation axes are a strict subset of applicable global attributes.
- Descriptive/filter-only attributes must not generate unnecessary variations.
- Numeric dimensions retain value, unit, and dimensional context; composite Size is not a replacement for structured values.
- Local product attributes require an approved exception showing that the value is genuinely product-specific and not reusable.
- Exact values and WooCommerce option flags remain unconfigured until approval.

### Local Attribute Exception Record

Every proposed local attribute must record:

- Stable exception ID and affected Variable Parent Product.
- Attribute label, meaning, value type, and reason a global attribute is unsuitable.
- Duplicate search against canonical attributes, aliases, local exceptions, and pending proposals.
- Accountable owner, reviewer, approval authority, decision date, and status.
- Review date or expiry condition.
- Migration trigger, including reuse by another product, integration need, filtering need, variation reuse, or taxonomy overlap.
- Impact on variations, inquiries, imports/exports, SEO, CRM, ERP, and CentralSteel mappings.
- Replacement or migration evidence when the exception ends.

The owner and approval authority are TODO (Founder Decision Required). An exception does not permit uncontrolled term creation and never becomes a second authority for an existing global concept.

## Global Attribute Policy

The canonical attributes are governed by [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md). Future WooCommerce implementation must:

- Reuse the approved English internal key and Persian label.
- Preserve one canonical term per concept.
- Prevent duplicate spelling, spacing, script, unit, and synonym variants.
- Distinguish specification, variation, filtering, visibility, and SEO use.
- Restrict term creation to authorized Admin roles.
- Record external mappings without replacing the canonical internal identity.

## Product Visibility Policy

| Product lifecycle or availability condition | Proposed visibility boundary |
| --- | --- |
| Product lifecycle `draft` | Admin-only; not public or indexable |
| Product lifecycle `review` | Reviewer access only; no public authority |
| Product lifecycle `approved` and inquiry-eligible | Public catalog visibility according to approved SEO/indexation policy |
| Product lifecycle `approved` but not inquiry-eligible | Informational or hidden behavior requires explicit Product/Sales decision |
| Product lifecycle `suspended` | Hidden or informational behavior requires Product/SEO approval; prior visibility is not retained automatically |
| Product lifecycle `discontinued` | Hidden, historical, replacement, redirect, and inquiry behavior requires SEO, Sales, and Product approval |
| Product lifecycle `archived` | Not operational or public unless a separately approved historical-content policy applies |
| Stock state `temporarily_unavailable` while lifecycle is `approved` | Visibility and inquiry behavior follow approved stock-state policy; no false availability |

The canonical product states and transitions are defined in [Proposed Product Lifecycle](19_PRODUCT_DATA_MODEL.md#proposed-product-lifecycle). Stock State never changes lifecycle automatically. Search visibility, catalog visibility, direct-link visibility, taxonomy archives, sitemap inclusion, and indexation are separate decisions. Batch 05 does not set WooCommerce visibility options.

## Hidden Price Rules

- No public regular price, sale price, price range, currency amount, discount, offer, or price-derived message.
- No price-bearing product schema, Open Graph content, feed, API response, search index, cache fragment, analytics event, export intended for public use, or rendered source.
- No cart, mini-cart, add-to-cart, checkout, payment, or shipping-purchase action.
- Admin or future integration handling of confidential pricing requires a separate approved security and architecture decision; it is not defined here.
- Future public or customer-specific pricing requires a superseding Founder decision and ADR-0001 review.

## Inquiry Action Rules

The product action is contextual inquiry, not purchase.

- Parent pages provide a clear Persian RTL, mobile-first inquiry action.
- When variation attributes are required, the action passes the selected valid variation or explicitly records unresolved selections.
- Inquiry context includes stable parent/variation IDs, submission-time labels, selected attributes, quantity/unit, source URL, and approved media/document references when relevant.
- The action remains usable for `supply_after_order` without presenting purchase, price, or delivery certainty.
- Exact Persian button label, placement, sticky mobile behavior, validation messages, and capability owner require UX/Founder approval.
- No button, form, or plugin is created or selected by this model.

## Out-of-Stock and Supply-After-Order Policy

`supply_after_order` is distinct from WooCommerce backorders and from current stock.

- It means supply or production may be investigated after inquiry and commercial acceptance.
- Public messaging must request confirmation and must not promise availability, lead time, quantity, price, or acceptance.
- Inquiry remains available when approved by Sales/Product policy.
- The product must not appear purchasable or marked as immediately in stock.
- Exact WooCommerce stock-status mapping, labels, filters, and transitions are pending decisions.

## Product Import and Export Strategy

Future import/export capability must provide:

- Versioned data contract and field dictionary.
- Stable IDs and external mapping keys.
- UTF-8 Persian support and explicit slug-language policy.
- Controlled taxonomy/attribute term matching without automatic uncontrolled creation.
- Parent-before-variation dependency validation.
- SKU uniqueness and variation-combination validation.
- Dry-run, row-level errors, warnings, impact summary, reviewer approval, and recovery plan.
- Media/document reference validation without embedding unapproved files.
- No public pricing columns or price import behavior under current rules.
- Export scope, access, personal/confidential data controls, and audit evidence.

No CSV, spreadsheet template, import file, mapping, plugin, scheduled job, or database operation is created in Batch 05.

## Admin Manageability Constraints

- Routine parent, variation, attribute, visibility, stock-state, inquiry-eligibility, media, document, and relationship management must be available through supported WordPress Admin workflows.
- The Founder must not need code, SQL, command line, direct database access, or vendor-file editing.
- Admin labels and help text must support Persian RTL while internal keys remain stable.
- Interfaces must prevent invalid combinations and uncontrolled term creation where possible.
- Bulk changes require preview, dry-run, validation, explicit approval, and recovery evidence.
- Advanced technical integration and migration tasks remain assigned to qualified administrators.

## WooCommerce Compatibility Boundaries

- Use supported WooCommerce product, variation, attribute, taxonomy, media, visibility, inventory, import/export, and API concepts.
- Avoid direct storage assumptions; future implementation uses supported Admin and public extension interfaces.
- Exact WordPress/WooCommerce versions and extension compatibility require a future approved matrix.
- WooCommerce order, payment, cart, checkout, coupon, tax, and shipping transaction domains remain inactive.
- Product data must remain portable enough for future CRM, ERP, and CentralSteel mappings.

## Founder Decisions

- Approve, revise, or reject WCM-001 through WCM-008.
- Confirm whether any Simple product exception is permitted.
- Approve SKU and parent-reference ownership and format.
- Approve visibility, stock-state, supply-after-order, and inquiry-action policies.
- Approve future import/export contract ownership and authorization roles.
- Approve local-attribute exception ownership, review/expiry, and migration authority.

## Open Questions

- Which Product Types and attributes create variations?
- Which variation combinations and required fields are valid?
- How will WooCommerce availability map to the proposed stock states?
- Which public visibility states apply to unavailable and discontinued products?
- Which future system owns SKU, stock, and confidential pricing data?
- Which Admin roles may create products, attributes, terms, variations, and imports?
- Who owns and approves local-attribute exceptions, how often are they reviewed, and which reuse condition forces migration to a global attribute?

## Approval Status

Review. This model is not approved and does not authorize WooCommerce installation, product creation, settings, pricing fields, inquiry UI, imports, or implementation.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.2.0 | 2026-07-03 | Batch 05B remediation: governed local-attribute exceptions and product-lifecycle/stock visibility separation; documentation only. |
| 0.1.0 | 2026-07-03 | Initial Batch 05 WooCommerce product mapping policy; documentation only. |

## References

- [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md)
- [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md)
- [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md)
- [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)
- [ADR 0001](adr/0001-inquiry-first-commerce.md)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Product Data Reading Path](READING_ORDER.md#product-data-and-woocommerce-reading-path)
