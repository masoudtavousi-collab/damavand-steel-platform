# PP-01 Public Homepage V1 Readiness Scope v1.0

## Document Control

- **Mission:** `PP-01 — PUBLIC HOMEPAGE V1 READINESS`
- **Status:** `REVIEW`
- **Classification:** `COMMERCIAL PUBLIC-PREVIEW PREPARATION`
- **Authority:** Founder + Project Commander reconciliation dated 2026-09-03
- **Starting main:** `e929e99066baebb5d3d7eb23e469e0e23213ab26`
- **Branch:** `codex/pp-01-public-homepage-v1-readiness`
- **Execution boundary:** Repository documentation and Git publication only
- **Runtime authority:** `NONE`
- **Production authority:** `NONE`
- **Publication authority:** `NONE`

## Decision and Objective

The approved direction is **Public Preview First + Progressive Enablement**. PP-01 prepares a credible Persian, mobile-first, inquiry-first homepage specification so the current unattractive Coming Soon experience can be replaced in a later separately authorized Mission while deeper platform work continues.

`PUBLIC PREVIEW ≠ FORMAL PUBLIC LAUNCH`

This package is planning evidence. It does not remove Coming Soon, configure WordPress, publish content, deploy code, or make the site public.

## Task Context Envelope

### Authority

The PP-01 Mission plus the Commander Reconciliation are the only execution authority for this package. They authorize creation of the exact branch, modification of the exact five files below, local validation, one commit, push, and one Draft PR. They do not authorize merge, runtime work, production work, publication, deployment, or PP-02.

### Live Main SHA

The required and verified starting `origin/main` is:

`e929e99066baebb5d3d7eb23e469e0e23213ab26`

### Objective

Prepare an implementation-ready but non-executable Public Homepage V1 package that fixes structure, approved copy, ownership boundaries, responsive behavior, fail-closed content rules, asset requirements, future SEO posture, and a gated PP-02 runtime plan.

### Role

Codex acts only as the bounded repository Build Engine and documentation author. Founder retains decision and visual approval authority. Project Commander retains scope, gate, and execution authority. Future runtime operators may act only under a separate PP-02 authorization.

### Allowed Paths and Systems

Exactly these five repository paths may change:

1. `docs/CURRENT_PROJECT_STATE.md`
2. `docs/17_FOUNDER_DECISION_LOG.md`
3. `docs/PP_01_PUBLIC_HOMEPAGE_V1_READINESS_SCOPE_V1.0.md`
4. `docs/PP_01_PUBLIC_HOMEPAGE_V1_SPEC_V1.0.md`
5. `docs/PP_01_PUBLIC_HOMEPAGE_V1_RUNTIME_PLAN_V1.0.md`

Allowed systems are the isolated local Git worktree, the exact PP-01 branch, the configured repository remote for pushing that branch, and GitHub for opening one Draft PR. No other remote or live system is in scope.

### Explicit No-Go

- No sixth changed repository path.
- No changes to `AGENTS.md`, validators, tests, schemas, Product Data, registries, workflows, deployment files, FT-RB packages, C010 packages, or PRs 59–61.
- No WordPress, WooCommerce, Blocksy, Elementor, hosting, DNS, TLS, Runtime, Staging, Production, cache, indexing, analytics, or external-service mutation.
- No Coming Soon removal, publication, deployment, formal public launch, merge, branch deletion, or PP-02 execution.
- No public price, cart, checkout, payment, public stock/availability/ETA/SLA promise, public `Offer` schema, or enabled fake interaction.
- No invented Product, combination, specification, availability, inventory, supplier, customer, address, certification, license, representation, social, delivery, leadership, or performance fact.
- No Trust, privacy, security, backup/restore, approval, or Founder-review bypass.
- No secrets, credentials, raw private evidence, or PII in repository artifacts.

### Dependencies

- Exact Founder decision: **Public Preview First + Progressive Enablement**.
- Effective Inquiry First, No Public Pricing, Product Data First, fail-closed, Persian RTL, mobile-first, and evidence-provenance controls.
- Blocksy shell ownership and Elementor homepage-body ownership.
- Rights-cleared brand/media inputs and final visual choices before runtime execution.
- Separately authorized PP-02, exact Production target identification, verified backup/restore, rollback ownership, package/license compatibility, and Founder visual checkpoint before any mutation.
- Lane A security clearance remains external and unresolved; PP-01 does not change it.

### Required Sources

The author must use the PP-01 Mission and reconciliation together with:

- [`AGENTS.md`](../AGENTS.md)
- [Current Project State](CURRENT_PROJECT_STATE.md)
- [Context Router](CONTEXT_ROUTER.md)
- [Project Baseline](PROJECT_BASELINE.md)
- [Source of Truth Priority](SOURCE_OF_TRUTH_PRIORITY.md)
- [AI Collaboration Standard](AI_COLLABORATION.md)
- [Codex Sprint Protocol](CODEX_SPRINT_PROTOCOL.md)
- [Git Governance](GIT_GOVERNANCE.md)
- [ADR-0001 Inquiry First Commerce](adr/0001-inquiry-first-commerce.md)
- [Design Manifest](../repository/design/DESIGN_MANIFEST.md)
- [Brand Language](../repository/design/BRAND_LANGUAGE.md)
- [Accessibility Rules](../repository/design/ACCESSIBILITY_RULES.md)
- [Motion System](../repository/design/MOTION_SYSTEM.md)
- [Performance Rules](../repository/design/PERFORMANCE_RULES.md)
- [Component Pattern Library](../repository/design/COMPONENT_PATTERN_LIBRARY.md)
- [Blocksy Configuration Blueprint](36_BLOCKSY_CONFIGURATION.md)
- [Elementor Architecture Blueprint](37_ELEMENTOR_ARCHITECTURE.md)
- [Content Architecture](29_CONTENT_ARCHITECTURE.md)
- [Media Strategy](33_MEDIA_STRATEGY.md)
- [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)
- [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md)
- [URL Architecture](26_URL_ARCHITECTURE.md)
- [Internal Linking Model](28_INTERNAL_LINKING_MODEL.md)
- [SEO Entity Model](34_SEO_ENTITY_MODEL.md)
- [Execution Gates](EXECUTION_GATES.md)
- [DS Program Charter](DS_PC_001_PROGRAM_CHARTER.md)
- [DS Strategic Program Directive](DS_SPD_001_STRATEGIC_PROGRAM_DIRECTIVE.md)
- [BP1 Local Prototype Notes](../prototypes/bp1-visible-local/README.md)

