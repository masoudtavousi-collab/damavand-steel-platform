# Blocksy Pro Configuration Blueprint

## Document Control

- **Document ID:** `docs/36_BLOCKSY_CONFIGURATION.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Solution Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On theme, presentation ownership, design-system, template, responsive, RTL, accessibility, performance, or upgrade change
- **Lifecycle:** Review
- **Source of Truth:** [Core Project Principles](00_PROJECT_BIBLE.md), [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), and [WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md)
- **Dependencies:** [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [Site Structure](25_SITE_STRUCTURE.md), [Content Types](32_CONTENT_TYPES.md), and [Media Strategy](33_MEDIA_STRATEGY.md)
- **Related Documents:** [Elementor Architecture](37_ELEMENTOR_ARCHITECTURE.md), [WooCommerce Configuration](38_WOOCOMMERCE_CONFIGURATION.md), [SEO Entity Model](34_SEO_ENTITY_MODEL.md), and [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md)
- **Traceability:** CP-002 through CP-007, CP-010, WP-FC-002, WPBP-002 through WPBP-006, and BLOCKSY-001 through BLOCKSY-009
- **AI Compatibility:** AI-readable Blueprint; no AI feature or theme configuration is authorized
- **Approval:** Pending Founder/design/technical approval; no Blocksy configuration is authorized

## Purpose

Define Blocksy Pro presentation ownership and future Admin-configuration boundaries without changing theme files or settings.

## Scope and Boundary

This Blueprint covers theme hierarchy, Customizer ownership, global presentation domains, hooks, layout ownership, performance, and extensibility. It creates no colors, fonts, measurements, layouts, headers, footers, hooks, templates, CSS, or theme files.

## Blocksy Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| BLOCKSY-001 | Blocksy remains the vendor-maintained presentation shell; no custom or child theme is authorized. | Required by CP-007 and WP-FC-002 |
| BLOCKSY-002 | Use supported Blocksy/WordPress Admin configuration before any extension. | Required by CP-001 and CP-002 |
| BLOCKSY-003 | Blocksy owns the global header, footer, primary navigation, shell, default archive/single layouts, and WooCommerce presentation by default. | Derived from WordPress Architecture; pending Blueprint approval |
| BLOCKSY-004 | Elementor owns only delegated body composition and must not create a competing global shell. | Derived from WordPress Architecture; pending Blueprint approval |
| BLOCKSY-005 | One approved design-token system coordinates Blocksy and Elementor values. | Proposed pending Founder/design approval |
| BLOCKSY-006 | Every configuration must pass Persian RTL, Mobile First, accessibility, inquiry, no-price, and performance review. | Required by CP-003 through CP-006 |
| BLOCKSY-007 | Supported hook configuration is permitted only after a named use case and owner are approved; executable snippets are not authorized. | Proposed pending Founder/technical approval |
| BLOCKSY-008 | Product and archive presentation remains Blocksy-owned unless a later explicit architecture decision delegates it. | Derived from WordPress Architecture |
| BLOCKSY-009 | Preserve vendor upgradeability: no core/theme edits, copied templates, unsupported overrides, or hidden configuration dependencies. | Required by CP-007 and maintainability constraints |

## Theme Hierarchy and Child Theme Policy

```text
WordPress rendering contract
  -> Vendor-managed Blocksy theme
    -> Licensed Blocksy Pro capabilities
      -> Supported Admin/Customizer configuration
        -> Approved page-body composition
