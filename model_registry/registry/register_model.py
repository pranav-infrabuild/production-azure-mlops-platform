from __future__ import annotations

import argparse
from pathlib import Path

import mlflow
from mlflow import MlflowClient


def register_model(
    model_uri: str,
    model_name: str,
    evaluation_report: str | None = None,
) -> str:
    """Register an MLflow model in the Model Registry."""

    client = MlflowClient()

    # Register the model version from the supplied MLflow model URI.
    registered_model = mlflow.register_model(
        model_uri=model_uri,
        name=model_name,
    )

    model_version = registered_model.version

    # Add useful metadata to the registered model version.
    client.set_model_version_tag(
        name=model_name,
        version=model_version,
        key="algorithm",
        value="xgboost",
    )

    client.set_model_version_tag(
        name=model_name,
        version=model_version,
        key="task",
        value="regression",
    )

    # Attach evaluation information when an evaluation report is available.
    if evaluation_report:
        report_path = Path(evaluation_report)

        if report_path.exists():
            client.set_model_version_tag(
                name=model_name,
                version=model_version,
                key="evaluation_report",
                value=str(report_path),
            )

    print("Model registration completed.")
    print(f"Model name: {model_name}")
    print(f"Model version: {model_version}")

    return str(model_version)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Register an MLflow model in the Model Registry."
    )

    parser.add_argument(
        "--model-uri",
        required=True,
        help="MLflow model URI, for example runs:/<run_id>/model",
    )

    parser.add_argument(
        "--model-name",
        required=True,
        help="Registered model name.",
    )

    parser.add_argument(
        "--evaluation-report",
        required=False,
        help="Optional path to the model evaluation report.",
    )

    args = parser.parse_args()

    register_model(
        model_uri=args.model_uri,
        model_name=args.model_name,
        evaluation_report=args.evaluation_report,
    )


if __name__ == "__main__":
    main()