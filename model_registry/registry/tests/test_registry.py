from __future__ import annotations

import json

import pytest

from model_registry.registry.promote_model import (
    load_evaluation_report,
    promote_to_candidate,
)


def test_load_evaluation_report(tmp_path):
    report = {
        "metric": "mae",
        "score": 0.1671,
        "threshold": 0.7,
        "passed": True,
        "promotion_eligible": True,
    }

    report_path = tmp_path / "evaluation_report.json"
    report_path.write_text(json.dumps(report), encoding="utf-8")

    result = load_evaluation_report(str(report_path))

    assert result["metric"] == "mae"
    assert result["passed"] is True
    assert result["promotion_eligible"] is True


def test_missing_evaluation_report():
    with pytest.raises(FileNotFoundError):
        load_evaluation_report("does-not-exist.json")


def test_failed_quality_gate(tmp_path):
    report = {
        "metric": "mae",
        "score": 1.2,
        "threshold": 0.7,
        "passed": False,
        "promotion_eligible": False,
    }

    report_path = tmp_path / "evaluation_report.json"
    report_path.write_text(json.dumps(report), encoding="utf-8")

    with pytest.raises(ValueError, match="failed the evaluation quality gate"):
        promote_to_candidate(
            model_name="test-model",
            model_version=1,
            evaluation_report=str(report_path),
        )


def test_not_promotion_eligible(tmp_path):
    report = {
        "metric": "mae",
        "score": 0.5,
        "threshold": 0.7,
        "passed": True,
        "promotion_eligible": False,
    }

    report_path = tmp_path / "evaluation_report.json"
    report_path.write_text(json.dumps(report), encoding="utf-8")

    with pytest.raises(ValueError, match="not promotion eligible"):
        promote_to_candidate(
            model_name="test-model",
            model_version=1,
            evaluation_report=str(report_path),
        )