# Site Health Remediation Plan

## Document Control

- **Document ID:** `docs/SITE_HEALTH_REMEDIATION_PLAN.md`
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Infrastructure Reviewer, WordPress Technical Reviewer, Security Reviewer, SEO Reviewer, Operations Reviewer, and Quality Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On evidence, priority, owner, status, dependency, remediation approval, validation, or production-readiness change
- **Lifecycle:** Review
- **Source of Truth:** [Infrastructure Audit](INFRASTRUCTURE_AUDIT.md), [REST API Diagnostic](REST_API_DIAGNOSTIC.md), [WordPress Connectivity Audit](WORDPRESS_CONNECTIVITY_AUDIT.md), and explicit future Founder remediation decisions
- **Dependencies:** [Infrastructure Audit](INFRASTRUCTURE_AUDIT.md), [REST API Diagnostic](REST_API_DIAGNOSTIC.md), [WordPress Connectivity Audit](WORDPRESS_CONNECTIVITY_AUDIT.md), and [Platform Governance](../repository/platform/PLATFORM_GOVERNANCE.md)
- **Related Documents:** [Sprint 02C Audit](AUDIT_REPORT_SPRINT02C.md), [Hosting Validation Checklist](../repository/config/HOSTING_VALIDATION_CHECKLIST.md), [Rollback Plan](../repository/config/ROLLBACK_PLAN.md), and [Sprint 04A Audit](AUDIT_REPORT_SPRINT04A.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, PM-007, PG-005 through PG-012, PLC-005 through PLC-011, Sprint 02C, and Sprint 04A
- **AI Compatibility:** AI-readable prioritized plan; no item authorizes execution or autonomous status change
- **Approval:** Pending Founder/infrastructure/security/operations review; all mutation steps are blocked until separately authorized

## Purpose

Prioritize evidence collection and future remediation gates for current Site Health findings without selecting or executing a fix.

## Plan Rules

- Investigation and remediation are separate phases.
- `Pending Evidence` is not failure/absence and cannot be replaced with a guess.
- The first action is read-only evidence collection through existing approved methods.
- No production experiment, plugin isolation, setting change, PHP change, DNS/TLS/firewall change, or hosting connection is authorized.
- Any future mutation requires backup/restore proof, staging where feasible, one-variable change, acceptance tests, rollback, and Founder approval.
- Coming Soon remains intentionally enabled until Founder launch approval.
- LiteSpeed Cache remains prohibited; object-cache recommendations require separate capability review.

## Status Vocabulary

| Status | Meaning |
| --- | --- |
| `Verified Issue` | Symptom is evidenced; root cause may remain unknown |
| `Pending Evidence` | Required evidence not supplied |
| `Blocked` | Cannot proceed due to missing dependency/approval |
| `Expected` | Intentional current state; no remediation needed now |
| `Not Authorized` | Would change runtime/infrastructure and requires a separate task |
| `Resolved` | Requires dated post-change evidence; no item is Resolved in Sprint 04A |

## Critical Priority

| ID | Work item | Expected impact | Difficulty | Dependencies | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SH-C01 | Capture full REST cURL 28 details and same-time Site Health context | Locates failure phase and prevents blind remediation | Low/Medium | Existing WordPress Admin evidence path; no changes | WordPress Technical Reviewer; assignee `TBD` | Pending Evidence |
| SH-C02 | Capture full `api.wordpress.org` failure details at same timestamp | Determines DNS/TCP/TLS/HTTP/policy failure class | Low/Medium | Existing Admin/support evidence path | WordPress Technical Reviewer; assignee `TBD` | Pending Evidence |
| SH-C03 | Server.ir read-only DNS/IPv4/IPv6/egress/loopback/firewall evidence | Tests common network-path root cause | Medium/Provider-dependent | Exact timestamp, support channel | Hosting Provider + Infrastructure Reviewer | Pending Evidence |
| SH-C04 | Server.ir read-only LiteSpeed/ModSecurity/CloudLinux/log correlation | Tests server/WAF/resource root causes | Medium/Provider-dependent | Exact request/timestamp; log retention | Hosting Provider + Security Reviewer | Pending Evidence |
| SH-C05 | Refresh TLS chain/SNI/hostname/redirect/Home-Site URL evidence | Resolves prior `Not Secure` conflict and self-HTTPS risk | Medium | Existing public/Admin/support evidence | Hosting Provider + Infrastructure/SEO Reviewers | Pending Evidence |
| SH-C06 | Establish backup scope/success and isolated restore evidence before any future change | Prevents unrecoverable remediation | High | Backup destination/access/retention and separate authorization | Operations Owner; assignee `TBD` | Blocked/Pending Evidence |

## High Priority

| ID | Work item | Expected impact | Difficulty | Dependencies | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SH-H01 | Obtain PHP SAPI/extensions/cURL/SSL/CA/effective timeout evidence | Tests transport/runtime compatibility causes | Medium | Provider/cPanel read-only evidence | Hosting Provider + WordPress Reviewer | Pending Evidence |
| SH-H02 | Review redacted WordPress HTTP API external-block/proxy/filter policy | Tests application-level request policy | Medium | Existing approved read-only config evidence; secrets excluded | WordPress/Security Reviewers | Pending Evidence |
| SH-H03 | Inventory MU-plugins, drop-ins, object-cache state, relevant settings/logs/change timeline | Identifies hidden request filters and timing changes | Medium | Existing read-only Admin/File Manager evidence if already approved | WordPress Reviewer | Pending Evidence |
| SH-H04 | Correlate security/network optimizer plugins without deactivation | Identifies candidate filter ownership/overlap | Medium | Settings/logs evidence for Kadence Security and Iran optimizer | Security/WordPress Reviewers | Pending Evidence |
| SH-H05 | Identify failed cron event and background-update diagnostic details | Separates shared network symptom from event-specific failure | Low/Medium | Expanded Site Health and scheduled-action evidence | WordPress/Operations Reviewers | Pending Evidence |
| SH-H06 | Confirm current runtime/component compatibility support matrix | Prevents unsafe remediation/update plan | High | Provider-supported PHP versions and vendor evidence | Architecture/WordPress Reviewers | Pending Evidence |

## Medium Priority

| ID | Work item | Expected impact | Difficulty | Dependencies | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SH-M01 | Design approved SMTP sender/provider/DNS/credential custody and delivery tests | Enables trustworthy inquiry/admin email later | Medium | Founder, email domain/DNS, secrets process, separate change approval | Founder + Email/Operations Owner | Verified Issue; Not Authorized |
| SH-M02 | Reconcile Rank Math old/new Site URL and reconnection requirements | Restores SEO service/account alignment | Medium | Stable canonical URL/TLS, account owner, privacy/security review | SEO Owner; assignee `TBD` | Blocked by SH-C05 |
| SH-M03 | Review plugin ownership/overlap/necessity against governance | Reduces future conflict/maintenance risk | High | Fresh inventory, settings, data ownership, backup, Founder decisions | Architecture/Plugin Owners | Pending Evidence; no cleanup |
| SH-M04 | Review persistent object-cache need/capability separately | Determines performance need without prohibited plugin assumption | Medium/High | Root cause closed, hosting capability/performance evidence | Performance/Infrastructure Reviewers | Deferred |
| SH-M05 | Validate Site Health after any future authorized root-cause remediation | Confirms REST/WordPress.org/cron/background-update outcomes | Medium | Approved change, baseline, staging/recovery | Quality/WordPress Reviewers | Blocked; future task |

## Low Priority / Expected State

| ID | Work item | Expected impact | Difficulty | Dependencies | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SH-L01 | Keep Coming Soon enabled until Founder launch gate | Prevents premature public/indexable launch | Low | Founder launch decision | Founder/SEO Owner | Expected; no change |
| SH-L02 | Review inactive-theme recommendation only after fresh inventory/dependency/recovery evidence | Reduces future maintenance surface without deleting required theme | Medium | Theme inventory, active/parent dependency, backup, separate approval | WordPress/Operations Reviewers | Pending Evidence; no deletion |
| SH-L03 | Reassess indexing after infrastructure/SEO launch readiness | Prevents accidental indexing or prolonged suppression | Medium | TLS, URL, Coming Soon, canonical, sitemap/schema/content approval | Founder + SEO Owner | Blocked by launch gates |

## Recommended Investigation Sequence

### Phase 0 — Change Freeze

- Preserve current files/settings/plugins/database/PHP/DNS/TLS/.htaccess/wp-config state.
- Record timestamps/timezone and current Site Health screenshots/details.
- Do not run setup wizards, reconnect, update, install, delete, deactivate, or change anything.

### Phase 1 — Application Evidence

- Complete SH-C01, SH-C02, SH-H02, SH-H03, and SH-H05 read-only.
- Produce one timeline joining REST, WordPress.org, cron, update, SMTP, Rank Math, and TLS observations.

### Phase 2 — Provider Evidence

- Complete SH-C03, SH-C04, SH-C05, and SH-H01 through the existing Server.ir support/cPanel path.
- Require explicit provider observations; do not accept an undocumented configuration change as diagnosis.

### Phase 3 — Root-Cause Decision

- Compare evidence against DNS, IPv6, egress, loopback, TLS, WAF, LiteSpeed, CloudLinux, cURL/CA, WordPress policy, plugin, and resource hypotheses.
- Select the narrowest evidence-supported cause.
- If evidence remains insufficient, design controlled staging isolation after SH-C06.

### Phase 4 — Separate Remediation Authorization

- Define exact one-variable change, owner, environment, backup/restore, expected result, negative tests, rollback, monitoring, and approval.
- Do not combine infrastructure, plugin, PHP, SEO, and SMTP changes into one release.

### Phase 5 — Validation and Closure

- Re-run REST, WordPress.org, cron/background updates, TLS, Site Health, plugin workflows, inquiry/no-price, security, RTL/mobile/accessibility, performance, and rollback checks as applicable.
- Mark Resolved only with dated before/after evidence.

## Acceptance Criteria Before WooCommerce Implementation

- REST API Site Health test passes consistently or an approved scoped exception exists with impact evidence.
- Official WordPress.org connectivity is healthy or an approved provider-supported alternative architecture is explicitly decided; no unverified mirrors.
- TLS/hostname/Home-Site URL state is valid and stable.
- Cron/background update health and ownership are understood.
- SMTP design does not need to be live for catalog design, but production inquiry/email launch requires successful delivery/failure tests.
- Backup/restore and rollback are proven.
- Runtime/component compatibility is approved.
- Plugin/MU/drop-in ownership and conflicts are understood.
- Critical/high findings have evidence-based disposition and Founder approval.

## Rejection / Stop Conditions

- Any request to disable security/WAF/plugins on production without approved staging/recovery.
- Any change to DNS, TLS, firewall, PHP, `.htaccess`, `wp-config.php`, database, WordPress settings, or plugins during this audit.
- Root cause described as fact without diagnostic evidence.
- Use of unknown/unverified package mirrors or replacement plugins.
- Missing backup/restore before mutation.
- Partial change, price exposure, inquiry failure, security regression, data loss, lockout, or unknown rollback.

## Current Plan Decision

**GO** for Phase 0–2 read-only evidence collection through existing approved methods.

**NO-GO** for Phase 4 remediation, WooCommerce implementation, production acceptance, or launch.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial Sprint 04A prioritized Site Health plan; no remediation executed. |

## Navigation

- [Infrastructure Audit](INFRASTRUCTURE_AUDIT.md)
- [REST API Diagnostic](REST_API_DIAGNOSTIC.md)
- [WordPress Connectivity Audit](WORDPRESS_CONNECTIVITY_AUDIT.md)
- [Sprint 04A Audit](AUDIT_REPORT_SPRINT04A.md)
