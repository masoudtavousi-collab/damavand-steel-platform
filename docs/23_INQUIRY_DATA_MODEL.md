# Inquiry Data Model

## Document Control

- **Document ID:** `docs/23_INQUIRY_DATA_MODEL.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Repository Guardian
- **Approval Authority:** Founder
- **Version:** 0.2.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On inquiry type, field, consent, status, routing, attachment, notification, anti-spam, CRM, retention, or pricing-boundary change
- **Lifecycle:** Review
- **Source of Truth:** CP-005 Inquiry First, CP-006 No Public Pricing, [ADR 0001](adr/0001-inquiry-first-commerce.md), and [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md#inquiry-first-architecture)
- **Dependencies:** [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md), [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md), and [Business Rules](03_BUSINESS_RULES.md)
- **Related Documents:** [Product Taxonomy Model](21_PRODUCT_TAXONOMY_MODEL.md), [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md), [Security](10_SECURITY.md), and [Traceability Matrix](TRACEABILITY_MATRIX.md)
- **Traceability:** CP-001 through CP-006, CP-008 through CP-010, ADR-0001, WP-ARC-009, and INQ-001 through INQ-008
- **AI Compatibility:** AI-readable with explicit personal-data, no-price, and no-implementation boundaries
- **Approval:** Pending Founder approval, Sales review, security review, and privacy/legal review where applicable

## Purpose

Define the logical inquiry object, sources, types, customer fields, product lines, states, routing, notifications, anti-spam, CRM compatibility, and no-public-pricing enforcement.

## Scope

This model defines data and lifecycle policy only. It does not create a form, plugin, database table, WooCommerce setting, UI, notification, CRM integration, API, import, or code.

## Inquiry Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| INQ-001 | Use one canonical Inquiry object for general, product, multi-product, and project inquiries. | Proposed pending Founder approval |
| INQ-002 | Store inquiry product lines by stable product/variation IDs plus a submission-time label and attribute snapshot. | Proposed pending Founder approval |
| INQ-003 | Minimize customer data and require one validated contact channel plus consent evidence. | Proposed pending Founder/privacy review |
| INQ-004 | Separate Inquiry State, Sales Follow-up Status, and CRM Synchronization Status. | Proposed pending Founder/Sales approval |
| INQ-005 | Route and notify through configurable, auditable rules without exposing unnecessary personal data. | Proposed pending Founder/Sales/security approval |
| INQ-006 | Apply accessible anti-spam, abuse, attachment, and rate controls without selecting a plugin brand. | Proposed pending security/UX approval |
| INQ-007 | Enforce No Public Pricing at capture, storage, notification, analytics, API, CRM handoff, and public confirmation boundaries. | Required by CP-006 and ADR-0001 |
| INQ-008 | Govern Customer as a distinct identity object related to one or more Inquiry records while preserving immutable submission snapshots, purpose-specific consent, retention/deletion controls, and external CRM identity mappings. | Proposed pending Founder/privacy/Sales/security approval |

## Inquiry Object

| Component | Logical data | Boundary |
| --- | --- | --- |
| Identity | Stable inquiry ID and human-safe reference | Reference must not expose sequential personal or commercial information publicly |
| Type | General, Product, Multi-product, or Project | Exact Persian labels pending approval |
| Source | Source channel, page, campaign reference when approved, referrer category, language, and device class where consent permits | No uncontrolled tracking or sensitive URL capture |
| Customer | Minimum approved identity, organization, and contact data | Data minimization, access, retention, and consent apply |
| Requirements | Free-text requirements plus structured type-specific fields | No price promise or transaction acceptance |
| Product lines | Parent/variation IDs, SKU snapshot when approved, attributes, quantity/unit, and notes | Stable IDs remain authoritative; labels are submission snapshots |
| Project context | Optional/conditional project name, location, stage, schedule, specifications, and documents | Exact fields and sensitivity require approval |
| Attachments | Protected file references, metadata, scan/validation state, owner, and retention | Never unrestricted public media |
| Consent | Privacy/communication consent version, result, timestamp, and source | Legal text and consent categories pending approval |
| Routing | Queue/representative assignment, rule version, reason, timestamps, and history | No territory or priority rules invented here |
| Inquiry state | Overall inquiry lifecycle | Separate from Sales and CRM statuses |
| Sales follow-up | Assignment and follow-up progress | Internal only; exact workflow pending Sales approval |
| CRM synchronization | Future external handoff and reconciliation status | CRM is not selected and not current authority |
| Notifications | Event, recipient role, template/version, delivery outcome, retry evidence | Avoid sensitive content in email/SMS subject or body |
| Audit | Creation, validation, assignment, access, status, export, and deletion evidence | Audit access is restricted and retention-governed |

## Inquiry Source Model

| Source | Required context | Notes |
| --- | --- | --- |
| General website inquiry | Page ID/URL reference and free requirements | No product required |
| Product inquiry | Parent product ID and selected variation/attributes when applicable | Inquiry action originates from approved catalog context |
| Multi-product inquiry | One or more inquiry lines or approved structured attachment | Each resolved line uses stable product identity |
| Project inquiry | Project requirements and optional product lines/documents | Exact project fields pending Sales/domain approval |
| Representative-assisted | Representative/queue context and consented customer data | Must record actor and avoid impersonating customer submission |
| Future approved channel | Stable channel ID and ingestion evidence | Email, CRM, API, SMS, or WhatsApp ingestion requires separate approval |

UTM or campaign fields, referrers, analytics IDs, and cookies are captured only under approved analytics and consent policy.

## Customer Object

Customer is a distinct logical identity object, not an Inquiry State, WordPress user account, WooCommerce customer account, CRM record, or public profile. Creating this logical boundary does not authorize a database schema, account system, CRM, or plugin.

| Customer concern | Required architectural boundary |
| --- | --- |
| Identity | Stable internal Customer ID independent of name, phone, email, organization label, WordPress user ID, and CRM ID |
| Party type | Person and organization are distinct party types; the approved relationship between an organization and its contacts remains pending |
| Inquiry relationship | One Customer may relate to multiple Inquiry records; every Inquiry retains its submission-time customer snapshot and consent evidence |
| Unresolved identity | An Inquiry may remain linked only to a provisional identity reference until authorized matching resolves or rejects a canonical Customer link |
| Duplicate handling | Matching creates review candidates; records are not auto-merged solely by a shared name, phone, email, organization, cookie, or device identifier |
| Merge and split | Authorized review records source IDs, surviving ID, reason, actor, affected inquiries, consent impact, CRM impact, and reversal/correction evidence |
| Organization/person relationship | A person may represent an organization only through an explicit role relationship; neither party silently replaces the other |
| Consent | Consent is purpose-, text/version-, source-, and time-specific evidence related to the Customer and Inquiry; it is not a permanent blanket Customer flag |
| Retention and deletion | Customer identity, Inquiry records, consent evidence, attachments, audit evidence, and CRM mappings may have different approved retention or deletion outcomes |
| CRM identity | External CRM IDs are system-scoped mappings to the internal Customer ID and do not replace internal identity authority unless a future approved source-of-truth decision states otherwise |
| Ownership | Customer-data owner, identity reviewer, privacy approver, deletion authority, and CRM mapping owner are TODO (Founder Decision Required) |

Customer lifecycle must be separate from Inquiry, Sales Follow-up, CRM Synchronization, WordPress user, and document lifecycle. Exact Customer lifecycle states, matching thresholds, merge/split authority, organization/contact rules, retention, anonymization, deletion, restoration, and legal basis remain TODO (Founder Decision Required) and require privacy/legal review. No Customer record may be implemented from this proposal before those decisions are approved.

## Inquiry Types

### General Inquiry

Used when the requester has a requirement without selecting a catalog product. Requirements text and at least one contact channel are required.

### Product Inquiry

References one Variable Parent Product and, when selected or required, one Variation. Quantity/unit may be supplied or explicitly recorded as unknown under an approved value policy.

### Multi-Product Inquiry

Contains multiple inquiry lines. Each line records product/variation context, quantity/unit or controlled unknown state, selected attributes, and notes. A bulk attachment does not replace validation of resolved product identities.

### Project Inquiry

Captures broader project requirements, optional product lines, technical documents, location or schedule context when approved, and specialist routing. It is still an inquiry, not a quote acceptance, order, checkout, or contract.

## Customer Fields

### Required Common Fields

| Field | Requirement |
| --- | --- |
| Full name | Required unless an approved business-identity alternative is defined |
| Contact channel | At least one valid approved channel such as phone/mobile or email; all channels are not simultaneously required by architecture |
| Inquiry type and source | System-recorded and required |
| Requirements | Required free text or type-specific structured requirement |
| Consent acknowledgment | Required versioned privacy/communication acknowledgment according to approved legal policy |
| Language | Required for routing and communication; Persian is Phase 1 default |

### Conditionally Required Fields

- Product/variation identity for Product Inquiry.
- At least one inquiry line for Multi-product Inquiry.
- Project description for Project Inquiry.
- Quantity and Unit, or an explicit approved `unknown` state, for product lines.
- Attachment acknowledgment and scan state when a file is submitted.
- Organization or business identity only when an approved workflow requires it.

### Optional Fields

- Organization, role/title, alternate contact channel, preferred contact method.
- Region/location, project name, project stage, desired schedule, technical notes.
- Product line notes, alternative-acceptance preference, and approved attachments.
- Marketing consent only as a separate optional choice; it must not be bundled with required inquiry processing consent.

Exact field labels, validation, legal basis, retention, and whether fields are required remain Founder, Sales, UX, security, and privacy/legal decisions.

## Inquiry Line Model

Each line supports:

- Stable parent product ID.
- Stable variation ID when resolved.
- Parent reference and variation SKU snapshot when approved.
- Persian product/variation label snapshot.
- Selected canonical attributes and submission-time values.
- Requested quantity, Unit, or controlled unknown state.
- Customer notes and alternative/compatibility request without implying a guarantee.
- Stock-state snapshot for internal context, not a promise.
- Source page and line order.

Public price, hidden price, quote value, discount, tax, payment, shipping charge, and order data are outside the inquiry line.

## Proposed Inquiry State

| Internal state | Meaning |
| --- | --- |
| `received` | Submission accepted by the inquiry boundary and assigned a reference |
| `validation_required` | Human or controlled validation is required before routing |
| `validated` | Required data and abuse/security checks passed sufficiently for routing |
| `routed` | Assigned to an approved Sales queue or Representative |
| `in_follow_up` | Sales follow-up is active |
| `closed` | Inquiry lifecycle ended with a recorded outcome category |
| `rejected` | Invalid or ineligible inquiry with an authorized reason |
| `spam` | Classified as abuse/spam with restricted handling |

These states are proposed. Persian labels, transition authority, reopening, deletion, and outcome categories require approval.

## Proposed Sales Follow-Up Status

| Status | Meaning |
| --- | --- |
| `unassigned` | No Sales owner assigned |
| `assigned` | Sales queue or Representative assigned |
| `contact_pending` | Initial contact action pending |
| `contacted` | Contact attempt recorded |
| `awaiting_customer` | Waiting for customer information or response |
| `under_review` | Commercial/technical review underway |
| `completed` | Follow-up completed with an approved outcome category |
| `not_qualified` | Inquiry not qualified, with controlled reason |

No service-level times, scoring, priority, territory, or commercial outcome rules are invented here.

## Proposed CRM Synchronization Status

| Status | Meaning |
| --- | --- |
| `not_applicable` | No CRM handoff is required or CRM is not active |
| `pending` | Approved handoff is queued |
| `synced` | CRM acknowledged the current mapped version |
| `failed` | Handoff failed and requires controlled retry |
| `reconciliation_required` | Internal and CRM states require reviewed reconciliation |

CRM synchronization status does not replace Inquiry State or Sales Follow-up Status.

## Routing Model

- Routing uses versioned Admin-manageable rules.
- Inputs may include inquiry type, Product Family, approved location, industry/use case, language, workload, and explicit representative assignment only after those rules are approved.
- Every assignment records rule version, result, reason, actor, and timestamp.
- Unmatched, invalid, or unavailable assignments use an approved fallback queue.
- Manual reassignment records reason and history.
- Exact representatives, territories, priorities, fallback, and escalation are not defined here.

## Admin Notification

- Notify only authorized roles for relevant events.
- Include inquiry reference and minimum necessary context; sensitive fields and attachments remain behind authenticated access.
- Record notification template/version, recipient role, channel, outcome, retries, and failure visibility.
- Delivery failure must be visible in Admin and must not lose the inquiry.
- Email/SMS/WhatsApp providers, templates, recipients, and triggers require separate approval.

## Anti-Spam and Abuse Policy

- Server-side validation and normalization of all fields.
- Rate limiting and abuse thresholds with monitored false-positive handling.
- Accessible honeypot or challenge capability that preserves mobile and Persian RTL usability.
- CSRF protection, replay controls, duplicate-submission handling, and idempotent reference creation.
- Allowlisted attachment types, size limits, content validation, malware-scanning capability, randomized protected storage, and retention.
- Disposable/invalid contact and suspicious-pattern checks only under approved privacy and accuracy policy.
- Spam classification must not train or introduce an AI feature in Phase 1.
- Gravity Forms is prohibited; no form or anti-spam plugin brand is selected.

## Future CRM Integration

- Internal Inquiry ID remains stable and maps to CRM external ID.
- Versioned field mapping defines direction and source of truth per field.
- Handoff is authenticated, encrypted, idempotent, retryable, observable, and reconcilable.
- Consent, deletion, access, and retention actions propagate according to approved policy.
- CRM failures do not delete or silently mutate the internal inquiry record.
- CRM may manage follow-up after an approved authority decision but does not become product master authority.

No CRM, API, provider, connector, webhook, credentials, field mapping, or synchronization is implemented.

## No Public Pricing Enforcement

- Inquiry forms never request, calculate, display, confirm, or return a public price.
- Confirmation pages and messages do not include price, quote, discount, tax, shipping charge, payment, or checkout action.
- Public APIs, analytics, logs, notifications, attachments, caches, schema, and URLs must not leak confidential pricing.
- A customer request for price is stored as requirements text, not answered automatically.
- Commercial offers remain private future Sales/CRM/accounting documents outside the public inquiry model.
- Any future pricing or transaction behavior requires a superseding Founder decision and ADR review.

## Admin Manageability and Access

- Authorized Admin users can search, filter, assign, review, update status, add internal notes, export approved scope, and access attachments through supported interfaces when later implemented.
- Founder dashboards use clear Persian RTL labels and avoid code or database access.
- Sales and Representatives see only authorized inquiries and fields.
- Bulk status, assignment, export, and deletion actions require confirmation and audit evidence.
- Personal data is excluded from general WordPress content search, public media, SEO, and frontend caches.

## Founder Decisions

- Approve, revise, or reject INQ-001 through INQ-008.
- Approve customer fields, required/optional logic, consent, retention, and legal basis.
- Approve Customer identity, party types, inquiry cardinality, matching, merge/split, lifecycle, organization/contact relationships, retention/deletion, ownership, and CRM identity policy.
- Approve Inquiry, Sales, and CRM statuses and transitions.
- Approve routing, roles, notifications, attachments, anti-spam, and fallback policy.
- Approve future CRM authority, mapping, synchronization, and reconciliation.

## Open Questions

- Which contact channels and customer fields are required for each inquiry type?
- Which project and bulk-inquiry fields and file formats are approved?
- What are the approved statuses, outcomes, routing rules, owners, and service levels?
- What consent language, retention, deletion, and access policy applies?
- Which attachment types, sizes, storage, scanning, and expiry rules are approved?
- Which CRM, communication providers, and field mappings will be selected later?
- Which Customer lifecycle states, identity-matching evidence, duplicate-review rules, merge/split authority, organization/contact relationships, retention/deletion outcomes, and owners are approved?

## Approval Status

Review. No inquiry form, object storage, database schema, plugin, notification, anti-spam control, CRM integration, public UI, or workflow configuration is approved or created.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.2.0 | 2026-07-03 | Batch 05B remediation: distinct governed Customer object and identity, duplicate, consent, retention/deletion, and CRM mapping boundaries; documentation only. |
| 0.1.0 | 2026-07-03 | Initial Batch 05 inquiry data and lifecycle model; documentation only. |

## References

- [Enterprise Product Data Model](19_PRODUCT_DATA_MODEL.md)
- [WooCommerce Product Model](20_WOOCOMMERCE_PRODUCT_MODEL.md)
- [Product Attribute Model](22_PRODUCT_ATTRIBUTE_MODEL.md)
- [ADR 0001](adr/0001-inquiry-first-commerce.md)

## Navigation

- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Product Data Reading Path](READING_ORDER.md#product-data-and-woocommerce-reading-path)
