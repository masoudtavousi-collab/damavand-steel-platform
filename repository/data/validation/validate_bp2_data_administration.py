#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = ROOT / "repository/data/contracts/bp2-data-administration-v1.0.json"
SCHEMA_PATH = ROOT / "repository/data/schemas/bp2-data-administration-v1.0.schema.json"
SOURCE_PATH = ROOT / "repository/data/contracts/bp2-pipe-data-blueprint-v0.1.json"


def fail(code, message):
    raise SystemExit(f"{code}: {message}")


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail("JSON_LOAD_ERROR", f"{path}: {exc}")


contract = load(CONTRACT_PATH)
schema = load(SCHEMA_PATH)
source = load(SOURCE_PATH)

expected_hierarchy = ["CATALOG", "PLATFORM", "FAMILY", "SERIES", "VARIANT_RULE_SET", "SKU"]
expected_statuses = [
    "APPROVED", "CANDIDATE_UNVERIFIED", "MISSING_DATA_VALUE",
    "FOUNDER_INPUT_REQUIRED", "DEFERRED", "NOT_APPLICABLE", "INVALID"
]
expected_registries = [
    "MATERIAL", "GRADE", "DIAMETER_SIZE", "THICKNESS", "COLOR_FINISH",
    "SURFACE_DESIGN", "BRANCH_LENGTH", "SALES_CALCULATION_UNITS",
    "SUPPLY_STATUS", "VALID_COMBINATION_RULES", "PILOT_COMBINATIONS",
    "PROVENANCE_EVIDENCE"
]
expected_sequence = [
    "FAMILY", "MATERIAL", "GRADE", "DIAMETER_SIZE", "VALID_THICKNESS",
    "COLOR_FINISH", "SURFACE_DESIGN", "LENGTH"
]

if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
    fail("SCHEMA_DRAFT", "schema must use JSON Schema 2020-12")
if schema.get("additionalProperties") is not False:
    fail("SCHEMA_OPEN_ROOT", "schema root must be closed")
if contract.get("contract_id") != "bp2-data-administration" or contract.get("contract_version") != "1.0.0":
    fail("CONTRACT_IDENTITY", "unexpected contract identity")

scope = contract.get("scope", {})
if scope.get("documentation_only") is not True:
    fail("IMPLEMENTATION_SCOPE", "contract must remain documentation-only")
for key in ("implements_admin_ui", "creates_products", "creates_skus", "changes_wordpress",
            "allows_import", "allows_publication", "allows_deployment"):
    if scope.get(key) is not False:
        fail("FORBIDDEN_AUTHORITY", f"{key} must be false")

if contract.get("canonical_hierarchy") != expected_hierarchy:
    fail("HIERARCHY_MISMATCH", "canonical hierarchy changed")
if contract.get("status_vocabulary") != expected_statuses:
    fail("STATUS_VOCABULARY", "status vocabulary must match governance standard")
if "ARCHIVED" in contract.get("status_vocabulary", []):
    fail("ARCHIVE_STATUS", "archival must be lifecycle metadata, not governance status")
if contract.get("registries") != expected_registries:
    fail("REGISTRY_SET", "expected exactly 12 governed registries")

capabilities = contract.get("registry_capabilities", {})
if capabilities.get("actions") != ["ADD", "EDIT", "DELETE_OR_ARCHIVE"]:
    fail("ADMIN_ACTIONS", "add/edit/delete-or-archive must be available")
if capabilities.get("default_delete_mode") != "SOFT_DELETE":
    fail("DELETE_MODE", "soft delete must be the default")
if not capabilities.get("dependency_check_required") or not capabilities.get("audit_required"):
    fail("MUTATION_GOVERNANCE", "dependency and audit checks are mandatory")

governance = contract.get("governance", {})
if not governance.get("preserve_history") or governance.get("cascade_delete") is not False:
    fail("HISTORY_OR_CASCADE", "history is required and cascade delete is forbidden")
if governance.get("approved_record_delete_requires_founder") is not True:
    fail("FOUNDER_APPROVAL", "approved deletion must require Founder approval")
if governance.get("archive_is_governance_status") is not False:
    fail("ARCHIVE_MODEL", "archive must remain lifecycle metadata")

if contract.get("smart_inquiry_sequence") != expected_sequence:
    fail("INQUIRY_SEQUENCE", "Smart Inquiry order changed")

policy = contract.get("pipe_family_policy", {})
if policy.get("administered_grades") != ["201", "304", "316"]:
    fail("GRADE_SCOPE", "administered grades must be 201/304/316")
if policy.get("excluded_grades") != [{"code": "430", "disposition": "DEFERRED"}]:
    fail("EXCLUDED_GRADE", "430 must remain deferred outside active administration")
if policy.get("base_lengths_m") != [3, 6] or policy.get("custom_length") != "INQUIRY_ONLY":
    fail("LENGTH_POLICY", "base lengths must be 3m/6m with custom inquiry-only")
if policy.get("sales_and_inquiry_unit") != "BRANCH" or policy.get("calculation_unit") != "METER":
    fail("UNIT_POLICY", "sales unit must be branch and calculation unit meter")
if policy.get("thickness_in_product_name") or policy.get("thickness_in_category"):
    fail("THICKNESS_NAMING", "thickness must not appear in names or categories")
if policy.get("cartesian_generation_forbidden") is not True:
    fail("CARTESIAN_POLICY", "Cartesian generation must remain forbidden")

source_pilots = source.get("approved_pilot_combinations", [])
historical = source.get("historical_matrix", {})
if len(source_pilots) != 3 or historical.get("approved_pilot_rows") != 3:
    fail("PILOT_RECONCILIATION", "source must preserve three approved pilots")
if historical.get("candidate_rows") != 879:
    fail("CANDIDATE_RECONCILIATION", "source must preserve 879 candidates")
if policy.get("approved_pilot_count") != 3 or policy.get("candidate_count") != 879:
    fail("COUNT_RECONCILIATION", "administration counts do not match source")

selection = contract.get("selection_policy", {})
if selection.get("candidate_selectable") or selection.get("candidate_auto_promotion"):
    fail("CANDIDATE_PROMOTION", "candidates cannot be selected or promoted")
for key in ("auto_creates_master_data", "auto_creates_product", "auto_creates_sku"):
    if selection.get(key) is not False:
        fail("AUTO_CREATE", f"{key} must be false")

experience = contract.get("future_admin_experience", {})
if experience.get("implementation_authority") is not False:
    fail("ADMIN_UI_AUTHORITY", "future UX specification cannot authorize implementation")

print(
    "BP2 DATA ADMINISTRATION VALIDATION PASSED: "
    "12 governed registries; add/edit/soft-delete; 3 approved pilots preserved; "
    "879 candidates not promoted; no admin UI, Product, SKU, WordPress, import, "
    "publication, or deployment authority."
)
