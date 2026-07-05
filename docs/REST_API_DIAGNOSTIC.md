# WordPress REST API Diagnostic

## Document Control

- **Document ID:** `docs/REST_API_DIAGNOSTIC.md`
- **Status:** Review
- **Authority:** Supporting
- **Owner:** Founder
- **Reviewer:** WordPress Technical Reviewer, Infrastructure Reviewer, Security Reviewer, and Quality Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On REST error, WordPress HTTP API, DNS/TLS/network/server/plugin evidence, diagnostic result, or remediation change
- **Lifecycle:** Review
- **Source of Truth:** [Infrastructure Audit](INFRASTRUCTURE_AUDIT.md), Sprint 04A task evidence, Sprint 02C Site Health evidence, and official runtime evidence supplied later
- **Dependencies:** [Infrastructure Audit](INFRASTRUCTURE_AUDIT.md), [Sprint 02C Audit](AUDIT_REPORT_SPRINT02C.md), and [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md)
- **Related Documents:** [WordPress Connectivity Audit](WORDPRESS_CONNECTIVITY_AUDIT.md), [Site Health Remediation Plan](SITE_HEALTH_REMEDIATION_PLAN.md), and [Platform Architecture](../repository/platform/PLATFORM_ARCHITECTURE.md)
- **Traceability:** CP-001 through CP-010, WP-FC-001 through WP-FC-005, PM-004, PM-007, PG-005 through PG-012, and Sprint 04A
- **AI Compatibility:** AI-readable diagnostic model; possible causes are not facts and no automated test/change is authorized
- **Approval:** Pending Founder/infrastructure/WordPress/security review; checklist execution must remain within separately approved read-only access

## Purpose

Explain the REST request lifecycle, distinguish loopback/HTTP API/server/plugin failure domains, and define a non-mutating investigation checklist for cURL error 28 at `/wp-json/wp/v2/`.

## Verified Symptom

| Property | Value | Meaning |
| --- | --- | --- |
| Endpoint | `/wp-json/wp/v2/` | Task-provided REST target/path |
| Transport result | cURL error 28 | A timeout occurred |
| Timeout | 10,000 ms | Request did not complete within the reported limit |
| Root cause | Pending Evidence | Error 28 alone does not identify DNS/TCP/TLS/server/application phase |
| Current severity | Critical Site Health / Infrastructure blocker | REST health must be restored before WooCommerce implementation |

## REST Request Lifecycle

```text
WordPress Site Health / caller
  -> WordPress HTTP API
      -> transport selection (cURL observed)
          -> DNS resolution (A/AAAA, internal/external resolver)
              -> route/firewall/loopback or public hairpin
                  -> TCP connection to web listener
                      -> TLS/SNI/certificate/CA validation for HTTPS
                          -> LiteSpeed virtual host/rewrite/WAF/ModSecurity
                              -> PHP bootstrap
                                  -> WordPress Core + MU/drop-ins + theme/plugins
                                      -> REST route dispatch/authentication
                                          -> database/callback work
                                              -> HTTP response
                                                  -> WordPress HTTP API result
```

The current evidence does not locate the timeout within this lifecycle.

## Loopback Explanation

A loopback request occurs when WordPress initiates an HTTP request back to its own site. The request may:

- Resolve the public hostname to the public IPv4/IPv6 address.
- Leave the PHP process/host and return through the hosting network, firewall, TLS listener, and WAF.
- Use split/internal DNS or an internal route if the provider configures one.
- Fail even though an external browser can load Admin, because the server-originated path differs from the visitor path.

The supplied Site Health error must be expanded to confirm exact request context and URL. Calling it “loopback failure” before that evidence would be an inference.

## WordPress HTTP API

The WordPress HTTP API is the application abstraction used for server-originated HTTP(S) requests. It can be affected by:

- Transport availability and cURL/SSL/CA configuration.
- DNS/IPv4/IPv6/network/firewall/proxy behavior.
- WordPress constants/policies that block or proxy external requests.
- Filters added by Core, MU-plugins, drop-ins, plugins, hosting integrations, or security/optimization tools.
- Timeout values and request arguments.
- Target server/TLS/application response time.

