# Plugin Installation Sequence

## Document Control

- **Document ID:** `repository/config/PLUGIN_INSTALLATION_SEQUENCE.md`
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Build Engineer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** Before component installation and on package, dependency, compatibility, license, sequence, or rollback change
- **Lifecycle:** Review
- **Source of Truth:** [Plugin Responsibility Matrix](../../docs/44_PLUGIN_RESPONSIBILITY_MATRIX.md), approved governing documents, and future approved exact package evidence
- **Dependencies:** [WordPress Installation Checklist](WORDPRESS_INSTALLATION_CHECKLIST.md), [Hosting Validation Checklist](HOSTING_VALIDATION_CHECKLIST.md), and [Rollback Plan](ROLLBACK_PLAN.md)
- **Related Documents:** [Plugin Inventory](PLUGIN_INVENTORY.md), [Post-Install Validation](POST_INSTALL_VALIDATION.md), [WordPress Blueprint](../../docs/35_WORDPRESS_BLUEPRINT.md), and [Sprint 01C Audit](../../docs/AUDIT_REPORT_SPRINT01C.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, WPBP-001 through WPBP-010, BLOCKSY-001 through BLOCKSY-009, ELEMENTOR-001 through ELEMENTOR-009, WCCFG-001 through WCCFG-012, PLUG-001 through PLUG-010, S01B-003 through S01B-005, and S01C-001 through S01C-008
- **AI Compatibility:** AI-readable gated sequence; names do not prove package availability, dependency approval, installation, activation, or licensing
- **Approval:** Pending Founder/technical/security/operations approval; sequence is not authorized for execution

## Purpose

Define a conditional installation and activation sequence using only components already named by approved repository governance.

## Evidence Boundary

- WordPress Core is the platform prerequisite, not a plugin.
- Blocksy is a vendor theme; Blocksy Pro is a commercial companion package whose exact form and dependency chain require evidence.
- WooCommerce is an approved commerce component.
- Elementor Pro is an approved commercial component; any required base package or dependency must be separately and explicitly approved before installation.
- This document does not approve versions, package sources, licenses, dependencies, configuration, content, or execution.
- Gravity Forms, LiteSpeed Cache, custom/child theme implementation, and Phase 1 AI features are excluded.

## Universal Entry Gate

- [ ] Clean WordPress checkpoint `R1` is accepted and restorable.
- [ ] Exact component version, official package source, checksum/signature method, license, compatibility, dependency graph, owner, and support lifecycle are approved.
- [ ] A new rollback checkpoint can be created and restored before the component changes state.
- [ ] Installation and activation are separately authorized for the named environment and maintenance window.
- [ ] Evidence capture excludes secrets, license keys, personal data, and commercial archives.

## Dependency and Activation Order

| Stage | Component | Type | Installation prerequisite | Activation prerequisite | Validation before next stage | Rollback point | Current state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | WordPress Core | Platform | Hosting gate, exact package approval, and `R0` | Clean-install checks | Exact version/checksums, HTTPS, Admin, permalinks capability, uploads, security, and restore | `R1` clean WordPress | Blocked |
| 1 | Blocksy | Vendor theme | Accepted `R1`; exact theme package/version/source/compatibility approved | Install integrity and no custom/child theme files | Theme availability, activation, frontend/Admin health, no customization, and restore | `R2` WordPress + Blocksy | Blocked |
| 2 | WooCommerce | Plugin | Accepted `R2`; exact package/version/source/compatibility approved | Install integrity; setup scope constrained to unavoidable installation defaults | Activation health, generated state inventory, no products/demo data/business settings/public pricing, and restore | `R3` WordPress + Blocksy + WooCommerce | Blocked |
| 3 | Blocksy Pro | Commercial companion package | Accepted `R3`; exact packaging, Blocksy dependency, source, version, license, and compatibility approved | All required dependencies active and license handling approved | Activation/license status, dependency health, no customization/templates, and restore | `R4` accepted Blocksy Pro state | Hold — package/dependency evidence missing |
| 4 | Elementor Pro | Commercial plugin | Accepted `R4`; exact package/source/version/license/compatibility and every required dependency explicitly approved | Every approved required dependency active; no inferred package permitted | Activation/license status, dependency health, no pages/templates/content, and restore | `R5` accepted Elementor Pro state | Hold — dependency evidence missing |

## Validation After Each Step

- [ ] Record exact installed and active versions against approved package evidence.
- [ ] Verify checksums/integrity where the vendor supports it.
- [ ] Verify WordPress Admin, frontend, HTTPS, permalinks, uploads, scheduled events, logs, and health remain functional.
- [ ] Compare filesystem/database/configuration state to the prior checkpoint and explain every observed change.
- [ ] Confirm no page, product, taxonomy, demo data, Elementor template, Blocksy customization, WooCommerce business configuration, or project content was introduced.
- [ ] Confirm no public price, purchasable cart/checkout flow, custom theme, Gravity Forms, LiteSpeed Cache, or Phase 1 AI feature exists.
- [ ] Create the stage checkpoint and complete isolated restore validation before proceeding.

## Stop Conditions

Stop and roll back the current stage when any of the following occurs:

- An exact version, package source, license, compatibility record, dependency, or approval is missing or mismatched.
- A dependency is merely assumed, bundled unexpectedly, or not listed in approved governance.
- Installation or activation creates unexpected content, settings, users, roles, files, database objects, scheduled jobs, network calls, or public behavior.
- Public pricing, ordering, cart/checkout, demo data, or an unapproved business flow becomes available.
- Integrity, security, permissions, logs, HTTPS, Admin, frontend, uploads, performance smoke checks, backup, or restoration fails.
- The prior accepted checkpoint cannot be reproduced.

## Rollback Rule

Restore the most recent accepted checkpoint, verify it independently, retain failure evidence without secrets, update the inventory/audit, and require a new approval before retrying. Deactivation or deletion alone is not treated as proven rollback.

## Current Outcome

`NO-GO — CLEAN WORDPRESS, EXACT PACKAGES, DEPENDENCIES, LICENSES, COMPATIBILITY, CHECKPOINTS, AND APPROVALS ARE NOT AVAILABLE`

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 01C gated sequence; no component installed or activated. |

## Navigation

- [Plugin Responsibility Matrix](../../docs/44_PLUGIN_RESPONSIBILITY_MATRIX.md)
- [Plugin Inventory](PLUGIN_INVENTORY.md)
- [Post-Install Validation](POST_INSTALL_VALIDATION.md)
- [Rollback Plan](ROLLBACK_PLAN.md)
- [Sprint 01C Audit](../../docs/AUDIT_REPORT_SPRINT01C.md)
