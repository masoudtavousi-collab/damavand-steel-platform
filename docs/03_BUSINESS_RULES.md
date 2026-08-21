# DS-003 Business Rules

## Table of Contents

- [Purpose](#purpose)
- [Core Principle Compliance](#core-principle-compliance)
- [Scope](#scope)
- [Audience](#audience)
- [Status](#status)
- [Owner](#owner)
- [Reviewer](#reviewer)
- [Approval Authority](#approval-authority)
- [Version](#version)
- [Last Updated](#last-updated)
- [Last Review](#last-review)
- [Related Documents](#related-documents)
- [Overview](#overview)
- [Definitions](#definitions)
- [Responsibilities](#responsibilities)
- [Decisions](#decisions)
- [Constraints](#constraints)
- [Open Questions](#open-questions)
- [Founder Decisions](#founder-decisions)
- [Future Improvements](#future-improvements)

## Purpose

Defines the governing purpose of the Business Rules document within the project documentation set.

## Core Principle Compliance

Business rules are governed by the authoritative [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles). CP-005 Inquiry First and CP-006 No Public Pricing are also supported by [ADR 0001](adr/0001-inquiry-first-commerce.md).

CP-001 Plugin First, CP-002 Configuration First, CP-003 Mobile First, CP-004 Persian RTL, CP-007 No Custom Theme, CP-008 No Gravity Forms, CP-009 No LiteSpeed Cache, and CP-010 No AI Features (Phase 1) are implementation constraints that business rules must not override.

This section does not create product structure, taxonomy, WooCommerce configuration, or implementation behavior.

## Scope

This Draft document summarizes the accepted cross-domain business constraints that
govern Phase 1 and links detailed Product, inquiry, commerce, content, and
operational rules to their canonical owners. It creates no new commercial policy,
Product record, customer rule, or Runtime behavior.

## Audience

Founder, Project Commander, Sales and domain reviewers, Repository Guardian,
Product/commerce planners, implementation teams, and independent QA/security
reviewers.

## Status

Draft

## Owner

Founder

## Reviewer

Repository Guardian

## Approval Authority

Founder

## Version

0.2.0

## Last Updated

2026-08-21

## Last Review

2026-08-21

## Related Documents

- [DS-000 Project Bible](00_PROJECT_BIBLE.md)
- [DS-001 Project Constitution](01_PROJECT_CONSTITUTION.md)
- [ADR 0001: Inquiry-first commerce](adr/0001-inquiry-first-commerce.md)
- [Founder Decision Log](17_FOUNDER_DECISION_LOG.md)
- [Open Questions](18_OPEN_QUESTIONS.md)
- [C002 Commercial Pilot and Product Administration Scope](C002_COMMERCIAL_PILOT_PRODUCT_ADMINISTRATION_CONTRACTS_SCOPE_V1.0.md)
- [C007 Governance Convergence Scope](C007_GOVERNANCE_CONVERGENCE_PHASE1_ARCHITECTURE_BASELINE_SCOPE_V1.0.md)

## Overview

Phase-1 customer interaction is inquiry-first and has no active public purchase
authority. Public Price, Offer schema, Cart, Checkout, Payment, and unsupported
Availability/stock claims remain disabled. Product, supplier, Mass, Availability,
Price, customer, inquiry, quote, reservation, order, and payment facts remain
separate and evidence-bound. The approved target of future per-SKU eligibility is
inactive and requires separate gates.

## Definitions

- **Inquiry First:** the current public commercial path ends in governed inquiry
  and operator follow-up, not checkout.
- **No Public Pricing:** no public price or Price/Offer structured data is active.
- **Commerce eligibility:** a future per-canonical-SKU, fail-closed state; Family,
  Series, Pilot, or Product existence does not confer it.
- **Availability:** a provenance- and validity-bound state, never inferred from
  Product existence, supplier habit, or missing evidence.
- **Founder-confirmed evidence:** bounded business evidence, not automatic Product
  or Runtime truth.

## Responsibilities

- Canonical owners validate Product and commercial evidence separately.
- Operators verify supply and handle inquiry/quotation transitions where
  applicable.
- Domain and legal/commercial reviewers validate policies before activation.
- Security/privacy reviewers govern protected customer and operational data.
- The Founder retains approval of protected commercial decisions and activation.

## Decisions

Current operation remains `INQUIRY_ONLY`. Exact inventory quantity is not public;
Availability may be projected only from valid evidence and applicable operator
verification. The three PD-03B records remain seed/reference evidence, not Product,
SKU, Availability, or a ceiling on future scope. C002 readiness remains fail-closed
and no C007 text changes those machine states.

## Constraints

- Do not infer Product, compatibility, stock, Availability, Price, discount,
  purchase eligibility, or fulfillment from planning evidence.
- Do not turn historical examples or demand patterns into bundles, quantity rules,
  Product relationships, or automatic cross-sell.
- Do not expose protected evidence, customer data, supplier facts, or internal
  inventory quantities.
- No commercial activation follows from documentation, review, CI, or Merge.

## Open Questions

`MISSING_AUTHORITY_INPUT` — exact input: separately governed decisions and evidence
for the first bounded Product/Variant promotion, Availability mechanics, Price
authority, fulfillment, legal/commercial gates, and any per-SKU purchase activation.
It is missing because C002 remains `0/9 / NOT_READY` and C007 cannot decide those
business matters. Affected domain/document: DS-003 and linked Product/commerce
owners. Safe behavior without it: keep inquiry-only operation and all activation
gates closed.

## Founder Decisions

Recorded Founder decisions and evidence are indexed in the
[Founder Decision Log](17_FOUNDER_DECISION_LOG.md). Evidence retains its original
classification and temporal role; C007 does not convert planning or evidence into
an approved business rule.

## Future Improvements

`NOT_APPLICABLE_WITH_EVIDENCE` — future business-rule sequencing is owned by
[Project Execution Roadmap](PROJECT_EXECUTION_ROADMAP.md). Evidence: the C007
authorization denies M3 and every successor Mission. No future policy, activation,
or backlog authority is inferred here.
