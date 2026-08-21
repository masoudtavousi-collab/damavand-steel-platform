# DS-001 Project Constitution

## Table of Contents

- [Purpose](#purpose)
- [Core Principle Compliance](#core-principle-compliance)
- [Governance Rule Inheritance](#governance-rule-inheritance)
- [Conflict Resolution Framework](#conflict-resolution-framework)
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

Defines the governing purpose of the Project Constitution within the project documentation set.

## Core Principle Compliance

The Constitution is governed by the ten authoritative [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles): CP-001 Plugin First, CP-002 Configuration First, CP-003 Mobile First, CP-004 Persian RTL, CP-005 Inquiry First, CP-006 No Public Pricing, CP-007 No Custom Theme, CP-008 No Gravity Forms, CP-009 No LiteSpeed Cache, and CP-010 No AI Features (Phase 1).

No constitutional rule may override a Core Project Principle. Changes to those principles require an explicit Founder decision and an update to the [Rule Traceability](00_PROJECT_BIBLE.md#rule-traceability) matrix.

## Governance Rule Inheritance

Rule inheritance is scope-bound. A dependent document receives applicable constraints from its authority sources but does not receive authority merely by referencing them.

```text
Accepted Founder Decisions and Core Project Principles
  -> Project Bible
      -> Project Constitution
          -> Business Rules + Enterprise Architecture
              -> Technology Stack
                  -> Repository Governance and Standards
                      -> SEO + UX + WordPress Architecture + Delivery Documents
                          -> Future Implementation Documents
```

Business Rules and Enterprise Architecture are peer authorities in their declared domains. The diagram expresses constraint flow, not permission for one peer to rewrite the other.

Inheritance rules:

- Every child preserves applicable parent constraints and links its Authority Source.
- A child may add detail only within its approved scope.
- A child cannot weaken, reinterpret, or silently exclude an inherited rule.
- Repository, SEO, UX, WordPress, delivery, and implementation documents inherit all applicable CP rules and domain decisions.
- Review, audit, validation, task, and conversation outputs inherit constraints but never inherit governing authority.
- If an inherited rule is not applicable, the child records `Not applicable` with approved rationale; omission is not an exception.

## Conflict Resolution Framework

Resolve a conflict using evidence in this order:

1. Confirm that both statements are current, applicable to the same scope, and correctly classified.
2. Apply approved governing authority before supporting, Review, Draft, audit, task, or conversation context.
3. Apply an explicitly accepted Founder decision within its recorded decision scope.
4. Apply the higher rule-inheritance level when a dependent document conflicts with its authority source.
5. Between approved peer authorities, apply the more specific in-scope statement only when it does not violate a shared parent constraint.
6. Apply an explicit approved supersession or replacement relationship.
7. Use version or date only between records with equal authority, approval, scope, and a valid lineage; a newer file does not automatically win.
8. If the conflict remains, mark affected work Blocked and obtain a recorded Founder decision.

Authority precedence is stronger than approval date, version number, filename number, document location, task recency, or author identity.

Founder override requires an explicit, recorded decision with scope, affected rules, rationale, and traceability updates. Conversation or task wording alone does not permanently amend repository authority.

Historical, Superseded, Deprecated, Archived, and Cancelled records provide context only and cannot override current Approved authority. Repository exceptions require the same approval and traceability as the rule they affect; no exception is implied by existing files, implementation, or operational convenience.

## Scope

This Draft Constitution summarizes the authority hierarchy, change controls,
separation of duties, evidence discipline, and fail-closed conflict handling that
already govern the repository. It does not replace the Project Bible, accepted
Founder decisions, domain owners, or Mission-specific approval packets.

## Audience

Founder, Project Commander, Repository Guardian, domain reviewers, independent
QA/security reviewers, and agents preparing or reviewing bounded repository work.

## Status

Draft

## Owner

Founder

## Reviewer

Repository Guardian

## Approval Authority

Founder

## Version

0.2.0

## Last Updated

2026-08-21

## Last Review

2026-08-21

## Related Documents

- [DS-000 Project Bible](00_PROJECT_BIBLE.md)
- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md)
- [Review Process](15_REVIEW_PROCESS.md)
- [C007 Governance Convergence Scope](C007_GOVERNANCE_CONVERGENCE_PHASE1_ARCHITECTURE_BASELINE_SCOPE_V1.0.md)

## Overview

Repository work is governed by explicit authority, bounded scope, traceable
evidence, separation of duties, and fail-closed validation. Planning, Draft,
Review, audit, Slack context, date, or implementation convenience does not create
mutation or approval authority. The current semantic state is owned by
[Current Project State](CURRENT_PROJECT_STATE.md); each Mission resolves the live
Git state dynamically.

## Definitions

- **Canonical owner:** the approved source responsible for a domain's governing
  truth; a reference or projection does not transfer that authority.
- **Execution authority:** a recorded, scope-bound authorization to mutate the
  repository or another governed system.
- **Evidence:** source material whose class, scope, time, and provenance determine
  what it may support.
- **NO-GO:** an explicit denial that remains effective until separately superseded
  by equal or higher authority.
- **Semantic state:** the current phase, gates, authorization, and next action,
  independent from an ordinary Git-tip change.

## Responsibilities

- The Founder approves protected business decisions and any authority expansion.
- The Project Commander bounds Missions and enforces stop conditions.
- The Repository Guardian protects source hierarchy, owner boundaries, and scope.
- Domain reviewers validate claims in their accountable domains.
- Independent reviewers inspect the integrated diff and evidence rather than agent
  summaries.
- Executors change only authorized paths, validate proportionately, and stop at
  the stated terminal condition.

## Decisions

The ten Core Project Principles, accepted ADRs, recorded Founder decisions, and
approved Mission packets apply only within their recorded scope. Repository First,
Documentation Before Implementation, Product Data First, Taxonomy First,
Knowledge First, Plugin First, Configuration First, and Founder Controlled remain
the Phase-1 governance baseline. C007 records no new business or architecture
decision and does not promote this Draft document.

## Constraints

- Historical context is not live state; a newer date is not higher authority.
- A top-level summary must link to, not duplicate, its canonical domain owner.
- Missing evidence is not negative evidence and `UNKNOWN` is not unavailable.
- Review, validation, CI success, or a clean PR does not authorize Merge or a
  successor Mission.
- Product, commercial, Runtime, Staging, Production, deployment, and publication
  changes require their own explicit gates.

## Open Questions

`MISSING_AUTHORITY_INPUT` — exact input: Founder approval, revision, or rejection
of this Draft Constitution as a governing controlled document. It is missing
because the C007 authorization permits bounded convergence and review, not
lifecycle approval. Affected domain/document: DS-001 governance lifecycle. Safe
behavior without it: keep status `Draft`, preserve existing accepted authorities,
and require Mission-specific approval for every mutation.

## Founder Decisions

Founder decisions are recorded in the [Founder Decision Log](17_FOUNDER_DECISION_LOG.md)
with durable locators and bounded effects. The C007 authorization permits this
documentation reconciliation only; it is not blanket approval of pending entries
and creates no Product, commercial, Runtime, Merge, or successor authority.

## Future Improvements

`NOT_APPLICABLE_WITH_EVIDENCE` — this top-level owner does not schedule future
work. [Current Project State](CURRENT_PROJECT_STATE.md) owns the active semantic
state and [Project Execution Roadmap](PROJECT_EXECUTION_ROADMAP.md) owns sequenced
planning. Evidence: the C007 packet authorizes no successor Mission. Any later
constitutional proposal requires its own bounded authority.