```

No child theme is part of the approved solution. The existing repository child-theme placeholder remains governed by FD-GOV-008 and is not validated, activated, edited, or used by this Blueprint.

## Customizer Strategy

- Treat Customizer settings as governed configuration with an owner, rationale, environment path, review evidence, export/restore method, and rollback plan.
- Prefer global settings over page-specific overrides.
- Maintain one recorded source for each token and layout responsibility.
- Do not store business facts, product facts, inquiry logic, SEO authority, secrets, or unsupported code in Customizer fields.
- Exact controls and values remain pending design and technical approval.

## Global Colors

Blocksy is the proposed Admin owner for approved global color tokens. Token names, values, contrast requirements, semantic roles, state colors, dark-mode policy, and Elementor synchronization remain unresolved. Per-widget and per-page colors require an approved exception and must not create a second token system.

## Typography

Blocksy is the proposed owner of the global Persian RTL typography scale and base element styles. Font families, licenses, hosting, weights, fallbacks, line heights, numeric behavior, Latin/Persian pairing, and performance budgets remain unresolved. Elementor consumes, rather than duplicates, approved tokens.

## Container Strategy

One approved container system must define content width, full-width exceptions, gutters, breakpoints, nested behavior, and mobile/RTL spacing. Exact values are not selected. Elementor sections must inherit or explicitly use approved container variants without accidental horizontal overflow.

## Header

Blocksy owns the global header and mobile navigation. Future configuration must map approved Site Structure navigation, Persian labels, inquiry action, accessibility, responsive behavior, authentication visibility, and search entry. Header rows, elements, dimensions, sticky behavior, and breakpoints remain unresolved.

## Footer

Blocksy owns the global footer. Future configuration must map approved footer groups, organization identity, policies, support/inquiry paths, accessibility, and lifecycle. Columns, labels, content, contact details, and legal statements remain unresolved.

## Sidebar

Sidebars are disabled by default as a design assumption only where no approved information need exists; each public sidebar requires a named purpose, content owner, mobile placement, RTL behavior, accessibility review, and canonical-link assessment. No actual sidebar state is changed by this document.

## Archive Layouts

Blocksy owns default WordPress and WooCommerce archive presentation. An archive may be public only if its logical content type, taxonomy, URL, canonical, navigation, and indexation role are approved. Filters, cards, pagination, empty states, inquiry actions, and responsive layout remain configuration decisions.

## Single Layouts

Blocksy owns default single-page and product presentation shells. Required content derives from the relevant content/product contract. Product layouts must not render price, cart, checkout, payment, or Offer data and must preserve the contextual inquiry action. Exact composition remains unresolved.

## Hooks Usage

| Hook use | Blueprint rule |
| --- | --- |
| Declarative placement through supported Admin controls | May be proposed with named owner, content source, conditions, accessibility, and rollback |
| Executable PHP/JavaScript/CSS snippets | Not authorized by this Blueprint |
| Duplicating Elementor/global template output | Prohibited |
| Injecting prices, transactions, unsupported schema, or protected data | Prohibited |
| Vendor/core file modification | Prohibited |

## Template Ownership

| Concern | Primary owner | Boundary |
| --- | --- | --- |
| Header, footer, navigation, shell | Blocksy | Elementor must not duplicate |
| Global tokens and base typography/layout | Blocksy-coordinated design system | Elementor consumes approved values |
| Standard page/landing body | Elementor within approved content areas | No shell or data authority |
| Product/archive presentation | Blocksy by default | Delegation requires future approval |
| Product/content data | WooCommerce/WordPress source | Theme only renders |
| Canonical/schema/breadcrumb output | Approved SEO capability | Exactly one primary owner |

## Performance Considerations

Future configuration must minimize duplicate assets, unused component features, third-party scripts, font cost, image layout shift, and overlapping optimization. Cache/CDN/media owners remain separate. Performance budgets and measurements require future approval; LiteSpeed Cache is prohibited.

## Future Extensibility

Extensions must use supported Blocksy capabilities and pass ownership, compatibility, accessibility, Persian RTL, mobile, performance, security, update, export, rollback, and retirement review. Vendor lock-in is reduced through canonical source data, documented configuration, and avoidance of copied templates.

## Founder Decisions

- Approve, revise, or reject BLOCKSY-001 through BLOCKSY-009.
- Approve the design-token owner and exact color, typography, container, header, footer, sidebar, archive, and single-layout policies.
- Resolve FD-GOV-008 without creating a custom-theme exception.
- Assign presentation configuration, design, accessibility, RTL, performance, and release reviewers.

## Open Questions

- Which Blocksy controls and Pro modules are required after version compatibility is established?
- What are the approved tokens, breakpoints, containers, shell variants, navigation labels, and responsive behaviors?
- Which archives/singles are public and which hook use cases, if any, are justified?
- How will supported configuration be exported, reviewed, restored, and compared across environments?

## Approval Status

Review. No theme, child theme, Customizer value, hook, layout, template, CSS, script, or WordPress setting is created or changed.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 08 Blocksy Pro configuration Blueprint; documentation only. |

## Related Documents

- [WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md)
- [Elementor Architecture](37_ELEMENTOR_ARCHITECTURE.md)
- [Site Structure](25_SITE_STRUCTURE.md)
- [Media Strategy](33_MEDIA_STRATEGY.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| BLOCKSY-001–BLOCKSY-009 | CP-002–CP-007, CP-010, WP-FC-002, WordPress template ownership | Elementor, WooCommerce, media, SEO, and future presentation configuration plans | Compatibility matrix, configuration inventory/export, viewport/RTL/accessibility/no-price/performance regression results, rollback evidence |

Implementation status: `Not authorized`.
