#!/usr/bin/env python3
"""Focused static contract checks for the sales-availability plugin.

This test deliberately avoids requiring a WordPress runtime. It verifies the
high-risk contract surface: dedicated meta ownership, parent/variation hooks,
fail-closed handling of malformed explicit states, parent-disabled inheritance,
Founder authorization boundaries, and absence of destructive catalog/commercial mutations.
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
        "manage_damavand_sales_availability",
        "register_activation_hook",
        "register_deactivation_hook",
        "WooCommerce reaches this hook from its product-save flow after the",
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

    # Parent-disabled state must override a child/SKU-local "yes" state.
    parent_guard = (
        "if ( ! $parent || ! self::is_sales_enabled( $parent ) ) {\n"
        "                return false;\n"
        "            }"
    )
    assert parent_guard in text, "parent-disabled inheritance guard is missing"
    assert (
        "// Product/SKU inheritance is fail-closed: a disabled parent always\n"
        "        // disables every variation, even when a child carries \"yes\" locally."
    ) in text, "parent/SKU inheritance contract note is missing"

    # Missing state is still active by default after parent inheritance is checked.
    missing_state_block = (
        "if ( '' === $raw || null === $raw ) {\n"
        "            return true;\n"
        "        }"
    )
    assert missing_state_block in text, "active-by-default missing-state policy is missing"

    # Founder-controlled authorization must be separate from generic product editing.
    assert "private const MANAGE_CAPABILITY = 'manage_damavand_sales_availability';" in text
    assert "current_user_can( self::MANAGE_CAPABILITY )" in text
    assert "current_user_can( 'edit_post', $post_id ) || ! self::can_manage_sales_availability()" in text
    assert "current_user_can( 'edit_post', $variation_id ) || ! self::can_manage_sales_availability()" in text
    assert "\$role->add_cap( self::MANAGE_CAPABILITY );" in text
    assert "\$role->remove_cap( self::MANAGE_CAPABILITY );" in text

    # Variation saves rely on WooCommerce's enclosing product-save nonce boundary;
    # do not invent a second nonce contract inside the per-variation hook.
    assert "plugin-specific nonce" not in text
    assert "product edit nonce" in text

    print("Sales Availability Control focused contract checks: PASS")


if __name__ == "__main__":
    main()
