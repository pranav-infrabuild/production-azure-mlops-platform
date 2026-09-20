from __future__ import annotations

from typing import Any

import pyarrow as pa
import pyarrow.parquet as pq


def _is_string_type(data_type: pa.DataType) -> bool:
    return pa.types.is_string(data_type) or pa.types.is_large_string(data_type)


def _is_numeric_type(data_type: pa.DataType) -> bool:
    return pa.types.is_integer(data_type) or pa.types.is_floating(data_type)


def _validate_column_type(
    column_name: str,
    actual_type: pa.DataType,
    expected_type: str,
) -> list[str]:
    errors: list[str] = []

    if expected_type == "string":
        if not _is_string_type(actual_type):
            errors.append(
                f"{column_name}: expected string, found {actual_type}"
            )

    elif expected_type == "double":
        if not _is_numeric_type(actual_type):
            errors.append(
                f"{column_name}: expected numeric type, found {actual_type}"
            )

    else:
        errors.append(
            f"{column_name}: unsupported expected type '{expected_type}'"
        )

    return errors


def validate_schema(
    parquet_path: str,
    schema_config: dict[str, Any],
) -> list[str]:
    """
    Validate a Parquet file against the configured schema contract.

    Returns:
        A list of validation errors.
        An empty list means the schema passed validation.
    """

    errors: list[str] = []

    parquet_schema = pq.read_schema(parquet_path)
    available_columns = set(parquet_schema.names)

    required_columns = schema_config.get("required_columns", [])
    configured_columns = schema_config.get("columns", {})

    # Required columns
    missing_columns = [
        column
        for column in required_columns
        if column not in available_columns
    ]

    for column in missing_columns:
        errors.append(f"Missing required column: {column}")

    # Column types
    for column_name, rules in configured_columns.items():
        if column_name not in available_columns:
            continue

        actual_type = parquet_schema.field(column_name).type
        expected_type = rules.get("type")

        errors.extend(
            _validate_column_type(
                column_name,
                actual_type,
                expected_type,
            )
        )

    # Unexpected columns
    expected_columns = set(configured_columns.keys())

    unexpected_columns = sorted(
        available_columns - expected_columns
    )

    if unexpected_columns:
        errors.append(
            "Unexpected columns: "
            + ", ".join(unexpected_columns)
        )

    return errors