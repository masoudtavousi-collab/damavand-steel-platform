# Deployment Access Policy

## Document Control

- **Document ID:** `repository/config/DEPLOYMENT_ACCESS_POLICY.md`
- **Status:** Review
- **Authority:** Proposed Supporting Policy
- **Owner:** Founder
- **Reviewer:** Build Engineer, Security Reviewer, and Operations Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** Before access grant/deployment and on role, target, privilege, secret, backup, rollback, emergency, or provider change
- **Lifecycle:** Review
- **Source of Truth:** Accepted Core Project Principles, [Engineering Guidelines](../../docs/ENGINEERING_GUIDELINES.md), and future approved access decisions/evidence
- **Dependencies:** [Remote Access Architecture](../../docs/45_REMOTE_ACCESS_ARCHITECTURE.md), [Repository Implementation Rules](../IMPLEMENTATION_RULES.md), [Hosting Validation Checklist](HOSTING_VALIDATION_CHECKLIST.md), and [Rollback Plan](ROLLBACK_PLAN.md)
- **Related Documents:** [SSH Access Checklist](SSH_ACCESS_CHECKLIST.md), [Iran Execution Risk Register](IRAN_EXECUTION_RISK_REGISTER.md), [Plugin Installation Sequence](PLUGIN_INSTALLATION_SEQUENCE.md), and [Sprint 01D Audit](../../docs/AUDIT_REPORT_SPRINT01D.md)
- **Traceability:** CP-001 through CP-010, FRZ-001 through FRZ-006, S01A-001 through S01A-010, S01C-001 through S01C-008, and RA-001 through RA-012
- **AI Compatibility:** AI-readable proposed access policy; AI may prepare reviewed changes but cannot hold credentials, grant access, approve, connect, deploy, or invoke emergency authority
- **Approval:** Pending Founder, security, operations, hosting, and technical review; grants no current access

## Purpose

Define who may access a future Damavand hosting target, what may change, which approvals apply, how secrets/backups/rollback are controlled, and how emergency access is bounded.

## Policy Scope

This policy applies to future access through SSH, cPanel, GitHub deployment, GitHub Actions, WP-CLI, database tools, hosting support, and emergency manual upload. It does not establish an account, credential, remote, connection, workflow, or deployment.

## Who Can Access

| Role | Default access | Permitted purpose | Boundary |
| --- | --- | --- | --- |
| Founder | Approval and account-custody access as required | Approve target, operators, risk, backup, deployment, rollback, emergency use, and revocation | Not required to perform routine technical commands |
| Build Engineer | No access until task-specific grant | Read-only validation and explicitly approved deployment/change | Named, time-bounded, project-limited, least privilege; no root |
| Security Reviewer | Read-only evidence by default | Review identity, secrets, permissions, logs, vulnerabilities, and incident controls | No deployment without separate approval |
| Operations/Hosting Reviewer | Read-only evidence or provider-scoped support | Validate target, path, runtime, backup, restore, monitoring, and provider capability | Changes require task-specific approval and evidence |
| Content/Admin operator | WordPress Admin only after future role approval | Approved content/administrative workflow | No shell, hosting, Git, database, plugin/theme, or secret access by default |
| Codex/AI collaborator | Repository context only | Prepare documentation, diffs, checks, and proposed commands for human review | No credentials, direct access, autonomous connection, approval, or deployment |

Access is denied by default. A role description is not an access grant.

## What Can Be Changed

Only an explicitly authorized task may change:

- Exact reviewed files/configuration inside the confirmed Damavand project boundary.
- Approved WordPress configuration or content through supported interfaces after WordPress implementation is separately authorized.
- Approved plugin/theme package state through supported vendor/WordPress mechanisms after exact package approval.
- Approved environment configuration through the hosting provider's secure mechanism.
- Approved deployment metadata, logs, and health evidence without secrets.

Every change must identify target, owner, reviewed commit/artifact, pre-state, file/database/configuration impact, tests, backup, rollback, window, and approval.

## Approval Requirements

| Activity | Minimum approval before action |
| --- | --- |
| Create/revoke SSH key or hosting user | Founder + security + operations/hosting |
| First connection or target/path validation | Founder + operations/hosting; read-only scope |
| Add/modify Git remote, deploy key, webhook, runner, or Actions secret | Founder + security + repository/operations review |
| Deploy reviewed files/configuration | Founder/delegate + Build Engineer + applicable technical/security/operations review |
| WordPress/WP-CLI mutation | Separate WordPress implementation authorization plus applicable domain/security approval |
| Database write/import/migration | Separate data-change authorization, backup/restore proof, technical/security/privacy review |
| Plugin/theme install/update/license activation | Exact package/dependency/license approval, backup, compatibility evidence, and Founder approval |
| DNS/TLS/email/cron/permission/runtime change | Founder + operations/security + provider evidence and rollback |
| Emergency access | Emergency authority defined below; retrospective review does not replace pre-approval when pre-approval is possible |

