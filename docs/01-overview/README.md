# 🏢 Project Overview

## 1. Business Scenario

Imagine an enterprise that wants to use Machine Learning and Generative AI
to improve internal and customer-facing processes.

The organization has two major workloads:

### Workload 1 — Machine Learning

The business wants to predict a customer-related outcome such as:

- Customer churn
- Customer risk
- Customer engagement

For this reference project, we will use a **customer churn prediction**
workload as the primary example.

The important part is not the specific business prediction.

The important part is how the model moves safely from:

```text
Data
 ↓
Training
 ↓
Evaluation
 ↓
Deployment
 ↓
Monitoring
 ↓
Retraining
 ↓
Production


---

# 2. The Problem With a Simple ML Project

A beginner ML project might look like:

```text
CSV
 ↓
Python
 ↓
Train Model
 ↓
model.pkl
```

This works for learning.

But production introduces many additional questions.

### Data

* Where does the data come from?
* Is the data valid?
* What happens if the schema changes?
* What happens if values are missing?
* How do we identify duplicate records?
* How do we know which dataset version was used?

### Model

* Which training run produced the model?
* Which parameters were used?
* Which dataset was used?
* Which model is currently in production?
* How was the model evaluated?
* What happens if the new model performs worse?

### Deployment

* How do we deploy the model automatically?
* How do we test it before production?
* How do we perform a canary deployment?
* How do we roll back?

### Operations

* Is the API healthy?
* Is inference latency increasing?
* Has the data distribution changed?
* Is model performance degrading?
* When should we retrain?

This is where **MLOps** becomes important.

---

# 3. Why MLOps?

MLOps applies software engineering and operations practices to the
Machine Learning lifecycle.

Instead of:

```text
Train → Deploy → Hope
```

we want:

```text
Develop
   ↓
Validate
   ↓
Train
   ↓
Evaluate
   ↓
Register
   ↓
Test
   ↓
Deploy
   ↓
Monitor
   ↓
Detect Problems
   ↓
Investigate
   ↓
Retrain if required
   ↓
Evaluate
   ↓
Promote or Reject
```

The objective is to make ML systems:

* Reproducible
* Testable
* Observable
* Secure
* Versioned
* Deployable
* Recoverable

---

# 4. GenAI / RAG Workload

The second workload is a **Retrieval-Augmented Generation (RAG)** system.

Imagine employees asking:

> "What is the company's leave policy?"

Instead of expecting the LLM to know the organization's internal documents,
we retrieve relevant information from a controlled document collection.

The simplified flow is:

```text
User Question
      ↓
RAG API
      ↓
Query Embedding
      ↓
Vector Search
      ↓
Qdrant
      ↓
Relevant Documents
      ↓
Reranker
      ↓
Relevant Context
      ↓
LLM
      ↓
Answer
```

The LLM therefore receives relevant retrieved context instead of relying
only on its pretrained knowledge.

---

# 5. Why RAG Needs Production Engineering

A simple RAG demo can be:

```text
PDF
 ↓
Vector Database
 ↓
LLM
 ↓
Answer
```

A production RAG platform needs much more.

We need to understand:

* Document ingestion
* Chunking
* Embeddings
* Vector search
* Reranking
* Prompt management
* Retrieval quality
* Groundedness
* Hallucination risk
* Safety
* Latency
* Token usage
* Evaluation
* Monitoring
* Versioning

For example, if the RAG system starts returning irrelevant answers,
we need to determine whether the problem is:

```text
Document ingestion
       OR
Chunking
       OR
Embedding model
       OR
Vector search
       OR
Reranker
       OR
Prompt
       OR
LLM
```

This is why RAG also needs production engineering.

---

# 6. Why Azure?

Azure is the primary cloud platform for this project.

We will use Azure because it allows us to demonstrate an enterprise-style
cloud architecture around the ML and GenAI workloads.

The major Azure components are:

```text
Azure
│
├── Resource Groups
├── VNet
├── Subnets
├── NSGs
├── Private Endpoints
├── Private DNS
│
├── ADLS Gen2
├── Azure Data Factory
│
├── Azure Container Registry
├── AKS
│
├── Key Vault
├── Entra ID
│
├── Azure Monitor
├── Log Analytics
└── Application Insights
```

Infrastructure will be created using **Terraform** rather than manually
creating resources wherever practical.

---

# 7. Role of Each Major Component

A common mistake in MLOps projects is adding technologies without
understanding why they exist.

Every component in this project must have a clear responsibility.

| Component                   | Responsibility                                   |
| --------------------------- | ------------------------------------------------ |
| Terraform                   | Infrastructure as Code                           |
| Azure Data Factory          | Data ingestion and data orchestration            |
| ADLS Gen2                   | Data lake and storage                            |
| Delta Lake                  | Dataset versioning and reliable data management  |
| Data Validation             | Detect invalid data before downstream processing |
| Feast                       | Feature Store                                    |
| XGBoost                     | Classical ML model                               |
| MLflow                      | Experiment tracking and model registry           |
| FastAPI                     | Inference APIs                                   |
| Docker                      | Containerization                                 |
| ACR                         | Container image registry                         |
| AKS                         | Production container orchestration               |
| Azure DevOps                | CI/CD                                            |
| Qdrant                      | Vector database                                  |
| BGE                         | Embeddings                                       |
| BGE Reranker                | Retrieval reranking                              |
| Llama / Mistral             | LLM workload                                     |
| LangChain                   | RAG application framework                        |
| Prometheus                  | Metrics                                          |
| Grafana                     | Dashboards                                       |
| Azure Monitor               | Azure monitoring                                 |
| Log Analytics               | Centralized logs                                 |
| Application Insights        | Application telemetry                            |
| Key Vault                   | Secrets                                          |
| Entra ID / Managed Identity | Authentication and authorization                 |

---

# 8. ADF vs ML Workflow vs CI/CD

These responsibilities must remain separate.

## Azure Data Factory

Responsible for:

```text
Data Sources
    ↓
