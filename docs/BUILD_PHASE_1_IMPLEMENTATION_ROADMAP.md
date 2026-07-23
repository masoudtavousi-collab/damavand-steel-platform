# Build Phase 1 Implementation Roadmap

## Document Control

- **Document ID:** `docs/BUILD_PHASE_1_IMPLEMENTATION_ROADMAP.md`
- **Status:** Draft
- **Authority:** Proposed implementation architecture and execution plan
- **Owner:** Founder
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-23
- **Repository Baseline:** `ed0841bcd46d315dba8c4ecfd64b1eb105048da5`
- **Lifecycle:** Founder review required
- **Implementation Authority:** None; this document does not authorize code, configuration, synchronization, migration, deployment, publication, or production mutation

## Purpose

Define the first implementation roadmap for transforming the Damavand Steel repository into a working enterprise Product and Knowledge Platform while preserving repository authority, Inquiry First, No Public Pricing, Mobile First, Persian RTL, and Founder-controlled release gates.

This is a planning artifact only. It creates no Product, SKU, runtime, WordPress configuration, WooCommerce configuration, plugin code, theme artifact, import, publication, deployment, or production change.

## Planning Basis

The roadmap starts from the verified baseline and the following implemented repository foundations:

- The [Product Core contract](../repository/data/contracts/product-core.contract.yaml) defines stable Product identities and the canonical `Catalog → Platform → Family → Series → Variant Rules → SKU` hierarchy.
- The [Product Attribute contract](../repository/data/contracts/product-attribute.contract.yaml) defines generic attribute identity, types, categories, requirement levels, unit policy, and validation boundaries.
- The [Measurement contract](../repository/data/contracts/measurement.contract.yaml) defines generic dimensions, units, deterministic conversion metadata, precision, and compatibility.
- No canonical Product Master Data, Golden reference package, commercial SKU, configurator, synchronization adapter, WordPress plugin, runtime mapping, or deployment implementation is present at this baseline.

The existing [Platform Architecture](../repository/platform/PLATFORM_ARCHITECTURE.md), [Engine Boundaries](../repository/platform/ENGINE_BOUNDARIES.md), [WordPress Blueprint](35_WORDPRESS_BLUEPRINT.md), [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md), and [AI Collaboration Standard](AI_COLLABORATION.md) provide design constraints. Their individual lifecycle and approval metadata remain intact; this roadmap does not promote those documents or unresolved choices.

## Architectural Outcome

The recommended architecture is a repository-controlled platform with replaceable runtime adapters:

```text
Founder approvals and governed evidence
                  |
                  v
GitHub repository: canonical contracts, identities, Master Data, content, SEO rules
                  |
                  v
Validated, versioned, immutable release bundle
                  |
                  v
Damavand Platform Bridge: supported APIs, mapping, dry run, apply, reconcile
        |                 |                 |                 |
        v                 v                 v                 v
 WordPress Core      WooCommerce      Search/SEO       Inquiry adapter
 content runtime     catalog view     projections       and context
        \                 |                 /
         \                v                /
          +---- Blocksy shell + Elementor body ----+
                              |
                              v
                    Persian RTL public website

Runtime observations -> reconciliation evidence -> reviewed repository change
Runtime observations never become canonical truth automatically.
```

### Architectural Principles

1. The repository is the canonical control plane for governed Product identities, contracts, Product Master Data, reusable content assets, mappings, and release evidence.
2. WordPress and WooCommerce are runtime projections. Their numeric IDs, slugs, post types, product IDs, variation IDs, and template state are not canonical identities.
3. A custom integration plugin is the sole synchronization and policy-enforcement adapter. It does not become a second source of Product or content truth.
4. Blocksy Pro owns the global site shell. Elementor Pro owns only delegated body composition. No custom theme or child theme is planned.
5. Every projection is versioned, deterministic, idempotent, auditable, dry-run capable, and reversible.
6. Runtime edits are accepted only for fields explicitly owned by the runtime. Changes to repository-owned fields become evidence or a change proposal, never an automatic upstream mutation.
7. WooCommerce provides catalog capabilities without public price, cart, checkout, payment, sale, discount, or Offer schema.
8. Search, SEO, analytics, and future AI are derived consumers. None may invent or approve Product facts.
9. Production access, publication, migration, and deployment each require a separate exact Founder authorization.

