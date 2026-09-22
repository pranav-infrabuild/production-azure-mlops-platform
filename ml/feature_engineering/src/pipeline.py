from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

from ml.feature_engineering.src.feature_transformer import (
    transform_dataset,
)


def load_config(config_path: str) -> dict[str, Any]:
    """Load feature engineering configuration."""

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def run_pipeline(
    input_path: str,
    output_path: str,
    config_path: str,
) -> None:
    """Run the feature engineering pipeline."""

    if not Path(input_path).exists():
        raise FileNotFoundError(
            f"Input dataset not found: {input_path}"
        )

    config = load_config(config_path)

    transformed = transform_dataset(
        input_path=input_path,
        output_path=output_path,
        feature_config=config,
    )

    print("Feature engineering completed successfully.")
    print(f"Input dataset : {input_path}")
    print(f"Output dataset: {output_path}")
    print(f"Records       : {len(transformed)}")
    print(
        "Features      : "
        + ", ".join(transformed.columns)
    )


def main() -> None:
    """CLI entry point."""

    parser = argparse.ArgumentParser(
        description="Run transaction feature engineering."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to processed Parquet dataset.",
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path for generated feature dataset.",
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to feature rules YAML.",
    )

    args = parser.parse_args()

    run_pipeline(
        input_path=args.input,
        output_path=args.output,
        config_path=args.config,
    )


if __name__ == "__main__":
    main()