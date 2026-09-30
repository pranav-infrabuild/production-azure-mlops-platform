from __future__ import annotations

import pytest

from ml.evaluation.src.evaluate import create_evaluation_report


def test_evaluation_passes_when_mae_is_below_threshold():
    report = create_evaluation_report(
        metric="mae",
        score=0.1671,
        threshold=0.70,
        direction="less_than_or_equal",
    )

    assert report["metric"] == "mae"
    assert report["score"] == pytest.approx(0.1671)
    assert report["threshold"] == 0.70
    assert report["passed"] is True
    assert report["promotion_eligible"] is True


def test_evaluation_fails_when_mae_exceeds_threshold():
    report = create_evaluation_report(
        metric="mae",
        score=0.85,
        threshold=0.70,
        direction="less_than_or_equal",
    )

    assert report["passed"] is False
    assert report["promotion_eligible"] is False


def test_unsupported_metric():
    with pytest.raises(
        ValueError,
        match="Unsupported evaluation metric",
    ):
        create_evaluation_report(
            metric="rmse",
            score=0.20,
            threshold=0.70,
            direction="less_than_or_equal",
        )


def test_unsupported_direction():
    with pytest.raises(
        ValueError,
        match="Unsupported evaluation direction",
    ):
        create_evaluation_report(
            metric="mae",
            score=0.20,
            threshold=0.70,
            direction="greater_than",
        )