## Recommended Project Architecture

| Layer | Canonical responsibility | Recommended implementation boundary | Must not own |
| --- | --- | --- | --- |
| Governance | Approval, lifecycle, ownership, provenance, release gates | Founder decisions and reviewed repository records | Runtime convenience decisions |
| Product Repository | Contracts, stable identities, hierarchy, attributes, units, Master Data, valid Variant Rules, derived SKU records after approval | `repository/data/` canonical paths and validators | WordPress/WooCommerce IDs, presentation, public price |
| Content Repository | Reusable approved content, localization, relationships, rights, review status | `repository/content/` after a separately approved content contract | Elementor layout state or WordPress revision metadata |
| Knowledge Repository | Governed Knowledge assets linked by stable identities | `repository/knowledge/` after Product identity dependencies and a separate authorization are satisfied | Product or commercial authority |
| Release Builder | Validate and package an immutable approved projection | Deterministic local/CI build producing a manifest, checksums, dependency versions, and validation report | Secrets, live state, approval decisions |
| Integration Adapter | Compare, plan, project, reconcile, and report through supported interfaces | Proposed custom plugin, provisionally named **Damavand Platform Bridge** | Canonical Product facts, theme rendering, direct database writes |
| WordPress Runtime | Pages, posts, media, users, roles, editorial workflow, revisions, supported APIs | WordPress Core and approved single-owner capabilities | Canonical Product identity or unreviewed business truth |
| Commerce Runtime | Inquiry-first catalog projection and valid selectable variations | WooCommerce with transaction surfaces disabled | Public pricing, canonical hierarchy, speculative combinations |
| Presentation | Site shell and bounded composition | Blocksy Pro shell; Elementor Pro delegated body regions | Product rules, data authority, schema authority |
| Discovery | Search index, filters, SEO metadata, redirects, sitemaps | Single approved owner per concern, fed by release projections | Independent facts, uncontrolled indexable archives |
| Operations | Environments, secrets, backup/restore, deployment, monitoring | Approved external services and least-privilege runbooks | Canonical content or approval authority |

## Repository to WordPress Relationship

The repository supplies approved, versioned projection inputs. WordPress supplies the runtime content-management and publication environment.

| Concern | Repository ownership | WordPress ownership | Synchronization rule |
| --- | --- | --- | --- |
| Stable identity | Canonical entity and content IDs | Mapping to post, term, attachment, and user-facing URL IDs | Mapping is stored separately and never changes canonical identity |
| Approved reusable content | Source content, locale, provenance, lifecycle, relationships | Draft/publish state, revisions, scheduled publication, runtime-only editorial notes | Repository content enters as Draft unless a separately approved publication gate permits otherwise |
| Media | Rights metadata, source identity, intended relationships | Attachment storage, renditions, delivery metadata | Binary transfer requires rights, checksum, privacy, and rollback validation |
| Navigation and pages | Information architecture and approved content intent | Menus, page records, revisions, runtime assembly | Runtime IDs are returned only as reconciliation evidence |
| Roles and workflow | Capability requirements and approval gates | WordPress users, roles, capabilities, editorial workflow | Least privilege; no role grants Founder authority |

Direct database mutation is prohibited. The adapter must use supported WordPress APIs, WooCommerce APIs, and documented extension points.

## Repository to WooCommerce Relationship

WooCommerce is the catalog projection for the website, not the canonical Product Repository.

