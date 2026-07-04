# SSH Access Checklist

## Document Control

- **Document ID:** `repository/config/SSH_ACCESS_CHECKLIST.md`
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Build Engineer, Security Reviewer, and Operations Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** Before SSH setup or connection and on device, key, user, host, path, permission, tool, or revocation change
- **Lifecycle:** Review
- **Source of Truth:** [Remote Access Architecture](../../docs/45_REMOTE_ACCESS_ARCHITECTURE.md), future approved provider evidence, and future read-only connection evidence
- **Dependencies:** [Hosting Validation Checklist](HOSTING_VALIDATION_CHECKLIST.md), [Deployment Access Policy](DEPLOYMENT_ACCESS_POLICY.md), and [Rollback Plan](ROLLBACK_PLAN.md)
- **Related Documents:** [Iran Execution Risk Register](IRAN_EXECUTION_RISK_REGISTER.md), [Environment Report](ENVIRONMENT_REPORT.md), [WordPress Baseline](WORDPRESS_BASELINE.md), and [Sprint 01D Audit](../../docs/AUDIT_REPORT_SPRINT01D.md)
- **Traceability:** CP-001 through CP-010, S01C-001 through S01C-008, and RA-001 through RA-012
- **AI Compatibility:** AI-readable setup checklist; no command, credential, private key, connection, or access grant is embedded
- **Approval:** Pending Founder, security, operations, hosting, and Build Engineer review; every item is unchecked

## Purpose

Provide a simple, evidence-based checklist for future key-based SSH setup and read-only validation. Sprint 01D executes none of these steps.

## Safety Rules

- Do not paste passwords, private keys, passphrases, recovery codes, tokens, database credentials, license keys, or full secret-bearing configuration into chat, Git, screenshots, logs, or this checklist.
- Record only redacted fingerprints, public identifiers, evidence locations, owners, dates, results, and limitations.
- Stop on host mismatch, unclear path, root/shared access, excessive permission, exposed secret, missing backup/restore, or missing approval.
- A successful login does not authorize file, database, WordPress, plugin, theme, DNS, email, or hosting changes.

## Roles

| Role | Responsibility |
| --- | --- |
| Founder | Approves target, identity owner, access scope, risk, backup/restore, setup window, and go/no-go; is not expected to run complex commands |
| Build Engineer | Prepares the approved key/setup procedure, performs only authorized checks, records evidence, and stops on mismatch |
| Security Reviewer | Reviews key custody, identity, least privilege, host verification, secret handling, logging, expiry, and revocation |
| Operations/Hosting Reviewer | Confirms provider capability, account, target, project path, service constraints, backup, and recovery |

## Phase 0 — Founder Preparation

- [ ] Founder confirms the intended Server.ir account/service and obtains official support confirmation for SSH without sharing credentials.
- [ ] Founder approves the named operator, key custodian, reviewers, setup window, target environment, and expiration/review date.
- [ ] Founder approves project-limited access and rejects root/shared access.
- [ ] Founder confirms a current complete backup and independently verified restore record.
- [ ] Founder approves the exact stop conditions and emergency support route.

## Phase 1 — MacBook and Key Preparation

- [ ] Confirm the approved MacBook identity, operating-system security updates, disk encryption, screen lock, malware posture, backup, and authorized user.
- [ ] Inventory existing SSH identities without displaying private material.
- [ ] Approve a dedicated Damavand key name, algorithm/strength supported by the provider, passphrase custody, owner, expiry/review, rotation, revocation, and loss response.
- [ ] Generate the dedicated key locally only after approval; never generate or store it in the repository.
- [ ] Record only the public-key fingerprint and protected evidence location.
- [ ] Verify private-key file permissions and backup/recovery policy without copying the key into project files.

## Phase 2 — Add Public Key to Hosting

- [ ] Confirm the authentic cPanel/hosting control-plane address through an approved channel.
- [ ] Confirm MFA and named-account access where supported.
- [ ] Add only the public key to the intended project-limited hosting identity.
- [ ] Verify the public fingerprint matches the approved local fingerprint.
- [ ] Confirm root, unrelated accounts, unrelated paths, and shared credentials are not granted.
- [ ] Record who authorized and added the key, when, where, scope, expiry/review, and revocation method.

## Phase 3 — Test Connection

