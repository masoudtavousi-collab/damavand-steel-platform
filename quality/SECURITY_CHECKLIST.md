# Enterprise Security Checklist

## Purpose

Provide a reusable review standard for application, infrastructure, supply-chain, and operational security.

## Scope

Applies to code, configuration, dependencies, identities, data, integrations, uploads, deployment, logging, and incident readiness.

## Owner

TODO (Owner Assignment Required)

## Status

Draft

## Checklist

- [ ] Threats, trust boundaries, assets, and abuse cases are reviewed for the change.
- [ ] Data classification, collection, retention, access, and deletion expectations are traceable.
- [ ] Least-privilege access and separation of duties are preserved.
- [ ] Authentication, authorization, session, and administrative controls are appropriate to the affected surface.
- [ ] Secrets are externally managed, rotated, and absent from source and review output.
- [ ] Secure defaults and environment-specific hardening are documented.
- [ ] Inputs, outputs, file paths, redirects, and external requests are safely handled.
- [ ] Dependencies and artifacts have approved provenance and vulnerability review evidence.
- [ ] HTTPS, security headers, cookies, and transport protections are verified where applicable.
- [ ] Uploads and generated files are constrained by type, size, location, execution, and scanning policy.
- [ ] Logs and telemetry support investigation without exposing protected information.
- [ ] Backup confidentiality, integrity, restoration, and access controls are verified.
- [ ] Incident detection, escalation, containment, recovery, and communication paths are current.
- [ ] Accepted risks and temporary exceptions have explicit expiry or review dates.

## Pass Criteria

Applicable threats and controls are evidenced, sensitive data is protected, supply-chain risks are reviewed, and no unaccepted blocking security finding remains.

## Fail Criteria

The review fails when a material threat is untreated, access is excessive, secrets or protected data are exposed, provenance is unknown, or a required security control lacks evidence.

## References

- [Enterprise Quality Standard](QUALITY_STANDARD.md)
- [Security Documentation](../docs/10_SECURITY.md)
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [WordPress Hardening Guide](https://developer.wordpress.org/advanced-administration/security/hardening/)
