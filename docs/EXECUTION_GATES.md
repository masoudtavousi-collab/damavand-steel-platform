# Remediation Execution Gates

## Document Control

- **Document ID:** `docs/EXECUTION_GATES.md`
- **Status:** Review
- **Authority:** Planning Record
- **Owner:** Founder
- **Reviewer:** Enterprise WordPress Platform Architect, Repository Guardian, Security Reviewer, Operations Reviewer, Commerce Reviewer, Product Data Reviewer, SEO Reviewer, Privacy Reviewer, and QA Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On roadmap, evidence, approver, gate, remediation, release, or rollback change
- **Lifecycle:** Review
- **Source of Truth:** [Master Remediation Roadmap](MASTER_REMEDIATION_ROADMAP.md), [Implementation Sequence](IMPLEMENTATION_SEQUENCE.md), and current repository governance
- **Dependencies:** [Master Remediation Roadmap](MASTER_REMEDIATION_ROADMAP.md), [Implementation Sequence](IMPLEMENTATION_SEQUENCE.md), [Platform Governance](../repository/platform/PLATFORM_GOVERNANCE.md), and [Engineering Guidelines](ENGINEERING_GUIDELINES.md)
- **Related Documents:** [Rollback Plan](../repository/config/ROLLBACK_PLAN.md), [Release Checklist](../quality/RELEASE_CHECKLIST.md), [Security Checklist](../quality/SECURITY_CHECKLIST.md), and [Sprint 04C Audit](AUDIT_REPORT_SPRINT04C.md)
- **Traceability:** RM-001 through RM-046 and G00 through G14
- **AI Compatibility:** AI-readable gate contract; missing evidence is failure, not implied approval
- **Approval:** Pending Founder and specialist review; every gate currently `NOT PASSED`

## Purpose

Define mandatory evidence and approval gates before remediation, implementation, catalog work, or production release.

## Gate Semantics

| State | Meaning |
| --- | --- |
| `NOT ASSESSED` | Required evidence has not been reviewed |
| `FAILED` | One or more mandatory criteria are absent or rejected |
| `CONDITIONAL` | Only explicitly listed non-mutable preparation may continue |
| `PASSED` | All evidence and named approvals are recorded for the exact scope/version/change set |
| `EXPIRED` | Evidence no longer matches the target or approved validity window |

Silence, chat output, document creation, plugin presence, a passing Site Health item, or prior approval for another scope never equals `PASSED`.

## Universal Gate Rules

Every mutable task must identify:

- Exact target, environment, files/options/data/components, and exclusions.
- Governing issue IDs and architecture/business rules.
- Current evidence and expected outcome.
- Approved owner, executor, reviewer, and rollback owner.
- Backup/restore checkpoint and rollback trigger.
- Test plan and evidence-retention location.
- Security/privacy/credential handling.
- Founder approval for the exact change set.

Any mismatch stops execution and returns the task to planning.

## Gate Register

### G00 — Roadmap Acceptance

**Before:** any remediation ticket is authorized.

**Required evidence:**

- Master issue register reviewed for completeness, classification, priority, dependencies, and duplication.
- Implementation Sequence and Execution Gates reviewed.
- Residual unknowns and evidence limitations accepted.

**Approvers:** Founder; Enterprise WordPress Platform Architect; Repository Guardian.

**Pass criteria:** explicit approval of the planning baseline and selected issues for ticket creation.

**Fail criteria:** architecture/business conflict, missing issue, unsupported priority, or inferred authority.

**Current state:** `NOT ASSESSED`.

### G01 — Governance and Authority

**Before:** any runtime change design.

**Required evidence:**

- Core principles confirmed: Plugin First, Configuration First, Mobile First, Persian RTL, Inquiry First, No Public Pricing, No Custom Theme, No Gravity Forms, No LiteSpeed Cache, and No AI Features Phase 1.
- Platform/Product Engine authority and owner delegations approved or explicitly bounded.
- Exact Founder and specialist approval authorities assigned.

**Approvers:** Founder; Architecture Authority when assigned; Repository Guardian.

**Pass criteria:** no authority conflict or unresolved governing rule affects the selected change.

**Fail criteria:** proposed change depends on a Draft/Review decision not explicitly accepted for scope.

**Current state:** `FAILED` — Platform/Engine approvals and delegations remain unresolved.

### G02 — Credential and Access Safety

**Before:** any authenticated implementation access.

**Required evidence:**

- Temporary audit credentials revoked and sessions invalidated.
- Named least-privilege executor/reviewer roles.
- Break-glass account custody, MFA, logging, session duration, and revocation process.
- No secrets in repository/chat/evidence artifacts.

**Approvers:** Founder; Security Reviewer.

**Pass criteria:** least-privilege access exists for the exact task and recovery access is proven.

**Fail criteria:** shared/full Administrator access without exception, active temporary credential, missing MFA/session control, or exposed secret.

