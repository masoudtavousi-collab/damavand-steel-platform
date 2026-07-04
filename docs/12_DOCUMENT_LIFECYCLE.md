# Document Lifecycle

## Document Control

- **Document ID:** `docs/12_DOCUMENT_LIFECYCLE.md` (provisional path identifier)
- **Status:** Draft
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On lifecycle, transition, approval, or version-policy change
- **Lifecycle:** Draft
- **Source of Truth:** [Project Constitution](01_PROJECT_CONSTITUTION.md) and recorded Founder approval; this lifecycle model remains Draft
- **Dependencies:** [Project Constitution](01_PROJECT_CONSTITUTION.md)
- **Related Documents:** [Repository Metadata Standard](REPOSITORY_METADATA.md), [Document Template](13_DOCUMENT_TEMPLATE.md), and [Review Process](15_REVIEW_PROCESS.md)
- **Traceability:** Lifecycle states, transition evidence, ownership, approval, and version implications defined in this document
- **AI Compatibility:** AI-readable with gaps until Founder approval
- **Approval:** Pending Founder approval

## Purpose

Define the requested lifecycle states and transition controls for repository documentation.

## Lifecycle States

### Draft

The document is under preparation, may contain controlled placeholders, and is not an approved source for new decisions.

### Review

The document is complete enough for the applicable architecture, business, technical, and quality reviews. Review findings remain visible until resolved.

### Approved

The document has passed required reviews and received approval from the authorized approver. The approver role remains subject to Founder confirmation.

### Superseded

The document has been replaced by an approved successor. It is not current authority and must identify the replacing document.

### Deprecated

The document remains available for transition or historical context but is no longer the preferred authority. It must link to its replacement when one exists.

### Archived

The document is retained as a historical record and removed from active reading paths. Archived documents must not be treated as current requirements.

### Historical

The document is retained as evidence of a past state or outcome and has no current governing authority. Its original context and terminal relationship must remain visible.

### Blocked

The document cannot progress because a named unresolved dependency, conflict, or approval is preventing review or transition. The blocker, owner, and exit condition are required.

### Cancelled

Work on the document ended before approval. It remains non-authoritative and records the cancellation authority, reason, and any successor.

## Status Vocabulary

- Document lifecycle uses only Draft, Review, Approved, Superseded, Deprecated, Archived, Historical, Blocked, and Cancelled.
- ADR decision status is separate and may use Proposed, Accepted, Rejected, Superseded, or Deprecated.
- An Accepted ADR must identify its document lifecycle independently.
- Qualifying text belongs in notes, not inside the controlled lifecycle value.

## Transition Model

```text
Draft <-> Review -> Approved -> Deprecated -> Archived
  |        |           |  \-> Superseded -> Historical
  |        |           \----> Historical
  |        \-> Blocked -> Draft or Review
  \-> Blocked -> Draft or Cancelled

Draft or Review -> Cancelled
Deprecated -> Superseded or Archived
Archived -> Historical
```

No lifecycle transition silently changes an underlying decision. Re-entering active work from an inactive terminal state requires a new document version or successor rather than rewriting the retained record.

## Metadata Source

The single canonical metadata model is defined by the [Repository Metadata Standard](REPOSITORY_METADATA.md) and represented by the [Document Template](13_DOCUMENT_TEMPLATE.md). This lifecycle document does not define a second field list.

For lifecycle control, `Status` and `Lifecycle` must use the same value and must be supported by the transition evidence defined below. Legacy-header normalization requires a separately authorized task.

## Allowed Transitions and Requirements

| Transition | Required evidence |
| --- | --- |
| Draft to Review | Complete required sections, resolved broken links, identified open questions, and named reviewers |
| Draft or Review to Blocked | Named blocker, owner, impact, and exit condition |
| Blocked to Draft or Review | Evidence that the blocker is resolved and the owner has accepted re-entry |
| Review to Approved | Completed review record, resolved blocking findings, and authorized approval |
| Approved to Draft or Review | Documented reason and impact assessment |
| Approved to Superseded | Approved successor, explicit supersession link, and dependent-reference review |
| Approved to Deprecated | Replacement or deprecation rationale and affected-reference review |
| Approved to Historical | Recorded end of governing effect and evidence-retention rationale |
| Deprecated to Superseded | Approved successor and completed transition record |
| Deprecated to Archived | Retention confirmation and removal from active reading paths |
| Superseded to Historical | Successor confirmed current and historical context preserved |
| Archived to Historical | Historical classification and retention context recorded |
| Draft or Review to Cancelled | Authorized cancellation, reason, owner, and successor when applicable |

## Illegal Transitions

- Draft directly to Approved without Review and approval evidence.
- Review directly to Superseded, Deprecated, Archived, or Historical without first becoming Approved.
- Blocked directly to Approved.
- Cancelled, Superseded, Archived, or Historical directly to an active state.
- Any transition that removes the prior state, approval evidence, replacement link, blocker, or cancellation reason.
- Any transition performed solely by a reviewer, auditor, AI agent, or task output without the recorded Approval Authority.

An illegal transition fails validation and must be reverted to the last evidence-supported state.

## Version Implications

| Transition type | Version implication |
| --- | --- |
| Draft or Review iteration | Update the working version according to the pending approved versioning policy; do not imply approval |
| Review to Approved | Record the approved version and approval reference |
| Approved content change | Create a new version and return it to Review; retain the approved predecessor |
| Approved to Superseded or Deprecated | Record terminal status and successor or rationale without rewriting approved content |
| Any state to Historical or Archived | Preserve the terminal version; metadata-only corrections must be identified as corrections |
| Blocked or Cancelled | Preserve the current version and record blocker or cancellation evidence |

## Ownership and Approval

- Document owners maintain accuracy and initiate reviews.
- Reviewers validate their assigned domain only.
- Approval authority is recorded explicitly in each document.
- The current Approval Authority is Founder.
- Future delegation requires a Founder decision and metadata update.
- Document owners may propose transitions but may not self-approve them unless an approved delegation explicitly permits it.
- Reviewers validate evidence and recommend an outcome; they do not grant repository authority.

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Document Template](13_DOCUMENT_TEMPLATE.md)
- [Review Process](15_REVIEW_PROCESS.md)
