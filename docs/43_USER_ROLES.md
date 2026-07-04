# Enterprise User Roles Blueprint

## Document Control

- **Document ID:** `docs/43_USER_ROLES.md` (provisional path identifier)
- **Status:** Review
- **Authority:** Proposed Governing
- **Owner:** Founder
- **Reviewer:** Lead Enterprise Solution Architect
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-03
- **Last Review:** 2026-07-03
- **Review Cycle:** On role, capability, workflow, ownership, privacy, security, integration, or administration change
- **Lifecycle:** Review
- **Source of Truth:** [Project Constitution](01_PROJECT_CONSTITUTION.md), [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [Entity Relationship Model](30_ENTITY_RELATIONSHIP_MODEL.md), and [WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md)
- **Dependencies:** [Content Architecture](29_CONTENT_ARCHITECTURE.md), [Inquiry Workflow](42_INQUIRY_WORKFLOW.md), [WooCommerce Configuration](38_WOOCOMMERCE_CONFIGURATION.md), and [Custom Fields Model](41_CUSTOM_FIELDS_MODEL.md)
- **Related Documents:** [Review Process](15_REVIEW_PROCESS.md), [Security](10_SECURITY.md), [Elementor Architecture](37_ELEMENTOR_ARCHITECTURE.md), and [Plugin Responsibility Matrix](44_PLUGIN_RESPONSIBILITY_MATRIX.md)
- **Traceability:** CP-001 through CP-010, WP-FC-005, WPBP-002, WPBP-005 through WPBP-007, INQWF-004 through INQWF-011, and ROLE-001 through ROLE-009
- **AI Compatibility:** AI-readable Blueprint; no AI identity, role, or automation is authorized
- **Approval:** Pending Founder/security/privacy/operational approval; no WordPress role or capability is authorized

## Purpose

Define logical enterprise role bundles, responsibilities, visibility, workflow ownership, and administration without creating WordPress roles or capabilities.

## Scope and Boundary

Roles are least-privilege responsibility bundles, not necessarily separate accounts or WordPress role slugs. The Founder may combine or delegate compatible bundles after segregation-of-duty review. This document grants no access and cannot delegate Founder approval authority.

## Role Decisions

| ID | Proposed decision | Status |
| --- | --- | --- |
| ROLE-001 | Separate repository/Founder approval authority from WordPress operational capabilities. | Required by governance authority |
| ROLE-002 | Grant least privilege by task, data scope, lifecycle transition, environment, and time; deny by default. | Proposed pending Founder/security approval |
| ROLE-003 | Use role bundles for Founder, Administrator, Editor, SEO Manager, Sales, Representative, Customer, and Guest as identified by WordPress Architecture. | Derived from WordPress Architecture; exact capabilities pending |
| ROLE-004 | Add specialized operational bundles only where product, taxonomy, content, media, inquiry, privacy, or release duties require separation. | Proposed pending Founder approval |
| ROLE-005 | Protect Inquiry, Customer, Representative, integration, security, and audit data by assignment and purpose. | Required by privacy/security boundaries |
| ROLE-006 | Require dual review or explicit approval for high-impact publication, role, plugin, configuration, import, deletion, and release actions. | Proposed pending Founder/security approval |
| ROLE-007 | Keep normal Founder and delegated administration manageable through WordPress Admin without code/CLI. | Required by WP-FC-005 |
| ROLE-008 | Review access at onboarding, responsibility change, incident, inactivity, and offboarding; preserve audit evidence. | Proposed pending Founder/security approval |
| ROLE-009 | Future CRM roles map explicitly to local identities and scopes; they do not inherit unrestricted WordPress access. | Proposed pending Founder/Sales/security approval |

## Core Role Catalog

| Logical role | Responsibilities | Visibility and workflow ownership | Explicit boundary |
| --- | --- | --- | --- |
| Founder | Approve governing decisions; assign owners; accept high-impact changes | Repository-wide decision context; operational access only as needed | WordPress role cannot transfer Founder authority |
| Administrator | Maintain approved WordPress configuration and users | Platform configuration within approved change/release process | Cannot invent business rules or edit vendor/core files |
| Editor | Govern approved editorial content lifecycle | Assigned public content, media references, reviews | No product schema, roles, plugins, protected inquiry data, or technical settings by default |
| SEO Manager | Govern approved SEO projections, canonicals, indexation, redirects, schema coordination | Public eligible content/entity SEO fields and evidence | Cannot change source facts, create taxonomy, expose prices, or override owners |
| Sales | Validate, assign, follow up, and close permitted inquiries | Assigned/authorized Inquiry and Customer context | No platform configuration, public pricing, broad export, or Founder authority |
| Representative | Act on assigned inquiry scope and approved representative data | Assigned inquiries and permitted profile/scope | No other representative/customer data or routing-rule ownership |
| Customer | Future optional authenticated self-service role | Only own approved records/actions | Not active or required in current public journey |
| Guest / Visitor | Browse approved public content and submit inquiry | Public data and own submission/confirmation | No protected data, Admin, price, cart, or checkout access |

## Specialized Operational Bundles

These may be combined with core roles; none is approved as a distinct WordPress role yet.

| Bundle | Responsibilities | Visibility | Workflow ownership |
| --- | --- | --- | --- |
| Product Data Manager | Maintain approved parents, variations, SKUs, attributes, availability, documents | Catalog records and approved source evidence | Product draft/review readiness; not Founder approval |
| Taxonomy and Attribute Manager | Govern approved registries and term requests | Terms, mappings, affected usage | Term proposal/change workflow |
| Content Manager | Coordinate inventory, assignment, review, reuse, expiry | Assigned editorial content and relationships | Content planning/review/publication as delegated |
| Media Manager | Rights, accessibility, variants, replacements, access | Approved media/document metadata | Media validation and lifecycle |
| Inquiry Manager | Validation queue, assignment, exceptions, escalation | Authorized Inquiry/Customer scope | Inquiry routing and operational recovery |
| Privacy and Security Reviewer | Review access, consent, retention, incidents, protected exposure | Minimum evidence needed for review | Privacy/security gate; not routine Sales ownership |
| Technical/Release Administrator | Plugins, configuration promotion, backups, rollback, releases | Technical configuration and operational evidence | Controlled technical change and release |
| Domain/Technical Reviewer | Validate steel/product facts and technical documents | Assigned source/evidence | Domain review only; no platform administration by default |

## Permissions Model

Permissions are decomposed into view, create, edit own, edit assigned, edit all in scope, transition, publish, suspend, archive, delete, export, import, assign, configure, manage users, and review audit evidence. Each capability requires object scope and field-level restrictions where protected data exists. Exact WordPress capabilities remain unselected.

## Responsibilities and Workflow Ownership

- Product, taxonomy, content, media, SEO, Inquiry, privacy/security, and technical release each have one accountable owner and named reviewers.
- Configuration owners implement approved settings but do not approve the business decision they encode.
- Publication does not grant taxonomy, schema, plugin, role, or release rights implicitly.
- Assignment does not grant access outside the assigned records or relationship scope.

## Visibility

Visibility follows data access class: public, authenticated, assigned/protected, internal, integration-only, secret, or evidence-limited. Search, lists, exports, email, notifications, APIs, logs, backups, and support access must enforce the same boundary. Secrets are not WordPress content.

## Administration

- Use named accounts, strong authentication, least privilege, and no shared operational credentials.
- Record role request, approver, purpose, scope, start/review/end dates, changes, and revocation.
- Separate everyday accounts from privileged technical access where supported.
- Test denied paths, not only allowed paths; review dormant and emergency access.
- Exact MFA, session, password, approval, emergency, and audit policies remain pending Security completion.

## Future CRM Roles

Future CRM roles may include Sales coordinator, Representative, Sales manager, quotation reviewer, and integration service identity. Mapping requires stable identity, least scope, source authority, conflict resolution, provisioning/deprovisioning, sync failure, audit, privacy, export, and incident rules. CRM selection and integration are not authorized.

## Founder Decisions

- Approve, revise, or reject ROLE-001 through ROLE-009.
- Approve which specialized bundles become separate roles and which compatible duties may be combined.
- Approve exact capability/object/field/transition matrix, segregation of duties, access reviews, emergency access, and authentication policy.
- Assign operational owners and reviewers, including future CRM mappings.

## Open Questions

- Which people or delegated functions fill each role bundle in each environment?
- Which actions require dual control, Founder approval, or technical/security review?
- What field/object scopes apply to Sales, Representatives, SEO, support, and technical administrators?
- Are customer accounts needed, and what future CRM role mappings are approved?

## Approval Status

Review. No WordPress role, capability, user, account, authentication rule, CRM role, permission, or access configuration is created or changed.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-03 | Initial Batch 08 enterprise user roles Blueprint; documentation only. |

## Related Documents

- [WordPress Solution Blueprint](35_WORDPRESS_BLUEPRINT.md)
- [Inquiry Workflow](42_INQUIRY_WORKFLOW.md)
- [Review Process](15_REVIEW_PROCESS.md)
- [Security](10_SECURITY.md)

## Traceability

| Decision range | Origin | Dependent documents | Future evidence |
| --- | --- | --- | --- |
| ROLE-001–ROLE-009 | CP-001–CP-010, WP-FC-005, governance authority, content/product/inquiry ownership | CPT, fields, inquiry, plugins, security, deployment, and future access configuration plan | Role-capability-field matrix, owner assignments, segregation review, allowed/denied tests, Admin walkthrough, access-review and revocation evidence |

Implementation status: `Not authorized`.