**Current state:** `FAILED` — authenticated audit found two Administrator accounts and no lower roles.

### G03 — Backup and Restore

**Before:** every mutable action.

**Required evidence:**

- Current complete files, database, uploads, configuration, and relevant external-system backup.
- Approved encrypted custody, retention, access, checksum/integrity, and timestamp.
- Successful isolated restore and application validation.
- Named rollback owner, time objective, triggers, and steps.

**Approvers:** Founder; Security/Operations Reviewers; task owner.

**Pass criteria:** restoration produces a working, internally consistent target matching the captured baseline.

**Fail criteria:** plugin presence or backup log without isolated restore proof.

**Current state:** `FAILED` — Kadence reports zero backups and UpdraftPlus restore is unproven.

### G04 — Staging Isolation

**Before:** diagnostic isolation, upgrades, plugin/theme/configuration changes, imports, or dry runs.

**Required evidence:**

- Isolated staging target with relevant runtime/network parity.
- Search blocking, email suppression/routing, payment/customer privacy isolation, and synthetic test data.
- Refresh, teardown, access, and rollback procedures.

**Approvers:** Founder; Security/Privacy/Operations Reviewers.

**Pass criteria:** tests cannot affect production users, data, email, payments, SEO, or credentials.

**Fail criteria:** production-only experimentation or unisolated copy with personal data.

**Current state:** `FAILED` — no staging evidence.

### G05 — Current Baseline and Scope

**Before:** selecting a remediation.

**Required evidence:**

- Timestamped versions, settings, users/roles, plugins/MU/drop-ins, themes, URLs, jobs, logs, content/data counts, and provider state applicable to the issue.
- Exact proposed delta, exclusions, and dependencies.
- No unresolved conflict between observed state and repository model.

**Approvers:** Task owner; independent reviewer; Repository Guardian for evidence location.

**Pass criteria:** another qualified reviewer can reproduce the baseline and proposed delta.

**Fail criteria:** stale screenshots, assumptions, or unrelated bundled changes.

**Current state:** `CONDITIONAL` — authenticated baseline exists, but provider/log/root-cause and several data states remain incomplete.

### G06 — Infrastructure Health

**Before:** Core/plugin/theme/WooCommerce implementation.

**Required evidence:**

- REST, DNS, WordPress.org official endpoints, loopback, page-cache test, HTTPS/TLS, canonical redirects, authorization header, and provider network controls pass.
- Root causes and changes documented separately for blacklisting, DNS, REST, and URL identity.
- No unofficial package mirror or broad firewall bypass.

**Approvers:** Hosting Provider; WordPress Platform Architect; Security Reviewer; Founder for URL/canonical changes.

**Pass criteria:** repeated tests pass from relevant server and client paths with stable logs.

**Fail criteria:** any current Sprint 04B-A critical connectivity issue remains.

**Current state:** `FAILED`.

### G07 — Runtime Compatibility

**Before:** PHP/Core/plugin/theme version or memory change.

**Required evidence:**

- Primary vendor compatibility/support matrix for exact versions.
- Staging upgrade/migration plan and rollback selector.
- Database/schema, cron, REST, Admin, email, Woo, Blocksy, Elementor, RTL/mobile, and security regression results.

**Approvers:** WordPress Platform Architect; Hosting Provider; Security Reviewer; Founder.

**Pass criteria:** approved runtime is supported by every mandatory component and passes staging regression.

**Fail criteria:** version change based only on Dashboard notice or general recommendation.

**Current state:** `FAILED`.

### G08 — Security and Operations Baseline

**Before:** feature implementation or production acceptance.

**Required evidence:**

- Least privilege, MFA, sessions, WAF/security responsibility, file integrity, permissions, debug/log policy, incident response, monitoring, cron, scheduled actions, update policy, and recovery.
- Security-plugin overlap and MU-plugin provenance resolved.

**Approvers:** Security Reviewer; Operations Reviewer; Founder.

**Pass criteria:** security checklist passes with recovery access and no Critical/High unaccepted exposure.

**Fail criteria:** two unrestricted Administrators, unproven recovery, unresolved update connectivity, or unknown privileged MU code.

**Current state:** `FAILED`.

### G09 — Core Business-Rule Compliance

**Before:** content, SEO, CRM, WooCommerce, or product implementation.

**Required evidence:**

- Rank Math Content AI inactive and no other Phase 1 AI feature active.
- Founder-approved treatment of price-related pages.
- Inquiry First and No Public Pricing acceptance criteria approved.

**Approvers:** Founder; Business Owner; SEO/Commerce/Security Reviewers as applicable.

**Pass criteria:** no active feature or content state conflicts with core rules.

**Fail criteria:** Rank Math `content-ai` active or price/inquiry decision unresolved.

**Current state:** `FAILED`.

### G10 — Approved Component and License

**Before:** Blocksy Pro or Elementor Pro installation/activation and presentation work.

**Required evidence:**

