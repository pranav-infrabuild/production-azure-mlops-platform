"""Tests for the data validation engine."""

from pathlib import Path

import pandas as pd
import yaml

from data.validation.validate_dataset import (
    validate_allowed_values,
    validate_columns,
    validate_data_types,
    validate_duplicates,
    validate_nulls,
    validate_ranges,
    validate_row_count,
    write_quarantine,
    write_validation_report,
)


DATA_FILE = Path("data/sample/customer_churn_sample.csv")
RULES_FILE = Path("data/validation-rules/customer-churn.yaml")


def load_test_data() -> pd.DataFrame:
    """Load the sample dataset."""
    return pd.read_csv(DATA_FILE)


def load_test_rules() -> dict:
    """Load validation rules."""
    with RULES_FILE.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def test_valid_dataset_has_no_column_errors():
    """Verify that all required columns exist."""
    dataframe = load_test_data()
    rules = load_test_rules()

    errors = validate_columns(dataframe, rules)

    assert errors == []


def test_valid_dataset_has_no_null_errors():
    """Verify that the valid dataset passes null checks."""
    dataframe = load_test_data()
    rules = load_test_rules()

    errors = validate_nulls(dataframe, rules)

    assert errors == []


def test_valid_dataset_has_no_duplicate_errors():
    """Verify that the valid dataset has no duplicates."""
    dataframe = load_test_data()
    rules = load_test_rules()

    errors = validate_duplicates(dataframe, rules)

    assert errors == []


def test_valid_dataset_has_enough_rows():
    """Verify that the dataset meets the minimum row requirement."""
    dataframe = load_test_data()
    rules = load_test_rules()

    errors = validate_row_count(dataframe, rules)

    assert errors == []


def test_valid_dataset_has_correct_data_types():
    """Verify that the valid dataset passes type validation."""
    dataframe = load_test_data()
    rules = load_test_rules()

    errors = validate_data_types(dataframe, rules)

    assert errors == []


def test_invalid_data_type_is_detected():
    """Verify that an invalid data type is detected."""
    dataframe = load_test_data()
    rules = load_test_rules()

    dataframe["tenure"] = dataframe["tenure"].astype(float)

    errors = validate_data_types(dataframe, rules)

    assert any("tenure" in error for error in errors)


def test_invalid_allowed_value_is_detected():
    """Verify that invalid categorical values are detected."""
    dataframe = load_test_data()
    rules = load_test_rules()

    dataframe.loc[0, "partner"] = "INVALID"

    errors = validate_allowed_values(dataframe, rules)

    assert any("partner" in error for error in errors)


def test_negative_tenure_is_detected():
    """Verify that negative tenure is detected."""
    dataframe = load_test_data()
    rules = load_test_rules()

    dataframe.loc[0, "tenure"] = -5

    errors = validate_ranges(dataframe, rules)

    assert any("tenure" in error for error in errors)


def test_negative_monthly_charges_are_detected():
    """Verify that negative monthly charges are detected."""
    dataframe = load_test_data()
    rules = load_test_rules()

    dataframe.loc[0, "monthly_charges"] = -100

    errors = validate_ranges(dataframe, rules)

    assert any("monthly_charges" in error for error in errors)


def test_missing_column_is_detected():
    """Verify that a missing required column is detected."""
    dataframe = load_test_data()
    rules = load_test_rules()

    dataframe = dataframe.drop(columns=["customer_id"])

    errors = validate_columns(dataframe, rules)

    assert any("customer_id" in error for error in errors)


def test_failed_dataset_is_written_to_quarantine(
    tmp_path,
    monkeypatch,
):
    """Verify that a failed dataset is written to quarantine."""

    import data.validation.validate_dataset as validator

    monkeypatch.setattr(
        validator,
        "QUARANTINE_DIR",
        tmp_path,
    )

    dataframe = load_test_data()
    input_file = Path("customer_churn_bad.csv")

    quarantine_file = write_quarantine(
        dataframe,
        input_file,
    )

    assert quarantine_file.exists()

    quarantined_data = pd.read_csv(
        quarantine_file,
    )

    assert len(quarantined_data) == len(dataframe)


def test_validation_report_is_created(
    tmp_path,
    monkeypatch,
):
    """Verify that validation errors are written to a report."""

    import data.validation.validate_dataset as validator

    monkeypatch.setattr(
        validator,
        "REPORT_DIR",
        tmp_path,
    )

    errors = [
        "partner: invalid values {'INVALID'}",
        "tenure: value below minimum 0",
    ]

    input_file = Path("customer_churn_bad.csv")

    report_file = write_validation_report(
        errors,
        input_file,
    )

    assert report_file.exists()

    report_content = report_file.read_text(
        encoding="utf-8",
    )

    assert "DATA VALIDATION REPORT" in report_content
    assert "Validation Errors:" in report_content
    assert "partner: invalid values" in report_content
    assert "tenure: value below minimum" in report_content