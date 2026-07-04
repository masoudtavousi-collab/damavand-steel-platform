# Changelog Policy

## Document Control

- **Document ID:** `docs/14_CHANGELOG_POLICY.md` (provisional path identifier)
- **Status:** Draft
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On changelog, version, release, baseline, or history-policy change
- **Lifecycle:** Draft
- **Source of Truth:** Approved [Repository Standards](07_REPOSITORY_GUIDE.md) and recorded Founder decisions; proposed version semantics remain non-authoritative until approved
- **Dependencies:** [Git Governance](GIT_GOVERNANCE.md), [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md)
- **Related Documents:** [Changelog](14_CHANGELOG.md), [Decision Log](10_DECISION_LOG.md), and [Release Checklist](../quality/RELEASE_CHECKLIST.md)
- **Traceability:** Changelog entry, approved commit or tag, decision source, compatibility impact, and release evidence
- **AI Compatibility:** AI-readable with gaps until Founder approval and first approved baseline
- **Approval:** Pending Founder approval

## Purpose

Define how changes are recorded without creating release or versioning decisions that have not been approved.

## Scope

Applies to the project changelog at [docs/14_CHANGELOG.md](14_CHANGELOG.md). ADR history and Git history remain separate records.

## Changelog Entry Requirements

Each entry must identify:

- Date
- Version or release identifier when approved and applicable
- Change category
- Concise description
- Related decision, issue, or change reference
- Migration, compatibility, security, or operational note when applicable

## Change Categories

- Added
- Changed
- Deprecated
- Removed
- Fixed
- Security
- Documentation

These categories classify records only and do not define release semantics.

## Record Boundaries

- The changelog summarizes approved changes; it does not replace Git history.
- ADRs explain significant decisions; the changelog links to them when implementation changes result.
- Audit reports record review findings; the changelog records adopted changes only.
- Unreleased or proposed work must not be represented as released work.

## Versioning

The proposed version classes, compatibility rules, and tag formats are defined once in [Git Governance](GIT_GOVERNANCE.md#versioning-strategy). They remain pending Founder approval under FD-GOV-002, FD-GOV-003, and FD-GOV-019.

This Changelog Policy does not define an independent versioning system.

## Review

Changelog entries are reviewed as part of the release or documentation change that introduces them.

## References

- [Changelog](14_CHANGELOG.md)
- [Decision Log](10_DECISION_LOG.md)
- [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md)
- [Release Checklist](../quality/RELEASE_CHECKLIST.md)
- [Git Governance](GIT_GOVERNANCE.md)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Review Process](15_REVIEW_PROCESS.md)
