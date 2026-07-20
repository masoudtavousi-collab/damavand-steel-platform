# Enterprise Platform Directory Standard

## Document Control

- **Document ID:** `repository/platform/PLATFORM_DIRECTORY_STANDARD.md`
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Enterprise Architect, Repository Guardian, Engine Owners, Build Authority, Security Reviewer, and Operations Reviewer
- **Approval Authority:** Founder
- **Version:** 0.2.0
- **Last Updated:** 2026-07-20
- **Last Review:** 2026-07-20
- **Review Cycle:** On platform layer, directory, ownership, artifact class, naming, retention, or repository-structure change
- **Lifecycle:** Review
- **Source of Truth:** [Platform Manifest](PLATFORM_MANIFEST.md), [Platform Architecture](PLATFORM_ARCHITECTURE.md), Repository Implementation Rules, and explicit Founder approval
- **Dependencies:** [Platform Manifest](PLATFORM_MANIFEST.md), [Platform Architecture](PLATFORM_ARCHITECTURE.md), and [Repository Implementation Rules](../IMPLEMENTATION_RULES.md)
- **Related Documents:** [Engine Boundaries](ENGINE_BOUNDARIES.md), [Platform Governance](PLATFORM_GOVERNANCE.md), [Platform Versioning](PLATFORM_VERSIONING.md), and [Repository Guide](../../docs/07_REPOSITORY_GUIDE.md)
- **Traceability:** PM-001 through PM-010, PP-004 through PP-008, S01A-001 through S01A-010, Sprint 03E, and directory rules PDS-001 through PDS-012
- **AI Compatibility:** AI-readable proposed directory standard; no autonomous folder creation, move, rename, or deletion
- **Approval:** Canonical path-ownership model approved by Founder on 2026-07-20; physical creation and remaining proposed rules require separate authorization

## Purpose

Define the permanent logical/physical location, ownership, artifact class, and boundary for Platform, Repository, Engines, Runtime, WordPress, Knowledge, imports, exports, backups, and validation without restructuring the existing repository.

## Directory Rules

| ID | Proposed rule | Status |
| --- | --- | --- |
| PDS-001 | Preserve the existing repository root and directory names; no implied rename/move occurs through this standard. | Proposed pending Founder approval |
| PDS-002 | Keep Platform constitution sources under `repository/platform/`. | Proposed pending Founder approval |
| PDS-003 | Keep reusable Engine contracts under `repository/engine/<engine-key>/`. | Proposed pending Founder approval |
| PDS-004 | Keep canonical machine contracts, schemas, registries, validators, Master Data, and Golden references under the approved `repository/data/` concern paths. | `APPROVED` by Founder on 2026-07-20; directory creation remains separately gated |
| PDS-005 | Keep derived implementation and runtime adapters separate from Platform/Engine/domain authority. | Ownership boundary `APPROVED` by Founder on 2026-07-20 |
| PDS-006 | Treat WordPress/WooCommerce as downstream adapters under `repository/wordpress/` and controlled runtime boundaries. | Ownership boundary `APPROVED` by Founder on 2026-07-20 |
| PDS-007 | Keep canonical Knowledge Repository assets under `repository/knowledge/`; documentation governance under `docs/` remains separate and must not duplicate business Knowledge authority. | `APPROVED` by Founder on 2026-07-20; directory creation remains separately gated |
| PDS-008 | Keep imports, exports, backups, logs, secrets, and generated data governed by access/retention/ignore rules; presence of a folder does not authorize payloads. | Proposed pending Founder approval |
| PDS-009 | Keep validation contracts/evidence close to their domain while repository-wide quality standards remain under `quality/`. | Proposed pending Founder approval |
| PDS-010 | Every directory has one primary owner and permitted artifact classes. | Proposed pending Founder approval |
| PDS-011 | New directories require demonstrated non-duplication, owner, lifecycle, access, version, navigation, and migration impact. | Proposed pending Founder approval |
| PDS-012 | Runtime-generated state never becomes canonical repository content by synchronization alone. | Proposed pending Founder approval |

## Permanent Physical Structure

