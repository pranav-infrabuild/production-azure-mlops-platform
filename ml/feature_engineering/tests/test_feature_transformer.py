from __future__ import annotations

import pandas as pd
import pytest

from ml.feature_engineering.src.feature_transformer import (
    COUNTRY_MAPPING,
    create_features,
    validate_input_columns,
)


FEATURE_CONFIG = {
    "features": {
        "amount_log": {
            "transformation": "log1p",
        },
        "risk_score_squared": {
            "transformation": "square",
        },
        "amount_risk_ratio": {
            "transformation": "divide",
        },
        "country_code": {
            "transformation": "categorical_encoding",
        },
    }
}


@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "transaction_id": [
                "TXN001",
                "TXN002",
            ],
            "amount": [
                100.0,
                200.0,
            ],
            "country": [
                "IN",
                "US",
            ],
            "risk_score": [
                0.10,
                0.20,
            ],
        }
    )


def test_create_features(sample_dataframe):
    result = create_features(
        dataframe=sample_dataframe,
        feature_config=FEATURE_CONFIG,
    )

    assert "amount_log" in result.columns
    assert "risk_score_squared" in result.columns
    assert "amount_risk_ratio" in result.columns
    assert "country_code" in result.columns


def test_amount_log(sample_dataframe):
    result = create_features(
        dataframe=sample_dataframe,
        feature_config=FEATURE_CONFIG,
    )

    assert result.loc[0, "amount_log"] == pytest.approx(
        4.6151205,
        rel=1e-5,
    )


def test_risk_score_squared(sample_dataframe):
    result = create_features(
        dataframe=sample_dataframe,
        feature_config=FEATURE_CONFIG,
    )

    assert result.loc[0, "risk_score_squared"] == pytest.approx(
        0.01
    )


def test_amount_risk_ratio(sample_dataframe):
    result = create_features(
        dataframe=sample_dataframe,
        feature_config=FEATURE_CONFIG,
    )

    assert result.loc[0, "amount_risk_ratio"] == pytest.approx(
        1000.0
    )


def test_country_mapping(sample_dataframe):
    result = create_features(
        dataframe=sample_dataframe,
        feature_config=FEATURE_CONFIG,
    )

    assert result.loc[0, "country_code"] == COUNTRY_MAPPING["IN"]
    assert result.loc[1, "country_code"] == COUNTRY_MAPPING["US"]


def test_missing_required_column():
    dataframe = pd.DataFrame(
        {
            "transaction_id": ["TXN001"],
            "amount": [100.0],
            "country": ["IN"],
        }
    )

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_input_columns(dataframe)