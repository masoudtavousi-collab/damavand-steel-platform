# Enterprise Architecture Checklist

## Purpose

Assess whether an architecture change is explicit, traceable, reviewable, and maintainable without prescribing a project architecture.

## Scope

Applies to proposed or changed system boundaries, components, integrations, data flows, infrastructure, and cross-cutting concerns.

## Owner

TODO (Owner Assignment Required)

## Status

Draft

## Checklist

- [ ] The architecture change traces to an approved requirement or decision request.
- [ ] System boundaries and external dependencies are identified.
- [ ] Component responsibilities and ownership boundaries are explicit.
- [ ] Relevant quality attributes and trade-offs are documented.
- [ ] Data flows, trust boundaries, and sensitive-data paths are represented.
- [ ] Failure modes, degraded behavior, and recovery expectations are considered.
- [ ] Security, privacy, operability, and maintainability impacts are reviewed.
- [ ] Scalability assumptions and capacity-sensitive elements are identified.
- [ ] Observability needs are defined at affected boundaries.
- [ ] Reversibility, migration, and rollback implications are assessed.
- [ ] Significant decisions are captured through the approved decision-record process.
- [ ] The proposal introduces no undocumented business rule or platform decision.

## Pass Criteria

The architecture change is decision-traceable, internally coherent, testable, operationally reviewable, and free of undocumented assumptions.

## Fail Criteria

The review fails when boundaries, trade-offs, data flows, risks, decision authority, or verification paths are missing or contradictory.

## References

- [Enterprise Quality Standard](QUALITY_STANDARD.md)
- [DS-002 Enterprise Architecture](../docs/02_ARCHITECTURE.md)
- [Architecture Decision Records](../docs/adr/README.md)
- [Security Checklist](SECURITY_CHECKLIST.md)
- [Performance Checklist](PERFORMANCE_CHECKLIST.md)
