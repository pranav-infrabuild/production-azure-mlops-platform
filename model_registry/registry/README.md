# MLflow Model Registry

This component manages model registration and promotion for the Azure MLOps platform.

## Model Lifecycle

```text
ML Training
    |
    v
MLflow Run
    |
    v
Model Evaluation
    |
    v
Quality Gate
    |
    | PASSED
    v
MLflow Model Registry
    |
    v
Model Version
    |
    v
candidate