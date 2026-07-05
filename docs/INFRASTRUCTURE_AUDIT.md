# Damavand Steel Infrastructure Audit

## Document Control

- **Document ID:** `docs/INFRASTRUCTURE_AUDIT.md`
- **Status:** Review
- **Authority:** Evidence Record
- **Owner:** Founder
- **Reviewer:** Infrastructure Reviewer, WordPress Technical Reviewer, Security Reviewer, and Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On refreshed Site Health, provider evidence, topology, DNS/TLS/network/runtime/plugin change, or diagnostic result
- **Lifecycle:** Review
- **Source of Truth:** Sprint 04A task-provided current findings, [Sprint 02C evidence](AUDIT_REPORT_SPRINT02C.md), and repository architecture/Platform constraints
- **Dependencies:** [Sprint 02C Audit](AUDIT_REPORT_SPRINT02C.md), [Platform Architecture](../repository/platform/PLATFORM_ARCHITECTURE.md), [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), and [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md)
- **Related Documents:** [REST API Diagnostic](REST_API_DIAGNOSTIC.md), [WordPress Connectivity Audit](WORDPRESS_CONNECTIVITY_AUDIT.md), [Site Health Remediation Plan](SITE_HEALTH_REMEDIATION_PLAN.md), and [Sprint 04A Audit](AUDIT_REPORT_SPRINT04A.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, WP-FC-001 through WP-FC-005, PM-001 through PM-016, PG-005 through PG-012, Sprint 02C evidence, and Sprint 04A
- **AI Compatibility:** AI-readable evidence audit; hypotheses, observations, inferences, and missing evidence are explicitly separated
- **Approval:** Pending Founder/infrastructure/security/WordPress review; no remediation or runtime change is authorized

## Executive Summary

The current evidence confirms two critical connectivity symptoms on `damavandsteel.com`:

1. A WordPress REST API test targeting `/wp-json/wp/v2/` reports cURL error 28 after 10,000 ms.
2. WordPress reports that it cannot reach `api.wordpress.org`.

cURL error 28 proves a timeout occurred; it does not identify whether time was spent in DNS resolution, TCP connection, TLS negotiation, server processing, or response transfer. The coexistence of a self/REST-path timeout and WordPress.org connectivity failure makes shared DNS/outbound-network/TLS/hosting controls a high-priority investigation path, but this is an inference, not a proven root cause.

SMTP is not configured, Rank Math reports a Site URL change with reconnection pending, and Coming Soon mode is enabled intentionally. These are separate operational/SEO findings unless future evidence demonstrates a shared cause.

No infrastructure root cause can be confirmed from the current evidence. WooCommerce implementation and production acceptance remain `NO-GO`. A read-only evidence-collection sequence is `GO` using only already approved access/support channels; no setting, file, plugin, database, server, or hosting change is authorized.

## Evidence Vocabulary

| Label | Meaning |
| --- | --- |
| `Verified` | Directly stated in supplied task evidence or captured Site Health/plugin evidence |
| `Prior Verified` | Verified in Sprint 02C but requires refreshed evidence before being treated as current |
| `Inference` | Reasoned relationship consistent with verified symptoms; not a fact/root cause |
| `Possible Cause` | Technically plausible hypothesis requiring targeted evidence |
| `Pending Evidence` | Evidence has not been supplied; absence/presence is not inferred |
| `Not Authorized` | Would require a separate approved mutation/connection task |

## Current Topology

```text
Browser / Visitor
  -> Public DNS for damavandsteel.com
      -> Shared hosting (Server.ir evidence)
          -> LiteSpeed web server
              -> PHP 7.4.33
                  -> WordPress 7.0 (fa_IR, timezone +03:30)
                      -> MariaDB 10.6.19
                      -> 13 captured active plugins

WordPress HTTP API / cURL
  -> Self/loopback path to damavandsteel.com/wp-json/wp/v2/
  -> External outbound HTTPS path to api.wordpress.org
```

Potential but unverified infrastructure layers include provider DNS resolvers, IPv4/IPv6 routing, CloudLinux controls, LiteSpeed virtual-host/listener policy, ModSecurity/WAF, server firewall/egress policy, proxy policy, CA trust store, and hosting resource limits.

### Verified Runtime Baseline

| Concern | Evidence state | Limitation |
| --- | --- | --- |
| Domain | `damavandsteel.com` | Production/staging classification remains Pending Evidence |
| WordPress | `7.0` | Exact build/checksum/update policy Pending Evidence |
| Language/timezone | `fa_IR`, `+03:30` | Named timezone and PHP/database alignment Pending Evidence |
| Theme | Blocksy `2.1.46` active | Blocksy Pro packaging/license/configuration Pending Evidence |
| Web server | LiteSpeed | Virtual host, listener, cache, timeout, WAF/module configuration Pending Evidence |
| PHP | `7.4.33` | SAPI, effective INI, extensions, cURL/SSL versions, CA bundle, limits Pending Evidence |
| Database | MariaDB `10.6.19` | Health, charset, privileges, connection/security, backup Pending Evidence |
| WordPress path | `/home/centrals/damavandsteel.com` | Document-root mapping, ownership, isolation Pending Evidence |
| Hosting | Shared hosting; shell unavailable | Plan, CloudLinux/network controls, logs/support capabilities Pending Evidence |
| SSH | `NO-GO`, Server.ir confirmed | No shell/WP-CLI diagnostic path |
| Plugins | 13 captured active | Fresh inventory, MU-plugins, drop-ins, exact settings Pending Evidence |

The local repository `public/` scaffold is not the live hosting filesystem and must not be used to infer live plugin/runtime state.

## Current Plugin Interaction Surface

| Captured active component | Version | Connectivity relevance | Evidence status |
| --- | --- | --- | --- |
| Elementor | `4.1.4` | May consume REST/Admin HTTP functions; not evidence of cause | Possible interaction only |
| FluentCRM | `3.1.6` | May use cron, email, and outbound services | Configuration/jobs Pending Evidence |
| Kadence Security Basic | `10.0.2` | Security rules may restrict REST/requests | Rule/log evidence Pending |
| Limit Login Attempts Reloaded | `3.3.1` | Login protection overlap; REST relevance not established | Configuration Pending |
| Rank Math SEO | `1.0.271.1` | Reports Site URL change; may use outbound account/services and REST | Reconnect/configuration evidence Pending |
| Social Chat | `8.5.5` | External service/contact integration possible | Configuration/network behavior Pending |
| UpdraftPlus | `1.26.5` | May use cron/outbound storage; presence is not recovery evidence | Schedule/log/restore evidence Pending |
| Variation Swatches for WooCommerce | `2.3.0` | WooCommerce/Admin interaction; no root-cause evidence | Configuration Pending |
| WP Mail SMTP | `4.8.0` | SMTP/provider connectivity; setup confirmed incomplete | Separate known issue |
| WPForms Lite | `1.10.2` | Form/REST/email interaction possible | Use/configuration Pending |
| بهینه‌ساز شبکه ایران | `3.1.35` | Its stated purpose relates to external WordPress requests; exact routing/filter behavior is highly relevant | Configuration/log/code-path evidence Pending; no blame inferred |
| WooCommerce | `10.8.1` | Uses REST/background/HTTP capabilities | No product implementation; cause unproven |
| ووکامرس فارسی | `10.0.4` | WooCommerce localization/integration | Connectivity relevance unproven |

Gravity Forms and LiteSpeed Cache were absent from the captured 13-plugin inventory. LiteSpeed server software is present; this must not be confused with the prohibited LiteSpeed Cache plugin.

## Known Issues

| ID | Issue | Evidence | Current interpretation |
| --- | --- | --- | --- |
| INF-01 | REST API cURL error 28 after 10,000 ms at `/wp-json/wp/v2/` | Sprint 04A task evidence | Verified timeout symptom; root cause Pending Evidence |
| INF-02 | WordPress cannot reach `api.wordpress.org` | Site Health/task evidence | Verified outbound connectivity symptom; exact failure phase Pending Evidence |
| INF-03 | SMTP not configured | Site Health and WP Mail SMTP evidence | Verified incomplete email setup; delivery untrusted |
| INF-04 | Rank Math Site URL changed; reconnect pending | Sprint 04A task evidence | Verified plugin/account state; exact URL transition and impact Pending Evidence |
| INF-05 | Coming Soon enabled | Sprint 04A task evidence | Expected current state; not a defect by itself |
| INF-06 | Prior public TLS state unresolved | Sprint 02C browser `Not Secure` versus WordPress HTTPS true | Prior Verified; current certificate/chain status needs refresh |
| INF-07 | Scheduled event failure/background-update warning | Sprint 02C Site Health | Prior Verified; event/test details Pending Evidence |
| INF-08 | Persistent object-cache recommendation | Sprint 02C Site Health | Recommendation only; not evidence of REST root cause or permission to install cache |

## Possible Root Causes

No item below is a confirmed cause.

| Candidate cause | Why it is relevant | Evidence available | Evidence missing | Investigation priority |
| --- | --- | --- | --- | --- |
| Shared outbound HTTPS restriction | Both self REST and WordPress.org paths may require server-originated HTTP(S) | Two connectivity symptoms coexist | Provider egress policy, destination/port logs, connection timing | Critical |
| Internal DNS resolution failure/latency | Server must resolve its own domain and `api.wordpress.org` | Timeout is compatible with DNS delay | Server resolver results/timing, resolvers, `/etc/hosts`, split DNS | Critical |
| Broken IPv6 preference/path | AAAA resolution with unavailable IPv6 can delay/fail before IPv4 fallback | No IPv4/IPv6 diagnostic supplied | A/AAAA answers from host, route/preference/connect timing | High |
| Loopback/hairpin routing restriction | Self-request may leave the host and return through public address/WAF | REST self-path times out | Internal resolution target, public/private routing, provider hairpin policy | Critical |
| Public TLS/certificate/chain/SNI problem | Prior browser evidence showed `Not Secure`; HTTPS self-request requires valid trust/hostname | Prior TLS inconsistency | Current chain, hostname, expiry, SNI, CA bundle, handshake timing | Critical |
| Server firewall/egress ACL | Outbound 443 may be denied/dropped | WordPress.org failure | Provider firewall rules/logs and allowed destinations/ports | Critical |
| ModSecurity/WAF rule | Inbound loopback REST may be blocked/delayed | cPanel ModSecurity interface was visible in prior screenshot only | Active rules, audit event ID/log, request action | High |
| LiteSpeed virtual-host/listener/timeout policy | Server receives REST path and may handle internal/public requests differently | LiteSpeed verified | vhost/listener/timeout/rewrite/error/access logs | High |
| CloudLinux/CageFS/LVE/network restriction | Shared hosting may constrain resources/network/processes | Shared hosting verified | CloudLinux presence, LVE faults, process/connection limits, provider policy | High |
| WordPress HTTP API policy/proxy constants | `WP_HTTP_BLOCK_EXTERNAL`, proxy settings, filters, or transport policy can alter requests | WordPress HTTP API produced cURL error | Redacted constants/filters/proxy configuration and HTTP API debug trace | High |
| cURL/OpenSSL/CA configuration | cURL transport is active; version, SSL backend, protocol support, and trust path are unknown | cURL error proves cURL transport participated | PHP extension list, cURL/SSL versions, CA file/path, errors/timings | High |
| Security/optimization plugin filtering | Security or network optimizer can filter REST/outbound requests | Relevant plugins captured active | Settings, hooks, logs, controlled staging isolation evidence | High |
| Slow plugin/theme callback on REST bootstrap | REST request loads WordPress/plugins and may stall before response | 13 plugins active | Per-request timing/profile, logs, safe staging isolation | Medium |
| Database/resource saturation | PHP/DB/resource wait could exceed 10 seconds | Shared hosting and old baseline values known | CPU/RAM/I/O/LVE/DB slow query/error metrics at timestamp | Medium |
| Cron lock/failure interaction | Failed scheduled event may share network/resource cause | Prior scheduled-event warning | Event identity, owner, timestamp, cron mode/logs | Medium |
| Object-cache absence/problem | Site Health recommends persistent cache; a drop-in may also be stale/misconfigured | Recommendation only | `object-cache.php`/drop-in inventory, cache service/status | Low for root cause; inspect for completeness |
| REST route/application permission error | Route/plugin/authentication may fail | Endpoint known | Exact response/timing; a timeout differs from immediate 4xx/5xx but does not exclude application stall | Medium |

## Architecture Verification

| Architecture concern | Audit result |
| --- | --- |
| Platform → Repository → Engine → Runtime → Website separation | Preserved; audit treats live WordPress as replaceable Runtime evidence, not repository authority |
| Product Engine/Product Data | Unchanged and unrelated to root-cause diagnosis |
| Plugin First/Configuration First | Preserved; no plugin/custom-code recommendation is selected before evidence |
| Inquiry First/No Public Pricing | Preserved; WooCommerce implementation remains blocked |
| Mobile First/Persian RTL | No change; future remediation must regress these behaviors |
| Prohibited components | No Gravity Forms or LiteSpeed Cache action; no custom theme or AI feature |
| Admin manageability | Shared-host/no-shell constraint requires future diagnostics/remediation to remain provider/Admin-manageable where possible |

## Network Topology Verification Status

| Layer | Status |
| --- | --- |
| Public DNS A/AAAA and authoritative records | Pending Evidence |
| Internal server DNS resolution and resolver health | Pending Evidence |
| IPv4/IPv6 routes and fallback | Pending Evidence |
| Outbound HTTP/HTTPS policy | Pending Evidence |
| Hairpin/loopback path to own hostname | Pending Evidence |
| TLS chain/SNI/trust | Prior issue; current status Pending Evidence |
| LiteSpeed listener/vhost/rewrite/logs | Pending Evidence |
| ModSecurity/WAF | Pending Evidence |
| CloudLinux/LVE | Pending Evidence |
| Reverse proxy/CDN | Pending Evidence; none assumed |
| WordPress HTTP API proxy/filter policy | Pending Evidence |

## Security Assumptions Audit

- Security-plugin presence does not prove correct configuration or protection.
- Inaccessibility/timeouts do not prove firewall security.
- Disabling a WAF/security plugin is not authorized and is not an acceptable first diagnostic step on production.
- Provider logs and redacted configuration evidence should precede any controlled isolation test.
- Credentials, certificate private keys, customer data, full config files, and raw sensitive logs must not enter the repository.
- Any future plugin/theme/core/PHP change requires backup/restore and staging evidence.

## Production Readiness

| Gate | Status | Reason |
| --- | --- | --- |
| REST/API health | Blocked | cURL timeout root cause unresolved |
| Official update/package connectivity | Blocked | `api.wordpress.org` unreachable |
| TLS | Pending refreshed evidence | Prior `Not Secure`/certificate issue unresolved in repository evidence |
| Email delivery | Blocked | SMTP incomplete/unverified |
| SEO account/site identity | Blocked | Rank Math reconnect pending; URL transition evidence missing |
| Cron/background updates | Blocked/Pending Evidence | Prior Site Health findings lack details |
| Backup/restore | Blocked/Pending Evidence | UpdraftPlus presence is not restore proof |
| Runtime compatibility | Blocked/Pending Evidence | Exact supported PHP/component compatibility not approved |
| Plugin interaction risk | Pending Evidence | Settings/MU/drop-ins/logs/change history absent |
| WooCommerce implementation | `NO-GO` | Infrastructure/production gates unresolved |

## Risk Analysis

| Risk | Impact | Current exposure | Control before change |
| --- | --- | --- | --- |
| Wrong root-cause remediation | Outage, lockout, hidden defect | High uncertainty | Evidence-first staged diagnosis |
| Update/connectivity failure | Security/update/package integrity risk | Confirmed symptom | Provider/network/root-cause evidence |
| REST failure | Editor, WooCommerce, plugin/API workflow failures | Confirmed symptom | Restore REST/loopback health before implementation |
| TLS inconsistency | Trust, API, SEO, login/session risk | Prior verified; current unknown | Current certificate/chain/URL validation |
| Email failure | Lost inquiry/admin notifications | SMTP incomplete | Approved provider/config and delivery tests later |
| Security-plugin overlap | Conflicting request rules/lockout | Possible | Settings/ownership/log review; staging isolation only later |
| Shared-host limitations | No shell/log/control access | Verified no SSH/shell | Provider-led evidence and supported Admin/cPanel path |
| No proven recovery | Unsafe remediation | Pending Evidence | Backup integrity and isolated restore proof |
| Premature WooCommerce work | Compounds unstable foundation | Implementation requested later | Maintain infrastructure `NO-GO` |

## Priority Matrix

| Priority | Investigation | Expected decision value | Status |
| --- | --- | --- | --- |
| P0 Critical | Capture exact Site Health REST/WordPress.org diagnostic details and timestamps | Identifies timeout phase/target and confirms current symptoms | Pending Evidence |
| P0 Critical | Provider confirms internal/external DNS, A/AAAA, outbound 443, loopback/hairpin, firewall/WAF actions | Tests shared network-path hypothesis | Pending Evidence |
| P0 Critical | Refresh public/internal TLS chain, hostname, SNI, validity, redirects, Home/Site URL evidence | Resolves prior TLS inconsistency and self-HTTPS dependency | Pending Evidence |
| P0 Critical | Obtain backup/restore evidence before any future mutation | Establishes safe remediation gate | Pending Evidence |
| P1 High | Capture PHP cURL/SSL/CA/extension and WordPress HTTP API policy evidence | Tests transport/configuration hypothesis | Pending Evidence |
| P1 High | Capture LiteSpeed/ModSecurity/CloudLinux logs around failed request | Tests server/WAF/resource hypotheses | Pending Evidence |
| P1 High | Inventory MU-plugins/drop-ins and relevant plugin settings/logs/change history | Tests application/filter hypotheses | Pending Evidence |
| P1 High | Identify failed cron event/background-update details | Determines shared or independent symptom | Pending Evidence |
| P2 Medium | Complete SMTP design/configuration/testing under separate approval | Restores reliable inquiry/admin email | Not Authorized in audit |
| P2 Medium | Reconcile Site URL and Rank Math connection after URL/TLS stability | Restores SEO account state | Blocked by URL/TLS evidence |
| P3 Low | Preserve Coming Soon until Founder launch gate | Avoids premature indexation | Expected/No change |
| P3 Low | Evaluate object cache only after root cause and approved capability selection | Performance consideration, not current fix | Deferred; LiteSpeed Cache prohibited |

## Evidence Available

- Current task-provided REST endpoint, cURL error 28, and 10,000 ms timeout.
- Current task-provided WordPress.org, SMTP, Rank Math, and Coming Soon findings.
- Sprint 02C WordPress/runtime/theme/server/PHP/database/path/hosting/SSH baseline.
- Sprint 02C 13-plugin captured active inventory and Site Health screenshots.
- Prior browser `Not Secure` and unresolved Let's Encrypt evidence.
- Repository architecture, Platform, Product Engine, plugin, security, validation, and no-change constraints.

## Evidence Missing

- Refreshed complete Site Health debug text for both critical findings.
- Request timestamps, resolved IPs, cURL phase timings, HTTP response/error body, WordPress debug trace.
- Public and server-side A/AAAA/DNS resolver evidence; IPv4/IPv6 routing/fallback.
- Provider outbound connection/firewall/loopback/hairpin policy and logs.
- ModSecurity audit events, LiteSpeed access/error logs, CloudLinux/LVE fault evidence.
- Current certificate chain, hostname/SNI/expiry/trust, Home URL, Site URL, redirect path.
- PHP SAPI/extensions, cURL/SSL versions, CA bundle/path, effective timeouts/limits.
- Redacted WordPress HTTP API proxy/block/filter constants and related plugin filters.
- MU-plugin/drop-in inventory, `object-cache.php` state, cron details, recent-change timeline.
- Relevant plugin settings/logs without secrets/personal data.
- Backup schedule/scope/destination/success and isolated restore proof.
- SMTP provider/sender/DNS/credential custody/delivery test.
- Rank Math old/new URL/account/reconnect error details.

## Recommended Investigation Order

1. Freeze changes and record a common diagnostic timestamp/timezone.
2. Capture expanded Site Health text for REST, WordPress.org, cron, background updates, SMTP, and URL/SEO state without changing anything.
3. Confirm current Home/Site URL and public TLS evidence through existing approved Admin/support evidence paths; redact sensitive details.
4. Ask Server.ir support to provide read-only DNS A/AAAA/resolver, outbound HTTPS, loopback/hairpin, firewall/WAF, LiteSpeed, ModSecurity, CloudLinux/LVE, and relevant log evidence for the timestamp.
5. Obtain redacted PHP cURL/SSL/CA/extension and WordPress HTTP API policy evidence through existing supported channels.
6. Inventory MU-plugins/drop-ins and relevant plugin settings/change history read-only.
7. Correlate both connectivity failures: shared cause versus independent failures.
8. Define a separate staging/backup/restore-controlled isolation plan only if evidence cannot isolate the cause.
9. Obtain Founder approval before any remediation, plugin isolation, setting change, PHP change, or provider action.
10. Re-run Site Health and regression gates only after separately authorized remediation.

## Current Decision

**GO** for documentation, provider support follow-up, and read-only evidence collection through already approved methods.

**NO-GO** for remediation, WooCommerce implementation, production acceptance, updates, plugin changes, server/configuration changes, or new hosting access methods.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial Sprint 04A evidence-based infrastructure audit; no root cause claimed and no runtime change. |

## Navigation

- [REST API Diagnostic](REST_API_DIAGNOSTIC.md)
- [WordPress Connectivity Audit](WORDPRESS_CONNECTIVITY_AUDIT.md)
- [Site Health Remediation Plan](SITE_HEALTH_REMEDIATION_PLAN.md)
- [Sprint 04A Audit](AUDIT_REPORT_SPRINT04A.md)
