FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    xgboost \
    mlflow

COPY ml ./ml

CMD ["python", "-m", "ml.training.src.train", "--help"]