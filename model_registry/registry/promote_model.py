from __future__ import annotations

import argparse
import json
from pathlib import Path

import mlflow
from mlflow import MlflowClient


def load_evaluation_report(report_path: str) -> dict:
    """Load the model evaluation report."""

    path = Path(report_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Evaluation report not found: {report_path}"
        )

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def promote_to_candidate(
    model_name: str,
    model_version: int,
    evaluation_report: str,
) -> None:
    """Promote a model version to the candidate alias."""

    report = load_evaluation_report(evaluation_report)

    if not report.get("passed", False):
        raise ValueError(
            "Model failed the evaluation quality gate. "
            "Promotion to candidate is blocked."
        )

    if not report.get("promotion_eligible", False):
        raise ValueError(
            "Model is not promotion eligible. "
            "Promotion to candidate is blocked."
        )

    client = MlflowClient()

    client.set_registered_model_alias(
        name=model_name,
        alias="candidate",
        version=model_version,
    )

    client.set_model_version_tag(
        name=model_name,
        version=model_version,
        key="promotion_status",
        value="candidate",
    )

    print("Model promotion completed.")
    print(f"Model: {model_name}")
    print(f"Version: {model_version}")
    print("Alias: candidate")
    print("Quality gate: PASSED")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Promote a validated MLflow model to candidate."
    )

    parser.add_argument(
        "--model-name",
        required=True,
        help="Registered model name.",
    )

    parser.add_argument(
        "--model-version",
        required=True,
        type=int,
        help="Model version to promote.",
    )

    parser.add_argument(
        "--evaluation-report",
        required=True,
        help="Path to the evaluation report JSON.",
    )

    args = parser.parse_args()

    promote_to_candidate(
        model_name=args.model_name,
        model_version=args.model_version,
        evaluation_report=args.evaluation_report,
    )


if __name__ == "__main__":
    main()