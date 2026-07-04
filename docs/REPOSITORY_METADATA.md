# Repository Metadata Standard

## Document Control

- **Document ID:** `docs/REPOSITORY_METADATA.md` (provisional path identifier)
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
- **Source of Truth:** Approved governing documents identified by the [Documentation Index](08_DOCUMENTATION_INDEX.md); this document is a proposed standard pending Founder approval
- **Dependencies:** [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md), [Repository Standards](07_REPOSITORY_GUIDE.md)
- **Related Documents:** [AI Collaboration Standard](AI_COLLABORATION.md), [Traceability Matrix](TRACEABILITY_MATRIX.md), [Knowledge Graph](KNOWLEDGE_GRAPH.md), [Documentation Quality Standard](16_QUALITY_STANDARD.md), [Git Governance](GIT_GOVERNANCE.md), and [Repository Health](REPOSITORY_HEALTH.md)
- **Traceability:** [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles) and [Repository Traceability Matrix](TRACEABILITY_MATRIX.md)
- **AI Compatibility:** AI-ready after Founder approval
- **Approval:** Pending Founder approval

## Purpose

Define consistent metadata that lets humans and AI agents identify a document's authority, ownership, dependencies, lifecycle, and traceability without historical conversation context.

## Scope

Applies to new governed repository documents and to existing documents when their headers are otherwise missing or an authorized normalization task updates them.

Existing filenames remain unchanged. Until the Founder approves a numbering migration, the repository-relative path is the provisional document identifier.

## Required Metadata

| Field | Requirement |
| --- | --- |
| Document ID | Stable identifier; use repository-relative path provisionally when no approved ID exists. |
| Status | Draft, Review, Approved, Superseded, Deprecated, Archived, Historical, Blocked, or Cancelled. |
| Authority | Governing, Proposed Governing, Supporting, Evidence Record, or Template; authority is constrained by lifecycle and approval state. |
| Owner | Role accountable for accuracy and lifecycle. |
| Reviewer | Role responsible for current review evidence. |
| Approval Authority | Role authorized to approve the document. |
| Version | Document version under the approved versioning policy. |
| Last Updated | ISO `YYYY-MM-DD` date of the latest content change. |
| Last Review | ISO `YYYY-MM-DD` date of the latest completed review. |
| Review Cycle | Event-driven or periodic condition that triggers reassessment; unresolved cadence must be explicit. |
| Lifecycle | Must match Status and use the lifecycle values defined by the Document Lifecycle. |
| Source of Truth | Approved governing source or current-state evidence on which the document relies; must not imply self-approval. |
| Dependencies | Documents that must be understood or approved before this document can be applied. |
| Related Documents | Navigationally relevant documents that are not strict dependencies. |
| Traceability | Rule IDs, ADRs, requirements, dependent documents, and evidence links. |
| AI Compatibility | Whether an AI can safely interpret the document and under what conditions. |
| Approval | Approval reference or explicit pending state. |

## Authority Values

| Value | Meaning |
| --- | --- |
| Governing | Defines approved direction or constraints within its declared scope; requires Approved status and recorded approval. |
| Proposed Governing | Intended to become governing if approved; provides review context only while Draft or Review. |
| Supporting | Explains or operationalizes a governing document without overriding it. |
| Evidence Record | Preserves observations, validation evidence, decisions, audits, or outcomes without becoming governing authority. |
| Template | Defines reusable structure but is not project content. |

Authority and lifecycle are separate metadata dimensions but must remain consistent. A proposed document does not become Governing until it is Approved and its approval is recorded.

## Authority and Context Boundaries

- **Repository Authority** comes only from approved governing documents within their declared scope.
- **Decision Authority** may come from an explicitly accepted Founder decision or accepted ADR within its recorded decision scope; it does not approve surrounding Draft content or create broader repository authority.
- **Review Context** includes Draft or Review documents, review notes, and audit reports. It may support evaluation but does not govern the repository.
- **Task Context** defines the scope, permissions, and constraints of the current task. It does not promote a document or task output to repository authority.
- **Audit and task outputs** are evidence or proposals unless an authorized approval process incorporates them into a governing document.
- **Conversation outputs** are non-authoritative context until the relevant decision is recorded and approved in the repository.

