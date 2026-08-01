#!/usr/bin/env sh
set -eu

if [ -n "${PYTHON:-}" ]; then
  python="$PYTHON"
elif [ -x ".venv/bin/python3" ]; then
  python=".venv/bin/python3"
else
  python="python3"
fi

expect_failure() {
  fixture="$1"
  expected_code="$2"
  validator="$3"

  set +e
  output="$("$python" "$validator" "$fixture" 2>&1)"
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
"$python" "$product_validator" tests/fixtures/product-core/valid-minimal.yaml
expect_failure tests/fixtures/product-core/invalid-missing-provenance.yaml MISSING_PROVENANCE "$product_validator"

measurement_validator="repository/data/validation/validate_measurements.py"
"$python" "$measurement_validator" canonical
"$python" "$measurement_validator" tests/fixtures/measurements/valid-foundation.yaml
expect_failure tests/fixtures/measurements/invalid-cycle.yaml UNIT_BASE_CYCLE "$measurement_validator"
expect_failure tests/fixtures/measurements/invalid-symbol-collision.yaml DUPLICATE_UNIT_SYMBOL "$measurement_validator"
expect_failure tests/fixtures/measurements/invalid-precision.yaml PRECISION_RANGE "$measurement_validator"
expect_failure tests/fixtures/measurements/invalid-data-type.yaml UNIT_DATA_TYPE_UNSUPPORTED "$measurement_validator"
expect_failure tests/fixtures/measurements/invalid-conversion.yaml RATIONAL_DENOMINATOR "$measurement_validator"

attribute_validator="repository/data/validation/validate_product_attributes.py"
"$python" "$attribute_validator" tests/fixtures/product-attributes/valid-foundation.yaml
"$python" "$attribute_validator" tests/fixtures/product-attributes/valid-measured-attribute.yaml
expect_failure tests/fixtures/product-attributes/invalid-naming.yaml ATTRIBUTE_KEY_FORMAT "$attribute_validator"

pd02a_value_validator="repository/data/validation/validate_product_attribute_values.py"
"$python" "$pd02a_value_validator"
"$python" "$pd02a_value_validator" tests/fixtures/pd02/valid-synthetic-controlled-values.yaml
expect_failure tests/fixtures/pd02/invalid-duplicate-normalized-term.yaml DUPLICATE_NORMALIZED_TERM "$pd02a_value_validator"

pd02a_profile_validator="repository/data/validation/validate_product_attribute_profiles.py"
"$python" "$pd02a_profile_validator"
"$python" "$pd02a_profile_validator" tests/fixtures/pd02/valid-synthetic-profile.yaml
expect_failure tests/fixtures/pd02/invalid-unresolved-registry.yaml UNRESOLVED_VALUE_REGISTRY "$pd02a_profile_validator"
expect_failure tests/fixtures/pd02/invalid-orphan-profile.yaml ORPHAN_PROFILE_SCOPE "$pd02a_profile_validator"
expect_failure tests/fixtures/pd02/invalid-term-attribute-mismatch.yaml VALUE_SOURCE_TYPE "$pd02a_profile_validator"
expect_failure tests/fixtures/pd02/invalid-status-promotion.yaml SYNTHETIC_STATUS "$pd02a_profile_validator"
"$python" tests/test_pd02_product_data.py

pd02b_label_validator="repository/data/validation/validate_product_data_localized_labels.py"
"$python" "$pd02b_label_validator"
"$python" "$pd02b_label_validator" tests/fixtures/pd02b/valid-synthetic-localized-labels.yaml
expect_failure tests/fixtures/pd02b/invalid-unicode-confusable-label.yaml UNICODE_CONFUSABLE_LABEL "$pd02b_label_validator"

pd02b_approval_validator="repository/data/validation/validate_product_data_approval_evidence.py"
"$python" "$pd02b_approval_validator"
"$python" "$pd02b_approval_validator" tests/fixtures/pd02b/valid-synthetic-approval-evidence.yaml
expect_failure tests/fixtures/pd02b/invalid-missing-domain-approval.yaml MISSING_DOMAIN_APPROVAL "$pd02b_approval_validator"
expect_failure tests/fixtures/pd02b/invalid-approval-replay.yaml APPROVAL_NOT_CONSUMED "$pd02b_approval_validator"

"$python" repository/data/validation/validate_product_core.py
"$python" repository/data/validation/validate_pd02b_canonical_slice.py
"$python" tests/test_pd02b_product_data.py

product_master_data_validator="repository/data/validation/validate_product_master_data.py"
"$python" "$product_master_data_validator" tests/fixtures/product-master-data/valid-synthetic-minimal.yaml
expect_failure tests/fixtures/product-master-data/invalid-duplicate-key.yaml DUPLICATE_KEY "$product_master_data_validator"
"$python" tests/test_product_master_data.py

pd03a_foundation_validator="repository/data/validation/validate_pd03a_pilot_prerequisite.py"
pd03a_approval_validator="repository/data/validation/validate_pd03a_approval_evidence.py"
pd03a_pilot_validator="repository/data/validation/validate_product_pilot_combinations.py"
"$python" "$pd03a_foundation_validator"
"$python" "$pd03a_approval_validator"
"$python" "$pd03a_pilot_validator" tests/fixtures/pd03a/valid-synthetic-pilot-combinations.yaml
"$python" tests/test_pd03a_foundation.py

"$python" repository/data/validation/validate_bp2_data_blueprint.py
"$python" repository/data/validation/validate_bp2_data_administration.py
"$python" tests/test_bp2_data_administration.py

"$python" prototypes/bp1-visible-local/tests/validate_bp1.py
"$python" scripts/validate_manifest.py
"$python" scripts/validate_atlas_adoption.py
./scripts/validate.sh

echo "All repository and foundation tests passed."
