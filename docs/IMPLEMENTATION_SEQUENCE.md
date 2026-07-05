# Remediation Implementation Sequence

## Document Control

- **Document ID:** `docs/IMPLEMENTATION_SEQUENCE.md`
- **Status:** Review
- **Authority:** Planning Record
- **Owner:** Founder
- **Reviewer:** Enterprise WordPress Platform Architect, Security Reviewer, Operations Reviewer, Commerce Reviewer, Product Data Reviewer, SEO Reviewer, and QA Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On roadmap, gate, evidence, ownership, dependency, remediation, or release change
- **Lifecycle:** Review
- **Source of Truth:** [Master Remediation Roadmap](MASTER_REMEDIATION_ROADMAP.md), [Execution Gates](EXECUTION_GATES.md), and current Sprint 02–04 evidence
- **Dependencies:** [Master Remediation Roadmap](MASTER_REMEDIATION_ROADMAP.md), [Execution Gates](EXECUTION_GATES.md), [Authenticated WordPress Audit](AUDIT_REPORT_SPRINT04B_AUTHENTICATED.md), and [Platform Governance](../repository/platform/PLATFORM_GOVERNANCE.md)
- **Related Documents:** [Site Health Remediation Plan](SITE_HEALTH_REMEDIATION_PLAN.md), [Sprint Roadmap](SPRINT_ROADMAP.md), [Rollback Plan](../repository/config/ROLLBACK_PLAN.md), and [Sprint 04C Audit](AUDIT_REPORT_SPRINT04C.md)
- **Traceability:** RM-001 through RM-046 and Gates G00 through G14
- **AI Compatibility:** AI-readable dependency sequence; phases are plans, not execution authority
- **Approval:** Pending Founder and specialist review; no phase is authorized by this document

## Purpose

Define the safest dependency-respecting order for remediation and eventual WooCommerce production work.

## Sequence Rules

1. No mutable action begins until the exact task scope and applicable gates are approved.
2. Recovery capability precedes every production or staging mutation.
3. Evidence collection precedes root-cause selection.
4. Infrastructure stability precedes plugin/theme/commerce configuration.
5. Governance conflicts precede feature implementation.
6. Approved component capability precedes templates, catalog, inquiry, content, CRM, SEO, and performance work.
7. Product Data approval precedes WooCommerce entity creation/import.
8. Production acceptance requires functional, security, data, SEO, mobile/RTL, accessibility, performance, email, cron, logging, and rollback evidence.

## Safest Execution Order

### Phase 0 — Planning and Authority Freeze

**Objective:** approve scope, ownership, rules, and issue priorities without changing runtime.

**Issues:** `RM-045`, roadmap-wide.

**Required gates:** `G00`, `G01`.

**Planned activities:**

- Founder reviews the roadmap, sequence, gates, Platform/Engine authority, and role delegations.
- Confirm Inquiry First, No Public Pricing, No AI Phase 1, No Custom Theme, No Gravity Forms, No LiteSpeed Cache, Plugin First, Configuration First, Mobile First, and Persian RTL remain authoritative.
- Convert approved roadmap entries into narrow tickets; one ticket must not combine unrelated high-risk changes.

**Exit criteria:** explicit authority, owners, approved priorities, and no unresolved conflict about governing rules.

**Rollback checkpoint:** repository-only review revision; no runtime rollback.

### Phase 1 — Temporary Access Closure and Recovery Foundation

**Objective:** eliminate audit-access exposure and prove recovery before other mutation.

**Issues:** `RM-033`, `RM-034`.

**Required gates:** `G02`, `G03`.

**Planned order:**

1. Confirm a known Founder-controlled break-glass Administrator path.
2. Revoke the temporary auditor account/credentials and invalidate sessions under a dedicated approved user-management task.
3. Define backup scope, custody, encryption, retention, and restoration owner.
4. Capture a complete files/database/configuration backup.
5. Restore it into an isolated target and validate integrity and application behavior.

