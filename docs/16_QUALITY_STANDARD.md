# Documentation Quality Standard

## Document Control

- **Document ID:** `docs/16_QUALITY_STANDARD.md` (provisional path identifier)
- **Status:** Draft
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On governance, metadata, lifecycle, validation, or quality-rule change
- **Lifecycle:** Draft
- **Source of Truth:** [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles), [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md), and recorded Founder approval
- **Dependencies:** [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles), [Repository Metadata Standard](REPOSITORY_METADATA.md), [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md)
- **Related Documents:** [Review Process](15_REVIEW_PROCESS.md), [Traceability Matrix](TRACEABILITY_MATRIX.md), and [Enterprise Quality Standard](../quality/QUALITY_STANDARD.md)
- **Traceability:** CP-001 through CP-010 and the controlled-document validation checklist
- **AI Compatibility:** AI-readable with gaps until Founder approval
- **Approval:** Pending Founder approval

## Purpose

Define documentation-specific conventions. Repository-wide gates remain governed by the [Enterprise Quality Standard](../quality/QUALITY_STANDARD.md).

## Core Principle Quality Gate

Every documentation review must verify the authoritative [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles).

| Rule ID | Required review result |
| --- | --- |
| CP-001 | No change bypasses Plugin First without an approved rule change. |
| CP-002 | No change bypasses Configuration First without an approved rule change. |
| CP-003 | Mobile First remains explicit and traceable. |
| CP-004 | Persian RTL remains explicit and traceable. |
| CP-005 | Inquiry First remains explicit and consistent with ADR 0001. |
| CP-006 | No Public Pricing remains explicit and consistent with ADR 0001. |
| CP-007 | No Custom Theme assumption or implementation is introduced. |
| CP-008 | No Gravity Forms assumption or implementation is introduced. |
| CP-009 | No LiteSpeed Cache assumption or implementation is introduced. |
| CP-010 | No AI Features are introduced in Phase 1. |

A document fails this gate when it contradicts a rule, omits an affected rule from traceability, or presents an excluded technology or feature as approved.

## Markdown Conventions

- Use CommonMark-compatible Markdown.
- Use one level-one title per document.
- Do not skip heading levels.
- Keep headings unique and descriptive.
- Use fenced code blocks with a language or text identifier when appropriate.
- Use tables only when they improve comparison or mapping.
- Keep checklist statements independently testable.

## Naming Conventions

- Preserve existing filenames and directories.
- Use the exact filename assigned by an approved task for new documents.
- Use uppercase snake case for governed top-level document filenames when specified by the existing pattern.
- Use stable ADR identifiers under `docs/adr/`.
- Do not reuse an identifier for a different document.
- Existing prefix collisions introduced by approved tasks must be recorded as technical debt rather than resolved through unauthorized renaming.

## Formatting Conventions

- Use ISO `YYYY-MM-DD` dates.
- Use the controlled lifecycle terms Draft, Review, Approved, Superseded, Deprecated, Archived, Historical, Blocked, and Cancelled.
- Use `TODO (Founder Decision Required)` only for founder decisions.
- Use a role-specific TODO when another assignment or input type is known.
- Distinguish current state, approved decisions, proposals, and future improvements.
- Do not leave ambiguous `TBD.` placeholders in documents normalized under this standard.

## Reference Conventions

- Prefer relative links for repository documents.
- Link to canonical sources rather than copying their content.
- Include descriptive link text.
- Avoid circular authority even when reciprocal navigation is useful.
- Verify local links during every review.
- Record external sources with enough context to revalidate them later.

## Content Quality Rules

- Do not invent business rules, product taxonomy, architecture, or technical decisions.
- Identify the source and status of every decision statement.
- Keep governing and supporting document roles separate.
- Remove duplicate concepts or replace them with canonical references.
- Resolve contradictory statements before approval.
- Keep open questions and Founder decisions in their controlled registers.

## AI Readability and Repository Intelligence