Producing, reviewing, referencing, or using a document does not by itself grant governing authority.

## Dependency Rules

- Dependencies are directional.
- A dependent document must not override its dependency.
- Missing or unapproved dependencies must be visible before a document is applied.
- Circular navigation is permitted; circular authority is not.
- Dependency changes require traceability review.

## Relationship Metadata Model

The canonical relationship vocabulary is defined in the [Repository Knowledge Graph](KNOWLEDGE_GRAPH.md#relationship-types). Controlled documents express it through metadata and explicit relationship statements:

| Relationship | Metadata expression | Required reciprocal or evidence |
| --- | --- | --- |
| Depends On | `Dependencies` | Authority source or prerequisite exists and is linked |
| Required By | Traceability or dependent-document list | Reciprocal `Depends On` is discoverable |
| Extends | Relationship statement plus `Dependencies` | Parent remains authoritative within scope |
| References | `Related Documents` or inline link | No authority transfer is implied |
| Replaces | Relationship statement and approval evidence | Replaced document identifies the replacement |
| Supersedes | Relationship statement, lifecycle update, and approval evidence | Superseded record identifies the successor |
| Related Documents | `Related Documents` | Navigational relationship only |
| Parent | `Source of Truth` or explicit parent statement | Child identifies inherited rules |
| Child | Traceability or dependent-document list | Parent can discover affected child |
| Authority Source | `Source of Truth` and `Traceability` | Source is approved or its accepted decision scope is explicit |

`Dependencies`, `Related Documents`, and `Source of Truth` are not interchangeable. A reciprocal navigation link does not create circular authority.

## Related Document Rules

- Use relative Markdown links.
- Describe the relationship when it is not obvious.
- Link to canonical sources instead of restating their decisions.
- Keep historical records separate from active governing paths.

## Approval Metadata

- `Pending Founder approval` means the document remains non-authoritative. An individually accepted decision recorded inside it retains only its explicit decision authority and does not approve the surrounding document.
- Approved metadata must identify the approver and approval reference when available.
- Review completion does not equal approval.
- A superseded approval must point to the replacement or superseding decision.

## AI Compatibility Values

| Value | Meaning |
| --- | --- |
| AI-ready | Authority, dependencies, terms, traceability, and unresolved items are explicit. |
| AI-readable with gaps | The document can provide context but requires human clarification before action. |
| Human review required | Ambiguity, sensitivity, missing authority, or unresolved conflict prevents safe autonomous interpretation. |

AI compatibility does not authorize an AI feature, autonomous mutation, or implementation.

## Traceability Requirements

- Cite applicable CP rule IDs.
- Link accepted ADRs for significant decisions.
- Identify governing, referenced, and dependent documents.
- Link review evidence and audit records when relevant.
- Register unresolved authority or content gaps in the Founder Decision Log or Open Questions.

## Transitional Rule for Existing Documents

- Do not rename existing files to satisfy metadata.
- Do not overwrite approved content.
- Add missing metadata only through an authorized task.
- Use the Documentation Index as the current authority map.
- Record identifier migration as a Founder decision before changing IDs.

## Standard Header Example

```markdown
## Document Control

- **Document ID:** `repository/relative/path.md`
- **Status:** Draft
- **Authority:** Supporting
- **Owner:** TODO (Owner Assignment Required)
- **Reviewer:** TODO (Reviewer Assignment Required)
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** YYYY-MM-DD
- **Last Review:** YYYY-MM-DD
- **Review Cycle:** TODO (Review Cycle Required)
- **Lifecycle:** Draft
- **Source of Truth:** TODO (Approved Source Required)
- **Dependencies:** TODO (Required Input)
- **Related Documents:** TODO (Related Documents Required)
- **Traceability:** TODO (Traceability Required)
- **AI Compatibility:** AI-readable with gaps
- **Approval:** Pending Founder approval
```

## References

- [Document Template](13_DOCUMENT_TEMPLATE.md)
- [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md)
- [Documentation Quality Standard](16_QUALITY_STANDARD.md)
- [Knowledge Graph](KNOWLEDGE_GRAPH.md)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [AI Collaboration Standard](AI_COLLABORATION.md)
