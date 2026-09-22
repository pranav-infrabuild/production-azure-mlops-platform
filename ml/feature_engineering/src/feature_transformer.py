from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


COUNTRY_MAPPING = {
    "IN": 1,
    "US": 2,
    "GB": 3,
}


def load_dataset(input_path: str) -> pd.DataFrame:
    """Load the processed transaction dataset."""

    return pd.read_parquet(input_path)


def validate_input_columns(
    dataframe: pd.DataFrame,
) -> None:
    """Validate that required input columns are present."""

    required_columns = {
        "transaction_id",
        "amount",
        "country",
        "risk_score",
    }

    missing_columns = required_columns - set(dataframe.columns)

    if missing_columns:
        raise ValueError(
            "Missing required columns: "
            + ", ".join(sorted(missing_columns))
        )


def create_features(
    dataframe: pd.DataFrame,
    feature_config: dict[str, Any],
) -> pd.DataFrame:
    """
    Create model features from the processed transaction dataset.

    The transformation logic is driven by feature_rules.yaml.
    """

    validate_input_columns(dataframe)

    result = dataframe.copy()

    features = feature_config.get("features", {})

    # ---------------------------------------------------------
    # amount_log
    # ---------------------------------------------------------

    if "amount_log" in features:
        result["amount_log"] = np.log1p(
            result["amount"].astype(float)
        )

    # ---------------------------------------------------------
    # risk_score_squared
    # ---------------------------------------------------------

    if "risk_score_squared" in features:
        result["risk_score_squared"] = (
            result["risk_score"].astype(float) ** 2
        )

    # ---------------------------------------------------------
    # amount_risk_ratio
    # ---------------------------------------------------------

    if "amount_risk_ratio" in features:

        risk_score = result["risk_score"].astype(float)

        result["amount_risk_ratio"] = np.where(
            risk_score != 0,
            result["amount"].astype(float) / risk_score,
            0.0,
        )

    # ---------------------------------------------------------
    # country_code
    # ---------------------------------------------------------

    if "country_code" in features:

        result["country_code"] = (
            result["country"]
            .map(COUNTRY_MAPPING)
            .fillna(0)
            .astype(int)
        )

    return result


def transform_dataset(
    input_path: str,
    output_path: str,
    feature_config: dict[str, Any],
) -> pd.DataFrame:
    """Transform the input dataset and save the feature dataset."""

    dataframe = load_dataset(input_path)

    transformed = create_features(
        dataframe=dataframe,
        feature_config=feature_config,
    )

    transformed.to_parquet(
        output_path,
        index=False,
    )

    return transformed