# Git Governance

## Document Control

- **Document ID:** `docs/GIT_GOVERNANCE.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On repository, branch, version, baseline, tag, commit, release, backup, or approval-policy change
- **Lifecycle:** Review
- **Source of Truth:** [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles) and future recorded Founder approval; supporting governance dependencies remain Draft or Review until approved
- **Dependencies:** [Project Constitution](01_PROJECT_CONSTITUTION.md), [Repository Standards](07_REPOSITORY_GUIDE.md), [Document Lifecycle](12_DOCUMENT_LIFECYCLE.md), and [Review Process](15_REVIEW_PROCESS.md)
- **Related Documents:** [Changelog Policy](14_CHANGELOG_POLICY.md), [Decision Log](10_DECISION_LOG.md), [Repository Metadata Standard](REPOSITORY_METADATA.md), [Repository Health](REPOSITORY_HEALTH.md), and [Batch 03 Audit](AUDIT_REPORT_BATCH03.md)
- **Traceability:** FD-GOV-002, FD-GOV-003, FD-GOV-007, FD-GOV-019, and Git validation evidence in the Batch 03 audit
- **AI Compatibility:** AI-readable with gaps until Founder approval and baseline creation
- **Approval:** Pending Founder approval

## Purpose

Define how the Damavand Steel Enterprise Repository evolves through Git without authorizing WordPress, WooCommerce, plugin, theme, infrastructure, CI/CD, deployment, feature, or business-logic implementation.

## Repository Strategy

### Purpose and Scope

The repository preserves approved project knowledge, governance, decisions, configuration templates, future authorized implementation, and evidence as one traceable version-controlled system.

Repository scope includes controlled documentation, ADRs, approved configuration templates, quality standards, prompts, assets, scripts, tests, and future explicitly authorized project artifacts. Scope inclusion does not approve the content of a Draft file or authorize implementation.

### Ownership

- Repository Owner and current Approval Authority: Founder.
- Repository Guardian: governance and consistency reviewer.
- Domain reviewers: review only within recorded responsibility.
- `CODEOWNERS` routes review requests; it does not grant approval authority or prove that listed teams are assigned and active.
- Delegation requires an approved Founder decision and corresponding metadata and protection-rule update.

### Boundaries

The repository must exclude secrets, credentials, personal or customer data, runtime logs, generated caches, WordPress core, uploads, installed dependencies, licensed commercial archives, and any other material excluded by `.gitignore`, security policy, licensing, or an approved governing rule.

No branch, commit, tag, baseline, or release may weaken CP-001 through CP-010 or convert unresolved Draft content into approved authority.

### Lifetime and History Preservation

The repository is a long-lived project record. Approved commits, annotated tags, accepted ADRs, baseline manifests, and release evidence are retained for the project lifetime and applicable retention period. History is extended through new commits and explicit supersession; it is not rewritten to conceal prior approved state.

Force-push, tag movement, destructive rebasing of shared branches, and deletion of approved evidence are prohibited.

## Source of Truth Policy

- The approved commit referenced by an immutable approved tag is the source for a baseline or release.
- `main` represents the latest integrated approved repository state only after the first approved baseline exists.
- Until that baseline exists, the working tree and unborn `main` are unapproved repository inputs, not an approved source of truth.
- Local working copies, branches, forks, mirrors, task outputs, audits, and conversations are not governing authority.
- A mirror proves recoverability only when its commit and tag identifiers match the approved primary record.
- A newer timestamp, branch, file, or commit does not override approval and authority precedence.

## Branch Strategy

### Branch Definitions

| Branch | Lifetime and source | Permitted purpose | Merge target | Approval | Deletion policy |
| --- | --- | --- | --- | --- | --- |
| `main` | Permanent; begins with the first approved baseline commit | Integrated approved repository state | None | Founder approval required for every merge | Never delete |
| `develop` | Permanent; created from approved `main` after the first baseline | Integration of reviewed work for a future release | `release/*` | Founder approval until delegation is approved | Never delete |
| `release/*` | Short-lived from `develop` | Release stabilization, documentation, validation, and approved corrections | `main`, then back to `develop` | Founder plus applicable domain review | Delete after approved tag and verified back-merge |
| `hotfix/*` | Short-lived from `main` | Urgent correction to current approved state | `main`, then `develop` | Founder plus applicable domain review | Delete after approved tag and verified back-merge |
| `feature/*` | Short-lived from `develop` | Future explicitly authorized feature work | `develop` | Founder plus applicable domain review | Delete after accepted merge |
| `docs/*` | Short-lived from `develop` | Documentation-only changes | `develop` | Founder plus documentation review | Delete after accepted merge |
| `architecture/*` | Short-lived from `develop` | Architecture proposals and accepted architecture updates | `develop` | Architecture review and Founder approval | Delete after accepted merge and decision traceability |
| `research/*` | Time-bound from `develop` | Research evidence and recommendations; no implementation authority | `develop` for approved evidence only | Founder plus applicable reviewer | Delete after evidence retention is verified |
| `experiment/*` | Isolated and time-bound | Disposable experiments with no authority or release status | No direct merge; approved results move to a correctly classified branch | Explicit Founder authorization before extraction | Delete when conclusion and retained evidence are recorded |

### Naming Conventions

- Use lowercase kebab-case after the required prefix.
- General form: `<type>/<decision-or-task-id>-<short-description>`.
- `release/*` form: `release/<repository-version>`.
- `hotfix/*` form: `hotfix/<issue-id>-<short-description>`.
- Examples: `docs/fd-gov-019-git-governance`, `architecture/adr-0002-example-scope`, `release/1.0.0`.
- Examples are format illustrations and do not assert current branches, decisions, or releases.

### Allowed Merge Paths

```text
feature/* ---------> develop
docs/* ------------> develop
architecture/* ----> develop
research/* --------> develop (approved evidence only)
develop -----------> release/*
release/* ---------> main and develop
hotfix/* ----------> main and develop
experiment/* ------> no direct merge
```

### Forbidden Merges and History Actions

- Direct commits or unreviewed merges to `main`, `develop`, or `release/*`.
- Direct merge from `feature/*`, `docs/*`, `architecture/*`, `research/*`, or `experiment/*` to `main`.
- Direct merge from `experiment/*` to any protected branch.
- Merge while required review, validation, decision, or approval is missing.
- Merge that combines unrelated change scopes or hides an unresolved conflict.
- Force-push or destructive rebase of a protected or shared branch.
- Merge of secrets, licensed archives, generated runtime data, or excluded dependencies.

### Merge Policy

- Every governed merge uses a review record or pull request linked to scope, decisions, validation, and Approval Authority.
- Conflicts are resolved under the Project Constitution; a merge must not silently choose an authority interpretation.
- Release and hotfix integration into protected branches preserves an explicit merge record.
- Squash merge may be used for a short-lived branch only when the resulting commit retains all required decision, review, and validation references.
- Rebase is limited to an author's unshared short-lived branch before final review.
- Required back-merges are verified before branch deletion.

## Versioning Strategy

Version classes are independent. A shared number does not imply shared approval, compatibility, or release status.

| Version class | Format | Meaning | Increment rules |
| --- | --- | --- | --- |
| Repository version | `X.Y.Z` | Approved integrated repository governance and artifact state | Major: incompatible governance or structure; Minor: compatible approved capability; Patch: compatible correction |
| Documentation version | `X.Y.Z` in document metadata | Version of one controlled document | Major: authority or structure change; Minor: substantive compatible content; Patch: non-semantic correction |
| Architecture version | `X.Y.Z` for the approved architecture set | Compatibility of approved architecture decisions and constraints | Major: incompatible architecture; Minor: compatible extension; Patch: clarification without decision change |
| Release version | `X.Y.Z` | Approved deliverable release; no release currently exists | Major, Minor, Patch according to approved compatibility impact |
| ADR version | `ADR-NNNN/rN` | Revision of one ADR record | Decision change requires a new ADR or explicit supersession; revision only preserves the same decision |
| Baseline version | `X.Y.Z` | Immutable approved repository snapshot | Increment according to repository compatibility since the prior approved baseline |

Draft documents may use `0.y.z` without implying approval. An Approved document records the approved version and approval reference. Version numbers never replace lifecycle, decision status, or compatibility evidence.

### Compatibility Rules

- A compatible child must preserve all applicable parent rules and accepted decisions.
- Repository, documentation, and architecture compatibility are evaluated separately.
- A release may reference a repository baseline but does not inherit approval merely from matching numbers.
- Major-version changes require migration and impact evidence.
- Minor versions must remain compatible with the current major authority set.
- Patch versions must not introduce new decisions, requirements, or incompatible behavior.
- ADR revisions must not alter the accepted decision; changed decisions require a new or superseding ADR.

## Tag Policy

| Tag class | Format | Example |
| --- | --- | --- |
| Repository | `repo-vX.Y.Z` | `repo-v1.0.0` |
| Baseline | `baseline-vX.Y.Z` | `baseline-v1.0.0` |
| Architecture | `arch-vX.Y.Z` | `arch-v1.0.0` |
| Release | `release-vX.Y.Z` | `release-v1.0.0` |
| Document | `doc-<id>-vX.Y.Z` | `doc-git-governance-v1.0.0` |
| ADR revision | `adr-NNNN-rN` | `adr-0001-r1` |

Examples are illustrative; they do not assert that any current tag or version exists.

- Approved tags are annotated and identify version class, commit, approver, approval reference, validation record, and date.
- Tag creation requires Founder approval. Signing is required after key custody and signing policy are approved.
- Approved tags are immutable. Never move, reuse, or delete them to correct a mistake; create a corrected successor tag and preserve the prior record.
- Lightweight tags are not valid baseline or release evidence.
- Tag and document metadata must agree on version and lifecycle.

## Baseline Strategy

### Baseline Definition

A baseline is an immutable Founder-approved commit plus annotated baseline tag and manifest. The manifest identifies repository version, baseline version, commit ID, included approved documents and decisions, excluded Draft content, validation evidence, known gaps, approver, and date.

### Baseline Approval and Creation

1. Define baseline scope and candidate commit.
2. Verify repository boundaries, secrets exclusions, metadata, decisions, links, dependencies, and quality gates.
3. Record unresolved content and confirm it is excluded from approved authority.
4. Obtain Repository Guardian and required domain reviews.
5. Obtain explicit Founder approval for the exact commit, manifest, and baseline version.
6. Create the annotated immutable baseline tag on that commit.
7. Verify tag, commit, manifest, primary remote, and independent mirror identifiers.

No current working tree, uncommitted change, branch name, or audit recommendation constitutes a baseline.

### Baseline Evolution

- Every future baseline uses a new version, commit, manifest, review, approval, and tag.
- A baseline never absorbs later changes retroactively.
- Compatibility with the prior baseline is recorded before approval.
- Superseded baselines remain retrievable and immutable.

### Rollback and Recovery

- Rollback creates a new reviewed revert or recovery commit from an approved tag; it does not move the tag or rewrite `main`.
- Recovery verifies commit and tag identifiers against the approved manifest and at least one independent mirror or backup.
- Emergency recovery does not bypass post-recovery review, traceability, or Founder confirmation.
- If integrity cannot be proven, repository state is Blocked and must not be promoted.

## Commit Governance

### Commit Format

Use `<type>(<optional-scope>): <imperative summary>` with a concise body when decisions, risks, compatibility, or validation require explanation.

Every governed commit identifies applicable task or decision references, affected CP rules, validation evidence, and breaking or migration impact when relevant. Commits remain atomic and must not mix unrelated authority domains.

| Type | Intended use | Illustrative example |
| --- | --- | --- |
| `docs:` | Documentation content without changing architecture authority | `docs(index): add approved navigation reference` |
| `arch:` | Architecture proposal or approved architecture record | `arch(adr): record accepted decision reference` |
| `seo:` | SEO documentation or future authorized SEO scope | `seo(strategy): clarify approved review evidence` |
| `ux:` | UX documentation or future authorized UX scope | `ux(principles): document approved accessibility constraint` |
| `repo:` | Repository structure or Git-governance change | `repo(git): define protected branch policy` |
| `fix:` | Correction that does not introduce a new decision | `fix(links): correct broken documentation anchor` |
| `refactor:` | Structure-only change with unchanged behavior and authority | `refactor(docs): consolidate duplicate navigation references` |
| `research:` | Evidence, experiment conclusion, or recommendation | `research(cache): record comparison evidence` |
| `decision:` | Accepted decision record or decision-status update | `decision(adr-0001): record Founder acceptance` |
| `governance:` | Governance model, lifecycle, authority, or policy change | `governance(git): establish baseline approval rules` |

Examples demonstrate syntax only and are not current commits or approvals.

### Commit Rules

- Use imperative, specific, non-promotional summaries.
- Never claim approval, release, baseline, compatibility, or validation without evidence.
- Do not amend or replace an approved shared commit to alter history.
- Correct an approved record through a new traceable commit.
- Secret scanning and repository-boundary validation must pass before approval.
- AI-generated commit text remains a proposal and must be verified by a human reviewer.

## Release Governance

Release status is separate from document lifecycle and decision status.

| Release state | Meaning | Entry authority | Allowed transition |
| --- | --- | --- | --- |
| Draft Release | Candidate scope assembled; no approval or release claim | Repository Owner | Review Release or Cancelled under the lifecycle record |
| Review Release | Candidate is frozen for required validation and review | Repository Guardian recommends; Founder controls progression | Draft Release or Approved Release |
| Approved Release | Exact commit, version, evidence, and release scope approved | Founder | Production Release, Deprecated Release, or Superseded Release |
| Production Release | Approved release explicitly promoted to production | Founder after operational approval | Historical, Deprecated, or Superseded Release |
| Historical Release | Retained evidence with no current delivery authority | Founder or approved retention authority | Terminal |
| Deprecated Release | Release remains retrievable but is not preferred and has transition guidance | Founder | Historical or Superseded Release |
| Superseded Release | A named approved successor replaces the release | Founder | Historical Release |

- No release exists until an exact commit and annotated release tag are approved.
- Release approval does not automatically authorize production promotion.
- Production rollback follows the approved baseline and recovery policy and preserves history.
- Release notes and Changelog link to decisions and compatibility evidence but do not replace Git history.

## Repository Backup Policy

### Backup Frequency

- Synchronize the approved primary remote and independent mirror after every approved protected-branch push and approved tag.
- Verify mirror synchronization at least daily while the repository is active.
- Create an encrypted repository bundle at least weekly and immediately before and after an approved baseline or release.
- Perform a documented restore and integrity check at least monthly and after backup-system changes.

These frequencies are proposed governance until Founder approval; no backup automation or infrastructure is implemented by this document.

### Mirrors and Custody

- Maintain one approved primary remote and at least one independent mirror under separate administrative or provider failure boundaries.
- Store encrypted repository bundles outside the primary and mirror failure domains.
- The Founder approves providers, locations, custodians, access, encryption, retention, and recovery roles before use.
- TODO (Founder Decision Required): identify approved primary remote, independent mirror, backup location, and custodians.

### Disaster Recovery and Historical Preservation

1. Declare the repository state Blocked when integrity or availability is uncertain.
2. Select the latest approved baseline or release manifest within the recovery objective.
3. Restore into an isolated location from the primary, mirror, or encrypted bundle.
4. Verify commit graph, annotated tags, manifest identifiers, protected-branch tips, and required files.
5. Obtain Repository Guardian review and Founder authorization before replacing an active remote.
6. Record the incident, recovery source, validation, data gap, and resulting repository state.

Approved history and tags are retained across primary, mirror, and backup copies. Backup retention must not be shorter than the approved legal, security, and project-retention requirement; that duration remains a Founder decision.

## Change Governance

| Action | Authorized role |
| --- | --- |
| Propose | Founder, authorized contributor, assigned domain reviewer, or AI within explicit task scope |
| Review | Repository Guardian and applicable assigned domain reviewers |
| Approve | Founder until an approved delegation is recorded |
| Reject or require rework | Founder; reviewers may recommend rejection or rework within their review scope |
| Merge to a protected branch | Authorized maintainer only after recorded approval and validation |
| Create approved baseline or release tag | Authorized maintainer only for the exact Founder-approved commit and metadata |

- Founder authority is explicit, recorded, scoped, and traceable; it is not inferred from conversation history.
- AI may inspect, propose, and perform explicitly authorized repository-documentation changes.
- AI may not approve, merge, commit, tag, force-push, delete branches, rewrite history, configure remotes, create backups, or release unless an exact future task and applicable approvals authorize the specific action.
- Review and audit results are evidence, not approval.

## Documentation Freeze

- The exact versions of approved governing documents, accepted decisions, baseline manifests, and release evidence are frozen at their approved commit and tag.
- Draft and Review documents remain editable only on authorized branches and do not alter the frozen approved version.
- Approved documents evolve through a new version, review, approval, commit, and tag or baseline relationship.
- Metadata corrections to an approved document use a new commit and preserve the original record.
- Superseded, Deprecated, Archived, Historical, and Cancelled documents remain retrievable and are not rewritten as current authority.
- An emergency correction does not bypass history preservation or post-change approval.

## Repository Validation Rules

| Validation area | Pass criteria | Fail criteria |
| --- | --- | --- |
| Git | Valid repository, readable object database, expected working-tree state, and no unresolved Git operation | Corruption, unresolved merge/rebase, or unexplained working-tree state |
| Branches | Protected branches and active short-lived branches follow names, sources, targets, ownership, and approval rules | Direct protected-branch work, invalid name, stale unowned branch, or forbidden merge path |
| Tags | Approved tags are annotated, immutable, correctly formatted, and point to the approved commit | Lightweight, moved, reused, deleted, malformed, or unsupported tag |
| Versions | Version class, metadata, compatibility, tag, and approval evidence agree | Conflicting versions or unsupported compatibility claim |
| Commits | Atomic commit with allowed type, scope, references, validation, and no excluded content | Mixed scope, unsupported claim, missing reference, secret, licensed archive, or generated data |
| Baselines | Exact commit, manifest, validation, review, Founder approval, tag, remote, and mirror identifiers agree | Working tree or unapproved commit represented as a baseline |
| Repository metadata | Owner, authority, lifecycle, source, dependencies, traceability, version, and approval are consistent | Missing, circular, ambiguous, or conflicting metadata |

Validation is read-only until the exact mutation is approved. A failed mandatory check blocks merge, tag, baseline, or release progression.

## Current-State Boundary

Current Git state is reported only in [Repository Health](REPOSITORY_HEALTH.md) and the [Batch 03 Audit](AUDIT_REPORT_BATCH03.md). This policy does not claim that a baseline, commit, tag, branch set, remote, mirror, backup, or release currently exists.

## References

- [Repository Standards](07_REPOSITORY_GUIDE.md)
- [Development Workflow](08_DEVELOPMENT_WORKFLOW.md)
- [Changelog Policy](14_CHANGELOG_POLICY.md)
- [Review Process](15_REVIEW_PROCESS.md)
- [AI Collaboration Standard](AI_COLLABORATION.md)
- [Repository Health](REPOSITORY_HEALTH.md)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Repository Reading Order](READING_ORDER.md)
- [Batch 03 Audit](AUDIT_REPORT_BATCH03.md)
