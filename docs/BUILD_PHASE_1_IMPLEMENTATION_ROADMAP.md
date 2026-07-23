# Build Phase 1 Implementation Roadmap

## Document Control

- **Document ID:** `docs/BUILD_PHASE_1_IMPLEMENTATION_ROADMAP.md`
- **Status:** Draft
- **Authority:** Proposed implementation architecture and execution plan
- **Owner:** Founder
- **Approval Authority:** Founder
- **Version:** 0.2.0
- **Last Updated:** 2026-07-23
- **Repository Baseline:** `ed0841bcd46d315dba8c4ecfd64b1eb105048da5`
- **Lifecycle:** Founder review required
- **Implementation Authority:** None; this document does not authorize code, configuration, synchronization, migration, deployment, publication, or production mutation

## Purpose

Define a visible-product-first implementation roadmap for transforming the Damavand Steel repository into a working enterprise Product and Knowledge Platform while preserving repository authority, Inquiry First, No Public Pricing, Mobile First, Persian RTL, and Founder-controlled release gates.

This is a planning artifact only. It creates no Product, SKU, runtime, WordPress configuration, WooCommerce configuration, plugin code, theme artifact, import, publication, deployment, or production change.

## Planning Basis

The roadmap starts from the verified baseline and the following implemented repository foundations:

- The [Product Core contract](../repository/data/contracts/product-core.contract.yaml) defines stable Product identities and the canonical `Catalog → Platform → Family → Series → Variant Rules → SKU` hierarchy.
- The [Product Attribute contract](../repository/data/contracts/product-attribute.contract.yaml) defines generic attribute identity, types, categories, requirement levels, unit policy, and validation boundaries.
- The [Measurement contract](../repository/data/contracts/measurement.contract.yaml) defines generic dimensions, units, deterministic conversion metadata, precision, and compatibility.
- No canonical Product Master Data, Golden reference package, commercial SKU, configurator, synchronization adapter, WordPress plugin, runtime mapping, or deployment implementation is present at this baseline.

The existing [Platform Architecture](../repository/platform/PLATFORM_ARCHITECTURE.md), [Engine Boundaries](../repository/platform/ENGINE_BOUNDARIES.md), [WordPress Blueprint](35_WORDPRESS_BLUEPRINT.md), [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md), and [AI Collaboration Standard](AI_COLLABORATION.md) provide design constraints. Their individual lifecycle and approval metadata remain intact; this roadmap does not promote those documents or unresolved choices.

## Visible-Product-First Strategy

The first implementation milestone must produce a locally runnable, visibly coherent Persian RTL website prototype. Architecture is established through a narrow vertical slice, then hardened only as the slice proves which boundaries are necessary.

BP1 must include exactly this first visible scope:

- homepage shell;
- main navigation;
- Pipes category landing page;
- one representative Pipe product page;
- inquiry-first call to action;
- no public pricing, cart, checkout, payment, sale, discount, or Offer schema;
- mobile-first Persian RTL presentation;
- reusable design tokens for color, type, spacing, layout, radius, state, and motion;
- local-only execution with no production connection or mutation; and
- accessibility, security, deterministic setup, and simple rollback acceptance checks.

The prototype may use a minimal local fixture or view model that conforms to repository identities and approved facts. It must not create canonical Product data, infer availability, generate a commercial SKU, or require the complete synchronization architecture. Any placeholder copy or media must be unmistakably non-authoritative and excluded from publication.

The repository remains authoritative throughout. Visible implementation may begin before advanced release bundles, automated reconciliation, broad migration, or AI work because those capabilities move to later phases after the product experience exposes their real requirements.

## Architectural Outcome

The recommended architecture is a repository-controlled platform delivered through progressive vertical slices:

