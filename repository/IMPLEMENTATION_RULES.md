# Repository Implementation Rules

## Document Control

- **Document ID:** `repository/IMPLEMENTATION_RULES.md`
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Build Engineer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On repository structure, folder ownership, naming, versioning, migration, backup, build, quality, or rollback change
- **Lifecycle:** Review
- **Source of Truth:** [Repository Baseline v1.0](../docs/BASELINE_v1.0.md), accepted Core Project Principles, accepted ADR-0001, and future approved implementation decisions
- **Dependencies:** [Engineering Guidelines](../docs/ENGINEERING_GUIDELINES.md), [Implementation Readiness](../docs/IMPLEMENTATION_READINESS.md), and [WordPress Solution Blueprint](../docs/35_WORDPRESS_BLUEPRINT.md)
- **Related Documents:** [Build Checklist](BUILD_CHECKLIST.md), [Pre-Implementation Checklist](PRE_IMPLEMENTATION_CHECKLIST.md), [Sprint Roadmap](../docs/SPRINT_ROADMAP.md), and [Sprint 01A Audit](../docs/AUDIT_REPORT_SPRINT01A.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, WP-FC-001 through WP-FC-005, FRZ-001 through FRZ-006, and S01A-001 through S01A-010
- **AI Compatibility:** AI-readable repository-engineering rules; no AI product feature or autonomous approval authority
- **Approval:** Pending Founder review; no build, installation, configuration, or implementation is authorized

## Purpose

Define how the implementation workspace is organized and governed before any WordPress installation or production code exists.

## Scope and Boundary

These rules govern only the `repository/` engineering workspace. They do not modify the approved v1.0 baseline, business rules, architecture, product structure, taxonomy, plugin decisions, or WordPress behavior.

The workspace is empty by design except for controlled Markdown documents, `.gitkeep` placeholders, and its repository-only `.gitignore`. No folder name implies approval to create its future contents.

## Repository Bootstrap Decisions

| ID | Proposed rule | Status |
| --- | --- | --- |
| S01A-001 | Keep future implementation artifacts under the isolated `repository/` workspace and preserve existing top-level architecture. | Proposed pending Founder approval |
| S01A-002 | Give every workspace folder one documented owner and permitted artifact class before use. | Proposed pending Founder approval |
| S01A-003 | Exclude secrets, runtime logs, binary backups, generated exports, generated documentation, and unreviewed imports from version control. | Required by baseline/security boundaries |
| S01A-004 | Use stable lowercase ASCII names with hyphens for files and directories unless a vendor or approved standard requires another form. | Proposed pending Founder approval |
| S01A-005 | Keep repository, document, migration, configuration, dependency, and release versions distinct and traceable. | Derived from Git Governance; broad policy pending Founder approval |
| S01A-006 | Require reversible, ordered, validated, and evidence-backed migrations with no direct production mutation. | Proposed pending Founder/technical approval |
| S01A-007 | Keep backup data outside Git and require restore evidence before a risky future change. | Required by repository and security boundaries |
| S01A-008 | Block a build when authority, prerequisites, quality gates, rollback, or environment evidence is incomplete. | Required by Implementation Readiness |
| S01A-009 | Do not install WordPress/plugins/themes or generate production code/configuration until a separate exact implementation task is approved. | Required by current Sprint 01A scope |
| S01A-010 | Preserve the immutable v1.0 tags and recover through new reviewed commits rather than rewriting baseline history. | Required by FRZ decisions and baseline integrity |

## Folder Ownership

| Folder | Intended owner | Permitted future contents after approval | Current Sprint 01A state |
| --- | --- | --- | --- |
| `wordpress/` | WordPress Platform Owner | Approved WordPress integration artifacts excluding Core, uploads, vendor packages, and secrets | Empty placeholder |
| `config/` | Configuration Owner | Non-secret, environment-aware configuration sources/templates | Empty placeholder |
| `deployment/` | Release/Operations Owner | Approved deployment definitions and runbooks | Empty placeholder |
| `scripts/` | Build/Operations Owner | Reviewed, safe, idempotent automation | Empty placeholder |
| `quality/` | Quality Owner | Sprint-specific gates and retained validation evidence | Empty placeholder |
| `backups/` | Operations/Security Owner | No backup payloads in Git; placeholder or approved non-sensitive manifest references only | Ignored except `.gitkeep` |
| `migration/` | Data/Platform Owner | Ordered migration plans and future approved migration artifacts | Empty placeholder |
| `assets/` | Content/Design Owner | Approved implementation assets with rights, source, and optimization evidence | Empty placeholder |
| `imports/` | Data Owner | Explicitly reviewed import definitions or sanitized inputs only | Ignored except `.gitkeep` |
| `exports/` | Data/Operations Owner | No generated exports in Git; approved schema descriptions belong in controlled documentation | Ignored except `.gitkeep` |
| `logs/` | Operations/Security Owner | No runtime logs in Git | Ignored except `.gitkeep` |
| `tools/` | Build/Technical Owner | Approved repository-local tool configuration without binaries, dependencies, or credentials | Empty placeholder |
| `docs_generated/` | Documentation Owner | Generated non-authoritative output only | Ignored except `.gitkeep` |
| `templates/` | Applicable Domain Owner | Approved reusable implementation templates that do not duplicate canonical data | Empty placeholder |

Owner titles are responsibility placeholders until the Founder assigns people or delegated roles. Configuration ownership does not grant business or architecture approval authority.

## Repository Engineering Rules

- Start every future change from the immutable v1.0 baseline or an approved successor.
- Read the applicable authority, readiness blockers, Blueprint, decision registers, and open questions before proposing artifacts.
- Change only the authorized folders and preserve unrelated user work.
- Keep canonical source data separate from generated output, runtime state, credentials, and backups.
- Do not commit WordPress Core, uploads, cache, dependencies, commercial archives, environment secrets, customer/Inquiry data, or production logs.
- Use supported vendor interfaces and configuration after approval; never modify WordPress Core or vendor files.
- Preserve Plugin First, Configuration First, Mobile First, Persian RTL, Inquiry First, No Public Pricing, No Custom Theme, No Gravity Forms, No LiteSpeed Cache, and No AI Features in Phase 1.
- Record every material artifact's owner, source, version, dependencies, review, tests, rollback, and retirement path.

## Naming Rules

- Directories and implementation files use lowercase ASCII kebab-case by default: `purpose-variant.ext`.
- Stable machine identifiers use approved lowercase ASCII keys; public Persian labels remain separate controlled data.
- Do not encode secrets, personal names, environment credentials, temporary dates, or unapproved business terms in names.
- Migration artifacts, if approved later, use an ordered immutable identifier plus concise purpose; exact format requires approval before the first migration.
- Environment-specific variants use explicit approved environment names and contain no secret values.
- Generated files identify their source and generator but never become governing authority merely by generation.

The requested `docs_generated/` folder name is retained exactly as a task-defined repository path; it is the only current underscore exception and does not establish a general naming pattern.

## Versioning Rules

- Repository baseline remains `1.0.0` until an approved successor is created.
- Document versions remain independent from repository, dependency, migration, configuration, and product-release versions.
- Future dependencies use exact approved versions or lock evidence; no version is selected in Sprint 01A.
- A version change must record compatibility, affected consumers, migration, tests, rollback, and approval.
- Draft rules and templates use `0.y.z` metadata without implying approval.
- Broad versioning semantics remain subject to Founder decisions in Git Governance.

## Migration Rules

- No migration is authorized or created in Sprint 01A.
- A future migration requires source/target authority, ordered identity, scope, owner, preconditions, dry run, validation, backup/restore, rollback or forward-recovery plan, audit evidence, and approval.
- Never run direct production database changes, uncontrolled search/replace, or destructive imports.
- Preserve stable entity IDs, relationships, Persian content, RTL meaning, units, consent, access classes, and lifecycle states.
- Migrations must be repeatable or explicitly one-time with detection that prevents accidental replay.
- Failed or partial migration behavior must be defined before execution.

## Backup Rules

- Git is not a backup store for databases, uploads, secrets, runtime configuration, customer data, or binary archives.
- The `backups/` folder contains no backup payload and is ignored except for its placeholder.
- Future backups require approved scope, encryption, custody, retention, access, integrity verification, restore test, deletion, and incident procedures.
- Backup evidence references protected external artifacts without exposing sensitive paths, credentials, or contents.
- A risky future change is blocked until the applicable backup and restoration path is verified.

## Quality Gates

| Gate | Minimum pass condition before future build activity |
| --- | --- |
| Authority | Exact task, approved sources, owner, reviewer, and approval are recorded |
| Readiness | Applicable blockers in Implementation Readiness are closed |
| Structure | Artifact is in the owned folder and does not duplicate an existing repository concern |
| Naming/version | Stable name and version semantics are approved and traceable |
| Security/privacy | No secrets, personal data, unsafe dependency, or protected-data exposure |
| Architecture/business | CP-001 through CP-010, ADR-0001, and approved Blueprint boundaries are preserved |
| Documentation | Metadata, references, index/navigation, decisions, and rollback guidance are current |
| Validation | Required static, functional, accessibility, RTL/mobile, security, performance, and regression evidence exists |
| Recovery | Backup/restore and rollback or forward-recovery are verified where applicable |
| Approval | Blocking findings are resolved and the authorized approver records the decision |

Any mandatory failure blocks build, migration, installation, merge, deployment, or release.

## Build Policy

- Sprint 01A permits no build, dependency download, package installation, WordPress installation, plugin/theme installation, production configuration, compilation, bundling, database creation, or runtime start.
- A future build must be deterministic, isolated from secrets, pinned to approved inputs, observable, and reproducible from controlled sources.
- Build outputs are generated artifacts, not source authority, and must not be committed unless an approved policy explicitly requires it.
- Build scripts require review for safety, idempotency, failure handling, portability, and cleanup.
- A successful build does not approve deployment or production promotion.

## Rollback Policy

- Never alter `baseline-v1.0.0` or `repo-v1.0.0` to reverse a later change.
- Repository rollback uses a new reviewed revert/recovery commit from an approved reference.
- Future configuration/data/deployment rollback must define trigger, owner, recovery point, protected data handling, verification, and maximum acceptable impact.
- If rollback is unsafe or unavailable, define and approve a forward-recovery plan before execution.
- Stop and isolate the change when integrity or recovery evidence is uncertain.

## Approval Status

Review. The folder skeleton and controlled engineering documents are ready for Founder review. No future folder use, build, installation, migration, backup operation, configuration, or implementation is approved.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 01A repository implementation rules and folder ownership model. |

## Navigation

- [Build Checklist](BUILD_CHECKLIST.md)
- [Pre-Implementation Checklist](PRE_IMPLEMENTATION_CHECKLIST.md)
- [Implementation Readiness](../docs/IMPLEMENTATION_READINESS.md)
- [Sprint 01A Audit](../docs/AUDIT_REPORT_SPRINT01A.md)
