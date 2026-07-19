# Repository Relationship Map

## Document Control

- **Document ID:** `docs/REPOSITORY_RELATIONSHIP_MAP.md`
- **Status:** Review
- **Authority:** Repository Disposition Record
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.2.0
- **Last Updated:** 2026-07-19
- **Last Review:** 2026-07-19
- **Review Cycle:** On repository creation, disposition, authority, ownership, namespace, lifecycle, merge, or promotion proposal
- **Lifecycle:** Review
- **Source of Truth:** Explicit Founder decisions in the GIT-02S directive dated 2026-07-14, the Class B Wave 1 authorization dated 2026-07-19, and Repository A governance
- **Dependencies:** [Project Baseline](PROJECT_BASELINE.md), [Source of Truth Priority](SOURCE_OF_TRUTH_PRIORITY.md), and [Project Constitution](01_PROJECT_CONSTITUTION.md)
- **Related Documents:** [Git Governance](GIT_GOVERNANCE.md), [AI Collaboration Standard](AI_COLLABORATION.md), and GIT-02S Audit (`docs/AUDIT_REPORT_GIT02S.md`, not yet part of the bootstrap baseline)
- **Traceability:** GIT-02S Founder decisions 1–3 and 10; CP-001, CP-002, CP-010
- **AI Compatibility:** Explicit cross-repository authority and isolation contract
- **Approval:** Repository dispositions accepted by explicit Founder directive; document presentation pending Founder review

## Purpose

Define the authority, isolation, adoption, and future-promotion boundaries between the canonical Damavand Steel repository and the secondary research repository. This map authorizes no copy, move, merge, Git initialization, implementation, runtime action, or status promotion.

## Repository A — Canonical Project

| Property | Definition |
| --- | --- |
| Canonical name | Damavand Steel Enterprise Product and Knowledge Platform Repository |
| Path | `/Users/masoudtavousi/Desktop/damavand steel` |
| Purpose | Govern project architecture, decisions, Product and Knowledge Repositories, Master Data, implementation assets, evidence, and future controlled projections |
| Authority | Only canonical and authoritative Damavand Steel project repository |
| Owner / approval authority | Founder |
| Consumers | DamavandSteel.com; future approved CentralSteel.ir and other explicitly approved systems |
| Outputs | Approved governance, product/knowledge truth, controlled assets, evidence, and separately authorized runtime projections |
| Source-of-truth scope | Scope-bound sources ordered by [Source of Truth Priority](SOURCE_OF_TRUTH_PRIORITY.md) |
| Git status | Remote `main` verified at `96f2ea70f9010fce416a18310e98915e2be537b9`; bootstrap commit `b20e95de8b1b67d2bc610130648700e82a6855b3` remains in open, Draft, unmerged PR #1; Wave 1 is limited to its separately approved 19-path branch and Draft PR |
| Allowed future operations | Read-only review; approved documentation work; later explicitly scoped Git, backup, import, or runtime operations after applicable gates |
| Prohibited authority inversions | WordPress, external tools, Repository B, generated outputs, audits, AI, or runtime observations cannot silently override approved Repository A truth |

## Repository B — Isolated Research

| Property | Definition |
| --- | --- |
| Path | `/Users/masoudtavousi/Desktop/damavand-enterprise-repository` |
| Provisional classification | `QUARANTINED_ARCHITECTURE_RESEARCH` |
| Approval state | Unapproved |
| Version state | Unversioned; no Git repository was observed during GIT-02S pre-verification |
| Authority | None for Damavand Steel |
| Purpose | Isolated research concepts pending explicit Founder disposition |
| Known contents | Ten acronym domain placeholders, a Factory architecture concept, and a legacy Generator concept with empty implementation folders |
| Undefined acronyms | EDA, EDAI, EDE, EDG, EDM, EDR, EDSYS, and EDX; meanings must not be inferred |
| Explicit examples | EDP is shown as Enterprise Data Platform and EDS as Enterprise Data Standards in Factory examples only |
| Factory concept | Proposed canonical data model, registries, validation, deterministic generation, outputs, and AI knowledge indexing; no implementation or approval evidence |
| Generator concept | Legacy Markdown/AST generation proposal described by its README as superseded by Factory; no implementation evidence |

Repository B has:

- no current project authority;
- no merge authority;
- no runtime or implementation authority;
- no ability to override the Founder;
- no source-of-truth authority for Damavand Steel;
- no authorization for Phase 1 AI features;
- no permission in GIT-02S to be copied, moved, renamed, deleted, initialized as Git, or modified.

## Cross-Repository Authority Matrix