```text
Founder approvals and governed evidence
                  |
                  v
GitHub repository: canonical contracts, identities, approved facts, design intent
                  |
                  v
BP1 local visible prototype
homepage -> navigation -> Pipes landing -> representative Pipe -> inquiry CTA
                  |
                  v
BP2-BP4: real Pipes model, inquiry workflow, and approved runtime boundary
                  |
                  v
BP5 staging -> BP6 synchronization -> BP7 quality/discovery
                  |
                  v
BP8 separately authorized controlled production pilot
```

### Architectural Principles

1. The repository is the canonical control plane for governed Product identities, contracts, Product Master Data, reusable content assets, mappings, and release evidence.
2. The first build proves the real user experience locally before the project invests in broad platform infrastructure.
3. Repository contracts constrain the prototype, but a minimal local adapter or fixture is sufficient until the WordPress/WooCommerce boundary is approved.
4. Theme, page-builder, custom-plugin, and child-theme choices require a short comparative architecture decision before they become implementation commitments; the WordPress/WooCommerce target boundary is defined in BP4.
5. WordPress and WooCommerce numeric IDs, slugs, post types, product IDs, variation IDs, and template state never become canonical identities.
6. WooCommerce, if selected for the runtime slice, provides catalog capabilities without public price, cart, checkout, payment, sale, discount, or Offer schema.
7. Every phase is reversible and carries proportionate validation, backup, rollback, security, accessibility, mobile, and Persian RTL gates.
8. Search, SEO, analytics, synchronization, migration, and future AI are later derived consumers. None may invent or approve Product facts.
9. Production access, publication, migration, and deployment each require a separate exact Founder authorization.

## Recommended Project Architecture

| Layer | Canonical responsibility | Recommended implementation boundary | Must not own |
| --- | --- | --- | --- |
| Governance | Approval, lifecycle, ownership, provenance, release gates | Founder decisions and reviewed repository records | Runtime convenience decisions |
| Product Repository | Contracts, stable identities, hierarchy, attributes, units, Master Data, valid Variant Rules, derived SKU records after approval | `repository/data/` canonical paths and validators | WordPress/WooCommerce IDs, presentation, public price |
| Experience prototype | Reusable design tokens, responsive layout, page composition, and local fixtures | Small local-only vertical slice in BP1; exact implementation technology approved within the wave | Canonical Product facts, production behavior, vendor lock-in |
| Content Repository | Reusable approved content, localization, relationships, rights, review status | `repository/content/` after a separately approved content contract | Page-builder layout state or WordPress revision metadata |
| Knowledge Repository | Governed Knowledge assets linked by stable identities | `repository/knowledge/` after Product identity dependencies and a separate authorization are satisfied | Product or commercial authority |
| Integration Adapter | Map approved repository records through supported runtime interfaces | Minimal boundary in BP4; advanced packaging and reconciliation in BP6 or later | Canonical Product facts, theme rendering, direct database writes |
| WordPress Runtime | Pages, posts, media, users, roles, editorial workflow, revisions, supported APIs | WordPress Core and approved single-owner capabilities | Canonical Product identity or unreviewed business truth |
| Commerce Runtime | Inquiry-first catalog projection and valid selectable variations | WooCommerce with transaction surfaces disabled | Public pricing, canonical hierarchy, speculative combinations |
| Presentation | Site shell, templates, responsive behavior, and bounded composition | Theme/page-builder/child-theme approach pending comparative Founder decision | Product rules, data authority, schema authority |
| Discovery | Search index, filters, SEO metadata, redirects, sitemaps | BP7 single-owner capabilities fed by approved public projections | Independent facts, uncontrolled indexable archives |
| Operations | Environments, secrets, backup/restore, deployment, monitoring | Approved external services and least-privilege runbooks | Canonical content or approval authority |

## Repository to WordPress Relationship

The repository supplies approved source identities and facts. WordPress remains the target content-management and publication runtime, but it is not a BP1 prerequisite and enters implementation only after the visible experience proves the required BP4 integration boundary.

