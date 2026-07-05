# Master Remediation Roadmap

## Document Control

- **Document ID:** `docs/MASTER_REMEDIATION_ROADMAP.md`
- **Status:** Review
- **Authority:** Planning Record
- **Owner:** Founder
- **Reviewer:** Enterprise WordPress Platform Architect, Repository Guardian, Security Reviewer, Commerce Reviewer, SEO Reviewer, and Operations Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On evidence, scope, ownership, priority, dependency, approval, remediation, or runtime change
- **Lifecycle:** Review
- **Source of Truth:** Current repository state and Sprint 02A–02C, Sprint 03A–03E, Sprint 04A, Sprint 04B, and Sprint 04B-A authenticated audit evidence
- **Dependencies:** [Authenticated WordPress Audit](AUDIT_REPORT_SPRINT04B_AUTHENTICATED.md), [Infrastructure Audit](INFRASTRUCTURE_AUDIT.md), [Product Data Validation Rules](../repository/data/validation/PRODUCT_DATA_VALIDATION_RULES.md), and [Platform Governance](../repository/platform/PLATFORM_GOVERNANCE.md)
- **Related Documents:** [Implementation Sequence](IMPLEMENTATION_SEQUENCE.md), [Execution Gates](EXECUTION_GATES.md), [Site Health Remediation Plan](SITE_HEALTH_REMEDIATION_PLAN.md), and [Sprint 04C Audit](AUDIT_REPORT_SPRINT04C.md)
- **Traceability:** CP-001 through CP-010, Sprint 02A–02C, Sprint 03A–03E, Sprint 04A, Sprint 04B, Sprint 04B-A, and RM-001 through RM-046
- **AI Compatibility:** AI-readable remediation register with one classification and one primary execution group per issue
- **Approval:** Pending Founder and applicable specialist approval; planning only and no remediation is authorized

## Purpose

Provide the complete, evidence-based remediation roadmap required before WooCommerce product implementation or production acceptance.

## Scope and Planning Boundary

This roadmap:

- Consolidates current issues and unresolved prerequisites without duplicating superseded unknowns.
- Assigns every issue exactly one approved classification.
- Provides risk, impact, priority, dependencies, effort, rollback, validation, owner, and primary execution group.
- Defines planning intent only. It does not approve or execute any runtime, hosting, plugin, configuration, database, content, product, user, or repository-structure change.

Authenticated Sprint 04B-A evidence supersedes earlier `UNKNOWN` states where it provides direct observation. Older reports remain evidence provenance and source of unresolved Product Engine/Platform decisions.

## Scales

### Priority

| Priority | Meaning |
| --- | --- |
| `P0` | Blocks every mutable action or creates immediate governance/security/recovery exposure |
| `P1` | Blocks WooCommerce implementation or production acceptance |
| `P2` | Required before content/catalog/SEO/CRM release |
| `P3` | Required before optimization or operational maturity |
| `P4` | Deferrable hygiene with no current release-critical impact |

### Estimated Effort

| Band | Planning range | Meaning |
| --- | --- | --- |
| `XS` | Up to 0.5 specialist day | Narrow, reversible task after prerequisites |
| `S` | 0.5–1 day | One bounded component or evidence stream |
| `M` | 2–3 days | Multi-step configuration and regression validation |
| `L` | 4–7 days | Cross-component remediation or migration |
| `XL` | More than 7 days | Multi-party program or unresolved external dependency |

Effort is an order-of-magnitude planning band, not a commercial estimate or implementation commitment.

### Primary Execution Group

Every issue has exactly one primary group: `Quick Wins`, `Safe Changes`, `High Risk`, `Founder Approval Required`, `Hosting Required`, or `Can Wait`. Dependencies may require other parties without changing the primary group.

## Master Issue Register