```text
repository-root/
├── docs/                              controlled knowledge and governance
├── quality/                           reusable quality standards/checklists
├── prompts/                           controlled collaboration/task prompts
├── scripts/                           reviewed repository automation only
├── public/                            local/runtime-facing WordPress scaffold boundary
└── repository/
    ├── platform/                      Platform Constitution set
    ├── engine/
    │   ├── product/                   current Product Engine
    │   └── <future-engine>/           only after Engine admission approval
    ├── data/
    │   ├── contracts/                 canonical machine-readable contracts
    │   ├── schemas/                   canonical schemas
    │   ├── registries/                controlled vocabularies and identifier registries
    │   ├── validation/                canonical domain validators
    │   ├── master-data/               canonical governed Product Master Data
    │   ├── golden-reference/          canonical Golden reference packages
    │   ├── products/
    │   ├── attributes/
    │   ├── taxonomies/
    │   ├── imports/woocommerce/
    │   ├── seo/
    │   └── templates/                 reserved; not a second Engine-template authority
    ├── knowledge/                     canonical Knowledge Repository assets
    ├── content/                       governed reusable content assets
    ├── implementation-assets/         derived implementation and adapter assets
    ├── wordpress/                     WordPress/WooCommerce adapters only
    ├── config/                        non-secret configuration inventories/templates
    ├── deployment/                    approved deployment definitions/runbooks
    ├── migration/                     approved ordered migration artifacts/plans
    ├── imports/                       reviewed sanitized implementation imports only
    ├── exports/                       generated exports excluded; contracts/manifests only if approved
    ├── backups/                       no backup payload in Git
    ├── validation/                    future cross-platform validation artifacts if approved
    ├── quality/                       sprint/runtime quality evidence if approved
    ├── assets/                        approved implementation assets with rights evidence
    ├── logs/                          no runtime logs in Git
    ├── tools/                         approved tool configuration, no binaries/secrets
    ├── docs_generated/                non-authoritative generated documentation only
    └── templates/                     general implementation templates, not Product Engine authority
```

This tree records approved ownership, not file presence or implementation. As of the verified `d702c5217f7caa2f23e56f965f3f993967e3c17d` baseline, the new canonical contract/schema/registry/Master Data/Golden/Knowledge/content/implementation paths are absent, and `repository/wordpress/` has no substantive adapter artifacts. Creation requires a separate exact-scope Founder authorization.

## Logical-to-Physical Mapping

| Requested logical concern | Canonical physical location/boundary | Notes |
| --- | --- | --- |
| Platform | `repository/platform/` | Constitutional architecture only |
| Repository | Repository root plus `repository/` workspace | Controlled source/evidence boundary |
| Engine | `repository/engine/<engine-key>/` | One approved Engine per subdirectory |
| Runtime | Logical layer; adapters/artifacts under `repository/wordpress/`, future approved runtime paths, and environment-specific external systems | No generic runtime folder is created now |
| Canonical Product contracts | `repository/data/contracts/`, `repository/data/schemas/`, `repository/data/registries/`, and `repository/data/validation/` | Approved ownership; not yet created or implemented |
| Product Master Data | `repository/data/master-data/` | Approved ownership; absent until separately authorized |
| Golden reference packages | `repository/data/golden-reference/` | Approved ownership; absent until separately authorized |
| WordPress | `repository/wordpress/` and controlled `public/` scaffold boundary | Replaceable adapter only; never canonical Product or Knowledge owner |
| Knowledge | `repository/knowledge/` | Canonical business Knowledge Repository; approved future location, currently absent |
| Reusable content | `repository/content/` | Governed reusable content; currently absent |
| Derived implementation assets | `repository/implementation-assets/` | Downstream artifacts only; currently absent |
| Exports | `repository/exports/` | Generated/export payloads stay out of Git; schemas/manifests only when approved |
| Imports | Domain staging under `repository/data/imports/`; implementation imports under `repository/imports/` | Both require explicit contracts/review; no execution implied |
| Backups | `repository/backups/` placeholder plus approved external protected custody | No backup payload in Git |
| Validation | Domain rules under `repository/data/validation/`; reusable standards under `quality/`; future cross-platform evidence under `repository/validation/` if approved | Avoid duplicate governing standards |

## Directory Ownership

