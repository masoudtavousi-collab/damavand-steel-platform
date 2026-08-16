# ADR 0001: Inquiry-first commerce

## Document Control

- **Document Status:** Approved
- **Decision Status:** Accepted
- **Owner:** Product and Architecture
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Last Updated:** 2026-08-16
- **Last Review:** 2026-08-16

- Date: 2026-07-03

## Context

Damavand Steel sells through consultation and quotation rather than public transactional pricing.

## Decision

WooCommerce is the product catalog authority, while public prices, cart, checkout, payments, and price-bearing structured data remain disabled. Product journeys culminate in a contextual inquiry.

## Applicability after C1-T06 and C000

Inquiry-first and no-public-pricing remain current operational behavior. C1-T06 supersedes the sentence above only where it assigns canonical Product authority to WooCommerce: the Repository hierarchy `Catalog → Platform → Family → Series → Variant Rules → SKU` owns Product truth, and WooCommerce is a downstream projection.

C000 approves `Inquiry First by default + future SKU-level purchase eligibility` as a target architecture only. It enables no pricing, purchase, cart, checkout, payment, Product/SKU, Availability, Runtime, or Production behavior. Any future purchase activation still requires a separately approved superseding activation decision/ADR and Product, commercial, legal, Sales, SEO, technical, Runtime, Production, and Founder gates.

## Consequences

Inquiry conversion, response time, and lead quality become primary commerce metrics. Any future public pricing requires a superseding ADR and legal, sales, SEO, and technical review.

## Alternatives considered

Public e-commerce and request-a-quote as a secondary path were rejected for the initial system.

## Related Documents

- [Core Project Principles](../00_PROJECT_BIBLE.md#core-project-principles)
- [Enterprise Architecture](../02_ARCHITECTURE.md)
- [Business Rules](../03_BUSINESS_RULES.md)
- [Technology Stack](../05_TECH_STACK.md)
- [Decision Log](../10_DECISION_LOG.md)
- [SEO Strategy](../11_SEO_STRATEGY.md)

## Navigation

- [ADR Guide](README.md)
- [Documentation Index](../08_DOCUMENTATION_INDEX.md)