### Infrastructure

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-001 | REST API edit-context request times out after 10 seconds. | Sprint 04B-A Site Health: cURL 28, zero bytes. | Blind fixes may mask DNS, transport, or application delay. | Blocks editor, integrations, WooCommerce APIs, and reliable Admin operation. | P0 | RM-007, RM-008, RM-009, provider/application logs, recoverable staging. | L | Restore pre-change staging snapshot and reverse one variable at a time. | REST endpoint passes repeatedly; editor/API regressions pass; no new errors. | WordPress Platform Architect + Hosting Provider | Hosting Required |
| RM-002 | Page-cache diagnostic fails during DNS resolution after five seconds. | Sprint 04B-A async Site Health test. | Cache work could conceal unresolved resolver failure. | Unreliable self-requests and performance diagnostics. | P0 | Provider resolver/A/AAAA/IPv4/IPv6 evidence, RM-007, RM-009. | M | Revert only approved DNS/provider change to captured baseline. | Three repeated server-originated homepage requests resolve and complete; Site Health retest passes. | Hosting Provider | Hosting Required |
| RM-003 | Effective HTTPS URLs conflict with Site Health stored-URL result and Rank Math URL-change state. | Effective Home/Site URLs are HTTPS; HTTPS test says stored defaults are not; Rank Math reconnect notice. | Wrong URL edit can break login, sessions, REST, canonicals, and redirects. | Security, SEO identity, API, and session instability. | P0 | Current database options/filter/proxy/TLS/redirect evidence, backup, staging, Founder canonical-host decision. | L | Database/config snapshot; restore prior option/filter/redirect set as one change set. | Admin/front URLs, redirects, REST, cookies, TLS, canonical, sitemap, and Rank Math identity agree. | WordPress Platform Architect + Hosting Provider + SEO Reviewer | High Risk |
| RM-004 | WordPress.org/API requests are blacklisted and checksums cannot be retrieved. | Sprint 04B-A dotorg and background-update tests; Admin RSS blacklist messages. | Unverified bypass or mirror could create supply-chain exposure. | Core/plugin/theme update and integrity workflows are unreliable. | P0 | RM-016, exact blacklist source, provider/request-filter evidence, approved official-source policy. | M | Restore prior request-filter policy; remove only approved allow-list change if validation fails. | Official WordPress endpoints/checksums succeed; no non-approved destinations become allowed. | WordPress Platform Architect + Security Reviewer | High Risk |

### Hosting

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-005 | Shared hosting provides no shell/SSH path and provider-only controls/logs remain limited. | Sprint 02C and Sprint 04A/B-A. | Diagnostics, deployment, rollback, and evidence collection may be incomplete. | Slower recovery and higher dependence on support operations. | P1 | Founder hosting decision, provider capability matrix, backup/staging design. | M | Retain current plan until replacement/migration has proven rollback. | Approved capability matrix covers logs, backups, staging, DNS/TLS, cron, PHP, DB, and recovery. | Founder + Hosting Provider | Founder Approval Required |
| RM-006 | CloudLinux/LiteSpeed/WAF/resource behavior and server-side telemetry are not baselined. | CloudLinux/LVE and LiteSpeed observed; logs/limits absent. | Resource/WAF faults may be misdiagnosed as WordPress defects. | Infrastructure causes cannot be isolated or capacity planned. | P1 | Provider cooperation, timestamped tests, privacy-safe log handling. | M | Evidence-only first; later setting changes revert to provider-captured baseline. | Provider supplies timestamped LVE, LiteSpeed, WAF/ModSecurity, DNS, and outbound evidence. | Hosting Provider + Operations Reviewer | Hosting Required |