- Canonical Product entities and Variant Rules retain stable repository IDs independent of WooCommerce.
- The exact mapping from `Family`, `Series`, and `Variant Rules` to variable parents and variations is defined per approved Product profile; no universal one-to-one mapping is assumed.
- A Variable Parent Product may present a Family or another coherent commercial grouping but never replaces the canonical hierarchy.
- Only approved combinations are projected. A Cartesian product is never used as evidence of availability.
- WooCommerce attributes reference canonical Attribute and Unit definitions through explicit mapping records.
- Commercial SKU generation occurs only after approved Product modeling and a separately authorized SKU policy.
- Public price fields, price ranges, sales, cart, checkout, payment, and Offer schema remain disabled and are tested across HTML, APIs, feeds, caches, email, search, and structured data.
- WooCommerce stock or visibility values may be projections only after source authority, freshness, wording, and failure behavior are approved.

## Repository to Custom Plugin Relationship

The proposed **Damavand Platform Bridge** is a replaceable integration adapter. Its name and final package path remain subject to the implementation-wave approval.

### Proposed Plugin Modules

| Module | Responsibility |
| --- | --- |
| Release reader | Read an approved release manifest and verify version, checksum, dependencies, and environment compatibility |
| Contract validator | Reject invalid or unsupported records before any runtime write |
| Identity mapper | Maintain canonical-ID-to-runtime-ID mappings with uniqueness and lifecycle controls |
| Difference planner | Produce a human-readable create/update/archive/no-op plan without mutation |
| Product projector | Apply approved catalog and attribute projections through WooCommerce interfaces |
| Content projector | Apply approved content and media projections through WordPress interfaces |
| Discovery projector | Apply approved SEO, redirect, synonym, and search-index metadata through one owner per concern |
| Inquiry context adapter | Pass canonical Product context into the approved Inquiry workflow without invoking checkout |
| Reconciler | Compare expected and actual runtime state and report drift without automatically changing repository truth |
| Audit and recovery | Record release ID, actor, time, result, affected mappings, errors, and rollback point without logging secrets or protected inquiry data |

### Plugin Safety Contract

- Fail closed on an unknown contract version, missing approval evidence, checksum mismatch, invalid mapping, secret exposure, partial dependency, or environment mismatch.
- Separate `validate`, `plan`, `apply`, `reconcile`, and `rollback` operations.
- Require an exact environment and a one-time approved release for every write.
- Use idempotency keys based on environment, release identity, and operation.
- Prevent concurrent or out-of-order release application.
- Use supported APIs and transaction-safe batches; never edit Core, vendor packages, theme files, or the database directly.
- Keep secrets in an approved secret manager or runtime credential facility, never in Git or release bundles.
- Expose no automatic repository write-back.

## Repository to Theme Relationship

The repository provides design intent, tokens, content relationships, and presentation requirements. It does not vendor or modify the theme.

- Blocksy Pro owns header, footer, navigation shell, global layout, default archives, and theme-level WooCommerce presentation.
- Elementor Pro owns only explicitly delegated page and landing body composition.
- Dynamic templates read WordPress/WooCommerce projections by stable mappings; template-local copied Product facts are prohibited.
- Theme and Elementor exports are implementation artifacts, not canonical business or Product sources.
- Custom theme, child theme, copied vendor template, and vendor-file modification are outside the recommended architecture.
- Every visual release must pass Persian RTL, mobile, accessibility, inquiry-only, no-price, performance, and rollback checks.

## Product Configurator Architecture

The Product Configurator is a governed selection interface over approved Variant Rules, not a Product generator.

### Configurator Components

1. **Configuration contract:** Declares the approved Series, selectable Attribute IDs, Unit policies, dependency rules, exclusions, defaults, and output context.
2. **Rule evaluator:** Deterministically evaluates allowed next values and valid terminal selections from approved rules.
3. **Server authority:** Validates every submitted configuration independently of the browser.
4. **Presentation client:** Provides mobile-first Persian RTL progressive disclosure, accessible keyboard behavior, clear invalid-state messages, and resilient no-JavaScript fallback where feasible.
5. **Inquiry handoff:** Produces a tamper-evident configuration reference and human-readable summary for inquiry; it does not create a cart, order, price, or unapproved SKU.
6. **Analytics boundary:** Records privacy-approved interaction events by stable non-personal identifiers; it does not promote demand signals into availability.

