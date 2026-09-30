from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import mlflow
import mlflow.xgboost
import pandas as pd
import yaml
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor


def load_config(config_path: str) -> dict[str, Any]:
    """Load training configuration from YAML."""

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def load_dataset(input_path: str) -> pd.DataFrame:
    """Load the feature dataset."""

    return pd.read_parquet(input_path)


def prepare_training_data(
    dataframe: pd.DataFrame,
    feature_columns: list[str],
    target_column: str,
) -> tuple[pd.DataFrame, pd.Series]:
    """Prepare model features and target."""

    missing_columns = [
        column
        for column in feature_columns + [target_column]
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            "Missing required training columns: "
            + ", ".join(missing_columns)
        )

    features = dataframe[feature_columns].copy()
    target = dataframe[target_column].copy()

    return features, target


def train_model(
    features: pd.DataFrame,
    target: pd.Series,
    training_config: dict[str, Any],
) -> tuple[XGBRegressor, float]:
    """Train XGBoost regression model and calculate MAE."""

    test_size = training_config.get("test_size", 0.2)
    random_state = training_config.get("random_state", 42)

    x_train, x_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=test_size,
        random_state=random_state,
    )

    parameters = training_config.get("parameters", {})

    model = XGBRegressor(
        objective="reg:squarederror",
        random_state=random_state,
        **parameters,
    )

    model.fit(
        x_train,
        y_train,
    )

    predictions = model.predict(x_test)

    mae = mean_absolute_error(
        y_test,
        predictions,
    )

    return model, float(mae)


def run_training(
    input_path: str,
    config_path: str,
    model_output_path: str,
) -> None:
    """Run the complete ML training workflow."""

    config = load_config(config_path)

    dataset_config = config["dataset"]
    training_config = config["training"]
    feature_config = config["features"]
    mlflow_config = config["mlflow"]

    target_column = dataset_config["target_column"]
    feature_columns = feature_config["numerical"]

    dataframe = load_dataset(input_path)

    features, target = prepare_training_data(
        dataframe=dataframe,
        feature_columns=feature_columns,
        target_column=target_column,
    )

    mlflow.set_experiment(
        mlflow_config["experiment_name"]
    )

    with mlflow.start_run(
        run_name=mlflow_config["run_name"]
    ):
        mlflow.log_params(
            training_config["parameters"]
        )

        mlflow.log_param(
            "algorithm",
            training_config["algorithm"],
        )

        mlflow.log_param(
            "task",
            training_config["task"],
        )

        mlflow.log_param(
            "feature_columns",
            ",".join(feature_columns),
        )

        mlflow.log_param(
            "target_column",
            target_column,
        )

        mlflow.log_param(
            "training_rows",
            len(features),
        )

        model, score = train_model(
            features=features,
            target=target,
            training_config=training_config,
        )

        mlflow.log_metric(
            "test_mae",
            score,
        )

        output_path = Path(model_output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        model.save_model(
            output_path,
        )

        mlflow.xgboost.log_model(
            model,
            name="model",
        )

        print(
            f"Training completed successfully. "
            f"Test MAE: {score:.4f}"
        )

        print(
            f"Model saved to: {output_path}"
        )


def main() -> None:
    """CLI entry point."""

    parser = argparse.ArgumentParser(
        description="Train XGBoost transaction risk model."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to feature Parquet dataset.",
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to training configuration.",
    )

    parser.add_argument(
        "--model-output",
        required=True,
        help="Path for trained XGBoost model.",
    )

    args = parser.parse_args()

    run_training(
        input_path=args.input,
        config_path=args.config,
        model_output_path=args.model_output,
    )


if __name__ == "__main__":
    main()