# ADR 0001: Inquiry-first commerce

## Document Control

- **Document Status:** Approved
- **Decision Status:** Accepted
- **Owner:** Product and Architecture
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03

- Date: 2026-07-03

## Context

Damavand Steel sells through consultation and quotation rather than public transactional pricing.

## Decision

WooCommerce is the product catalog authority, while public prices, cart, checkout, payments, and price-bearing structured data remain disabled. Product journeys culminate in a contextual inquiry.

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