### Configurator Rules

- Present only values and combinations explicitly permitted by an approved Product profile.
- Never infer commercial availability from mathematical compatibility.
- Never create Product records, SKUs, prices, weights, compatibility claims, or supply promises.
- Keep display labels and units localized while retaining canonical IDs in all requests.
- Version every rule set and preserve the rule-set version with an inquiry.
- Reject stale, unknown, or tampered configurations and guide the user back to a valid state.
- Define deterministic empty, unavailable, superseded, and partial-data behavior.

## Product Repository Synchronization Strategy

### Release Flow

```text
Author/approve canonical data
  -> validate contracts and references
  -> build immutable release bundle
  -> verify release in target environment
  -> create dry-run difference plan
  -> obtain exact write approval
  -> apply bounded batches
  -> reconcile expected vs actual state
  -> retain evidence and rollback point
```

### Synchronization Controls

- **Direction:** Approved repository release to runtime. Runtime-to-repository is evidence-only.
- **Granularity:** Entity and field ownership are explicit. Undeclared fields block synchronization.
- **Identity:** Canonical IDs map to runtime IDs in a versioned mapping store with uniqueness constraints.
- **Idempotency:** Reapplying the same release produces no additional change.
- **Ordering:** Releases apply in sequence and declare contract and dependency versions.
- **Deletion:** Hard deletion is not the default. Deprecation, archive, replacement, and redirect behavior are planned explicitly.
- **Conflict handling:** Repository-owned drift blocks or is overwritten only by the approved plan. Runtime-owned fields are preserved. Ambiguous ownership stops the operation.
- **Partial failure:** Stop the batch, retain completed-operation evidence, and execute the pre-approved rollback or forward-recovery plan.
- **Reconciliation:** Report missing, extra, changed, orphaned, stale, and unmapped records by canonical ID.
- **Freshness:** The public runtime exposes the active release identity and health state to administrators, not as sensitive public detail.

## Content Synchronization Strategy

Content synchronization follows the same release discipline but respects editorial workflow:

1. Define a content contract for stable identity, locale, content type, source, provenance, lifecycle, access class, relationships, media references, SEO intent, and review evidence.
2. Keep reusable approved source content in the repository and project it into WordPress as a Draft by default.
3. Preserve WordPress-owned workflow fields such as revision history, scheduled time, editor notes, and publication state unless a future contract explicitly assigns them elsewhere.
4. Represent Elementor composition as a derived presentation artifact. Canonical text and Product facts remain outside template-local storage.
5. Resolve content conflicts by declared field ownership. An ambiguous field blocks the release.
6. Validate Persian language, RTL rendering, links, media rights, accessibility text, canonical Product references, and expiry/review dates.
7. Archive or supersede content through lifecycle and redirect rules; do not silently delete public history.
8. Return runtime URLs, revision IDs, and drift as reconciliation evidence only.

## SEO Integration

SEO is a controlled projection, not a parallel content or Product repository.

- Select exactly one owner for title, description, canonical URL, breadcrumb, sitemap, redirect, robots, and structured-data output.
- Store approved SEO intent and entity relationships with stable repository identities.
- Generate public schema only from approved facts and public lifecycle state.
- Prohibit price, Offer, AggregateOffer, sale, availability, or transactional schema leakage.
- Define canonical behavior for parents, variations, filters, parameters, pagination, and curated landing pages before enabling indexation.
- Maintain a versioned redirect ledger for migrated, renamed, merged, archived, and superseded URLs.
- Validate rendered HTML, headers, canonical tags, hreflang when applicable, structured data, sitemaps, robots rules, internal links, and duplicate output in staging.
- Require an SEO crawl comparison and rollback plan before any future public cutover.

## Search Integration

Search is a rebuildable index of approved public projections.

