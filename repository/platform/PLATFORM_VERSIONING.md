# Enterprise Platform Versioning

## Document Control

- **Document ID:** `repository/platform/PLATFORM_VERSIONING.md`
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Enterprise Architect, Repository Guardian, Engine Owners, Data Owner, Release Owner, Migration Owner, and Quality Reviewer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On version domain, compatibility, migration, release, baseline, deprecation, or version-format change
- **Lifecycle:** Review
- **Source of Truth:** [Platform Manifest](PLATFORM_MANIFEST.md), Repository Baseline v1.0, Product Engine Rules, and explicit Founder approval
- **Dependencies:** [Platform Manifest](PLATFORM_MANIFEST.md), [Platform Governance](PLATFORM_GOVERNANCE.md), [Repository Baseline v1.0](../../docs/BASELINE_v1.0.md), and [Product Engine Rules](../engine/product/ENGINE_RULES.md)
- **Related Documents:** [Platform Lifecycle](PLATFORM_LIFECYCLE.md), [Platform Evolution](PLATFORM_EVOLUTION.md), [Engineering Guidelines](../../docs/ENGINEERING_GUIDELINES.md), and [Release Notes v1.0](../../docs/RELEASE_NOTES_v1.0.md)
- **Traceability:** PM-008, PM-009, PP-013 through PP-015, FRZ-001 through FRZ-006, Sprint 03E, and versioning rules PV-001 through PV-012
- **AI Compatibility:** AI-readable proposed versioning; no autonomous bump, migration, release, or compatibility approval
- **Approval:** Pending Founder/repository/architecture/release review; existing Repository v1.0.0 remains unchanged

## Purpose

Define independent version domains and compatibility rules so Platform, Repository, Engines, Templates, Data, Releases, and Migrations evolve without ambiguous coupling.

## Versioning Rules

| ID | Proposed rule | Status |
| --- | --- | --- |
| PV-001 | Every material controlled artifact identifies its version domain and current version. | Proposed pending Founder approval |
| PV-002 | A version change in one domain never automatically bumps another domain. | Proposed pending Founder approval |
| PV-003 | Use `MAJOR.MINOR.PATCH` for Platform, Repository, Engine, Template, Data-contract, and Release versions unless an approved domain standard requires otherwise. | Proposed pending Founder approval |
| PV-004 | Major means incompatible contract/authority change requiring migration; Minor means backward-compatible capability; Patch means compatible correction/clarification. | Proposed pending Founder approval |
| PV-005 | Draft/Review versions do not imply approval or release. | Required by repository governance |
| PV-006 | Every consumer records compatible source/engine/template/data/runtime ranges or exact approved versions. | Proposed pending Founder approval |
| PV-007 | Migration identifiers are immutable, ordered, non-reused, and trace source/target versions. | Proposed pending Founder approval |
| PV-008 | Release versions identify exact component/configuration/data/migration sets and environment promotion evidence. | Proposed pending Founder approval |
| PV-009 | Breaking changes preserve predecessor, migration, rollback/forward recovery, deprecation, and consumer evidence. | Proposed pending Founder approval |
| PV-010 | Version/date/filename does not override authority, lifecycle, or approval. | Required by Project Constitution |
| PV-011 | Runtime/vendor versions are dependency versions, not Platform versions. | Proposed pending Founder approval |
| PV-012 | Security/emergency fixes still record compatibility, recovery, review, and retrospective approval. | Proposed pending Founder approval |

## Version Domains

### Platform Version

Versions the approved constitutional set: Manifest, Principles, Architecture, Engine Boundaries, Lifecycle, Governance, Directory Standard, Versioning, and Evolution.

- Major: purpose/authority/layer semantics or required engine-admission contract breaks.
- Minor: backward-compatible principle, boundary, engine type, lifecycle/gate, or extension capability.
- Patch: non-semantic clarification, link/metadata correction, or compatible validation tightening.

The Sprint 03E Platform set is `0.1.0` Review, not an approved Platform release.

### Repository Version

Versions an exact controlled repository baseline/tree and manifest. Repository v1.0.0 remains the accepted local baseline. New working files do not change that frozen version until a separately approved baseline/release task creates a successor.

### Engine Version

Versions one Engine's purpose, inputs, outputs, templates, validation, and compatibility contract. Engines version independently. Product Engine is currently `0.1.0` Review.

