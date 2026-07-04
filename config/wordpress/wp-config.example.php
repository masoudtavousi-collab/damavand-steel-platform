<?php
/**
 * Non-secret WordPress configuration template.
 * Replace environment access with the deployment platform's approved loader.
 */

define('DB_NAME', getenv('DB_NAME'));
define('DB_USER', getenv('DB_USER'));
define('DB_PASSWORD', getenv('DB_PASSWORD'));
define('DB_HOST', getenv('DB_HOST') . ':' . (getenv('DB_PORT') ?: '3306'));
define('DB_CHARSET', 'utf8mb4');
define('DB_COLLATE', '');

$table_prefix = getenv('DB_TABLE_PREFIX') ?: 'wp_';

define('WPLANG', 'fa_IR');
define('DISALLOW_FILE_EDIT', true);
define('WP_POST_REVISIONS', 20);
define('AUTOSAVE_INTERVAL', 120);
define('EMPTY_TRASH_DAYS', 14);
define('WP_DEBUG', filter_var(getenv('WP_DEBUG'), FILTER_VALIDATE_BOOL));
define('WP_DEBUG_LOG', filter_var(getenv('WP_DEBUG_LOG'), FILTER_VALIDATE_BOOL));
define('WP_DEBUG_DISPLAY', false);

// Add unique authentication keys and salts from environment variables here.
// Define WP_HOME and WP_SITEURL according to the deployment topology.
// Finish by requiring ABSPATH . 'wp-settings.php'.
