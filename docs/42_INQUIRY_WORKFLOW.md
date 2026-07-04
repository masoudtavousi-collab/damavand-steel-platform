# Enterprise Inquiry Workflow Blueprint

## Document Control

- **Document ID:** `docs/42_INQUIRY_WORKFLOW.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Solution Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On inquiry, customer, assignment, representative, quotation, follow-up, notification, permission, escalation, retention, CRM, or privacy change
- **Lifecycle:** Review
- **Source of Truth:** [Business Rules](03_BUSINESS_RULES.md), [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md), and [ADR-0001](adr/0001-inquiry-first-commerce.md)
- **Dependencies:** [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md), [WooCommerce Configuration](38_WOOCOMMERCE_CONFIGURATION.md), and [Custom Fields Model](41_CUSTOM_FIELDS_MODEL.md)
- **Related Documents:** [Product Data Model](19_PRODUCT_DATA_MODEL.md), [Site Structure](25_SITE_STRUCTURE.md), [User Roles](43_USER_ROLES.md), [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md), and [Security](10_SECURITY.md)
- **Traceability:** CP-001 through CP-006, CP-008 through CP-010, ADR-0001, INQ-001 through INQ-008, WCCFG-003 through WCCFG-012, and INQWF-001 through INQWF-011
- **AI Compatibility:** AI-readable Blueprint; no AI feature, automation, form, or inquiry configuration is authorized
- **Approval:** Pending Founder/Sales/security/privacy approval; no inquiry implementation is authorized

## Purpose

Define the complete human-governed Inquiry lifecycle, roles, statuses, notifications, permissions, and escalation boundaries without selecting or configuring a form, CRM, or workflow system.

## Scope and Boundary

This Blueprint covers Visitor through archival and includes Product, Multi-product, Project, and General inquiries. It does not approve exact fields, consent text, recipients, routing rules, service levels, quotation content, retention, CRM integration, public pricing, automation, or storage technology.

## Inquiry Workflow Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| INQWF-001 | Every public commercial journey uses the canonical Inquiry object and never public checkout. | Required by CP-006 and ADR-0001 |
| INQWF-002 | Capture only approved minimum data and explicit source/product context with clear validation and consent. | Derived from INQ-001 through INQ-008 |
| INQWF-003 | Separate Inquiry lifecycle, Sales follow-up, CRM synchronization, and future Quotation states. | Proposed pending Founder/Sales approval |
| INQWF-004 | Validate before assignment; preserve immutable source evidence and auditable status transitions. | Proposed pending Founder/Sales/security approval |
| INQWF-005 | Route to an authorized Sales/Representative owner only through approved rules, with manual recovery. | Proposed pending Founder/Sales approval |
| INQWF-006 | Keep Inquiry/Customer/attachment data protected and visible by least privilege. | Required by security/privacy boundaries |
| INQWF-007 | Treat a future Quotation as a protected, versioned subprocess; it is not public pricing or WooCommerce checkout. | Proposed pending Founder approval |
| INQWF-008 | Notifications signal work but do not become the canonical Inquiry record or expose sensitive details unnecessarily. | Proposed pending Founder/security approval |
| INQWF-009 | Escalation uses approved time/event thresholds, accountable owners, and failure visibility; no service level is invented here. | Proposed pending Founder/Sales approval |
| INQWF-010 | Completion and archive require outcome, retention, access, and relationship rules; archive is not deletion. | Proposed pending Founder/privacy approval |
| INQWF-011 | Use an approved Plugin First capability, excluding Gravity Forms, and preserve Admin manageability and exportability. | Required by CP-001, CP-002, CP-008, and WP-FC-005 |

## Lifecycle Overview

```text
Visitor context
  -> Inquiry submitted
    -> received
      -> validation_required -> validated | rejected | spam
        -> routed
          -> assigned follow-up
            -> in_follow_up
              -> completed/closed | not_qualified/closed
                -> retained archive or approved deletion/anonymization path