### WordPress Core

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-007 | WordPress/PHP/runtime compatibility is not approved; Dashboard and Site Health disagree on PHP `7.4.33`. | Sprint 04B-A Dashboard warning versus synchronous Site Health pass. | Unplanned upgrade can break 13 plugins/theme; no change leaves support/security risk unresolved. | Blocks trusted production baseline. | P0 | Vendor compatibility matrix, provider-supported versions, staging, restore proof. | L | Hosting snapshot plus documented PHP/runtime rollback selector. | Core, theme, plugins, REST, cron, email, Woo, RTL/mobile, and logs pass on approved runtime. | WordPress Platform Architect + Hosting Provider | High Risk |
| RM-008 | WordPress frontend memory limit is 40 MB while Admin maximum is 512 MB. | Site Health constants and Elementor System Info. | Frontend/integration requests may fail differently from Admin. | Unpredictable product, inquiry, import, and Elementor behavior. | P1 | Workload baseline, vendor requirements, RM-007, hosting approval. | S | Restore prior memory values. | Frontend/Admin/import staging tests complete without memory errors; limits documented. | Hosting Provider + WordPress Platform Architect | Hosting Required |
| RM-009 | `wp_site_health_scheduled_check` failed. | Sprint 04B-A Site Health. | Cron fixes without event ownership may create duplicate execution. | Scheduled maintenance and updates may be unreliable. | P1 | Exact cron mode/event timestamps, RM-001/RM-002/RM-004, staging. | M | Restore cron mode/schedule baseline and remove only test-created schedules. | Site Health event executes on schedule twice; no duplicate/missed jobs. | WordPress Platform Architect + Hosting Provider | High Risk |
| RM-010 | Four inactive default themes remain installed. | Authenticated Themes inventory; Site Health recommends reviewing three unused defaults while retaining one fallback. | Premature deletion can remove fallback or dependency; retention adds attack surface. | Security hygiene and maintenance overhead. | P3 | RM-038 backup/restore, approved fallback-theme policy. | XS | Restore approved theme package from official verified source/snapshot. | Active Blocksy unchanged; one approved fallback remains; Site Health/theme checks pass. | WordPress Administrator + Security Reviewer | Can Wait |

### WooCommerce

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-011 | WooCommerce setup is partial and its task widget remains at 1 of 5. | Authenticated Dashboard; Status onboarding data is not equivalent to completed governed setup. | Default wizard choices may invent business configuration. | Commerce baseline is not reproducible or approved. | P1 | RM-038, RM-041, Founder-approved Woo blueprint decisions. | M | Restore Woo options/database snapshot. | Approved configuration inventory matches blueprint; no unapproved wizard/task output remains. | WooCommerce Architect + Founder | Founder Approval Required |
| RM-012 | Shop, Cart, Checkout, and My Account assignments reference missing pages; Terms is unset. | WooCommerce Status. | Auto-repair or page generation can create unauthorized transaction flow. | Broken commerce routes and architecture conflict. | P1 | RM-011, Inquiry First/cart-checkout policy, content ownership, staging. | M | Restore prior page IDs/options and remove only task-created test pages in staging. | Page assignments intentionally match approved inquiry-only policy; no broken endpoints. | WooCommerce Architect + Content Owner | High Risk |
| RM-013 | Point of Sale, marketplace, remote logging, analytics, attribution, coupons, stock, and transaction-oriented defaults require governance. | Woo Status enabled-feature/runtime payload. | Data egress, transaction scope, UI clutter, and architecture drift. | Inquiry First/admin manageability/security can be undermined. | P0 | Founder decisions, privacy/security review, RM-011, feature inventory. | M | Export/capture options in staging; restore prior feature flags/options. | Only explicitly approved capabilities remain; no prohibited transaction/AI/data flow. | Founder + WooCommerce Architect + Privacy/Security Reviewers | Founder Approval Required |
| RM-014 | Product taxonomy/attribute foundation is absent: only empty `Uncategorized`; no global attributes. | Authenticated category/attribute lists. | Ad hoc creation would duplicate taxonomy and bypass Product Engine. | Product import and filtering cannot proceed. | P1 | RM-043, RM-044, approved IDs/slugs/values/combinations. | L | Restore staging DB; delete only uniquely tagged dry-run entities after reconciliation. | Exact categories/attributes/terms match approved manifests with zero duplicates/orphans. | Product Data Manager + WooCommerce Architect | High Risk |
| RM-015 | Product count and catalog state are not directly proven because the list redirects to onboarding. | Authenticated product-list redirect; Woo status omits product post count. | Assuming zero products could overwrite hidden data. | Unsafe imports and duplicate identities. | P0 | Read-only DB/Admin/API count evidence after RM-001, full backup. | S | Evidence-only; no data rollback required. | Three independent counts reconcile across DB/API/Admin without exposing customer data. | WooCommerce Administrator + Product Data Manager | Safe Changes |
| RM-016 | Woo scheduled actions include 3 failed, 20 pending, and a daily recurring task not scheduled. | WooCommerce Status. | Running/deleting actions could create side effects or data loss. | Emails, analytics, cleanup, and future inquiries may not execute reliably. | P1 | Action names/logs, RM-001/RM-004/RM-009, backup/staging. | M | Restore scheduler tables/options snapshot; reverse one hook-specific fix. | Failed causes resolved; expected pending queue drains normally; recurrence observed twice. | WooCommerce Architect + WordPress Platform Architect | High Risk |
| RM-017 | Inquiry First and No Public Pricing are not enforced across Woo outputs. | No products/approved configuration; currency and transaction features exist; Sprint 03 gates remain blocked. | Price/cart/checkout may leak through HTML, REST, schema, email, feeds, search, or cache. | Direct breach of core business rules. | P0 | Founder-approved acceptance contract, RM-011–RM-015, staging, approved inquiry capability. | XL | Full database/files snapshot; feature-flag rollback; restore prior template/config set. | Automated/manual matrix proves no public price/transaction and complete inquiry context on all surfaces. | Founder + WooCommerce Architect + QA/Security/SEO Reviewers | Founder Approval Required |

