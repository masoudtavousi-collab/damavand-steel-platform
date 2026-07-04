# Pipe Data Governance Checklist

## Document Control

- **Document ID:** `repository/data/validation/PIPE_DATA_GOVERNANCE_CHECKLIST.md`
- **Status:** Review
- **Authority:** Product Data Quality Gate
- **Owner:** Founder
- **Reviewer:** Product Data Owner, Qualified Steel-Domain Reviewer, SEO Reviewer, CRM Reviewer, Quality Reviewer, and WooCommerce Technical Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** Before classification approval, import readiness review, or any Pipe data/model change
- **Lifecycle:** Review
- **Source of Truth:** Current Sprint 03A through Sprint 03C Pipe data, mapping, classification, category, attribute, and validation assets
- **Dependencies:** [Pipe Taxonomy and Attribute Classification](../taxonomies/PIPE_TAXONOMY_ATTRIBUTE_CLASSIFICATION.md), [Pipe Category Model](../taxonomies/PIPE_CATEGORY_MODEL.md), [Pipe Attribute Model](../attributes/PIPE_ATTRIBUTE_MODEL.md), and [Pipe Import Precheck](PIPE_IMPORT_PRECHECK.md)
- **Related Documents:** [Pipe Product Family](../products/pipes/PIPE_PRODUCT_FAMILY.md), [Pipe Variation Matrix](../products/pipes/PIPE_VARIATION_MATRIX.md), [Pipe Import Mapping](../imports/woocommerce/PIPE_IMPORT_MAPPING.md), and [Product Data Validation Rules](PRODUCT_DATA_VALIDATION_RULES.md)
- **Traceability:** CP-001 through CP-010, PDM-001 through PDM-008, TAX-001 through TAX-008, ATT-001 through ATT-007, WCM-001 through WCM-008, INQ-001 through INQ-008, SEOENT-001 through SEOENT-009, FIELD-001 through FIELD-009, Sprint 03A, Sprint 03B, and Sprint 03C
- **AI Compatibility:** AI-readable review gate; checkboxes require accountable human evidence and are not autonomously approved
- **Approval:** Pending Founder and specialist review; current implementation/import status is `NO-GO`

## Purpose

Provide the mandatory human-review and rejection gates for Pipe classification, categories, attributes, imports, Inquiry First, No Public Pricing, SEO, CRM, and future WooCommerce readiness.

## Checklist Rules

- `[x]` records repository-observable evidence only.
- `[ ]` means evidence or approval is pending; it must not be treated as a pass.
- Each checked approval item requires reviewer, date, evidence reference, and affected version in the eventual review record.
- Any unchecked hard gate or rejection condition keeps implementation/import at `NO-GO`.
- This checklist does not authorize access, configuration, product creation, dry run, or import.

## Founder Approval Checklist

- [ ] Approve the Pipe Product Family/category identity, Persian/English names, and scope.
- [ ] Approve or revise every classification marked Founder review required.
- [ ] Approve Material/Grade/Finish terminology.
- [ ] Approve the five variation axes and selection order.
- [ ] Approve the valid commercial-combination dataset.
- [ ] Approve the category parent/root placement and public slug policy.
- [ ] Approve Custom Field, CRM, SEO, filter, and product-table boundaries.
- [ ] Assign Product Data, domain, Sales/Operations, SEO, CRM/privacy, and WooCommerce reviewers.
- [ ] Issue separate authorization before any implementation or import activity.

## Attribute Approval Checklist

- [x] All 14 product-specification attributes are assigned one global attribute identity.
- [x] No local attribute is proposed for a reusable specification.
- [x] Grade, Finish, Diameter, Thickness, and Length are the only variation-driving attributes.
- [x] Controlled candidate values match the Sprint 03A matrix.
- [ ] Founder/domain reviewer approves every attribute name, Persian label, slug, definition, and scope.
- [ ] Founder/domain reviewer approves every allowed value and alias.
- [ ] Dimension units, precision, tolerance, and display rules are approved.
- [ ] Surface-versus-Finish and Material-versus-Grade definitions are approved.
- [ ] Optional Brand, Country, Quality Level, Application, Environment, and Installation Use registries are approved.
- [ ] Runtime global attribute and term identities/mappings are approved.

## Category Approval Checklist

- [x] Product Family is separated from product specifications.
- [x] Grade, Finish, dimensions, and other Pipe specifications are prohibited as Pipe subcategories.
- [x] No unsupported child category is invented.
- [ ] Founder approves `لوله استیل / Stainless Steel Pipe` as the category label/scope.
- [ ] Founder approves the higher parent/Product Group or explicit root-level placement.
- [ ] Founder/SEO approves the public slug language policy and final slug.
- [ ] Founder/SEO approves category-versus-parent-product search intent and canonical ownership.
- [ ] Category content, owner, indexation, internal links, lifecycle, and review cycle are approved.
- [ ] Duplicate, alias, former-term, redirect, reserved-path, and external-mapping checks pass.

## Import Readiness Checklist

