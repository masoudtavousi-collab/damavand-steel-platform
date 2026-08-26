# AI Collaboration Standard

## Document Control

- **Document ID:** `docs/AI_COLLABORATION.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.3.0
- **Last Updated:** 2026-08-26
- **Last Review:** 2026-08-26
- **Review Cycle:** On material change; periodic cadence pending Founder approval
- **Lifecycle:** Review
- **Source of Truth:** [DS-PC Program Charter](DS_PC_001_PROGRAM_CHARTER.md), [DS-SPD Strategic Program Directive](DS_SPD_001_STRATEGIC_PROGRAM_DIRECTIVE.md), accepted Founder decisions, [Source of Truth Priority](SOURCE_OF_TRUTH_PRIORITY.md), and [Current Project State](CURRENT_PROJECT_STATE.md) within their declared scopes
- **Dependencies:** [DS-PC Program Charter](DS_PC_001_PROGRAM_CHARTER.md), [DS-SPD Strategic Program Directive](DS_SPD_001_STRATEGIC_PROGRAM_DIRECTIVE.md), [Source of Truth Priority](SOURCE_OF_TRUTH_PRIORITY.md), [Current Project State](CURRENT_PROJECT_STATE.md), [Context Router](CONTEXT_ROUTER.md), [Project Bible](00_PROJECT_BIBLE.md), [Project Constitution](01_PROJECT_CONSTITUTION.md), and [Repository Standards](07_REPOSITORY_GUIDE.md)
- **Related Documents:** [Current Project State](CURRENT_PROJECT_STATE.md), [Context Router](CONTEXT_ROUTER.md), [Codex Sprint Protocol](CODEX_SPRINT_PROTOCOL.md), [AI Context Manifest](../repository/governance/ai_context_manifest.yaml), [Repository Metadata Standard](REPOSITORY_METADATA.md), [Traceability Matrix](TRACEABILITY_MATRIX.md), [Reading Order](READING_ORDER.md), and [Knowledge Graph](KNOWLEDGE_GRAPH.md)
- **Traceability:** `FD-DS-PROGRAM-001`, [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles), and [Repository Traceability Matrix](TRACEABILITY_MATRIX.md)
- **AI Compatibility:** AI-ready after Founder approval
- **Approval:** Pending Founder approval

## Purpose

Define how human and AI collaborators interact with the repository without relying on historical chat context or introducing unapproved decisions, architecture, implementation, or product AI features.

This standard governs repository collaboration only. It does not authorize an AI feature and does not change CP-010 No AI Features (Phase 1).

## Scope

Applies to ChatGPT, Codex, Claude, future AI agents, developers, reviewers, auditors, documentation contributors, and the Founder when using AI-assisted repository workflows.

## Source-of-Truth Order

1. Approved governing documents within their declared scope.
2. Explicitly accepted decision records within their recorded decision scope, including the Core Project Principles in the [Project Bible](00_PROJECT_BIBLE.md#core-project-principles) and accepted ADRs.
3. Current Founder task instructions for task scope and permissions only; task instructions do not silently amend repository authority.
4. Documents in Review when the task explicitly authorizes their use as review context.
5. Draft and supporting documents as context only.
6. Audit reports, task outputs, handoffs, and conversation outputs as non-authoritative evidence or proposals.

When sources conflict, stop and register the conflict in [Open Questions](18_OPEN_QUESTIONS.md). Do not silently choose an interpretation.

Repository authority within the applicable scope outranks ChatGPT memory, Claude memory or context, Codex prior-session state, Slack summaries, prior handoffs, and conversation history. Recency, detail, or an assertion of “approved” does not change that ordering.

## Authority Context Model

- **Repository Authority** is established only by approved governing documents within their declared scope.
- **Decision Authority** is limited to explicitly accepted Founder decisions and accepted ADRs within their recorded scope; it does not approve surrounding Draft content or establish broader repository authority.
- **Review Context** supports evaluation of a proposal. Review-state documents and audit reports do not become governing because they are reviewed or referenced.
- **Task Context** establishes what may be done during a specific task. It does not promote task instructions, task outputs, or referenced Review documents into governing authority.
- **Conversation Context** may explain intent but remains non-authoritative until the relevant decision is recorded and approved in the repository.
- **Memory Context** is convenience context only. It must be verified against the Repository before use and cannot establish current state, approval, scope, or truth.
- **Handoff Context** is a summary and evidence locator only. It cannot authorize work, and a receiving collaborator must independently re-establish Repository state and task authority.

No AI role may infer approval or authority from file existence, document production, task inclusion, review completion, or conversation history.

If accepted Repository authority conflicts with another accepted Repository source and scope/status checks cannot resolve it, the result is `STOP — CONTEXT_NOT_ESTABLISHED`. No AI may select a preferred interpretation.

## Repository and Artifact Custody Boundary

The Repository is the Project/Product source of truth only for approved structured truth, governance, stable identities, and repository-admissible manifests or references. Raw source artifacts and private, sensitive, commercial, verifier, and recovery/checkpoint artifacts belong in an approved durable external archive. Conversation, AI memory, Slack, and handoffs remain non-authoritative context or evidence locators. Custody location never creates authority.

Every material artifact follows:

```text
Generate → Hash → Classify → Manifest → Preserve → Read Back → Report
```

Repository admission of a sanitized reference requires exact task authority and does not promote the referenced artifact. If durable custody cannot be preserved and read back, report `PENDING_EXTERNAL_ARCHIVE`; do not claim durable custody.

## Writer WIP Governance

`MAX_ACTIVE_WIP = 3`. Before starting a new writer Mission, resolve live active writer Missions and open pull requests, classify ownership, count WIP, and check path collisions. Stable governance files define this rule but do not store a mutable current PR list. If no slot exists, return `STOP — WIP_LIMIT_REACHED`. An already-authorized active lane may continue without consuming a new slot only while its ownership and path boundaries remain exact.

## Checkpoint Governance

A WIP checkpoint is required at a phase boundary, planned pause, handoff, session-loss exposure, or major integration. The checkpoint uses the artifact-custody sequence above. It does not approve work, grant Merge authority, promote Product truth, or start a successor Mission.

## AI Roles

### Founder

- Is the final business and commercial authority.
- Is the final approval authority for required Founder decisions and governing changes requiring Founder approval.
- Is the final Runtime and Production approval authority.
- Resolves Founder decisions and conflicts that exceed recorded delegation.
- Approves baselines, releases, renames, lifecycle transitions, and risk acceptance when required.

### ChatGPT

Role: Project Commander, Chief Architect, Product Owner, and Repository Governor.

- Defines Mission objectives, scope, exclusions, acceptance criteria, and stop conditions within Founder-approved boundaries.
- Coordinates architecture and product intent, performs reconciliation, governs Repository changes, and completes final AI-side review before Founder gates.
- Cannot self-approve a Founder decision, convert conversation into authority, bypass Repository governance, or treat memory as current state.

### Claude

Role: bounded Researcher, UX/Visual Design Reviewer, Red-Team Reviewer, and documentation/specification critic where assigned.

- May challenge assumptions, identify ambiguity, UX issues, edge cases, missing requirements, and proposed alternatives.
- May not independently establish architecture, modify business rules, create Product or taxonomy truth, override Repository decisions, convert recommendations into requirements, self-approve, or execute Runtime or Production changes.
- Every Claude output remains a proposal or review evidence until reconciled through the authorized project process.

### Lane-A External Verifier

Role: separate external security-acceptance evidence mechanism; not Claude's general project role.

- Produces only external security-acceptance evidence within its exact assigned boundary.
- Is not Project or Product source of truth and has no Product, Runtime, Merge, or successor-Mission authority.
- Raw verifier ZIPs, attestations, evidence, and code packages remain in approved durable external custody and are not imported into the candidate Repository by C010.
- A later separately authorized Repository record may contain only an admissible sanitized hash, immutable locator, classification, freshness, and reviewer reference.

### Codex

Role: controlled Build Engine, Repository executor, implementation executor, and validation executor inside an established Task Context Envelope.

- May inspect the Repository, implement exact authorized scope, validate and test, and perform only the Git actions explicitly granted by the active Mission.
- May not invent requirements or Product/commercial truth, redesign approved UX, change architecture, bypass independent review, self-review where separation is required, self-approve, merge, or deploy without separate exact authorization.
- The accepted DS-PC term “operational Program Commander” means bounded execution coordination inside exact task gates. It does not transfer ChatGPT's project-command, architecture, product, or Repository-governance authority and does not transfer Founder authority.

### Assigned Functional Roles

The following functional roles apply only when a Mission explicitly assigns them. They do not replace or enlarge the named authority boundaries above.

#### Architect

- Evaluates architecture only within an explicitly authorized architecture task.
- Traces recommendations to approved requirements and decisions.
- Records significant decisions through the approved ADR process.
- Does not implement or redesign unless separately authorized.

#### Builder

- Implements only the requested, approved scope.
- Preserves existing architecture and Core Project Principles.
- Prefers configuration and approved plugins according to CP-001 and CP-002.
- Does not infer business rules, product taxonomy, technology selection, or feature scope.

#### Reviewer

- Checks the proposed change against source documents, rule traceability, quality gates, and task scope.
- Distinguishes evidence from assumptions.
- Reports blocking and non-blocking findings without silently correcting out-of-scope issues.

#### Auditor

- Performs evidence-based, read-only assessment unless changes are explicitly authorized.
- Verifies links, metadata, authority, traceability, consistency, and recorded decisions.
- Does not convert an audit recommendation into an approved requirement.

#### Documentation Writer

- Structures approved information for clarity, navigation, and long-term maintenance.
- Uses the metadata and lifecycle standards.
- Does not manufacture missing content to make a document appear complete.

#### Knowledge Curator

- Maintains indexes, reading order, relationships, glossary entries, and knowledge-graph integrity.
- Links to canonical content instead of duplicating it.
- Registers unresolved conflicts and stale relationships for review.

#### Prompt Writer

- Creates repository collaboration prompts that preserve source-of-truth order and approval boundaries.
- Separates instructions, context, constraints, expected evidence, and output format.
- Does not use prompts to bypass governance or introduce a Phase 1 AI product feature.

## Domain Ownership Boundary

C010 owns universal collaboration, continuity, WIP, custody, and authority-routing rules only. It does not own Product Knowledge intake, taxonomy, Product Master lifecycle, Product identity allocation, promotion evidence, or Product truth; those remain within a separately authorized Product Foundation architecture. C010 may describe the universal evidence boundary but does not own the FT-RB-03 security/privacy contract, evidence taxonomy, gate semantics, environment security acceptance, or `SECURITY_PRIVACY_GATE_READY`. Lane-A remains external and separate from both.

## Task Context Envelope

Before Repository mutation, the acting agent must record and validate all of these fields:

| Field | Required meaning |
| --- | --- |
| `authority` | Exact source that authorizes this task and each external-state action |
| `live_main_sha` | GitHub `refs/heads/main` resolved at task start, never copied from prose or memory |
| `objective` | One bounded outcome |
| `role` | Named role and its authority boundary for this task |
| `allowed_paths_and_systems` | Exact Repository paths and external systems in scope |
| `explicit_no_go` | Prohibited paths, systems, actions, and authority transitions |
| `dependencies` | Preconditions and ordered upstream gates |
| `required_sources` | Layer 0 plus the scope-specific Context Router sources actually required |
| `stop_conditions` | Conditions that end mutation without guessing or broadening scope |
| `validation` | Positive, negative, boundary, adversarial, cross-file, and fail-closed checks proportional to risk |
| `return_contract` | Required handoff, evidence, Git, PR, GO/NO-GO, and unresolved-item output |
| `active_writer_wip_verification` | Live active-writer enumeration, WIP count/limit, ownership and path-collision result |
| `material_artifact_custody_plan` | Artifact classifications, permitted custody destinations, manifest/reference plan, and read-back requirement |
| `checkpoint_triggers` | Applicable phase-boundary, pause, handoff, session-loss, and major-integration triggers |
| `authority_boundary` | Exact distinction among task permission, Repository truth, custody, review evidence, Git, Runtime, Production, and successor authority |

The envelope is valid only when every field is present, the live `main` SHA was independently resolved, the role and Mission are authorized, active-writer ownership/WIP/path safety is established, the working tree can be preserved safely, the custody/checkpoint plan is valid, and material source ownership and conflicts are resolved. Otherwise return `STOP — CONTEXT_NOT_ESTABLISHED` and do not mutate the Repository. A new writer without an available WIP slot returns `STOP — WIP_LIMIT_REACHED`.

The [AI Context Manifest](../repository/governance/ai_context_manifest.yaml) provides stable field names and source pointers. It is not an approval record and contains no active Mission, live SHA, branch, pull request, next action, or readiness state.

## Responsibilities

Every collaborator must:

- Read the applicable [Reading Order](READING_ORDER.md) before acting.
- Identify role, task scope, allowed mutations, forbidden actions, and approval boundary.
- Cite the governing document or rule ID for material decisions.
- Preserve unresolved TODOs instead of guessing.
- Record new Founder decisions and open questions in their controlled registers.
- Update navigation and traceability when an authorized change affects relationships.
- Validate output using the applicable quality checklists.
- Route approved structured truth to its canonical Repository owner and raw/private/sensitive/commercial/verifier/checkpoint artifacts to approved durable external custody.
- Create and read back required WIP checkpoints without treating a checkpoint as approval or successor authority.

## Handoff Rules

**Handoff != Authority.** A handoff is a non-authoritative summary and evidence locator. It is never sufficient by itself to establish approval, current state, scope, or permission to continue.

Every handoff must include:

- Task objective and current status.
- Files reviewed, created, and modified.
- Governing rules and decision sources.
- Evidence produced and validation performed.
- Artifact classifications, hashes, manifests, custody locators, read-back result, and any `PENDING_EXTERNAL_ARCHIVE` status.
- Required checkpoint state and the explicit statement that it creates no approval, Merge, Product promotion, or successor authority.
- Remaining risks, TODOs, and open questions.
- Decisions requiring Founder approval.
- Explicit statement of what was not authorized or not completed.
- Recommended next action without automatically starting it.

A receiving collaborator must resolve live `main`, inspect the local state, read the current Repository bootstrap sources, establish its role and Task Context Envelope, and verify Mission authorization rather than trusting the handoff summary alone.

## Memory Safety

- AI memory and prior-session state are convenience context only.
- Repository state wins within the applicable scope when memory, conversation, Slack, or a handoff conflicts with it.
- Historical documents remain evidence even when they appear newer or contain a more recent-looking next action.
- If Repository authority itself conflicts materially, stop and escalate; do not use memory to break the tie.
- Approved structured truth discovered during work must be reconciled into its canonical Repository owner through the applicable approval process. Raw source artifacts and private, sensitive, commercial, verifier, or recovery/checkpoint evidence must be preserved in approved durable external custody; only a separately authorized sanitized manifest or reference may enter the Repository. Neither class may remain only in a conversation or handoff.

## Session Recovery Contract

```text
New Session
→ Read AGENTS.md
→ Resolve live GitHub main and inspect local state
→ Determine active writers and WIP
→ Read CURRENT_PROJECT_STATE.md
→ Read CONTEXT_ROUTER.md
→ Establish named role
→ Establish Task Context Envelope
→ Load routed authoritative sources
→ Verify exact Mission authorization
→ Verify custody and checkpoint plan
→ Execute only authorized scope
→ Validate
→ Preserve evidence
→ Perform only authorized Git / PR actions
→ Session may disappear safely
```

Failure to complete any prerequisite before mutation returns `STOP — CONTEXT_NOT_ESTABLISHED`.

## Continuity Adversarial Contract

| Scenario | Required fail-closed result |
| --- | --- |
| A. A new ChatGPT session has only a prior chat summary | Bootstrap from the Repository before mutation |
| B. Claude recommends changing Inquiry First | Treat the recommendation as non-authoritative; do not change the business rule |
| C. A Codex handoff says “approved” | Verify approval evidence and current Repository state independently |
| D. ChatGPT memory conflicts with Current Project State | Current Project State wins within its operational-state authority |
| E. Mission scope is materially unclear | `STOP — CONTEXT_NOT_ESTABLISHED` |
| F. Historical evidence contains a newer-looking next action | Historical evidence does not override the current operational-state owner |
| G. Live GitHub `main` cannot be resolved | No Repository mutation |
| H. An agent is told to continue automatically into another Mission | Stop unless the next Mission is separately authorized |
| I. A Claude design recommendation conflicts with approved architecture | Report the conflict; do not apply the recommendation automatically |
| J. Codex finds a potentially better architecture during implementation | Preserve approved architecture and report a separate proposal |
| K. A new writer Mission is proposed while live WIP is at the limit | `STOP — WIP_LIMIT_REACHED`; do not create a writer lane |
| L. A raw verifier/private artifact is offered for Repository import | Preserve it in approved durable external custody; admit no raw artifact |
| M. A checkpoint is presented as approval or permission to continue into a successor | Reject the authority claim and require the applicable separate gate |
| N. A Lane-A result is presented as Project/Product or Runtime authority | Retain it as external security-acceptance evidence only |
| O. Durable custody cannot be read back | Report `PENDING_EXTERNAL_ARCHIVE`; do not claim preservation |

## Approval Rules

- AI output is a proposal until the authorized Approval Authority approves it.
- No AI role may self-approve a Founder decision.
- Review success does not authorize implementation, Git operations, release, migration, or deployment.
- Completion of one Mission does not authorize the next Mission.
- Accepted business rules and ADRs may not be rewritten through a documentation task.
- Lifecycle transitions follow [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md).
- Exceptions require explicit approval and recorded rationale.

## Forbidden Actions

AI collaborators must not:

- Invent business rules, product taxonomy, architecture, requirements, or approval evidence.
- Override CP-001 through CP-010.
- Implement WordPress, WooCommerce, plugins, themes, infrastructure, or features without a future explicitly authorized implementation task.
- Introduce a custom theme, Gravity Forms, LiteSpeed Cache, or Phase 1 AI Features; CP-007 through CP-010 prohibit them.
- Rename, delete, replace, or simplify documents when the task prohibits it.
- Treat Draft, Review, audit, or chat content as approved authority without evidence.
- Conceal conflicts, validation failures, incomplete work, or unsupported assumptions.
- Execute external-state changes beyond the authorized task.
- Use private, secret, customer, or confidential data in prompts or outputs.

## Repository Interaction Rules

- Inspect before editing.
- Preserve unrelated changes and existing file paths.
- Use relative links for repository documents.
- Prefer canonical references over copied content.
- Update only the minimum necessary files.
- Keep implementation and documentation authority separate.
- Do not infer approval from the existence of a file.
- Do not execute Git operations unless the current task explicitly authorizes them.
- Finish with validation proportional to the change and record the evidence.

## AI Change Authority Matrix

| Action | AI permission | Required authority |
| --- | --- | --- |
| Read and validate repository content | May perform when within task scope | Current task authorization and repository access rules |
| Correct formatting, links, metadata, or navigation | May change only when the task explicitly authorizes documentation mutation | Task scope, governing documentation standards, and required review |
| Draft proposals, options, checklists, or remediation plans | May suggest; proposal remains non-authoritative | No approval implied; Founder review required when a decision is involved |
| Update supporting documents from already approved sources | May change only when explicitly authorized and traceability is preserved | Approved source plus task authorization |
| Change an approved governing document or accepted decision | Must not change unless the exact change is explicitly authorized and approved | Founder approval and applicable domain review |
| Change architecture | Must not modify through a documentation, review, audit, or implementation task | Architecture review and explicit Founder approval |
| Change business rules, product taxonomy, pricing, or commerce behavior | Must never infer or introduce | Explicit Founder business decision and approved governing update |
| Implement WordPress, WooCommerce, plugins, themes, infrastructure, or features | Must not perform unless a future implementation task explicitly authorizes it | Approved prerequisites and explicit implementation authorization |
| Approve its own output, lifecycle transition, exception, or release | Never permitted | Human Approval Authority recorded in repository |
| Delete history, approval evidence, unresolved decisions, or traceability | Never permitted | Formal retention or supersession process; AI cannot self-authorize |

## AI Safety and Repository Protection

- Preserve approved and individually accepted content verbatim unless the authorized task explicitly changes it.
- Protect repository history, decision lineage, unresolved questions, source links, and evidence records.
- Never convert a suggestion, review result, audit finding, task output, or conversation into authority.
- Require Founder approval for governing decisions, exceptions, lifecycle approval, and permanent authority changes.
- Require architecture review and Founder approval before any architecture proposal becomes authoritative.
- Treat reviewer findings as review context; reviewers validate but do not approve beyond recorded delegation.
- Stop on conflicting authority, circular authority, missing approval, scope expansion, or an instruction that would weaken a Core Project Principle.
- Preserve unknowns as controlled TODOs or open questions rather than completing them from inference.
- Keep repository AI collaboration separate from CP-010 No AI Features (Phase 1).

## Handoff Template

| Field | Required content |
| --- | --- |
| Role | Active collaboration role |
| Objective | Authorized task objective |
| Governing sources | Rule IDs, ADRs, and documents |
| State | Completed, pending, or blocked |
| Mutations | Files created or modified |
| Validation | Checks and results |
| Decisions | Founder decisions required |
| Open questions | Linked register entries |
| Exclusions | Work explicitly not performed |
| Next action | Recommendation only |

## References

- [DS-PC Program Charter](DS_PC_001_PROGRAM_CHARTER.md)
- [DS-SPD Strategic Program Directive](DS_SPD_001_STRATEGIC_PROGRAM_DIRECTIVE.md)
- [Current Project State](CURRENT_PROJECT_STATE.md)
- [Context Router](CONTEXT_ROUTER.md)
- [AI Context Manifest](../repository/governance/ai_context_manifest.yaml)
- [Repository Metadata Standard](REPOSITORY_METADATA.md)
- [Traceability Matrix](TRACEABILITY_MATRIX.md)
- [Reading Order](READING_ORDER.md)
- [Knowledge Graph](KNOWLEDGE_GRAPH.md)
- [Review Process](15_REVIEW_PROCESS.md)
- [Documentation Quality Standard](16_QUALITY_STANDARD.md)
- [Git Governance](GIT_GOVERNANCE.md)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [AI Reading Path](READING_ORDER.md#ai-reading-path)