### Blocksy

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-018 | Blocksy Pro/Companion is uninstalled although it is the approved presentation target. | Authenticated Blocksy payload. | Installing without package/license/compatibility evidence may destabilize presentation. | Blueprint cannot be implemented or supported as approved. | P1 | Founder license/package approval, compatibility matrix, RM-038, staging. | M | Restore theme/plugin/config snapshot and deactivate only the newly introduced approved package in staging. | License/package provenance, version compatibility, header/footer/Woo/RTL/mobile regression pass. | Founder + Presentation Architect | Founder Approval Required |
| RM-019 | Header, footer, responsive visibility, menu placement, and Customizer ownership are not approved against live state. | Blocksy exposes relevant panels; no classic menu; one block navigation. | Overlap with Elementor/block navigation can duplicate shell output. | Navigation, mobile, RTL, accessibility, and maintainability risk. | P2 | RM-018, RM-035, approved design/content ownership. | L | Restore Blocksy configuration export/snapshot. | Header/footer ownership matrix and viewport/RTL/accessibility regression pass. | Presentation Architect + UX/Content Owners | High Risk |

### Elementor

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-020 | Elementor Pro is absent; only Elementor base `4.1.4` is active. | Authenticated plugin/System Info evidence. | Installing without package/license/compatibility evidence creates lock-in and version risk. | Approved composition blueprint unavailable. | P1 | Founder package/license approval, RM-007, RM-038, staging. | M | Restore plugin/template/database snapshot; remove only introduced package after rollback approval. | Pro activation/license/compatibility verified; zero templates created; Blocksy ownership preserved. | Founder + Presentation Architect | Founder Approval Required |
| RM-021 | Elementor Library returns invalid JSON; Default Kit, draft artifact, experiments, and Safe Mode provenance need review. | Elementor System Info and template/page inventories. | Reset/regeneration could change styles/content; experiments can alter editor/runtime behavior. | Template reliability and future maintenance are uncertain. | P2 | RM-001/RM-003/RM-004, template inventory, backup/staging, RM-024. | M | Restore Elementor options/CSS/template snapshot; revert one experiment at a time. | Library connects or documented offline policy passes; artifacts/experiments have approved owners and regression evidence. | Presentation Architect + WordPress Platform Architect | High Risk |

