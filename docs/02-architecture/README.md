# 🏗️ Platform Architecture

This document describes how the complete Production Azure MLOps & GenAI/RAG
Platform is designed and how its major components interact.

The architecture is divided into several layers:

```text
Users
  ↓
Application / API Layer
  ↓
ML & GenAI Workloads
  ↓
Data & Model Platform
  ↓
Infrastructure & Cloud Platform
  ↓
Security / Identity / Networking
  ↓
Observability & Operations


---

# 1. Overall Architecture

The platform contains two primary workloads:

1. **Classical Machine Learning**
2. **GenAI / Retrieval-Augmented Generation (RAG)**

Both workloads run on a common Azure platform.

```text
                                USERS
                                  │
                                  ▼
                       ┌─────────────────────┐
                       │ Application Gateway │
                       │        + WAF        │
                       └──────────┬──────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   AKS Ingress    │
                         └────────┬─────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
             ┌──────────────┐            ┌──────────────┐
             │ ML Inference │            │    RAG API   │
             │     API      │            │              │
             └──────┬───────┘            └──────┬───────┘
                    │                           │
                    ▼                           ▼
             ┌──────────────┐            ┌──────────────┐
             │ Feature      │            │   Qdrant     │
             │ Store/Feast  │            │ Vector DB    │
             └──────┬───────┘            └──────┬───────┘
                    │                           │
                    │                           ▼
                    │                    ┌──────────────┐
                    │                    │  Reranker    │
                    │                    └──────┬───────┘
                    │                           │
                    │                           ▼
                    │                    ┌──────────────┐
                    │                    │ Llama /      │
                    │                    │ Mistral LLM  │
                    │                    └──────────────┘
                    │
                    │
                    ▼
             ┌──────────────┐
             │   XGBoost    │
             │    Model     │
             └──────────────┘


              DATA & ML PLATFORM

Data Sources
     │
     ▼
Azure Data Factory
     │
     ▼
ADLS Gen2
     │
     ▼
Data Validation
     │
     ├─────────────── Invalid ───────────► Quarantine
     │
     ▼
Processed / Curated Data
     │
     ▼
Feature Engineering
     │
     ▼
Feature Store
     │
     ▼
XGBoost Training
     │
     ▼
MLflow
     │
     ▼
Model Registry
     │
     ▼
Evaluation
     │
     ▼
Deployment
     │
     ▼
AKS


             PLATFORM SERVICES

Terraform
Azure DevOps
Azure Key Vault
Entra ID / Managed Identity
Private Endpoints
Private DNS
Prometheus
Grafana
Azure Monitor
Log Analytics
Application Insights
```

---

# 2. Architecture Layers

The platform can be understood through the following layers.

## Layer 1 — User / Access Layer

Users interact with the platform through APIs or applications.

```text
User
  ↓
HTTPS
  ↓
Application Gateway
  ↓
WAF
```

The Application Gateway provides the external entry point and WAF provides
an additional security layer.

---

## Layer 2 — Application Layer

Application workloads run on AKS.

The primary services are:

```text
AKS
│
├── ML Inference API
├── RAG API
└── Health API
```

These services expose controlled APIs to consumers.

---

## Layer 3 — ML Layer

The ML workload contains:

```text
Feature Store
      ↓
XGBoost
      ↓
Model
      ↓
Inference API
```

The model is not treated as an isolated Python file.

It is part of a managed lifecycle involving training, evaluation,
registration, deployment and monitoring.

---

## Layer 4 — GenAI / RAG Layer

The RAG workload contains:

```text
Documents
    ↓
Ingestion
    ↓
Chunking
    ↓
Embeddings
    ↓
Qdrant
    ↓
Retrieval
    ↓
Reranking
    ↓
LLM
    ↓
RAG API
```

The RAG components are versioned and evaluated independently where
appropriate.

---

## Layer 5 — Data Layer

The data platform is based around:

```text
Data Sources
     ↓
Azure Data Factory
     ↓
ADLS Gen2
     ↓
Validation
     ↓
Processed / Curated Data
```

ADLS Gen2 acts as the primary data lake.

Delta Lake will be used for reliable dataset management and versioning.

---

## Layer 6 — MLOps Layer

The MLOps lifecycle includes:

```text
Training
   ↓
Experiment Tracking
   ↓
Model Evaluation
   ↓
Model Registry
   ↓
Deployment
   ↓
Monitoring
   ↓
Drift Detection
   ↓
Retraining
```

MLflow provides experiment tracking and model registry capabilities.

---

## Layer 7 — DevOps Layer

Azure DevOps manages software delivery:

```text
Git
 ↓
CI
 ↓