## Forbidden Actions

- Root login or root deployment.
- Shared, anonymous, inherited, or unowned credentials.
- Password, private-key, token, license-key, database credential, recovery code, or secret sharing through chat/Git/docs/logs/screenshots.
- Direct edits to WordPress Core, vendor plugin/theme files, or an unconfirmed server path.
- Unreviewed File Manager edits, direct database writes, production experiments, or changes outside the approved task.
- Installing WordPress, plugins, themes, WP-CLI, packages, scripts, agents, cron jobs, runners, or services without explicit scope and approval.
- Disabling security, logging, backup, integrity, access controls, Inquiry First, No Public Pricing, or other accepted constraints.
- Custom/child theme implementation, Gravity Forms, LiteSpeed Cache, or Phase 1 AI features.
- Deployment from a dirty/unexpected Git state or unverified package source.
- Continuing after connectivity loss, partial transfer, mismatch, exposed secret, failed backup, failed validation, or unavailable rollback.

## Backup Rules

- Create a complete checkpoint before every server, database, content, configuration, plugin, theme, runtime, DNS, TLS, or access mutation.
- Store backups outside Git and outside the live application failure domain under approved encrypted custody.
- Record target, time, scope, versions, manifest, checksums, retention, owner, and restore procedure without secrets.
- Verify integrity and isolated restoration before change approval.
- Do not treat a hosting snapshot, export, archive, or backup-status message as recoverable until restoration is proven.

## Rollback Rules

- Define the immediately preceding accepted checkpoint and rollback authority before action.
- Trigger rollback on path/identity mismatch, partial transfer, unexpected diff, integrity/security failure, service failure, public-pricing/transaction exposure, or failed smoke test.
- Restore complete state; deletion, deactivation, or manual replacement alone is not proven rollback.
- Validate restored versions, files, database, configuration, permissions, HTTPS, Admin/frontend, logs, scheduled work, security, and accepted business boundaries.
- Record residual risk and require new approval before retry.

## Secret Handling

- Private keys and secrets remain outside the repository and AI context.
- Use dedicated, scoped, revocable identities; prefer key-based SSH and provider secret stores where approved.
- Store only public key/fingerprint, secret reference name, owner, purpose, creation/review/expiry, and revocation evidence in documentation.
- Redact command output, logs, screenshots, and support messages before repository inclusion.
- Rotate/revoke on exposure, operator change, device loss, task completion, scope change, or provider incident.
- Never store `wp-config.php`, `.env` secrets, authentication salts, database credentials, GitHub tokens, deploy keys, or license keys in Git.

## Emergency Access

- Emergency access is limited to service recovery, security containment, secret revocation, or rollback when the primary approved route is unavailable.
- Founder or a pre-approved emergency delegate authorizes the target, operator, scope, duration, fallback method, and rollback when feasible.
- Manual cPanel upload may be used only with an exact reviewed artifact, path confirmation, current restorable backup, integrity check, and post-change validation.
- Emergency access never authorizes root, shared secrets, unrelated-directory access, unverified packages, business-rule changes, or bypass of evidence retention.
- Revoke temporary access immediately after recovery and complete an incident/change review.

## Access Grant Record Requirements

- Named role and accountable owner.
- Exact environment, account, project path, permissions, and command/change class.
- Business/technical reason, task ID, start, expiry, reviewer, and approval.
- Authentication method and public fingerprint/reference only.
- Backup/rollback checkpoint and evidence location.
- Session/deployment log location, validation result, and revocation result.

## Current Status

`NO ACCESS GRANTED — SSH, CPANEL, GITHUB DEPLOYMENT, WP-CLI, DATABASE, AND HOSTING CAPABILITIES REMAIN UNVERIFIED`

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 01D proposed deployment-access policy; no access or hosting change. |

## Navigation

- [Remote Access Architecture](../../docs/45_REMOTE_ACCESS_ARCHITECTURE.md)
- [SSH Access Checklist](SSH_ACCESS_CHECKLIST.md)
- [Iran Execution Risk Register](IRAN_EXECUTION_RISK_REGISTER.md)
- [Rollback Plan](ROLLBACK_PLAN.md)
- [Sprint 01D Audit](../../docs/AUDIT_REPORT_SPRINT01D.md)