- Begin with the simplest supported WordPress/WooCommerce search capability that satisfies Persian normalization, stable identity, filtering, and performance requirements.
- Normalize Arabic/Persian character variants, spacing, digits, and approved aliases without changing displayed canonical labels.
- Index only approved public fields and explicitly searchable Attribute values.
- Build facets from canonical taxonomy and Attribute mappings; do not create uncontrolled tags or index every URL combination.
- Keep Product availability, compatibility, and ranking claims source-bound and freshness-aware.
- Return configured selections to the inquiry flow without exposing price or transaction behavior.
- Version synonyms and search rules in the repository and test positive, zero-result, adversarial, typo, Persian RTL, and performance cases.
- Treat an external search service as a replaceable later adapter, not an initial dependency or authority.

## AI Integration

Phase 1 includes no product-facing or operational AI runtime.

The platform should become AI-ready without activating AI by:

- preserving machine-readable contracts, stable IDs, provenance, status, access class, locale, and supersession;
- separating approved facts from candidates, missing values, and derived presentation;
- defining read-only retrieval interfaces over approved public Knowledge and Product projections;
- preparing evaluation cases for citation accuracy, access control, Persian language, abstention, and prohibited pricing claims; and
- recording model, provider, privacy, retention, cost, observability, human review, and shutdown requirements as unresolved future decisions.

A future AI feature requires a separate Founder-approved architecture and implementation wave. It must retrieve from approved sources, cite them, abstain when evidence is missing, respect access controls, and never create Product truth, commercial approval, price, compatibility, availability, or publication authority.

## Build Order

1. Approve this target architecture, ownership model, capability boundaries, and unresolved-decision register.
2. Create a small Founder-approved Product Master Data and Variant Rules pilot using the existing contracts.
3. Define the versioned release bundle, mapping, synchronization, reconciliation, and rollback contracts.
4. Build and test the custom adapter locally without connecting to production.
5. Establish an isolated development and staging platform with approved versions, access, secrets, backup, restore, and observability.
6. Implement Product projection and reconciliation in staging.
7. Implement content/media projection and editorial handoff in staging.
8. Configure the Blocksy shell, Elementor body patterns, and inquiry-only WooCommerce presentation in staging.
9. Implement the configurator, inquiry handoff, SEO projection, and search index in staging.
10. Rehearse migration, validate non-functional requirements, and complete Founder user-acceptance testing.
11. Prepare a bounded production pilot plan with exact rollback evidence.
12. Deploy only after a new, exact Founder runtime and production authorization.

## Deployment Order

Deployment is future work and must progress through isolated gates:

| Order | Target | Entry gate | Exit evidence | Rollback boundary |
| --- | --- | --- | --- | --- |
| 1 | Local validation | Approved source and deterministic toolchain | Contracts, tests, release manifest, and no-secret report pass | Discard local generated output |
| 2 | Disposable integration environment | Approved package versions and non-production fixtures | Installation is reproducible; adapter validate/plan/reconcile pass | Destroy and rebuild environment |
| 3 | Persistent staging | Least-privilege access, backup/restore, monitoring, and sanitized data approved | End-to-end Product, content, configurator, inquiry, SEO, search, RTL/mobile, accessibility, security, and performance evidence | Restore staging snapshot or reapply prior release |
| 4 | Founder acceptance | Staging release frozen and all blocking checks pass | Founder records scope-specific acceptance or rejection | Return to staging backlog; no production effect |
| 5 | Limited production pilot | Separate exact production authorization, verified backup/restore, maintenance and rollback owners | Small approved scope reconciles with no critical regression | Disable adapter/pilot surface and restore prior release/data |
| 6 | Progressive expansion | Pilot observation window passes and new scope is approved | Each bounded batch reconciles and passes regression checks | Roll back only the affected batch/release |
| 7 | Steady-state operation | Ownership, support, monitoring, incident, upgrade, and recovery procedures accepted | Scheduled reconciliation, backup restore tests, and release reviews | Activate incident-specific rollback or forward recovery |

No row in this table is authorized merely by approval of this roadmap.

## Migration Strategy

