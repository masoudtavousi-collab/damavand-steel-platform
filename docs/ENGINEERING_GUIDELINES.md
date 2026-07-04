# Enterprise Engineering Guidelines

## Document Control

- **Document ID:** `docs/ENGINEERING_GUIDELINES.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Build Engineer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On engineering workflow, branch, commit, review, approval, rollback, documentation, implementation, or quality-gate change
- **Lifecycle:** Review
- **Source of Truth:** Accepted Core Project Principles and ADRs; approved portions of [Repository Standards](07_REPOSITORY_GUIDE.md) and future Founder-approved [Git Governance](GIT_GOVERNANCE.md)
- **Dependencies:** [Repository Baseline v1.0](BASELINE_v1.0.md), [Git Governance](GIT_GOVERNANCE.md), [Review Process](15_REVIEW_PROCESS.md), and [Documentation Quality Standard](16_QUALITY_STANDARD.md)
- **Related Documents:** [Implementation Readiness](IMPLEMENTATION_READINESS.md), [Sprint Roadmap](SPRINT_ROADMAP.md), [Development Workflow](08_DEVELOPMENT_WORKFLOW.md), [Testing Strategy](13_TESTING_STRATEGY.md), and [Release Checklist](../quality/RELEASE_CHECKLIST.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, baseline v1.0, and future task/decision/review/test/release evidence
- **AI Compatibility:** AI-readable proposed engineering guidance; no AI product feature or autonomous approval authority
- **Approval:** Pending Founder review; the exact v1.0 baseline action is separately authorized and does not approve all future guidance

## Purpose

Define maintainable engineering controls for future repository work without changing architecture, business rules, or implementation scope.

## Engineering Principles

- Preserve accepted authority and stop on conflict or missing approval.
- Prefer approved plugins and supported configuration before custom development.
- Keep business/domain authority separate from platform configuration and presentation.
- Design and verify Mobile First and Persian RTL from the earliest change.
- Preserve Inquiry First and No Public Pricing on every surface and integration.
- Maintain one owner per data, template, schema, cache, workflow, and integration concern.
- Make changes small, traceable, reviewable, reversible, testable, observable, and exportable.
- Never commit secrets, personal/customer data, commercial archives, runtime files, generated dependencies, or WordPress Core.
- Preserve No Custom Theme, No Gravity Forms, No LiteSpeed Cache, and No AI Features in Phase 1.
- Optimize for routine non-programmer Founder/Admin manageability.

## Repository Workflow

1. Identify authorized task, governing sources, affected decisions, owner, reviewer, approval boundary, risks, and exclusions.
2. Start from the approved baseline/branch defined by the current Git policy.
3. Create a narrowly scoped branch when the approved branch model requires one.
4. Implement only approved scope; update related documentation and traceability in the same change.
5. Run applicable repository, documentation, architecture, security, platform, accessibility, performance, and test gates.
6. Record review evidence, findings, corrections, residual risks, rollback, and approval.
7. Merge/tag/release only through the authorized path.
8. Verify post-change state and retain evidence; do not rewrite approved history.

## Branch Strategy

The branch model remains the one proposed in [Git Governance](GIT_GOVERNANCE.md#branch-strategy) until Founder approval. The v1.0.0 initial baseline is the explicitly authorized bootstrap of unborn `main`; it is not precedent for future direct commits.

| Branch class | Intended use | Boundary |
| --- | --- | --- |
| `main` | Approved integrated baseline/release history | No future direct/unreviewed changes |
| `develop` | Future approved integration branch | Create only after branch policy approval |
| `feature/*` | Authorized implementation scope | No direct merge to `main` |
| `docs/*` | Documentation-only change | Cannot alter accepted authority without approval |
| `architecture/*` | Architecture proposal/approved record | No implementation mixed into architecture scope |
| `release/*` | Stabilization and validation | Only approved corrections; no scope expansion |
| `hotfix/*` | Urgent approved correction | Preserve back-merge, tests, and history |

Exact branch protection, merge method, provider settings, and delegated maintainers remain pending Founder approval.

## Commit Strategy

- Follow the proposed conventional format in Git Governance: `<type>(<scope>): <imperative summary>`.
- Keep one coherent change and authority domain per commit.
- Reference task/decision IDs, affected Core Principles, tests, compatibility, migration, security, and rollback when applicable.
- Never use a commit message to claim approval that is absent from repository evidence.
- Do not amend, force-push, squash away required evidence, or move approved tags.
- Validate ignored/excluded content and secrets before staging.
- The initial `repo(freeze): establish repository baseline v1.0.0` commit is limited to the exact Founder-authorized first baseline.

## Review Strategy

Every change receives review proportionate to risk:

| Change concern | Required review capability |
| --- | --- |
| Governance/authority | Repository Guardian and Founder |
| Architecture/platform boundary | Architecture reviewer and Founder |
| Product/taxonomy/technical steel facts | Qualified domain reviewer and Founder/delegate |
| Inquiry/Sales/CRM | Sales owner plus privacy/security as applicable |
| Content/SEO/media | Content, SEO, accessibility, domain, and legal/privacy as applicable |
| Security/privacy/infrastructure | Security, privacy/legal, operations, and technical review |
| Release/production | Quality, testing, operations, security, applicable domain reviewers, and Founder |

Self-review may find defects but does not replace independent review or Founder approval.

## Approval Workflow

```text
Authorized task
  -> scoped proposal/change
    -> objective validation
      -> assigned specialist review
        -> blocking findings resolved
          -> Founder approval or recorded delegation
            -> controlled merge/tag/release
              -> post-change verification
```

Draft/Review documents, audits, task outputs, AI output, successful tests, commits, or tags do not independently approve architecture, business rules, implementation, or production promotion.

## Rollback Policy

- Define rollback trigger, accountable decision-maker, recovery point, data/config/content implications, time boundary, and verification before change approval.
- Prefer a new reviewed revert/recovery commit; never move an approved tag or rewrite shared history.
- Back up and test restoration before database, content, configuration, plugin, theme, dependency, or infrastructure changes.
- Preserve forward migrations and reverse/restore limitations explicitly.
- If integrity, privacy, or recovery cannot be proven, block promotion and isolate the affected state.
- Production rollback does not close the incident; perform post-recovery review and record follow-up.

## Documentation Policy

- Update canonical documents, ADRs, decisions, open questions, traceability, navigation, health, runbooks, tests, and release notes when their subject changes.
- Use canonical metadata and relative links; preserve authority/lifecycle distinctions.
- Link to source facts instead of duplicating them in templates or operational notes.
- Record unknowns; do not invent business, product, taxonomy, field, role, provider, or service-level decisions.
- Documentation and implementation must remain synchronized within an approved change, but documentation cannot authorize implementation by itself.
- Preserve old decisions through supersession/deprecation/archive rather than silent rewriting.

## Implementation Policy

- No implementation begins without exact scope, approved architecture inputs, owner, branch, acceptance tests, rollback, environment, and explicit authorization.
- Use supported WordPress/WooCommerce/Blocksy/Elementor interfaces; never edit Core or vendor files.
- Do not add a custom/child theme, Gravity Forms, LiteSpeed Cache, or Phase 1 AI feature.
- Keep public pricing, Offer, cart, checkout, payment, and public quotation behavior disabled.
- Never create unapproved product/taxonomy/attribute/field values or infer protected Inquiry/Customer data.
- Keep configuration reproducible, environment-specific secrets external, licenses protected, and routine Admin workflows documented.
- Direct database writes and undocumented manual production changes are prohibited.

## Quality Gates

| Gate | Minimum evidence |
| --- | --- |
| Scope/authority | Task, source decisions, owner, reviewer, approval, exclusions |
| Repository | Clean expected state, valid branch, ignored/excluded files, no unresolved Git operation |
| Documentation | Metadata, links, anchors, index, navigation, traceability, no conflicts/orphans |
| Architecture/business | Applicable rules preserved; no drift or invented requirements |
| WordPress/WooCommerce | Supported versions/interfaces, no-price/inquiry/variable-parent/Admin boundaries |
| Blocksy/Elementor | Single template/design ownership, Mobile First, Persian RTL, accessibility |
| Security/privacy | Secrets, least privilege, data minimization, consent, logs, dependencies, abuse/failure paths |
| Data/content/SEO | Canonical identity, approved values, lifecycle, public/protected boundary, no cannibalization/price schema |
| Performance | Reproducible baseline/budget, no cache/privacy/functional regression; no LiteSpeed Cache |
| Testing | Traceable required tests, defects resolved, residual risks approved |
| Release | Exact artifact/configuration, backup/restore, rollback, monitoring, support, go/no-go authority |

A mandatory failure blocks merge, tag, release, deployment, or sprint exit. `Not applicable` requires recorded rationale.

## Exceptions

An exception requires a governing source, reason, scope, risk, owner, approver, expiry/review date, compensating control, tests, rollback, and traceability. No exception may silently weaken a Core Project Principle; changing one requires a new explicit Founder decision and impact review.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial v1.0 repository engineering guidelines; proposed for Founder review. |

## Navigation

- [Repository Baseline v1.0](BASELINE_v1.0.md)
- [Implementation Readiness](IMPLEMENTATION_READINESS.md)
- [Sprint Roadmap](SPRINT_ROADMAP.md)
- [Git Governance](GIT_GOVERNANCE.md)
