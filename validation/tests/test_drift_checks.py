from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

from validation.src.drift_checks import validate_drift


def _write_parquet(path: Path, data: dict) -> None:
    table = pa.table(data)
    pq.write_table(table, path)


def _schema_config() -> dict:
    return {
        "columns": {
            "transaction_id": {
                "type": "string",
            },
            "amount": {
                "type": "double",
            },
            "country": {
                "type": "string",
            },
            "risk_score": {
                "type": "double",
            },
        }
    }


def _drift_config() -> dict:
    return {
        "enabled": True,
        "mode": "warning",
    }


def test_no_drift(tmp_path):
    baseline = tmp_path / "baseline.parquet"
    current = tmp_path / "current.parquet"

    data = {
        "transaction_id": ["TXN001", "TXN002"],
        "amount": [100.0, 200.0],
        "country": ["IN", "US"],
        "risk_score": [0.10, 0.80],
    }

    _write_parquet(baseline, data)
    _write_parquet(current, data)

    warnings = validate_drift(
        str(current),
        str(baseline),
        _drift_config(),
        _schema_config(),
    )

    assert warnings == []


def test_detect_record_count_drift(tmp_path):
    baseline = tmp_path / "baseline.parquet"
    current = tmp_path / "current.parquet"

    _write_parquet(
        baseline,
        {
            "transaction_id": ["TXN001", "TXN002", "TXN003", "TXN004", "TXN005"],
            "amount": [100.0, 200.0, 300.0, 400.0, 500.0],
            "country": ["IN", "US", "GB", "DE", "FR"],
            "risk_score": [0.10, 0.20, 0.30, 0.40, 0.50],
        },
    )

    _write_parquet(
        current,
        {
            "transaction_id": ["TXN001", "TXN002"],
            "amount": [100.0, 200.0],
            "country": ["IN", "US"],
            "risk_score": [0.10, 0.20],
        },
    )

    warnings = validate_drift(
        str(current),
        str(baseline),
        _drift_config(),
        _schema_config(),
    )

    assert any(
        "Record count drift detected" in warning
        for warning in warnings
    )


def test_detect_numeric_mean_drift(tmp_path):
    baseline = tmp_path / "baseline.parquet"
    current = tmp_path / "current.parquet"

    _write_parquet(
        baseline,
        {
            "transaction_id": ["TXN001", "TXN002"],
            "amount": [100.0, 200.0],
            "country": ["IN", "US"],
            "risk_score": [0.10, 0.20],
        },
    )

    _write_parquet(
        current,
        {
            "transaction_id": ["TXN003", "TXN004"],
            "amount": [1000.0, 1200.0],
            "country": ["IN", "US"],
            "risk_score": [0.10, 0.20],
        },
    )

    warnings = validate_drift(
        str(current),
        str(baseline),
        _drift_config(),
        _schema_config(),
    )

    assert any(
        "amount: mean drift detected" in warning
        for warning in warnings
    )