# FT-RB-02 — Inquiry / CRM Flow Readiness Foundation

## Document control

- Mission: `FT-RB-02`
- Campaign authority: `slack:C0BNHRRTE9F:1787485976.633809`
- Fast-Track parent: `slack:C0BNHRRTE9F:1787398697.475999`
- Campaign-authorized starting main: `310d0ac3f6f9da67a975a32beb0b55361aa176d5`
- Mission base main after the authorized FT-RB-01 single-file regression repair: `5f452703dd35e1fee050f09529a0de379767e2bb`
- Starting-main CI: `32665124526 = PASS`
- Branch: `codex/ft-rb-02-inquiry-crm-flow-readiness`
- Owner: `INQUIRY_DATA_MODEL`
- Status: repository package review candidate; no implementation or gate transition

## Objective

Define a fail-closed, repository-only Inquiry/CRM flow contract for the first commercial slice. This package records approved minimum input semantics, status-plane separation, manual supply-check boundaries, privacy and analytics constraints, missing authority inputs, and validation evidence. It creates no form, Inquiry, Customer, CRM record, provider, endpoint, credential, runtime configuration, or public commercial claim.

## Source reconciliation

Founder reply `1787398832.469889` supplies the Inquiry/CRM payload and Inquiry Type direction. Founder reply `1787400933.711809` supplies planned content visibility. Reply `1787401091.613509` controls the future Lead/operator workflow and noncanonical supply-check states. Reply `1787401125.584279` controls the analytics/commercial-funnel boundary. The later, same-scope privacy-specific reply `1787401309.508679` controls requiredness: Name and Mobile are required; City is optional/conditional and may be requested only when operationally useful; Quantity and Notes are optional. Missing City is not an error and no City value or operational condition may be inferred.

The single-file repair authority `1787515209.992049` and merge/resume authority `1787517433.749679` are procedural restart evidence only. PR #53 integrated at `5f452703dd35e1fee050f09529a0de379767e2bb`, and exact-main CI `32665124526` passed on that SHA. These records permit restarting this bounded lane from the repaired main; they set no Inquiry, CRM, Product, privacy, commercial, or runtime field semantics.

Inquiry Type remains required and intent-only with exact source tokens `PRICE`, `STOCK_CHECK`, and `CONSULTATION`; literal runtime labels/localization remain missing authority input. Product context is system-attached from approved owners and is never retyped by the customer. Its future roles are Family, Material, Grade, Diameter, Brand, Thickness, Finish/Color, Length, canonical Product/Variant references when available, and source page path; this package populates none of those values and infers no absent value.

## Exact write allowlist

1. `docs/FT_RB_02_INQUIRY_CRM_FLOW_READINESS_SCOPE_V1.0.md`
2. `repository/data/contracts/ft-rb-02-inquiry-crm-flow-readiness.contract.yaml`
3. `repository/data/registries/extensions/ftrb02/inquiry-crm-flow-readiness.yaml`
4. `repository/data/schemas/ft-rb-02-inquiry-crm-flow-readiness.schema.json`
5. `repository/data/validation/validate_ft_rb_02_inquiry_crm_flow_readiness.py`
6. `scripts/test.sh`
7. `tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/README.md`
8. `tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/adversarial-duplicate-keys.json`
9. `tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/adversarial-duplicate-keys.yaml`
10. `tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/adversarial-permissive-schema.json`
11. `tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/adversarial-remote-ref-schema.json`
12. `tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/mutation-cases.json`
13. `tests/fixtures/ft-rb-02-inquiry-crm-flow-readiness/valid-synthetic.yaml`
14. `tests/test_ft_rb_02_inquiry_crm_flow_readiness.py`

`scripts/test.sh` is condition-bound to one strict canonical, one strict synthetic, and one focused unittest dispatch. All other runner behavior is immutable.

## Readiness ceiling

- Repository package: `REPOSITORY_READY`
- Workflow: `BLOCKED_EXTERNAL_INPUT`
- Implementation/configuration: `MISSING_AUTHORITY_INPUT`
- Runtime: `NOT_IMPLEMENTED`
- Staging end-to-end: `NOT_RUN`
- `INQUIRY_CRM_FLOW_READY`: `UNMET`
- Fast-Track gate: `FALSE / 5 MET / 7 UNMET / 12`
- Gate transition: none

## Plane and owner boundaries

Inquiry is not Quote, Reservation, Order, Payment, Availability, Stock, Price, ETA, SLA, or supplier truth. The Inquiry lifecycle, future Sales/lead vocabulary, CRM synchronization state, Customer identity, private Quotation, and canonical Product facts remain separate planes.

The Founder-supplied lead-stage vocabulary has an ordered prefix `NEW → CONTACTED → QUALIFIED → SUPPLY_CHECK → QUOTE_PREPARED` and alternative terminal outcomes `WON | LOST | CLOSED`. It is a future operator/Lead vocabulary only, not an implemented transition graph. `QUOTE_PREPARED` creates no Quote or value. `WON` means a customer accepted a commercial offer and may progress only under a later Order process; `LOST` records a lost commercial opportunity with a reason where useful; `CLOSED` is reserved for duplicate, invalid, spam, unreachable, or intentionally closed-without-sale records. Every future transition requires actor, timestamp, previous/new state, reason, and audit evidence; automatic transitions are prohibited.

