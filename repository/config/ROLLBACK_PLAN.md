# Rollback Plan

## Document Control

- **Document ID:** `repository/config/ROLLBACK_PLAN.md`
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Build Engineer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** Before installation or component change and on environment, backup, recovery, sequence, ownership, or risk change
- **Lifecycle:** Review
- **Source of Truth:** Future approved backup/restore evidence, [Engineering Guidelines](../../docs/ENGINEERING_GUIDELINES.md), and the accepted state preceding each change
- **Dependencies:** [Hosting Validation Checklist](HOSTING_VALIDATION_CHECKLIST.md), [Engineering Guidelines](../../docs/ENGINEERING_GUIDELINES.md), and future approved backup/recovery ownership
- **Related Documents:** [Plugin Installation Sequence](PLUGIN_INSTALLATION_SEQUENCE.md), [Post-Install Validation](POST_INSTALL_VALIDATION.md), [WordPress Baseline](WORDPRESS_BASELINE.md), and [Sprint 01C Audit](../../docs/AUDIT_REPORT_SPRINT01C.md)
- **Traceability:** CP-001 through CP-010, S01A-007 through S01A-010, S01B-001 through S01B-005, and S01C-001 through S01C-008
- **AI Compatibility:** AI-readable rollback gate; a documented checkpoint is not assumed restorable without isolated restore evidence
- **Approval:** Pending Founder/technical/security/operations approval; no backup or restore has been performed by Sprint 01C

## Purpose

Define the backup, recovery, checkpoint, failure, and restore-validation controls required before a future WordPress or approved component installation.

## Rollback Principles

- Rollback restores the complete last accepted state; deactivation, deletion, or manual file replacement alone does not prove recovery.
- Every mutation requires a current checkpoint created and restore-tested before execution.
- Backups remain outside Git and outside the live application failure domain.
- Recovery evidence must not expose credentials, secrets, personal data, protected Inquiry data, or commercial packages.
- Failed restore, incomplete scope, unknown target state, or missing authority makes the change `NO-GO`.

## Backup

- [ ] Backup owner, operator, approver, storage owner, recovery owner, and emergency contacts are assigned.
- [ ] Scope includes target inventory, database, application/configuration state, approved secrets recovery path, uploads, permissions/ownership, scheduled jobs, DNS/TLS references, and required service settings.
- [ ] Exact target, timestamp, environment, component versions, manifest, checksums, dependencies, and accepted-state identifier are recorded.
- [ ] Encryption, key custody, access, immutability, retention, deletion, location/provider separation, monitoring, and audit evidence are approved.
- [ ] Backup excludes transient/unneeded data only through explicit reviewed rules.
- [ ] Backup completion, integrity, freshness, completeness, and isolated restoration pass before mutation.

## Recovery

- [ ] Recovery target and isolation prevent overwrite of an accepted or production state.
- [ ] Recovery order for infrastructure, storage, database, files, configuration/secrets, permissions, services, DNS/TLS, cron/email, and validation is approved.
- [ ] Required tools, access, keys, packages, exact versions, owners, time window, and communication path are available.
- [ ] Recovery point and recovery time objectives are approved using measured evidence when available.
- [ ] Partial recovery, dependency mismatch, data divergence, secret rotation, DNS/cache effects, and failed cutover behavior are defined.
- [ ] Return-to-service requires independent technical, security, operations, and Founder acceptance.

## Rollback Checkpoints