cURL error 28 confirms cURL participated in the failing request. It does not prove that the cURL extension/version/trust configuration is healthy.

## Potential Blockers

| Layer | Potential blocker | Typical evidence | Current state |
| --- | --- | --- | --- |
| DNS | Slow/failing resolver, wrong A/AAAA, stale/split DNS | Host-side resolution answers/timings | Pending Evidence |
| IPv6 | AAAA preferred but route/listener unavailable | A/AAAA plus IPv4/IPv6 connect timing | Pending Evidence |
| Network | Egress 443 denied/dropped, hairpin unavailable | Provider firewall/connection logs/policy | Pending Evidence |
| TLS | Invalid/incomplete chain, hostname/SNI mismatch, stale CA, handshake delay | Current chain plus cURL TLS phase/error | Prior risk; current Pending |
| LiteSpeed | Wrong vhost/listener, timeout, rewrite, request routing | Access/error log and vhost evidence | Pending Evidence |
| ModSecurity/WAF | Rule drops/delays loopback REST request | Audit ID/rule/action at timestamp | Pending Evidence |
| CloudLinux/LVE | Resource/process/network limit | Fault counters/resource log | Pending Evidence |
| WordPress policy | External blocking/proxy/filter policy | Redacted constants/filter inventory | Pending Evidence |
| REST routing | Route/auth/permission/callback behavior | Exact response/error when request completes | Timeout prevents conclusion |
| Plugin/theme | Security/optimizer/filter or slow callback | Logs/timing and approved staging isolation | Pending Evidence |
| Database/resources | Slow bootstrap/query/I/O | PHP/LiteSpeed/DB/LVE timing/errors | Pending Evidence |
| Object cache/drop-in | Misconfigured/stale drop-in/service | Drop-in/service inventory/logs | Pending Evidence; recommendation alone proves nothing |

## Typical Shared-Hosting Causes

These are general diagnostic categories, not claims about Server.ir:

- Provider blocks/drops selected outbound destinations or ports.
- Internal hostname resolves to an address that cannot hairpin back to the same account/server.
- IPv6 DNS exists without a usable route/listener.
- Shared resolver latency/failure.
- WAF/ModSecurity rules treat server-originated REST requests as suspicious.
- LiteSpeed/vhost/SNI/listener mapping differs between internal and public paths.
- CloudLinux/LVE process, CPU, memory, I/O, or entry-process limits delay PHP.
- CA trust store or PHP cURL/SSL backend is outdated/misconfigured.
- Account isolation/CageFS hides an expected CA/config path.
- Provider proxy or network policy interferes with WordPress.org connectivity.

Provider evidence is required before assigning any of these causes.

## Plugin Causes

Possible plugin-side mechanisms include:

- Security plugin blocks REST routes or self-originated requests.
- Network optimization plugin rewrites/short-circuits WordPress HTTP API destinations.
- SEO/account plugin adds REST callbacks or outbound account validation.
- CRM/form/backup plugins add slow hooks, cron work, or external requests during bootstrap.
- WooCommerce/localization/swatches plugins add REST routes or initialization overhead.
- MU-plugin or drop-in changes HTTP API/REST behavior outside the visible plugin list.

No plugin is identified as the cause. Production deactivation, deletion, update, replacement, or settings change is prohibited in Sprint 04A. Any future isolation must occur in an approved recoverable staging environment after logs/config evidence is reviewed.

## Infrastructure Causes

- DNS/route/firewall/egress/hairpin.
- TLS/SNI/certificate/CA/OpenSSL/cURL.
- LiteSpeed listener/vhost/rewrite/timeout.
- ModSecurity/WAF.
- CloudLinux/LVE/CageFS/resource limits.
- Database/PHP process/I/O saturation.
- Hosting proxy/NAT/restriction.

The shared failure with `api.wordpress.org` makes these categories high-value to investigate first, not proven more likely.

## Cron and Object Cache