| Concern | Repository ownership | WordPress ownership | Synchronization rule |
| --- | --- | --- | --- |
| Stable identity | Canonical entity and content IDs | Mapping to post, term, attachment, and user-facing URL IDs | Mapping is stored separately and never changes canonical identity |
| Approved reusable content | Source content, locale, provenance, lifecycle, relationships | Draft/publish state, revisions, scheduled publication, runtime-only editorial notes | Repository content enters as Draft unless a separately approved publication gate permits otherwise |
| Media | Rights metadata, source identity, intended relationships | Attachment storage, renditions, delivery metadata | Binary transfer requires rights, checksum, privacy, and rollback validation |
| Navigation and pages | Information architecture and approved content intent | Menus, page records, revisions, runtime assembly | Runtime IDs are returned only as reconciliation evidence |
| Roles and workflow | Capability requirements and approval gates | WordPress users, roles, capabilities, editorial workflow | Least privilege; no role grants Founder authority |

BP1 does not require WordPress. If WordPress is selected in BP4, direct database mutation is prohibited and the integration must use supported WordPress APIs and documented extension points.

## Repository to WooCommerce Relationship

WooCommerce remains the target catalog runtime, but it is not a BP1 prerequisite, its exact mapping is decided in BP4, and it never becomes the canonical Product Repository.

- Canonical Product entities and Variant Rules retain stable repository IDs independent of WooCommerce.
- The exact mapping from `Family`, `Series`, and `Variant Rules` to variable parents and variations is defined per approved Product profile; no universal one-to-one mapping is assumed.
- A Variable Parent Product may present a Family or another coherent commercial grouping but never replaces the canonical hierarchy.
- Only approved combinations are projected. A Cartesian product is never used as evidence of availability.
- WooCommerce attributes reference canonical Attribute and Unit definitions through explicit mapping records.
- Commercial SKU generation occurs only after approved Product modeling and a separately authorized SKU policy.
- Public price fields, price ranges, sales, cart, checkout, payment, and Offer schema remain disabled and are tested across HTML, APIs, feeds, caches, email, search, and structured data.
- WooCommerce stock or visibility values may be projections only after source authority, freshness, wording, and failure behavior are approved.

## Repository to Custom Plugin Relationship

Custom plugin work begins only if BP4 proves that native configuration and approved capabilities cannot provide the required boundary. The provisional **Damavand Platform Bridge** remains a replaceable later adapter; its necessity, name, modules, and package path are Founder decisions. BP1–BP3 must not wait for it.

### Proposed Plugin Modules

| Module | Responsibility |
| --- | --- |
| Input reader | Read an approved local input and validate version and environment compatibility; advanced release manifests are deferred |
| Contract validator | Reject invalid or unsupported records before any runtime write |
| Identity mapper | Maintain canonical-ID-to-runtime-ID mappings with uniqueness and lifecycle controls |
| Difference planner | Later produce a human-readable create/update/archive/no-op plan without mutation |
| Product projector | Apply approved catalog and attribute projections through WooCommerce interfaces |
| Content projector | Apply approved content and media projections through WordPress interfaces |
| Discovery projector | Apply approved SEO, redirect, synonym, and search-index metadata through one owner per concern |
| Inquiry context adapter | Pass canonical Product context into the approved Inquiry workflow without invoking checkout |
| Reconciler | In BP6 or later, compare expected and actual runtime state without automatically changing repository truth |
| Audit and recovery | Record operation identity, actor, time, result, affected mappings, errors, and rollback point without logging secrets or protected inquiry data |

### Plugin Safety Contract

- Fail closed on an unknown contract version, missing approval evidence, invalid mapping, secret exposure, partial dependency, or environment mismatch.
- In BP4, separate validation from any write. Add `plan`, `apply`, `reconcile`, and `rollback` operations only as BP6 requires them.
- Require an exact environment and explicit approval for every runtime write.
- Add idempotency, ordering, and release identity when automated synchronization begins; they are not BP1 blockers.
- Use supported APIs and transaction-safe batches; never edit Core, vendor packages, theme files, or the database directly.
- Keep secrets in an approved secret manager or runtime credential facility, never in Git or synchronization inputs.
- Expose no automatic repository write-back.

