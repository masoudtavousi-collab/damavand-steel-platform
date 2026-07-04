# Iran Execution Risk Register

## Document Control

- **Document ID:** `repository/config/IRAN_EXECUTION_RISK_REGISTER.md`
- **Status:** Review
- **Authority:** Evidence and Risk Register
- **Owner:** Founder
- **Reviewer:** Build Engineer, Security Reviewer, and Operations Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** Before remote setup/deployment and on connectivity, provider, vendor, license, DNS, TLS, email, toolchain, or operational change
- **Lifecycle:** Review
- **Source of Truth:** Sprint 01D planning constraints, [Remote Access Architecture](../../docs/45_REMOTE_ACCESS_ARCHITECTURE.md), and future dated measurements/provider evidence
- **Dependencies:** [Deployment Access Policy](DEPLOYMENT_ACCESS_POLICY.md), [Hosting Validation Checklist](HOSTING_VALIDATION_CHECKLIST.md), and [Rollback Plan](ROLLBACK_PLAN.md)
- **Related Documents:** [SSH Access Checklist](SSH_ACCESS_CHECKLIST.md), [Plugin Installation Sequence](PLUGIN_INSTALLATION_SEQUENCE.md), [Post-Install Validation](POST_INSTALL_VALIDATION.md), and [Sprint 01D Audit](../../docs/AUDIT_REPORT_SPRINT01D.md)
- **Traceability:** CP-001 through CP-010, S01B-001 through S01B-005, S01C-001 through S01C-008, RA-001 through RA-012, and IR-001 through IR-012
- **AI Compatibility:** AI-readable risk register; planning risks are not represented as measured incidents or universal availability facts
- **Approval:** Pending Founder, technical, security, operations, hosting, legal/compliance, and vendor review

## Purpose

Track execution risks relevant to an Iran-based operator and intended hosting workflow, with impact, mitigation, fallback, evidence, and stop boundaries. No network path was tested in Sprint 01D.

## Interpretation Rules

- Likelihood is `Unknown` until measured on the approved operator network and target hosting path.
- Impact describes a credible consequence, not a current incident.
- A fallback must preserve legality, licensing, provenance, integrity, security, approval, backup, and rollback.
- Connectivity pressure does not justify credential exposure, unverified packages, root access, or unreviewed production change.
- Update each risk with observation date, environment/path, evidence, owner, result, and next review after an authorized test.

## Risk Register