Use a staged, identity-first migration rather than a big-bang import:

1. **Read-only inventory:** Identify any future source WordPress, WooCommerce, content, media, URL, taxonomy, and integration records without changing them.
2. **Authority classification:** Mark each field as repository-owned, runtime-owned, external-authority, candidate, missing, duplicate, or prohibited.
3. **Identity map:** Assign or resolve canonical IDs without deriving identity from slugs or runtime numeric IDs.
4. **Quarantine:** Keep unverified exports and legacy data outside canonical paths until provenance, rights, and quality pass.
5. **Transform:** Convert only approved records into current contracts; preserve source references and reject unknown mappings.
6. **Rehearse:** Apply the candidate release to a disposable environment, then staging, and compare counts, identities, relationships, content, media, URLs, and no-price behavior.
7. **Freeze and delta:** Define a short source freeze or controlled delta capture before cutover. Dual write is prohibited unless separately designed and approved.
8. **Pilot:** Migrate a minimal Founder-approved slice and verify inquiries, SEO, search, RTL/mobile, accessibility, and rollback.
9. **Cutover:** Promote by bounded batches only after evidence and explicit authorization.
10. **Reconcile and retain:** Record expected/actual state, unresolved exceptions, redirect coverage, active release, and rollback point.
11. **Decommission:** Retire legacy paths or integrations only after retention, redirect, audit, and recovery obligations are approved and met.

## Build Waves

Complexity estimates are relative: **Low** is primarily bounded documentation or configuration; **Medium** combines contracts and tested integration work; **High** spans multiple systems or sensitive migration; **Very High** includes production cutover or broad operational risk.

| Wave | Objective | Expected output | Complexity | Dependencies | Rollback strategy |
| --- | --- | --- | --- | --- | --- |
| BP1 — Architecture acceptance | Resolve target ownership, environment, provider, version, security, privacy, inquiry, SEO, and operational decisions | Approved roadmap, decision records, responsibility matrix, acceptance criteria, exact next-wave allowlist | Medium | Founder and specialist review | Revert proposal commits; no runtime exists |
| BP2 — Product pilot data | Model one bounded approved Product slice through Product identities, Attributes, Units, Variant Rules, provenance, and statuses | Validated canonical pilot package; no speculative combinations or public SKU policy | High | BP1; domain evidence; Product data approval | Revert pilot package or mark records superseded; no runtime projection |
| BP3 — Release and synchronization contracts | Define immutable release manifest, checksums, field ownership, mappings, operation plan, reconciliation, and rollback formats | Versioned schemas, validators, deterministic fixtures, release runbook | High | BP1–BP2; repository path approval | Revert contract version before adoption; version-forward migration after adoption |
| BP4 — Adapter foundation | Create the custom plugin skeleton, dependency boundaries, command/admin interfaces, audit model, and contract compatibility layer | Installable local package with no production credentials and validate/plan-only behavior | High | BP3; exact supported stack; code-quality and security rules | Uninstall package; remove generated local state; retain repository history |
| BP5 — Environment foundation | Establish disposable development and persistent staging with supported versions, secrets, least privilege, backup, restore, logs, and monitoring | Reproducible non-production environments and verified restore evidence | High | BP1; hosting/provider decisions; licenses; security review | Destroy/rebuild disposable environment; restore staging baseline |
| BP6 — Product projection | Implement idempotent Product, Attribute, Unit, taxonomy, parent/variation, lifecycle, and mapping projection in staging | Dry-run plan, bounded apply, reconciliation report, positive/adversarial tests | Very High | BP2–BP5; exact WooCommerce mapping; no-price controls | Apply prior release or restore staging snapshot; preserve canonical data |
| BP7 — Content and media projection | Implement governed content, relationships, media, localization, Draft handoff, and drift reporting | Staging content projection with rights, checksum, accessibility, and editorial evidence | High | BP3–BP5; approved content contract and ownership | Apply prior content release; restore affected revisions/media mappings |
| BP8 — Presentation and inquiry shell | Configure Blocksy, bounded Elementor patterns, WooCommerce inquiry-only presentation, roles, and inquiry context | Persian RTL/mobile staging experience with no price/cart/checkout and Admin walkthrough | High | BP5–BP7; design tokens; inquiry/privacy decisions | Restore configuration export/snapshot; deactivate affected template/pattern |
| BP9 — Configurator | Implement versioned Variant Rule evaluation, accessible selection UI, server validation, and inquiry handoff | Staging configurator for the approved pilot with deterministic and adversarial tests | Very High | BP2, BP3, BP6, BP8 | Disable configurator feature flag and retain basic contextual inquiry |
| BP10 — SEO and search | Implement single-owner SEO projection, redirects, sitemaps, Persian search normalization, synonyms, filters, and index rebuild | Validated staging crawl, schema report, search corpus, zero-result and performance evidence | High | BP6–BP9; SEO/indexation decisions | Restore prior metadata/redirect set; rebuild prior search index |
| BP11 — Migration rehearsal and UAT | Execute sanitized full rehearsal, reconcile, load/security/accessibility test, train administrators, and complete Founder UAT | Signed evidence pack, exception ledger, operating runbooks, production pilot recommendation | Very High | BP5–BP10; migration source access; acceptance criteria | Restore staging; discard rehearsal imports; return defects to owning wave |
| BP12 — Controlled production pilot | Deploy only a minimal separately approved scope, observe, reconcile, and decide expand/rollback | Pilot release evidence, monitoring, inquiry verification, rollback outcome, Founder decision | Very High | BP11; separate production authorization; verified backup/restore and owners | Disable pilot, restore prior release/data, verify public and inquiry recovery |
| BP13 — AI readiness boundary | Define future read-only retrieval contract, access classes, evaluation suite, provider risks, and shutdown controls without activating AI | Founder-reviewable future AI architecture and evaluation plan; no Phase 1 AI runtime | Medium | Stable Product/Knowledge identities; privacy/security architecture | Revert planning artifacts; no model or external service is active |