## Repository to Theme Relationship

The repository provides design intent, reusable tokens, content relationships, and presentation requirements. It does not decide the implementation package merely by naming a preferred stack.

- BP1 defines portable design tokens and visible acceptance criteria before selecting a long-term theme or page builder.
- A short BP1/BP4 comparative architecture decision must assess at least native block/theme capabilities, Blocksy Pro, Elementor Pro where relevant, and the minimum child-theme or custom-code boundary.
- The comparison must cover repository fit, RTL/mobile quality, accessibility, performance, WooCommerce/inquiry behavior, maintainability, exportability, licensing, security, upgrade risk, Founder Admin usability, and rollback.
- Existing repository references to Blocksy Pro and Elementor Pro are design inputs whose lifecycle and explicit approval evidence must be verified; this roadmap does not lock them in.
- No-child-theme is not assumed by this roadmap. Any child-theme or custom-theme proposal must identify the exact governed need, conflict with existing constraints, maintenance cost, migration path, and explicit Founder approval.
- Dynamic templates read WordPress/WooCommerce projections by stable mappings; template-local copied Product facts are prohibited.
- Theme and page-builder exports are implementation artifacts, not canonical business or Product sources.
- Vendor-file modification remains prohibited.
- Every visual release must pass Persian RTL, mobile, accessibility, inquiry-only, no-price, performance, and rollback checks.

## Product Configurator Architecture

The Product Configurator is a governed selection interface over approved Variant Rules, not a Product generator. BP1 may show only the representative Product presentation and inquiry CTA. BP2 may add a narrow Pipes configuration interaction after the underlying rules are approved; a broad configurator is not a prerequisite for the first visible milestone.

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

Synchronization is deliberately deferred to BP6. The local prototype and first Pipes experience use a bounded, reviewable fixture or manually prepared adapter that references canonical IDs and approved facts. This avoids coupling visible-product progress to a complete synchronization platform.

### Progressive Synchronization Flow

1. **BP1 local fixture:** Render one representative Pipe experience from a transparent, local-only, non-canonical fixture that references repository concepts.
2. **BP2 governed Pipes data:** Replace placeholder facts with the smallest Founder-approved Pipes family records and Variant Rules.
3. **BP4 integration boundary:** Define stable runtime mapping and supported interfaces without building the full release system.
4. **BP5 staging import:** Apply a manual or minimal automated bounded dataset with backup and rollback evidence.
5. **BP6 synchronization:** Add automated validation, mapping, dry-run planning, idempotent apply, reconciliation, and rollback.
6. **Later hardening:** Add immutable release bundles, checksums, broader content synchronization, advanced drift management, and multi-consumer release orchestration only when scale requires them.

### Synchronization Controls

- **Direction:** Approved repository input to runtime. Runtime-to-repository is evidence-only.
- **Granularity:** Entity and field ownership are explicit. Undeclared fields block synchronization.
- **Identity:** Canonical IDs map to runtime IDs in a versioned mapping store with uniqueness constraints.
- **Idempotency:** From BP6, reapplying the same approved input produces no additional change.
- **Ordering:** From BP6, synchronization operations apply in sequence and declare contract and dependency versions.
- **Deletion:** Hard deletion is not the default. Deprecation, archive, replacement, and redirect behavior are planned explicitly.
- **Conflict handling:** Repository-owned drift blocks or is overwritten only by the approved plan. Runtime-owned fields are preserved. Ambiguous ownership stops the operation.
- **Partial failure:** Stop the batch, retain completed-operation evidence, and execute the pre-approved rollback or forward-recovery plan.
- **Reconciliation:** From BP6, report missing, extra, changed, orphaned, stale, and unmapped records by canonical ID.
- **Freshness:** Once automated synchronization exists, administrators can see the active input version and health state without exposing sensitive public detail.

## Content Synchronization Strategy

