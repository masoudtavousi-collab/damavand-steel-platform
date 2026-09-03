# PP-01 Public Homepage V1 Runtime Plan v1.0

## Document Control

- **Purpose:** Prepare the future PP-02 execution gate; execute nothing
- **Status:** `REVIEW / PRE-RUNTIME PLAN`
- **Classification:** `NOT_DEPLOYED / NOT_PUBLISHED / NONAUTHORITATIVE FOR EXECUTION`
- **Authority:** [PP-01 Scope](PP_01_PUBLIC_HOMEPAGE_V1_READINESS_SCOPE_V1.0.md)
- **Design input:** [Public Homepage V1 Specification](PP_01_PUBLIC_HOMEPAGE_V1_SPEC_V1.0.md)
- **Required successor:** Separate Founder/Commander-authorized PP-02 Mission

## Non-Execution Statement

This document is a future operator plan only. PP-01 performs no authentication, backup, plugin/theme configuration, Elementor editing, DNS/TLS change, indexing change, Coming Soon removal, publication, deployment, or Production mutation. A checked box in this plan is not evidence unless a future authorized operator records the exact command/action, timestamp, actor, target identity, output, hash, and readback.

## Exact Future Production Target

The only intended public target is:

| Target field | Required value or gate |
| --- | --- |
| Canonical public origin | `https://damavandsteel.com` |
| Host policy | HTTPS, non-`www`; any alternate host must redirect only after separate verification and authority. |
| Application | The existing WordPress installation currently serving the canonical origin. |
| Homepage | The WordPress front page mapped to `/` on that exact installation. |
| Current public behavior | Mission-reported Coming Soon baseline; not independently runtime-verified by PP-01. |
| Hosting account/server identity | `NOT_VERIFIED`; PP-02 must record provider, account, server/site ID, document root, database identifier, and environment fingerprint before credentials or mutation. |
| WordPress identity | `NOT_VERIFIED`; PP-02 must record site URL/home URL, core version, active theme and version, active plugins and versions, front-page setting, administrator identity/role, and checksum/fingerprint evidence. |
| Excluded targets | Local, test, staging, preview, legacy, `www`, IP-address, alternate-domain, or similarly named installations are not Production. |

The canonical host identifies the intended public surface, but it is not sufficient target proof. If the authenticated installation cannot be cross-bound to that host and the recorded infrastructure identifiers, stop before mutation.

## Current Coming Soon Baseline

The Mission reports an unattractive Coming Soon public experience. PP-01 has not opened or changed the live site and does not treat that description as captured evidence. Before any future change, PP-02 must preserve:

- timestamped desktop and mobile full-page screenshots of the canonical origin;
- HTTP status, redirect chain, final URL, response headers relevant to cache/indexing, and TLS certificate identity;
- rendered page title, meta robots, canonical, visible copy, links, forms, and page source hash;
- current WordPress front-page/Coming Soon configuration and the owner of that behavior;
- current Blocksy and Elementor roles, versions, templates, global settings, and active dependencies;
- current robots/sitemap/indexing behavior without changing it; and
- an external readback from a clean session to prove what anonymous visitors see.

If the baseline differs materially, contains an incident, or cannot be captured consistently, stop and obtain Commander disposition.

## PP-02 Entry Gates

Every gate below is mandatory before any Production mutation:

1. Exact PP-02 Mission, path/system allowlist, actor, maintenance window, rollback owner, and communication plan approved.
2. Exact target identity cross-bound to `https://damavandsteel.com` and independently read back.
3. Current Coming Soon baseline captured and hashed.
4. Full backup generated, hashed, access-classified, preserved, restored in isolation, and read back successfully.
5. Blocksy and Elementor installed versions, package provenance, license status, compatibility, and ownership boundaries verified.
6. WordPress/PHP/database/server versions and resource limits recorded; no unsupported upgrade is combined with homepage work.
7. Rights-cleared, checksum-bound assets and Founder-approved visual tokens available, or the approved no-image fallback selected.
8. Every public copy/contact fact approved; the deferred email remains hidden until operational verification.
9. Inquiry action has a governed destination and fail-closed behavior. If no lead backend is approved, no form may be published.
10. Security/privacy/consent, spam/abuse, logging, notification, replay, retention, deletion, monitoring, and incident ownership applicable to the chosen inquiry path are approved and tested.
11. SEO/indexing disposition is explicit. No schema or indexing change is bundled by inference.
12. Staging or equivalent isolated rehearsal passes the desktop/mobile/RTL/accessibility/performance/no-price checklist.
13. Founder visual checkpoint passes on the exact candidate bytes/configuration.
14. Commander issues explicit Production and Coming Soon removal authority for the exact candidate and window.

Existing unresolved Runtime, authenticated target, backup/restore, package/license, product-level suppression, media-right, and security gates remain effective. PP-01 does not close them.

## Full Backup and Recovery Procedure

Before the first authorized change, the future operator must:

1. Quiesce or otherwise establish a documented consistency point appropriate to the host.
2. Export the complete database with engine/version, encoding, table prefix, row counts, and tool version recorded.
3. Archive WordPress core identity, `wp-content` (themes, plugins, uploads, must-use plugins, language files), configuration, web-server rules, PHP settings, cron/task configuration, and host-level settings needed for recovery.
4. Export WordPress front-page settings, menus, widgets, Blocksy customizer/options, Elementor site settings/templates, and the current Coming Soon mechanism separately for rapid rollback.
5. Record file modes, ownership expectations, symlinks, excluded volatile/cache paths, and secrets-handling classification. Never place raw credentials or private configuration in this repository.
6. Generate SHA-256 manifests, encrypt sensitive custody, restrict access, and preserve at least one copy outside the target host under a named custodian.
7. Restore the package to an isolated target compatible with the recorded stack.
8. Verify database and file integrity, anonymous rendering, admin access, Blocksy shell, Elementor rendering, media, URLs, inquiry behavior, and restoration of the Coming Soon baseline.
9. Record restore duration, evidence hashes, discrepancies, and an explicit `RESTORE_VERIFIED` approval from the rollback owner.

No mutation begins if backup or restore proof is partial, stale, unbound to the target, unreadable, or controlled only by the same failing system.

## Blocksy and Elementor Configuration Boundary

- Blocksy owns Header, Footer, navigation, global shell, container behavior, and global semantic visual tokens.
- Elementor owns only the homepage body from Hero through Contact Surface.
- Elementor must consume Blocksy/global tokens rather than create an independent design system.
- Do not install a custom theme, duplicate the global header/footer in Elementor, use Elementor for Product/archive templates, or introduce page-level scripts to replace governed platform behavior.
- Do not assume Blocksy Pro or Elementor Pro. Select a Pro feature only after package provenance, license, version compatibility, rollback, and ongoing ownership are proven.
- Do not introduce a cache/performance plugin as part of homepage publication. Existing cache/CDN behavior must be documented and safely purged only under explicit authority.

## Future Implementation Sequence

After all entry gates pass, PP-02 should use this bounded order:

1. Freeze the exact target/candidate identities and open the approved change window.
2. Re-confirm anonymous Coming Soon baseline and backup/restore evidence freshness.
3. Create or select a non-public homepage draft; do not replace the live front page.
4. Configure approved Blocksy global tokens and shell changes in the isolated candidate path, with an export before and after each controlled group.
5. Build the Elementor body using the exact hierarchy in the specification, frozen hero content, verified contacts, and rights-cleared assets or no-image fallback.
6. Keep all unverified navigation, email, forms, capability copy, Product details, schema, and interactions hidden.
7. Validate section order, one-H1 hierarchy, no-public-price behavior, fail-closed inquiry behavior, responsive/RTL behavior, and ownership separation.
8. Rehearse export/import and rollback in isolation; compare resulting hashes/configuration and anonymous rendering.
9. Capture Founder checkpoint evidence from the exact candidate at all required viewports and record approve/revise/reject.
10. Obtain explicit Commander Production and Coming Soon removal authorization bound to the candidate, backup, target, operator, and window.
11. Apply the minimum approved Blocksy settings and import/build the approved Elementor page on the exact Production target while Coming Soon remains active.
12. Run authenticated and bypass-safe preview QA; do not expose the candidate publicly.
13. At the removal gate, atomically select the verified homepage and disable only the verified Coming Soon mechanism.
14. Purge only documented caches, then perform immediate clean-session and external readback.
15. Monitor and preserve evidence through the approved observation window. Roll back on any trigger below.

No later step may compensate for a failed earlier gate.

## Post-Change QA Matrix

| Area | Required checks | Pass condition |
| --- | --- | --- |
| Identity | Final URL, canonical origin, target fingerprint, deployed page/configuration hash. | Exact authorized target and candidate; no alternate installation changed. |
| Desktop | Current supported desktop browsers, common widths, zoom, keyboard navigation. | Exact IA, no overflow/overlap, correct hierarchy, visible focus, verified actions only. |
| Mobile | 360px, 390px, 430px, portrait and landscape, touch behavior. | No horizontal overflow, tall hero, clipped Persian, undersized targets, or broken actions. |
| Tablet | Portrait/landscape and navigation transition. | Reading/focus order remains logical and stable. |
| RTL/BiDi | Persian source order, menus, punctuation, phone/email/URL isolation. | No reversed sequence, joining defect, misplaced icon, or focus/visual-order conflict. |
| Content truth | Hero, family, capability, why, CTA, contact, footer. | Only approved copy/facts; deferred email and unverified sections hidden. |
| Inquiry | Every visible telephone/WhatsApp/link/form behavior, validation, errors, privacy and monitoring. | Verified destination and fail-closed errors; no fake success or lost lead. |
| No-price | Visible page, source, structured data, metadata, linked homepage surfaces. | No amount, range, discount, cart, checkout, payment, Offer, or public availability/stock promise. |
| Accessibility | Landmarks, headings, alternative text, contrast, focus, keyboard, large text, reduced motion. | No material keyboard/screen-reader/contrast/zoom blocker; exact test evidence preserved. |
| Performance | Request/asset inventory, dimensions, font loading, LCP candidate, layout shift, JS, third parties. | No unapproved dependency or obvious regression; approved numeric budget met once defined. |
| HTTPS | Redirects, certificate/hostname, active/passive mixed content, forms and asset URLs. | One approved HTTPS origin, valid certificate, zero mixed content, no insecure submission. |
| SEO | Title, H1, canonical, robots, sitemap, schema and status codes. | Exact authorized disposition; no accidental indexing or unsupported Offer/Product facts. |
| Shell/body ownership | Blocksy header/footer/tokens and Elementor body/template assignment. | No duplication, override drift, or scope leakage. |
| Cache/readback | Authenticated view, anonymous clean session, alternate network/external probe where approved. | All surfaces return the same authorized public state after documented purge. |