### Plugin

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-022 | Active-plugin ownership, approval, license, data flow, replacement, and necessity are incomplete. | 13 active plugins; Matrix approves only target capabilities, not every live component/config. | Unowned plugins create security, privacy, compatibility, and maintenance debt. | Enterprise supportability is unproven. | P1 | Founder/component-owner review, exact configuration/data dependency inventory. | L | Evidence-only first; future removals use backup, dependency map, and one-plugin rollback. | Every plugin has approved owner/purpose/source/version/data/upgrade/replacement record. | WordPress Platform Architect + Repository Guardian | Safe Changes |
| RM-023 | Request filtering/blacklisting may involve the Iran network optimizer, but attribution is unproven. | Optimizer active; WordPress.org and feeds explicitly blacklisted. | Disabling or bypassing blindly can break Iran connectivity/security policy. | Updates and vendor services remain unreliable. | P0 | Exact plugin settings/hooks/logs, provider policy, RM-004, staging. | M | Restore captured optimizer settings and request policy. | Official endpoints work; approved blocked destinations remain blocked; no regression in local access. | WordPress Platform Architect + Security Reviewer | High Risk |
| RM-024 | Kadence Security and Limit Login Attempts overlap; Elementor Safe Mode MU-plugin purpose is unexplained. | Authenticated plugin/MU-plugin inventories. | Duplicate controls can lock out users; unexplained MU code bypasses normal plugin lifecycle. | Access reliability and governance risk. | P1 | Config/hook/log comparison, provenance, backup/staging. | M | Restore plugin/MU-plugin files/options and prior activation state. | One approved owner per capability; login/MFA/lockout tests pass; MU-plugin disposition documented. | Security Reviewer + WordPress Platform Architect | High Risk |
| RM-025 | Auto-update and unused-capability policy is inconsistent; only the Iran optimizer shows auto-update enabled, while inactive/unused components remain. | Authenticated plugin filter and inventories. | Uncontrolled update or cleanup can cause outage. | Version drift and operational inconsistency. | P2 | RM-038, approved update windows, plugin responsibility decisions. | S | Restore prior auto-update flags/packages from snapshot. | Approved policy matches every component; staged update/rollback evidence exists. | WordPress Administrator + Security/Operations Reviewers | Safe Changes |

### SEO

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-026 | Rank Math site identity is disconnected after a URL change. | Authenticated reconnect notice; Search Console/Analytics disconnected. | Reconnect before canonical/TLS resolution can bind wrong property. | Analytics, sitemap, canonical, and account identity inconsistency. | P1 | RM-003, Founder canonical-host/property decision, credential owner. | M | Disconnect new binding and restore prior verified account/property mapping. | Effective/stored URLs, canonical, sitemap, Search Console property, and Rank Math identity agree. | SEO Owner + Founder | Founder Approval Required |
| RM-027 | All pages show SEO N/A, no focus keyword, zero link counts, and default Article schema. | Authenticated Pages list. | Bulk defaults can create incorrect schema and thin/duplicate metadata. | Search quality and entity architecture remain unimplemented. | P2 | Approved content/entity/SEO models, content owners, RM-034. | L | Restore metadata/schema export or database snapshot. | Page-by-page metadata/schema/link review passes without duplication. | SEO Owner + Content Owner | High Risk |
| RM-028 | Indexing is blocked and Coming Soon is enabled. | Site Health and Dashboard. | Premature removal exposes incomplete/unsafe site; indefinite retention blocks launch. | No indexable production release. | P2 | All release gates, Founder launch decision, RM-003/RM-017/RM-027. | XS | Re-enable Coming Soon/index blocking immediately. | Robots/meta/status/sitemap/public access match approved launch state. | Founder + SEO Owner | Founder Approval Required |
| RM-029 | Canonical, sitemap, robots, redirects, breadcrumbs, schema ownership, and public-price schema are not validated. | Authenticated Admin evidence plus Sprint 03 SEO TBDs. | Competing owners may emit duplicate or price-bearing structured data. | SEO cannibalization and No Public Pricing breach. | P1 | RM-003, RM-017, RM-018–RM-021, approved schema strategy. | L | Restore SEO/theme/plugin configuration snapshot. | Crawl/test matrix shows one canonical/schema/breadcrumb owner and no price/Offer leakage. | SEO Owner + WooCommerce/Presentation Architects | High Risk |