**Exit criteria:** temporary access closed; current complete backup and isolated restore proof accepted.

**Rollback checkpoint:** verified break-glass access and first restorable baseline (`R0`).

### Phase 2 — Staging and Evidence Baseline

**Objective:** establish a recoverable environment and current evidence without altering production behavior.

**Issues:** `RM-005`, `RM-006`, `RM-015`, `RM-022`, `RM-035` evidence subset.

**Required gates:** `G04`, `G05`.

**Planned order:**

1. Confirm shared-hosting capabilities and limitations.
2. Establish an isolated staging target or an approved equivalent recovery test target.
3. Record exact runtime/component/configuration inventories with secrets redacted.
4. Reconcile product counts, plugin ownership, MU-plugin/drop-ins, logs, jobs, users/roles, and data dependencies.
5. Create reproducible pre-change smoke and regression checks.

**Exit criteria:** staging parity for affected layers, evidence inventory, and rollback rehearsal accepted.

**Rollback checkpoint:** immutable production baseline plus validated staging clone (`R1`).

### Phase 3 — Hosting and Connectivity Root Causes

**Objective:** resolve connectivity and URL identity before runtime or commerce changes.

**Issues:** `RM-001`, `RM-002`, `RM-003`, `RM-004`, `RM-006`, `RM-023`.

**Required gates:** `G06` and issue-specific security/provider approval.

**Planned order:**

1. Correlate DNS, A/AAAA, IPv4/IPv6, resolver timing, provider egress, firewall/WAF, CloudLinux/LVE, and LiteSpeed logs.
2. Identify the exact request-control source for WordPress.org blacklisting.
3. Correct only the proven WordPress.org request policy in staging.
4. Separate REST application-bootstrap latency from the passing loopback test.
5. Resolve page-cache-test DNS timeout.
6. Reconcile stored/effective Home/Site URLs, HTTPS, TLS, proxy/filter behavior, redirects, and canonical host in staging.
7. Repeat REST, WordPress.org, DNS, loopback, page-cache, authorization-header, TLS, login, and redirect tests.

**Exit criteria:** stable official-source connectivity, REST, DNS, HTTPS identity, and loopback/page-cache diagnostics.

**Rollback checkpoint:** pre-connectivity provider/options/plugin-policy baseline (`R2`).

### Phase 4 — Runtime Compatibility, Cron, and Security Baseline

**Objective:** create a supported, recoverable, least-privilege WordPress foundation.

**Issues:** `RM-007`, `RM-008`, `RM-009`, `RM-016`, `RM-024`, `RM-025`, `RM-031`, `RM-035`, `RM-036`.

**Required gates:** `G07`, `G08`.

**Planned order:**

1. Build an exact Core/PHP/MariaDB/theme/plugin compatibility matrix from primary vendor evidence.
2. Test the proposed PHP/runtime path in staging; do not combine it with plugin cleanup.
3. Align WordPress memory only from measured requirements.
4. Diagnose WordPress Cron and Woo scheduled actions by owner/hook; never bulk-run/delete.
5. Review security responsibility overlap and Elementor Safe Mode MU-plugin provenance.
6. Establish MFA/session/log/file-integrity/WAF/permission/debug/update controls.
7. Standardize update ownership/windows after rollback tests.
8. Consider OPcache tuning only with provider measurements.

**Exit criteria:** approved runtime, stable cron/actions, security baseline, and least-privilege access pass.

**Rollback checkpoint:** supported pre-hardening runtime snapshot (`R3`).

### Phase 5 — Mandatory Governance Conflict Remediation

**Objective:** remove runtime conflicts with explicit Phase 1 rules.

**Issues:** `RM-043`, `RM-044`.

**Required gates:** `G09`.

**Planned order:**

