# Enterprise Platform Lifecycle

## Document Control

- **Document ID:** `repository/platform/PLATFORM_LIFECYCLE.md`
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Enterprise Architect, Repository Guardian, Engine Owners, Build Authority, Operations Owner, and Quality Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On platform stage, transition, gate, role, evidence, maintenance, evolution, or deprecation change
- **Lifecycle:** Review
- **Source of Truth:** [Platform Manifest](PLATFORM_MANIFEST.md), [Platform Governance](PLATFORM_GOVERNANCE.md), and explicit Founder approval
- **Dependencies:** [Platform Manifest](PLATFORM_MANIFEST.md), [Platform Architecture](PLATFORM_ARCHITECTURE.md), and [Platform Governance](PLATFORM_GOVERNANCE.md)
- **Related Documents:** [Engine Boundaries](ENGINE_BOUNDARIES.md), [Platform Versioning](PLATFORM_VERSIONING.md), [Platform Evolution](PLATFORM_EVOLUTION.md), and [Sprint Roadmap](../../docs/SPRINT_ROADMAP.md)
- **Traceability:** PM-007 through PM-010, PP-006, PP-019, Sprint 03E, and lifecycle rules PLC-001 through PLC-011
- **AI Compatibility:** AI-readable proposed lifecycle; no autonomous stage transition or approval
- **Approval:** Pending Founder and architecture/operations/quality review; no implementation lifecycle is activated

## Purpose

Define the permanent evidence-based path from an idea to controlled evolution/deprecation while separating Founder decision, repository authority, engine contracts, runtime implementation, QA, release, and maintenance.

## Lifecycle

```text
Idea
  ↓
Founder Decision
  ↓
Repository
  ↓
Engine
  ↓
Validation
  ↓
Implementation
  ↓
QA
  ↓
Release
  ↓
Maintenance
  ↓
Evolution
  ↓
Deprecation
```

## Lifecycle Rules

| ID | Proposed rule | Status |
| --- | --- | --- |
| PLC-001 | No stage begins without the previous stage's required evidence and exact scope. | Proposed pending Founder approval |
| PLC-002 | Founder Decision identifies purpose/constraints; it does not itself implement a change. | Proposed pending Founder approval |
| PLC-003 | Repository records authority/contracts before Engine or implementation work. | Proposed pending Founder approval |
| PLC-004 | Engine stage creates/reuses bounded contracts before Runtime binding. | Proposed pending Founder approval |
| PLC-005 | Validation is continuous and stage-specific; a later pass cannot erase an earlier authority defect. | Proposed pending Founder approval |
| PLC-006 | Implementation, QA, and Release require separate authorization even when architecture is approved. | Proposed pending Founder approval |
| PLC-007 | Maintenance cannot introduce unreviewed architecture or business behavior. | Proposed pending Founder approval |
| PLC-008 | Evolution uses compatible extension before constitutional redesign. | Proposed pending Founder approval |
| PLC-009 | Deprecation preserves replacements, consumers, data, redirects/mappings, retention, and recovery evidence. | Proposed pending Founder approval |
| PLC-010 | A failed gate returns to the authoritative upstream stage; downstream patching is prohibited. | Proposed pending Founder approval |
| PLC-011 | GO is scoped to one named transition; all later transitions remain NO-GO until separately passed. | Proposed pending Founder approval |

## Stage Contracts

