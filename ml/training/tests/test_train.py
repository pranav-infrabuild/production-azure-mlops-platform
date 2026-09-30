from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from ml.training.src.train import (
    prepare_training_data,
    train_model,
)


def test_prepare_training_data():
    dataframe = pd.DataFrame(
        {
            "transaction_id": [
                "TXN001",
                "TXN002",
            ],
            "amount": [
                100.0,
                200.0,
            ],
            "amount_log": [
                4.6151,
                5.3033,
            ],
            "country_code": [
                1,
                2,
            ],
            "risk_score": [
                0.10,
                0.20,
            ],
        }
    )

    features, target = prepare_training_data(
        dataframe=dataframe,
        feature_columns=[
            "amount",
            "amount_log",
            "country_code",
        ],
        target_column="risk_score",
    )

    assert list(features.columns) == [
        "amount",
        "amount_log",
        "country_code",
    ]

    assert target.name == "risk_score"

    assert len(features) == 2
    assert len(target) == 2


def test_missing_training_column():
    dataframe = pd.DataFrame(
        {
            "amount": [100.0],
            "risk_score": [0.10],
        }
    )

    with pytest.raises(
        ValueError,
        match="Missing required training columns",
    ):
        prepare_training_data(
            dataframe=dataframe,
            feature_columns=[
                "amount",
                "amount_log",
                "country_code",
            ],
            target_column="risk_score",
        )


def test_train_model():
    features = pd.DataFrame(
        {
            "amount": [
                100.0,
                200.0,
                300.0,
                400.0,
                500.0,
                600.0,
                700.0,
                800.0,
                900.0,
                1000.0,
            ],
            "amount_log": [
                4.6151,
                5.3033,
                5.7071,
                5.9939,
                6.2166,
                6.3986,
                6.5525,
                6.6859,
                6.8024,
                6.9088,
            ],
            "country_code": [
                1,
                2,
                1,
                3,
                2,
                1,
                3,
                2,
                1,
                3,
            ],
        }
    )

    target = pd.Series(
        [
            0.10,
            0.20,
            0.30,
            0.40,
            0.50,
            0.60,
            0.70,
            0.80,
            0.90,
            0.95,
        ],
        name="risk_score",
    )

    training_config = {
        "test_size": 0.2,
        "random_state": 42,
        "parameters": {
            "n_estimators": 10,
            "max_depth": 2,
            "learning_rate": 0.1,
        },
    }

    model, mae = train_model(
        features=features,
        target=target,
        training_config=training_config,
    )

    assert model is not None
    assert mae >= 0
    assert isinstance(mae, float)