from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import pandas as pd
import yaml
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor


def load_config(config_path: str) -> dict[str, Any]:
    """Load evaluation configuration."""

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def load_dataset(input_path: str) -> pd.DataFrame:
    """Load the feature dataset."""

    return pd.read_parquet(input_path)


def evaluate_model(
    model_path: str,
    dataframe: pd.DataFrame,
    feature_columns: list[str],
    target_column: str,
) -> float:
    """Evaluate the trained XGBoost model using MAE."""

    missing_columns = [
        column
        for column in feature_columns + [target_column]
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            "Missing required evaluation columns: "
            + ", ".join(missing_columns)
        )

    features = dataframe[feature_columns]
    target = dataframe[target_column]

    model = XGBRegressor()
    model.load_model(model_path)

    predictions = model.predict(features)

    return float(
        mean_absolute_error(
            target,
            predictions,
        )
    )


def create_evaluation_report(
    metric: str,
    score: float,
    threshold: float,
    direction: str,
) -> dict[str, Any]:
    """Create the model evaluation quality-gate report."""

    if metric != "mae":
        raise ValueError(
            f"Unsupported evaluation metric: {metric}"
        )

    if direction == "less_than_or_equal":
        passed = score <= threshold
    else:
        raise ValueError(
            f"Unsupported evaluation direction: {direction}"
        )

    return {
        "metric": metric,
        "score": score,
        "threshold": threshold,
        "direction": direction,
        "passed": passed,
        "promotion_eligible": passed,
    }


def run_evaluation(
    model_path: str,
    input_path: str,
    config_path: str,
    report_path: str,
) -> dict[str, Any]:
    """Run model evaluation and write the quality-gate report."""

    config = load_config(config_path)

    evaluation_config = config["evaluation"]
    model_config = config["model"]

    if model_config["algorithm"] != "xgboost":
        raise ValueError(
            "This evaluator currently supports XGBoost only."
        )

    dataframe = load_dataset(input_path)

    feature_columns = [
        "amount",
        "amount_log",
        "country_code",
    ]

    target_column = "risk_score"

    score = evaluate_model(
        model_path=model_path,
        dataframe=dataframe,
        feature_columns=feature_columns,
        target_column=target_column,
    )

    report = create_evaluation_report(
        metric=evaluation_config["metric"],
        score=score,
        threshold=evaluation_config["threshold"],
        direction=evaluation_config["direction"],
    )

    report["model"] = {
        "algorithm": model_config["algorithm"],
        "task": model_config["task"],
        "path": model_path,
    }

    output_path = Path(report_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        output_path,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            report,
            file,
            indent=2,
        )

    print(
        f"Evaluation completed. "
        f"MAE: {score:.4f}"
    )

    print(
        f"Quality gate: "
        f"{'PASSED' if report['passed'] else 'FAILED'}"
    )

    print(
        f"Evaluation report: {output_path}"
    )

    return report


def main() -> None:
    """CLI entry point."""

    parser = argparse.ArgumentParser(
        description="Evaluate an XGBoost model."
    )

    parser.add_argument(
        "--model",
        required=True,
        help="Path to trained XGBoost model.",
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to feature Parquet dataset.",
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to evaluation configuration.",
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Path for evaluation report.",
    )

    args = parser.parse_args()

    report = run_evaluation(
        model_path=args.model,
        input_path=args.input,
        config_path=args.config,
        report_path=args.report,
    )

    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()