No wave begins automatically. Every wave requires an exact Founder-approved scope, branch, allowed paths, validation, rollback, exclusions, and stop conditions.

## Milestones

| Milestone | Completion evidence | Founder decision |
| --- | --- | --- |
| M0 — Roadmap accepted | Architecture, ownership, exclusions, waves, and unresolved decisions reviewed | Approve/revise roadmap and BP1 |
| M1 — Canonical pilot ready | Approved Product pilot validates with provenance and no speculative data | Approve/reject release-contract work |
| M2 — Release system ready | Release, mapping, sync, reconciliation, and rollback contracts pass fixtures | Approve/reject adapter implementation |
| M3 — Adapter and staging ready | Local adapter and staging platform pass security, restore, and compatibility gates | Approve/reject staging projection |
| M4 — Staging product experience ready | Product, content, presentation, configurator, inquiry, SEO, and search pass end-to-end checks | Approve/reject migration rehearsal |
| M5 — Operational readiness established | Rehearsal, UAT, performance, security, backup/restore, training, and runbooks pass | Approve/reject bounded production pilot |
| M6 — Production pilot decided | Pilot is reconciled and observed with no unresolved critical issue | Expand, hold, or roll back |
| M7 — Platform steady state | Release ownership, monitoring, incident, upgrade, reconciliation, and recovery cadence are accepted | Approve normal operating model |

## Principal Risks

