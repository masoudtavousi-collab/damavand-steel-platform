# DS-005 Repository Standards

## Table of Contents

- [Purpose](#purpose)
- [Core Principle Enforcement](#core-principle-enforcement)
- [Numbering Scalability Proposal](#numbering-scalability-proposal)
- [Repository and Approval Baseline](#repository-and-approval-baseline)
- [Git Governance Relationship](#git-governance-relationship)
- [Scope](#scope)
- [Audience](#audience)
- [Status](#status)
- [Owner](#owner)
- [Reviewer](#reviewer)
- [Approval Authority](#approval-authority)
- [Version](#version)
- [Last Updated](#last-updated)
- [Last Review](#last-review)
- [Related Documents](#related-documents)
- [Overview](#overview)
- [Definitions](#definitions)
- [Responsibilities](#responsibilities)
- [Decisions](#decisions)
- [Constraints](#constraints)
- [Open Questions](#open-questions)
- [Founder Decisions](#founder-decisions)
- [Future Improvements](#future-improvements)

## Purpose

Defines the governing purpose of the Repository Standards document within the project documentation set.

## Core Principle Enforcement

Every repository change must trace to and preserve the authoritative [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles): CP-001 Plugin First, CP-002 Configuration First, CP-003 Mobile First, CP-004 Persian RTL, CP-005 Inquiry First, CP-006 No Public Pricing, CP-007 No Custom Theme, CP-008 No Gravity Forms, CP-009 No LiteSpeed Cache, and CP-010 No AI Features (Phase 1).

Review evidence must identify affected rule IDs. A change that contradicts a Core Project Principle fails review unless the Founder first changes the authoritative rule and its traceability.

## Numbering Scalability Proposal

### Current Issue

The current top-level documentation contains duplicate numeric prefixes `08` through `14`. DS-004 and DS-005 also do not match their filename prefixes. This can create ambiguous sorting, unclear identifier ownership, and future collision risk as the document set grows.

No file is renamed by Batch 02A.

### Recommended Modular Strategy

| Proposed namespace | Intended document family |
| --- | --- |
| `GOV-NNN` | Governance, lifecycle, review, navigation, and policy documents |
| `BUS-NNN` | Business-rule and business-strategy documents |
| `ARC-NNN` | Enterprise and platform architecture documents |
| `TEC-NNN` | Technology, repository, and development standards |
| `OPS-NNN` | Deployment, operations, security, and release documents |
| `QUA-NNN` | Quality, testing, UX, SEO, and assurance documents |
| `ADR-NNNN` | Architecture Decision Records; existing ADR sequence remains distinct |
| `AUD-BATCH-NN` | Historical audit reports |

The namespace is a proposal only. If approved, a separate migration plan must preserve link integrity, historical identity, and an old-to-new identifier map.

### Founder Decision

TODO (Founder Decision Required): approve, revise, or reject the modular numbering strategy before any rename.

## Repository and Approval Baseline

The canonical proposed branch, version, tag, baseline, commit, release, backup, change, freeze, and Git-validation rules are maintained in [Git Governance](GIT_GOVERNANCE.md). This section preserves the Batch 02A baseline context and does not define a separate Git policy.

### Repository Baseline

The Repository Baseline is the first Founder-approved, version-controlled snapshot of the repository. Batch 02A documents the baseline criteria but does not create the baseline or execute Git operations.

### Approval Baseline

The Approval Baseline is the set of documents, ADRs, Core Project Principles, review evidence, and quality results explicitly approved by the Founder. Draft content and unresolved Founder decisions are excluded from approved authority unless their governing source explicitly states otherwise.

### Versioning Strategy

Document versions, ADR identifiers, repository versions, and release versions remain separate identifiers. Their detailed increment and compatibility semantics require Founder approval through the existing versioning decisions.

### Review Strategy

The Repository Guardian performs governance and consistency review. The Founder is the Approval Authority. Domain review evidence must be added when a change affects architecture, business, security, operations, or another controlled domain.

### Commit Strategy

No Git operation is performed in Batch 02A. After Founder approval, the proposed baseline should be recorded as one reviewable, scoped baseline change with an approval reference. Subsequent changes should remain traceable to their authorized task and review evidence.

### Release Strategy

A repository release may be proposed only after an Approval Baseline exists, required quality gates pass, release scope is identified, and the Founder records approval. Release-version semantics remain governed by the pending Founder versioning decision.

### Baseline Decision

TODO (Founder Decision Required): approve the baseline, commit, and release strategy before creating the first baseline.

## Git Governance Relationship

- Repository Standards defines repository-wide boundaries and Core Project Principle enforcement.
- [Git Governance](GIT_GOVERNANCE.md) defines proposed Git evolution and history controls.
- [Changelog Policy](14_CHANGELOG_POLICY.md) defines change-record content and defers version and release semantics to Git Governance.
- No Git operation, baseline, tag, branch creation, remote configuration, backup, or release is authorized merely by these cross-references.

## Scope

TODO (Founder Decision Required)

## Audience

TODO (Founder Decision Required)

## Status

Draft

## Owner

Founder

## Reviewer

Repository Guardian

## Approval Authority

Founder

## Version

0.1.0

## Last Updated

2026-07-03

## Last Review

2026-07-03

## Related Documents

- [DS-000 Project Bible](00_PROJECT_BIBLE.md)
- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Navigation Map](09_NAVIGATION_MAP.md)
- [Documentation Quality Standard](16_QUALITY_STANDARD.md)
- [Document Template](13_DOCUMENT_TEMPLATE.md)
- [Repository Metadata Standard](REPOSITORY_METADATA.md)
- [Repository Traceability Matrix](TRACEABILITY_MATRIX.md)
- [Repository Knowledge Graph](KNOWLEDGE_GRAPH.md)
- [Git Governance](GIT_GOVERNANCE.md)

## Overview

This section will provide the approved overview for this document.

TODO (Founder Decision Required)

## Definitions

TODO (Founder Decision Required)

## Responsibilities

TODO (Founder Decision Required)

## Decisions

TODO (Founder Decision Required)

## Constraints

TODO (Founder Decision Required)

## Open Questions

TODO (Founder Decision Required)

## Founder Decisions

TODO (Founder Decision Required)

## Future Improvements

TODO (Founder Decision Required)
