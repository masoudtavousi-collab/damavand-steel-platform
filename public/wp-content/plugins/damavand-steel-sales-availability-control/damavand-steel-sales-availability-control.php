<?php
/**
 * Plugin Name: Damavand Steel Sales Availability Control
 * Description: Founder-controlled per-product and per-variation sales availability for WooCommerce. Keeps commerce mode and product-data status independent and fails closed on an explicit disable or malformed state.
 * Version: 1.0.1
 * Author: Damavand Steel
 * Requires Plugins: woocommerce
 * License: GPL-2.0-or-later
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

final class Damavand_Steel_Sales_Availability_Control {
    private const SALES_ENABLED_META = '_ds_sales_enabled';
    private const COMMERCE_MODE_META = '_ds_commerce_mode';
    private const DATA_STATUS_META = '_ds_data_status';
    private const NONCE_ACTION = 'ds_sales_availability_save';
    private const NONCE_NAME = 'ds_sales_availability_nonce';

    public static function boot(): void {
        add_action( 'add_meta_boxes_product', [ __CLASS__, 'add_product_meta_box' ] );
        add_action( 'save_post_product', [ __CLASS__, 'save_product_meta' ], 20, 2 );
        add_action( 'woocommerce_variation_options', [ __CLASS__, 'render_variation_field' ], 10, 3 );
        add_action( 'woocommerce_save_product_variation', [ __CLASS__, 'save_variation_field' ], 20, 2 );

        add_filter( 'woocommerce_is_purchasable', [ __CLASS__, 'filter_product_purchasable' ], 20, 2 );
        add_filter( 'woocommerce_variation_is_purchasable', [ __CLASS__, 'filter_variation_purchasable' ], 20, 2 );
        add_filter( 'woocommerce_add_to_cart_validation', [ __CLASS__, 'validate_add_to_cart' ], 20, 5 );
        add_action( 'woocommerce_check_cart_items', [ __CLASS__, 'validate_existing_cart_items' ], 20 );
    }

    public static function add_product_meta_box(): void {
        add_meta_box(
            'ds_sales_availability',
            'وضعیت فروش',
            [ __CLASS__, 'render_meta_box' ],
            'product',
            'side',
            'high'
        );
    }

    public static function render_meta_box( WP_Post $post ): void {
        wp_nonce_field( self::NONCE_ACTION, self::NONCE_NAME );
        $product = wc_get_product( $post->ID );
        $enabled = $product ? self::is_sales_enabled( $product ) : true;
        $commerce_mode = $product ? self::get_meta( $product, self::COMMERCE_MODE_META ) : '';
        $data_status = $product ? self::get_meta( $product, self::DATA_STATUS_META ) : '';
        ?>
        <p>
            <label>
                <input type="checkbox" name="ds_sales_enabled" value="yes" <?php checked( $enabled ); ?> />
                فعال / قابل فروش
            </label>
        </p>
        <p class="description">غیرفعال‌کردن فروش، محصول و سابقه آن را حذف نمی‌کند.</p>
        <?php if ( $commerce_mode || $data_status ) : ?>
            <p class="description">
                <?php echo esc_html( sprintf( 'commerce_mode: %s | data_status: %s', $commerce_mode ?: '—', $data_status ?: '—' ) ); ?>
            </p>
        <?php endif;
    }

    public static function save_product_meta( int $post_id, WP_Post $post ): void {
        if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
            return;
        }
        if ( 'product' !== $post->post_type || ! current_user_can( 'edit_post', $post_id ) ) {
            return;
        }
        if ( empty( $_POST[ self::NONCE_NAME ] ) || ! wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST[ self::NONCE_NAME ] ) ), self::NONCE_ACTION ) ) {
            return;
        }

        update_post_meta( $post_id, self::SALES_ENABLED_META, self::normalize_state( $_POST['ds_sales_enabled'] ?? 'no' ) );
    }

    public static function render_variation_field( int $loop, array $variation_data, WP_Post $variation ): void {
        $product = wc_get_product( $variation->ID );
        if ( ! $product ) {
            return;
        }
        $enabled = self::is_sales_enabled( $product );
        woocommerce_wp_checkbox(
            [
                'id'            => self::SALES_ENABLED_META . '[' . $loop . ']',
                'name'          => self::SALES_ENABLED_META . '[' . $loop . ']',
                'value'         => $enabled ? 'yes' : 'no',
                'label'         => 'فروش این SKU فعال',
                'wrapper_class' => 'form-row form-row-full',
                'cbvalue'       => 'yes',
            ]
        );
    }

    public static function save_variation_field( int $variation_id, int $i ): void {
        if ( ! current_user_can( 'edit_post', $variation_id ) ) {
            return;
        }
        $values = isset( $_POST[ self::SALES_ENABLED_META ] ) && is_array( $_POST[ self::SALES_ENABLED_META ] )
            ? wp_unslash( $_POST[ self::SALES_ENABLED_META ] )
            : [];
        $value = isset( $values[ $i ] ) ? sanitize_text_field( $values[ $i ] ) : 'no';
        update_post_meta( $variation_id, self::SALES_ENABLED_META, self::normalize_state( $value ) );
    }

    public static function filter_product_purchasable( bool $purchasable, WC_Product $product ): bool {
        return self::is_sales_enabled( $product ) && $purchasable;
    }

    public static function filter_variation_purchasable( bool $purchasable, WC_Product_Variation $variation ): bool {
        return self::is_sales_enabled( $variation ) && $purchasable;
    }

    public static function validate_add_to_cart( bool $passed, int $product_id, int $quantity, int $variation_id = 0, array $variation = [] ): bool {
        $target_id = $variation_id > 0 ? $variation_id : $product_id;
        $product = wc_get_product( $target_id );
        if ( ! $product || self::is_sales_enabled( $product ) ) {
            return $passed;
        }
        wc_add_notice( 'این محصول یا SKU فعلاً برای فروش غیرفعال است.', 'error' );
        return false;
    }

    public static function validate_existing_cart_items(): void {
        if ( ! function_exists( 'WC' ) || ! WC()->cart ) {
            return;
        }
        foreach ( WC()->cart->get_cart() as $cart_key => $cart_item ) {
            $product = $cart_item['data'] ?? null;
            if ( $product instanceof WC_Product && ! self::is_sales_enabled( $product ) ) {
                WC()->cart->remove_cart_item( $cart_key );
                wc_add_notice( 'یک قلم غیرفعال از سبد خرید حذف شد.', 'error' );
            }
        }
    }

    private static function get_meta( WC_Product $product, string $key ): string {
        $value = $product->get_meta( $key, true );
        return is_string( $value ) ? $value : '';
    }

    private static function normalize_state( $value ): string {
        $value = is_string( $value ) ? strtolower( trim( $value ) ) : '';
        return 'yes' === $value ? 'yes' : 'no';
    }

    public static function is_sales_enabled( WC_Product $product ): bool {
        // Product/SKU inheritance is fail-closed: a disabled parent always
        // disables every variation, even when a child carries "yes" locally.
        if ( $product->is_type( 'variation' ) && $product->get_parent_id() ) {
            $parent = wc_get_product( $product->get_parent_id() );
            if ( ! $parent || ! self::is_sales_enabled( $parent ) ) {
                return false;
            }
        }

        $raw = $product->get_meta( self::SALES_ENABLED_META, true );

        // Explicitly malformed states fail closed. A missing value follows the
        // Founder-approved ACTIVE-by-default policy. WooCommerce continues to
        // own price, stock, and overall commercial purchasability.
        if ( '' === $raw || null === $raw ) {
            return true;
        }

        return 'yes' === self::normalize_state( $raw );
    }
}

add_action( 'plugins_loaded', [ 'Damavand_Steel_Sales_Availability_Control', 'boot' ] );