Testing
 ↓
Security Scanning
 ↓
Container Build
 ↓
ACR
 ↓
Continuous Testing
 ↓
Staging
 ↓
Approval
 ↓
Production
```

CI/CD is kept separate from the ML training workflow.

---

## Layer 8 — Infrastructure Layer

Terraform manages Azure infrastructure.

```text
Terraform
    ↓
Azure Resource Group
    ↓
VNet
    ├── AKS Subnet
    ├── Application Gateway Subnet
    └── Private Endpoint Subnet
```

Terraform will eventually manage the platform consistently across:

```text
dev
staging
prod
```

---

## Layer 9 — Security Layer

Security applies across the entire platform.

```text
Entra ID
     │
     ├── Managed Identity
     └── Workload Identity
              │
              ▼
          Azure Services

Key Vault
     │
     ▼
Secrets / Certificates

VNet
 │
 ├── NSGs
 ├── Private Endpoints
 └── Private DNS

AKS
 │
 └── Network Policies
```

Credentials should not be hardcoded in application code, Terraform files
or pipeline definitions.

---

## Layer 10 — Observability Layer

The platform must provide visibility into:

```text
Infrastructure
      │
      ├── CPU
      ├── Memory
      ├── Nodes
      └── Pods

Application
      │
      ├── Requests
      ├── Errors
      └── Latency

ML
      │
      ├── Predictions
      ├── Drift
      └── Model Performance

RAG / LLM
      │
      ├── Retrieval Quality
      ├── Groundedness
      ├── Latency
      └── Token Usage
```

Monitoring technologies include:

* Prometheus
* Grafana
* Azure Monitor
* Log Analytics
* Application Insights

---

# 3. End-to-End Platform View

The complete platform can therefore be viewed as:

```text
                         ┌─────────────┐
                         │    USERS    │
                         └──────┬──────┘
                                │
                                ▼
                    ┌──────────────────────┐
                    │ Application Gateway  │
                    │        + WAF         │
                    └──────────┬───────────┘
                               │
                               ▼
                         ┌───────────┐
                         │    AKS    │
                         └─────┬─────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
              ┌───────────┐         ┌───────────┐
              │ ML Inference│        │  RAG API  │
              └─────┬─────┘         └─────┬─────┘
                    │                     │
                    ▼                     ▼
              ┌───────────┐         ┌───────────┐
              │   Feast   │         │  Qdrant   │
              └─────┬─────┘         └─────┬─────┘
                    │                     │
                    ▼                     ▼
              ┌───────────┐         ┌───────────┐
              │  XGBoost  │         │ Reranker  │
              └───────────┘         └─────┬─────┘
                                          │
                                          ▼
                                    ┌───────────┐
                                    │    LLM    │
                                    └───────────┘


                         DATA PLATFORM

 Data Sources
      │
      ▼
     ADF
      │
      ▼
   ADLS Gen2
      │
      ▼
 Data Validation
      │
      ▼
 Feature Engineering
      │
      ▼
    Feast
      │
      ▼
   Training
      │
      ▼
   MLflow
      │
      ▼
 Model Registry
      │
      ▼
 Evaluation
      │
      ▼
 Deployment
      │
      ▼
     AKS
```

---

# 4. Cross-Cutting Platform Services

The following capabilities apply across the platform:

```text
                 ┌───────────────────────┐
                 │      SECURITY         │
                 └───────────┬───────────┘
                             │
                 ┌───────────┴───────────┐
                 │                       │
                 ▼                       ▼
            Identity                Networking
                 │                       │
                 ▼                       ▼
              Key Vault             Private DNS
                                      Private EP
                                      NSG
                                      NetworkPolicy


                 ┌───────────────────────┐
                 │    OBSERVABILITY      │
                 └───────────┬───────────┘
                             │
             ┌───────────────┼───────────────┐
             ▼               ▼               ▼
        Prometheus        Grafana       Azure Monitor


                 ┌───────────────────────┐
                 │      GOVERNANCE       │
                 └───────────┬───────────┘
                             │
             ┌───────────────┼───────────────┐
             ▼               ▼               ▼
          Model Cards      Audit          Lineage
```

---

# 5. Key Architectural Principle

The platform is intentionally divided into clear responsibilities.

```text
ADF
 ↓
Data ingestion / orchestration

ML Workflow
 ↓
Training / evaluation

MLflow
 ↓
Experiment tracking / model registry

Azure DevOps
 ↓
Software CI/CD

Terraform
 ↓
Infrastructure

AKS
 ↓
Production serving

Prometheus / Grafana / Azure Monitor
 ↓