Advanced content synchronization is later work. BP1 keeps its small Persian prototype copy local and reviewable. BP2–BP3 replace only the content needed for the real Pipes and Inquiry slices. Broader synchronization follows BP6 discipline and respects editorial workflow:

1. Define a content contract for stable identity, locale, content type, source, provenance, lifecycle, access class, relationships, media references, SEO intent, and review evidence.
2. Keep reusable approved source content in the repository and project it into WordPress as a Draft by default.
3. Preserve WordPress-owned workflow fields such as revision history, scheduled time, editor notes, and publication state unless a future contract explicitly assigns them elsewhere.
4. Represent theme or page-builder composition as a derived presentation artifact. Canonical text and Product facts remain outside template-local storage.
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

Phase 1 includes no product-facing or operational AI runtime. AI architecture and activation are outside BP1–BP8 and must not delay the visible prototype, Pipes family, inquiry workflow, staging, synchronization, or production-pilot decisions.

The platform should become AI-ready without activating AI by:

- preserving machine-readable contracts, stable IDs, provenance, status, access class, locale, and supersession;
- separating approved facts from candidates, missing values, and derived presentation;
- defining read-only retrieval interfaces over approved public Knowledge and Product projections;
- preparing evaluation cases for citation accuracy, access control, Persian language, abstention, and prohibited pricing claims; and
- recording model, provider, privacy, retention, cost, observability, human review, and shutdown requirements as unresolved future decisions.

A future post-BP8 AI feature requires a separate Founder-approved architecture and implementation wave. It must retrieve from approved sources, cite them, abstain when evidence is missing, respect access controls, and never create Product truth, commercial approval, price, compatibility, availability, or publication authority.

## Build Order

1. **BP1 — Visible Local Prototype:** Put a locally runnable Persian RTL homepage shell, navigation, Pipes landing, representative Pipe page, and inquiry-first CTA in front of the Founder.
2. **BP2 — First Product Family: Pipes:** Replace the thin prototype model with the smallest governed Pipes family data and narrow configuration behavior.
3. **BP3 — Inquiry Workflow:** Make the visible inquiry journey functional in a local, privacy-safe environment without checkout or public pricing.
4. **BP4 — WordPress/WooCommerce Integration Boundary:** Define the target runtime mapping, compare and decide the theme/page-builder/child-theme/plugin boundaries, then prove the minimum supported adapter.
5. **BP5 — Staging Deployment:** Reproduce the approved slice in an isolated staging environment with access, backup, restore, monitoring, and rollback.
6. **BP6 — Product Data Synchronization:** Add bounded automated validation, mapping, dry run, apply, reconciliation, and rollback for the Pipes slice.
7. **BP7 — SEO, Search, Performance and QA:** Harden the staging product experience and close discovery, accessibility, security, Persian RTL/mobile, and performance gates.
8. **BP8 — Controlled Production Pilot:** Deploy only a minimal separately approved pilot after explicit production authorization and verified recovery.

## Deployment Order

Execution progresses from a visible local slice to controlled production. Local execution is not deployment and must have no production credentials or network writes.

| Order | Target | Entry gate | Exit evidence | Rollback boundary |
| --- | --- | --- | --- | --- |
| 1 | Local BP1 prototype | Approved local-only scope, non-secret fixture, deterministic start/stop instructions | Founder can run and inspect all five visible surfaces on mobile and desktop; no production connection exists | Stop local process and revert the BP1 commit |
| 2 | Local integrated slice | Approved Pipes facts, inquiry/privacy rules, and selected runtime boundary | Pipes and Inquiry flows pass locally with no public pricing or transaction path | Restore local data snapshot or rebuild from the accepted commit |
| 3 | Persistent staging | Least-privilege access, sanitized data, approved packages, and verified backup/restore | End-to-end Product, Inquiry, SEO, search, RTL/mobile, accessibility, security, and performance evidence | Restore staging snapshot and previous accepted configuration |
| 4 | Founder acceptance | Staging scope frozen and all blocking checks pass | Founder records scope-specific acceptance or rejection | Return to the owning build wave; no production effect |
| 5 | Limited production pilot | Separate exact production authorization, maintenance window, verified backup/restore, monitoring, and rollback owners | Minimal approved public slice operates without critical regression | Disable pilot and restore prior release/data/configuration |
| 6 | Progressive expansion | Pilot observation window passes and each additional scope is separately approved | Each bounded expansion passes reconciliation and regression checks | Roll back only the affected expansion |

