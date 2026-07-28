# Changelog

## Document Control

- **Document ID:** `docs/14_CHANGELOG.md`
- **Status:** Review
- **Authority:** Historical Evidence Index
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.5.0
- **Last Updated:** 2026-07-28
- **Lifecycle:** Review
- **Source of Truth:** Merged Git history and scoped decision/evidence records
- **Approval:** Pending Founder review; merged Git history remains evidence

This changelog records repository outcomes. It does not create approval, runtime readiness, Product facts, or release authority.

## 2026-07-28 — BP2 Data Administration Lifecycle Approval

- `FD-BP2-ADM-001` records the ordered `DRAFT → REVIEW → APPROVED` lifecycle and completed review record `BP2-ADM-REVIEW-001`.
- Contract, Schema, Validator, and tests now require Founder decision evidence, named review roles, a linear transition history, and rejection of direct `DRAFT → APPROVED`.
- PR #18 merged the reviewed lifecycle record by Merge Commit, and protected Review-stage, final-PR, and post-merge `main` CI succeeded.
- Approval is documentation governance only: `implementation_authority` remains false and Product/Knowledge population, Admin UI, WordPress/WooCommerce, import, publication, deployment, runtime, and production remain `NO-GO`.

## 2026-07-28 — Post-PR16 Governance Reconciliation

- PR #17 reconciled the active current-state, baseline, roadmap, repository relationship, documentation index, navigation, repository health, traceability, changelog, and open-question records after PR #16.
- The reconciliation records the completed BP1 M1 hardening, removes its closed validation-tooling blocker, and advances the next safe action to read-only BP2 lifecycle decision preparation.
- BP2 remains `DRAFT`; Product/Knowledge population, Admin UI, WordPress/WooCommerce, import, publication, deployment, runtime, and production remain `NO-GO`.

## 2026-07-28 — BP1 M1 Accessibility and Local Validation Hardening

- PR #16 corrected primary-CTA contrast and added fail-closed contrast validation for the bounded BP1 local prototype.
- Local setup now creates an ignored validation environment from shared pinned requirements, and the BP1 validator is included in `make test`.
- PR and post-merge `main` CI succeeded. The merge created no WordPress/WooCommerce, Product/SKU, import, publication, deployment, runtime, or production authority.

## 2026-07-27 — Post-PR12 Governance Reconciliation

- PR #15 reconciled the active current-state, baseline, readiness, roadmap, documentation index, navigation, reading order, repository health, traceability, changelog, and open-question records after PR #12.
- Obsolete claims that PR #12 remained open or blocked for merge were removed from active documents; historical audit evidence was preserved unchanged.
- The reconciliation retains the BP2 Data Administration contract's `DRAFT` lifecycle and all Product, Knowledge, Admin UI, WordPress/WooCommerce, import, publication, deployment, and production `NO-GO` boundaries.

## 2026-07-27 — BP2 Data Administration Hardening

- PR #12 merged the documentation-only BP2 Data Administration scope and machine-readable contract.
- The merge added a closed JSON Schema Draft 2020-12 contract, deterministic offline validation, and positive, negative, and adversarial tests.
- The contract remains `DRAFT` with `implementation_authority: false`; no Admin UI, Product/SKU, WordPress/WooCommerce, import, publication, deployment, or production authority was created.

## 2026-07-26 — Post-Recovery Current State

- PR #14 aligned the current-state pointer after the recovery consolidation and preserved PR #12 as the then-open independent review target.
- That state was accurate before PR #12 hardening and merge; later active documents supersede its mutable operational facts.

## 2026-07-26 — Claude Recovery Consolidation

- PR #13 added a security-sanitized evidence report covering recovered Claude conversations, Project Knowledge, recovered file packages, and comparison with the then-current `main`.
- It recorded the Founder-confirmed closure of four exposed credentials without retaining their values.
- It rejected wholesale restoration of superseded repositories, raw exports, Mac inventory reports, legacy runtime code, and voided Product drafts.
- It reconciled the named current-state/navigation documents and retained mutable operational state exclusively in Current Project State.
- The merge granted no WordPress, Product/SKU, publication, deployment, or production authority.

## 2026-07-23 — BP2 Machine-Readable Data Blueprint

- PR #11 merged the controlled Pipe data blueprint, schema, and offline validator.
- It creates no final SKU, import, WordPress, WooCommerce, publication, deployment, or production authority.

## 2026-07-23 — BP1 Visible Local Prototype

- PR #10 merged the bounded Persian RTL local prototype and safety validator.
- It remains local review evidence and is not a canonical runtime implementation or Product truth source.

## 2026-07-23 — K-01 Governance and Knowledge Reconciliation

- Reconcile current-state, baseline, decision, traceability, navigation, and health records after Wave 2A–2C.
- Establish one Knowledge Archive Standard and separate lifecycle, Product Data, execution, and Atlas disposition vocabularies.
- Disposition all 173 Atlas planning rows and mark legacy Library Atlas documents as noncanonical archive references.
- Replace the placeholder test entry point with the validators already enforced by CI.
- PR #9 merged the bounded K-01 result; the merge did not create runtime, Product facts, Atlas promotion, or document lifecycle approval.

## 2026-07-23 — Build Phase 1 Implementation Roadmap

- PR #8 merged the visible-product-first Build Phase 1 implementation roadmap after the PR #9 governance baseline.
- The roadmap is planning evidence only; it created no Product/SKU, WordPress/WooCommerce, publication, deployment, or production authority.

## 2026-07-23 — Wave 2C Measurement Foundation

- PR #7 merged measurement contract/schema, two candidate dimensions, four candidate units, validator, fixtures, and CI checks.
- Measurement entries remain `CANDIDATE_UNVERIFIED`; no Product value, weight, availability, price, import, or runtime fact was created.

## 2026-07-23 — Wave 2B Product Attribute Foundation

- PR #6 merged Product Attribute contract/schema, supporting controlled registries, validator, fixtures, and CI checks.
- Canonical Product Attribute registry remains empty; no business values or Product records were created.

## 2026-07-23 — Wave 2A Product Core Foundation

- PR #5 merged Product core contract/schema, hierarchy entity/status registries, validator, fixtures, and CI checks.
- No canonical Product rows, Master Data, Golden data, commercial SKU, import, or runtime asset was created.

## 2026-07-20 — Wave 2 Governance Reconciliation

- PR #4 merged pre-implementation governance reconciliation.
- Canonical Product hierarchy and repository path ownership were recorded.

## Earlier Repository Integration

- PR #3 merged post-Wave-1 governance reconciliation.
- PR #2 merged Wave 1 governance.
- PR #1 merged repository bootstrap.

Exact SHAs and current branch state belong in [Current Project State](CURRENT_PROJECT_STATE.md), not this historical index.

## Related Documents

- [Changelog Policy](14_CHANGELOG_POLICY.md)
- [Current Project State](CURRENT_PROJECT_STATE.md)
- [Decision Log](10_DECISION_LOG.md)
- [Founder Decision Log](17_FOUNDER_DECISION_LOG.md)
- [Knowledge Archive Standard](KNOWLEDGE_ARCHIVE_STANDARD.md)
- [Claude Recovery and Repository Consolidation Audit](AUDIT_REPORT_CLAUDE_RECOVERY_2026-07-26.md)