```

The canonical Inquiry states remain `received`, `validation_required`, `validated`, `routed`, `in_follow_up`, `closed`, `rejected`, and `spam`. Sales follow-up states remain `unassigned`, `assigned`, `contact_pending`, `contacted`, `awaiting_customer`, `under_review`, `completed`, and `not_qualified`. CRM synchronization remains a separate optional future state.

## Visitor

- Enters through an approved product, multi-product, project, general, representative, landing, knowledge, or support context.
- Receives Persian RTL, mobile-accessible purpose, required-field, consent/privacy, attachment, response-expectation, and error guidance.
- Can verify selected Product/Variation/context before submission.
- Does not see a public price, quote result, cart, checkout, payment, or transaction claim.

## Inquiry Capture

The future capture surface creates one canonical Inquiry ID, timestamp, source, type, permitted Customer fields, consent evidence, context lines, and validation state. Server-side validation, spam controls, safe attachment handling, rate limits, failure recovery, and duplicate handling require security approval. Exact fields remain governed by the Inquiry Data Model.

## Validation

Authorized validation confirms minimum fields, contact format, context integrity, consent, attachment safety, duplicate/spam indicators, access, and routing eligibility. Validation does not qualify commercial value, promise availability, or infer missing product facts. Invalid records follow explicit correction, rejection, or spam handling with audit evidence.

## Assignment

Assignment records assignee role/entity, reason/rule, timestamp, assigner, state, and reassignment history. A fallback queue and manual assignment must exist before automated routing is trusted. Exact territories, families, industries, workload rules, and service thresholds remain pending.

## Representative

A Representative may receive only inquiries within approved scope and permissions. Public representative selection, automatic assignment, profile visibility, coverage, absence/backup, reassignment, data export, and CRM identity remain unresolved. Representative access never grants Founder approval or unrestricted customer access.

## Quotation

A future private Quotation may begin only from an authorized validated Inquiry. It requires its own ID, owner, version, protected line items, commercial approvals, validity, status, delivery evidence, access, acceptance/rejection, expiry, and retention. No quotation workflow or pricing engine is implemented or approved here.

## Follow-up

Sales follow-up records current owner, state, next action, due event/time if approved, contact evidence, outcome, and permitted notes. It must distinguish facts from internal notes and avoid sensitive or excessive personal data. Customer communication channels and templates remain pending.

## Completion

Completion requires an approved outcome such as `completed` or `not_qualified`, resolution evidence, unresolved-task handling, relationship updates, and owner sign-off. `closed` is the Inquiry lifecycle state and does not imply a sale, order, payment, or public commercial record.

## Archive

Closed/rejected/spam records follow approved retention, legal hold, deletion/anonymization, attachment, audit, backup, CRM, and access rules. No retention duration is defined. Archive removes operational visibility as approved but preserves required evidence and does not silently break entity references.

## Notifications

| Event family | Intended recipient class | Boundary |
| --- | --- | --- |
| Submission receipt | Visitor/customer contact | No price/availability promise; exact content pending |
| Validation failure/recovery | Authorized Inquiry operator | Minimum protected detail; secure record link preferred |
| Assignment/reassignment | Assignee and responsible queue | No broad distribution |
| Follow-up/escalation due | Assigned Sales/manager role | Threshold and recipient pending |
| Delivery/system failure | Technical operator and workflow owner | Retry/failure evidence required |
| Closure | Authorized Sales/customer as approved | Outcome wording and privacy pending |

Email is a notification channel, not the record authority. Outbound delivery requires an approved mail capability; WordPress native mail is not assumed reliable.

## Status Model

Transitions must record previous/new state, actor, timestamp, reason, validation, and related assignment/follow-up/CRM state. Only approved transitions are allowed; reopening requires a governed reason and preserves history. Inquiry, Sales, CRM, and Quotation status names cannot be conflated.

## Permissions

- Visitor: submit and receive approved confirmation only.
- Inquiry Manager/Sales: view and update assigned/permitted inquiries and follow-up.
- Representative: view and act only on assigned scope.
- Privacy/Security reviewer: access only for authorized review or incident handling.
- Technical administrator: maintain capability without routine content access unless explicitly needed and audited.
- Founder: approval authority; operational access still follows least privilege.

Exact WordPress capabilities are not defined.

## Escalation

Escalation may respond to unvalidated, unassigned, overdue, delivery-failed, repeated-reassignment, integration-failed, security, privacy, or attachment events. Each requires an approved threshold, severity, recipient, backup owner, channel, acknowledgement, resolution, and audit. No automated decision or AI routing is authorized.

## Founder Decisions

- Approve, revise, or reject INQWF-001 through INQWF-011.
- Approve exact fields, consent, validation, spam, attachments, routing, roles, statuses, transitions, notifications, service thresholds, retention, deletion, and reopening.
- Approve representative involvement and any future private Quotation/CRM mapping separately.
- Select an inquiry capability through Plugin First review; Gravity Forms remains prohibited.

## Open Questions

- What minimum data, consent, attachments, anti-spam controls, and response expectations are approved?
- Which Sales/Representative routing, assignment, fallback, escalation, and service thresholds apply?
- Who may view/change/export each protected field and status?
- What retention, deletion/anonymization, CRM sync, notification, and failure-recovery policies apply?

## Approval Status

Review. No form, inquiry record, route, status, notification, role capability, quotation, CRM integration, automation, retention job, plugin, or setting is created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 08 Inquiry workflow Blueprint; documentation only. |

## Related Documents

- [Inquiry Data Model](23_INQUIRY_DATA_MODEL.md)
- [WooCommerce Configuration](38_WOOCOMMERCE_CONFIGURATION.md)
- [User Roles](43_USER_ROLES.md)
- [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| INQWF-001–INQWF-011 | CP-001–CP-006, CP-008–CP-010, ADR-0001, INQ/WCCFG rules | Roles, plugin selection, mail/security/privacy, CRM/quotation, and future workflow configuration plan | Field/status/transition/permission matrix, threat/privacy review, routing and notification tests, failure recovery, RTL/mobile/accessibility/Admin walkthrough, no-price validation |

Implementation status: `Not authorized`.