No row in this table is authorized merely by approval of this roadmap.

## Migration Strategy

Broad migration is not an early build dependency. BP1–BP4 use new local-only artifacts and the smallest approved data slice. Migration planning begins only when BP5 has a concrete staging target and a real legacy source is identified.

1. **BP5 read-only inventory:** Identify only the sources needed for the approved staging slice.
2. **Authority classification:** Mark each relevant field as repository-owned, runtime-owned, external-authority, candidate, missing, duplicate, or prohibited.
3. **Identity map:** Preserve canonical IDs without deriving identity from slugs or runtime numeric IDs.
4. **Quarantine:** Keep unverified exports and legacy data outside canonical paths.
5. **BP6 transform and rehearse:** Convert only approved Pipes and Inquiry records, apply them to staging, and verify counts, relationships, URLs, media, and no-price behavior.
6. **BP8 pilot:** Move only the explicitly approved minimal slice after backup, restore, redirect, freeze/delta, rollback, and acceptance gates pass.
7. **Later expansion:** Broader migration, dual-system transition, decommissioning, and historical retention receive separate plans when actual scale and sources are known.

## Build Waves

Complexity estimates are relative: **Low** is primarily bounded documentation or configuration; **Medium** combines contracts and tested integration work; **High** spans multiple systems or sensitive migration; **Very High** includes production cutover or broad operational risk.

| Wave | Objective | Expected output | Complexity | Dependencies | Rollback strategy |
| --- | --- | --- | --- | --- | --- |
| BP1 — Visible Local Prototype | Build the first visible vertical slice and make it locally runnable without production connectivity | Homepage shell, main navigation, Pipes landing, representative Pipe page, inquiry-first CTA, no pricing, reusable tokens, Persian RTL/mobile behavior, accessibility/security smoke tests, start/stop instructions, and theme/page-builder comparison brief | Medium | Approved BP1 scope; representative content boundaries; local toolchain | Stop local process; revert BP1 commit; no external state exists |
| BP2 — First Product Family: Pipes | Replace the thin fixture with the smallest governed real Pipes family model and narrow configuration behavior | Approved Pipes family records, attributes/units, representative Product presentation, allowed Variant Rules, content/media references, and Product tests; no speculative combinations | High | BP1 visual acceptance; Founder-approved Pipes evidence; existing contracts | Revert candidate records before approval or supersede them after adoption; restore BP1 fixture |
| BP3 — Inquiry Workflow | Implement the end-to-end inquiry-first interaction for the representative Pipe without commerce transactions | Accessible local inquiry form/context, consent and privacy handling, validation, success/failure states, protected storage or approved mock boundary, and no cart/checkout/payment | High | BP1–BP2; Founder approval of fields, consent, routing, retention, and security | Disable inquiry feature; remove local protected test data; restore static CTA |
| BP4 — WordPress/WooCommerce Integration Boundary | Define the target runtime mapping, make the short presentation-architecture decision, and prove only the minimum runtime boundary | Approved Product/content/Inquiry mapping to WordPress/WooCommerce; Founder decision on theme, page builder, child-theme/custom-code boundary, capability ownership, supported versions, and a local integration proof using supported APIs | High | BP1–BP3 evidence; governance review; license/version/security data | Remove local proof package/configuration; return to the accepted local prototype |
| BP5 — Staging Deployment | Reproduce the accepted visible slice in isolated staging without production mutation | Staging environment, least privilege, secrets handling, sanitized data, backup/restore proof, monitoring, reproducible deployment, and Founder UAT URL | High | BP4 decisions; hosting approval; operations/security owners | Destroy/rebuild staging or restore baseline snapshot; revoke temporary access |
| BP6 — Product Data Synchronization | Automate only the approved Pipes projection after runtime boundaries are proven | Validated mapping, dry-run plan, idempotent bounded apply, reconciliation, audit evidence, rollback, and positive/adversarial tests | Very High | BP2, BP4, BP5; source/field authority; backup/restore | Apply prior accepted input or restore staging; disable synchronization and retain canonical records |
| BP7 — SEO, Search, Performance and QA | Harden the complete staging slice for discovery, speed, security, accessibility, and Persian use | SEO/schema/no-price report, Persian search and filters, redirect/canonical plan, performance budget, accessibility/security results, mobile/RTL regression suite, and resolved blocking defects | High | BP5–BP6; SEO/indexation/search decisions | Restore previous metadata/configuration/index; disable affected capability; return defects to owning wave |
| BP8 — Controlled Production Pilot | Release the smallest approved Pipes and Inquiry slice to production under explicit authority | Verified backup/restore, maintenance and rollback plan, bounded pilot, monitoring, post-release QA, reconciliation, incident ownership, and Founder expand/hold/rollback decision | Very High | BP7 pass; separate production authorization; named owners and tested recovery | Disable pilot; restore prior production data/configuration; verify public and inquiry recovery |

