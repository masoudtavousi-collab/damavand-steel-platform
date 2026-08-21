# Testing Strategy

## Purpose

Define the evidence layers and fail-closed quality gates used to validate repository
changes and any separately authorized future Runtime work.

## Scope

This Draft covers local and CI repository validation, contract/schema/validator
tests, domain review, security/privacy review, accessibility/RTL checks, integration
and migration evidence, Runtime/UAT separation, rollback/recovery proof, and release
acceptance. C007 runs repository tests only and authorizes no environment activity.

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

## Testing Baseline

- Every change must pass the repository's unified validation entry points, link and
  manifest checks, scope checks, and diff hygiene without weakening controls.
- Machine-readable packages require deterministic positive, negative, mutation,
  and adversarial validation; documentation requires source, authority, owner,
  lifecycle, traceability, and link review.
- Domain correctness, security/privacy, Mobile First, Persian RTL, accessibility,
  inquiry/no-price behavior, and regression anchors are distinct gates.
- Local and CI PASS prove the reviewed patch only. Runtime verification, UAT,
  backup/restore, deployment, Production acceptance, and Merge each require their
  own evidence and authorization.

`MISSING_AUTHORITY_INPUT` — exact input: named test and release owners, approved
Runtime/Staging targets, supported device/browser matrix, domain/UAT scenarios,
severity and acceptance thresholds, test-data/privacy policy, and recovery/release
criteria. It is missing because no Runtime, Staging, Production, deployment, or
release Mission is authorized. Affected domain/document: Testing Strategy and
future release owners. Safe behavior without it: run repository-local/CI validation
only and block Runtime or release claims.

Original `Placeholder Sections` disposition: `RESOLVED_FROM_CANONICAL_EVIDENCE`;
environment-specific acceptance remains separately gated.

## Related Documents

- [Business Rules](03_BUSINESS_RULES.md)
- [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md)
- [Testing Checklist](../quality/TESTING_CHECKLIST.md)
- [Quality Standard](16_QUALITY_STANDARD.md)
- [C007 Governance Convergence Scope](C007_GOVERNANCE_CONVERGENCE_PHASE1_ARCHITECTURE_BASELINE_SCOPE_V1.0.md)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Technical Reading Path](09_NAVIGATION_MAP.md#technical-path)
