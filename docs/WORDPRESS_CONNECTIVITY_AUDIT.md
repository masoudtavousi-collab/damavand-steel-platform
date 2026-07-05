# WordPress Connectivity Audit

## Document Control

- **Document ID:** `docs/WORDPRESS_CONNECTIVITY_AUDIT.md`
- **Status:** Review
- **Authority:** Evidence Record
- **Owner:** Founder
- **Reviewer:** Infrastructure Reviewer, Hosting/Network Reviewer, WordPress Technical Reviewer, Security Reviewer, and Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-05
- **Last Review:** 2026-07-05
- **Review Cycle:** On WordPress.org, outbound HTTP, DNS, TLS, certificate, firewall, port, hosting, or connectivity evidence change
- **Lifecycle:** Review
- **Source of Truth:** Sprint 04A task evidence, [Sprint 02C Audit](AUDIT_REPORT_SPRINT02C.md), and future redacted provider/runtime evidence
- **Dependencies:** [Infrastructure Audit](INFRASTRUCTURE_AUDIT.md), [REST API Diagnostic](REST_API_DIAGNOSTIC.md), and [Sprint 02C Audit](AUDIT_REPORT_SPRINT02C.md)
- **Related Documents:** [Site Health Remediation Plan](SITE_HEALTH_REMEDIATION_PLAN.md), [Platform Architecture](../repository/platform/PLATFORM_ARCHITECTURE.md), [Deployment Access Policy](../repository/config/DEPLOYMENT_ACCESS_POLICY.md), and [Sprint 04A Audit](AUDIT_REPORT_SPRINT04A.md)
- **Traceability:** CP-001 through CP-010, PM-004, PM-007, PM-014, PP-015, PP-019, PG-005 through PG-012, Sprint 02C, and Sprint 04A
- **AI Compatibility:** AI-readable connectivity evidence model; no probe, access, provider action, or configuration change is authorized
- **Approval:** Pending Founder/infrastructure/hosting/security review; no network remediation is approved

## Purpose

Audit the evidence and missing evidence for WordPress.org connectivity, outbound HTTP(S), DNS, SSL/certificates, firewall/ports, and shared-hosting limits without connecting to hosting or changing any setting.

## Executive Finding

WordPress currently reports that it cannot reach `api.wordpress.org`. The exact URL, DNS result, IP address, transport phase, error code/message, HTTP status, and provider action are not supplied. Therefore the failure cannot be attributed to WordPress.org, Iran network routing, Server.ir, DNS, IPv6, TLS, firewall, proxy, PHP cURL, WordPress policy, or a plugin.

The simultaneous REST cURL timeout creates a reasonable shared-connectivity hypothesis. That relationship remains an inference pending same-timestamp transport evidence.

## Connectivity Topology

```text
WordPress/PHP process on shared hosting
  -> WordPress HTTP API
      -> PHP cURL transport
          -> hosting resolver (A/AAAA)
              -> IPv4/IPv6 route
                  -> provider egress firewall/proxy/NAT
                      -> outbound TCP 443
                          -> TLS handshake and CA validation
                              -> api.wordpress.org
                                  -> response through reverse path
```

For self REST traffic, the destination may be the site's public address and return through LiteSpeed/WAF, creating a different path after DNS/route.

## WordPress.org Connectivity

| Concern | Current evidence | Status |
| --- | --- | --- |
| Site Health finding | Unable to access WordPress.org | Verified |
| Target named in Sprint 04A | `api.wordpress.org` | Verified |
| Exact requested URL/path | Not supplied | Pending Evidence |
| Error code/message/timing | Not supplied in current evidence | Pending Evidence |
| DNS result from server | Not supplied | Pending Evidence |
| IPv4/IPv6 connection result | Not supplied | Pending Evidence |
| TLS/HTTP response | Not supplied | Pending Evidence |
| Provider block/restriction | Not supplied | Pending Evidence |
| WordPress/plugin policy | Not supplied | Pending Evidence |
| Root cause | Not established | Pending Evidence |

Impact can include update/package checks, translation/plugin/theme metadata, scheduled/background update tests, and other official-service features. Exact affected functions remain Pending Evidence; no update/package action is authorized.

## Outbound HTTP and HTTPS

### Evidence Available

