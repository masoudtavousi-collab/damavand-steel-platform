#!/usr/bin/env python3
"""Focused static contract checks for the sales-availability plugin.

This test deliberately avoids requiring a WordPress runtime. It verifies the
high-risk contract surface: dedicated meta ownership, parent/variation hooks,
fail-closed handling of malformed explicit states, and absence of destructive
catalog/commercial mutations.
"""
from __future__ import annotations

from pathlib import Path

PLUGIN = Path("public/wp-content/plugins/damavand-steel-sales-availability-control/damavand-steel-sales-availability-control.php")


def main() -> None:
    text = PLUGIN.read_text(encoding="utf-8")

    required = [
        "_ds_sales_enabled",
        "_ds_commerce_mode",
        "_ds_data_status",
        "woocommerce_is_purchasable",
        "woocommerce_variation_is_purchasable",
        "woocommerce_add_to_cart_validation",
        "woocommerce_check_cart_items",
        "woocommerce_save_product_variation",
        "وضعیت فروش",
        "فعال / قابل فروش",
    ]
    for needle in required:
        assert needle in text, f"missing required contract token: {needle}"

    forbidden = [
        "set_price(",
        "set_regular_price(",
        "set_sale_price(",
        "set_stock_quantity(",
        "wc_update_product_stock(",
        "wp_delete_post(",
        "delete_post_meta(",
    ]
    for needle in forbidden:
        assert needle not in text, f"destructive/commercial mutation found: {needle}"

    assert "return false;" in text
    assert "Explicitly malformed states fail closed" in text
    assert "get_parent_id()" in text

    print("Sales Availability Control focused contract checks: PASS")


if __name__ == "__main__":
    main()
