# Git Baseline Approval Checklist

## Current Applicability — 2026-07-20

This checklist is preserved as historical GIT-01/GIT-02 review evidence. Its 298-row counts and future-authorization wording below were valid for that earlier review and do not describe the current repository or grant current authority.

The current `docs/GIT_FILE_CLASSIFICATION.csv` is a dated 2026-07-14 inventory snapshot with 550 rows: 110 `TRACK_CANONICAL`, 236 `TRACK_DOCUMENTATION`, 172 `TRACK_IMPLEMENTATION_ASSET`, 20 `TRACK_CONFIGURATION_TEMPLATE`, 11 `IGNORE_LOCAL`, and 1 `DELETION_CANDIDATE`. Its renamed state column records snapshot state, not current Git state, and the CSV authorizes no deletion.

Historically, the explicit 2026-07-19 Class B Wave 1 Founder authorization permitted exactly 19 approved paths, one scoped commit, push of only `codex/class-b-wave-01-governance`, and one Draft PR while merge remained excluded. That authorization must not be rewritten as earlier merge authority.

PR #1, PR #2, and PR #3 were later separately approved and merged; Wave 1 and read-only Wave 2 discovery are complete. Canonical/default `main` is verified at shared baseline `d702c5217f7caa2f23e56f965f3f993967e3c17d`, `origin/HEAD` resolves to `origin/main`, and main protection is active with administrator enforcement and strict required check `repository-validation`; force-push and deletion are disabled. The old Wave 1 and post-merge Draft-PR authorizations remain historical evidence only. Current Git mutation authority is limited to the Founder-approved 21-file-ceiling Wave 2 pre-implementation documentation reconciliation, one commit, push of only `codex/wave-2-preimplementation-reconciliation`, and one Draft PR against `main`; Codex may not merge it. Wave 2A implementation remains unauthorized. No workflow activation, runtime execution, WordPress or Product Repository implementation, publication, deployment, or production mutation has occurred.

## Historical Review Scope

This checklist authorizes review only. Completing it does not stage, commit, push, deploy, import, publish, or change runtime systems.

## Founder Review

- [ ] I reviewed `docs/GIT_BASELINE_AUDIT.md`.
- [ ] I reviewed all 298 rows in `docs/GIT_FILE_CLASSIFICATION.csv`.
- [ ] I accept the 110 `TRACK_CANONICAL` classifications.
- [ ] I accept the 45 `TRACK_DOCUMENTATION` classifications.
- [ ] I accept the 129 `TRACK_IMPLEMENTATION_ASSET` classifications.
- [ ] I accept the 3 `TRACK_CONFIGURATION_TEMPLATE` classifications.
- [ ] I confirm `.env.example` is a non-secret template and must remain trackable.
- [ ] I accept that 11 `.DS_Store` files remain ignored and are not deleted in this sprint.
- [ ] I confirm no Product DNA, Master Data, or Golden Reference content was altered by GIT-01.
- [ ] I accept the `.gitignore` additions for secrets, local files, caches, logs, backups, dumps, and deployment artifacts.
- [ ] I accept the `.gitattributes` LF text and binary-file rules.
- [ ] I accept that no file larger than 10 MB or Git LFS candidate currently exists.
- [ ] I accept that empty `.gitkeep` files are intentional directory placeholders.
- [ ] I accept that there are no current `REVIEW_REQUIRED`, `DUPLICATE_CANDIDATE`, or `DELETION_CANDIDATE` items.

## Required Decision

- [ ] **APPROVE CLASSIFICATION ONLY** — authorize a separate future local baseline commit sprint.
- [ ] **REQUEST CORRECTIONS** — identify exact CSV rows and required classification changes.
- [ ] **DEFER** — leave the working tree unchanged and do not begin a commit sprint.

Only one decision should be selected and recorded with date and Founder identity.

## Separate Authorization Boundaries

- [ ] No commit is authorized by this checklist alone.
- [ ] No push is authorized by this checklist.
- [ ] No deployment is authorized by this checklist.
- [ ] No WordPress, cPanel, FTP, database, or remote access is authorized.
- [ ] No runtime, import, or publishing action is authorized.

## Exit Condition

A future commit sprint may begin only after the Founder approves the classification, specifies the exact staging scope, and explicitly authorizes a local commit without push. Any classification correction must update the CSV and re-run Git/secret validation first.

## Historical Decision and Current Boundary

- Historical GIT-01/GIT-02 Founder review: **GO within its dated scope**
- Class B Wave 1 exact-path commit: **GO by separate 2026-07-19 authorization**
- Push of `codex/class-b-wave-01-governance`: **GO by separate 2026-07-19 authorization**
- One Draft PR for Wave 1: **GO by separate 2026-07-19 authorization**
- Historical Wave 1 and PR #3 merges: **COMPLETE by later separate Founder approvals**
- Default branch and main protection remediation: **COMPLETE by separate Founder approvals**
- Wave 2 discovery: **COMPLETE, read-only**
- Wave 2 pre-implementation documentation Draft PR: **GO within the exact current authorization; merge requires Founder review**
- Wave 2A implementation and later implementation work: **NO-GO pending separate Founder authorization**
- Deployment: **NO-GO**
- Runtime: **NO-GO**
- Import: **NO-GO**
- Publishing: **NO-GO**
