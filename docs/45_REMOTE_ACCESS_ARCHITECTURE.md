# Remote Access and Iran Execution Constraints Architecture

## Document Control

- **Document ID:** `docs/45_REMOTE_ACCESS_ARCHITECTURE.md`
- **Status:** Review
- **Authority:** Architecture Proposal
- **Owner:** Founder
- **Reviewer:** Build Engineer, Security Reviewer, and Operations Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On access model, hosting capability, network constraint, deployment, security, recovery, toolchain, or ownership change
- **Lifecycle:** Review
- **Source of Truth:** Accepted Core Project Principles, [Repository Baseline v1.0](BASELINE_v1.0.md), [Engineering Guidelines](ENGINEERING_GUIDELINES.md), and future approved access/hosting evidence
- **Dependencies:** [Implementation Readiness](IMPLEMENTATION_READINESS.md), [Repository Implementation Rules](../repository/IMPLEMENTATION_RULES.md), [Hosting Validation Checklist](../repository/config/HOSTING_VALIDATION_CHECKLIST.md), and [Rollback Plan](../repository/config/ROLLBACK_PLAN.md)
- **Related Documents:** [SSH Access Checklist](../repository/config/SSH_ACCESS_CHECKLIST.md), [Deployment Access Policy](../repository/config/DEPLOYMENT_ACCESS_POLICY.md), [Iran Execution Risk Register](../repository/config/IRAN_EXECUTION_RISK_REGISTER.md), [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md), and [Sprint 01D Audit](AUDIT_REPORT_SPRINT01D.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, FRZ-001 through FRZ-006, S01A-001 through S01A-010, S01B-001 through S01B-005, S01C-001 through S01C-008, and RA-001 through RA-012
- **AI Compatibility:** AI-readable proposed remote-execution architecture; no autonomous access, credential authority, connection authority, deployment authority, or Phase 1 AI product feature
- **Approval:** Pending Founder, technical, security, operations, hosting, and recovery review; no SSH setup or connection is authorized

## Purpose

Define a controlled, auditable, reversible, and Founder-manageable architecture for future remote execution under Iran-specific connectivity and service-access constraints. This document does not establish a remote, change hosting, create credentials, connect to a server, or install WordPress.

## Why Direct Hosting Access Is Needed

Future project delivery needs a controlled path that can:

- Apply an approved change to an exact project path without repeated manual File Manager operations.
- Preserve Git identity, change history, review evidence, and rollback references.
- Support read-only environment inspection and future WP-CLI validation when explicitly authorized and available.
- Reduce upload mistakes, partial replacements, path confusion, and undocumented server drift.
- Allow repeatable Build Engineer procedures while keeping daily Founder operation simple.

Direct access is not inherently trusted. It is acceptable only when identity, scope, path, permissions, backup, validation, logging, rollback, and approval are all proven.

## Current Environment

| Component | Current evidence classification | Boundary |
| --- | --- | --- |
| MacBook | Sprint task identifies the intended Founder/operator device; Sprint 01B observed a local macOS workstation | Exact device identity, security posture, backup, key custody, and authorized operator remain unverified |
| VS Code | Intended local editing interface stated by Sprint 01D | Installation, version, extensions, workspace trust, and server access are not validated |
| Codex | Intended repository collaborator stated by Sprint 01D | No autonomous authority, credentials, server connection, or deployment permission |
| GitHub | Intended private remote and collaboration service | Baseline v1.0 records no approved primary remote, mirror, provider control, or recovery evidence |
| Server.ir hosting | Intended hosting target stated by Sprint 01D | Account, service, region, SSH, Git, PHP CLI, WP-CLI, cPanel, limits, support, and path are not verified |
| cPanel | Intended hosting control plane stated by Sprint 01D | URL, account, capabilities, MFA, file access, backup, terminal, and audit facilities are not verified |
| WordPress target | Future target | WordPress is not installed; target domain, path, database, staging boundary, and runtime are not verified |

Task-provided context is planning input, not proof of active service capability. Current readiness remains governed by Sprint 01B and Sprint 01C evidence.

## Recommended Architecture

```text
MacBook / VS Code / Codex
  -> approved local Git working copy
    -> GitHub Private Repository (future approved primary remote)
      -> controlled SSH deployment/access path
        -> Server.ir Hosting (capability unverified)
          -> confirmed Damavand project directory
            -> WordPress / WP-CLI (future, separately authorized)
```

Control flow:

1. Founder authorizes an exact task, target, evidence requirement, risk, and rollback.
2. Build Engineer works in a reviewed local Git change without storing secrets.
3. Approved history is pushed to the approved private remote when connectivity and policy permit.
4. A project-limited SSH identity reaches only the confirmed target path when future access is authorized.
5. Deployment uses an approved artifact or exact reviewed commit; it does not edit WordPress Core or vendor files.
6. Read-only checks, future WP-CLI validation, smoke tests, and rollback evidence close the change.

The arrows describe a proposed future route, not existing connectivity or deployment automation.

## Access Models

| Model | Security | Speed | Founder difficulty | Iran limitations | Rollback ability | Maintenance | Recommended status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — Manual cPanel only | Medium-to-low unless MFA, path controls, and logs are proven; prone to untracked edits | Low for repeated changes | Medium; visual but error-prone | May remain available when other services fail; browser timeout risk remains | Low unless every operation has external backup and file manifest | High manual burden and drift risk | Emergency fallback only |
| B — GitHub + manual upload | Medium; reviewed source but manual server transfer | Medium for small artifacts | Medium-to-high | GitHub and large uploads may be unstable independently | Medium if exact artifact and pre-upload backup exist | Manual synchronization remains fragile | Temporary fallback, not primary |
| C — SSH from MacBook to hosting | High when key-based, project-limited, logged, and approved; otherwise high risk | High for inspection and controlled transfer | Low for Founder when Build Engineer owns documented procedures | SSH reachability must be measured; may be more resilient than browser workflows but is not assumed | High with clean Git state, external backup, exact path, and tested restore | Manageable through later reviewed scripts/runbooks | Primary candidate after validation |
| D — GitHub deploy to hosting | High when hosting pull/deploy identity, protected branch, artifact, and logs are controlled | High | Low after setup | Depends on hosting-to-GitHub connectivity and provider capability | High with immutable commit/artifact and release checkpoints | Moderate; credential rotation and deploy hooks require ownership | Future candidate if hosting supports a secure pull/deploy path |
| E — GitHub Actions deploy | Potentially high with protected environments, short-lived/scoped secrets, approvals, and signed artifacts | High | Low after setup | Depends on reliable GitHub Actions and runner-to-host connectivity | High with immutable releases and automated rollback evidence | Moderate-to-high governance and pipeline burden | Future option only after hosting, GitHub, secret, and runner approval |

The comparison is architectural. Real security, speed, availability, and maintainability require measured target evidence.

## Recommended Model for Damavand Steel

### Primary

MacBook + VS Code + Codex + a future approved GitHub Private Repository + project-limited SSH to the intended Server.ir hosting target.

This is Model C with GitHub as the reviewed source-history and collaboration layer. It becomes usable only after the Git remote, SSH capability, key custody, target path, permissions, backup/restore, Git state, and approval gates pass.

### Future

GitHub Actions deployment may be evaluated only if the hosting service supports a secure and auditable connection, protected environments and secrets are approved, rollback is tested, and Iran-related connectivity is measured. Its mention is not approval to create a workflow or secret.

### Fallback

Manual cPanel upload is reserved for an approved emergency when primary paths are unavailable. It requires the same change record, exact artifact, pre-change backup, path confirmation, post-change validation, rollback, and audit evidence. File Manager is not a routine source-of-truth workflow.

## Security Rules

- No root access.
- Never share or request passwords, private keys, recovery codes, database credentials, API tokens, license keys, or secrets in chat, prompts, tickets, screenshots, logs, Git, or documentation.
- Prefer a passphrase-protected SSH key whose private half remains under approved local custody.
- Use a named, project-limited hosting user where supported; never reuse a personal or shared administrative identity for automation.
- Restrict filesystem and command access to the confirmed Damavand project path and required read/write operations.
- Require MFA for GitHub, cPanel, registrar/DNS, and hosting accounts where supported.
- Back up and prove restoration before every deployment or server mutation.
- Never expose or commit `wp-config.php`, `.env`, hosting configuration secrets, authentication salts, database credentials, or service credentials.
- Never commit commercial archives or license keys.
- Use environment variables or secure hosting configuration only after the exact mechanism and permissions are approved.
- Keep WordPress Core and vendor packages immutable to ad hoc editing; changes use supported update/configuration paths.
- Log identity, time, target, reviewed commit/artifact, command class, result, validation, and rollback without logging secrets.
- High-risk and destructive commands require explicit per-change approval and a verified current backup.

## Iran Constraints

The following are Sprint 01D planning risks and must be measured on the approved operator network and hosting target. They are not universal availability claims:

- GitHub may be unstable, slow, filtered, or intermittently unavailable.
- WordPress.org and plugin/theme repository access may be blocked or unreliable.
- OpenAI/Codex availability may be unstable; execution must not depend on an active AI session for recovery.
- cPanel may remain reachable when GitHub is unavailable, but browser sessions may time out.
- Direct plugin installation or updates may fail because the server cannot reach a vendor repository.
- Commercial license activation may fail or require a lawful and approved alternate network path; no VPN method is prescribed by this architecture.
- Verified packages may require a controlled manual upload when direct download is unavailable.
- SSH may be more stable than browser workflows on some paths, but this must be tested rather than assumed.
- Large uploads may fail or resume incorrectly; artifacts require checksum and completeness validation.
- Backup-first operation is mandatory because connectivity loss can interrupt a change.

Fallbacks must preserve provenance, integrity, licensing, least privilege, approval, and rollback. Connectivity pressure never permits an unverified package or exposed credential.

## Founder Usability Constraints

- The Founder is not expected to be a developer or server administrator.
- Daily operation must not require memorizing or running complex commands.
- Repeatable scripts and runbooks may be created in a later, separately authorized implementation task after exact hosting evidence exists.
- Checklists and operational prompts must use short, observable, non-technical instructions with explicit stop conditions.
- Build Engineer procedures must produce a Founder-readable result, risk, rollback point, and next decision.
- High-risk commands require explicit Founder approval or approved delegation.
- Any destructive command requires current backup and restore verification before approval.
- Emergency procedures must work without Codex and must identify the hosting support escalation route.

## Launch Speed Impact

After validation and approval, the recommended path is expected to improve:

- Faster updates by transferring an exact reviewed artifact or commit to a confirmed path.
- Fewer manual uploads and fewer opportunities for partial or wrong-directory replacement.
- Better rollback through Git references, pre-deploy checkpoints, and restoration evidence.
- Better auditability through identity, commit/artifact, deployment, validation, and approval records.
- Easier Codex-assisted preparation while keeping access and execution under human approval.
- Cleaner Git history by separating reviewed source changes from runtime state and manual server edits.
- Safer plugin/theme updates through package provenance, compatibility, backup, and staged validation.
- Faster MVP launch by making approved tasks repeatable and reducing avoidable handoffs.

These are expected process benefits, not measured delivery-time or reliability claims.

## Risk Controls

1. Verify the exact target identity and project path.
2. Confirm a clean, expected Git state and record the reviewed commit/artifact before change.
3. Create a complete pre-deploy backup outside the live failure domain and pass isolated restore verification.
4. Review a dry-run, diff, file list, or no-change preview where the approved tool supports it.
5. Apply least privilege and restrict the SSH identity to the required project scope where supported.
6. Use future WP-CLI only when installed/validated and only for an approved command class; do not assume availability.
7. Run post-deploy health, HTTPS, Admin/frontend, upload, permalink, Inquiry/No Public Pricing, log, security, and smoke checks applicable to the change.
8. Roll back on mismatch, interruption, unexpected file/database change, security failure, or failed validation.
9. Record Founder and specialist approval at the defined entry and exit gates.

## Required Future Setup Checklist

- [ ] Confirm Server.ir hosting account/service identity and SSH support with provider evidence.
- [ ] Create a dedicated SSH key on the approved MacBook under an approved key-custody process.
- [ ] Add only the public key to the approved cPanel/hosting account.
- [ ] Test SSH authentication and record host-key verification without exposing secrets.
- [ ] Confirm the exact Damavand project path and prevent access to unrelated hosting paths where supported.
- [ ] Confirm active PHP CLI version and configuration path.
- [ ] Confirm WP-CLI availability; install it only through a separate authorized task if allowed and required.
- [ ] Confirm Git availability/version and safe repository ownership on hosting.
- [ ] Confirm the approved database access method without recording credentials.
- [ ] Confirm complete backup and isolated restore capability.
- [ ] Confirm staging or an isolated safe test directory.
- [ ] Confirm approved domain/subdomain and environment strategy.
- [ ] Confirm GitHub private remote, ownership, MFA, access, protection, recovery, and connectivity.
- [ ] Complete the [SSH Access Checklist](../repository/config/SSH_ACCESS_CHECKLIST.md) and [Deployment Access Policy](../repository/config/DEPLOYMENT_ACCESS_POLICY.md).

## Go / No-Go Decision Rules

### GO for actual SSH setup only if

- SSH capability and authorized target identity are confirmed.
- A complete current backup exists and restoration is proven.
- The local Git state is clean and the exact reviewed state is identified.
- The project path and access boundary are confirmed.
- No secret is exposed in the repository, evidence, chat, or procedure.
- A tested rollback path and accountable rollback authority exist.
- Founder, security, operations, and hosting approvals required for setup are recorded.

### NO-GO

- SSH target identity or project path is unclear.
- Backup or restore evidence is unavailable.
- Git has unexplained changes or an unresolved operation.
- A credential or secret is exposed or requested through an unsafe channel.
- Required package/plugin/license source or integrity evidence is unavailable for the intended task.
- Founder approval or required specialist approval is missing.
- Access requires root, shared credentials, unrelated-directory permission, or an unapproved workaround.

## Proposed Architecture Decisions

| ID | Proposal | Status |
| --- | --- | --- |
| RA-001 | Treat Sprint 01D as documentation and access-architecture preparation only. | Review; no connection authority |
| RA-002 | Use a future approved private GitHub repository as collaboration/history remote, not as runtime storage. | Review; remote not established |
| RA-003 | Prefer project-limited, key-based SSH from the approved MacBook as the primary future server access path. | Review; capability unverified |
| RA-004 | Evaluate GitHub-to-host deployment and GitHub Actions only after hosting/connectivity/security evidence and separate approval. | Review |
| RA-005 | Reserve manual cPanel upload for controlled emergency fallback. | Review |
| RA-006 | Prohibit root and shared identities; enforce least privilege and project-path restriction where supported. | Review |
| RA-007 | Keep credentials, private keys, `wp-config.php`, environment secrets, and license keys outside Git and collaboration channels. | Required security boundary |
| RA-008 | Require complete pre-change backup and proven restore before every server mutation. | Review; evidence missing |
| RA-009 | Require a clean expected Git state and exact reviewed commit/artifact before deployment. | Review |
| RA-010 | Require validation, audit evidence, and tested rollback for every deployment. | Review |
| RA-011 | Keep routine Founder operation simple and delegate complex technical execution through approved roles and runbooks. | Review |
| RA-012 | Maintain connectivity-independent fallback and recovery procedures without weakening package integrity, licensing, security, or approval. | Review |

## Founder Decisions

- Approve or reject RA-001 through RA-012.
- Approve the intended Server.ir account/service as the target only after provider evidence.
- Approve GitHub as the primary private remote, including ownership, access, MFA, recovery, protection, and backup.
- Approve the SSH identity owner, key custodian, target scope, hosting user, and revocation process.
- Approve primary, future, and emergency access models plus delegation and emergency authority.
- Approve backup/restore ownership, staging/environment strategy, and actual SSH setup go/no-go.

## Open Questions

- Does the exact Server.ir plan support SSH, dedicated/project-limited users, Git, PHP CLI, WP-CLI, host-key evidence, and audit logs?
- What is the exact Damavand project path and isolation boundary?
- What private GitHub organization/account, recovery owner, protection model, and independent backup will be approved?
- What staging or safe test target is available?
- What backup method has a measured, independently verified restore?
- Which operator and reviewer roles receive access, for how long, and through what revocation process?
- Which lawful, secure fallback is approved when GitHub, vendor licensing, or repository access is unavailable?

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 01D proposed remote-access and Iran execution-constraints architecture; no setup or connection. |

## Navigation

- [Repository Baseline v1.0](BASELINE_v1.0.md)
- [Engineering Guidelines](ENGINEERING_GUIDELINES.md)
- [SSH Access Checklist](../repository/config/SSH_ACCESS_CHECKLIST.md)
- [Deployment Access Policy](../repository/config/DEPLOYMENT_ACCESS_POLICY.md)
- [Iran Execution Risk Register](../repository/config/IRAN_EXECUTION_RISK_REGISTER.md)
- [Sprint 01D Audit](AUDIT_REPORT_SPRINT01D.md)