- Exact vendor package, checksum/provenance, version, license entitlement/custody, dependencies, support, and compatibility.
- Blocksy shell and Elementor body ownership matrix.
- Staging install and rollback evidence.

**Approvers:** Founder; Presentation Architect; Security/Operations Reviewers.

**Pass criteria:** approved components operate without ownership overlap or regression.

**Fail criteria:** missing commercial package/license or version inference.

**Current state:** `FAILED` — both Pro targets absent.

### G11 — WooCommerce Inquiry-Only Contract

**Before:** WooCommerce configuration, product creation, or import.

**Required evidence:**

- Founder-approved cart/checkout/order/payment/shipping/tax/customer/stock/email/pages/features policy.
- Inquiry First and No Public Pricing controls for HTML, REST, schema, feeds, email, search, cache, Admin, and exports.
- HPOS, cron/actions, logging, privacy, and rollback validation.

**Approvers:** Founder; WooCommerce Architect; Product Data, SEO, Security, Privacy, QA, and Operations Reviewers.

**Pass criteria:** staging matrix proves inquiry-only behavior and zero public transaction/price leakage.

**Fail criteria:** missing page assignments, enabled unapproved transaction features, or untested output surface.

**Current state:** `FAILED`.

### G12 — Product Data and Import

**Before:** taxonomy/attribute/term/product/variation creation or import.

**Required evidence:**

- Stable IDs, final SKU policy, valid combinations, approved terms/categories/slugs, commercial/technical sources, owners, and all required fields.
- Zero blocking `TBD` in execution data.
- Exact importer/version mapping, duplicate checks, dry run, reconciliation, rollback, and Admin manageability.

**Approvers:** Founder; Product Data Manager; qualified steel-domain, WooCommerce, SEO, Security, QA, and Operations Reviewers.

**Pass criteria:** every Product Data precheck passes and staging dry run is deterministic/reversible.

**Fail criteria:** placeholder SKU/TBD, Cartesian expansion, unapproved value, missing evidence, or no restore proof.

**Current state:** `FAILED`.

### G13 — Inquiry, CRM, Email, and Privacy

**Before:** inquiry form/CRM/email implementation or live data collection.

**Required evidence:**

- Approved inquiry types/fields/requiredness, consent, retention, access, anti-spam, notifications, assignment/statuses, and escalation.
- Approved SMTP provider/sender/DNS/credential/log/failure design.
- Approved CRM/form/plugin responsibility and data mapping.
- Synthetic end-to-end staging tests and rollback.

**Approvers:** Founder; Inquiry/CRM Owner; Privacy, Security, Email Operations, Sales, and QA Reviewers.

**Pass criteria:** delivery, privacy, reconciliation, permissions, no-price, and failure/recovery tests pass.

**Fail criteria:** Default/none mailer, setup wizard decisions, unapproved personal-data flow, or production test data.

**Current state:** `FAILED`.

### G14 — Content, SEO, Quality, and Production Release

**Before:** indexing, Coming Soon removal, production release, or public acceptance.

**Required evidence:**

- Every content/navigation/media entity has approved owner, lifecycle, URL, SEO, schema, and accessibility role.
- One canonical/schema/breadcrumb/navigation owner per output.
- Mobile First, Persian RTL, accessibility, performance, security, inquiry, no-price, email, cron, cache, analytics, logging, recovery, and rollback tests pass.
- No Critical/High unresolved defect; residual risks explicitly accepted.
- Release window, monitoring, support, rollback trigger, and post-release validation approved.

**Approvers:** Founder; Architecture, Content, SEO, UX/Accessibility, Security, Privacy, Commerce, Product Data, QA, Operations, and Release Reviewers.

**Pass criteria:** signed release Go decision for the exact immutable change set.

**Fail criteria:** inferred approval, indexing while Coming Soon gates fail, or untested production delta.

**Current state:** `FAILED`.

## Gate Dependency Chain

```text
G00 -> G01 -> G02 -> G03 -> G04 -> G05
                                  |
                                  v
G06 -> G07 -> G08 -> G09 -> G10 -> G11 -> G12 -> G13 -> G14
```

`G03` remains mandatory for every later mutable task even after its initial pass. Evidence expires when the target changes.

## Stop Conditions

Stop immediately when:

- Backup/restore, staging, credentials, or rollback evidence is missing.
- The observed target differs from the approved baseline.
- A task requires an unapproved plugin, package, license, provider action, or business decision.
- Any core principle would be weakened.
- A test exposes secrets, personal data, public pricing, transaction flow, or production email/payment effects.
- A rollback cannot be completed within the approved window.
- A Critical/High regression appears.

## Current Gate Decision

No gate is fully passed. Repository-only planning may continue under `G00` review; runtime execution remains blocked.

**GO** for gate review and evidence planning.

**NO-GO** for remediation execution, WooCommerce implementation, Product Data import, indexable launch, or production release.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial remediation execution-gate contract; all gates begin unpassed. |

