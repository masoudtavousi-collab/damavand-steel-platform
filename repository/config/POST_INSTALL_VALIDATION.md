# Post-Install Validation

## Document Control

- **Document ID:** `repository/config/POST_INSTALL_VALIDATION.md`
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Build Engineer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** After clean WordPress installation, after each approved component activation, and on runtime or validation-policy change
- **Lifecycle:** Review
- **Source of Truth:** Future runtime evidence from an approved target, [WordPress Installation Checklist](WORDPRESS_INSTALLATION_CHECKLIST.md), and approved component records
- **Dependencies:** [Hosting Validation Checklist](HOSTING_VALIDATION_CHECKLIST.md), [Plugin Installation Sequence](PLUGIN_INSTALLATION_SEQUENCE.md), and [Rollback Plan](ROLLBACK_PLAN.md)
- **Related Documents:** [Environment Report](ENVIRONMENT_REPORT.md), [Plugin Inventory](PLUGIN_INVENTORY.md), [WordPress Baseline](WORDPRESS_BASELINE.md), and [Sprint 01C Audit](../../docs/AUDIT_REPORT_SPRINT01C.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, WP-FC-001 through WP-FC-005, WPBP-001 through WPBP-010, S01B-001 through S01B-005, and S01C-001 through S01C-008
- **AI Compatibility:** AI-readable validation record; unchecked checks and absent evidence must remain unresolved
- **Approval:** Pending Founder/technical/security/operations approval; not applicable until authorized installation evidence exists

## Purpose

Define evidence required after a future clean WordPress installation and after each approved component stage. This document records no current runtime result.

## Validation Rules

- [ ] Identify the exact environment, checkpoint, component stage, evidence time, collector, and reviewers.
- [ ] Use observed runtime values and reproducible tests; never substitute repository templates or expected values.
- [ ] Record failures and unavailable evidence explicitly.
- [ ] Stop the sequence on any mandatory failure and invoke the Rollback Plan.
- [ ] Exclude credentials, keys, personal data, protected Inquiry data, and commercial archives from evidence.

## Version Validation

- [ ] Exact WordPress Core, PHP, MariaDB, web-server, active theme, and active plugin versions match approvals.
- [ ] WordPress Core and supported component integrity/checksums pass.
- [ ] Package provenance, license state where observable, support lifecycle, and compatibility evidence are attached.
- [ ] No unapproved plugin, theme, must-use plugin, drop-in, runtime package, or dependency is present.
- [ ] Plugin Inventory, Environment Report, and WordPress Baseline match runtime evidence.

## Permalinks

- [ ] Home/site URLs and HTTPS behavior match the approved environment.
- [ ] Rewrite capability works without editing unapproved URL architecture.
- [ ] Selected permalink structure is separately approved and recorded before mutation.
- [ ] Canonical, redirect, 404, query-string, Admin, REST, and feed behavior are checked within scope.
- [ ] Server rules contain no secrets or unexplained directives and rollback is proven.

## Media Uploads

- [ ] Approved non-sensitive fixture can be uploaded, retrieved, inspected, and deleted.
- [ ] Allowed type/size/dimension, MIME validation, generated variants, path, URL, ownership, and modes are observed.
- [ ] Script execution and unsafe direct access are blocked in uploads.
- [ ] Disk/quota impact, cleanup, backup/restore, privacy, and error logging are verified.
- [ ] No project media or production personal data is used for this validation.

## Theme

- [ ] Blocksy is the only approved active vendor theme for this stage.
- [ ] Exact version/source/integrity/compatibility and activation state are recorded.
- [ ] No custom theme, child theme implementation, template edit, Customizer change, hook, CSS, JavaScript, or project design is introduced.
- [ ] Frontend, Admin, RTL capability, mobile smoke behavior, and accessibility baseline exhibit no blocking error.
- [ ] Theme-stage checkpoint restoration returns the prior accepted state.

## WooCommerce

- [ ] Exact approved version/source/integrity/compatibility and activation state are recorded.
- [ ] Installer-created files, tables, options, pages, roles, capabilities, jobs, and endpoints are inventoried.
- [ ] No products, demo data, tax/shipping/payment/business settings, public prices, or unauthorized ordering flow are created.
- [ ] Inquiry First and No Public Pricing remain enforced by scope; implementation is not claimed.
- [ ] Admin/frontend/cron/log/database health and rollback pass.

## Elementor

- [ ] Elementor Pro exact version/source/integrity/license/compatibility is recorded only after every required dependency is explicitly approved.
- [ ] Installed dependencies exactly match the approved dependency graph.
- [ ] No page, global template, loop template, Theme Builder asset, reusable block, CSS, or project content is created.
- [ ] Admin/frontend/RTL/mobile smoke behavior contains no blocking error.
- [ ] Activation-stage rollback restores the prior accepted state.

## Blocksy

- [ ] Blocksy and Blocksy Pro exact versions, sources, integrity, license state, dependency relation, and compatibility are recorded.
- [ ] No header, footer, sidebar, archive, single, hook, Customizer, typography, color, container, or performance customization is made.
- [ ] Theme and companion package expose no blocking PHP, JavaScript, REST, Admin, frontend, RTL, or mobile error.
- [ ] No custom/child theme assumption or artifact exists.
- [ ] Each Blocksy checkpoint restores independently.

## PHP Extensions

- [ ] Active PHP SAPI, configuration files, extension names/versions, and effective settings are observed.
- [ ] Required extensions are justified by exact WordPress/component compatibility evidence.
- [ ] Missing, duplicate, deprecated, unsupported, or unnecessary extensions are reported.
- [ ] OPcache, image processing, database, HTTP, crypto, internationalization, XML, archive, session, and file behavior are validated as applicable.
- [ ] Extension or configuration changes require separate approval and rollback.

## Security

- [ ] HTTPS, authentication, sessions, Admin access, least privilege, secrets, filesystem, uploads, database, logs, cron, email, backups, updates, APIs, and error exposure pass approved controls.
- [ ] No default/shared credentials, exposed keys, debug display, directory listing, executable upload, public backup, or Git-secret leakage exists.
- [ ] Installer/default accounts, roles, capabilities, content, endpoints, and scheduled jobs are inventoried and reviewed.
- [ ] Vulnerability/integrity findings have owner, severity, treatment, evidence, and approval.
- [ ] No unapproved security plugin is introduced.

## Performance

- [ ] Server response, Admin response, PHP/database errors, resource use, cache headers, media behavior, and scheduled work are measured on the named environment.
- [ ] Test method, sample, conditions, evidence time, limits, and acceptance owner are recorded.
- [ ] Results are treated as a smoke baseline, not a production-capacity claim without representative load evidence.
- [ ] No LiteSpeed Cache or other unapproved performance plugin/configuration is introduced.
- [ ] Blocking regression invokes rollback.

## Acceptance

- [ ] Every mandatory check passes or has an approved exception with owner, expiry, risk, and remediation.
- [ ] Exact observed versions and state are reflected in inventory/baseline records.
- [ ] Rollback checkpoint is restored in isolation and accepted.
- [ ] Founder, technical, security, and operations approvals are recorded.
- [ ] Next stage has a separate go/no-go decision.

## Current Outcome

`NOT APPLICABLE / NO-GO — NO AUTHORIZED WORDPRESS INSTALLATION OR COMPONENT ACTIVATION EXISTS`

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 01C post-install evidence checklist; no runtime result asserted. |

## Navigation

- [Hosting Validation Checklist](HOSTING_VALIDATION_CHECKLIST.md)
- [WordPress Installation Checklist](WORDPRESS_INSTALLATION_CHECKLIST.md)
- [Plugin Installation Sequence](PLUGIN_INSTALLATION_SEQUENCE.md)
- [Rollback Plan](ROLLBACK_PLAN.md)
- [Sprint 01C Audit](../../docs/AUDIT_REPORT_SPRINT01C.md)