Every failure is classified as pre-existing or introduced. Introduced material failures require rollback, not live experimentation.

## Explicit Coming Soon Removal Gate

Coming Soon may be removed only when one authorization record binds all of the following:

- exact Production target fingerprint and canonical origin;
- exact homepage and configuration identity;
- complete successful backup/restore evidence and named rollback owner;
- successful isolated rehearsal and post-import preview QA;
- Founder visual approval of the exact candidate;
- verified public contacts/inquiry destinations and fail-closed behavior;
- no-price/no-commerce/no-stock/no-Offer evidence;
- desktop, 360px, 390px, 430px, tablet, RTL, accessibility, HTTPS, mixed-content, and performance results;
- SEO/indexing disposition;
- cache/readback procedure, observation window, and rollback triggers; and
- explicit Commander wording that authorizes **Coming Soon removal and Production publication for this exact candidate**.

A general PP-01 approval, Draft PR, merge, backup, successful preview, or Founder visual approval alone is not removal authority. If any binding item changes, the gate resets to closed.

## Progressive Enablement Model

The future public preview should advance only through separately recorded states:

1. **Prepared:** repository plan/specification exists; no runtime authority.
2. **Isolated Candidate:** approved design is built off-public on an exact target; Coming Soon remains public.
3. **Verified Candidate:** backup/restore, functional, visual, responsive, accessibility, security/privacy, no-price, and rollback evidence pass.
4. **Public Preview:** explicit removal/publication gate passes; only verified homepage surfaces are visible. This is not formal launch.
5. **Progressively Enabled:** later Missions may enable additional verified navigation, capability content, governed inquiry backend, Product surfaces, or SEO elements one bounded gate at a time.
6. **Formal Public Launch:** separate Founder/Commander decision after all applicable launch gates; never inferred from preview uptime.

Any unverified capability remains hidden at every stage.

## Rollback Triggers

Immediately invoke rollback if any of the following is observed:

- wrong target/site, wrong candidate, unintended page/template, or configuration drift;
- unavailable site, redirect loop, certificate/TLS failure, mixed content, server/PHP/database error, or broken asset loading;
- Coming Soon still intercepts inconsistently or is removed without the bound authorization;
- broken Header/Footer/navigation, Elementor render, mobile layout, RTL order, focus/keyboard path, or critical accessibility behavior;
- visible price, cart, checkout, payment, Offer schema, stock/availability promise, invented claim, unapproved copy, or unlicensed media;
- fake/dead inquiry action, lead loss, incorrect destination, privacy/consent failure, spam exposure, or unmonitored channel;
- accidental indexing/noindex change, canonical/robots/sitemap/schema drift, or unexpected cache/CDN exposure;
- material performance regression, layout instability, excessive requests, or third-party dependency not present in the approved candidate;
- inability to complete independent anonymous readback; or
- Founder, Commander, security/privacy owner, runtime owner, or rollback owner calls stop within their authority.

## Rollback Procedure

1. Stop further changes and record timestamp, observer, exact symptom, request IDs/log references, screenshots, and current hashes without exposing secrets.
2. Re-enable the previously verified Coming Soon mechanism if it can be done safely and is part of the tested rapid rollback.
3. Restore the prior WordPress front-page assignment, Blocksy export, Elementor templates/site settings, menus/widgets, and cache state from the bound pre-change package.
4. If configuration rollback is insufficient or integrity is uncertain, restore the full verified database and file backup using the rehearsed procedure.
5. Purge only documented caches and perform clean-session/external readback of the restored Coming Soon baseline, HTTPS, redirects, title, source hash, and key links.
6. Preserve incident and recovery evidence; compare restored hashes with the pre-change manifest and record discrepancies.
7. Keep the public preview closed. A new attempt requires root-cause correction, fresh validation, refreshed backup where needed, and new explicit authorization.

## Founder and Commander Checkpoints

- Founder reviews the exact visual checklist and candidate screenshots; approval is visual/content disposition only.
- Project Commander reviews gate completeness, scope, target binding, evidence, operator plan, and removal wording.
- Runtime, security/privacy, backup/restore, and rollback owners approve only their assigned gates.
- No role may treat another role's approval as its own, and no generated artifact self-approves.

RUNTIME_AUTHORITY = NONE
PRODUCTION_MUTATION = NO
PUBLICATION_AUTHORITY = NONE
