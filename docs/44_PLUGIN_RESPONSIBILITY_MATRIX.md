# Enterprise Plugin Responsibility Matrix

## Document Control

- **Document ID:** `docs/44_PLUGIN_RESPONSIBILITY_MATRIX.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Solution Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On capability, plugin, theme package, version, ownership, overlap, replacement, upgrade, risk, or retirement change
- **Lifecycle:** Review
- **Source of Truth:** [Technology Stack](05_TECH_STACK.md), [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), and [WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md)
- **Dependencies:** [Blocksy Configuration](36_BLOCKSY_CONFIGURATION.md), [Elementor Architecture](37_ELEMENTOR_ARCHITECTURE.md), [WooCommerce Configuration](38_WOOCOMMERCE_CONFIGURATION.md), [Inquiry Workflow](42_INQUIRY_WORKFLOW.md), and [User Roles](43_USER_ROLES.md)
- **Related Documents:** [Security](10_SECURITY.md), [SEO Strategy](11_SEO_STRATEGY.md), [Media Strategy](33_MEDIA_STRATEGY.md), [Search and Discovery](27_SEARCH_AND_DISCOVERY.md), and [Deployment](09_DEPLOYMENT.md)
- **Traceability:** CP-001 through CP-010, WP-FC-001 through WP-FC-005, WPBP-002 through WPBP-010, and PLUG-001 through PLUG-010
- **AI Compatibility:** AI-readable Blueprint; no AI feature, plugin selection, installation, or configuration is authorized
- **Approval:** Pending Founder/technical/security/operational approval; no plugin action is authorized

## Purpose

Assign one accountable owner and explicit boundary to every approved component and unresolved plugin capability before vendor selection or installation.

## Scope and Boundary

This is a responsibility and selection-gate matrix, not an installed-plugin inventory. Only WooCommerce and Elementor Pro are approved named plugins; Blocksy Pro is an approved presentation package spanning the vendor theme and licensed capabilities. Other rows are capability slots with no selected brand. WordPress Core is included for overlap clarity and is not a plugin.

## Plugin Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| PLUG-001 | Select plugins by a single required capability and lifecycle fit, not convenience or popularity. | Required by CP-001 |
| PLUG-002 | Prefer supported Admin configuration and minimize custom code and overlapping owners. | Required by CP-002 |
| PLUG-003 | Maintain one primary owner for schema, breadcrumbs, cache, optimization, inquiry, redirects, mail, and each integration. | Proposed pending Founder/technical approval |
| PLUG-004 | Require WordPress/WooCommerce/Blocksy/Elementor/version, Persian RTL, mobile, accessibility, security, performance, and Admin-manageability evidence. | Derived from platform architecture |
| PLUG-005 | Require data ownership, export, uninstall, migration, replacement, upgrade, rollback, support, licensing, and retirement evidence. | Proposed pending Founder/technical approval |
| PLUG-006 | Prevent plugins from exposing public prices, transactions, protected data, unsupported schema, or invented business rules. | Required by CP-005, CP-006, and ADR-0001 |
| PLUG-007 | Prohibit Gravity Forms and LiteSpeed Cache; do not select equivalent capability brands in this document. | Required by CP-008 and CP-009 |
| PLUG-008 | Prohibit AI features, connectors, generation, search, routing, or external model access in Phase 1. | Required by CP-010 |
| PLUG-009 | Treat Blocksy/Elementor/WooCommerce updates as coordinated platform changes with compatibility and rollback review. | Proposed pending Founder/technical approval |
| PLUG-010 | Do not install a capability when Core, the approved stack, hosting, or an existing non-overlapping owner safely satisfies it. | Required by Plugin First governance |

## Approved Named Components

| Component | Type/status | Reason | Authority owner | Configuration owner | Replacement policy | Upgrade policy | Principal risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WordPress Core | Platform, not plugin; approved | CMS, identity, media, content lifecycle, extension interfaces | Founder/architecture | Technical Administrator | Platform replacement requires architecture decision and migration | Coordinated staging/security/compatibility/rollback review | Core/vendor modification, unsupported versions, privilege sprawl |
| WooCommerce | Approved plugin; not configured | Canonical product/variation/attribute catalog | Founder/product architecture | Product Data Manager plus Technical Administrator | Replacement requires catalog/ID/export/inquiry migration plan | Validate no-price/no-transaction, product data, Blocksy/Elementor, APIs, rollback | Transaction defaults or extensions re-expose price/cart/checkout |
| Elementor Pro | Approved plugin; no templates/configuration | Bounded page/landing body composition | Founder/presentation architecture | Content/Presentation Administrator | Preserve canonical content/data and template export/mapping | Validate Blocksy ownership, widgets, responsive/RTL/accessibility/performance, rollback | Lock-in, duplicate templates/tokens, performance, unsupported widgets |
| Blocksy Pro | Approved vendor theme/package; not configured | Global presentation shell and supported WooCommerce integration | Founder/presentation architecture | Presentation Administrator | No custom/child-theme fork; migration requires shell/template/config inventory | Validate Core/Woo/Elementor, RTL/mobile/accessibility/performance, restore | Ownership overlap, vendor settings drift, child-theme assumption |

## Capability Matrix

No vendor below is selected.

| Capability slot | Reason | Authority owner | Configuration owner | Replacement/upgrade policy | Principal risk and boundary |
| --- | --- | --- | --- | --- | --- |
| Inquiry/form/workflow | Secure canonical Inquiry capture and lifecycle | Founder/Sales/privacy | Inquiry Manager + Technical Administrator | Export canonical records/config; validate transitions, mail, security, rollback | Must not be Gravity Forms; protected data, spam, routing, notification failure |
| SEO/schema/breadcrumb/sitemap | One coordinated public search projection owner | Founder/SEO | SEO Manager + Technical Administrator | Preserve metadata/canonical/redirect/schema inventory; prevent duplicate output | Price-bearing Offer, competing schema/breadcrumb/canonical owners |
| Redirects | Govern URL migration and 404 recovery | Founder/SEO/URL owner | SEO Manager | Export mappings; loop/chain/conflict checks before/after update | Broken canonicals, loops, silent automatic redirects |
| Security | Hardening, monitoring, integrity, abuse and event evidence | Founder/security | Security/Technical Administrator | Preserve logs/config; staged rule and recovery tests | Lockout, data access, false confidence; does not replace secure hosting |
| Backup/restore | Application/database backup coordination and restore evidence | Founder/operations | Technical Administrator | External custody and tested restore required before replacement/update | Untested backup, same-system custody, incomplete media/database restore |
| SMTP/email delivery | Authenticated delivery, retries and failure evidence | Founder/operations | Technical Administrator | Sender/DNS/config inventory and cutover/rollback plan | Sensitive notification leakage, spoofing, silent delivery failure |
| Cache/page delivery | Page caching, invalidation, exclusions and observability | Founder/technical | Technical Administrator | Purge/disable rollback; validate authenticated/inquiry/no-price surfaces | Must not be LiteSpeed Cache; stale/private/price-bearing output |
| Performance/asset optimization | Measured asset optimization without owner overlap | Founder/technical | Technical Administrator | Baseline/compare/rollback every optimization | Duplicate cache/media/CDN responsibility, broken RTL/Elementor behavior |
| Media optimization | Derivatives, compression and metadata workflow | Founder/media | Media Manager + Technical Administrator | Preserve originals/rights/metadata and reversible derivatives | Data loss, accessibility metadata loss, format incompatibility |
| Search | Persian-aware catalog/content discovery | Founder/IA/search | Search owner + Technical Administrator | Rebuild/fallback/export; evaluate known queries and privacy | Wrong ranking, stale/private indexing, no-price leakage |
| Filtering | Canonical taxonomy/attribute filters | Founder/domain/IA | Taxonomy/Product owner + Technical Administrator | Preserve canonical IDs; validate mobile/RTL/query/canonical behavior | Taxonomy drift, invalid combinations, index bloat |
| Consent/privacy | Consent states and approved script gating | Founder/privacy/legal | Privacy owner + Technical Administrator | Preserve consent evidence/version; safe default on failure | Unapproved legal assumptions, tracking before consent |
| Analytics | Consent-aware measurement | Founder/analytics/privacy | Analytics owner + Technical Administrator | Tag/event inventory, data retention/export, disable/rollback | Personal-data leakage, duplicate tags, commercial claims without evidence |
| Import/export | Validated bulk exchange and rollback | Founder/data | Product/Content owner + Technical Administrator | Dry run, stable IDs, validation/error/rollback evidence | Destructive overwrite, duplicates, invalid terms/variations |
| Roles/capabilities | Least-privilege operational roles | Founder/security | Administrator under approved change | Export matrix, test allowed/denied paths, emergency rollback | Privilege escalation; cannot grant Founder authority |
| Content type/field/relationship | Configure only approved physical entity mappings | Founder/content/data | Technical Administrator | Export schema/data; migration/uninstall and rollback plan | No ACF assumption; lock-in, orphan metadata, inconsistent relationships |
| CRM connector | Future governed Inquiry/Customer handoff | Founder/Sales/privacy | Integration owner | Stable IDs, retry/reconcile, disable/fallback, migration | Future only; data leakage, duplicate authority, silent sync failure |
| ERP/CentralSteel connector | Future product/inventory/document mappings | Founder/domain/integration | Integration owner | Source-by-field contract, reconciliation, rollback | Future only; authority conflict, destructive sync |
| Cookie/script manager | Controlled third-party script inventory | Founder/privacy/technical | Privacy/Technical Administrator | Export inventory and fail-closed replacement | Duplicate consent owner or uncontrolled scripts |
| Multilingual/localization | Future language workflow beyond Persian | Founder/content/IA | Localization owner | Stable entity/URL mapping, export, fallback, rollback | Future only; duplicate URLs/entities and broken canonicals |

## Selection Gate

For each capability, document necessity, current owner, overlap analysis, supported versions, update history, security record, support/SLA, licensing, data location, privacy, export/uninstall behavior, Persian RTL/mobile/accessibility, Admin workflow, performance, failure behavior, configuration custody, staging plan, backup, rollback, replacement, and retirement. Founder approval is required before installation.

## Ownership Rules

- Authority owners approve purpose and policy; configuration owners operate approved settings; reviewers verify evidence.
- A component cannot approve the rule it implements.
- Shared capabilities require one primary owner and explicitly disabled/limited duplicate outputs.
- Service identities use minimum scope and are governed like privileged users.

## Replacement Policy

Replacement requires capability parity and intentional gaps, data/config export, stable identity mapping, dependency/consumer inventory, migration rehearsal, coexistence prohibition or controlled bridge, user training, rollback, retention, uninstall cleanup, and post-cutover evidence. Vendor lock-in is a risk to manage, not a reason to create custom code automatically.

## Upgrade Policy

Upgrades require approved target version, release/security review, dependency matrix, staging backup/restore, data migration check, Blocksy/Elementor/WooCommerce compatibility, Persian RTL/mobile/accessibility, Inquiry/no-price/security/performance/Admin regression, rollback point, maintenance owner, and post-release monitoring. Exact version and automatic-update policies remain unresolved.

## Founder Decisions

- Approve, revise, or reject PLUG-001 through PLUG-010.
- Approve the need and owner for each capability slot before any vendor evaluation.
- Select exact vendors, versions, licenses, update policy, maintenance windows, replacement evidence, and risk acceptance later.
- Preserve Gravity Forms, LiteSpeed Cache, custom theme, public pricing, and Phase 1 AI prohibitions.

## Open Questions

- Which capability slots are required in the initial implementation and which are already satisfied by platform/hosting?
- Which exact packages and supported versions pass the selection gate without ownership overlap?
- Who owns licensing, credentials, configuration custody, updates, incident response, and vendor exit?
- What staging, backup/restore, regression, rollback, and maintenance policies are approved?

## Approval Status

Review. No plugin, theme package, license, provider, version, installation, activation, update, configuration, credential, or integration is selected or changed.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 08 plugin responsibility matrix; documentation only. |

## Related Documents

- [WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md)
- [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md)
- [Inquiry Workflow](42_INQUIRY_WORKFLOW.md)
- [User Roles](43_USER_ROLES.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| PLUG-001–PLUG-010 | CP-001–CP-010, WP-FC-001–WP-FC-005, WordPress Plugin Architecture, 35–43 | Future vendor evaluations, implementation plan, release/security/operations records | Capability inventory, owner/overlap matrix, vendor/version compatibility, Admin/RTL/mobile/accessibility/security/performance tests, export/uninstall/upgrade/rollback evidence |

Implementation status: `Not authorized`.
