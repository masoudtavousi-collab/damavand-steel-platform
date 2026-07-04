# Enterprise Platform Principles

## Document Control

- **Document ID:** `repository/platform/PLATFORM_PRINCIPLES.md`
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Enterprise Architect, Repository Guardian, Business Reviewer, Security Reviewer, and Quality Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On accepted Core Project Principle, platform principle, precedence, interpretation, or exception change
- **Lifecycle:** Review
- **Source of Truth:** [Platform Manifest](PLATFORM_MANIFEST.md), accepted CP-001 through CP-010, ADR-0001, and explicit Founder approval
- **Dependencies:** [Platform Manifest](PLATFORM_MANIFEST.md), [Project Bible](../../docs/00_PROJECT_BIBLE.md), and [Project Constitution](../../docs/01_PROJECT_CONSTITUTION.md)
- **Related Documents:** [Platform Architecture](PLATFORM_ARCHITECTURE.md), [Platform Governance](PLATFORM_GOVERNANCE.md), [Engine Boundaries](ENGINE_BOUNDARIES.md), and [Product Engine Rules](../engine/product/ENGINE_RULES.md)
- **Traceability:** CP-001 through CP-010 and Sprint 03E principles PP-001 through PP-020
- **AI Compatibility:** AI-readable proposed principles; no AI authority, feature, or autonomous exception
- **Approval:** Pending explicit Founder approval; platform-specific principles are not yet Governing

## Purpose

Define the durable principles used to evaluate Platform, Repository, Engine, Runtime, Website, integration, release, and evolution decisions without changing accepted business rules.

## Precedence

Accepted Founder decisions, Core Project Principles, business rules, and accepted ADRs remain controlling. These Platform principles explain architectural application within that boundary. A principle conflict is blocked and escalated; convenience, cost, age, or implementation state does not silently resolve it.

## Principles

| ID | Principle | Rule |
| --- | --- | --- |
| PP-001 | Single Source of Truth | Assign one canonical authority per fact, decision, identity, contract, configuration concern, and metric; projections reference rather than duplicate it. |
| PP-002 | Configuration First | Use supported configuration before custom code, preserving export, review, validation, and rollback. This inherits CP-002. |
| PP-003 | Plugin First | For runtime extension, prefer one approved supported plugin/capability owner over custom development or overlapping plugins. This inherits CP-001. |
| PP-004 | Template First | Generate repeatable family/content/configuration contracts from versioned approved templates with provenance, never blank-start duplicates. |
| PP-005 | Engine First | Put reusable domain transformation behind an owned Engine contract before binding it to a runtime or website. |
| PP-006 | Repository First | Record authority, contract, version, change, validation, and recovery before applicable implementation. |
| PP-007 | Data First | Define stable identities, ownership, classification, validation, lifecycle, and portability before presentation or integration. |
| PP-008 | Knowledge First | Make approved context, relationships, decisions, unknowns, and evidence understandable without historical conversation. |
| PP-009 | Inquiry First | Every commercial channel remains inquiry-first and preserves selected context without creating public transaction behavior. This inherits CP-005. |
| PP-010 | No Public Pricing | No runtime, website, API, feed, schema, cache, search, analytics, integration, or future channel exposes public pricing. This inherits CP-006. |
| PP-011 | Founder Controlled | Founder retains final approval authority unless an explicit approved delegation defines narrower authority. |
| PP-012 | Enterprise Ready | Every material capability has ownership, lifecycle, security, privacy, performance, accessibility, operations, support, export, replacement, and recovery considerations. |
| PP-013 | Long-Term Maintainability | Prefer stable contracts, supported capabilities, clear ownership, low duplication, reversible changes, and documented deprecation over short-term convenience. |
| PP-014 | Scalable Architecture | Extend through bounded engines, templates, adapters, and consumers without copying authority or redesigning unrelated domains. |
| PP-015 | Runtime Replaceability | Runtime technology implements Platform contracts; stable data and knowledge remain portable and independent. |
| PP-016 | Mobile First | Every applicable public/admin workflow and validation begins with constrained mobile behavior. This inherits CP-003. |
| PP-017 | Persian RTL | Persian RTL labels, content, navigation, forms, tables, search, accessibility, and Admin workflows are first-class. This inherits CP-004. |
| PP-018 | Explicit Ownership | Every active platform concern has one authority owner, operational owner, reviewers, approver, and escalation path. |
| PP-019 | Reversible and Evidence-Based | High-risk change requires evidence, staging, backup/restore, rollback or forward recovery, reconciliation, and acceptance criteria. |
| PP-020 | Secure and Minimal | Minimize capability, data, privilege, dependency, duplication, and exposure while preserving required outcomes and auditability. |

## Inherited Prohibitions

- No Custom Theme (CP-007).
- No Gravity Forms (CP-008).
- No LiteSpeed Cache (CP-009).
- No AI Features in Phase 1 (CP-010).

These remain Platform-wide constraints for every current runtime/website. Future technology does not create an implied exception.

## Principle Sequence

For a new capability:

```text
Founder-approved need
  -> Knowledge/Repository authority
      -> Data contract
          -> Engine boundary/template
              -> Configuration/Plugin evaluation
                  -> Runtime adapter
                      -> Website/channel delivery
                          -> Validation + release + maintenance
```

This is a design sequence, not a claim that every concern requires a new plugin or engine. Use the smallest existing approved owner that satisfies the need.

## Single-Source Rules

- Business rules: approved business authority/accepted ADR.
- Platform architecture: approved Platform Manifest set.
- Repository governance: approved repository-governance sources.
- Engine contract: approved engine standard within its boundary.
- Product facts: approved Product Data sources.
- Content facts: approved content/entity sources.
- SEO metadata/schema: projections of approved public facts.
- Runtime configuration: approved configuration source/inventory, not ad hoc Admin state.
- Analytics: measurement evidence, never business/domain truth by itself.

One source of truth does not mean one file contains everything. It means each concern has one canonical owner and explicit references.

## Exception Policy

An exception requires:

- Exact principle and scope.
- Business/technical reason and rejected alternatives.
- Owner, duration, risk, controls, tests, migration, rollback, and expiry.
- Founder approval at the same or higher authority as the affected rule.
- Traceability and dependent-document updates.

No accepted Core Project Principle exception is created by Sprint 03E.

## Validation Questions

- Is the source authority explicit and approved?
- Is the concern owned exactly once?
- Does it preserve all applicable CP rules?
- Can data/knowledge survive runtime replacement?
- Is the change generated/configured through the correct Engine/template/adapter?
- Are security, privacy, Persian RTL, mobile, accessibility, operations, and recovery addressed?
- Is the next action explicitly approved and bounded?

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03E proposed Platform Principles. |

## Navigation

- [Platform Manifest](PLATFORM_MANIFEST.md)
- [Platform Architecture](PLATFORM_ARCHITECTURE.md)
- [Engine Boundaries](ENGINE_BOUNDARIES.md)
- [Platform Governance](PLATFORM_GOVERNANCE.md)