- [ ] Obtain hostname, port, username, provider host-key fingerprints, and allowed source/network policy through a secure approved channel.
- [ ] Verify the server host key out-of-band before accepting it.
- [ ] Perform the first login only in the authorized window and record success/failure without secrets.
- [ ] Confirm the session identity is non-root and matches the approved user.
- [ ] Confirm disconnection, failed-login behavior, logs, rate limits, timeout, and revocation where observable.
- [ ] Stop immediately on unexpected host key, privilege, directory, banner, or account scope.

## Phase 4 — Identify Hosting Path

- [ ] Record the home directory and exact Damavand document root/project path without exposing unrelated customer/account data.
- [ ] Confirm domain/subdomain mapping to that path through hosting evidence.
- [ ] Verify access cannot modify unrelated sites/directories where provider controls support restriction.
- [ ] Confirm WordPress is absent or identify its exact state before any later installation task.
- [ ] Record symlink, mount, ownership, group, ACL, quota, and deployment boundary evidence.

## Phase 5 — Check PHP CLI

- [ ] Confirm whether PHP CLI exists.
- [ ] Record exact CLI version, binary path, configuration-file paths, SAPI, extensions, limits, timezone, and owner without changing them.
- [ ] Compare CLI PHP with the future web runtime; record differences rather than assuming equivalence.
- [ ] Confirm no command changes PHP configuration or hosting state.

## Phase 6 — Check Database Access Method

- [ ] Identify the approved database access method, network boundary, client availability, and least-privilege identity process.
- [ ] Do not display, store, test in command history, or record database credentials in repository evidence.
- [ ] Confirm backup/export and restore methods without executing a production mutation.
- [ ] Record whether secure connection, host restrictions, logs, and revocation are available.
- [ ] Defer any database connection or query to a separately authorized validation task.

## Phase 7 — Check WP-CLI

- [ ] Confirm whether WP-CLI exists and record exact version/path/source/owner without installing it.
- [ ] Confirm the intended project path and future WordPress state before any WP-CLI command.
- [ ] Verify WP-CLI compatibility and allowed command classes through future approved evidence.
- [ ] Do not install WP-CLI, run WordPress mutations, or infer availability during Sprint 01D.

## Phase 8 — Check Git

- [ ] Confirm whether Git exists and record exact version/path without installing or configuring it.
- [ ] Confirm repository ownership/safe-directory behavior, filesystem boundary, and available disk space.
- [ ] Do not clone, pull, push, initialize, add a remote, or store GitHub credentials during Sprint 01D.
- [ ] Record whether outbound GitHub access works only in a separately authorized connectivity test.

## Phase 9 — Check File Permissions

- [ ] Record effective SSH user/group and the future web/PHP user/group.
- [ ] Inspect project-path ownership, modes, ACLs, umask, symlinks, and writable locations read-only.
- [ ] Confirm uploads can be isolated from executable code and that Core/vendor files are protected from ad hoc editing.
- [ ] Confirm the user cannot modify unrelated hosting paths where supported.
- [ ] Do not change ownership or permissions in Sprint 01D.

## Phase 10 — Record Findings

- [ ] Record target identifier, evidence date, collector, reviewer, observed values, unavailable checks, risks, and limitations.
- [ ] Update Environment Report, Hosting Validation Checklist, access policy, risk register, Repository Health, and audit only through an authorized documentation task.
- [ ] Store no secrets or sensitive account data.
- [ ] Record key fingerprint only; never record private-key contents or passphrase.
- [ ] Record the final SSH setup `GO` or `NO-GO` with evidence and approval.

## Current Outcome

`NO-GO — HOSTING SSH CAPABILITY, IDENTITY, KEY, HOST FINGERPRINT, TARGET PATH, BACKUP/RESTORE, AND APPROVAL ARE UNVERIFIED`

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 01D Founder/Build Engineer SSH setup and validation checklist; no key or connection created. |

## Navigation

- [Remote Access Architecture](../../docs/45_REMOTE_ACCESS_ARCHITECTURE.md)
- [Deployment Access Policy](DEPLOYMENT_ACCESS_POLICY.md)
- [Iran Execution Risk Register](IRAN_EXECUTION_RISK_REGISTER.md)
- [Rollback Plan](ROLLBACK_PLAN.md)
- [Sprint 01D Audit](../../docs/AUDIT_REPORT_SPRINT01D.md)