| Subject | Repository A | Repository B | Controlling rule |
| --- | --- | --- | --- |
| Damavand project governance | Canonical when approved within scope | None | Founder-controlled Repository A governance |
| Product and Master Data | Canonical approved records | None | Master Data Governance and source priority |
| Knowledge authority | Approved Repository A knowledge | Research concepts only | Approved knowledge cannot be replaced by conceptual tooling |
| Document IDs and namespaces | Existing Repository A identities and governance | Proposed, unapproved ID patterns | No collision or replacement without Founder-approved mapping |
| Lifecycle | Repository A controlled vocabulary | Narrower proposed Factory vocabulary | Repository A controls; no silent translation |
| Git and baselines | Existing local history and governed future review | None | No cross-repository baseline claim |
| Runtime/import/publishing | Separately gated and currently `NO-GO` | None | Execution Gates and explicit Founder approval |
| AI | Repository collaboration only; Phase 1 feature prohibition preserved | Proposed AI Knowledge Engine has no authority | CP-010 and AI-boundary policy |
| Approval | Founder is final authority | “Enterprise Architect” wording has no Damavand authority | No Founder override or delegation by research text |

## Merge and Isolation Policy

1. Keep both repositories physically and logically separate.
2. Do not copy files or directories between them without an explicit, path-level Founder-approved task.
3. Do not merge histories, initialize Repository B as Git, add remotes, create submodules, or create symbolic links under this disposition.
4. Repository B filenames, recency, terminology, or apparent completeness never confer authority.
5. A future review may evaluate concepts, but adoption must occur through approved Repository A decisions and controlled native documents, not wholesale copying.

## Concept Adoption Policy

A Repository B concept may be considered only when:

- the exact problem and Repository A owner are identified;
- applicable Founder, architecture, security, product, documentation, and AI reviews are complete;
- the concept is checked against CP-001 through CP-010 and existing Repository A architecture;
- source, provenance, licensing, migration, rollback, testing, maintenance, and retirement are defined;
- generated output remains derivative and cannot self-approve;
- a separate Founder decision authorizes adoption and exact implementation scope.

Conceptual similarity is not a merge instruction.

## Namespace Collision Policy

- Repository A document IDs, entity IDs, Master Data IDs, decision IDs, slugs, and filenames retain priority within Damavand Steel.
- Repository B patterns such as Factory/Generator document IDs cannot be imported directly.
- A future proposal must inventory collisions and define explicit mapping, ownership, aliases, migration, and rollback.
- No acronym may be expanded or assigned a domain from inference.

## Lifecycle Collision Policy

- Repository A lifecycle and decision vocabularies control Damavand work.
- Repository B's proposed `draft/review/approved/deprecated/archived` model cannot replace or narrow Repository A states.
- Generator's stated supersession by Factory remains Repository B research context, not an approved Damavand lifecycle transition.
- Any promoted concept must receive a new Repository A lifecycle record and preserve its research provenance.

## AI-Boundary Policy

- CP-010 prohibits AI features in Phase 1.
- Internal repository analysis or retrieval assistance does not authorize a customer-facing, runtime, autonomous, or publishing AI capability.
- Repository B's AI Knowledge Engine proposal is unapproved and must not be implemented, connected to production data, or treated as an exception.
- AI cannot approve data, decisions, generated documents, merges, or lifecycle transitions.

## Future Promotion Gates

Repository B or any concept within it can change status only after:

1. Founder identifies its owner, purpose, and relationship to Damavand Steel.
2. Undefined acronyms and scope are documented from authoritative evidence.
3. Factory versus Generator disposition is decided.
4. Governance, lifecycle, source-of-truth, namespace, licensing, security, AI, testing, backup, and rollback models are approved.
5. Conflicts with Repository A are mapped and resolved.
6. A versioned, reviewable proposal is prepared without altering Repository A authority.
7. Founder records the exact promotion, adoption, or retirement decision.

No passage of time, new file, Git initialization, architecture review, or AI recommendation changes the current disposition.

## Current Decision

- Repository A canonical authority: **CONFIRMED**.
- Repository B classification: **`QUARANTINED_ARCHITECTURE_RESEARCH`**.
- Class B Wave 1 exact 19-path Git/documentation integration: **GO under the 2026-07-19 Founder authorization**.
- PR #1 modification, merge, and Class B Waves 2–10: **NO-GO**.
- Repository B merge, implementation, runtime, Git initialization, or authority: **NO-GO**.
- Concept review in a separately approved future sprint: **CONDITIONAL GO**.
- Any status change: **FOUNDER DECISION REQUIRED**.

## References

- [Project Baseline](PROJECT_BASELINE.md)
- [Project Constitution](01_PROJECT_CONSTITUTION.md)
- [Source of Truth Priority](SOURCE_OF_TRUTH_PRIORITY.md)
- [AI Collaboration Standard](AI_COLLABORATION.md)
- [Git Governance](GIT_GOVERNANCE.md)

## Navigation

- [Repository Reading Order](READING_ORDER.md)
- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- GIT-02S Audit — `docs/AUDIT_REPORT_GIT02S.md` (not yet part of the bootstrap baseline)
