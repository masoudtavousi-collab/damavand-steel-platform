# WordPress Installation Checklist

## Document Control

- **Document ID:** `repository/config/WORDPRESS_INSTALLATION_CHECKLIST.md`
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Build Engineer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** Before a clean WordPress installation and on scope, environment, version, security, recovery, or procedure change
- **Lifecycle:** Review
- **Source of Truth:** [WordPress Solution Blueprint](../../docs/35_WORDPRESS_BLUEPRINT.md), [Hosting Validation Checklist](HOSTING_VALIDATION_CHECKLIST.md), and future approved exact installation plan
- **Dependencies:** [Pre-Implementation Checklist](../PRE_IMPLEMENTATION_CHECKLIST.md), [Hosting Validation Checklist](HOSTING_VALIDATION_CHECKLIST.md), and [Rollback Plan](ROLLBACK_PLAN.md)
- **Related Documents:** [WordPress Baseline](WORDPRESS_BASELINE.md), [Post-Install Validation](POST_INSTALL_VALIDATION.md), [Engineering Guidelines](../../docs/ENGINEERING_GUIDELINES.md), and [Sprint 01C Audit](../../docs/AUDIT_REPORT_SPRINT01C.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, WP-FC-001 through WP-FC-005, WPBP-001 through WPBP-010, S01B-002 through S01B-005, and S01C-001 through S01C-008
- **AI Compatibility:** AI-readable procedure gate; no step may be treated as executed without runtime evidence
- **Approval:** Pending Founder/technical/security/operations approval; all steps remain unchecked and no installation is authorized

## Purpose

Define every evidence and control step required for a future clean WordPress installation without running an installer or selecting unresolved values.

## Execution Rules

- This is a checklist, not an installation script.
- No step may begin until its dependencies and prior rollback checkpoint pass.
- Record exact commands/procedures in a separately approved execution record; do not invent them here.
- Stop on missing approval, mismatch, unexpected existing data/files, failed validation, or unavailable rollback.
- Do not proceed to plugin/theme installation until the clean WordPress checkpoint is accepted.

## Phase 0 — Authorization and Scope

- [ ] Founder approves the exact environment, installation scope, owner, reviewers, window, exclusions, success criteria, stop criteria, and rollback authority.
- [ ] Applicable architecture/Blueprint decisions and Sprint 01A/01B/01C gates are approved or explicitly bounded.
- [ ] Exact WordPress version and verified package source are approved.
- [ ] No page, product, taxonomy, template, business logic, or project content is in installation scope.
- [ ] Repository branch/change, evidence, documentation, and handoff requirements are approved.

## Phase 1 — Hosting Gate

- [ ] Every mandatory Hosting Validation Checklist item passes with evidence.
- [ ] Target identity, environment type, DNS/TLS, web server, PHP, MariaDB, storage, permissions, cron, email, backup, monitoring, and security owners are known.
- [ ] Target is isolated from unrelated applications and unapproved production/customer data.
- [ ] Required access is least-privilege, named, tested, and revocable.
- [ ] Maintenance/communication and incident contacts are ready.

## Phase 2 — Version and Package Gate

- [ ] Exact WordPress version is compatible with approved PHP/MariaDB/web-server versions.
- [ ] Official package provenance, checksum/signature verification method, license, and support lifecycle are approved.
- [ ] No “latest” alias or unpinned source is used.
- [ ] Package is inspected for expected contents before deployment.
- [ ] Acquisition and temporary-storage paths expose no credentials or unreviewed artifacts.

## Phase 3 — Pre-Installation Backup and Recovery

- [ ] Target pre-state inventory records files, database, DNS/TLS, permissions, configuration, and services.
- [ ] Checkpoint `R0 — pre-install` is created outside Git under approved custody.
- [ ] R0 integrity and isolated restoration are verified.
- [ ] Installation removal/rebuild procedure and decision authority are approved.
- [ ] Rollback time/data impact and failure communication are accepted.

## Phase 4 — Database Preparation

- [ ] Approved empty database and least-privilege application identity are provisioned.
- [ ] Database host/port/name/charset/collation/timezone/table-prefix choices are approved without documenting secrets.
- [ ] Connection encryption, firewall/access, timeout, resource, backup, monitoring, and log behavior pass.
- [ ] No existing table/data would be overwritten.
- [ ] Connection from the approved PHP runtime is tested safely.

## Phase 5 — Filesystem Preparation

- [ ] Approved web root and WordPress Core/`wp-content` boundaries are empty or contain only expected controlled placeholders.
- [ ] Effective deployment and web/PHP identities, ownership, modes, umask, ACLs, and extended attributes are approved.
- [ ] Core/vendor files, configuration, uploads, cache, logs, temporary files, and secrets have separate write/execute rules.
- [ ] Script execution is blocked in uploads.
- [ ] WordPress Core, uploads, dependencies, caches, logs, backups, secrets, and commercial archives remain excluded from Git.

## Phase 6 — WordPress Package Placement

- [ ] Verified exact WordPress package is placed only in the approved web root.
- [ ] File inventory/checksum and ownership/modes match the approved package and policy.
- [ ] No Core/vendor file is edited.
- [ ] Existing `wp-content` controlled boundaries are preserved or migrated through an approved plan.
- [ ] Unexpected files stop the installation and trigger investigation/rollback.

## Phase 7 — Configuration and Secrets

- [ ] Non-secret configuration source and secret manager/loader are approved.
- [ ] Database credentials, authentication keys/salts, licenses, service credentials, and private keys are generated/stored outside Git and evidence.
- [ ] Environment type, canonical URLs, `fa_IR`, `Asia/Tehran`, debug/log display, cron, filesystem method, file-edit/modification policy, memory, revisions, and update behavior are approved.
- [ ] Charset is `utf8mb4` only after database/runtime verification; collation is explicitly approved.
- [ ] No public pricing, plugin, theme, product, Inquiry, or business setting is added in Core configuration.

## Phase 8 — Installer Execution

- [ ] Final go/no-go is recorded immediately before execution.
- [ ] Installer uses the approved URL, site identity placeholder policy, locale, timezone, database, and least-privilege initial Admin process.
- [ ] Admin credentials are transmitted/stored securely and never copied into Git, logs, screenshots, or audit text.
- [ ] Installer output and timestamps are retained without secrets.
- [ ] Any unexpected default, error, redirect, file, table, or permission change stops execution.

## Phase 9 — Immediate Clean-Install Validation

- [ ] Exact WordPress version, checksums, database tables, site URLs, locale/timezone, HTTPS, and Admin access are verified.
- [ ] Default installer-created content/options are inventoried; no project content is created and removal/change requires approved scope.
- [ ] REST/API, login, logout, password reset, scheduled events, mail, updates, and health behavior are reviewed according to scope.
- [ ] Permalink capability and server rewrite behavior are tested without selecting an unapproved public URL policy.
- [ ] Upload write/read/serve/deny-execution behavior is tested with approved non-sensitive fixture evidence.

## Phase 10 — Security and Operations Validation

- [ ] File editor/modification, Admin access, authentication, sessions, headers, TLS, database, uploads, logs, backups, monitoring, cron, email, and incident controls pass.
- [ ] No secret or personal data is exposed in repository, web root, logs, errors, backups, or evidence.
- [ ] Checkpoint `R1 — clean WordPress` is created and restored in isolation.
- [ ] Rebuild and rollback procedures reproduce the accepted state.
- [ ] Blocking findings are closed before plugin/theme work.

## Phase 11 — Clean WordPress Acceptance

- [ ] Founder/technical/security/operations reviewers accept the exact clean-install evidence.
- [ ] WordPress Baseline is updated with actual version, environment, directory, database, permalink, uploads, security, and limitations.
- [ ] Repository Health, decisions, traceability, inventories, and audit are updated.
- [ ] Plugin Installation Sequence receives separate go/no-go approval.
- [ ] No page, product, Elementor template, WooCommerce business setting, Blocksy customization, or project content exists.

## Current Outcome

`NO-GO — HOSTING, RUNTIME, EXACT VERSION, PACKAGE, RECOVERY, AND APPROVAL EVIDENCE ARE MISSING`

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 01C clean WordPress installation checklist; no step executed. |

## Navigation

- [Hosting Validation Checklist](HOSTING_VALIDATION_CHECKLIST.md)
- [Plugin Installation Sequence](PLUGIN_INSTALLATION_SEQUENCE.md)
- [Post-Install Validation](POST_INSTALL_VALIDATION.md)
- [Rollback Plan](ROLLBACK_PLAN.md)
- [Sprint 01C Audit](../../docs/AUDIT_REPORT_SPRINT01C.md)
