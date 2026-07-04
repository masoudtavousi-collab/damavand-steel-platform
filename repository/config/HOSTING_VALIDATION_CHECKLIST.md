# Hosting Validation Checklist

## Document Control

- **Document ID:** `repository/config/HOSTING_VALIDATION_CHECKLIST.md`
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Build Engineer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** Before WordPress installation and on hosting, runtime, network, database, security, backup, or access change
- **Lifecycle:** Review
- **Source of Truth:** [Sprint 01B Environment Report](ENVIRONMENT_REPORT.md), future read-only hosting evidence, and approved environment decisions
- **Dependencies:** [Build Checklist](../BUILD_CHECKLIST.md), [Pre-Implementation Checklist](../PRE_IMPLEMENTATION_CHECKLIST.md), and [Implementation Readiness](../../docs/IMPLEMENTATION_READINESS.md)
- **Related Documents:** [WordPress Installation Checklist](WORDPRESS_INSTALLATION_CHECKLIST.md), [Post-Install Validation](POST_INSTALL_VALIDATION.md), [Rollback Plan](ROLLBACK_PLAN.md), and [Sprint 01C Audit](../../docs/AUDIT_REPORT_SPRINT01C.md)
- **Traceability:** CP-001 through CP-010, S01A-008 through S01A-010, S01B-001 through S01B-005, and S01C-001 through S01C-008
- **AI Compatibility:** AI-readable hosting gate; unchecked or unavailable evidence must not be inferred as passing
- **Approval:** Pending Founder/technical/operations/security review; all validation gates remain unchecked

## Purpose

Define the evidence required to validate a real production-ready hosting environment before a clean WordPress installation.

## Checklist Rules

- Every `[ ]` item is unresolved until an evidence link, observed value, owner, review date, and reviewer are recorded.
- Repository templates, local workstation values, screenshots without source context, vendor marketing claims, and verbal assurances are not sufficient evidence.
- `N/A` requires written rationale and Founder/technical approval.
- A mandatory unchecked item makes the installation decision `NO-GO`.

## Sprint 01B Review Classification

### Verified Items

- Baseline `HEAD`, `baseline-v1.0.0`, and `repo-v1.0.0` resolve the same commit.
- The observed machine is a local macOS workstation, not a verified hosting environment.
- Apache 2.4.66 exists as an inactive local binary; ports 80, 443, 8080, and 3306 were closed.
- PHP, MariaDB/MySQL, WP-CLI, Docker/Podman, Composer, Node/npm, WordPress, WooCommerce, Blocksy, and Elementor were absent.
- Local `wp-content` and `uploads` paths were mode `0755` and writable by the local owner.
- No installation, package download, content, plugin/theme activation, configuration, or baseline mutation occurred.

### Unknown Items

- Hosting provider, region, topology, service tier, ownership, support, and exit process.
- Exact approved software versions, package sources, licenses, compatibility, and maintenance windows.
- Production-ready resource limits, availability targets, monitoring, incident response, and recovery objectives.
- Web-service identity, effective permissions, runtime filesystem method, and deployment ownership.

### Runtime-Dependent Items

- Active PHP version/SAPI/extensions/limits/timezone/error and session behavior.
- Active MariaDB version, charset/collation, SQL modes, timezone, users, privileges, and connection security.
- WordPress version, filesystem method, permalinks, uploads, cron, mail, memory limits, and health.
- WooCommerce, Blocksy/Blocksy Pro, and Elementor Pro package/activation/license/compatibility state.

### Hosting-Dependent Items

- DNS, TLS/certificates, HTTP behavior, filesystem owner, cron, email delivery, backups, restore, WAF/firewall, logs, monitoring, resource limits, and production access.

### Founder Actions Required

- Approve the hosting target, environment purpose, provider/region, owners, access, costs, support, data custody, and exit terms.
- Approve exact PHP, MariaDB, WordPress, WooCommerce, Blocksy/Blocksy Pro, Elementor Pro, and required dependency versions.
- Approve commercial package acquisition/license custody and every required plugin dependency.
- Assign technical, security/privacy, operations, backup/recovery, release, and Founder Admin reviewers.
- Approve security, privacy, backup/restore, rollback, testing, and go/no-go evidence.

## Hosting

- [ ] Provider, region, service/product, account owner, billing owner, technical owner, and support route are approved.
- [ ] Environment purpose and separation from development, staging, and production are explicit.
- [ ] Architecture/topology, network boundary, resource allocation, scaling, availability, maintenance, and end-of-life are documented.
- [ ] Service terms, data location, data ownership, export, deletion, and vendor-exit requirements are approved.
- [ ] Access uses named least-privilege accounts with approved authentication, review, and revocation.
- [ ] Host identity and evidence collection method are recorded without exposing credentials.

## PHP

- [ ] Exact PHP version and SAPI are observed on the real target and approved.
- [ ] Compatibility is evidenced for exact WordPress and every approved component version.
- [ ] Required extensions are inventoried with versions/status; unnecessary extensions are reviewed.
- [ ] Active configuration file paths and effective values are recorded.
- [ ] Memory, upload, POST, execution, input, session, error, logging, timezone, and OPcache behavior are approved.
- [ ] Upgrade, security patch, support lifecycle, rollback, and failure monitoring are documented.

## MariaDB

- [ ] Exact MariaDB server/client version is observed and approved.
- [ ] Compatibility with exact WordPress/WooCommerce/PHP versions is evidenced.
- [ ] Character set, collation, SQL modes, timezone, storage engine, packet/connection limits, and resource allocation are approved.
- [ ] Administrative and application identities are separated and least-privilege.
- [ ] Network encryption/access, logs, monitoring, maintenance, upgrades, backup/restore, and rollback are approved.
- [ ] No direct uncontrolled production mutation path is permitted.