Ingestion
    ↓
Raw Data
    ↓
Processing
    ↓
Curated Data
```

ADF is primarily about **data movement and data orchestration**.

---

## ML Workflow

Responsible for:

```text
Dataset
   ↓
Features
   ↓
Training
   ↓
Evaluation
   ↓
Model
```

This is the **ML lifecycle**.

---

## Azure DevOps

Responsible for:

```text
Code
 ↓
Tests
 ↓
Security Checks
 ↓
Build
 ↓
Container
 ↓
Deployment
```

This is the **software delivery lifecycle**.

Keeping these responsibilities separate makes the platform easier to
understand and operate.

---

# 9. Production Model Lifecycle

Suppose the current production model is:

```text
Model V1
```

A new model is trained:

```text
Model V2
```

We do not immediately replace V1.

Instead:

```text
                 Model V2
                    ↓
                Evaluation
                    ↓
                 Approval
                    ↓
                 Canary
                    ↓
              90% V1 / 10% V2
                    ↓
                 Monitoring
```

If V2 behaves correctly:

```text
V1 → 50%
V2 → 50%

        ↓

V1 → 0%
V2 → 100%
```

If V2 causes problems:

```text
V2
 ↓
Problem detected
 ↓
Rollback
 ↓
V1 becomes active again
```

The previous model remains available.

---

# 10. What Does "Bad Model" Mean?

A model is not considered bad simply because someone thinks it is bad.

We need measurable signals.

Possible signals include:

### Model performance

* Precision
* Recall
* F1
* ROC-AUC
* Business-specific metrics

### Data drift

The distribution of incoming data changes significantly.

### Prediction drift

The distribution of model predictions changes unexpectedly.

### Business metrics

For example:

* Conversion
* Churn
* Fraud detection rate
* False-positive cost

### RAG / LLM quality

For the RAG workload:

* Retrieval relevance
* Context relevance
* Groundedness
* Answer quality
* User feedback

These signals trigger an **investigation**.

Drift detection alone should not automatically mean:

```text
DRIFT → RETRAIN
```

Instead:

```text
Drift detected
      ↓
Investigate
      ↓
Determine cause
      ↓
Decide whether retraining is required
      ↓
Train candidate
      ↓
Evaluate
      ↓
Compare
      ↓
Promote only if acceptable
```

---

# 11. Traceability

A production ML prediction should be traceable.

For example:

```text
Prediction ID
      ↓
Dataset Version
      ↓
Feature Version
      ↓
Git Commit
      ↓
MLflow Run
      ↓
Model Version
      ↓
Evaluation Report
      ↓
Container Image
      ↓
AKS Deployment Revision
```

This allows engineers to answer:

> "Exactly how was this prediction generated?"

The same concept applies to RAG:

```text
Request ID
    ↓
Prompt Version
    ↓
RAG Configuration
    ↓
Embedding Version
    ↓
Retrieved Documents
    ↓
Reranker Version
    ↓
LLM Version
    ↓
Response
```

---

# 12. Production Engineering Mindset

The project will follow one principle:

> **Everything that can affect production should be observable,
> versioned, testable, and recoverable.**

Examples:

```text
Code              → Git
Infrastructure    → Terraform
Data              → Delta/versioning
Experiments       → MLflow
Models            → Model Registry
Features          → Feast
Containers        → ACR
Deployment        → Kubernetes
Secrets           → Key Vault
Metrics           → Prometheus
Dashboards        → Grafana
Logs              → Log Analytics
Application       → Application Insights
RAG configuration → Version control
Prompts           → Version control
```

---

# 13. What Makes This Project Different?

This project is intentionally not just:

```text
Train Model
+
Create API
+
Deploy
```

It will demonstrate the complete lifecycle:

```text
                ┌───────────────┐
                │     DATA      │
                └───────┬───────┘
                        ↓
                   VALIDATION
                        ↓
                 FEATURE STORE
                        ↓
                    TRAINING
                        ↓
                    MLflow
                        ↓
                   EVALUATION
                        ↓
                 MODEL REGISTRY
                        ↓
                 CI / CT / CD
                        ↓
                      AKS
                        ↓
                  PRODUCTION
                        ↓
                 OBSERVABILITY
                        ↓
                DRIFT / QUALITY
                        ↓
                  INVESTIGATION
                        ↓
                   RETRAINING
                        ↓
                CANARY / ROLLBACK
```

And alongside it:

```text
             DOCUMENTS
                  ↓
                 RAG
                  ↓
             RETRIEVAL
                  ↓
              RERANKING
                  ↓
                 LLM
                  ↓
            RAG EVALUATION
                  ↓
             MONITORING
```

---

# 14. Final Objective

By the end of this project, another engineer should be able to:

1. Understand the architecture
2. Clone the repository
3. Run components locally
4. Provision Azure infrastructure
5. Ingest and validate data
6. Train an ML model
7. Track experiments
8. Register and evaluate models
9. Deploy inference
10. Deploy the RAG workload
11. Run CI/CT/CD
12. Monitor production
13. Detect drift
14. Retrain models
15. Perform canary deployment
16. Roll back a bad deployment
17. Troubleshoot production incidents
18. Understand security and governance
19. Understand disaster recovery
20. Explain the entire platform in an interview

---