### Performance

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-030 | Persistent object cache is absent although hosting reports Redis availability. | Site Health; `WP_CACHE` off; no external object cache. | Adding cache before connectivity correctness can hide defects or corrupt state. | Potential DB load and inconsistent performance. | P3 | RM-001–RM-004, provider capability, approved cache component; LiteSpeed Cache remains prohibited. | M | Disable approved cache, remove its drop-in/config, restore snapshot, flush only under rollback plan. | Functional, cache-coherence, purge, admin, inquiry, and performance tests pass. | Performance Engineer + Hosting Provider | Can Wait |
| RM-031 | OPcache interned string buffer is fully utilized. | Site Health: 6 MB at 100%; OPcache overall not full. | Blind tuning can consume shared-host resources or have no benefit. | Possible compilation/cache churn. | P3 | Provider metrics, repeat measurements, RM-007. | S | Restore provider OPcache values. | Interned usage/headroom and hit rate remain stable under representative load. | Hosting Provider + Performance Engineer | Hosting Required |
| RM-032 | No frontend mobile/RTL/accessibility/Core Web Vitals baseline exists. | Admin-only authenticated audit; Sprint 03/architecture requires Mobile First/Persian RTL. | Optimization without baseline can regress UX or hide bottlenecks. | Release quality cannot be measured. | P2 | Stable infrastructure, approved templates/content, test devices/method. | M | Measurement-only first; future change reverts through component snapshot. | Reproducible page-type baseline and thresholds approved for mobile RTL. | Performance Engineer + UX/Accessibility Reviewers | Can Wait |

### Security

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-033 | Complete backup and isolated restore are not proven; Kadence reports zero backups. | Authenticated security status; UpdraftPlus presence only. | Any change can become unrecoverable. | Blocks every mutable remediation. | P0 | Approved storage/custody/encryption/retention, staging restore target. | L | This issue establishes rollback; no mutable action before proof. | Full files/database/config backup restores to isolated environment and passes integrity/app tests. | Security/Operations Owners + Founder | Founder Approval Required |
| RM-034 | Both users are Administrators; temporary auditor removal and least-privilege role design are pending. | Authenticated Users list: 2 administrators, no other roles. | Credential compromise grants full control. | Critical account/security/governance exposure. | P0 | Founder identity/role decisions, recovery admin, session evidence, RM-033. | S | Retain verified break-glass admin; recreate only approved temporary role/account if rollback needed. | Temporary account absent, sessions invalidated, role matrix/capabilities/2FA pass. | Founder + Security Reviewer | Quick Wins |
| RM-035 | MFA, sessions, security/WAF logs, file integrity, XML-RPC, headers, and incident response are unverified. | Sprint 04B-A security gaps. | Hidden compromise or lockout exposure may remain. | Production security cannot be accepted. | P1 | RM-033/RM-034, privacy-safe evidence, provider logs. | L | Restore security plugin/policy snapshot; retain recovery access. | Security checklist, log retention, MFA, session, header, file-integrity, and incident tests pass. | Security Reviewer + Hosting Provider | High Risk |
| RM-036 | Writable runtime directories, custom `.htaccess`, and production debug-display posture need hardening review. | Site Health paths writable; custom rules; `WP_DEBUG_DISPLAY` on while debug off. | Over-hardening can break updates/uploads; under-hardening increases tampering/exposure. | Filesystem and error-disclosure risk. | P1 | Exact owner/mode/web identity, deployment/update method, RM-033, staging. | M | Restore captured modes/ownership/config/rules. | Approved permission matrix, uploads, updates, logs, and public error-disclosure tests pass. | Security Reviewer + Hosting Provider | High Risk |