## SSL

- [ ] Approved domain names match the certificate scope.
- [ ] Certificate authority, issuance, private-key custody, renewal, expiry monitoring, and emergency replacement are approved.
- [ ] TLS protocols/ciphers and HTTP-to-HTTPS behavior meet the approved security policy.
- [ ] Certificate chain, hostname, expiry, redirect, mixed-content, and failure behavior are validated from an independent client.
- [ ] Private keys and certificate secrets are absent from Git and evidence documents.

## Disk

- [ ] Filesystem type, mount, quota, capacity, available space, inode/file limits, and growth monitoring are recorded.
- [ ] WordPress Core, `wp-content`, uploads, logs, cache, backups, and temporary storage boundaries are defined.
- [ ] Storage persistence, snapshot behavior, encryption, permissions, and failure handling are approved.
- [ ] Low-space alert and recovery thresholds are documented and tested where safe.
- [ ] Backup storage is outside the live application failure domain.

## Memory

- [ ] Host/container memory and swap limits are observed.
- [ ] PHP process limits, WordPress memory constants, database memory, web-server workers, and cache allocations are compatible.
- [ ] Normal and peak workload assumptions are documented without claiming unmeasured performance.
- [ ] Memory exhaustion alerts, failure behavior, and rollback/scale response are approved.

## Cron

- [ ] System cron/scheduler capability, owner, timezone, locking, overlap behavior, logging, and failure alerts are verified.
- [ ] WordPress cron policy and relationship to system scheduling are approved.
- [ ] Jobs never expose secrets or protected Inquiry/Customer data in command lines/logs.
- [ ] Missed/duplicate job behavior, recovery, maintenance, and rollback are documented.
- [ ] No cron task is created before installation authorization.

## Email

- [ ] Approved outbound provider, sender domains/addresses, authentication, credentials custody, and ownership are recorded.
- [ ] DNS authentication requirements, TLS, rate limits, retry, bounce/complaint handling, and delivery monitoring are approved.
- [ ] Development/staging recipient suppression and safe testing are defined.
- [ ] Inquiry/security/administrative notification privacy and minimum-data rules are approved.
- [ ] Native WordPress mail is not treated as reliable delivery authority without evidence.

## File Permissions

- [ ] Effective web/PHP process user/group and deployment identity are observed.
- [ ] WordPress Core, configuration, plugins, themes, uploads, cache, logs, and temporary directories have approved ownership/modes.
- [ ] Uploads are writable only as required and cannot execute scripts.
- [ ] Core/vendor files are immutable to routine Admin workflows as approved.
- [ ] Symlink, ACL, extended-attribute, umask, and shared-hosting behavior are reviewed.
- [ ] Permission validation includes allowed and denied operations plus rollback.

## DNS

- [ ] Domain ownership, registrar/DNS provider, account owner, MFA/access, and recovery are approved.
- [ ] A/AAAA/CNAME and required mail/security records are inventoried and reviewed.
- [ ] TTL, change window, propagation check, split-horizon, IPv6, CDN/proxy, and rollback are documented.
- [ ] Development/staging and production names cannot be confused.
- [ ] DNS changes occur only after target, TLS, monitoring, and rollback readiness.

## Database

- [ ] Database host/name/port/source are approved without exposing credentials.
- [ ] Application user permissions are least-privilege and tested.
- [ ] Connection encryption, timeout, pooling/persistence, failure, retry, and monitoring are approved.
- [ ] Initial empty database state is verified before installation.
- [ ] Backup/restore checkpoint exists before any installer writes.
- [ ] Charset/collation/timezone/table-prefix choices are approved and runtime-verified.

## Backups

- [ ] Database, uploads, configuration, and required application state are included according to approved scope.
- [ ] Storage, encryption, custody, access, frequency, retention, immutability, geographic/provider separation, and deletion are approved.
- [ ] Backup success, integrity, age, completeness, and restore tests are monitored.
- [ ] Pre-install, post-install, pre-component, post-component, and pre-change checkpoints are defined.
- [ ] Restore is tested in isolation and does not overwrite evidence or production unexpectedly.
- [ ] Backup payloads remain outside Git and repository evidence contains no secrets.

## Security

- [ ] Threat model, asset/data classification, attack surface, owners, and risk acceptance are approved.
- [ ] Network firewall/WAF, SSH/control-panel access, MFA, least privilege, secrets, dependency verification, malware/integrity monitoring, and vulnerability response are defined.
- [ ] TLS, headers, filesystem, uploads, database, logs, backups, email, cron, Admin, API, and XML-RPC policies are approved.
- [ ] Security logging avoids secrets and protected personal data while supporting incident investigation.
- [ ] Patch, emergency change, incident, isolation, recovery, evidence retention, and notification processes are tested.
- [ ] No security plugin is installed unless selected through the approved Plugin First gate.

## Gate Outcome

`NO-GO — REAL HOSTING EVIDENCE IS UNAVAILABLE AND ALL CHECKS REMAIN OPEN`

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 01C hosting validation checklist based on Sprint 01B evidence gaps. |

## Navigation

- [Environment Report](ENVIRONMENT_REPORT.md)
- [WordPress Installation Checklist](WORDPRESS_INSTALLATION_CHECKLIST.md)
- [Rollback Plan](ROLLBACK_PLAN.md)
- [Sprint 01C Audit](../../docs/AUDIT_REPORT_SPRINT01C.md)