1. Confirm Founder decision that No AI Features Phase 1 remains unchanged.
2. Disable Rank Math Content AI only in staging; validate no other AI modules/jobs/features are active.
3. Review price-related page content and purpose read-only.
4. Approve retain/rewrite/unpublish decisions that preserve No Public Pricing; execute only in a separate content task.

**Exit criteria:** no active Phase 1 AI feature and Founder-approved treatment of pricing-related content.

**Rollback checkpoint:** Rank Math/content snapshot (`R4`).

### Phase 6 — Approved Presentation Stack Alignment

**Objective:** establish approved vendor components without building templates/pages.

**Issues:** `RM-018`, `RM-019`, `RM-020`, `RM-021`, `RM-041` dependency preparation.

**Required gates:** `G10`.

**Planned order:**

1. Verify Blocksy Pro and Elementor Pro package provenance, licenses, exact versions, dependencies, support, and compatibility.
2. Introduce one component at a time in staging.
3. Validate Blocksy ownership of shell/header/footer/navigation/Woo presentation.
4. Validate Elementor ownership only for delegated body composition.
5. Resolve Elementor Library invalid JSON after infrastructure stability.
6. Review experiments, Default Kit, draft artifact, and template lifecycle without creating production templates.

**Exit criteria:** approved Pro components work in staging with no ownership overlap or RTL/mobile/accessibility/performance regression.

**Rollback checkpoint:** pre-component staging snapshot plus package-specific rollback (`R5`).

### Phase 7 — WooCommerce Inquiry-Only Foundation

**Objective:** establish an explicit commerce configuration contract before catalog data.

**Issues:** `RM-011`, `RM-012`, `RM-013`, `RM-017`.

**Required gates:** `G11`.

**Planned order:**

1. Approve the exact Inquiry First, No Public Pricing, cart, checkout, order, payment, shipping, tax, customer, stock, email, schema, feed, REST, search, and cache policy.
2. Review/disable only unapproved Woo capabilities such as Point of Sale, marketplace, remote logging, transactional promotions, coupons, or stock behavior.
3. Resolve missing Woo page assignments according to the approved inquiry-only policy; do not run default page-generation wizards blindly.
4. Validate HPOS, logs, scheduled actions, and plugin compatibility.
5. Implement and test no-price/inquiry controls in staging through approved configuration/capability only.

**Exit criteria:** exhaustive acceptance matrix proves no public pricing/transaction exposure and correct inquiry context.

**Rollback checkpoint:** Woo options/pages/database baseline (`R6`).

### Phase 8 — Product Data Approval and Staging Dry Run

**Objective:** resolve Product Engine blockers before creating runtime product entities.

**Issues:** `RM-014`, `RM-015`, `RM-046`.

**Required gates:** `G12`.

**Planned order:**

1. Approve Platform/Product Engine authority and assigned reviewers.
2. Resolve Pipe stable IDs, SKU policy, taxonomy/attribute/term identities, slug policy, valid commercial combinations, technical/commercial evidence, and CRM/SEO mappings.
3. Remove every blocking `TBD` from execution data while preserving unknowns outside runtime.
4. Approve exact WooCommerce importer/version/field mappings.
5. Run a uniquely tagged staging dry run only after prechecks pass.
6. Reconcile every parent, variation, term, attribute, SKU, media relation, and inquiry/no-price output.
7. Roll back the dry run and prove deterministic cleanup/re-execution.

**Exit criteria:** Product Data governance and import prechecks pass; repeatable dry run and rollback accepted.

**Rollback checkpoint:** empty/known staging catalog plus tagged import snapshot (`R7`).

### Phase 9 — Inquiry, CRM, Email, and Privacy

**Objective:** create a reliable inquiry lifecycle without inventing CRM/business rules.

**Issues:** `RM-037`, `RM-038`, `RM-039`.

**Required gates:** `G13`.

**Planned order:**