### CRM

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-037 | FluentCRM is active but redirects to its Setup Wizard; ownership and Phase 1 need are unapproved. | Authenticated FluentCRM entry. | Completing wizard can invent CRM/email/data settings. | CRM is non-operational and can create ungoverned personal data. | P2 | Founder CRM decision, privacy model, RM-022/RM-039, staging. | M | Restore CRM options/tables snapshot; remove only test data in staging. | Approved owner, fields, consent, lifecycle, permissions, integrations, and recovery pass. | Founder + CRM/Privacy Owners | Founder Approval Required |
| RM-038 | SMTP uses Default/none and has failed delivery evidence. | WP Mail SMTP settings/Site Health; five failures in 30 days. | Inquiry/admin notifications may be lost; unsafe test sends can expose data. | Inquiry First cannot operate reliably. | P0 | Approved sender/provider/DNS/credential custody, RM-003/RM-004/RM-033. | M | Restore mailer/DNS configuration; retain prior sender identity and logs. | SPF/DKIM/DMARC policy, authenticated delivery, bounce/failure/admin/inquiry tests pass. | Email Operations Owner + Founder | Founder Approval Required |
| RM-039 | WPForms has zero forms and the inquiry capture/CRM/privacy flow is not implemented. | Authenticated WPForms status; Sprint 03 inquiry mapping blocked. | Ad hoc form creation can violate Inquiry architecture/privacy and duplicate CRM data. | Core conversion path is absent. | P1 | Founder-approved inquiry capability, field/consent/anti-spam/CRM model, RM-037/RM-038. | L | Restore form/plugin/CRM snapshot; remove uniquely identified staging submissions. | Product/multi-product/project inquiry tests, consent, anti-spam, notification, CRM, and no-price gates pass. | Inquiry/CRM Architect + Privacy/Security Reviewers | Founder Approval Required |

### Content

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-040 | Twelve pages predate approved content mapping; titles/statuses exist without lifecycle/owner validation. | 11 published pages and one Elementor draft. | Editing or deleting may lose accepted content; keeping them may create drift. | Content architecture and maintainability are unverified. | P2 | Founder/content inventory review, approved Content Types/IA/URLs, RM-027. | L | Versioned content export/database snapshot and per-page rollback. | Every page maps to approved type, owner, URL, lifecycle, SEO, and navigation role. | Content Owner + Founder | Founder Approval Required |
| RM-041 | No classic menu exists; one block Navigation entity has unknown contents/assignment. | Authenticated Menus and Navigation lists. | Creating parallel menus can duplicate ownership and break mobile navigation. | Header/footer/site discovery cannot be implemented safely. | P2 | RM-019, approved Site Structure/Navigation Map, content/page review. | M | Restore navigation/menu/theme configuration snapshot. | One approved source per desktop/mobile/footer location; link/accessibility/RTL tests pass. | Content/UX Owners + Presentation Architect | High Risk |
| RM-042 | Default “Hello World”/comment, one unattached Woo placeholder media item, and draft artifact require disposition. | Dashboard, Media, and Pages evidence. | Cleanup without ownership/recovery can delete referenced assets; retention exposes placeholder content. | Launch hygiene and content quality. | P4 | RM-033, RM-040, reference check, Founder approval. | XS | Restore deleted items from snapshot/trash where supported. | No approved reference breaks; placeholders absent from public launch inventory. | Content Owner | Can Wait |

### Business Rule

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-043 | Rank Math `content-ai` module is active against No AI Features Phase 1. | Authenticated active-module payload. | AI processing/data use violates an explicit core rule. | Governance noncompliance blocks approval. | P0 | RM-033, Founder confirmation of unchanged Phase 1 rule, Rank Math configuration snapshot. | XS | Restore prior Rank Math module state if disabling causes regression; no AI use during validation. | Content AI absent from active modules/UI/API jobs; no other Phase 1 AI capability active. | Founder + SEO/WordPress Administrators | Founder Approval Required |
| RM-044 | “قیمت روز استیل” and “محاسبه‌گر قیمت” require an explicit decision under No Public Pricing. | Authenticated published page titles; page output not inspected. | Names/content could expose or imply public pricing contrary to business rules. | Legal/commercial/SEO and trust risk. | P0 | Founder content/business decision, read-only content/frontend review, RM-040. | S | Restore prior page status/content/URL from versioned snapshot. | Founder-approved purpose and tests prove no prohibited public price/calculator output. | Founder + Business/Content/SEO Owners | Founder Approval Required |

### Repository