- [x] The staging template has 23 columns and four shape-only placeholder rows.
- [x] All 23 columns have a documented mapping class/rule.
- [x] All 29 unique Pipe fields have exactly one primary classification.
- [ ] Final stable family, parent, and variation identities exist.
- [ ] Final SKU policy and values exist and pass collision checks.
- [ ] Approved valid combinations replace placeholder-only samples.
- [ ] Required commercial values, including approved stock-state mapping, are resolved without invention.
- [ ] Category, global attribute, term, and canonical-slug mappings are approved.
- [ ] Exact target importer/version capability and field mapping are verified.
- [ ] Isolated staging, backup/restore, dry-run, reconciliation, rollback, operator, and permissions evidence exists.
- [ ] [Pipe Import Precheck](PIPE_IMPORT_PRECHECK.md) contains no pending, blocked, failed, or required not-run hard gate.
- [ ] Founder grants separate import authorization.

## No Public Pricing Checklist

- [x] `public_price` is classified `Excluded`.
- [x] Current CSV public-price cells are empty.
- [x] Mapping defines no target for public price.
- [x] Zero, free, `TBD`, hidden text, currency, sentinel, and formula values are prohibited.
- [ ] Future runtime validation confirms no price in page output, source, API, schema, feed, cache, search, email, analytics, cart, checkout, payment, or inquiry context.
- [ ] Future rollback trigger is proven for any detected price exposure.

## Inquiry First Checklist

- [x] `inquiry_only` is classified as a required logical behavior field.
- [x] Current parent and variation rows use `inquiry_only=yes`.
- [x] Product and selected variation context is defined for future inquiry handoff.
- [x] Cart, checkout, payment, public order, and public quotation output remain prohibited.
- [ ] Founder approves the physical inquiry capability and configuration.
- [ ] Sales/privacy/security approve required fields, consent, access, notification, retention, and CRM handoff.
- [ ] Future runtime validation proves inquiry continuity on mobile Persian RTL flows.

## SEO Readiness Checklist

- [x] Category, canonical metadata, and attribute SEO responsibilities are separated.
- [x] Variable Parent Product/category canonical conflict requires explicit review.
- [x] Variation states and filter combinations are non-canonical/non-indexable by default.
- [x] Offer/price schema and unsupported availability claims are prohibited.
- [ ] Public category/product slugs and canonical owner are approved.
- [ ] Search intent, Persian content, title, description, FAQ answers, internal links, and schema eligibility are approved.
- [ ] Cannibalization, duplicate URL, reserved path, redirect, sitemap, and indexation checks pass.
- [ ] Future rendered metadata/schema matches visible approved facts.

## CRM Readiness Checklist

- [x] `inquiry_priority` is the only primary Internal CRM Field in the Pipe classification.
- [x] Product facts remain product-master data; CRM receives references/snapshots only.
- [x] Stock status, notes, and CRM controls are not public.
- [ ] CRM owner, statuses, field mapping, access, retention, consent, audit, and error handling are approved.
- [ ] Stable product/variation IDs and approved SKU snapshots exist.
- [ ] CRM integration capability, authentication, retry, reconciliation, and rollback remain separately approved before use.

## WooCommerce Readiness Checklist

- [x] Variable Parent Product and variation roles are explicit.
- [x] Five controlled global variation attributes are explicit.
- [x] Category-versus-attribute decisions are explicit.
- [x] No global attribute, local attribute, term, category, field, filter, or product has been created.
- [ ] Target WordPress/WooCommerce versions and importer capabilities are verified for the future execution window.
- [ ] Runtime category/global attribute/term identities are approved.
- [ ] Inquiry-only/no-price behavior and permissions are proven in isolated staging.
- [ ] Admin manageability, mobile Persian RTL selection, performance, accessibility, SEO, security, backup, and rollback pass.
- [ ] Founder issues separate implementation authorization.

## Rejection Conditions

Reject or stop when any of the following occurs:

- A field has no primary classification or more than one primary classification.
- A reusable specification is implemented as a local duplicate, category duplicate, tag, or free text.
- Grade, Finish, Diameter, Thickness, or Length contains an uncontrolled value or an unapproved combination.
- The 1,584 theoretical candidate tuples are treated as approved/available products.
- A required value is blank, `TBD`, inferred, defaulted, or silently corrected for execution.
- A price, stock promise, supplier, origin, certification, warranty, safety, suitability, or availability claim lacks approved evidence.
- A `TBD-*` placeholder is treated as a final SKU or stable ID.
- A category, attribute, term, slug, custom field, or CRM field is auto-created without approval.
- A filter state or attribute archive becomes an uncontrolled canonical/indexable URL.
- Inquiry First or No Public Pricing is bypassed anywhere.
- WordPress, hosting, plugins, database, products, pages, or imports are changed without a separate authorized implementation task.
- Backup, recovery, rollback, reconciliation, permissions, accountable reviewer, or Founder approval is absent.

## Current Gate Result

**GO** for Founder and specialist classification review.

**NO-GO** for WordPress/WooCommerce implementation, dry run, import, product creation, publication, pricing, stock assignment, final SKU assignment, or CRM integration.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03C Pipe data governance checklist; no implementation or import. |

## Navigation

- [Pipe Taxonomy and Attribute Classification](../taxonomies/PIPE_TAXONOMY_ATTRIBUTE_CLASSIFICATION.md)
- [Pipe Category Model](../taxonomies/PIPE_CATEGORY_MODEL.md)
- [Pipe Attribute Model](../attributes/PIPE_ATTRIBUTE_MODEL.md)
- [Pipe Import Precheck](PIPE_IMPORT_PRECHECK.md)
- [Sprint 03C Audit](../../../docs/AUDIT_REPORT_SPRINT03C.md)