| Checkpoint | State | Required before | Minimum evidence | Current status |
| --- | --- | --- | --- | --- |
| `R0` | Target pre-install state | WordPress package placement or installer write | Empty/known target inventory, database state, configuration/services, permissions, backup manifest, integrity, isolated restore | Missing |
| `R1` | Accepted clean WordPress | Blocksy installation | Exact Core/runtime state, database/files/configuration, HTTPS, Admin, permalinks capability, uploads, security, backup and isolated restore | Missing |
| `R2` | Accepted WordPress + Blocksy | WooCommerce installation | `R1` evidence plus exact Blocksy state, no customization, health, backup and isolated restore | Missing |
| `R3` | Accepted WordPress + Blocksy + WooCommerce | Blocksy Pro installation | `R2` evidence plus exact WooCommerce state, generated-state inventory, no products/business configuration/public pricing, backup and isolated restore | Missing |
| `R4` | Accepted Blocksy Pro state | Elementor Pro installation | `R3` evidence plus exact Blocksy Pro/dependency/license state, no customization, backup and isolated restore | Missing |
| `R5` | Accepted Elementor Pro state | Any later authorized implementation sprint | `R4` evidence plus exact Elementor Pro/approved dependencies, no pages/templates/content, backup and isolated restore | Missing |

Checkpoint names describe planned states only. They do not prove that any installation, backup, or restore exists.

## Failure Criteria

Invoke rollback and stop when:

- Authorization, exact version/source/license/dependency, compatibility, package integrity, or target identity differs from approval.
- A prerequisite/checkpoint is missing, stale, incomplete, corrupt, inaccessible, or not independently restorable.
- Installation/activation errors, PHP/database errors, unavailable Admin/frontend, HTTPS/redirect failure, permalink failure, upload failure, or permissions failure occurs.
- Unexpected files, tables, options, users, roles, capabilities, pages, products, demo content, templates, scheduled jobs, services, network calls, or public endpoints appear.
- Public pricing, cart/checkout ordering, an unapproved business flow, custom/child theme implementation, Gravity Forms, LiteSpeed Cache, or Phase 1 AI feature is introduced.
- Security, privacy, integrity, logging, monitoring, resource, email, cron, backup, restore, or smoke-performance acceptance fails.
- The accepted prior state cannot be proven after restoration.

## Rollback Procedure Gate

- [ ] Stop writes, isolate the failed stage, record incident/change identifiers, and notify assigned authority.
- [ ] Preserve failure evidence and logs without preserving exposed secrets or unsafe artifacts.
- [ ] Select the immediately preceding accepted checkpoint and confirm its manifest/integrity.
- [ ] Restore in the approved order using approved access and exact packages/configuration.
- [ ] Rotate affected secrets and invalidate unsafe sessions/artifacts where required.
- [ ] Complete Restore Validation before traffic, Admin work, cron, email, or further installation resumes.
- [ ] Update inventory, baseline, health, decision/audit records, risks, and owner actions.
- [ ] Require a new go/no-go approval before retry.

## Restore Validation

- [ ] Restored files, database, configuration, permissions, services, versions, checksums, and dependencies match the checkpoint manifest.
- [ ] HTTPS, Admin/frontend, database connectivity, permalinks capability, uploads, cron, email, logs, monitoring, backups, and health match the accepted state.
- [ ] No failed-stage file, table, option, role, capability, content, job, cache, secret, or public behavior remains.
- [ ] Security/integrity scan and protected-data checks pass.
- [ ] Data loss/divergence, recovery duration, evidence gaps, and residual risks are recorded.
- [ ] Independent technical, security, operations, and Founder reviewers accept the restored state.

## Current Outcome

`NO-GO — NO REAL TARGET, BACKUP, RESTORE TEST, CHECKPOINT, RECOVERY OWNER, OR APPROVAL EVIDENCE EXISTS`

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 01C rollback plan; checkpoints are planned and no backup/restore is claimed. |

## Navigation

- [Hosting Validation Checklist](HOSTING_VALIDATION_CHECKLIST.md)
- [WordPress Installation Checklist](WORDPRESS_INSTALLATION_CHECKLIST.md)
- [Plugin Installation Sequence](PLUGIN_INSTALLATION_SEQUENCE.md)
- [Post-Install Validation](POST_INSTALL_VALIDATION.md)
- [Sprint 01C Audit](../../docs/AUDIT_REPORT_SPRINT01C.md)
