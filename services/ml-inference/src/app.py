from __future__ import annotations

import os
from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from xgboost import XGBRegressor


MODEL_PATH = Path(
    os.getenv(
        "MODEL_PATH",
        "/models/xgboost-risk-model.json",
    )
)

FEATURE_COLUMNS = [
    "amount",
    "amount_log",
    "country_code",
]

app = FastAPI(
    title="Transaction Risk Inference API",
    version="1.0.0",
)

model: XGBRegressor | None = None


class PredictionRequest(BaseModel):
    amount: float
    amount_log: float
    country_code: int


class PredictionResponse(BaseModel):
    risk_score: float
    model: str
    version: str


@app.on_event("startup")
def load_model() -> None:
    global model

    if not MODEL_PATH.exists():
        raise RuntimeError(
            f"Model file not found: {MODEL_PATH}"
        )

    loaded_model = XGBRegressor()
    loaded_model.load_model(str(MODEL_PATH))

    model = loaded_model


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/ready")
def readiness() -> dict[str, str]:
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model is not loaded",
        )

    return {"status": "ready"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model is not loaded",
        )

    features = pd.DataFrame(
        [
            {
                "amount": request.amount,
                "amount_log": request.amount_log,
                "country_code": request.country_code,
            }
        ],
        columns=FEATURE_COLUMNS,
    )

    prediction = float(model.predict(features)[0])

    return PredictionResponse(
        risk_score=prediction,
        model="transaction-risk-xgboost",
        version=os.getenv("MODEL_VERSION", "unknown"),
    )