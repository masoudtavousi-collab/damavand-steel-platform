# Context Router

## Purpose

Load the smallest authoritative context required for a task. This router reduces token use; it does not replace governing sources, Current Project State, or domain contracts.

## Authority Rule

- **Current authority** decides what may happen now: accepted governing sources, explicit Founder decisions, Current Project State, and the active Mission Packet within their exact scopes.
- **Historical evidence** explains provenance and prior outcomes. It cannot become current authority because it is newer, detailed, or present in a conversation.
- Resolve the live GitHub `main` ref at task start. A fixed SHA in prose is an evidence anchor, not a permanent live-tip claim.
- If scope/status checks do not resolve a material conflict, stop and return a reconciliation blocker instead of selecting an authority by intuition.

## Layer 0 — Boot Context

Load for every repository task:

1. root [`AGENTS.md`](../AGENTS.md);
2. live GitHub `main` SHA plus local branch and clean/dirty state;
3. [Current Project State](CURRENT_PROJECT_STATE.md);
4. [C000 / Project OS 2.0 Decision Package](C000_OS2_STRATEGIC_RECONCILIATION_DECISION_PACKAGE.md);
5. [Project Baseline](PROJECT_BASELINE.md);
6. [Source of Truth Priority](SOURCE_OF_TRUTH_PRIORITY.md);
7. the active Founder/Project Commander Mission Packet.

Do not load every file referenced by Layer 0. Continue only through the relevant Layer 1 route.

## Layer 1 — Domain Routes

| Task domain | Minimum additional sources |
| --- | --- |
| Program authority / governance | [DS-PC — HOW](DS_PC_001_PROGRAM_CHARTER.md), [DS-SPD — WHAT](DS_SPD_001_STRATEGIC_PROGRAM_DIRECTIVE.md), [Decision Log](10_DECISION_LOG.md), [Founder Decision Log](17_FOUNDER_DECISION_LOG.md), and relevant accepted ADRs |
| Product Data / taxonomy / Product Experience | [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), relevant contracts/schemas/registries under `repository/data/`, [C006 Scope](C006_PRODUCT_DATA_SEMANTIC_PRODUCT_EXPERIENCE_ARCHITECTURE_SCOPE_V1.0.md) and [Product Experience Engine](../repository/enterprise-platform/05_PRODUCT_EXPERIENCE_ENGINE.md) when projection semantics are in scope, plus only the applicable approved PD scope |
| Commerce / inquiry / CRM | [ADR-0001](adr/0001-inquiry-first-commerce.md), [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md), [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md), and the exact Founder commercial decision |
| Knowledge / content / SEO | Knowledge ownership sources plus the exact Product IDs and directly relevant content/SEO model; never use Knowledge to invent Product facts |
| Git / documentation / traceability | [Git Governance](GIT_GOVERNANCE.md), [Codex Sprint Protocol](CODEX_SPRINT_PROTOCOL.md), [Project Execution Roadmap](PROJECT_EXECUTION_ROADMAP.md), [Repository Relationship Map](REPOSITORY_RELATIONSHIP_MAP.md), [Documentation Index](08_DOCUMENTATION_INDEX.md), and directly affected validation rules |
| Runtime / WordPress / WooCommerce | [Execution Gates](EXECUTION_GATES.md), exact target evidence, backup/restore/rollback evidence, and the separately authorized Runtime packet |
| C1-T03 frozen evidence | The C000 disposition first; load protected C1-T03 evidence only for an explicit dependency or evidence-preservation task |

## Layer 2 — Deep or Historical Evidence

Load only to resolve a cited provenance question, conflict, regression, or audit requirement:

- historical audits and superseded snapshots;
- old Mission/Scope packets;
- archived Atlas or recovery material;
- prior implementation evidence;
- raw C1-T03 technical artifacts;
- external research explicitly requested by the active Mission.

Label Layer 2 material as evidence. Do not copy its mutable next-action claims into current documents.

## Do Not Read by Default

- the entire repository or every linked document;
- all 879 candidate combinations or theoretical Cartesian matrices;
- raw conversation exports, credentials, workstation inventories, or quarantined repositories;
- WordPress/hosting/runtime evidence when Runtime is not authorized;
- Central Steel, n8n, OpenAI API, or automation material before its track and gate;
- every C1-T03 revision or finding when the task does not reuse that architecture.

## Task Context Envelope

Before action, record:

```text
authority
live_main_sha
objective
allowed_paths_and_systems
explicit_no_go
dependencies
stop_conditions
validation
return_contract
```

Read more only when one of these fields cannot be resolved from the current layer.

## Context Handoff

Return durable facts to the correct canonical owner:

- operational state → Current Project State;
- approved decisions → decision source and decision logs;
- Product truth → governed Product contracts/registries;
- Knowledge → Knowledge Repository;
- historical evidence → audit/archive reference;
- implementation/runtime evidence → separately authorized environment record.

Do not duplicate mutable branch, PR, live-SHA, next-action, or readiness claims across stable governance documents.

## Navigation

- [C000 / Project OS 2.0 Decision Package](C000_OS2_STRATEGIC_RECONCILIATION_DECISION_PACKAGE.md)
- [Repository Reading Order](READING_ORDER.md)
- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Current Project State](CURRENT_PROJECT_STATE.md)
