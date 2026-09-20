from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

from validation.src.validator import validate_dataset


def _write_parquet(path: Path, data: dict) -> None:
    table = pa.table(data)
    pq.write_table(table, path)


def test_valid_dataset_passes(tmp_path):
    parquet_path = tmp_path / "valid.parquet"
    config_path = Path("validation/config/transaction_rules.yaml")

    _write_parquet(
        parquet_path,
        {
            "transaction_id": ["TXN001", "TXN002"],
            "amount": [100.0, 200.0],
            "country": ["IN", "US"],
            "risk_score": [0.10, 0.80],
        },
    )

    result = validate_dataset(
        parquet_path=str(parquet_path),
        config_path=str(config_path),
    )

    assert result["passed"] is True
    assert result["schema"]["passed"] is True
    assert result["quality"]["passed"] is True


def test_invalid_dataset_fails_quality_gate(tmp_path):
    parquet_path = tmp_path / "invalid.parquet"
    config_path = Path("validation/config/transaction_rules.yaml")

    _write_parquet(
        parquet_path,
        {
            "transaction_id": ["TXN001", "TXN001"],
            "amount": [-100.0, 200.0],
            "country": ["IN", "US"],
            "risk_score": [0.10, 1.50],
        },
    )

    result = validate_dataset(
        parquet_path=str(parquet_path),
        config_path=str(config_path),
    )

    assert result["passed"] is False
    assert result["quality"]["passed"] is False
    assert len(result["quality"]["errors"]) > 0