Observability
```

This separation prevents the platform from becoming a collection of
overlapping tools with unclear responsibilities.




# 6. Data Flow Architecture

The data platform is responsible for moving data from the source system
into a form that can safely be consumed by Machine Learning workloads.

The high-level flow is:

```text
Data Sources
     ↓
Azure Data Factory
     ↓
ADLS Gen2 - Raw
     ↓
Data Validation
     ↓
 ┌───┴──────────────┐
 │                  │
 ▼                  ▼
Valid Data      Invalid Data
 │                  │
 ▼                  ▼
Processed       Quarantine
 │
 ▼
Curated Data
 │
 ▼
Feature Engineering
 │
 ▼
Feature Store
 │
 ▼
ML Training
````

---

# 7. Data Sources

For this reference project, we will use **public and synthetic data** rather
than confidential enterprise data.

The data will represent a production-like customer dataset.

Example:

```text
Customer ID
Age
Tenure
Monthly Charges
Contract Type
Payment Method
Support Calls
Internet Service
Churn
```

The initial dataset is only a starting point.

We will later generate multiple production-like batches to simulate what
would happen when new data arrives every day or every few hours.

For example:

```text
Batch 001
Batch 002
Batch 003
Batch 004
...
Batch 012
```

This allows us to simulate:

* New customers
* Updated customers
* Missing values
* Duplicate records
* Invalid data types
* Invalid ranges
* New categories
* Distribution changes
* Data drift

---

# 8. Azure Data Factory

**Azure Data Factory (ADF)** is responsible for data ingestion and
data orchestration.

ADF sits between the data source and the data lake.

```text
Source
  ↓
ADF Pipeline
  ↓
ADLS Gen2
```

ADF can handle:

* Data ingestion
* Scheduling
* Triggers
* Incremental loads
* Data movement
* Pipeline dependencies
* Retry handling
* Failure handling
* Pipeline monitoring

ADF is **not** responsible for:

* Training the ML model
* Tracking ML experiments
* Deploying containers to AKS
* Managing Kubernetes
* Replacing Azure DevOps

Its primary responsibility is the **data movement and data orchestration
layer**.

---

# 9. Raw Data Layer

The first destination is the **Raw zone** in ADLS Gen2.

```text
ADF
 ↓
ADLS Gen2
 ↓
Raw
```

The raw layer should preserve the incoming data as much as practical.

Example:

```text
adls/
└── raw/
    └── customer/
        ├── 2026-09-18/
        │   └── customers.csv
        ├── 2026-09-19/
        │   └── customers.csv
        └── 2026-09-20/
            └── customers.csv
```

The exact storage layout will be finalized during implementation.

The important principle is:

> **Do not destroy the original data before validation and processing.**

Keeping raw data helps with:

* Reprocessing
* Debugging
* Auditing
* Reproducing failures
* Investigating data quality problems

---

# 10. Data Validation

Before data reaches the ML pipeline, it must be validated.

The validation layer checks whether incoming data follows the expected
schema and business rules.

Example validation rules:

```text
Column Exists?
     ↓
Correct Data Type?
     ↓
Required Fields Present?
     ↓
Null Check
     ↓
Range Check
     ↓
Duplicate Check
     ↓
Allowed Category Check
     ↓
Business Rule Check
```

For example:

```text
Age
    → integer
    → minimum 18
    → maximum 100

MonthlyCharges
    → numeric
    → must be >= 0

ContractType
    → allowed values:
       Month-to-month
       One year
       Two year
```

Validation rules will be stored in **version-controlled configuration**,
rather than being hidden inside application code.

Example:

```text
data/
└── validation-rules/
    └── customer-schema.yaml
```

A simplified example could look like:

```yaml
columns:
  age:
    type: integer
    nullable: false
    min: 18
    max: 100

  monthly_charges:
    type: float
    nullable: false
    min: 0

  contract_type:
    type: string
    nullable: false
    allowed_values:
      - month-to-month
      - one-year
      - two-year
```

The actual validation framework and implementation will be created later.

---

# 11. Invalid Data — Quarantine

Not every incoming batch will be valid.

For example:

```text
Incoming Batch
      ↓
Validation
      ↓
 ┌────┴─────┐
 │          │
Valid     Invalid
 │          │
 ▼          ▼
Process   Quarantine
```

Invalid data should not silently continue into training.

Example quarantine structure:

```text
adls/
└── quarantine/
    └── customer/
        └── 2026-09-18/
            ├── invalid-records.csv
            └── validation-report.json
```

The validation report should explain why the records were rejected.

Example:

```text
Record: 10234
Column: age
Value: -5
Rule: age >= 18
Status: FAILED
```

