# n8n Safety Model

## Status and Scope

All imported Damavand Steel n8n workflows are inactive and **NO-GO for activation or production use**. This model governs the current Atlas workflow files only. It does not authorize credentials, remote execution, publication, deployment, or production mutation.

## Four-Stage Execution Model

`execution_mode` is a closed enum with exactly four values:

| Mode | Local validation | OpenAI | GitHub read | GitHub write | Publish/deploy |
| --- | --- | --- | --- | --- | --- |
| `OFFLINE` | Allowed | Blocked | Blocked | Blocked | Blocked |
| `VALIDATE` | Required | Blocked | Blocked | Blocked | Blocked |
| `DRY_RUN` | Allowed | Allowed | Read-only | Blocked | Blocked |
| `LIVE` | Required before use | Allowed | Allowed | Conditional | Blocked unless separately governed and approved |

The default is `OFFLINE`. Every workflow resolves a missing, null, malformed, differently cased, or unknown mode to `OFFLINE`. Only an exact enum string is accepted. OFFLINE and VALIDATE paths terminate before all GitHub, OpenAI, and other external API nodes with `network_performed: false` and `write_performed: false`.

### OFFLINE

- No network, OpenAI, GitHub, or external API access.
- Local repository validation only.
- The authoritative command is `python3 scripts/validate_manifest.py`.

### VALIDATE

- No network, OpenAI, GitHub, or external API access.
- Runs or requires local manifest, registry, schema, workflow, execution-mode, secret, and connection validation through the repository validator.
- n8n local-only result nodes identify the command; they do not execute a shell command themselves.

### DRY_RUN

- OpenAI requests and GitHub reads are permitted in an isolated, approved test environment.
- GitHub and all other remote writes are prohibited regardless of the values of `dry_run`, Founder approval, credentials, or workflow state.
- No remote file, branch, commit, pull request, release, publication, or deployment may be created.

### LIVE

LIVE is necessary but not sufficient for a write. The write gate requires all of the following strict conditions at the same time:

1. `execution_mode === 'LIVE'`
2. `dry_run === false`
3. `founder_write_approved === true`
4. `credentials_configured === true`
5. `$workflow.active === true`

Only LIVE may perform a GitHub write. Any missing or malformed value fails closed. The imported workflow files have `active: false`, so the current repository artifacts cannot satisfy the LIVE gate.

## Dry-Run Compatibility Field

`dry_run` defaults to the boolean value `true`. The write gate treats a missing, null, string, number, or otherwise malformed value as dry run. Only the strict boolean value `false` can satisfy the first write condition.

When the effective dry-run value is true, the GitHub write node cannot execute. The workflow terminates that path with:

```json
{
  "status": "dry_run_blocked_write",
  "write_performed": false
}
```

`dry_run` does not select the execution stage. `execution_mode` is authoritative. In DRY_RUN, a GitHub write remains impossible even if `dry_run` is incorrectly set to false. OFFLINE is the only mode that guarantees no network activity.

## Founder Approval Behavior

`founder_write_approved` defaults to the boolean value `false`. A missing, null, string, number, or malformed value does not grant approval. Only the strict boolean value `true` can satisfy the second write condition.

If dry run is strictly false but Founder approval is not strictly true, the workflow terminates with `status: founder_approval_blocked_write` and `write_performed: false`.

## Write Gates

The current workflow set contains one recognized remote repository write: `Commit Draft To GitHub`, an HTTP `PUT` in WF-02. `LIVE Remote Write Safety Gate` is its immediate predecessor and checks all five LIVE requirements. The true output reaches the write; the false output reaches a terminal blocked-result node. Validation failures terminate without reaching the write gate.

Every future GitHub mutation, file creation/replacement, branch, commit, pull request, release, publishing, or deployment node must have its own immediate full LIVE gate and terminal blocked path. Reusing a distant upstream check is insufficient.

## Credential Handling

