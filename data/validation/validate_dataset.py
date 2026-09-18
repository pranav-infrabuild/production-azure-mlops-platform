"""Data validation engine for production datasets."""

from pathlib import Path
import argparse

import pandas as pd
import yaml


RULES_FILE = Path("data/validation-rules/customer-churn.yaml")
QUARANTINE_DIR = Path("data/quarantine")
REPORT_DIR = Path("data/validation-reports")


def load_rules():
    """Load validation rules from YAML."""
    with RULES_FILE.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_columns(dataframe, rules):
    """Validate that all required columns exist."""
    errors = []

    schema = rules.get("schema", {})
    required_columns = schema.get("required_columns", [])

    missing_columns = [
        column
        for column in required_columns
        if column not in dataframe.columns
    ]

    if missing_columns:
        errors.append(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    return errors


def validate_nulls(dataframe, rules):
    """Validate null percentage and nullable rules."""
    errors = []

    quality_rules = rules.get("quality", {})

    maximum_null_percentage = quality_rules.get(
        "maximum_null_percentage",
        100,
    )

    schema = rules.get("schema", {})
    columns_rules = schema.get("columns", {})

    for column in dataframe.columns:
        null_percentage = dataframe[column].isnull().mean() * 100

        if null_percentage > maximum_null_percentage:
            errors.append(
                f"{column}: null percentage "
                f"{null_percentage:.2f}% exceeds maximum "
                f"{maximum_null_percentage}%"
            )

    for column, column_rules in columns_rules.items():

        if column not in dataframe.columns:
            continue

        nullable = column_rules.get("nullable", True)

        if not nullable:
            null_count = dataframe[column].isnull().sum()

            if null_count > 0:
                errors.append(
                    f"{column}: contains {null_count} null values "
                    f"but nullable is false"
                )

    return errors


def validate_duplicates(dataframe, rules):
    """Validate duplicate rows."""
    errors = []

    quality_rules = rules.get("quality", {})

    allow_duplicates = quality_rules.get(
        "allow_duplicates",
        True,
    )

    if not allow_duplicates:
        duplicate_count = dataframe.duplicated().sum()

        if duplicate_count > 0:
            errors.append(
                f"Dataset contains {duplicate_count} duplicate rows"
            )

    return errors


def validate_row_count(dataframe, rules):
    """Validate minimum dataset row count."""
    errors = []

    quality_rules = rules.get("quality", {})

    minimum_rows = quality_rules.get(
        "minimum_rows",
        0,
    )

    if len(dataframe) < minimum_rows:
        errors.append(
            f"Dataset contains {len(dataframe)} rows, "
            f"minimum required is {minimum_rows}"
        )

    return errors


def validate_data_types(dataframe, rules):
    """Validate dataframe column data types."""
    errors = []

    schema = rules.get("schema", {})
    columns_rules = schema.get("columns", {})

    for column, column_rules in columns_rules.items():

        if column not in dataframe.columns:
            continue

        expected_type = column_rules.get("type")
        actual_type = str(dataframe[column].dtype)

        if expected_type == "string":
            if not (
                pd.api.types.is_object_dtype(dataframe[column])
                or pd.api.types.is_string_dtype(dataframe[column])
            ):
                errors.append(
                    f"{column}: expected string, "
                    f"found {actual_type}"
                )

        elif expected_type == "integer":
            if not pd.api.types.is_integer_dtype(dataframe[column]):
                errors.append(
                    f"{column}: expected integer, "
                    f"found {actual_type}"
                )

        elif expected_type == "float":
            if not pd.api.types.is_float_dtype(dataframe[column]):
                errors.append(
                    f"{column}: expected float, "
                    f"found {actual_type}"
                )

    return errors


def validate_allowed_values(dataframe, rules):
    """Validate categorical columns against allowed values."""
    errors = []

    schema = rules.get("schema", {})
    columns_rules = schema.get("columns", {})

    for column, column_rules in columns_rules.items():

        if column not in dataframe.columns:
            continue

        allowed_values = column_rules.get("allowed_values")

        if allowed_values is None:
            continue

        actual_values = set(
            dataframe[column].dropna().unique()
        )

        allowed_values_set = set(allowed_values)

        invalid_values = actual_values - allowed_values_set

        if invalid_values:
            errors.append(
                f"{column}: invalid values {invalid_values}"
            )

    return errors


def validate_ranges(dataframe, rules):
    """Validate minimum and maximum numeric ranges."""
    errors = []

    schema = rules.get("schema", {})
    columns_rules = schema.get("columns", {})

    for column, column_rules in columns_rules.items():

        if column not in dataframe.columns:
            continue

        minimum = column_rules.get("min")
        maximum = column_rules.get("max")

        if minimum is not None:
            invalid_count = (
                dataframe[column] < minimum
            ).sum()

            if invalid_count > 0:
                errors.append(
                    f"{column}: value below minimum {minimum}"
                )

        if maximum is not None:
            invalid_count = (
                dataframe[column] > maximum
            ).sum()

            if invalid_count > 0:
                errors.append(
                    f"{column}: value above maximum {maximum}"
                )

    return errors


def write_quarantine(dataframe, input_file):
    """Write failed dataset to quarantine directory."""
    QUARANTINE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    input_path = Path(input_file)

    quarantine_file = (
        QUARANTINE_DIR
        / f"{input_path.stem}_failed.csv"
    )

    dataframe.to_csv(
        quarantine_file,
        index=False,
    )

    return quarantine_file


def write_validation_report(errors, input_file):
    """Write validation errors to a report."""
    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    input_path = Path(input_file)

    report_file = (
        REPORT_DIR
        / f"{input_path.stem}_validation_report.txt"
    )

    with report_file.open(
        "w",
        encoding="utf-8",
    ) as file:

        file.write(
            "DATA VALIDATION REPORT\n"
        )

        file.write(
            "======================\n\n"
        )

        file.write(
            f"Dataset: {input_file}\n\n"
        )

        file.write(
            "Validation Errors:\n"
        )

        for error in errors:
            file.write(
                f"- {error}\n"
            )

    return report_file


def validate_dataset(input_file):
    """Run all validation checks against a dataset."""
    dataframe = pd.read_csv(input_file)

    rules = load_rules()

    errors = []

    errors.extend(
        validate_columns(
            dataframe,
            rules,
        )
    )

    errors.extend(
        validate_nulls(
            dataframe,
            rules,
        )
    )

    errors.extend(
        validate_duplicates(
            dataframe,
            rules,
        )
    )

    errors.extend(
        validate_row_count(
            dataframe,
            rules,
        )
    )

    errors.extend(
        validate_data_types(
            dataframe,
            rules,
        )
    )

    errors.extend(
        validate_allowed_values(
            dataframe,
            rules,
        )
    )

    errors.extend(
        validate_ranges(
            dataframe,
            rules,
        )
    )

    if errors:
        print("VALIDATION FAILED")
        print("=================")

        for error in errors:
            print(f"- {error}")

        quarantine_file = write_quarantine(
            dataframe,
            input_file,
        )

        report_file = write_validation_report(
            errors,
            input_file,
        )

        print()
        print(
            f"Quarantine file: {quarantine_file}"
        )

        print(
            f"Validation report: {report_file}"
        )

        return False

    print("VALIDATION PASSED")

    return True


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Validate a dataset using "
            "YAML validation rules."
        )
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input CSV dataset",
    )

    return parser.parse_args()


def main():
    """CLI entry point."""
    args = parse_arguments()

    is_valid = validate_dataset(
        args.input
    )

    if not is_valid:
        raise SystemExit(1)


if __name__ == "__main__":
    main()