No wave begins automatically. Every wave requires an exact Founder-approved scope, branch, allowed paths, validation, rollback, exclusions, and stop conditions.

### Gates Required in Every Wave

- **Repository first:** Approved identities, facts, decisions, and reusable artifacts are recorded in the repository before external projection.
- **Founder controlled:** Entry, material scope changes, external writes, and exit require the applicable Founder approval.
- **No public pricing:** No public price, Offer, sale, cart, checkout, payment, or transactional behavior may appear.
- **Environment isolation:** BP1–BP4 are local only unless a later exact authorization says otherwise; BP5 is staging only; BP8 is the first possible production mutation and requires separate approval.
- **Recovery:** Every wave defines a rollback point. Local-only waves use reproducible rebuild and Git reversion; data or environment writes require verified backup and restore evidence before execution.
- **Experience quality:** Persian RTL, Mobile First, accessibility, browser behavior, performance budgets, clear failure states, and Founder usability are acceptance criteria from BP1 onward.
- **Security and privacy:** Least privilege, no committed secrets, dependency review, protected-data minimization, safe logs, and bounded external endpoints apply throughout.
- **Evidence:** Validation, changed paths, unresolved questions, rollback readiness, and GO/NO-GO are reported before the next wave.

## Milestones

| Milestone | Completion evidence | Founder decision |
| --- | --- | --- |
| M0 — Roadmap accepted | Visible-product-first sequence, safeguards, and exclusions reviewed | Approve/revise BP1 |
| M1 — Visible local prototype | Founder can locally run and inspect the Persian RTL homepage, navigation, Pipes landing, representative Pipe page, and inquiry CTA on mobile and desktop | Approve/revise the experience and authorize BP2 |
| M2 — Real Pipes slice | Approved Pipes facts and narrow Variant Rules replace the thin fixture without speculative data | Approve/revise Product slice and authorize BP3 |
| M3 — Inquiry slice | Local end-to-end inquiry behavior passes privacy, validation, accessibility, and no-transaction gates | Approve/revise Inquiry and authorize BP4 |
| M4 — Runtime boundary decided | Comparative architecture decision and local integration proof are accepted | Approve/reject staging implementation |
| M5 — Staging experience ready | Founder-accessible staging slice has recovery, security, and UAT evidence | Approve/reject synchronization |
| M6 — Staging release candidate | Product synchronization, SEO, search, performance, accessibility, security, RTL/mobile, and QA pass | Approve/reject production pilot |
| M7 — Production pilot decided | Bounded pilot is observed with no unresolved critical issue | Expand, hold, or roll back |

