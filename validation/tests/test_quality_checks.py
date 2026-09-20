from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

from validation.src.quality_checks import validate_quality


def _write_parquet(path: Path, data: dict) -> None:
    table = pa.table(data)
    pq.write_table(table, path)


def _quality_config() -> dict:
    return {
        "minimum_record_count": 1,
        "duplicate_check": {
            "enabled": True,
            "column": "transaction_id",
        },
        "null_check": {
            "enabled": True,
        },
        "range_checks": {
            "enabled": True,
        },
    }


def _schema_config() -> dict:
    return {
        "columns": {
            "transaction_id": {
                "type": "string",
                "nullable": False,
            },
            "amount": {
                "type": "double",
                "nullable": False,
                "min": 0,
            },
            "country": {
                "type": "string",
                "nullable": False,
            },
            "risk_score": {
                "type": "double",
                "nullable": False,
                "min": 0,
                "max": 1,
            },
        }
    }


def test_valid_quality(tmp_path):
    parquet_path = tmp_path / "valid.parquet"

    _write_parquet(
        parquet_path,
        {
            "transaction_id": ["TXN001", "TXN002"],
            "amount": [100.0, 200.0],
            "country": ["IN", "US"],
            "risk_score": [0.10, 0.80],
        },
    )

    errors = validate_quality(
        str(parquet_path),
        _quality_config(),
        _schema_config(),
    )

    assert errors == []


def test_detect_duplicate_records(tmp_path):
    parquet_path = tmp_path / "duplicate.parquet"

    _write_parquet(
        parquet_path,
        {
            "transaction_id": ["TXN001", "TXN001"],
            "amount": [100.0, 200.0],
            "country": ["IN", "US"],
            "risk_score": [0.10, 0.80],
        },
    )

    errors = validate_quality(
        str(parquet_path),
        _quality_config(),
        _schema_config(),
    )

    assert "transaction_id: found 1 duplicate records" in errors


def test_detect_null_values(tmp_path):
    parquet_path = tmp_path / "nulls.parquet"

    _write_parquet(
        parquet_path,
        {
            "transaction_id": ["TXN001", "TXN002"],
            "amount": [100.0, None],
            "country": ["IN", "US"],
            "risk_score": [0.10, 0.80],
        },
    )

    errors = validate_quality(
        str(parquet_path),
        _quality_config(),
        _schema_config(),
    )

    assert "amount: found 1 null values" in errors


def test_detect_out_of_range_values(tmp_path):
    parquet_path = tmp_path / "invalid_range.parquet"

    _write_parquet(
        parquet_path,
        {
            "transaction_id": ["TXN001", "TXN002"],
            "amount": [-100.0, 200.0],
            "country": ["IN", "US"],
            "risk_score": [0.10, 1.50],
        },
    )

    errors = validate_quality(
        str(parquet_path),
        _quality_config(),
        _schema_config(),
    )

    assert "amount: found 1 values below minimum 0" in errors
    assert "risk_score: found 1 values above maximum 1" in errors