- No token, API key, password, credential ID, account identifier, or production value may be committed in workflow JSON.
- Repository and workflow identifiers remain explicit non-secret configuration placeholders.
- The imported JSON currently references environment-variable names but contains no values.
- Before any manual test or activation, GitHub and OpenAI authentication must be configured through n8n Credentials, scoped with least privilege, and reviewed for log and prompt exposure.
- `credentials_configured` is a fail-closed confirmation field, not proof that a credential exists or is safe. It may become true only after the actual n8n Credentials configuration is reviewed.
- Credential exports and n8n local state must never enter Git.

## Activation Prohibition

Imported workflows must remain inactive until all of the following are independently satisfied:

1. Credentials are configured through n8n Credentials with least privilege.
2. Repository owner, repository, branch, paths, and workflow IDs are reviewed against an isolated non-production target.
3. OFFLINE and VALIDATE checks pass without network access.
4. A DRY_RUN test passes and proves that no remote write occurs.
5. Failure and stop paths are reviewed.
6. The Founder explicitly approves remote writes and separately approves any activation scope.

Import success, JSON validity, a passing local validator, or Founder approval of repository files does not authorize activation.

## Safe Testing Procedure

1. Keep all workflows inactive and run `python3 scripts/validate_manifest.py` locally in OFFLINE/VALIDATE scope.
2. Confirm the validator reports zero OFFLINE/VALIDATE network violations and zero execution-mode policy errors.
3. Use an isolated non-production n8n instance and a disposable test repository; never use production hosting, WordPress, WooCommerce, or a production branch.
4. Configure least-privilege authentication through n8n Credentials. Begin with read-only GitHub access.
5. Replace only the named configuration placeholders with reviewed test values.
6. Select `execution_mode = DRY_RUN`, keep `dry_run = true`, `founder_write_approved = false`, and `credentials_configured = false` until credential review is recorded.
7. Manually test one controlled document and verify `status = dry_run_blocked_write`, `write_performed = false`, and no remote repository change.
8. Review execution data and logs for secrets, unexpected endpoints, excessive permissions, or unsafe error output.
9. A limited LIVE write test requires separate recorded Founder approval, reviewed n8n Credentials, an isolated branch, a known backup/rollback path, explicit activation, and all five strict LIVE gate conditions. Production remains separately prohibited.

## Emergency Stop Procedure

If an unexpected write, endpoint, credential exposure, or execution occurs:

1. Stop the current execution and keep or set every affected workflow inactive.
2. Disable the affected n8n credential and revoke the provider token if exposure is possible.
3. Do not retry, publish, deploy, or clean up evidence automatically.
4. Preserve execution IDs, timestamps, node output, target paths, Git history, and audit logs without copying secret values into reports.
5. Inspect the remote target read-only to determine impact.
6. Notify the Founder, record the incident and affected scope, and require explicit rollback or remediation approval.
7. Rotate credentials and revalidate in isolation before any future execution is considered.

## Known Limitations

- OFFLINE/VALIDATE behavior is enforced by static workflow routing but has not been runtime-tested in an n8n instance.
- DRY_RUN permits GitHub reads and OpenAI requests by design; it is not an offline mode.
- Static validation recognizes declared GitHub HTTP writes and n8n GitHub mutation nodes. A future custom Code node could conceal a write and therefore requires human review.
- The supplied authorization expressions are non-secret placeholders, not configured n8n Credentials. This is an activation stop condition.
- `credentials_configured` is a reviewed assertion and cannot itself verify credential scope, storage, or validity.
- The LIVE gate relies on n8n exposing `$workflow.active` as a strict runtime boolean; version compatibility remains untested.
- Runtime import compatibility and behavior have not been tested in an n8n instance.
- The repair workflow is intentionally not wired automatically to the generator.
- Repository values and imported workflow IDs remain unconfigured.
- The three-attempt repair guard limits attempts but does not replace human review of repaired content.
- No workflow in this package is approved for production, publishing, deployment, or unattended execution.