- A failed scheduled event may be another symptom of HTTP/network/resource/plugin problems or an independent event-specific failure. Event identity and execution method are missing.
- Persistent object-cache recommendation is not evidence that lack of object cache caused the REST timeout.
- A stale/misconfigured `object-cache.php` drop-in could affect runtime behavior, but drop-in/service evidence is missing.
- LiteSpeed Cache remains prohibited; Site Health's cache recommendation is not permission to install it.

## Risk Level

**Critical for implementation readiness.** REST failure can affect WordPress Admin/editor behavior, WooCommerce, plugin APIs, scheduled/background jobs, integrations, and future inquiry workflows. Impact on each feature is Pending Evidence; no feature-specific outage is asserted without testing.

## Investigation Checklist — Read-Only

### Capture the Exact Failure

- [ ] Record Site Health timestamp and timezone.
- [ ] Capture complete expanded REST error text, exact URL, method, status/error data, and test context.
- [ ] Confirm whether the timeout is reproducible and whether it is constant at 10,000 ms.
- [ ] Capture the complete WordPress.org connectivity error at the same time.
- [ ] Record current Home URL/Site URL and preferred hostname without changing them.

### DNS and Address Family

- [ ] Obtain provider-supplied server-side A/AAAA results for own hostname and `api.wordpress.org`.
- [ ] Record resolver addresses, resolution timing, TTL, split-DNS/hosts-file behavior.
- [ ] Compare IPv4 and IPv6 route/connect results without changing DNS.
- [ ] Confirm the own-domain address maps to the correct LiteSpeed virtual host/account.

### Network and Hosting

- [ ] Obtain Server.ir outbound HTTP/HTTPS and loopback/hairpin policy.
- [ ] Obtain firewall/WAF connection/action evidence for the timestamp.
- [ ] Confirm whether outbound TCP 443 to WordPress.org and own hostname is permitted.
- [ ] Obtain CloudLinux/LVE/CageFS presence and fault/resource evidence.

### TLS and Transport

- [ ] Capture current certificate chain, hostname/SNI, issuer, validity, and trust status.
- [ ] Obtain PHP cURL version, SSL backend/version, protocols, and CA file/path evidence.
- [ ] Capture timing phase if provider tools expose DNS/connect/TLS/first-byte safely.
- [ ] Confirm certificate/chain behavior from the server-originated path.

### LiteSpeed/WAF/Application

- [ ] Obtain LiteSpeed access/error entries for the exact request.
- [ ] Obtain ModSecurity audit entry/rule/action or explicit no-match evidence.
- [ ] Inventory redacted WordPress HTTP API proxy/block constants and filters.
- [ ] Inventory MU-plugins, drop-ins, and `object-cache.php` state.
- [ ] Capture PHP/WordPress fatal/error logs for the timestamp, redacted.
- [ ] Capture relevant plugin settings/logs/change timeline without changing them.

### Correlation

- [ ] Determine whether REST, WordPress.org, cron, background update, TLS, and Rank Math URL findings began together.
- [ ] Separate shared infrastructure failures from independent configuration issues.
- [ ] Record the narrowest evidence-supported root cause and affected layers.

## Future Controlled Isolation — Not Authorized Now

Only if read-only evidence is insufficient, a later task may define:

- Verified backup and isolated restore.
- Staging clone matching runtime/network conditions.
- One-variable-at-a-time plugin/theme/drop-in/network isolation.
- Baseline and post-test REST/outbound/cron/inquiry/no-price/security/RTL/mobile checks.
- Rollback and evidence retention.

No production plugin deactivation or configuration experiment is authorized by this document.

## Current Diagnostic Decision

Root cause: **Pending Evidence**.

**GO** for read-only evidence collection through existing approved channels.

**NO-GO** for remediation or WooCommerce implementation.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial Sprint 04A REST API lifecycle and evidence checklist; no diagnostic request or change executed. |

## Navigation

- [Infrastructure Audit](INFRASTRUCTURE_AUDIT.md)
- [WordPress Connectivity Audit](WORDPRESS_CONNECTIVITY_AUDIT.md)
- [Site Health Remediation Plan](SITE_HEALTH_REMEDIATION_PLAN.md)
- [Sprint 04A Audit](AUDIT_REPORT_SPRINT04A.md)