This makes data-quality failures easier to investigate.

---

# 12. Processed Data

Valid data moves into the processed layer.

```text
Raw
 ↓
Validation
 ↓
Processed
```

Processing may include:

* Data type normalization
* Standardization
* Deduplication
* Cleaning
* Transformation
* Business rules

Example:

```text
Raw Customer Data
        ↓
Schema Validation
        ↓
Clean Data
        ↓
Deduplication
        ↓
Standardization
        ↓
Processed Data
```

---

# 13. Curated Data

The processed data can then be transformed into a curated dataset suitable
for downstream ML workloads.

```text
Processed
    ↓
Feature Engineering
    ↓
Curated Dataset
```

The curated dataset should contain the fields required by the ML workflow.

Example:

```text
Customer
   ↓
Historical Behavior
   ↓
Aggregations
   ↓
Features
```

---

# 14. Data Versioning

Data must be versioned because a model cannot be reproduced reliably if we
don't know which data was used.

The project will use **Delta Lake** for dataset management and versioning.

Conceptually:

```text
Dataset
   │
   ├── Version 1
   ├── Version 2
   ├── Version 3
   └── Version 4
```

Suppose Model V7 was trained using Dataset V12.

We should be able to establish:

```text
Dataset V12
     ↓
Training Run 145
     ↓
Model V7
```

This is part of model lineage.

---

# 15. Feature Engineering

After validation and processing, the data is transformed into ML features.

Example:

```text
Raw Data
   ↓
Customer History
   ↓
Feature Engineering
   ↓
Features
```

Possible features:

```text
tenure_months
average_monthly_charges
support_calls_last_30_days
payment_failure_count
contract_duration
```

Feature engineering must be reproducible.

The same feature definitions should be used consistently between training
and inference wherever possible.

---

# 16. Feature Store

The project will use **Feast** as the Feature Store.

The Feature Store helps manage features used by ML workloads.

Conceptually:

```text
Historical Data
      ↓
Feature Engineering
      ↓
Offline Features
      ↓
Training

Online Feature Store
      ↓
Real-time Inference
```

This helps reduce **training-serving skew**, where the features used during
training are different from the features used during production inference.

Feature freshness will also be monitored.

---

# 17. Training Data Flow

The complete training data path is:

```text
Data Source
     ↓
Azure Data Factory
     ↓
ADLS Raw
     ↓
Validation
     ├──────────────► Quarantine
     │
     ▼
Processed
     ↓
Curated
     ↓
Feature Engineering
     ↓
Feast
     ↓
Training Dataset
     ↓
XGBoost
```

This gives us a clear separation between:

```text
Data Ingestion
      ≠
Data Validation
      ≠
Feature Engineering
      ≠
Model Training
```

---

# 18. What Happens When New Data Arrives?

Suppose a new daily batch arrives.

```text
Day 1
  ↓
Batch 001

Day 2
  ↓
Batch 002

Day 3
  ↓
Batch 003
```

ADF detects or is triggered for the new data.

The flow becomes:

```text
New Data
   ↓
ADF
   ↓
ADLS Raw
   ↓
Validation
   ↓
Processed
   ↓
Feature Engineering
   ↓
Feature Store
```

The arrival of new data does **not automatically mean the model should
be retrained**.

Training and retraining decisions are handled separately.

---

# 19. Data Failure Scenario

We will intentionally create a data-quality failure later.

Example:

```text
Expected:

Age = 18 to 100

Incoming:

Age = -5
```

The pipeline should behave like:

```text
Incoming Data
      ↓
Validation
      ↓
Age = -5
      ↓
Validation Failed
      ↓
Quarantine
      ↓
Alert / Investigation
```

The invalid record must not silently enter the training dataset.

This will become one of our **Production Incident Labs**.

---

# 20. Data Flow Summary

The complete data platform can be summarized as:

```text
                    DATA SOURCES
                         │
                         ▼
                Azure Data Factory
                         │
                         ▼
                   ADLS Gen2
                    RAW ZONE
                         │
                         ▼
                  DATA VALIDATION
                    │         │
                    │         └────────► QUARANTINE
                    │
                    ▼
                PROCESSED DATA
                    │
                    ▼
                CURATED DATA
                    │
                    ▼
             FEATURE ENGINEERING
                    │
                    ▼
                  FEAST
                    │
                    ▼
              TRAINING DATASET
                    │
                    ▼
                 XGBOOST
```

The next architecture section will explain what happens **after training**:

```text
XGBoost
   ↓
MLflow
   ↓
Evaluation
   ↓
Model Registry
   ↓
Inference
   ↓
Docker
   ↓
ACR
   ↓
AKS
```



