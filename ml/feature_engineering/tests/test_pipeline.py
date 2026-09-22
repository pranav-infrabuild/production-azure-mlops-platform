from __future__ import annotations

from pathlib import Path

import pandas as pd
import yaml

from ml.feature_engineering.src.pipeline import run_pipeline


def test_feature_engineering_pipeline(tmp_path):
    input_path = tmp_path / "input.parquet"
    output_path = tmp_path / "features.parquet"
    config_path = tmp_path / "feature_rules.yaml"

    input_dataframe = pd.DataFrame(
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

    input_dataframe.to_parquet(
        input_path,
        index=False,
    )

    config = {
        "dataset": {
            "name": "transactions",
            "input_format": "parquet",
            "output_format": "parquet",
            "schema_version": "1.0",
        },
        "features": {
            "amount_log": {
                "source_column": "amount",
                "transformation": "log1p",
            },
            "risk_score_squared": {
                "source_column": "risk_score",
                "transformation": "square",
            },
            "amount_risk_ratio": {
                "source_columns": [
                    "amount",
                    "risk_score",
                ],
                "transformation": "divide",
            },
            "country_code": {
                "source_column": "country",
                "transformation": "categorical_encoding",
                "method": "ordinal",
            },
        },
    }

    config_path.write_text(
        yaml.safe_dump(config),
        encoding="utf-8",
    )

    run_pipeline(
        input_path=str(input_path),
        output_path=str(output_path),
        config_path=str(config_path),
    )

    assert Path(output_path).exists()

    result = pd.read_parquet(output_path)

    assert len(result) == 2

    expected_features = {
        "amount_log",
        "risk_score_squared",
        "amount_risk_ratio",
        "country_code",
    }

    assert expected_features.issubset(
        set(result.columns)
    )

    assert result.loc[0, "country_code"] == 1
    assert result.loc[1, "country_code"] == 2