### Template Version

Versions one reusable generation structure. Generated outputs record exact template ID/version. A template bump triggers affected-output compatibility review; it does not silently regenerate families.

### Data Version

Versions a governed schema/contract or approved dataset snapshot, explicitly labeled as one of:

- Schema/contract version.
- Controlled vocabulary/registry version.
- Family data-set version.
- Mapping version.

Data version never means stock freshness, price validity, supplier availability, or runtime database version. Content/value changes record evidence, owner, compatibility, and affected consumers.

### Release Version

Versions a promoted, deployable runtime/website delivery set. It references exact Repository, Platform, Engine, Template-generated outputs, Data, migrations, configuration, dependencies, and environment evidence. Repository freeze is not automatically a product/runtime release.

### Migration Version

Identifies one ordered immutable source-to-target transition. Each migration records:

- Unique non-reused ordered ID; exact token syntax remains fixed by the first separately approved migration standard.
- Source/target version domains and values.
- Preconditions, owner, scope, transformations, stable-ID mapping.
- Dry run, backup/restore, validation, reconciliation, rollback/forward recovery.
- Applied environments, timestamps/evidence, result, and re-run protection.

Sprint 03E creates no migration identifier or migration.

## Compatibility Levels

| Level | Meaning | Required action |
| --- | --- | --- |
| Compatible | Existing approved consumers operate without change | Validate and record |
| Compatible with adoption | New optional capability; old consumers retain defined absence behavior | Plan adoption and test both states |
| Conditionally compatible | Requires supported adapter/configuration/data preparation | Document conditions, migrate/test/recover |
| Breaking | Existing contract/consumer cannot safely continue | Major version, full migration/deprecation/approval |
| Unknown | Evidence insufficient | Block promotion/release |

## Compatibility Matrix

Every release/change can record:

| Consumer | Platform | Engine | Template/output | Data/mapping | Runtime/dependency | Compatibility | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{CONSUMER}}` | `{{VERSION}}` | `{{VERSION}}` | `{{VERSION}}` | `{{VERSION}}` | `{{VERSION}}` | Compatible/Conditional/Breaking/Unknown | `{{REFERENCE}}` |

Placeholder rows are template structure only and create no current compatibility claim.

## Version Bump Decision

1. Identify semantic change and authority.
2. Inventory all direct/indirect consumers and stored/generated data.
3. Determine compatible/additive/conditional/breaking/unknown impact.
4. Select version bump in the owning domain only.
5. Define migration, tests, recovery, deprecation, and release impacts.
6. Review and obtain Founder/owner approval.
7. Update manifests, dependencies, traceability, changelog/release notes, health, and consumers.

## Backward Compatibility

- Preserve stable IDs, field meanings, accepted rules, URLs/contracts, and source ownership.
- Add optional fields with explicit null/absence behavior.
- Never reuse removed IDs/versions for different meaning.
- Provide adapters only as explicit temporary/maintained contracts, not silent dual authority.
- Deprecate before removal when consumers exist.
- Keep predecessor accessible for audit/recovery according to retention policy.
- Unknown compatibility blocks implementation/release.

## Version Authority

Only the approved owner/Approval Authority may accept a version/release transition. Automated tools may calculate candidates or validate manifests but cannot approve versions. Git tags, filenames, dates, package versions, or deployed state do not independently establish Platform authority.

## Current Version Evidence

| Domain | Current observable state | Meaning |
| --- | --- | --- |
| Platform | `0.1.0` Review | Proposed Sprint 03E constitution set; not approved |
| Repository | `1.0.0` accepted baseline plus later working changes | Baseline remains frozen; no successor created here |
| Product Engine | `0.1.0` Review | Template contract pending Founder approval |
| Product Engine templates | `0.1.0` Review individually | No approved generated non-Pipe family set |
| Pipe data assets | Individual `0.1.0` Review documents | Not a released product dataset/import |
| Runtime release | `TBD` | No release created by Sprint 03E |
| Migration | None | No migration created or executed |

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 03E proposed multi-domain Platform Versioning. |

## Navigation

- [Platform Manifest](PLATFORM_MANIFEST.md)
- [Platform Governance](PLATFORM_GOVERNANCE.md)
- [Platform Lifecycle](PLATFORM_LIFECYCLE.md)
- [Platform Evolution](PLATFORM_EVOLUTION.md)