The local prototype is reference evidence only; it is not authority for final copy, color, typography, media, layout, Product truth, or runtime behavior.

### Active WIP and Temporary Exception

At mission start, PRs 59, 60, and 61 consume the normal three writer slots. `WIP_EXCEPTION_PP01 = APPROVED` permits this one isolated docs-only PP-01 lane because its exact five-path allowlist does not collide with those PRs.

The exception:

- applies only to this Mission and exact branch;
- permits no modification, merge, comment-side mutation, or state change to PRs 59, 60, or 61;
- does not change Lane A, the launch counter, or any runtime/production gate; and
- expires when PP-01 completes, stops, merges, or closes—whichever occurs first.

### Stop Conditions

Stop immediately and report if:

- the diff exceeds the exact five-path allowlist;
- any WordPress, Runtime, Staging, Production, deployment, indexing, or Coming Soon mutation becomes necessary;
- any existing PR would be changed;
- a Product, commercial, contact, brand, media-right, availability, or performance fact would have to be invented;
- architecture, Lane A status, or launch counter would change;
- a secret, credential, private evidence payload, or unapproved PII is encountered; or
- a material validation failure cannot be corrected within the exact five paths.

The normal WIP count is not a stop condition because the PP-01 exception is explicit and bounded.

### Validation

Before Git publication, verify:

1. starting main and branch identity;
2. exact changed-path count of five and zero unexpected paths;
3. `git diff --check`;
4. all local Markdown links and anchors introduced by PP-01;
5. repository scaffold validation and the applicable repository test suite;
6. no secret, credential, prohibited PII, public price, `Offer` schema, inventory/availability promise, forbidden marketing claim, or invented Product truth;
7. no Runtime, WordPress, deployment, workflow, FT-RB, C010, or existing-PR mutation;
8. preservation of PRs 59–61, Lane A blocked state, launch counter 8, and all no-go declarations;
9. pushed branch head equals local committed head; and
10. Draft PR title, body disclaimer, head branch, base branch, and Draft state.

Pre-existing findings must be distinguished from changes introduced by PP-01. Unrelated findings must not be repaired under this authority.

### Custody and Checkpoints

The material artifact is the five-file Git tree. Generate it, hash it through the commit/tree identities, classify it as `REVIEW / IMPLEMENTATION-READY PACKAGE / NOT_DEPLOYED / NOT_PUBLISHED`, preserve it in the local commit and pushed branch, read back the remote head and changed-path set, and report the result. The Draft PR is the review surface, not approval or runtime evidence.

Checkpoint and stop review occurs after authoring, validation, commit, push, and Draft PR creation. Any scope expansion requires new Commander authority.

### Return Contract

The final report must return:

- `MISSION_STATUS`
- `STARTING_MAIN_SHA`
- `WIP_EXCEPTION_STATUS`
- `BRANCH`
- `COMMIT_SHA`
- `PUSH_STATUS`
- `DRAFT_PR`
- `DRAFT_PR_HEAD_SHA`
- `FILES_ADDED_MODIFIED`
- `EXACT_PATH_ALLOWLIST_STATUS`
- `FOUNDER_DECISION_RECORDED`
- `CURRENT_STATE_PP01_RECORDED`
- `HOMEPAGE_STRUCTURE`
- `DESIGN_SYSTEM_STATUS`
- `CONTENT_MATRIX_STATUS`
- `ASSET_REQUIREMENTS_STATUS`
- `BLOCKSY_ELEMENTOR_OWNERSHIP_STATUS`
- `RESPONSIVE_STATUS`
- `SEO_NO_PRICE_STATUS`
- `RUNTIME_PLAN_STATUS`
- `VALIDATION`
- `PR59_MUTATION = NO`
- `PR60_MUTATION = NO`
- `PR61_MUTATION = NO`
- `PRODUCTION_MUTATION = NO`
- `RUNTIME_MUTATION = NO`
- `DEPLOYMENT_PERFORMED = NO`
- `MERGE_PERFORMED = NO`
- `MATERIAL_FINDINGS`
- `COMMANDER_REVIEW_REQUIRED = YES`
- `NEXT_ACTION`

## Required Outputs

This five-file package provides:

- the bounded scope and Task Context Envelope in this document;
- the IA, content matrix, design system, ownership model, responsive rules, asset manifest, Elementor build map, and Founder visual checklist in the [Public Homepage V1 Specification](PP_01_PUBLIC_HOMEPAGE_V1_SPEC_V1.0.md); and
- the exact future target, preflight, backup, implementation, QA, rollback, Coming Soon removal gate, and progressive-enablement plan in the [PP-02 Runtime Plan](PP_01_PUBLIC_HOMEPAGE_V1_RUNTIME_PLAN_V1.0.md).

## Completion Boundary

PP-01 ends after the one Draft PR is opened and reported. The Draft PR must remain unmerged and not Ready for Review. PP-02 does not start automatically.