| Directory/domain | Authority owner | Operational owner | Permitted content |
| --- | --- | --- | --- |
| `repository/platform/` | Founder/Platform Architecture | Repository Guardian | Proposed/approved Platform constitutional sources |
| `repository/engine/` | Founder + relevant Engine authority | Engine Owner | Versioned Engine contracts/templates/guides |
| `repository/data/` | Product/domain authorities | Product Data Owner | Canonical contracts, schemas, registries, validators, Master Data, Golden references, and approved staging inputs by subpath |
| `repository/knowledge/` | Knowledge authority | Knowledge Owner | Canonical Knowledge contracts, governed instances, relationships, and provenance |
| `repository/content/` | Content authority | Content Owner | Governed reusable content assets that reference canonical facts |
| `repository/implementation-assets/` | Applicable source authority | Build/Adapter Owner | Derived implementation and adapter assets only |
| `docs/` | Applicable governing owner | Documentation Owner | Governance, decisions, audits, guides, and repository navigation; not duplicate business Knowledge authority |
| `quality/` | Quality authority | Quality Owner | Reusable standards/checklists |
| `repository/wordpress/` | Platform/WordPress architecture | Runtime/Build Owner | Approved runtime adapter artifacts only |
| `repository/config/` | Platform/runtime authority | Configuration Owner | Non-secret inventories/templates |
| deployment/migration | Release/Data authority | Operations/Build/Data Owner | Approved plans/artifacts with recovery evidence |
| imports/exports/backups/logs | Data/Operations/Security authority | Authorized operator | Restricted/ignored payloads and approved manifests only |

Actual assignments remain `TBD`; Founder is current Approval Authority.

## Naming and Versioning

- Directory names use stable lowercase ASCII kebab-case unless an accepted vendor/task-defined path requires otherwise.
- Platform filenames use task-defined uppercase ASCII underscore names.
- Engine-specific conventions are declared by the Engine and cannot change general repository naming outside their boundary.
- Persian labels belong in controlled data/content, not machine paths by default.
- Environment, version, migration, and generated status are metadata/manifest concerns, not ad hoc filename suffixes unless the applicable approved standard requires them.
- Paths never contain credentials, personal data, supplier/customer names, transient status, or unapproved business terminology.

## Runtime and Environment Separation

- Development, staging, production, and future environments have separate configuration/secrets/data/deployment evidence.
- Environment secrets never enter Git.
- Runtime databases/uploads/caches/logs/backups are not repository sources.
- Runtime adapter artifacts reference canonical Engine/data contracts by version.
- Direct runtime drift must be detected and reconciled through approved change control.

## Imports, Exports, and Backups

- Import contract, staging data, execution payload, result, and error report are distinct artifacts with different retention/access.
- Generated exports are evidence/transfer artifacts, not automatic source authority.
- Backups require protected external custody, encryption/access/retention/integrity/restore evidence.
- No secrets, personal/customer/inquiry data, price, supplier, or unapproved commercial data enters repository examples.

## Prohibited Repository Content

- WordPress Core/vendor packages, uploads, cache, runtime logs, production databases, binary backups.
- Credentials, API keys, certificates/private keys, tokens, personal/customer/inquiry payloads.
- Unreviewed imports/exports, generated commercial data, public-price data, stock/supplier claims.
- Duplicate Engine/template/knowledge authority.
- Files created solely to preserve an empty folder unless governed `.gitkeep` is already approved.

## Change Gate

Directory creation/move/rename/removal requires scope, owner, purpose, overlap search, affected links/tools/deployments, compatibility, migration, rollback, security/access, ignore policy, index/graph/health updates, and Founder approval. Destructive restructuring is outside Sprint 03E.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.2.0 | 2026-07-20 | Recorded Founder-approved canonical ownership for Product contracts, schemas, registries, validation, Master Data, Golden references, Knowledge, content, implementation assets, and WordPress adapters; no directory created. |
| 0.1.0 | 2026-07-04 | Initial Sprint 03E proposed permanent Platform Directory Standard; no restructuring. |

## Navigation

- [Platform Manifest](PLATFORM_MANIFEST.md)
- [Platform Architecture](PLATFORM_ARCHITECTURE.md)
- [Engine Boundaries](ENGINE_BOUNDARIES.md)
- [Platform Versioning](PLATFORM_VERSIONING.md)