- WordPress.org access test fails.
- REST self-request times out through cURL after 10 seconds.
- PHP cURL transport is therefore participating in at least the REST failure.
- Shared hosting and no-shell/no-SSH limitations are verified.

### Evidence Missing

- Whether outbound HTTP port 80 and HTTPS port 443 are permitted generally or selectively.
- Whether traffic is rejected, dropped, proxied, rate-limited, filtered by destination, or failing upstream.
- Whether IPv4 succeeds while IPv6 fails.
- Whether DNS, TCP, TLS, first-byte, or transfer consumes the timeout.
- Whether hosting requires a proxy or has WordPress.org-specific restrictions.
- Whether simultaneous requests from the account exceed a resource/connection limit.

No direct outbound probe was made in Sprint 04A.

## DNS Audit

| DNS item | Required evidence | Current status |
| --- | --- | --- |
| Authoritative records for own domain | Current A/AAAA/CNAME/NS/TTL evidence | Pending Evidence |
| Server-side own-domain resolution | Answer, resolver, timing, split-DNS/hosts behavior | Pending Evidence |
| Server-side `api.wordpress.org` resolution | A/AAAA answer and timing | Pending Evidence |
| Resolver health | Configured resolver(s), timeout/retry/failure evidence | Pending Evidence |
| IPv6 preference/fallback | Address selection and route/connect behavior | Pending Evidence |
| DNSSEC/provider filtering | Validation/filter policy if applicable | Pending Evidence; applicability not assumed |

Possible DNS failures include no answer, slow resolver, stale/wrong record, split-horizon mismatch, unreachable IPv6, or provider filtering. None is confirmed.

## SSL and Certificate Audit

### Prior Evidence

- WordPress reported HTTPS true.
- Browser screenshots showed `Not Secure`.
- Let's Encrypt/certificate resolution was pending with Server.ir.

This is prior evidence from Sprint 02C. No refreshed proof shows whether the certificate issue is resolved.

### Evidence Required

- Preferred hostname and current Home URL/Site URL.
- Certificate subject/SAN, issuer, validity, full chain, and hostname match.
- SNI/vhost mapping for public and server-originated requests.
- Redirect chain and HTTP/HTTPS consistency.
- Server trust result from the PHP cURL path.
- PHP cURL SSL backend/version and CA file/path.
- OCSP/revocation or other trust behavior only where the provider/runtime uses it.

An invalid chain commonly produces a certificate-specific error rather than error 28, but stalled DNS/connect/TLS or routing can still end as timeout. Therefore TLS remains relevant and unproven.

## Firewall and WAF Audit

| Control plane | Potential relevance | Evidence required | Status |
| --- | --- | --- | --- |
| Provider egress firewall | May block/drop outbound WordPress.org or self-public IP traffic | Rules/policy/log result at timestamp | Pending Evidence |
| Host firewall | May restrict destination/port/address family | Rules/logs/provider statement | Pending Evidence |
| ModSecurity/WAF | May block/delay inbound loopback REST request | Audit entry/rule/action or no-match evidence | Pending Evidence |
| LiteSpeed security/vhost policy | May route/reject/timeout self request | Listener/vhost/access/error evidence | Pending Evidence |
| CloudLinux/CageFS/LVE | May constrain network/process/resources | Presence/policy/fault counters | Pending Evidence |
| Security plugins | May filter REST/HTTP API | Settings/hooks/logs and later staging isolation | Pending Evidence |

The presence of a cPanel ModSecurity tab in a prior screenshot is not proof that a particular rule is enabled or responsible.

## Ports

| Direction | Port/protocol | Expected use in this diagnostic | Current state |
| --- | --- | --- | --- |
| Outbound | TCP 443 / HTTPS | WordPress.org and HTTPS self request | Pending Evidence |
| Outbound | TCP 80 / HTTP | Redirects or legacy HTTP request paths if used | Pending Evidence; necessity depends on exact URL |
| Inbound | TCP 443 / HTTPS | Public/self-return LiteSpeed listener | Public Admin was visible previously; server-originated path Pending Evidence |
| Inbound | TCP 80 / HTTP | Redirect to HTTPS if configured | Pending Evidence |
| Outbound | DNS to configured resolver | A/AAAA resolution | Pending Evidence |
| SMTP | Provider-specific | Future WP Mail SMTP delivery | Not configured; provider/port Pending Evidence |

