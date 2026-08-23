# FT-RB-00 — Fast-Track Remaining Blockers Campaign Status v1.0

## Control

- Mission: `FT-RB-00`
- Lifecycle: Review
- Authority: Founder campaign authorization `C0BNHRRTE9F / 1787485976.633809`, Founder `U0BNFS43TBL`, complete thread with zero replies
- Fast-Track parent: `C0BNHRRTE9F / 1787398697.475999`
- Separate current-instruction SHA-256: `f49f01222adc1b1389e61a99f1a07db13c07d01b2d36522a2469975a2015f839`; the Slack authorization is not represented as hash-binding that attachment
- Authorized starting `main`: `310d0ac3f6f9da67a975a32beb0b55361aa176d5`; post-merge CI `32637163057 = PASS`

## Purpose and boundary

This immutable baseline router records the campaign plan and machine-readable
status for the seven remaining Fast-Track blockers. Lane updates must be
append-only lane-local deltas, and an effective resolution may consume only
integrated evidence. It does not start a lane, create a PR, claim a merge, change
a prerequisite, or transfer a canonical owner. The router becomes effective only
if its carrying PR is merged to `main`.

`workflow_status` is exactly one of `NOT_STARTED`, `IN_PROGRESS`, `PR_READY`,
`WAITING_FOR_MERGE`, `BLOCKED_EXTERNAL_INPUT`, `INTEGRATED`,
`READY_FOR_GATE_REEVALUATION`, `MET`, `FAILED`, or `SUPERSEDED`.
`readiness_classification` is deliberately separate: a repository-ready package
is not gate-MET or Runtime/Staging evidence.

## Preserved effective state

- `FAST_TRACK_INQUIRY_LAUNCH_ELIGIBLE = FALSE`; `5 MET / 7 UNMET / 12 TOTAL`.
- Exact blockers: `RIGHTS_SAFE_MEDIA_READY`, `INQUIRY_CRM_FLOW_READY`,
  `SECURITY_PRIVACY_GATE_READY`, `SEO_INDEXING_GATE_READY`,
  `MOBILE_PERFORMANCE_GATE_READY`, `STAGING_ACCEPTANCE_PASS`, and
  `PRODUCTION_FOUNDER_GO`.
- C002 remains `6/9 / NOT_READY`; Founder selection is false and candidate count
  is zero. Supply/Fulfillment remain submitted/incomplete and Photo/Content stays
  missing evidence.
- The sole slice remains `pilot:f5922666261e` / `pcomb:829e387ccdcb` /
  `prd:sku:66ebd0510693`; Availability is `MISSING_DATA_VALUE`; Brand and Color
  are absent-not-promoted; Price, Stock, ETA/SLA, and supplier truth are absent.

## Lane board

| Mission | Blocker/package | Workflow status | Readiness classification | Gate state | Next action |
| --- | --- | --- | --- | --- | --- |
| FT-RB-01 | Rights-safe media | NOT_STARTED | BLOCKED_EXTERNAL_EVIDENCE | UNMET | Governed intake and rights checklist only |
| FT-RB-02 | Inquiry/CRM | NOT_STARTED | NOT_REVIEWED | UNMET | Repository-only no-price flow package |
| FT-RB-03 | Security/privacy | NOT_STARTED | NOT_REVIEWED | UNMET | Repository-only hardening package |
| FT-RB-04 | SEO/indexing | NOT_STARTED | NOT_REVIEWED | UNMET | Canonical/noindex package only |
| FT-RB-05 | Mobile/performance | NOT_STARTED | NOT_REVIEWED | UNMET | Static controls and future measurement plan |
| FT-RB-06 | WordPress/Woo projection enabler | NOT_STARTED | NOT_REVIEWED | Not a gate prerequisite | Wait for applicable integrated packages |
| FT-RB-07 | Integrated release candidate | NOT_STARTED | NOT_REVIEWED | Not a gate prerequisite | Wait for integrated dependencies |
| FT-RB-08 | Staging acceptance preparation | NOT_STARTED | NOT_REVIEWED | UNMET | Prepare only; first mutation needs Founder gate |

## Execution controls

Each lane must have one writer, worktree, and branch; re-resolve live `main`;
avoid cross-Mission unreviewed stacking; and observe maximum WIP of one Commercial,
one Core, and one Enabler lane. Each has one non-draft PR, independent review and
exact-head CI; a changed head invalidates both review and CI. Every PR stops before
Merge. The eight-mission DAG is FT-RB-01 through FT-RB-05, then FT-RB-06, then
FT-RB-07, then FT-RB-08. The seven gate blockers remain distinct, including
`PRODUCTION_FOUNDER_GO` separately from the eight-Mission DAG.

## Exact realized allowlist

The machine registry binds the exact sorted 20-path allowlist. No path outside it
is authorized by FT-RB-00.

```text
docs/08_DOCUMENTATION_INDEX.md
docs/14_CHANGELOG.md
docs/18_OPEN_QUESTIONS.md
docs/CURRENT_PROJECT_STATE.md
docs/FT_RB_00_FAST_TRACK_REMAINING_BLOCKERS_CAMPAIGN_STATUS_V1.0.md
docs/PROJECT_EXECUTION_ROADMAP.md
docs/TRACEABILITY_MATRIX.md
repository/data/contracts/ft-rb-campaign-status.contract.yaml
repository/data/registries/extensions/ftrb/campaign-status.yaml
repository/data/schemas/ft-rb-campaign-status.schema.json
repository/data/validation/validate_ft_rb_campaign_status.py
scripts/test.sh
tests/fixtures/ft-rb-campaign-status/README.md
tests/fixtures/ft-rb-campaign-status/adversarial-duplicate-keys.json
tests/fixtures/ft-rb-campaign-status/adversarial-duplicate-keys.yaml
tests/fixtures/ft-rb-campaign-status/adversarial-permissive-schema.json
tests/fixtures/ft-rb-campaign-status/adversarial-remote-ref-schema.json
tests/fixtures/ft-rb-campaign-status/mutation-cases.json
tests/fixtures/ft-rb-campaign-status/valid-synthetic.yaml
tests/test_ft_rb_campaign_status.py
```

## No-GO

No Product/combination/SKU mutation, Price/Stock/Availability/ETA/SLA claim,
media asset/right creation, Runtime, WordPress/WooCommerce, Staging, Production,
publication, deployment, merge, auto-merge, branch deletion, M4, or successor
Mission is created here. Each later gate re-evaluation must be an append-only,
merged-evidence delta and may change only proven prerequisites.

## Validation and review

- Semantic digests are pinned exactly: contract `0abac587…f59aca`, schema
  `9ccc2f73…f86a0d`, canonical registry `242df96b…419b1`, and distinct synthetic
  fixture `4ace489d…12ad`.
- Strict canonical and synthetic validation passed; 12 focused tests and all 19
  named mutations passed.
- `make validate`, full `make test`, the 173-document manifest, 173-row / 21-domain
  Atlas, 5,136 Markdown links/anchors, the agentic validator and 15 agentic tests
  passed on the frozen tree. The protected C009 stable-ID collision regression
  passed after this router stopped persisting canonical Product IDs.
- Independent pre-pin and final pinned-tree reviews each returned
  `0 material / 0 non-material` findings. Exact-head CI remains pending until
  independently completed on the immutable pushed head.
