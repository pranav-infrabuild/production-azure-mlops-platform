from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

from validation.src.schema_checks import validate_schema


def _write_parquet(path: Path, data: dict) -> None:
    table = pa.table(data)
    pq.write_table(table, path)


def test_valid_schema(tmp_path):
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

    config = {
        "required_columns": [
            "transaction_id",
            "amount",
            "country",
            "risk_score",
        ],
        "columns": {
            "transaction_id": {"type": "string"},
            "amount": {"type": "double"},
            "country": {"type": "string"},
            "risk_score": {"type": "double"},
        },
    }

    errors = validate_schema(
        str(parquet_path),
        config,
    )

    assert errors == []


def test_missing_required_column(tmp_path):
    parquet_path = tmp_path / "invalid.parquet"

    _write_parquet(
        parquet_path,
        {
            "transaction_id": ["TXN001"],
            "amount": [100.0],
            "country": ["IN"],
        },
    )

    config = {
        "required_columns": [
            "transaction_id",
            "amount",
            "country",
            "risk_score",
        ],
        "columns": {
            "transaction_id": {"type": "string"},
            "amount": {"type": "double"},
            "country": {"type": "string"},
            "risk_score": {"type": "double"},
        },
    }

    errors = validate_schema(
        str(parquet_path),
        config,
    )

    assert "Missing required column: risk_score" in errors