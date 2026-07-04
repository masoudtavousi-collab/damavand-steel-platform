# AI Collaboration Standard

## Document Control

- **Document ID:** `docs/AI_COLLABORATION.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On material change; periodic cadence pending Founder approval
- **Lifecycle:** Review
- **Source of Truth:** [Project Bible](00_PROJECT_BIBLE.md), [Project Constitution](01_PROJECT_CONSTITUTION.md), and [Repository Standards](07_REPOSITORY_GUIDE.md)
- **Dependencies:** [Project Bible](00_PROJECT_BIBLE.md), [Project Constitution](01_PROJECT_CONSTITUTION.md), [Repository Standards](07_REPOSITORY_GUIDE.md)
- **Related Documents:** [Repository Metadata Standard](REPOSITORY_METADATA.md), [Traceability Matrix](TRACEABILITY_MATRIX.md), [Reading Order](READING_ORDER.md), and [Knowledge Graph](KNOWLEDGE_GRAPH.md)
- **Traceability:** [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles) and [Repository Traceability Matrix](TRACEABILITY_MATRIX.md)
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

## Authority Context Model

- **Repository Authority** is established only by approved governing documents within their declared scope.
- **Decision Authority** is limited to explicitly accepted Founder decisions and accepted ADRs within their recorded scope; it does not approve surrounding Draft content or establish broader repository authority.
- **Review Context** supports evaluation of a proposal. Review-state documents and audit reports do not become governing because they are reviewed or referenced.
- **Task Context** establishes what may be done during a specific task. It does not promote task instructions, task outputs, or referenced Review documents into governing authority.
- **Conversation Context** may explain intent but remains non-authoritative until the relevant decision is recorded and approved in the repository.

No AI role may infer approval or authority from file existence, document production, task inclusion, review completion, or conversation history.

## AI Roles

### Founder

- Defines and approves project principles, business decisions, architecture authority, governance, and implementation authorization.
- Resolves Founder decisions and conflicts that exceed delegated authority.
- Approves baselines, releases, renames, and lifecycle transitions when required.

### Architect

- Evaluates architecture only within an explicitly authorized architecture task.
- Traces recommendations to approved requirements and decisions.
- Records significant decisions through the approved ADR process.
- Does not implement or redesign unless separately authorized.

### Builder

- Implements only the requested, approved scope.
- Preserves existing architecture and Core Project Principles.
- Prefers configuration and approved plugins according to CP-001 and CP-002.
- Does not infer business rules, product taxonomy, technology selection, or feature scope.

### Reviewer

- Checks the proposed change against source documents, rule traceability, quality gates, and task scope.
- Distinguishes evidence from assumptions.
- Reports blocking and non-blocking findings without silently correcting out-of-scope issues.

### Auditor

- Performs evidence-based, read-only assessment unless changes are explicitly authorized.
- Verifies links, metadata, authority, traceability, consistency, and recorded decisions.
- Does not convert an audit recommendation into an approved requirement.

### Documentation Writer

- Structures approved information for clarity, navigation, and long-term maintenance.
- Uses the metadata and lifecycle standards.
- Does not manufacture missing content to make a document appear complete.

### Knowledge Curator

- Maintains indexes, reading order, relationships, glossary entries, and knowledge-graph integrity.
- Links to canonical content instead of duplicating it.
- Registers unresolved conflicts and stale relationships for review.

### Prompt Writer

- Creates repository collaboration prompts that preserve source-of-truth order and approval boundaries.
- Separates instructions, context, constraints, expected evidence, and output format.
- Does not use prompts to bypass governance or introduce a Phase 1 AI product feature.

## Responsibilities

Every collaborator must:

- Read the applicable [Reading Order](READING_ORDER.md) before acting.
- Identify role, task scope, allowed mutations, forbidden actions, and approval boundary.
- Cite the governing document or rule ID for material decisions.
- Preserve unresolved TODOs instead of guessing.
- Record new Founder decisions and open questions in their controlled registers.
- Update navigation and traceability when an authorized change affects relationships.
- Validate output using the applicable quality checklists.

## Handoff Rules

Every handoff must include:

- Task objective and current status.
- Files reviewed, created, and modified.
- Governing rules and decision sources.
- Evidence produced and validation performed.
- Remaining risks, TODOs, and open questions.
- Decisions requiring Founder approval.
- Explicit statement of what was not authorized or not completed.
- Recommended next action without automatically starting it.

A receiving collaborator must verify the repository state rather than trusting the handoff summary alone.

## Approval Rules

- AI output is a proposal until the authorized Approval Authority approves it.
- No AI role may self-approve a Founder decision.
- Review success does not authorize implementation, Git operations, release, migration, or deployment.
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
