#!/usr/bin/env sh
set -eu

expect_failure() {
  fixture="$1"
  expected_code="$2"
  validator="$3"

  set +e
  output="$(python3 "$validator" "$fixture" 2>&1)"
  status=$?
  set -e

  if [ "$status" -eq 0 ]; then
    echo "Expected $fixture to fail validation" >&2
    exit 1
  fi

  case "$output" in
    *"$expected_code"*) ;;
    *)
      echo "Expected $expected_code from $fixture" >&2
      printf '%s\n' "$output" >&2
      exit 1
      ;;
  esac
}

product_validator="repository/data/validation/validate_product_core.py"
python3 "$product_validator" tests/fixtures/product-core/valid-minimal.yaml
expect_failure tests/fixtures/product-core/invalid-missing-provenance.yaml MISSING_PROVENANCE "$product_validator"

measurement_validator="repository/data/validation/validate_measurements.py"
python3 "$measurement_validator" canonical
python3 "$measurement_validator" tests/fixtures/measurements/valid-foundation.yaml
expect_failure tests/fixtures/measurements/invalid-cycle.yaml UNIT_BASE_CYCLE "$measurement_validator"
expect_failure tests/fixtures/measurements/invalid-symbol-collision.yaml DUPLICATE_UNIT_SYMBOL "$measurement_validator"
expect_failure tests/fixtures/measurements/invalid-precision.yaml PRECISION_RANGE "$measurement_validator"
expect_failure tests/fixtures/measurements/invalid-data-type.yaml UNIT_DATA_TYPE_UNSUPPORTED "$measurement_validator"
expect_failure tests/fixtures/measurements/invalid-conversion.yaml RATIONAL_DENOMINATOR "$measurement_validator"

attribute_validator="repository/data/validation/validate_product_attributes.py"
python3 "$attribute_validator" tests/fixtures/product-attributes/valid-foundation.yaml
python3 "$attribute_validator" tests/fixtures/product-attributes/valid-measured-attribute.yaml
expect_failure tests/fixtures/product-attributes/invalid-naming.yaml ATTRIBUTE_KEY_FORMAT "$attribute_validator"

python3 repository/data/validation/validate_bp2_data_blueprint.py
python3 repository/data/validation/validate_bp2_data_administration.py

python3 scripts/validate_manifest.py
python3 scripts/validate_atlas_adoption.py
./scripts/validate.sh

echo "All repository and foundation tests passed."