| Risk | Probability | Impact | Control and gate |
| --- | --- | --- | --- |
| Draft architecture is treated as approved implementation authority | Medium | Critical | Explicit lifecycle metadata; exact Founder authorization per wave |
| Canonical and runtime ownership diverge | High | Critical | Field ownership contract, stable mappings, drift reports, no automatic write-back |
| Invalid Product combinations or invented commercial facts appear | High | Critical | Approved Variant Rules only, provenance/status enforcement, adversarial validation |
| Public price or transaction behavior leaks through WooCommerce, extensions, APIs, feeds, schema, or cache | Medium | Critical | Exhaustive no-price/no-transaction test matrix and single-owner review |
| WordPress/WooCommerce/plugin/theme versions conflict | Medium | High | Supported-version matrix, staged upgrade rehearsal, pinned release evidence |
| Plugin, theme, Elementor, SEO, and search responsibilities overlap | High | High | One owner per concern and capability responsibility review before installation |
| Synchronization partially applies or cannot reconcile | Medium | Critical | Bounded batches, idempotency, ordered releases, audit log, restore and forward-recovery tests |
| Runtime edits are overwritten or silently become canonical | Medium | High | Field ownership, difference approval, Draft default, evidence-only upstream path |
| Legacy slugs or runtime IDs become canonical identity | Medium | High | Identity-first migration and explicit mapping registry |
| Persian RTL, mobile, accessibility, or search normalization is discovered late | Medium | High | Acceptance fixtures from BP1 and continuous staging tests |
| SEO traffic is lost during URL or taxonomy migration | Medium | High | Redirect ledger, crawl comparison, bounded pilot, rapid rollback |
| Inquiry context or protected customer data is exposed | Medium | Critical | Privacy classification, least privilege, log redaction, retention and incident gates |
| Founder administration requires technical intervention | Medium | High | Admin workflow acceptance, training, role design, reconciliation reports |
| Vendor lock-in prevents replacement | Medium | Medium | Repository-owned contracts, adapter interfaces, export/uninstall and migration evidence |
| AI is activated early or presents unapproved facts | Low | Critical | Phase 1 prohibition, no AI dependency, separate future approval and shutdown gate |
| Backup exists but restore is unverified | Medium | Critical | Restore test is an entry gate for staging writes and production pilot |

## Validation and Acceptance Framework

Each implementation wave must define and retain proportionate evidence for:

- schema parsing, referential integrity, unique stable IDs, controlled status, provenance, dependency versions, and deterministic output;
- positive, boundary, adversarial, replay, partial-failure, rollback, and reconciliation tests;
- secret, credential, personal-data, dependency, permission, and external-endpoint review;
- public no-price, no-Offer, no-cart, no-checkout, no-payment, and inquiry-only behavior;
- Persian language, RTL, mobile, accessibility, browser, performance, and failure-state behavior;
- search relevance, zero results, filters, indexability, canonical URLs, redirects, sitemaps, and structured data;
- backup integrity, restore evidence, observability, incident ownership, and post-change verification; and
- final repository status, exact changed paths, validation output, unresolved questions, GO/NO-GO, and rollback readiness.

A successful technical check never substitutes for Founder approval.

## Decisions Required Before BP1 Can Close

1. Approve or revise the recommended repository-to-runtime architecture and proposed custom adapter boundary.
2. Assign Product, content, taxonomy, SEO, inquiry, security/privacy, release, and operations owners.
3. Approve target development/staging topology and later production ownership; no provider is selected here.
4. Approve the supported WordPress, WooCommerce, Blocksy Pro, Elementor Pro, PHP, database, and single-owner capability version matrix.
5. Approve the canonical Product pilot scope and its evidence sources.
6. Approve Product-to-WooCommerce mapping rules, SKU policy timing, availability authority, and publication lifecycle.
7. Approve content field ownership, editorial handoff, media rights, localization, and publication gates.
8. Approve inquiry fields, consent, routing, retention, protected-data handling, and failure behavior.
9. Approve SEO/indexation, URL, redirect, search/facet, analytics, and privacy boundaries.
10. Approve environment, secret, backup, restore, monitoring, incident, deployment, and rollback owners and acceptance thresholds.

## Current GO/NO-GO

- **GO:** Founder review and revision or approval of this roadmap.
- **NO-GO:** Product creation, SKU creation, plugin implementation, WordPress/WooCommerce/theme modification, synchronization, migration, publication, deployment, production mutation, and AI activation.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-23 | Initial Build Phase 1 implementation roadmap based on the verified post-Wave 2C baseline; planning only. |