## Principal Risks

| Risk | Probability | Impact | Control and gate |
| --- | --- | --- | --- |
| Draft architecture is treated as approved implementation authority | Medium | Critical | Explicit lifecycle metadata; exact Founder authorization per wave |
| Infrastructure work delays visible product feedback | Medium | High | BP1 visible local prototype is the first implementation milestone |
| Prototype placeholders are mistaken for approved Product facts | Medium | Critical | Clearly marked local fixtures, canonical IDs where available, no publication, BP2 replacement gate |
| Canonical and runtime ownership diverge | High | Critical | Field ownership contract, stable mappings, drift reports, no automatic write-back |
| Invalid Product combinations or invented commercial facts appear | High | Critical | Approved Variant Rules only, provenance/status enforcement, adversarial validation |
| Public price or transaction behavior leaks through WooCommerce, extensions, APIs, feeds, schema, or cache | Medium | Critical | Exhaustive no-price/no-transaction test matrix and single-owner review |
| WordPress/WooCommerce/plugin/theme versions conflict | Medium | High | Supported-version matrix, staged upgrade rehearsal, pinned release evidence |
| Theme or page-builder choice is locked before comparison | Medium | High | BP1 comparison brief, BP4 Founder decision, portable design tokens, no vendor commitment in BP1 |
| Plugin, theme/page-builder, SEO, and search responsibilities overlap | High | High | One owner per concern and capability responsibility review before installation |
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
- positive, boundary, adversarial, failure-state, and rollback tests, with replay and reconciliation added when synchronization begins;
- secret, credential, personal-data, dependency, permission, and external-endpoint review;
- public no-price, no-Offer, no-cart, no-checkout, no-payment, and inquiry-only behavior;
- Persian language, RTL, mobile, accessibility, browser, performance, and failure-state behavior;
- search relevance, zero results, filters, indexability, canonical URLs, redirects, sitemaps, and structured data;
- backup integrity, restore evidence, observability, incident ownership, and post-change verification; and
- final repository status, exact changed paths, validation output, unresolved questions, GO/NO-GO, and rollback readiness.

A successful technical check never substitutes for Founder approval.

## Decisions Required Before BP1 Can Close

1. Approve the exact BP1 visible scope and acceptance criteria listed in this roadmap.
2. Approve the representative Pipe page's permitted local fixture facts, labels, media, and placeholder policy.
3. Approve a provisional local prototype toolchain that does not establish the long-term runtime choice.
4. Approve the short comparative architecture brief and criteria for the later Founder decision on native theme/block capabilities, Blocksy Pro, Elementor Pro, other justified presentation options, and any child-theme/custom-code boundary.
5. Assign BP1 Product/content, Persian RTL/mobile, accessibility, security, and Founder acceptance reviewers.
6. Confirm BP1 contains no production credentials, external writes, publication, Product/SKU creation, or production mutation.

Product-to-WooCommerce mapping, supported runtime versions, inquiry retention/routing, staging operations, synchronization, SEO/search, migration, and production ownership are resolved in the waves where they become necessary; they do not block the BP1 visible prototype.

## Current GO/NO-GO

- **GO:** Founder review and revision or approval of this roadmap, followed by a separate exact authorization for BP1.
- **NO-GO:** Product creation, SKU creation, plugin implementation, WordPress/WooCommerce/theme modification, synchronization, migration, publication, deployment, production mutation, and AI activation.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.2.0 | 2026-07-23 | Replaced the infrastructure-first sequence with the Founder-directed visible-product-first model; made BP1 a local Persian RTL Pipes prototype; reduced delivery to BP1–BP8; deferred synchronization, migration, release hardening, and AI; moved theme/page-builder/child-theme choices to a comparative Founder decision. |
| 0.1.0 | 2026-07-23 | Initial Build Phase 1 implementation roadmap based on the verified post-Wave 2C baseline; planning only. |
