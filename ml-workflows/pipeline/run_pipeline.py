from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def run_step(name: str, command: list[str]) -> None:
    """Run one pipeline stage and stop if it fails."""

    print()
    print("=" * 70)
    print(f"STARTING: {name}")
    print("=" * 70)

    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        check=False,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Pipeline stage failed: {name} "
            f"(exit code {result.returncode})"
        )

    print()
    print(f"COMPLETED: {name}")


def run_pipeline() -> None:
    """Execute the ML workflow in dependency order."""

    python = sys.executable

    stages = [
        (
            "Validation Tests",
            [
                python,
                "-m",
                "pytest",
                "validation/tests",
                "-v",
            ],
        ),
        (
            "Feature Engineering Tests",
            [
                python,
                "-m",
                "pytest",
                "ml/feature_engineering/tests",
                "-v",
            ],
        ),
        (
            "ML Training Tests",
            [
                python,
                "-m",
                "pytest",
                "ml/training/tests",
                "-v",
            ],
        ),
        (
            "Model Evaluation Tests",
            [
                python,
                "-m",
                "pytest",
                "ml/evaluation/tests",
                "-v",
            ],
        ),
        (
            "Model Registry Tests",
            [
                python,
                "-m",
                "pytest",
                "model_registry/registry/tests",
                "-v",
            ],
        ),
    ]

    for name, command in stages:
        run_step(name, command)

    print()
    print("=" * 70)
    print("ML WORKFLOW VALIDATION COMPLETED SUCCESSFULLY")
    print("=" * 70)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the Azure MLOps ML workflow validation pipeline."
    )

    parser.parse_args()

    run_pipeline()


if __name__ == "__main__":
    main()