# Sprint 01B WordPress Baseline

## Document Control

- **Document ID:** `repository/config/WORDPRESS_BASELINE.md`
- **Status:** Review
- **Authority:** Evidence Record
- **Owner:** Founder
- **Reviewer:** Build Engineer
- **Approval Authority:** Founder
- **Version:** 0.1.0
- **Last Updated:** 2026-07-04
- **Last Review:** 2026-07-04
- **Review Cycle:** On WordPress files, database, permalink, upload, theme, plugin, environment, or limitation change
- **Lifecycle:** Review
- **Source of Truth:** Current `public/` and `public/wp-content/` filesystem plus read-only local runtime checks observed on 2026-07-04
- **Dependencies:** [Environment Report](ENVIRONMENT_REPORT.md), [Plugin Inventory](PLUGIN_INVENTORY.md), [Pre-Implementation Checklist](../PRE_IMPLEMENTATION_CHECKLIST.md), and [WordPress Solution Blueprint](../../docs/35_WORDPRESS_BLUEPRINT.md)
- **Related Documents:** [WooCommerce Blueprint](../../docs/38_WOOCOMMERCE_CONFIGURATION.md), [Blocksy Blueprint](../../docs/36_BLOCKSY_CONFIGURATION.md), [Elementor Blueprint](../../docs/37_ELEMENTOR_ARCHITECTURE.md), and [Sprint 01B Audit](../../docs/AUDIT_REPORT_SPRINT01B.md)
- **Traceability:** CP-001 through CP-010, ADR-0001, WP-FC-001 through WP-FC-005, WPBP-001 through WPBP-010, and S01B-001 through S01B-005
- **AI Compatibility:** AI-readable current-state baseline; absence of WordPress prevents runtime inference
- **Approval:** Pending Founder/technical review; this is a blocked pre-installation record, not an installed baseline

## Purpose

Record the observable WordPress foundation state and why installation was stopped without creating runtime or business configuration.

## Fresh Installation Verification

| Verification | Observation | Result |
| --- | --- | --- |
| WordPress Core present | `public/wp-load.php`, `public/wp-admin/`, and `public/wp-includes/version.php` absent | Not installed |
| Exact WordPress version | No runtime/version file/WP-CLI | Unavailable |
| Installer completed | No installation action attempted | No |
| Database tables | No database runtime/connection | Not created/not verifiable |
| Default content | No WordPress installation | None created by Sprint 01B |
| Admin account | No WordPress installation | None created |

Fresh installation cannot be verified because it does not exist. Installation was intentionally stopped at the preflight gate.

## Directory Structure

```text
public/
└── wp-content/
    ├── languages/                 (empty local directory)
    ├── mu-plugins/
    │   └── README.md              (documentation only)
    ├── plugins/
    │   ├── README.md              (documentation only)
    │   └── .gitkeep
    ├── themes/
    │   ├── README.md              (documentation only)
    │   └── blocksy-child/
    │       ├── README.md          (unresolved placeholder)
    │       └── .gitkeep
    └── uploads/
        └── .gitkeep
```

Absent required WordPress Core paths include `wp-admin/`, `wp-includes/`, `wp-load.php`, `wp-settings.php`, and `index.php`.

## Database Connection

- No MariaDB/MySQL server or client is installed locally.
- TCP 3306 is closed.
- No database connection was attempted.
- `.env.example` contains placeholder development values only.
- `wp-config.example.php` reads environment variables and proposes `utf8mb4`, but it is not active configuration.
- No database name, credential, table, charset, collation, SQL mode, timezone, backup, or restore behavior is runtime-verified.

Status: `NOT ESTABLISHED`.

## Permalinks

- WordPress rewrite rules do not exist.
- No active web server is running.
- `public/.htaccess` is absent.
- Current Apache module output does not list a loaded rewrite module.
- The repository Nginx template includes a WordPress-style `try_files` rule but is not active.

Status: `NOT VERIFIED`.

## Uploads

- `public/wp-content/uploads/` exists with mode `0755`, owned by the local user and group `staff`.
- The directory is writable by the current local owner.
- No web-service identity exists to validate runtime write access or least privilege.
- No media file was uploaded.
- PHP upload and POST limits are unavailable; repository template values are not runtime evidence.

Status: `LOCAL OWNER WRITABLE; RUNTIME NOT VERIFIED`.

## Theme

- Blocksy and Blocksy Pro are not installed.
- No theme is active because WordPress is absent.
- Blocksy Pro license state cannot be verified.
- The existing `blocksy-child` path is a documentation placeholder only; it remains unresolved under FD-GOV-008 and is not an active theme.
- No Customizer setting, design token, header, footer, sidebar, archive, single layout, hook, template, CSS, JavaScript, or PHP was created.

Status: `NOT INSTALLED`.

## Plugins

- WooCommerce is not installed or activated.
- Elementor Pro is not installed or activated.
- No other regular or MU plugin code is installed.
- No setup wizard ran and no plugin setting was changed.
- No product, product type, taxonomy, attribute, price, cart, checkout, payment, shipping, tax, order, form, Inquiry, page, template, or demo data was created.

Status: `NONE INSTALLED`.

## Filesystem and Configuration

| Concern | Observation |
| --- | --- |
| `wp-content` mode | `0755`, local user:`staff` |
| Uploads mode | `0755`, local user:`staff` |
| Active `FS_METHOD` | Unavailable/not defined |
| Active WordPress memory limit | Unavailable |
| Active upload/POST limits | Unavailable |
| Active WordPress timezone | Unavailable |
| Active database charset/collation | Unavailable |
| Active HTTPS URL | Unavailable |
| Active permalink structure | Unavailable |

## Repository and Blueprint Compliance

- Baseline commit/tag refs remain unchanged.
- No WordPress Core or dependency was committed.
- WordPress, WooCommerce, Blocksy, Elementor, and Plugin Matrix documents remain unchanged.
- Inquiry First and No Public Pricing remain constraints; no commerce runtime exists.
- No Custom Theme, Gravity Forms, LiteSpeed Cache, or Phase 1 AI feature was introduced.
- Repository work is limited to Markdown evidence under `repository/config/` plus required governance links.

## Known Limitations

1. No approved/active hosting environment.
2. No PHP or extension inventory.
3. No MariaDB/MySQL runtime or database.
4. No active HTTP/HTTPS server or verified DNS/TLS.
5. No exact approved WordPress/component version matrix.
6. No WordPress Core, WP-CLI, Composer, Docker/Podman, or Node/npm.
7. No Blocksy Pro or Elementor Pro packages/license path.
8. No backup/restore or installation rollback evidence.
9. No completed security/privacy/testing/operations prerequisites.
10. All Build and Pre-Implementation checklist items remain unchecked.

## Installation Decision

`STOPPED — REQUIRED DEPENDENCIES AND APPROVALS ARE MISSING`

No substitute, latest version, free edition, alternate plugin/theme, or default business configuration was selected.

## Change Notes

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-07-04 | Initial Sprint 01B blocked WordPress baseline record; no installation performed. |

## Navigation

- [Environment Report](ENVIRONMENT_REPORT.md)
- [Plugin Inventory](PLUGIN_INVENTORY.md)
- [Pre-Implementation Checklist](../PRE_IMPLEMENTATION_CHECKLIST.md)
- [Sprint 01B Audit](../../docs/AUDIT_REPORT_SPRINT01B.md)
