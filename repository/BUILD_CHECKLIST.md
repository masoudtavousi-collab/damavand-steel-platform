# Repository Build Checklist

## Document Control

- **Document ID:** `repository/BUILD_CHECKLIST.md`
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** Build Engineer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** Before build authorization and on environment, hosting, platform, dependency, ownership, or readiness change
- **Lifecycle:** Review
- **Source of Truth:** [Implementation Rules](IMPLEMENTATION_RULES.md), [Implementation Readiness](../docs/IMPLEMENTATION_READINESS.md), and future approved platform/environment decisions
- **Dependencies:** [Implementation Rules](IMPLEMENTATION_RULES.md), [Implementation Readiness](../docs/IMPLEMENTATION_READINESS.md), [WordPress Solution Blueprint](../docs/35_WORDPRESS_BLUEPRINT.md), and [Engineering Guidelines](../docs/ENGINEERING_GUIDELINES.md)
- **Related Documents:** [Pre-Implementation Checklist](PRE_IMPLEMENTATION_CHECKLIST.md), [Sprint Roadmap](../docs/SPRINT_ROADMAP.md), [Repository Health](../docs/REPOSITORY_HEALTH.md), and [Sprint 01A Audit](../docs/AUDIT_REPORT_SPRINT01A.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, WP-FC-001 through WP-FC-005, and S01A-008 through S01A-010
- **AI Compatibility:** AI-readable readiness checklist; unchecked items cannot be inferred as complete
- **Approval:** Pending Founder review; every item is unchecked and no build is authorized

## Purpose

Provide the evidence checklist that must be completed before a future repository build or WordPress foundation activity.

## Checklist Rules

- `[ ]` means not evidenced, not approved, or not applicable without rationale.
- Check an item only when its evidence link, owner, date, and reviewer are recorded.
- `N/A` requires written rationale and approval.
- A mandatory unchecked item blocks the build.

## Environment Readiness

- [ ] Approved environment inventory and purpose exist for every in-scope environment.
- [ ] Environment ownership, access, isolation, lifecycle, refresh, and destruction rules are approved.
- [ ] Non-secret configuration sources and secret-management boundaries are documented.
- [ ] Development/staging use no unapproved production personal data.
- [ ] Timezone, locale, Persian RTL, URLs, mail, cache, cron, and debug policies are approved per environment.

## Hosting Readiness

- [ ] Hosting provider and region are approved.
- [ ] Supported WordPress/PHP/MariaDB requirements and resource limits are evidenced.
- [ ] Storage, file permissions, process ownership, network access, logging, monitoring, backup, and recovery responsibilities are approved.
- [ ] Service availability, support, maintenance, incident, and exit expectations are documented.

## DNS Readiness

- [ ] Approved domains/subdomains, ownership, registrar/DNS access, and responsible role are recorded.
- [ ] Environment-specific DNS plan, TTL/change window, validation, rollback, and propagation checks are approved.
- [ ] Mail-related DNS and sender authentication ownership are defined where applicable.
- [ ] No DNS change is scheduled before environment and rollback readiness.

## SSL Readiness

- [ ] Certificate authority/provisioning method, domains, renewal, custody, and monitoring are approved.
- [ ] TLS policy and HTTP-to-HTTPS behavior are approved and testable.
- [ ] Certificate failure and renewal recovery paths are documented.
- [ ] No private key or certificate secret is stored in Git.

## Database Readiness

- [ ] Database purpose, owner, environment isolation, access, network boundary, and least privilege are approved.
- [ ] Naming, charset/collation, timezone, table-prefix, capacity, connection, backup, restore, and retention rules are approved.
- [ ] Migration, import/export, sanitization, rollback, and failure procedures are approved.
- [ ] No real credential or production data is committed to the repository.

## PHP Readiness

- [ ] Exact supported PHP version is approved against WordPress and every approved dependency.
- [ ] Required extensions, limits, timezone, error display/logging, file upload, execution, and security settings are approved.
- [ ] Development/staging/production differences are documented without secrets.
- [ ] Upgrade, compatibility, vulnerability, rollback, and support evidence exists.

## MariaDB Readiness

- [ ] Exact supported MariaDB version is approved against WordPress/WooCommerce requirements.
- [ ] Character set, collation, SQL modes, timezone, connection security, users/privileges, and resource policy are approved.
- [ ] Backup/restore, integrity, monitoring, upgrade, rollback, and support evidence exists.
- [ ] Database access does not permit uncontrolled direct production mutation.

## WordPress Readiness

- [ ] Applicable WordPress Architecture and Solution Blueprint decisions are Approved.
- [ ] Exact WordPress version, source verification, update policy, filesystem boundary, environment type, URLs, locale/timezone, cron, mail, media, and Admin policy are approved.
- [ ] WordPress Core, uploads, dependencies, secrets, and runtime files remain excluded from Git as required.
- [ ] Inquiry First, No Public Pricing, Mobile First, Persian RTL, and Admin manageability acceptance tests are defined.
- [ ] Installation, backup/restore, rollback, smoke test, and removal/rebuild procedures are approved.

## Plugin Readiness

- [ ] Every required capability has one approved owner and overlap analysis.
- [ ] Exact plugin package/version/license/source/support/security/export/uninstall/rollback evidence is approved.
- [ ] WordPress/WooCommerce/Blocksy/Elementor/PHP/MariaDB compatibility is evidenced.
- [ ] Gravity Forms and LiteSpeed Cache are absent from the approved set.
- [ ] No Phase 1 AI feature, connector, routing, generation, model access, or search capability is included.
- [ ] No plugin can expose public prices, cart, checkout, payments, protected data, or duplicate schema/template ownership.

## Theme Readiness

- [ ] Blocksy/Blocksy Pro exact supported versions, license handling, source, update, export, restore, and rollback are approved.
- [ ] Blocksy owns the global shell and Elementor owns only delegated content areas.
- [ ] No custom or child theme is included; FD-GOV-008 is resolved consistently with CP-007.
- [ ] Global design-token, Persian RTL, mobile, accessibility, WooCommerce catalog, and no-price test requirements are approved.
- [ ] No vendor/core file edit, copied template, executable hook snippet, or unsupported override is planned.

## Developer Readiness

- [ ] Named developer/build owner and reviewers are assigned.
- [ ] Repository, branch, commit, review, approval, secrets, dependency, testing, rollback, incident, and handoff rules are understood.
- [ ] Required local tools and versions are approved and reproducible without committing binaries/dependencies.
- [ ] Access is least-privilege, individual, time-bounded where appropriate, and revocable.
- [ ] The developer can demonstrate preservation of CP-001 through CP-010 and ADR-0001.

## Founder Readiness

- [ ] Founder has reviewed the Implementation Readiness blockers and assigned owners.
- [ ] Applicable architecture, Blueprint, environment, provider, version, security/privacy, and operations decisions are recorded.
- [ ] Sprint scope, deliverables, exclusions, acceptance evidence, budget/license implications, rollback, and support ownership are understood.
- [ ] Founder Admin manageability expectations and validation approach are approved.
- [ ] A separate exact implementation/build authorization is recorded.

## Gate Outcome

Current outcome: `BLOCKED — ALL ITEMS REQUIRE EVIDENCE`.

No item is checked by Sprint 01A. This checklist does not install, configure, validate, or approve any platform component.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 01A build-readiness checklist; all gates unchecked. |

## Navigation

- [Implementation Rules](IMPLEMENTATION_RULES.md)
- [Pre-Implementation Checklist](PRE_IMPLEMENTATION_CHECKLIST.md)
- [Implementation Readiness](../docs/IMPLEMENTATION_READINESS.md)
- [Sprint 01A Audit](../docs/AUDIT_REPORT_SPRINT01A.md)
