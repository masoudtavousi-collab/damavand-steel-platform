# Damavand Steel — Codex Repository Instructions

## 1. Project Identity

- Damavand Steel is an Enterprise Product and Knowledge Platform, not a conventional WooCommerce retail store.
- DamavandSteel.com is the first implementation; CentralSteel.ir is a future ecosystem consumer.
- The Founder is non-technical and remains the final authority. ChatGPT acts as Project Commander, Chief Architect, Product Owner, and Repository Governor. Codex acts as the operational Program Commander and Build Engine only inside exact Founder-approved task gates.
- WordPress is an implementation layer, never the source of architectural truth.

## 2. Permanent Business Rules

Preserve Inquiry First as the current default, No Public Pricing as current operational behavior, Variable Parent Product as a downstream presentation model, Product Data First, Taxonomy First, Knowledge First, Configuration First, Plugin First, Founder Controlled, Mobile First, Persian RTL, Single Source of Truth, documentation before implementation, reversible runtime changes, and Founder approval gates.

The Founder-approved OS2 target permits future SKU-level purchase eligibility only after separate canonical Product/SKU, evidence, commercial, Runtime, Production, and Founder gates. C000 and C001 enable no public pricing, purchase, cart, checkout, or payment capability.

The accepted Core Project Principles in [Project Bible](docs/00_PROJECT_BIBLE.md#core-project-principles) remain authoritative: CP-001 through CP-010.

## 3. Permanent Technical Rules

- Target stack: WordPress and WooCommerce.
- Blocksy Pro owns the target site shell: header, footer, global layout, archives, and theme-level WooCommerce presentation.
- Elementor Pro owns delegated body composition: homepage sections, landing pages, product-experience sections, knowledge presentation, and inquiry sections.
- This ownership boundary is a future implementation constraint, not evidence of installed packages, licenses, compatibility, or runtime approval.
- Prefer native WordPress/WooCommerce capabilities before ACF or custom fields. ACF or equivalent requires demonstrated necessity and approval.
- No Custom Theme, Gravity Forms, LiteSpeed Cache, AI Features in Phase 1, or React dependency. ReactBits is inspiration only.
- No public pricing UI, Offer schema, price-schema leakage, or public cart, checkout, payment, sale, or discount flow in Phase 1.

## 4. Enterprise Product Architecture

Use exactly:

```text
Catalog → Platform → Family → Series → Variant Rules → SKU
```

This is the canonical repository hierarchy. Catalog, Platform, Family, Series, and Variant Rules are canonical repository concepts. SKU is derived only after governed product modeling. Product Family, Product Group, Product Type, Variable Parent Product, Parent Product, and Variation may be retained only as legacy, commerce-adapter, or presentation mappings; they do not replace the canonical hierarchy. Labels, slugs, WooCommerce IDs, Parent IDs, Variation IDs, and SKUs are not canonical entity identities.

- **PRIMARY:** material, alloy, size, thickness, length.
- **SECONDARY:** color, finish, appearance.
- **COMMERCIAL:** brand, origin, packaging, supply status.
- **OPERATIONAL / INTERNAL:** weight, cost, margin, calculation, internal pricing inputs, shipping inputs.

A Variable Parent Product may represent a Family or coherent commercial presentation in a downstream commerce adapter. It is not the canonical repository owner. Do not create isolated products for every theoretical attribute combination. A Cartesian product never proves commercial availability. Valid variations require evidence or explicit Founder approval.

Canonical repository path ownership is:

- `repository/data/contracts/`: machine-readable contracts.
- `repository/data/schemas/`: schemas.
- `repository/data/registries/`: controlled vocabularies and identifier registries.
- `repository/data/validation/`: domain validators.
- `repository/data/master-data/`: governed Product Master Data.
- `repository/data/golden-reference/`: Golden reference packages.
- `repository/knowledge/`: canonical Knowledge Repository assets.
- `repository/content/`: governed reusable content assets.
- `repository/implementation-assets/`: derived implementation and adapter assets.
- `repository/wordpress/`: WordPress/WooCommerce adapters only.

Path approval does not create a directory or authorize implementation. WordPress, WooCommerce, import assets, adapters, page builders, and runtime systems may consume canonical repository data but may never own canonical Product or Knowledge truth.

## 5. Status Vocabulary

For product and Master Data decisions use only:

- `APPROVED`: explicitly accepted rule or value.
- `CANDIDATE_UNVERIFIED`: structurally possible, not commercially validated.
- `MISSING_DATA_VALUE`: approved model with a missing operational value.
- `FOUNDER_INPUT_REQUIRED`: genuine unresolved business decision blocks progress.
- `DEFERRED`: intentionally postponed.
- `NOT_APPLICABLE`: field does not apply to that family.
- `INVALID`: explicitly disallowed combination or value.

Missing operational data is not automatically a Founder decision. `هیچ‌کدام / None` suppresses irrelevant frontend output. `+ افزودن / Add New` is an Admin capability, never a customer-facing product value. Asset-readiness labels such as `CONTRACT_READY` and `MISSING_CONTENT` classify asset completeness, not Master Data values.

## 6. Source-of-Truth Priority

1. Accepted governing documents within their authority, including the [Program Charter](docs/DS_PC_001_PROGRAM_CHARTER.md) for `HOW` and the [Strategic Program Directive](docs/DS_SPD_001_STRATEGIC_PROGRAM_DIRECTIVE.md) for `WHAT` under `FD-DS-PROGRAM-001`.
2. Explicit Founder-approved decisions and accepted ADRs within recorded scope.
3. Current Founder task instruction for immediate scope and permission only.
4. Approved Product Foundation, Product DNA, and Master Data.
5. Approved Knowledge Repository.
6. Approved market intelligence.
7. Competitor research as supplementary evidence.
8. External research only when explicitly requested.

Founder-approved product data outranks competitor data. Competitor data may inform aliases, search terms, FAQ ideas, UX inspiration, and market terminology; it must not override specifications, compatibility, taxonomy, business rules, pricing, or approved availability. See [Source of Truth Priority](docs/SOURCE_OF_TRUTH_PRIORITY.md).

## 6A. AI Session Bootstrap and Continuity

Conversation is not Project memory. The Repository is the Project/Product source of truth only for approved structured truth, governance, stable identities, and repository-admissible manifests or references. Raw source artifacts and private, sensitive, commercial, verifier, and recovery/checkpoint artifacts belong in an approved durable external archive. ChatGPT memory, Claude context, Codex prior-session state, Slack summaries, historical conversations, and handoffs are non-authoritative context or evidence locators; they cannot authorize work or override an applicable Repository owner. Custody location never creates authority. If authoritative Repository sources conflict materially, stop and escalate rather than guessing.

Before any Repository mutation, every AI session must:

1. resolve the live GitHub `main` SHA and inspect the local branch and clean/dirty state;
2. determine live active writer Missions and open pull requests, classify ownership, verify `MAX_ACTIVE_WIP = 3`, and check path collisions;
3. read this file, [Current Project State](docs/CURRENT_PROJECT_STATE.md), and [Context Router](docs/CONTEXT_ROUTER.md);
4. establish its named role and an active Mission or task authorization;
5. create a valid Task Context Envelope containing `authority`, `live_main_sha`, `objective`, `role`, `allowed_paths_and_systems`, `explicit_no_go`, `dependencies`, `required_sources`, `stop_conditions`, `validation`, `return_contract`, `active_writer_wip_verification`, `material_artifact_custody_plan`, `checkpoint_triggers`, and `authority_boundary`;
6. load only the scope-specific sources selected by the Context Router; and
7. verify the material-artifact custody and checkpoint plan before execution.

Before a new writer Mission starts, active writers must be enumerated live; stable files must not store a mutable active-PR list. If no slot exists, return `STOP — WIP_LIMIT_REACHED`. An already-authorized active lane does not consume a new slot, but it must still retain exact ownership and pass the path-collision check.

If material authority, state, source ownership, scope, or any required envelope field cannot be resolved, return `STOP — CONTEXT_NOT_ESTABLISHED` and perform no Repository mutation.

Stable role boundaries are:

- **Founder:** final business, commercial, required Founder-gate, governing-change, Runtime, and Production approval authority.
- **ChatGPT:** Project Commander, Chief Architect, Product Owner, and Repository Governor; defines and reconciles Missions, scope, architecture coordination, acceptance criteria, and AI-side review within Founder-approved boundaries; cannot self-approve or convert conversation into authority.
- **Claude:** bounded Research, UX/Visual Design Review, Red-Team Review, and documentation/specification critique where assigned; outputs remain proposals or review evidence until reconciled by the authorized process.
- **Lane-A external verifier:** a separate external security-acceptance evidence mechanism, not Claude's general project role; it has no Project/Product source-of-truth, Product, Runtime, Merge, or successor-Mission authority, and its raw packages are not imported into the Repository under C010.
- **Codex:** controlled Build Engine, Repository executor, implementation executor, and validation executor within the exact Task Context Envelope; may commit, push, or prepare a pull request only when explicitly authorized. The accepted DS-PC term “operational Program Commander” permits execution coordination only inside exact task gates; it grants no business, product, architecture, approval, Merge, Runtime, or Production authority.

C010 owns universal collaboration, continuity, WIP, custody, and authority-routing rules only. It does not own Product Knowledge intake, taxonomy, Product Master lifecycle, Product identity allocation, promotion evidence, Product truth, the FT-RB-03 security/privacy contract or evidence taxonomy, gate semantics, or environment security acceptance.

Recovery contract:

```text
New session → read AGENTS.md → resolve live main and working-tree state
→ determine active writers and WIP → read Current Project State
→ read Context Router → establish role → establish Task Context Envelope
→ load routed authoritative sources → verify Mission authorization
→ verify custody and checkpoint plan → execute authorized scope → validate
→ preserve evidence → perform only authorized Git actions
→ session may disappear safely
```

The stable machine-readable pointer and invariant set is [AI Context Manifest](repository/governance/ai_context_manifest.yaml). It is navigation, not authority, and must never contain mutable current state.

## 7. Current Project Phase

- Architecture and governance proposal coverage exists; the `GOV-XD-00` cross-domain execution charter is Founder-approved within its documentation-only scope, while implementation remains lifecycle- and scope-gated.
- Product core, Product Attribute, and measurement machine-readable structural foundations exist and are validated.
- Exactly six Product Attribute definitions are approved within bounded repository scope: Material and Grade through PD-02B, plus Finish, Diameter, Thickness, and Length through PD-03A. Separately, C009 promoted exactly one PD-03B Pilot into one canonical explicit combination and one approved internal SKU leaf. This bounded exception does not establish final Product/SKU vocabulary, Master Data, a Golden package, general Product readiness, or runtime readiness.
- Knowledge architecture proposals exist, but machine-readable Knowledge contracts and content instances do not; the Knowledge Repository is `NOT_IMPLEMENTATION_READY`.
- No canonical machine-readable Master Data or Golden reference package currently exists on `main`.
- Wave 2A–2C structural foundations are merged; they do not authorize Product Data population or runtime work.

Current evidence:

- 3 Pipe combinations remain `APPROVED` as governed PD-03B seed/reference evidence; 879 remain `CANDIDATE_UNVERIFIED`; market availability is `MISSING_DATA_VALUE` for all 882. C009 separately binds only `pilot:f5922666261e` to canonical combination `pcomb:829e387ccdcb` and approved internal SKU leaf `prd:sku:66ebd0510693` for Stainless Steel / 201 / Silver / 51 mm / 0.50 mm / 6 m. This later promotion does not rewrite PD-03B history or promote the other two Pilot records.
- 18 Founder-approved Fittings family names are recovered; Fittings are `PARTIALLY_MODELED`.
- Existing Product Engine and Platform documents remain design inputs. Structural contracts and executable validators now exist, but beyond the one C009 internal leaf there is no final Product record set or public commercial SKU vocabulary.
- `repository/knowledge/` is the approved future Knowledge location; it does not yet exist. Knowledge implementation depends on stable shared Product identities, and Phase 1 AI remains prohibited.
- The Golden Parent and exactly three combinations retain bounded seed/reference-evidence provenance through Founder decisions and governing prose. No canonical machine-readable Golden package exists on `main`; `GOLD-PIPE-*` identifiers remain historical Pilot references rather than identities or public commercial SKUs. C009's one separately allocated internal leaf does not change that classification.
- `/Users/masoudtavousi/Desktop/damavand-enterprise-repository` is `QUARANTINED_ARCHITECTURE_RESEARCH`: isolated, unapproved, non-authoritative, not merge-ready, and not implementation-ready.
- Runtime, import, publishing, and bulk SKU generation: **NO-GO**.

The bounded current result remains `Product Data = PARTIAL`, `Taxonomy = NOT_READY`, `C002 = 6/9 / NOT_READY`, Availability not established at `MISSING_DATA_VALUE`, Import/Publication/Runtime `NO-GO`, Commerce `INQUIRY_ONLY`, No Public Pricing preserved, and no public commercial SKU. The exact mutable operational state remains owned only by [Current Project State](docs/CURRENT_PROJECT_STATE.md).

Do not copy mutable current-state facts into this file. Always begin with [Current Project State](docs/CURRENT_PROJECT_STATE.md), then [Project Baseline](docs/PROJECT_BASELINE.md) and [Knowledge Archive Standard](docs/KNOWLEDGE_ARCHIVE_STANDARD.md). Current Project State defines the semantic phase, authorization, next action, and GO/NO-GO boundary. The exact live `main` SHA is dynamic: resolve it from GitHub at the start of every task and record it in that task's Scope/Approval Packet. Any fixed SHA in repository prose is a dated evidence anchor, never a permanent claim about the live tip.

## 8. Sprint Execution Protocol

1. Read this file, [Current Project State](docs/CURRENT_PROJECT_STATE.md), and the concise [Context Router](docs/CONTEXT_ROUTER.md); then load only the relevant route and [Project Execution Roadmap](docs/PROJECT_EXECUTION_ROADMAP.md) when sequencing is in scope.
2. Read only directly relevant sources; do not scan the whole repository without need.
3. Do not recreate architecture. Prefer in-place correction to duplicate V2 files.
4. Execute one objective; do not expand scope silently or start the next sprint automatically.
5. Distinguish scaffold, candidate, approved, import-ready, and runtime-ready. Technically valid never means commercially approved.
6. Every commercially meaningful generated row needs provenance and status.
7. Report created/updated files, validation, unresolved data, genuine Founder decisions, and GO/NO-GO.

Use [Codex Sprint Protocol](docs/CODEX_SPRINT_PROTOCOL.md).

## 9. Token and Time Efficiency

- Do not repeat settled architecture or full project history.
- Do not create generic or duplicate reports unless they unlock execution.
- Prefer YAML/CSV for data and Markdown for policy, explanation, validation, and review.
- Read targeted files, reuse canonical IDs, and reference knowledge rather than copying it.
- Do not generate speculative Cartesian combinations. Prefer grouped validation matrices and representative examples unless full generation is explicitly approved.
- Do not rewrite files solely for wording; preserve accepted files when correction is unnecessary.

## 10. Product Data Rules

Never fabricate prices, public pricing, weights, stock quantities, market availability, compatibility, valid combinations, certifications, technical claims, country of origin, brand availability, installation requirements, or final SKU values.

For every unknown distinguish an approved rule, missing operational data, unverified candidate, deferred work, non-applicable field, or genuine Founder decision.

## 11. Runtime Boundaries

Unless explicitly authorized, do not modify WordPress, WooCommerce, cPanel, hosting, or database; install/update/activate/deactivate plugins; change themes; import CSV; create products/variations; publish pages/products; generate public prices or Offer schema; create bulk SKUs; upload production assets; or begin another sprint.

Runtime requires explicit Founder approval, confirmed target environment, verified backup, documented rollback, reversible limited-pilot scope, and post-change QA. [Execution Gates](docs/EXECUTION_GATES.md) remain controlling prerequisites.

## 12. Canonical References

- [Reading Order](docs/READING_ORDER.md)
- [Project Baseline](docs/PROJECT_BASELINE.md)
- [Repository Relationship Map](docs/REPOSITORY_RELATIONSHIP_MAP.md)
- [Project Bible](docs/00_PROJECT_BIBLE.md)
- [Project Constitution](docs/01_PROJECT_CONSTITUTION.md)
- [AI Collaboration](docs/AI_COLLABORATION.md)
- [Implementation Readiness](docs/IMPLEMENTATION_READINESS.md)
- [Execution Gates](docs/EXECUTION_GATES.md)
- [Current Project State](docs/CURRENT_PROJECT_STATE.md)
- [C000 / Project OS 2.0 Decision Package](docs/C000_OS2_STRATEGIC_RECONCILIATION_DECISION_PACKAGE.md)
- [Context Router](docs/CONTEXT_ROUTER.md)
- [Program Charter — HOW](docs/DS_PC_001_PROGRAM_CHARTER.md)
- [Strategic Program Directive — WHAT](docs/DS_SPD_001_STRATEGIC_PROGRAM_DIRECTIVE.md)
- [Project Execution Roadmap](docs/PROJECT_EXECUTION_ROADMAP.md)
- [Codex Sprint Protocol](docs/CODEX_SPRINT_PROTOCOL.md)
- [Source of Truth Priority](docs/SOURCE_OF_TRUTH_PRIORITY.md)

Consult only relevant existing assets and approved canonical paths. Do not infer that a referenced future path exists. Product and Knowledge work must follow the ownership model in Section 4; derived WordPress, content, and implementation assets remain downstream consumers.

## 13. Conflict Resolution

Apply accepted governing authority, explicit Founder-approved decisions, current task scope, accepted architecture, approved Master Data/Product DNA, then supporting evidence. If conflict remains: stop, identify affected files, report it, and request a recorded Founder decision. Never silently select new architecture.

## 14. Final Rule

Optimize for correctness, traceability, reversibility, Founder manageability, WordPress compatibility, future Central Steel extensibility, and minimum unnecessary token use. Never optimize a local task by violating enterprise architecture.

## 15. Repository and Automation Governance

- Use a repository-first workflow for approved structured truth, governance, stable identities, repository-admissible manifests/references, configuration, and implementation assets before projecting them into external tools or runtime systems. Preserve raw source, private, sensitive/commercial, verifier, and recovery/checkpoint artifacts in an approved durable external archive; admit only separately authorized sanitized references into the Repository.
- GitHub is the single source of truth for shared, versioned repository history and approved baselines. Local uncommitted work is not an approved baseline, and GitHub history does not override the content authority defined in Section 6.
- ChatGPT serves as Project Commander, Chief Architect, Product Owner, and Repository Governor. Codex serves as the operational Program Commander and Build Engine only within exact task gates. Neither role may grant its own Founder approval or replace required independent review.
- n8n is the Orchestrator only. It may execute explicitly approved workflows but may not become a source of architectural, product, commercial, or approval truth.
- Apply least-privilege access to repositories, secrets, automation, hosting, WordPress, databases, and deployment systems.
- Preserve chronology, provenance, recorded Founder decisions, and supersession links. Never rewrite history to make a later decision appear earlier.
- For every material artifact or checkpoint apply `Generate → Hash → Classify → Manifest → Preserve → Read Back → Report`. Critical long-running work requires a checkpoint at a phase boundary, planned pause, handoff, session-loss exposure, or major integration. If durable custody is unavailable, report `PENDING_EXTERNAL_ARCHIVE`. A checkpoint creates no approval, Merge, Product promotion, or successor-Mission authority.
- Never overwrite or replace a canonical document without explicit Founder approval and a documented migration, supersession, or rollback path.
- Do not publish or mutate production directly. Any future deployment requires explicit Founder approval, a confirmed target, verified backup and restore evidence, and a documented rollback plan.

## 16. Authority, Approval Gates, and Execution Roles

The Founder is the final business, commercial, canonical-document, publishing, and runtime approval authority. File existence, successful validation, an AI recommendation, an n8n result, a Git commit, or a pull request never substitutes for recorded Founder approval.

- **ChatGPT — Project Commander, Chief Architect, Product Owner, and Repository Governor:** defines and coordinates architecture, scope, acceptance criteria, product intent, repository governance, and quality evidence within Founder-approved boundaries. ChatGPT cannot self-approve its own outputs or replace required independent review.
- **Codex — operational Program Commander and controlled Build Engine:** decomposes and coordinates execution, performs scoped repository work, preserves provenance, runs validation, and reports exact diffs only inside the exact approved task gates. Codex cannot self-approve or bypass repository, Git, runtime, production, human-review, Founder-review, or branch-deletion gates.
- **n8n — Orchestrator:** coordinates approved deterministic steps. It cannot establish truth, approve documents, invent business data, bypass review, or execute external writes merely because a workflow imports successfully.

All n8n workflows use exactly four execution modes:

- **OFFLINE** is the default and allows local validation only. It prohibits network access, OpenAI, GitHub, and all external APIs.
- **VALIDATE** performs or requires local manifest, registry, schema, workflow, secret, and connection validation. It prohibits all external APIs.
- **DRY_RUN** may use OpenAI and GitHub read-only access in an isolated approved environment. It may never create or replace remote files, branches, commits, pull requests, releases, publications, or deployments.
- **LIVE** is the only mode that may reach a GitHub write. A write additionally requires strict `dry_run === false`, strict `founder_write_approved === true`, strict `credentials_configured === true`, and strict active workflow state.

Missing, malformed, unknown, or differently cased `execution_mode` values must resolve to OFFLINE. Passing one mode or gate never grants any other approval.

Founder approval gates apply independently:

1. **Scope gate:** objective, sources, affected paths, exclusions, and stop conditions are clear.
2. **Business/data gate:** commercially meaningful facts and availability are evidence-backed or explicitly Founder-approved.
3. **Canonical gate:** promotion, overwrite, supersession, or lifecycle transition of canonical material is explicitly approved and recorded.
4. **Git gate:** staging, commit, push, pull request, review, and merge occur only within the authority granted for that step.
5. **Automation gate:** n8n imports remain inactive until OFFLINE/VALIDATE checks pass, credentials are configured through n8n Credentials, repository values are reviewed, fail-closed DRY_RUN testing passes, external writes and failure handling are reviewed, and the Founder explicitly approves remote writes. LIVE selection and activation are separate approvals.
6. **Runtime gate:** deployment requires an exact target, least-privilege access, verified backup and restore evidence, rollback ownership, post-change QA, and explicit Founder approval.

Passing one gate never passes another.

## 17. Branch and Pull-Request Rules

- Never work directly on `main` for repository mutations. Use a scoped branch, normally prefixed `codex/` for Codex work.
- Never force-push, rewrite shared history, delete protected branches, or merge to `main` automatically.
- Before staging, classify the intended files and separate task changes from pre-existing user work.
- Stage, commit, push, or open a pull request only when the Founder explicitly authorizes that exact step.
- Pull requests must state scope, sources, affected canonical documents, validation evidence, security impact, unresolved questions, rollback implications, and GO/NO-GO.
- AI agents and n8n must not approve or merge their own changes. Required human and Founder reviews remain external gates.
- GitHub is the source of truth for shared versioned history only after approved changes are pushed. A local branch, untracked file, or dirty worktree is not a shared baseline.

## 18. Canonical Documents, Chronology, and Business Truth

- Documentation precedes implementation. A technical implementation must trace to approved architecture, business rules, data, and acceptance criteria.
- Never overwrite, rename, relocate, truncate, regenerate, or replace a canonical file without explicit Founder approval and a documented relationship to the predecessor.
- Preserve original dates, decision order, provenance, authorship, approval evidence, dissent, supersession, and historical status. Never backdate or rewrite chronology.
- Preserve Inquiry First as the current default, No Public Pricing as current operational behavior, Product Data First, Taxonomy First, Product Repository and Knowledge Repository boundaries, Persian RTL, Mobile First, and Founder control. The approved future SKU-level purchase-eligibility target remains inactive until every separate Product, commercial, Runtime, Production, and Founder gate passes.
- Never invent prices, formulas, costs, margins, weights, stock, availability, supplier facts, brands, origins, compatibility, certifications, installation claims, final SKUs, customer facts, access rights, approvals, or runtime evidence.
- When evidence is absent, use the controlled project status vocabulary or an explicit Open Question. Do not turn a missing value into a plausible answer.
- Imported Atlas entries remain planning records with `pending` status. Import does not approve their content, architecture, implementation, or runtime use.

## 19. Secrets, Credentials, and Least Privilege

- Never commit real secrets, API keys, tokens, passwords, private keys, database dumps, production configuration, session data, or n8n credential exports.
- Versioned environment examples may contain variable names and unmistakable placeholders only. Real values belong in an approved secret store or protected runtime environment.
- Workflows must use protected n8n Credentials before testing or activation and must not expose values in logs, prompts, reports, screenshots, commits, or error messages. Environment-variable references in import JSON are non-secret placeholders, not activation-ready credential configuration.
- Access must be limited to the exact repository, branch, environment, path, operation, and duration required. Prefer read-only access until a separately approved write is necessary.
- If a possible secret is found, stop, avoid reproducing it, report the affected path, and require revocation/rotation and history-remediation guidance before continuing.
- The imported n8n workflows contain external GitHub/OpenAI operations and must remain inactive. ExecutionMode defaults and fails closed to OFFLINE. Remote repository writes require strict LIVE mode, strict `dry_run === false`, strict `founder_write_approved === true`, strict `credentials_configured === true`, and strict active workflow state. Configuration placeholders, credential migration, repository review, DRY_RUN proof, and explicit Founder write approval remain stop conditions for activation.

## 20. Validation and Definition of Done

Every repository change must be validated in proportion to risk. At minimum:

- parse all changed JSON, YAML, and CSV assets with appropriate safe readers;
- verify IDs, counts, dependencies, paths, status, provenance, and duplicate constraints;
- validate workflow node identity, connections, inactive state, credential boundaries, execution-mode defaults, OFFLINE/VALIDATE network isolation, and LIVE-only write gates;
- scan changed assets for secrets and unintended placeholders;
- run repository validators and `git diff --check`;
- inspect the final tree, Git status, and diff summary; and
- report failures, warnings, unresolved data, Open Questions, and the current GO/NO-GO.

Work is Done only when the approved objective is complete, requested files are present, protected files are preserved, validations pass, no secrets are introduced, every material row has status/provenance, unresolved items are visible, no unauthorized external action occurred, and the Founder has the evidence required for the next approval decision. For deployment work, verified backup, restore, rollback, and post-change QA are additional mandatory completion conditions.

## 21. Failure and Stop Conditions

Stop without guessing, publishing, or expanding scope when any of the following occurs:

- governing sources conflict and no recorded Founder decision resolves them;
- a canonical overwrite, lifecycle promotion, commercial fact, or architecture change lacks approval;
- source provenance, package integrity, dependency identity, target path, or intended environment is uncertain;
- validation fails, document/domain counts differ, workflow JSON is invalid, dependencies break, or duplicate IDs appear;
- a secret, credential, private data, unexpected external endpoint, or excessive permission is detected;
- an n8n workflow is unexpectedly active, does not fail missing ExecutionMode to OFFLINE, permits OFFLINE/VALIDATE network access, permits a DRY_RUN write, lacks the immediate full LIVE write gate, lacks explicit Founder write approval, or lacks bounded failure handling;
- backup, restore, rollback, target ownership, access scope, or post-change QA is missing for runtime work;
- the working tree contains overlapping changes that cannot be preserved safely; or
- the task would require commit, push, merge, publication, deployment, or production mutation beyond explicit authority.

When stopped, preserve the current state, identify exact affected paths and evidence, state the GO/NO-GO, and request a recorded Founder decision.