`CONTACTED` requires contact-attempt/result evidence and accepts corrections only when customer-provided. `QUALIFIED` records intended use only when useful; an invalid Product configuration remains unresolved and triggers clarification rather than fabrication. Requested quantity and unit are separate, the unit is never guessed, and supplier-detail collection remains deferred. Response time is a repository requirement measured from `created_at` to the first real operator action, never a public SLA. The future minimum operator screen covers contact, source, selected Product configuration, requested quantity/unit, optional City/Notes, lifecycle, timestamps, contact history, next action, and Quote-handoff status; no screen is implemented here.

Supply-check states are internal operational context only: `CHECK_REQUIRED`, `CHECKED_CAN_PROCEED`, and `CHECKED_CANNOT_PROCEED`. They never become canonical or public Availability, Stock, ETA, SLA, or supplier truth.

## Privacy, identity, delivery, and analytics

- Name and Mobile are required PII; the exact Iranian-mobile accepted formats and normalization algorithm remain missing authority input.
- City is customer-provided only, optional/conditional, never inferred, and cannot silently drive routing or supply truth.
- Inquiry-processing disclosure is required, but exact approved Persian text, version, legal basis, retention, deletion, anonymization, correction, and access policy remain missing.
- Marketing consent is separate, optional, and never prechecked.
- Matching may create review candidates only. No Customer record or automatic merge may be created from name, mobile, email, organization, cookie, device, or shared identifiers.
- Attachments are disabled for this launch package.
- Idempotency, safe retry, duplicate-submit prevention, reconciliation, and failure visibility are requirements; exact thresholds/provider behavior remain missing.
- A future payload may define an Inquiry ID, creation time, website source channel, safe source path, payload-schema/version reference, consent/privacy state and policy-version reference, minimized customer contact, immutable Product-selection snapshot, Inquiry intent, optional quantity/unit/notes, and operator-workflow fields. Unknown units stay unknown. Future operator roles include contact attempts/results, customer-provided corrections, requested quantity/unit, useful-only intended use, current owner/assignee, fallback, routing, escalation, reopen authority, next action, and Quote-handoff status; every value remains missing authority input and no payload or record is created here.
- Repository requirements include HTTPS, authoritative server validation, convenience-only client validation, CSRF/nonce, low-friction rate limiting and anti-spam, conditional visible CAPTCHA only upon abuse, untrusted-input handling, output escaping, safe public errors, duplicate-submit suppression, safe retry/fallback, and Staging verification. Every implementation/verification state remains not implemented/not verified/not run.
- The analytics contract is requirements-only and emits nothing. Its exact event vocabulary is `page_view`, `product_family_view`, `product_201_51_view`, `variant_selector_interaction`, `valid_variant_completed`, `inquiry_cta_click`, `inquiry_form_start`, `inquiry_submit_success`, `call_cta_click`, `contacted`, `qualified`, `supply_check_started`, `quote_prepared`, `won`, `lost`, and `closed`. Primary KPI definitions, diagnostics, non-success-alone metrics, the nine minimum payload roles, and daily/weekly/monthly review cadence are machine-bound in the registry. Anonymous/session, device and referrer/source/UTM roles remain privacy-conditional; a generated Lead ID is permitted only after successful submit. Analytics owns no policy, Product, or commercial truth, emits no PII/raw-query URL, and fabricates no benchmark, revenue, conversion, or result.

## Missing authority inputs

Approved privacy/consent text and legal basis; retention/deletion/anonymization/correction policy; exact Iranian-mobile validation; named operational owner/assignees/fallback/routing/escalation/reopen authority; role/object/field/export permissions; LOST/CLOSED reasons; notification recipients/templates; approved CRM/form/SMTP/anti-spam/analytics provider, version, license and provenance; endpoint and secret-reference model; field mapping and retry/reconciliation; dedupe/idempotency thresholds; security acceptance; Runtime target; and observed Staging end-to-end evidence.

## No-go

No Inquiry/Customer/CRM record is populated. No canonical Product identifier is duplicated in this package. No Product, Combination, SKU, Brand, Color, Mass, Availability, Price, Stock, ETA, SLA, supplier truth, Quote, Reservation, Order, Payment, WordPress, WooCommerce, Runtime, Staging, Production, deployment, publication, Merge, auto-merge, source-branch deletion, M4, gate transition, or successor Mission is authorized.

## Validation and stop

Current local evidence on the final semantic surfaces: contract `21d16949…3850`, schema `146e75ce…d479`, canonical registry `5fdc9a5e…c6f2`, and distinct synthetic registry `2c778bc6…9019` are pinned; strict canonical and synthetic validation passed; the focused 45-test suite and all 200 named mutations passed; and full `make test` passed with 173 manifest documents, 173 Atlas rows across 21 domains, 5,136 links/anchors, the agentic validator and 15 tests, zero detected secrets, and inactive/offline workflow controls.

Exact-head CI and independent Project Commander review remain pull-request gates. No review or CI result creates Merge authority.

Stop before Merge. A later merge requires separate Founder / Project Commander authorization.
