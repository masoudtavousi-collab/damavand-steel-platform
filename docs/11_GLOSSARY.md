# Glossary

## Document Control

- **Status:** Draft
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Lifecycle:** Draft

## Purpose

Maintain controlled terminology used by repository documentation without creating business rules or product taxonomy.

## Enterprise Terminology

| Term | Definition |
| --- | --- |
| Architecture Decision Record (ADR) | A version-controlled record of one significant decision, its context, consequences, and alternatives. |
| Approved Exception | A documented deviation with an approver, rationale, risk, and review or expiry date. |
| Document Owner | The role accountable for document accuracy, review, and lifecycle management. |
| Review Evidence | Objective information supporting a review conclusion. |
| Source of Truth | The declared authoritative document for a defined concern. |

## WordPress Terminology

| Term | Definition |
| --- | --- |
| WordPress Core | The upstream WordPress application, excluding project-owned and third-party themes and plugins. |
| Plugin | A WordPress extension packaged separately from WordPress Core and themes. |
| Must-Use Plugin | A plugin loaded automatically from the WordPress must-use plugin directory. |
| Theme | A WordPress presentation package controlling templates and presentation behavior. |
| Child Theme | A theme that inherits from a parent theme while isolating supported project-owned changes. |
| WP-CLI | The command-line interface used to administer WordPress through supported commands. |

## WooCommerce Terminology

| Term | Definition |
| --- | --- |
| WooCommerce | The WordPress commerce platform identified by the repository requirements. |
| Product | The WooCommerce catalog entity; project-specific product structure remains undefined. |
| High-Performance Order Storage (HPOS) | WooCommerce's dedicated order-data storage capability. Project configuration remains undecided. |
| Action Scheduler | The background job system used by WooCommerce and compatible extensions. |
| Store API | WooCommerce's public-facing API surface for store interactions. Project exposure rules remain governed by approved business decisions. |

## Steel Industry Terminology

TODO (Founder and Steel Subject-Matter Expert Input Required)

No steel term, classification, grade, standard, dimension, or taxonomy is approved by this glossary.

## Project Terminology

| Term | Definition |
| --- | --- |
| Damavand Steel Enterprise Repository | The existing version-controlled repository governed by the project documentation. |
| Founder Decision | A project decision explicitly awaiting or receiving Founder approval. |
| Inquiry-First | The accepted commercial direction recorded in [ADR 0001](adr/0001-inquiry-first-commerce.md). |
| No Public Pricing | The accepted constraint recorded in [ADR 0001](adr/0001-inquiry-first-commerce.md); implementation details remain undefined. |
| Supporting Document | A document that elaborates a governing document without overriding it. |

## Terminology Rules

## PD-03A Controlled Prerequisite Terms

- **لوله استیل دکوراتیو:** Persian-only official Series label in the exact
  PD-03A prerequisite scope; it is not a Product, SKU, Slug, availability, or
  commerce record.
- **Finish / رنگ و پوشش:** internal key/label used only for the bounded pilot
  prerequisite. It does not establish a general Finish/Color/Surface taxonomy.
- **Silver / نقره‌ای:** appearance designation with code `silver`; it asserts
  no PVD, coating type, material, quality, standard, tolerance, application, or
  availability.
- **Synthetic Pilot Combination:** test fixture exercising the three approved
  reference tuples. It is never a canonical Pilot record and cannot be promoted.
- **Immutable Product Data Extension:** separately governed additive records
  that cannot mutate or shadow the approved base registries or historical hashes.

## PD-02B Controlled Terms

- **فولاد زنگ‌نزن / Stainless Steel:** canonical Material term with code
  `stainless_steel`; `استیل` is a common Persian alias only.
- **گرید فولاد / Steel Grade:** the Attribute that holds the exact identifiers
  `201`, `304`, and `316` in PD-02B, without technical/application claims.
- **لوله استیل / Stainless Steel Pipe:** the exact PD-02B Family label; it does
  not imply a Product, SKU, availability, finish, dimension, or runtime entry.
- **INTERNAL Attribute Profile:** repository-only requirement policy; it grants
  no SEO, filtering, variation, inquiry, or commerce authority.

- Use the glossary term exactly when it has an approved definition.
- Do not define project product taxonomy in this glossary without an approved source.
- Add or change controlled terms through the [Review Process](15_REVIEW_PROCESS.md).

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Business Rules](03_BUSINESS_RULES.md)
- [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md)