| ID | Description | Evidence | Risk | Impact | Priority | Dependencies | Effort | Rollback strategy | Validation method | Owner | Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RM-045 | Platform Manifest, Product Engine, templates, and owner delegations remain Review/pending Founder approval. | Sprint 03D/03E audits. | Runtime work may treat proposed authority as approved. | Governance and change authority remain ambiguous. | P0 | Founder/specialist review of Platform/Engine decisions and role assignments. | M | Revert document lifecycle/authority metadata through reviewed repository change. | Explicit approvals/rejections, owners, versions, dependencies, and decision log evidence exist. | Founder + Repository Guardian | Founder Approval Required |
| RM-046 | Pipe/Product Data still lacks stable IDs, final SKUs, valid commercial combinations, taxonomy/term IDs, slugs, technical/commercial evidence, and import/recovery approval. | Sprint 03A–03C audits and Product Data prechecks. | `TBD` or Cartesian data can leak into WooCommerce and create unmanageable variations. | Product implementation/import remains blocked. | P0 | Qualified steel-domain review, Founder decisions, Product Engine approval, RM-014/RM-017/RM-033. | XL | Repository version rollback; staging DB restore; reconcile/delete only uniquely tagged dry-run entities. | All prechecks pass with zero `TBD`, duplicates, invalid tuples, prices, orphan mappings, or reconciliation gaps. | Founder + Product Data Manager + Steel-domain/Woo/SEO Reviewers | Founder Approval Required |

## Grouped Remediation Views

These are primary groups only; dependencies and approvals still apply.

### Quick Wins

- `RM-034` — revoke temporary audit access and establish least-privilege role controls after recovery access is confirmed.

### Safe Changes

- `RM-015` — reconcile product counts read-only.
- `RM-022` — complete plugin responsibility/ownership records.
- `RM-025` — standardize update-policy evidence before changing flags.

### High Risk

- `RM-003`, `RM-004`, `RM-007`, `RM-009`, `RM-012`, `RM-014`, `RM-016`, `RM-019`, `RM-021`, `RM-023`, `RM-024`, `RM-027`, `RM-029`, `RM-035`, `RM-036`, and `RM-041`.

### Founder Approval Required

- `RM-005`, `RM-011`, `RM-013`, `RM-017`, `RM-018`, `RM-020`, `RM-026`, `RM-028`, `RM-033`, `RM-037`, `RM-038`, `RM-039`, `RM-040`, `RM-043`, `RM-044`, `RM-045`, and `RM-046`.

### Hosting Required

- `RM-001`, `RM-002`, `RM-006`, `RM-008`, and `RM-031`.

### Can Wait

- `RM-010`, `RM-030`, `RM-032`, and `RM-042`.

## Dependency Order

```text
Founder approval and authority
  -> recovery and temporary-access closure
      -> hosting/runtime evidence and infrastructure health
          -> Core/security/plugin governance
              -> approved Blocksy/Elementor capability baseline
                  -> WooCommerce Inquiry/No-Price configuration
                      -> Product Data approval and staging dry run
                          -> CRM/content/navigation/SEO
                              -> performance/accessibility/RTL QA
                                  -> production release gate
```

No downstream work may close an upstream issue by assumption.

## Global Rollback Rule

Every mutable task must have:

1. An approved staging target matching relevant production conditions.
2. A current complete backup and isolated restore proof.
3. Captured pre-change options/files/data and a uniquely identified change set.
4. One-variable-at-a-time execution where technically possible.
5. A tested rollback owner, time limit, trigger, and validation checklist.
6. Evidence that rollback preserves Inquiry First, No Public Pricing, Persian RTL, Mobile First, security, and content/data integrity.

## Global Validation Rule

An issue closes only when:

- Its evidence is current and reproducible.
- All dependencies and required gates pass.
- Validation covers functional, security, data, SEO, mobile/RTL, accessibility, performance, email, cron, logging, and rollback impacts applicable to the issue.
- Founder and required specialist approvals are recorded.
- The repository evidence and decision records are updated after—not before—the successful change.

## Current Roadmap Decision

**GO** for Founder/specialist review and preparation of separately scoped remediation tickets.

**NO-GO** for executing any roadmap item, WooCommerce implementation, Product Data import, production acceptance, indexable launch, or public release.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial consolidated remediation register based on Sprint 02–04 evidence; planning only. |

