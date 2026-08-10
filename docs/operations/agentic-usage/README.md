# Agentic Usage Register

## Document Control

- **Status:** Draft
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Purpose:** Local, documentation-only operational evidence for Mission execution activity and user-reported Usage snapshots.

## Boundary

This register is not a billing system, Token counter, external telemetry collector, runtime log, or Product/Knowledge authority. It never calls an external API and never infers Tokens, Credits, model, reasoning level, or usage percentage.

Only user-reported snapshots from `ChatGPT Usage and limits` are recorded. Absent values remain `null` with `NOT_OBSERVABLE`; forecasts are `INSUFFICIENT_DATA` until the closed contract permits an `ESTIMATE`.

The v1 register rejects `ESTIMATE` fail-closed: it has no register-wide resolver
for real snapshots across cycles or reproducible forecast arithmetic.

## Records

- [Data contract](agentic_usage.schema.yaml)
- [Current cycle](cycles/2026-c01.yaml)
- [Mission summary template](USAGE_SUMMARY_TEMPLATE.md)

At the beginning and end of a significant Mission, record only visible metadata. Store counts and bounded identifiers, never raw commands, credentials, cookies, sessions, PII, prompts, or sensitive file contents. `notes` is only `null` or up to 280 characters of semicolon-separated values from the closed `redacted_note_code_values` schema enum, for example `FOUNDER_REPORTED;NO_EXTERNAL_CALLS`. Reason and uncertainty fields use the closed enums in the schema.

## Validation

Run the frozen absolute interpreter with `-B`, `PYTHONDONTWRITEBYTECODE=1`, a
recorded `PATH`, and a dedicated `TMPDIR`; the exact command lines are frozen in
the Gate evidence. The register has no dependency-installation, hook, cron,
network, or telemetry behavior.