1. Approve SMTP provider, sender identity, DNS authentication, credential custody, logging, and failure handling.
2. Configure and validate SMTP in staging, then through a separately approved production task.
3. Approve inquiry fields, consent, retention, anti-spam, notification, assignment, CRM status, permissions, and recovery.
4. Decide whether FluentCRM and WPForms satisfy the approved capability model; do not complete wizards before that decision.
5. Test product, multi-product, and project inquiries end-to-end with synthetic data only.

**Exit criteria:** reliable delivery, privacy/security controls, CRM reconciliation, and inquiry lifecycle acceptance pass.

**Rollback checkpoint:** mail/CRM/form configuration and test-data snapshot (`R8`).

### Phase 10 — Content, Navigation, and SEO

**Objective:** align existing content with approved IA and prepare a non-indexed release candidate.

**Issues:** `RM-026`, `RM-027`, `RM-028`, `RM-029`, `RM-040`, `RM-041`, `RM-042`.

**Required gates:** `G14` pre-release-content portion.

**Planned order:**

1. Map every existing page/post/media/navigation entity to approved content type, owner, lifecycle, URL, and SEO role.
2. Resolve placeholders and draft artifacts only with versioned rollback.
3. Implement one approved navigation owner per desktop/mobile/footer location.
4. Reconcile Rank Math connection only after URL/TLS/canonical stability.
5. Apply approved metadata, schema, canonical, sitemap, robots, redirects, breadcrumbs, and internal linking.
6. Validate absence of price/Offer leakage and duplicate schema.
7. Keep Coming Soon and search blocking enabled.

**Exit criteria:** complete content/navigation/SEO acceptance while still non-indexed.

**Rollback checkpoint:** versioned content/navigation/SEO snapshot (`R9`).

### Phase 11 — Performance, Mobile RTL, Accessibility, and Full QA

**Objective:** validate release behavior before production acceptance.

**Issues:** `RM-030`, `RM-032` and regression scope of all prior issues.

**Required gates:** `G14` full release-candidate portion.

**Planned order:**

1. Establish representative mobile RTL, accessibility, security, SEO, functional, load, email, cron, cache, and recovery baselines.
2. Optimize only measured bottlenecks; do not add LiteSpeed Cache.
3. Evaluate an approved Redis object-cache capability only after functional stability.
4. Re-run Inquiry First/No Public Pricing tests across every public and machine-readable surface.
5. Perform rollback rehearsal from the release candidate.

**Exit criteria:** all quality gates pass with evidence and no critical/high unresolved defect.

**Rollback checkpoint:** release-candidate snapshot (`R10`).

### Phase 12 — Production Release Decision

**Objective:** make an explicit Founder Go/No-Go decision; do not infer approval.

**Required gate:** `G14` final approval.

**Planned order:**

1. Review all gate evidence, residual risks, rollback readiness, monitoring, support, and ownership.
2. Approve or reject the exact production change set and release window.
3. Execute only under a separate production-release authorization.
4. Remove Coming Soon/index blocking only after the release and SEO launch gate passes.

**Exit criteria:** explicit signed Founder release decision and completed production validation.

## Prohibited Sequence Shortcuts

- No product import before infrastructure, recovery, Inquiry First/No Public Pricing, and Product Data gates.
- No PHP/Core/plugin/theme update bundle.
- No default WooCommerce setup wizard as a substitute for approved configuration.
- No Elementor/Blocksy template build before ownership and Pro capability gates.
- No CRM/form wizard before privacy/inquiry decisions.
- No Rank Math reconnect before URL/TLS/canonical stability.
- No cache/optimization before functional and DNS/REST stability.
- No cleanup/removal before dependency and restore evidence.
- No indexing/public launch before final Founder approval.

## Current Sequence Decision

**GO** for Founder/specialist review and conversion of Phase 0–1 into separately authorized tickets.

**NO-GO** for executing Phase 1 or later, WooCommerce implementation, Product Data import, production acceptance, or release.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial dependency-safe remediation sequence; planning only. |

