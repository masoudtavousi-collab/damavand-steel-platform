# DS-004 Technology Stack

## Table of Contents

- [Purpose](#purpose)
- [Core Technology Constraints](#core-technology-constraints)
- [WordPress Platform Constraints](#wordpress-platform-constraints)
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

Defines the governing purpose of the Technology Stack document within the project documentation set.

## Core Technology Constraints

Technology selection and configuration are governed by the authoritative [Core Project Principles](00_PROJECT_BIBLE.md#core-project-principles).

| Rule ID | Technology constraint |
| --- | --- |
| CP-001 | Plugin First applies before custom development is considered. |
| CP-002 | Configuration First applies before custom code is considered. |
| CP-003 | Technology choices must preserve Mobile First. |
| CP-004 | Technology choices must preserve Persian RTL. |
| CP-005 | Technology choices must preserve Inquiry First. |
| CP-006 | Technology choices must preserve No Public Pricing. |
| CP-007 | Technology choices must preserve No Custom Theme. |
| CP-008 | Gravity Forms is excluded. |
| CP-009 | LiteSpeed Cache is excluded. |
| CP-010 | AI Features are excluded from Phase 1. |

This section records constraints only and does not approve a plugin, theme, form system, cache system, AI capability, or WordPress configuration.

## WordPress Platform Constraints

The explicit Batch 04 Founder directive establishes the following WordPress-scoped platform constraints. They do not approve installation, versions, configuration, licenses, or additional plugin brands.

| Decision ID | Platform constraint | Scope |
| --- | --- | --- |
| WP-FC-001 | WooCommerce | Product catalog authority within ADR-0001 Inquiry First and No Public Pricing boundaries |
| WP-FC-002 | Blocksy Pro | Vendor-controlled presentation shell under CP-007 No Custom Theme |
| WP-FC-003 | Elementor Pro | Admin-managed visual composition within explicit template ownership boundaries |
| WP-FC-004 | Variable Parent Product | Required WooCommerce product architecture |
| WP-FC-005 | Founder Admin Manageability | Routine management must use supported WordPress Admin capabilities whenever possible |

The detailed ownership and compatibility boundaries are defined in [WordPress Enterprise Architecture](06_WORDPRESS_ARCHITECTURE.md). All other plugin brands and exact version selections remain undecided.

## Scope

TODO (Founder Decision Required)

## Audience

TODO (Founder Decision Required)

## Status

Draft

## Owner

Founder

## Reviewer

Repository Guardian

## Approval Authority

Founder

## Version

0.1.0

## Last Updated

2026-07-03

## Last Review

2026-07-03

## Related Documents

- [DS-002 Enterprise Architecture](02_ARCHITECTURE.md)
- [DS-005 Repository Standards](07_REPOSITORY_GUIDE.md)
- [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md)
- [Decision Log](10_DECISION_LOG.md)
- [Open Questions](18_OPEN_QUESTIONS.md)

## Overview

This section will provide the approved overview for this document.

TODO (Founder Decision Required)

## Definitions

TODO (Founder Decision Required)

## Responsibilities

TODO (Founder Decision Required)

## Decisions

TODO (Founder Decision Required)

## Constraints

TODO (Founder Decision Required)

## Open Questions

TODO (Founder Decision Required)

## Founder Decisions

TODO (Founder Decision Required)

## Future Improvements

TODO (Founder Decision Required)
