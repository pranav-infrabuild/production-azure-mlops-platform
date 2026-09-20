from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

from validation.src.drift_checks import validate_drift
from validation.src.quality_checks import validate_quality
from validation.src.schema_checks import validate_schema


def load_config(config_path: str) -> dict[str, Any]:
    """Load validation rules from a YAML configuration file."""

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_dataset(
    parquet_path: str,
    config_path: str,
    baseline_parquet_path: str | None = None,
) -> dict[str, Any]:
    """
    Run all configured validation checks against a dataset.

    Validation stages:
        1. Schema validation
        2. Data quality validation
        3. Drift detection

    Returns:
        A structured validation result.
    """

    dataset_path = Path(parquet_path)

    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {parquet_path}"
        )

    config = load_config(config_path)

    schema_config = config.get("schema", {})
    quality_config = config.get("quality", {})
    drift_config = config.get("drift", {})

    # ---------------------------------------------------------
    # 1. Schema validation
    # ---------------------------------------------------------
    schema_errors = validate_schema(
        parquet_path,
        schema_config,
    )

    # ---------------------------------------------------------
    # 2. Data quality validation
    # ---------------------------------------------------------
    quality_errors = validate_quality(
        parquet_path,
        quality_config,
        schema_config,
    )

    # ---------------------------------------------------------
    # 3. Drift validation
    # ---------------------------------------------------------
    drift_warnings: list[str] = []

    if baseline_parquet_path:
        drift_warnings = validate_drift(
            parquet_path,
            baseline_parquet_path,
            drift_config,
            schema_config,
        )

    # ---------------------------------------------------------
    # Overall result
    # ---------------------------------------------------------
    passed = not schema_errors and not quality_errors

    return {
        "dataset": config.get("dataset", {}),
        "passed": passed,
        "schema": {
            "passed": not schema_errors,
            "errors": schema_errors,
        },
        "quality": {
            "passed": not quality_errors,
            "errors": quality_errors,
        },
        "drift": {
            "passed": not drift_warnings,
            "warnings": drift_warnings,
        },
    }


def main() -> None:
    """CLI entry point for the validation service."""

    parser = argparse.ArgumentParser(
        description="Run production data validation."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input Parquet dataset.",
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to the validation YAML configuration.",
    )

    parser.add_argument(
        "--baseline",
        required=False,
        default=None,
        help="Optional path to the baseline Parquet dataset.",
    )

    args = parser.parse_args()

    result = validate_dataset(
        parquet_path=args.input,
        config_path=args.config,
        baseline_parquet_path=args.baseline,
    )

    print(json.dumps(result, indent=2))

    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()