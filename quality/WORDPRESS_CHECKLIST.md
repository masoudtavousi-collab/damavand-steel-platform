# WordPress Quality Checklist

## Purpose

Provide a reusable review standard for WordPress compatibility, configuration, security, and maintainability.

## Scope

Applies to WordPress core integration, configuration, themes, plugins, content behavior, and operational changes.

## Owner

TODO (Owner Assignment Required)

## Status

Draft

## Checklist

- [ ] Supported WordPress, PHP, database, and web-server versions are recorded in an approved compatibility matrix.
- [ ] Environment-specific configuration is separated from source code and secrets.
- [ ] WordPress core and third-party files are not modified directly.
- [ ] Public WordPress APIs, hooks, and coding standards are used where applicable.
- [ ] Input handling, output escaping, capability checks, and nonce protections are reviewed.
- [ ] Localization, text direction, encoding, and translation behavior meet approved requirements.
- [ ] Scheduled work and background processing have an operational owner and monitoring path.
- [ ] File permissions, uploads, generated assets, and writable paths are controlled.
- [ ] Update, rollback, and database-migration behavior is documented and testable.
- [ ] Production debugging and error-display behavior follow the approved environment policy.
- [ ] Cache behavior and invalidation are reviewed for affected content and users.
- [ ] WordPress Site Health and relevant runtime diagnostics show no unexplained critical issue.

## Pass Criteria

The change is compatible with the approved WordPress platform matrix and meets applicable configuration, security, localization, update, and operational standards.

## Fail Criteria

The review fails when platform support is unknown, core files are altered, required safeguards are absent, or runtime compatibility lacks evidence.

## References

- [Enterprise Quality Standard](QUALITY_STANDARD.md)
- [WordPress Architecture](../docs/06_WORDPRESS_ARCHITECTURE.md)
- [WordPress Requirements](https://wordpress.org/about/requirements/)
- [WordPress Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/)
- [WordPress Hardening Guide](https://developer.wordpress.org/advanced-administration/security/hardening/)