| Stage | Required input | Controlled output | Primary owner | Exit gate | Blocking examples |
| --- | --- | --- | --- | --- | --- |
| Idea | Stated problem/opportunity | Non-authoritative proposal with scope/unknowns | Proposer + Founder | Founder authorizes decision analysis | No purpose, owner, authority, or scope |
| Founder Decision | Impact/options/evidence | Accepted/rejected/deferred decision with scope | Founder | Decision recorded and traced | Ambiguous directive, conflicting rule, missing impact |
| Repository | Accepted decision and sources | Versioned governing/supporting contracts, metadata, traceability | Repository Guardian + domain owner | Repository quality/authority gate | Broken authority, duplicate source, missing lifecycle |
| Engine | Approved repository inputs | Versioned bounded engine outputs/templates/mappings | Engine Owner | Engine boundary/compatibility/owner approval | Unowned output, overlap, runtime coupling, guessed data |
| Validation | Repository/Engine candidate | Pass/pending/blocked/fail evidence and remediation | Quality + domain reviewers | All hard gates for next stage pass | Required TBD, unsupported claim, no recovery |
| Implementation | Approved exact plan and validated inputs | Runtime/configuration/data change candidate | Build Authority + Runtime Owner | Change completed in approved environment with evidence | Scope expansion, missing backup, unauthorized dependency |
| QA | Implementation candidate | Functional/data/UX/security/performance/recovery evidence | Quality Owner + specialists | Acceptance criteria pass | Price leak, inquiry failure, RTL/mobile/accessibility/security defect |
| Release | Accepted QA and release plan | Versioned promoted release and release record | Release/Operations Owner | Founder/release approval, monitoring, rollback ready | Incomplete reconciliation, unknown rollback, unresolved critical issue |
| Maintenance | Released system + observations | Supported updates, incidents, health, backups, controlled corrections | Operations + Engine/Domain owners | Service/contract remains supported and compliant | Unsupported version, drift, ownerless dependency, repeated incident |
| Evolution | Approved new need/technology | Compatible extension or major-change proposal | Founder + Architecture Authority | Full impact/version/migration approval | Local redesign, silent breaking change, authority movement |
| Deprecation | Approved replacement/retirement | Transition, migration, retention, archive/historical evidence | Owner + Repository/Operations | Consumers migrated/retired and recovery preserved | Orphan consumers/data, broken links, lost history, no replacement |

## Validation Across Stages

| Concern | Repository/Engine | Implementation/QA | Release/Maintenance |
| --- | --- | --- | --- |
| Authority | Source, status, approval, traceability | Exact approved task/config mapping | Drift/decision conformance |
| Data | Contract, owner, schema, validation | Migration/import/reconciliation | Integrity, backup, retention, export |
| Security/privacy | Threat/access/data-flow design | Controls and negative tests | Monitoring, incidents, review |
| Experience | Mobile/RTL/accessibility requirements | Device/workflow/admin tests | Regression/user evidence |
| Inquiry/no-price | Contract and prohibited surfaces | Exhaustive runtime tests | Monitoring/regression |
| Compatibility | Versions, consumers, mappings | Staging/migration/rollback | Upgrade/deprecation evidence |

## Rework Flow

```text
Blocking evidence
  -> freeze affected transition
      -> identify authoritative source stage
          -> obtain approved correction
              -> regenerate/reimplement only affected outputs
                  -> rerun all dependent validations
```

Audit findings do not directly change runtime or governing sources.

## Maintenance Rules

- Maintain version/configuration/dependency/data/owner inventories.
- Monitor security, performance, availability, inquiry, no-price, SEO, integrations, backups, and data quality.
- Apply supported upgrades through compatibility/staging/recovery/release gates.
- Record incidents and correct at the authoritative layer.
- Revalidate after material vendor, runtime, engine, schema, content, or integration change.
- Maintenance convenience cannot bypass CP-001 through CP-010.

## Evolution Rules

- Minor compatible needs extend existing contracts.
- New reusable domain concern may create an Engine through admission review.
- New runtime implements existing contracts through an adapter.
- New website consumes existing Engines and adds channel-specific delivery contracts.
- Constitutional purpose/authority/layer change requires Platform major version and Founder approval.

## Deprecation Rules

- Identify replacement or explicit no-replacement rationale.
- Inventory all consumers, data, IDs, URLs, integrations, templates, releases, and owners.
- Define transition period, compatibility bridge if approved, migration, redirects/mappings, retention/deletion, validation, rollback, and end condition.
- Mark old source Deprecated/Superseded/Archived/Historical according to repository lifecycle; never delete authority history casually.
- Prevent new dependencies on deprecated assets.

## Lifecycle Separation

Platform Lifecycle does not replace:

- Document Lifecycle.
- ADR decision status.
- Product lifecycle.
- Inquiry/CRM workflow statuses.
- Engine/template versions.
- Runtime release/incident lifecycle.

Mappings among lifecycles are explicit; one status never silently changes another.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03E proposed Platform Lifecycle. |

## Navigation

- [Platform Manifest](PLATFORM_MANIFEST.md)
- [Platform Governance](PLATFORM_GOVERNANCE.md)
- [Platform Versioning](PLATFORM_VERSIONING.md)
- [Platform Evolution](PLATFORM_EVOLUTION.md)
