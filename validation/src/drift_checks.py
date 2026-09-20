from __future__ import annotations

from typing import Any

import pyarrow.compute as pc
import pyarrow.parquet as pq


def _calculate_numeric_stats(
    parquet_path: str,
    column_name: str,
) -> dict[str, float]:
    """Calculate basic statistics for a numeric column."""

    table = pq.read_table(parquet_path, columns=[column_name])
    values = table[column_name].drop_null()

    if len(values) == 0:
        return {}

    mean_value = pc.mean(values).as_py()
    min_value = pc.min(values).as_py()
    max_value = pc.max(values).as_py()

    return {
        "mean": float(mean_value),
        "min": float(min_value),
        "max": float(max_value),
    }


def validate_drift(
    current_parquet_path: str,
    baseline_parquet_path: str,
    drift_config: dict[str, Any],
    schema_config: dict[str, Any],
) -> list[str]:
    """
    Compare the current dataset against a baseline dataset.

    Drift is reported as a warning when configured thresholds
    are exceeded.

    Returns:
        A list of drift warnings.
        An empty list means no significant drift was detected.
    """

    warnings: list[str] = []

    if not drift_config.get("enabled", False):
        return warnings

    mode = drift_config.get("mode", "warning")

    if mode != "warning":
        warnings.append(
            f"Unsupported drift mode '{mode}', "
            "using warning mode"
        )

    current_table = pq.read_table(current_parquet_path)
    baseline_table = pq.read_table(baseline_parquet_path)

    current_count = current_table.num_rows
    baseline_count = baseline_table.num_rows

    # ---------------------------------------------------------
    # Record count drift
    # ---------------------------------------------------------
    if baseline_count > 0:
        record_count_change = abs(
            current_count - baseline_count
        ) / baseline_count

        if record_count_change > 0.20:
            warnings.append(
                "Record count drift detected: "
                f"baseline={baseline_count}, "
                f"current={current_count}, "
                f"change={record_count_change:.2%}"
            )

    # ---------------------------------------------------------
    # Numeric feature drift
    # ---------------------------------------------------------
    for column_name, rules in schema_config.get(
        "columns",
        {},
    ).items():

        expected_type = rules.get("type")

        if expected_type != "double":
            continue

        if column_name not in current_table.column_names:
            continue

        if column_name not in baseline_table.column_names:
            continue

        current_stats = _calculate_numeric_stats(
            current_parquet_path,
            column_name,
        )

        baseline_stats = _calculate_numeric_stats(
            baseline_parquet_path,
            column_name,
        )

        if not current_stats or not baseline_stats:
            continue

        baseline_mean = baseline_stats["mean"]

        if baseline_mean == 0:
            continue

        mean_change = abs(
            current_stats["mean"] - baseline_mean
        ) / abs(baseline_mean)

        if mean_change > 0.20:
            warnings.append(
                f"{column_name}: mean drift detected: "
                f"baseline={baseline_mean:.4f}, "
                f"current={current_stats['mean']:.4f}, "
                f"change={mean_change:.2%}"
            )

    return warnings