No port test or firewall change was performed.

## Hosting Limitations

Verified:

- Shared hosting.
- No shell access.
- SSH `NO-GO` confirmed by Server.ir.
- WordPress path is reported but direct filesystem access was not used in Sprint 04A.

Consequences:

- Codex cannot use shell/WP-CLI/server cURL/DNS/log tools through a new method.
- Provider support or existing approved cPanel/Admin evidence is required for server-side diagnostics.
- Full logs, network traces, PHP extension data, and CloudLinux/WAF controls may be provider-only.
- Plugin deactivation/testing on production is unsafe and unauthorized.

Unknown:

- Hosting plan limits, CloudLinux, CageFS, LVE, outbound policy, WAF rules, log retention/access, proxy, DNS resolver, IPv6 support, certificate automation, cron model, backup/restore capability.

## WordPress HTTP Policy

Read-only evidence is needed for:

- External-request blocking policy/constants.
- Proxy policy/constants.
- HTTP API filters/transports/timeouts.
- Host allow/block lists.
- MU-plugins/drop-ins/hosting plugins that modify requests.
- The Iran network optimizer's exact behavior.

Do not copy secrets or full `wp-config.php` into the repository. Redacted relevant values or provider statements are sufficient.

## Relationship to Other Findings

| Finding | Possible connectivity relationship | Current conclusion |
| --- | --- | --- |
| REST cURL 28 | May share DNS/route/TLS/egress path | Inference; correlate timestamps/transport phases |
| Failed scheduled event | May depend on loopback/outbound HTTP or be independent | Pending event details |
| Background updates | Likely affected by WordPress.org access | Site Health warning supports impact; exact failure Pending |
| SMTP incomplete | Separate protocol/provider setup; may later encounter egress limits | No shared cause established |
| Rank Math reconnect | May depend on stable URL/TLS/outbound access | Connection details Pending |
| Coming Soon | Application/SEO state, not network cause | Expected; preserve |

## Provider Evidence Request — Read-Only

Ask Server.ir through the existing support channel to confirm, without changing configuration:

1. Server-side DNS resolution/timing for own hostname and `api.wordpress.org`, including A/AAAA.
2. IPv4/IPv6 route and connection outcome.
3. Outbound TCP 443/HTTP(S) policy and any destination restrictions.
4. Loopback/hairpin policy for the account's public hostname/IP.
5. Firewall/WAF/ModSecurity action at the exact failure timestamp.
6. LiteSpeed vhost/listener/access/error result for the REST request.
7. CloudLinux/CageFS/LVE presence and fault counters at the timestamp.
8. PHP cURL/SSL/CA versions/paths and effective timeout settings.
9. Current certificate chain/SNI/hostname/trust state.
10. Whether a provider proxy or supported diagnostic method is required.

The request must contain no credentials and must not authorize changes.

## Risk Assessment

| Risk | Level | Reason |
| --- | --- | --- |
| Official update connectivity unavailable | Critical | Security/package/background-update reliability unresolved |
| Shared network cause affects REST and external services | Critical | Multiple core paths may be impacted; root cause unknown |
| TLS/URL identity unstable | High | Prior certificate conflict and Rank Math URL-change state |
| Provider-only evidence inaccessible | High | No shell/SSH; diagnosis depends on support/existing interfaces |
| Wrong remediation without phase evidence | High | Could cause outage or weaken security |
| SMTP outbound behavior | Medium/High | Setup incomplete; future inquiry delivery requires proof |

## Current Decision

Root cause: **Pending Evidence**.

**GO** for provider/WordPress read-only evidence collection through existing approved methods.

**NO-GO** for firewall, DNS, TLS, PHP, WordPress, plugin, SMTP, or hosting changes.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-05 | Initial Sprint 04A WordPress connectivity audit; no probe or remediation performed. |

## Navigation

- [Infrastructure Audit](INFRASTRUCTURE_AUDIT.md)
- [REST API Diagnostic](REST_API_DIAGNOSTIC.md)
- [Site Health Remediation Plan](SITE_HEALTH_REMEDIATION_PLAN.md)
- [Sprint 04A Audit](AUDIT_REPORT_SPRINT04A.md)
