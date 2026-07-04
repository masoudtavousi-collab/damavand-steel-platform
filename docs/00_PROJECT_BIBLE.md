# DS-000 Project Bible

## Table of Contents

- [Purpose](#purpose)
- [Core Project Principles](#core-project-principles)
- [Rule Traceability](#rule-traceability)
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

Defines the governing purpose of the Project Bible within the project documentation set.

## Core Project Principles

- **Authority:** Authoritative Founder Directive
- **Decision Status:** Accepted
- **Origin:** Batch 02A Governance Remediation, 2026-07-03
- **Change Control:** A change requires an explicit Founder decision and corresponding traceability update.

| Rule ID | Core Project Principle | Authoritative rule |
| --- | --- | --- |
| CP-001 | Plugin First | Prefer approved plugins over custom development. |
| CP-002 | Configuration First | Prefer supported configuration over custom code. |
| CP-003 | Mobile First | Mobile-first behavior is a governing requirement. |
| CP-004 | Persian RTL | Persian RTL is a governing requirement. |
| CP-005 | Inquiry First | The commercial interaction model is inquiry-first. |
| CP-006 | No Public Pricing | Public pricing must not be introduced. |
| CP-007 | No Custom Theme | A custom theme must not be introduced. |
| CP-008 | No Gravity Forms | Gravity Forms must not be introduced. |
| CP-009 | No LiteSpeed Cache | LiteSpeed Cache must not be introduced. |
| CP-010 | No AI Features (Phase 1) | AI features must not be introduced in Phase 1. |

These principles define constraints only. They do not select plugins, create product taxonomy, configure WooCommerce, or authorize implementation.

The Core Project Principles are authoritative because they originate from an explicit Founder directive. Other unfinished sections of this document remain Draft and do not gain approval through this section.

## Rule Traceability

| Rule ID | Origin document | Referenced governing documents | Dependent documents |
| --- | --- | --- | --- |
| CP-001 | This document | [Constitution](01_PROJECT_CONSTITUTION.md), [Architecture](02_ARCHITECTURE.md), [Business Rules](03_BUSINESS_RULES.md), [Technology Stack](05_TECH_STACK.md), [Repository Standards](07_REPOSITORY_GUIDE.md), [Quality Standard](16_QUALITY_STANDARD.md) | [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [Development Workflow](08_DEVELOPMENT_WORKFLOW.md), [Testing Strategy](13_TESTING_STRATEGY.md) |
| CP-002 | This document | [Constitution](01_PROJECT_CONSTITUTION.md), [Architecture](02_ARCHITECTURE.md), [Business Rules](03_BUSINESS_RULES.md), [Technology Stack](05_TECH_STACK.md), [Repository Standards](07_REPOSITORY_GUIDE.md), [Quality Standard](16_QUALITY_STANDARD.md) | [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [Deployment](09_DEPLOYMENT.md), [Security](10_SECURITY.md) |
| CP-003 | This document | [Constitution](01_PROJECT_CONSTITUTION.md), [Architecture](02_ARCHITECTURE.md), [Business Rules](03_BUSINESS_RULES.md), [Technology Stack](05_TECH_STACK.md), [Repository Standards](07_REPOSITORY_GUIDE.md), [Quality Standard](16_QUALITY_STANDARD.md) | [UX Principles](12_UX_PRINCIPLES.md), [SEO Strategy](11_SEO_STRATEGY.md), [Testing Strategy](13_TESTING_STRATEGY.md) |
| CP-004 | This document | [Constitution](01_PROJECT_CONSTITUTION.md), [Architecture](02_ARCHITECTURE.md), [Business Rules](03_BUSINESS_RULES.md), [Technology Stack](05_TECH_STACK.md), [Repository Standards](07_REPOSITORY_GUIDE.md), [Quality Standard](16_QUALITY_STANDARD.md) | [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [Content Operations](content/README.md), [UX Principles](12_UX_PRINCIPLES.md), [Testing Strategy](13_TESTING_STRATEGY.md) |
| CP-005 | This document and [ADR 0001](adr/0001-inquiry-first-commerce.md) | [Constitution](01_PROJECT_CONSTITUTION.md), [Architecture](02_ARCHITECTURE.md), [Business Rules](03_BUSINESS_RULES.md), [Technology Stack](05_TECH_STACK.md), [Repository Standards](07_REPOSITORY_GUIDE.md), [Quality Standard](16_QUALITY_STANDARD.md) | [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md), [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [SEO Strategy](11_SEO_STRATEGY.md), [Testing Strategy](13_TESTING_STRATEGY.md) |
| CP-006 | This document and [ADR 0001](adr/0001-inquiry-first-commerce.md) | [Constitution](01_PROJECT_CONSTITUTION.md), [Architecture](02_ARCHITECTURE.md), [Business Rules](03_BUSINESS_RULES.md), [Technology Stack](05_TECH_STACK.md), [Repository Standards](07_REPOSITORY_GUIDE.md), [Quality Standard](16_QUALITY_STANDARD.md) | [Product Data Strategy](04_PRODUCT_DATA_STRATEGY.md), [Content Operations](content/README.md), [SEO Strategy](11_SEO_STRATEGY.md), [Testing Strategy](13_TESTING_STRATEGY.md) |
| CP-007 | This document | [Constitution](01_PROJECT_CONSTITUTION.md), [Architecture](02_ARCHITECTURE.md), [Business Rules](03_BUSINESS_RULES.md), [Technology Stack](05_TECH_STACK.md), [Repository Standards](07_REPOSITORY_GUIDE.md), [Quality Standard](16_QUALITY_STANDARD.md) | [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [Development Workflow](08_DEVELOPMENT_WORKFLOW.md), [Testing Strategy](13_TESTING_STRATEGY.md) |
| CP-008 | This document | [Constitution](01_PROJECT_CONSTITUTION.md), [Architecture](02_ARCHITECTURE.md), [Business Rules](03_BUSINESS_RULES.md), [Technology Stack](05_TECH_STACK.md), [Repository Standards](07_REPOSITORY_GUIDE.md), [Quality Standard](16_QUALITY_STANDARD.md) | [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [Security](10_SECURITY.md), [Testing Strategy](13_TESTING_STRATEGY.md) |
| CP-009 | This document | [Constitution](01_PROJECT_CONSTITUTION.md), [Architecture](02_ARCHITECTURE.md), [Business Rules](03_BUSINESS_RULES.md), [Technology Stack](05_TECH_STACK.md), [Repository Standards](07_REPOSITORY_GUIDE.md), [Quality Standard](16_QUALITY_STANDARD.md) | [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [Deployment](09_DEPLOYMENT.md), [Performance Checklist](../quality/PERFORMANCE_CHECKLIST.md) |
| CP-010 | This document | [Constitution](01_PROJECT_CONSTITUTION.md), [Architecture](02_ARCHITECTURE.md), [Business Rules](03_BUSINESS_RULES.md), [Technology Stack](05_TECH_STACK.md), [Repository Standards](07_REPOSITORY_GUIDE.md), [Quality Standard](16_QUALITY_STANDARD.md) | [WordPress Architecture](06_WORDPRESS_ARCHITECTURE.md), [Development Workflow](08_DEVELOPMENT_WORKFLOW.md), [Testing Strategy](13_TESTING_STRATEGY.md) |

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

- [DS-001 Project Constitution](01_PROJECT_CONSTITUTION.md)
- [Documentation Index](08_DOCUMENTATION_INDEX.md)
- [Decision Log](10_DECISION_LOG.md)
- [Founder Decision Log](17_FOUNDER_DECISION_LOG.md)
- [Rule Traceability](#rule-traceability)
- [Repository Traceability Matrix](TRACEABILITY_MATRIX.md)
- [AI Collaboration Standard](AI_COLLABORATION.md)

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