| ID | Risk | Likelihood | Potential impact | Mitigation | Fallback | Evidence/status |
| --- | --- | --- | --- | --- | --- | --- |
| IR-001 | GitHub blocked, slow, or unstable | Unknown | Clone/fetch/push, review, package retrieval, or deployment interruption; local/remote divergence | Maintain clean local Git, small pushes, immutable commit IDs, independent repository backup, protected recovery accounts, and preflight connectivity check | Defer change; use an approved independent mirror or exact reviewed offline artifact only after policy/approval | Planning risk; no authorized path test |
| IR-002 | WordPress.org blocked or unreachable from operator/host | Unknown | Core/plugin/theme metadata or package acquisition/update failure | Pin exact approved versions, verify official provenance/checksum, retain approved package manifest outside Git, and test reachability before window | Controlled manual upload of a verified approved package; never select an unknown mirror | Planning risk; no host test |
| IR-003 | Plugin license activation blocked | Unknown | Commercial capability cannot activate/update/support | Confirm vendor terms, endpoint requirements, account custody, domain/environment rules, and connectivity before installation | Defer activation/install; contact vendor through approved support; use no crack, bypass, or substitute | Planning risk; licenses/packages unavailable |
| IR-004 | VPN or alternate-network instability | Unknown | Interrupted authentication/download, inconsistent source IP, lockout, or incomplete transfer | Do not make recovery depend on a VPN; preflight approved lawful network path and avoid mutations during instability | Stop safely; resume only from verified checkpoint through approved network/provider support | Planning risk; no VPN method approved |
| IR-005 | cPanel session timeout or unavailability | Unknown | Partial upload/edit, lost session, unclear server state | Avoid routine File Manager changes; use exact artifact, checksums, short bounded operations, and backup | Use approved SSH path if validated; otherwise stop and engage hosting support | Planning risk; cPanel unverified |
| IR-006 | SSH timeout or route instability | Unknown | Interrupted transfer/command and uncertain deployment state | Test reachability read-only, use resilient verified transfer tooling later, checksum files, keep changes atomic where possible, and define interruption stop | Restore prior checkpoint or defer; emergency cPanel only under policy | Planning risk; SSH unverified |
| IR-007 | Large upload failure | Unknown | Corrupt/incomplete plugin, theme, media, backup, or release artifact | Minimize artifact, record size/checksum, verify server limits/free space, use resumable approved method where available | Split only when vendor/artifact format permits; use hosting-side approved import/support; never accept unchecked partial file | Planning risk; limits unverified |
| IR-008 | DNS propagation delay or inconsistent resolver state | Unknown | Users reach old/wrong target, TLS mismatch, email or validation inconsistency | Approve DNS plan, lower TTL in advance when appropriate, inventory records, validate multiple resolvers, and keep rollback values | Revert records within approved window; keep old target available until cutover acceptance | Planning risk; DNS strategy unresolved |
| IR-009 | SSL issuance or renewal issue | Unknown | HTTPS failure, browser warnings, Admin/login exposure, API/license failure | Confirm certificate scope, issuer, challenge path, renewal owner, alerts, DNS/time dependencies, and expiry before launch | Restore prior certificate/configuration or use provider-supported recovery; no insecure production bypass | Planning risk; TLS unverified |
| IR-010 | Email delivery issue | Unknown | Inquiry, security, Admin, or recovery notifications fail or arrive late | Approve provider/sender/DNS authentication, safe test, queues/retries, bounce monitoring, and alternative alert route | Use approved manual Sales/operations escalation without exposing customer data; hold launch if critical mail is required | Planning risk; email unverified |
| IR-011 | Payment or license access issue | Unknown | Purchase, renewal, download, update, or support entitlement unavailable | Confirm lawful procurement, billing owner, renewal dates, vendor access, invoice/license custody, and export before dependency approval | Defer dependent component; use only an independently approved alternative decision, never an invented replacement | Planning risk; procurement unresolved |
| IR-012 | Founder execution complexity | Unknown | Operational error, unsafe command, delayed launch, lockout, or dependence on one expert | Simple checklists, named Build Engineer, scripted later runbooks, approval gates, dry-runs, training, support route, and readable evidence | Stop; escalate to approved technical/hosting support; use manual recovery checklist without Codex dependency | Planning risk; operating model pending approval |

## Cross-Risk Controls

- Preflight connectivity from both operator-to-service and hosting-to-service paths before a change window.
- Keep verified exact artifacts and manifests under approved secure custody outside Git when licensing permits.
- Maintain independent repository and complete application/data backups with tested restoration.
- Use small, atomic, observable, reversible changes and stop after any interrupted or partial step.
- Keep emergency contacts and recovery instructions available offline without credentials.
- Separate access setup, environment validation, installation, deployment, and production release approvals.

## Escalation and Review

- Security or secret exposure: stop, revoke/rotate, preserve safe evidence, and invoke incident review.
- Partial server mutation: isolate, compare to the accepted checkpoint, and roll back before retry.
- Vendor/package uncertainty: block installation until provenance, integrity, license, and compatibility are approved.
- Connectivity uncertainty before a high-risk task: issue `NO-GO` and reschedule.
- Founder complexity or uncertainty: stop and engage the approved Build Engineer/hosting support route.

## Current Risk Decision

`NO-GO FOR ACTUAL SSH SETUP OR REMOTE DEPLOYMENT — ALL PATH-SPECIFIC LIKELIHOODS AND HOSTING CAPABILITIES ARE UNVERIFIED`

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 01D Iran execution risk register; all entries are planning risks with unknown likelihood. |

## Navigation

- [Remote Access Architecture](../../docs/45_REMOTE_ACCESS_ARCHITECTURE.md)
- [SSH Access Checklist](SSH_ACCESS_CHECKLIST.md)
- [Deployment Access Policy](DEPLOYMENT_ACCESS_POLICY.md)
- [Hosting Validation Checklist](HOSTING_VALIDATION_CHECKLIST.md)
- [Sprint 01D Audit](../../docs/AUDIT_REPORT_SPRINT01D.md)
