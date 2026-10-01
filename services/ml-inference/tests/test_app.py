from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_readiness_without_model():
    response = client.get("/ready")

    assert response.status_code == 503
    assert response.json()["detail"] == "Model is not loaded"