from __future__ import annotations

from typing import Any

import pyarrow.compute as pc
import pyarrow.parquet as pq


def validate_quality(
    parquet_path: str,
    quality_config: dict[str, Any],
    schema_config: dict[str, Any],
) -> list[str]:
    """
    Validate data quality rules for a Parquet dataset.

    Returns:
        A list of validation errors.
        An empty list means the quality checks passed.
    """

    errors: list[str] = []

    table = pq.read_table(parquet_path)

    # ---------------------------------------------------------
    # Minimum record count
    # ---------------------------------------------------------
    minimum_record_count = quality_config.get(
        "minimum_record_count",
        0,
    )

    record_count = table.num_rows

    if record_count < minimum_record_count:
        errors.append(
            f"Record count {record_count} is below "
            f"minimum required count {minimum_record_count}"
        )

    # ---------------------------------------------------------
    # Null checks
    # ---------------------------------------------------------
    null_check = quality_config.get(
        "null_check",
        {},
    )

    if null_check.get("enabled", False):
        for column_name, rules in schema_config.get(
            "columns",
            {},
        ).items():

            if column_name not in table.column_names:
                continue

            if rules.get("nullable", True):
                continue

            null_count = table.column(column_name).null_count

            if null_count > 0:
                errors.append(
                    f"{column_name}: found {null_count} null values"
                )

    # ---------------------------------------------------------
    # Duplicate checks
    # ---------------------------------------------------------
    duplicate_check = quality_config.get(
        "duplicate_check",
        {},
    )

    if duplicate_check.get("enabled", False):

        column_name = duplicate_check.get("column")

        if column_name and column_name in table.column_names:

            column = table.column(column_name)

            unique_count = pc.count_distinct(column).as_py()
            total_count = table.num_rows

            duplicate_count = total_count - unique_count

            if duplicate_count > 0:
                errors.append(
                    f"{column_name}: found "
                    f"{duplicate_count} duplicate records"
                )

    # ---------------------------------------------------------
    # Range checks
    # ---------------------------------------------------------
    range_checks = quality_config.get(
        "range_checks",
        {},
    )

    if range_checks.get("enabled", False):

        for column_name, rules in schema_config.get(
            "columns",
            {},
        ).items():

            if column_name not in table.column_names:
                continue

            column = table.column(column_name)

            minimum = rules.get("min")
            maximum = rules.get("max")

            if minimum is not None:
                below_minimum = pc.less(
                    column,
                    minimum,
                )

                count = pc.sum(
                    pc.fill_null(below_minimum, False)
                ).as_py()

                if count > 0:
                    errors.append(
                        f"{column_name}: found {count} "
                        f"values below minimum {minimum}"
                    )

            if maximum is not None:
                above_maximum = pc.greater(
                    column,
                    maximum,
                )

                count = pc.sum(
                    pc.fill_null(above_maximum, False)
                ).as_py()

                if count > 0:
                    errors.append(
                        f"{column_name}: found {count} "
                        f"values above maximum {maximum}"
                    )

    return errors