- Identify document authority, lifecycle, owner, reviewer, Approval Authority, dependencies, and approval state.
- Preserve CP rule IDs and ADR links in summaries and handoffs.
- Provide a role-appropriate reading path.
- Keep the knowledge graph and traceability matrix aligned with canonical sources.
- Treat missing, Draft, Open, Pending, and TODO content as unresolved.
- Separate repository AI collaboration from CP-010 No AI Features (Phase 1).
- Fail review when an AI needs historical chat context to locate authority or understand an unresolved dependency.

## Controlled Document Validation Checklist

| Validation | Pass condition | Fail condition |
| --- | --- | --- |
| Metadata | Canonical metadata fields required for the document class are present and internally consistent | Required metadata is absent, duplicated, or contradictory |
| Document ID | Stable or explicitly provisional identifier is unique and resolves to the document | Identifier is missing, reused, or conflicts with the indexed path |
| Version | Version is present and consistent with approval and lifecycle evidence | Version is absent or implies an unsupported approval or lineage |
| Status | Status uses the controlled lifecycle vocabulary | Unknown, ambiguous, or qualified status value is used |
| Owner | Accountable owner is explicit | Ownership is missing or assigned only to an AI or transient task |
| Authority | Authority class and approval boundary are explicit | Review, audit, supporting, or task content claims governing authority |
| Related Documents | Contextual relationships use resolving links and do not imply dependency | Relationships are missing, broken, or used as authority shortcuts |
| Traceability | Applicable rule IDs, decisions, sources, dependents, and evidence are linked | A material rule or decision has no origin or impact path |
| Dependencies | `Depends On` and `Required By` paths are discoverable and non-circular | Required dependency is missing, circular, or falsely approved |
| Lifecycle | Status, Lifecycle, transition evidence, and Approval agree | Illegal transition or status/approval conflict exists |
| Cross References | Local files and explicit anchors resolve | Any required local file or anchor is broken |
| Broken Links | Automated or reproducible local-link check reports zero failures | One or more required local links fail |
| Naming | Filename, title, and identifier follow the current approved convention or recorded exception | Unapproved rename, collision, or ambiguous identity exists |
| Navigation | Document is indexed, reachable, and appears in relevant reading paths | Document is orphaned, unindexed, or unreachable for its audience |
| Rule Inheritance | Applicable parent constraints are preserved or approved non-applicability is recorded | Child weakens, omits, or conflicts with an inherited rule |
| Consistency | Terminology, authority, decisions, metadata, and relationship types agree across references | Duplicate definitions or unresolved contradictions remain |

## Repository Validation Gate

A controlled document passes only when every applicable checklist row passes or an approved exception is linked. `Not applicable` requires rationale and review evidence. Review, audit, AI, or task output cannot approve its own exception.

Repository-wide validation additionally checks duplicate documents, duplicate authority, orphan documents, circular authority, circular dependencies, missing metadata, conflicting rules, broken navigation, and synchronization of the Documentation Index, Navigation Map, Reading Order, Knowledge Graph, and Traceability Matrix.

Git-governance changes additionally apply the repository, branch, tag, version, commit, baseline, and metadata checks in [Git Governance](GIT_GOVERNANCE.md#repository-validation-rules).

## Pass Criteria

A document passes when required metadata and sections are complete, terminology is controlled, references resolve, authority is unambiguous, placeholders are valid, and no blocking inconsistency remains.

## Fail Criteria

A document fails when it contains broken links, duplicate authority, unsupported decisions, ambiguous placeholders, invalid heading structure, conflicting terminology, or unresolved blocking findings.

## References

- [Enterprise Quality Standard](../quality/QUALITY_STANDARD.md)
- [Documentation Checklist](../quality/DOCUMENTATION_CHECKLIST.md)
- [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md)
- [Document Template](13_DOCUMENT_TEMPLATE.md)
- [AI Collaboration Standard](AI_COLLABORATION.md)
- [Repository Metadata Standard](REPOSITORY_METADATA.md)
- [Repository Traceability Matrix](TRACEABILITY_MATRIX.md)
- [Repository Reading Order](READING_ORDER.md)
- [Repository Knowledge Graph](KNOWLEDGE_GRAPH.md)
- [Git Governance](GIT_GOVERNANCE.md)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Review Process](15_REVIEW_PROCESS.md)
