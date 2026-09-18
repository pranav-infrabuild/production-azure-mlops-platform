# 🎯 Interview Mode

This section converts the production Azure MLOps + LLM/RAG platform into an **interview preparation reference**.

The goal is not to memorize definitions.

The goal is to understand:

```text
Concept
   ↓
Why do we need it?
   ↓
How does it work?
   ↓
How did we implement it?
   ↓
What can fail?
   ↓
How do we troubleshoot it?
```

---

## 1. How to Use This Section

For every major technology, prepare answers at three levels:

### Level 1 — Concept

Explain the technology in simple language.

Example:

> What is MLflow?

Answer:

> MLflow is used to track machine learning experiments, store artifacts, manage model versions, and maintain a model registry.

---

### Level 2 — Project Implementation

Explain how the technology is used in this project.

Example:

> In our platform, MLflow tracks XGBoost training runs, stores metrics and artifacts, and manages registered model versions before deployment to AKS.

---

### Level 3 — Production Troubleshooting

Explain what happens when something fails.

Example:

> If a newly deployed model shows degraded performance, we compare its evaluation metrics with the previous production model and can roll back to the previous registered model version.

---

# 2. Interview Answer Structure

Use this structure when answering project-based questions:

```text
1. Direct Answer
2. Why we need it
3. How it works
4. How we implemented it
5. Production consideration
6. Failure/troubleshooting scenario
```

For behavioral/project questions, use:

```text
Situation
   ↓
Task
   ↓
Action
   ↓
Result
```

---

# 3. Project Story

## 3.1 Two-Minute Project Explanation

The project is a production-grade **Azure MLOps and LLM/RAG platform**.

It supports two major workloads:

1. Classical ML using **XGBoost**
2. GenAI using **LLM + RAG**

The data platform uses **Azure Data Factory**, **ADLS Gen2**, and **Delta Lake**.

For ML, we use **Feast** for feature management, **MLflow** for experiment tracking and model registry, and XGBoost for model training.

Models are containerized using **Docker**, stored in **Azure Container Registry**, and deployed to **AKS**.

The platform uses **Azure DevOps** for CI/CD and continuous testing.

For the GenAI workload, documents are processed, chunked, converted into embeddings using **BGE-small-en-v1.5**, stored in **Qdrant**, reranked using **BGE-reranker-base**, and passed to an LLM such as **Llama 3.1 8B** or **Mistral 7B**.

The platform is secured using **Entra ID, managed/workload identity, Azure Key Vault, private endpoints, private DNS, NSGs, and Kubernetes NetworkPolicy**.

Monitoring covers infrastructure, application, model, data drift, feature freshness, RAG quality, latency, errors, and cost using **Prometheus, Grafana, Azure Monitor, Log Analytics, and Application Insights**.

---

# 4. Interview Domains

## 4.1 MLOps

Topics:

- MLOps lifecycle
- Model training
- Experiment tracking
- MLflow
- Model registry
- Model evaluation
- Model promotion
- Model deployment
- Model rollback
- Data drift
- Model drift
- Feature drift
- Training-serving skew
- Feature Store
- Feast
- Batch inference
- Real-time inference
- Model explainability
- SHAP
- Retraining
- Model governance
- Model lineage

---

## 4.2 Azure

Topics:

- Azure Resource Groups
- VNet
- Subnets
- NSG
- Private Endpoint
- Private DNS
- ADLS Gen2
- Azure Data Factory
- Azure Database for MySQL Flexible Server
- Azure Container Registry
- AKS
- Azure Key Vault
- Application Gateway
- WAF
- Azure Monitor
- Log Analytics
- Application Insights
- Entra ID
- Managed Identity
- Workload Identity
- Azure Policy

---

## 4.3 Kubernetes

Topics:

- Pod
- Deployment
- ReplicaSet
- Service
- Ingress
- HPA
- PDB
- ConfigMap
- Secret
- Namespace
- Resource requests
- Resource limits
- Liveness probe
- Readiness probe
- Startup probe
- NetworkPolicy
- DaemonSet
- StatefulSet
- kubelet
- kube-proxy
- etcd
- Kubernetes networking
- AKS troubleshooting

---

## 4.4 DevOps

Topics:

- Git
- Git branching
- Merge
- Rebase
- Cherry-pick
- Azure Repos
- Azure Pipelines
- CI
- Continuous Testing
- CD
- Docker
- Dockerfile
- ACR
- Terraform
- Terraform state
- Remote backend
- State locking
- Drift
- `count`
- `for_each`
- Terraform modules
- Infrastructure promotion

---

## 4.5 GenAI / RAG

Topics:

- LLM
- Prompt engineering
- Embeddings
- Vector database
- Qdrant
- Chunking
- Retrieval
- Reranking
- BGE embeddings
- BGE reranker
- LangChain
- Prompt versioning
- RAG configuration versioning
- RAG evaluation
- Groundedness
- Context relevance
- Answer relevance
- Hallucination
- Prompt injection
- PII protection
- LLM latency
- LLM cost
- LLM observability

---

## 4.6 Production Engineering

Topics:

- High availability
- Scalability
- Reliability
- SLO
- SLA
- SLI
- Error budget
- RTO
- RPO
- Disaster recovery
- Backup and restore
- Cost optimization
- Security
- Supply-chain security
- SBOM
- Image signing
- Audit trail
- Incident management

---

# 5. Production Incident Questions

The project includes practical failure scenarios.

Examples:

```text
Data validation failure
        ↓
Model regression
        ↓
Data drift
        ↓
Pod CrashLoopBackOff
        ↓
502 Bad Gateway
        ↓
High inference latency
        ↓
RAG quality degradation
        ↓
CI/CD failure
        ↓
Identity/RBAC failure
        ↓
DNS failure
        ↓
Secret/certificate expiration
        ↓
Model rollback
        ↓
Qdrant failure
        ↓
Disaster recovery
```

Each incident will eventually contain:

```text
Problem
Symptoms
Impact
Root Cause
Investigation
Commands
Fix
Verification
Prevention
Interview Answer
```

---

# 6. Key Interview Principle

For this project, do not answer only with definitions.

Always connect the answer back to the platform.

For example:

### Weak Answer

> HPA automatically scales pods based on resource utilization.

### Project Answer

> HPA automatically scales our inference API pods based on configured metrics. We use resource requests and limits together with HPA so Kubernetes can scale the service when workload increases. We also monitor latency and error rate because CPU utilization alone may not represent the actual user experience.

The second answer demonstrates **concept + implementation + production thinking**.

---

# 7. Interview Preparation Path

We will prepare interview questions progressively:

```text
MLOps Fundamentals
        ↓
Azure Data Platform
        ↓
ML Training & MLflow
        ↓
Feature Store
        ↓
Model Serving
        ↓
Docker
        ↓
AKS
        ↓
Azure DevOps CI/CD
        ↓
Monitoring & Drift
        ↓
RAG / LLM
        ↓
Security & Governance
        ↓
Production Incidents
        ↓
System Design
```

---

# 8. Current Status

Interview Mode documentation is being built alongside the actual platform.

The objective is:

```text
Learn
  ↓
Implement
  ↓
Break
  ↓
Troubleshoot
  ↓
Document
  ↓
Explain in Interview
```

This ensures the interview answers are based on **actual implementation and production scenarios**, rather than memorized theory.

# 9. MLOps Interview Questions

## 9.1 What is MLOps?

### Direct Answer

**MLOps** is the practice of applying **DevOps principles to machine learning systems**.

It helps us automate and manage the complete ML lifecycle:

```text
Data
 ↓
Validation
 ↓
Feature Engineering
 ↓
Training
 ↓
Experiment Tracking
 ↓
Evaluation
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

### Why Do We Need MLOps?

A machine learning model is not finished after training.

In production, we need to manage:

- Data changes
- Model versions
- Experiments
- Deployment
- Monitoring
- Drift
- Retraining
- Rollback
- Security
- Governance
- Lineage

### In Our Project

Our platform uses:

| Requirement | Technology |
|---|---|
| Data ingestion | Azure Data Factory |
| Data lake | ADLS Gen2 |
| Data versioning | Delta Lake |
| Feature management | Feast |
| Model training | XGBoost |
| Experiment tracking | MLflow |
| Model registry | MLflow |
| Containerization | Docker |
| Image registry | Azure Container Registry |
| Deployment | AKS |
| CI/CD | Azure DevOps |
| Monitoring | Prometheus + Grafana + Azure Monitor |
| Drift monitoring | Monitoring pipeline |
| Explainability | SHAP |

---

## 9.2 Explain the MLOps Lifecycle

### Direct Answer

The MLOps lifecycle manages a model from **data collection to production monitoring and retraining**.

```text
Data Ingestion
      ↓
Data Validation
      ↓
Feature Engineering
      ↓
Feature Store
      ↓
Model Training
      ↓
Experiment Tracking
      ↓
Model Evaluation
      ↓
Model Registry
      ↓
Deployment
      ↓
Inference
      ↓
Monitoring
      ↓
Drift / Performance Detection
      ↓
Retraining
      ↓
Evaluation
      ↓
Promotion or Rejection
```

### Project Example

For our XGBoost churn model:

```text
Customer Data
     ↓
ADF
     ↓
ADLS Gen2
     ↓
Validation
     ↓
Feature Engineering
     ↓
Feast
     ↓
XGBoost Training
     ↓
MLflow
     ↓
Evaluation
     ↓
Model Registry
     ↓
Docker
     ↓
ACR
     ↓
AKS
     ↓
Real-time / Batch Inference
     ↓
Monitoring
```

---

## 9.3 Why Can't We Just Train a Model and Deploy It?

### Direct Answer

Because production ML is continuously affected by **data, model, infrastructure, and business changes**.

A model that works well today may perform poorly later because:

- Data distribution changes
- Customer behavior changes
- Features become stale
- Business rules change
- Dependencies change
- Model performance decreases
- Infrastructure changes

Therefore, production ML requires **continuous monitoring and lifecycle management**.

---

## 9.4 What is MLflow?

### Direct Answer

**MLflow** is an ML lifecycle platform used for:

- Experiment tracking
- Metrics tracking
- Parameter tracking
- Artifact storage
- Model packaging
- Model registry
- Model version management

### Project Example

During XGBoost training we can track:

```text
Run ID
 ↓
Parameters
 ↓
max_depth
learning_rate
n_estimators
 ↓
Metrics
 ↓
precision
recall
F1
ROC-AUC
 ↓
Artifacts
 ↓
model
evaluation report
plots
```

The trained model can then be registered in the **MLflow Model Registry**.

---

## 9.5 What is Experiment Tracking?

### Direct Answer

**Experiment tracking** means recording the details of every training run so that we can reproduce and compare experiments.

For example:

```text
Run 101
├── learning_rate = 0.1
├── max_depth = 6
├── F1 = 0.81
└── ROC-AUC = 0.87

Run 102
├── learning_rate = 0.05
├── max_depth = 8
├── F1 = 0.85
└── ROC-AUC = 0.90
```

Instead of manually remembering which configuration produced a model, MLflow stores this information.

---

## 9.6 How Do You Compare Two Model Runs?

### Direct Answer

I compare the models using **predefined evaluation metrics and business requirements**.

For our classification model, we can compare:

- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrix
- Inference latency
- Resource consumption
- Business-specific metrics

Example:

```text
Model A
F1      = 0.81
Recall  = 0.78
Latency = 80 ms

Model B
F1      = 0.86
Recall  = 0.84
Latency = 95 ms
```

I would not promote a model based only on one metric.

The promotion decision should follow the **defined evaluation and business acceptance criteria**.

---

## 9.7 What is a Model Registry?

### Direct Answer

A **Model Registry** is a centralized location where we manage **model versions and their lifecycle**.

It helps us know:

```text
Which model?
Which version?
Which training run?
Which stage/alias?
Which evaluation?
Which deployment?
```

Example:

```text
Churn Model
│
├── Version 1
├── Version 2
├── Version 3
└── Version 4
```

The registry provides traceability between the model and its training information.

---

## 9.8 Why Do We Need Model Versioning?

### Direct Answer

Model versioning allows us to **track, reproduce, compare, deploy, and roll back models**.

Example:

```text
Production
   ↓
Model V7

New candidate
   ↓
Model V8

If V8 performs well
   ↓
Promote V8

If V8 performs badly
   ↓
Rollback to V7
```

We should **not delete the previous production model** because it may be required for rollback and auditability.

---

## 9.9 How Do You Deploy a New Model?

### Direct Answer

A typical deployment flow is:

```text
Training
   ↓
Evaluation
   ↓
MLflow Registry
   ↓
Model Approval
   ↓
Container Image
   ↓
ACR
   ↓
AKS
   ↓
Staging
   ↓
Continuous Testing
   ↓
Production
```

The deployment strategy can be:

- Rolling deployment
- Canary deployment
- Blue-green deployment

---

## 9.10 What is Canary Deployment for ML Models?

### Direct Answer

In **canary deployment**, the new model initially receives only a small percentage of production traffic.

Example:

```text
Production Traffic
       │
       ├── 90% → Model V7
       │
       └── 10% → Model V8
```

We monitor:

- Error rate
- Latency
- Model performance
- Prediction distribution
- Business metrics

If the candidate behaves as expected, traffic can gradually increase.

If it fails the defined criteria, traffic can be returned to the previous model.

---

## 9.11 How Would You Roll Back a Bad Model?

### Direct Answer

I would keep the previous model version available in the **model registry** and retain the previous Kubernetes deployment revision.

Example:

```text
Current
Model V8
   ↓
Performance degradation
   ↓
Investigate
   ↓
Rollback
   ↓
Model V7
```

Rollback should restore the previously validated production configuration rather than retraining immediately.

After stabilization, we investigate the root cause.

---

## 9.12 What is Data Drift?

### Direct Answer

**Data drift** occurs when the distribution of production input data changes compared with the data used during training.

Example:

```text
Training data

Age:
20-30 → 40%
30-40 → 35%
40-50 → 25%

Production data

Age:
20-30 → 15%
30-40 → 30%
40-50 → 55%
```

The production distribution has changed significantly.

This can indicate that the model may eventually perform differently from its validation results.

---

## 9.13 Does Data Drift Automatically Mean We Should Retrain?

### Direct Answer

**No.**

Drift is a **signal**, not an automatic reason to retrain.

The workflow should be:

```text
Drift Detected
      ↓
Investigate
      ↓
Check Model Performance
      ↓
Check Business Impact
      ↓
Determine Root Cause
      ↓
Retrain if Required
      ↓
Evaluate New Model
      ↓
Promote only if it passes acceptance criteria
```

This prevents unnecessary retraining.

---

## 9.14 What is Training-Serving Skew?

### Direct Answer

**Training-serving skew** occurs when the way features are generated during training is different from the way they are generated during production inference.

Example:

```text
Training
Raw Data
   ↓
Feature Logic A
   ↓
Model

Production
Raw Data
   ↓
Feature Logic B
   ↓
Model
```

Even if both use the same model, different feature logic can produce incorrect predictions.

### How We Address It

We use a **Feature Store such as Feast** to help maintain consistent feature definitions between training and serving.

---

## 9.15 What is a Feature Store?

### Direct Answer

A **Feature Store** manages machine-learning features so they can be consistently used during both **training and inference**.

It helps address:

- Feature reuse
- Feature consistency
- Training-serving skew
- Feature freshness
- Feature discovery
- Online serving
- Offline training

In our project we use **Feast**.

---

## 9.16 Batch Inference vs Real-Time Inference

### Batch Inference

Predictions are generated for many records at scheduled or triggered intervals.

```text
Data
 ↓
Batch Job
 ↓
Model
 ↓
Predictions
 ↓
Storage
```

Example:

> Generate churn predictions for all customers every night.

### Real-Time Inference

A prediction is generated when an API request arrives.

```text
Client
 ↓
API
 ↓
Model
 ↓
Prediction
 ↓
Response
```

Example:

> A customer request arrives and the system immediately predicts churn probability.

### In Our Platform

We support both:

```text
                    ┌──→ Real-Time Inference
                    │
Model Registry ─────┤
                    │
                    └──→ Batch Inference
```

---

## 9.17 What is Model Monitoring?

### Direct Answer

Model monitoring means continuously checking whether the production ML system is behaving as expected.

We monitor:

### Infrastructure

- CPU
- Memory
- Pod health
- Node health

### Application

- Request rate
- Error rate
- Latency
- Availability

### ML

- Prediction distribution
- Data drift
- Feature drift
- Model performance
- Training-serving skew

### Business

- Business KPIs
- Prediction outcomes
- Business impact

---

## 9.18 What Happens When Model Performance Drops?

### Direct Answer

I would follow a structured investigation:

```text
Performance Drop
      ↓
Check Application Health
      ↓
Check Input Data
      ↓
Check Data Drift
      ↓
Check Feature Freshness
      ↓
Check Training-Serving Skew
      ↓
Check Model Version
      ↓
Check Business/Data Changes
      ↓
Determine Root Cause
```

Depending on the root cause, we may:

- Fix the data pipeline
- Fix feature generation
- Retrain the model
- Roll back the model
- Update the deployment
- Investigate business changes

---

# 10. Interview Rule

For every MLOps question, try to connect:

```text
Definition
   +
Why
   +
Our Architecture
   +
Production Example
   +
Failure Scenario
   +
Troubleshooting
```

This demonstrates that we understand both **MLOps theory and production implementation**.

# 11. Azure Interview Questions

## 11.1 Why Did We Choose Azure?

### Direct Answer

We chose **Azure** because the platform needs an integrated cloud environment for:

- Data storage
- Data orchestration
- Compute
- Kubernetes
- Identity
- Security
- Networking
- Monitoring
- CI/CD integration

Our major Azure services are:

```text
Azure
│
├── ADLS Gen2
├── Data Factory
├── MySQL Flexible Server
├── AKS
├── ACR
├── Key Vault
├── Application Gateway + WAF
├── Virtual Network
├── Private Endpoint
├── Private DNS
├── Entra ID
└── Azure Monitor
```

---

# 11.2 What is ADLS Gen2?

### Direct Answer

**Azure Data Lake Storage Gen2** is used as the central data storage layer for our ML platform.

It provides scalable storage for:

- Raw data
- Processed data
- Training datasets
- Feature data
- ML artifacts
- Historical data

### Project Architecture

```text
Data Sources
     ↓
Azure Data Factory
     ↓
ADLS Gen2
 ┌───────────────┐
 │ Raw           │
 │ Processed     │
 │ Curated       │
 │ Quarantine    │
 └───────────────┘
     ↓
Feature Engineering
     ↓
ML Training
```

---

# 11.3 Why Don't We Store Everything in MySQL?

### Direct Answer

**MySQL Flexible Server** and **ADLS Gen2** serve different purposes.

### MySQL

Used for operational/transactional data such as:

- Application data
- Request metadata
- Prediction metadata
- Operational records

### ADLS

Used for large-scale analytical and ML data:

- Raw datasets
- Historical data
- Training datasets
- Processed datasets
- Data versions

So:

```text
MySQL
   ↓
Operational / Transactional Data

ADLS
   ↓
Analytical / ML Data
```

---

# 11.4 Where Does Azure Database for MySQL Flexible Server Fit?

### Direct Answer

**Azure Database for MySQL Flexible Server** is part of our application/data infrastructure layer.

It is provisioned using **Terraform** and connected to the platform through private networking.

Architecture:

```text
Application
    ↓
AKS
    ↓
Private Network
    ↓
MySQL Flexible Server
```

The database is not a replacement for ADLS.

It complements ADLS by handling operational database workloads.

---

# 11.5 What is Azure Data Factory?

### Direct Answer

**Azure Data Factory (ADF)** is our **data ingestion and data orchestration layer**.

It is responsible for moving and preparing data before it enters the ML lifecycle.

Example:

```text
Source
  ↓
ADF Pipeline
  ↓
Validation
  ↓
ADLS Raw
  ↓
Processed / Quarantine
```

ADF can orchestrate:

- Data movement
- Scheduled ingestion
- Data transformation activities
- Pipeline dependencies
- Triggers
- Parameterized pipelines
- Failure handling

---

# 11.6 What is the Difference Between ADF, ML Workflow and Azure DevOps?

This is an important production architecture question.

### Azure Data Factory

Responsible for **data workflows**.

```text
Source
 ↓
Ingestion
 ↓
Validation
 ↓
Data Lake
```

### ML Workflow

Responsible for **machine-learning workflows**.

```text
Dataset
 ↓
Feature Engineering
 ↓
Training
 ↓
Evaluation
 ↓
Model Registration
```

### Azure DevOps

Responsible for **software delivery**.

```text
Git
 ↓
CI
 ↓
Testing
 ↓
Build
 ↓
ACR
 ↓
Deployment
```

### Simple Comparison

| Platform | Main Responsibility |
|---|---|
| ADF | Data orchestration |
| ML Workflow | ML lifecycle orchestration |
| Azure DevOps | Software CI/CD |

They work together but should not be treated as the same system.

---

# 11.7 What is a Virtual Network?

### Direct Answer

An **Azure Virtual Network (VNet)** provides private network connectivity for Azure resources.

Our platform uses a VNet such as:

```text
10.0.0.0/16
```

Example subnet structure:

```text
VNet
10.0.0.0/16
│
├── AKS Subnet
├── Application Gateway Subnet
├── Private Endpoint Subnet
└── Supporting Infrastructure Subnets
```

This provides network isolation and controlled communication between components.

---

# 11.8 What is a Private Endpoint?

### Direct Answer

A **Private Endpoint** provides private connectivity from a VNet to an Azure PaaS service using a private IP address.

Instead of:

```text
AKS
 ↓
Public Internet
 ↓
Azure Service
```

we aim for:

```text
AKS
 ↓
Private Network
 ↓
Private Endpoint
 ↓
Azure Service
```

We use private connectivity for services such as:

- ADLS
- ACR
- Key Vault
- MySQL Flexible Server

where supported by the architecture.

---

# 11.9 Private Endpoint vs Service Endpoint

### Private Endpoint

Uses a **private IP address** from the VNet.

```text
VNet
 ↓
Private IP
 ↓
Azure PaaS Service
```

### Service Endpoint

Extends VNet identity to the Azure service over the Azure backbone while the service continues to use its public endpoint.

### Simple Difference

```text
Private Endpoint
→ Private IP connectivity

Service Endpoint
→ VNet-based secure access to the service endpoint
```

For our production-oriented architecture, **Private Endpoint** is preferred where private connectivity is required.

---

# 11.10 Why Do We Need Private DNS?

### Direct Answer

When a service is accessed through a Private Endpoint, DNS must resolve its hostname to the correct **private IP address**.

Example:

```text
storage-account.azure.net
        ↓
DNS Resolution
        ↓
Private IP
        ↓
Private Endpoint
```

Without correct DNS configuration, the application may resolve the service to an incorrect/public endpoint or fail to connect as expected.

### Production Troubleshooting

We should verify:

```text
DNS Resolution
     ↓
Private IP
     ↓
Network Connectivity
     ↓
Authentication
     ↓
Application Connection
```

Commands such as `nslookup` can help during troubleshooting.

---

# 11.11 What is Azure Key Vault?

### Direct Answer

**Azure Key Vault** is used to securely store and manage sensitive information such as:

- Secrets
- Certificates
- Keys

We should avoid storing credentials directly in:

```text
Source Code
Dockerfile
Git Repository
Kubernetes YAML
Pipeline YAML
```

Instead:

```text
Application
    ↓
Identity
    ↓
Key Vault
    ↓
Secret / Certificate
```

---

# 11.12 Why Should We Avoid Hardcoded Secrets?

### Direct Answer

Hardcoded credentials create security and operational risks.

For example:

```text
password = "MyPassword123"
```

in source code can result in credential exposure through:

- Git history
- Logs
- Container images
- Developer machines
- Pull requests

Our architecture uses **Key Vault + identity-based access** instead.

---

# 11.13 What is Managed Identity?

### Direct Answer

**Managed Identity** allows an Azure resource to authenticate to supported Azure services without storing credentials in application code.

Example:

```text
AKS Workload
     ↓
Managed / Workload Identity
     ↓
Azure Entra ID
     ↓
Key Vault / Storage / Other Azure Service
```

The application does not need a hardcoded username/password.

---

# 11.14 Managed Identity vs Service Principal

### Service Principal

A service principal represents an application identity in Microsoft Entra ID.

It can authenticate using credentials such as:

- Secret
- Certificate
- Federated identity

### Managed Identity

Azure manages the identity lifecycle for the Azure resource.

This reduces the need to manually manage credentials.

### Project Approach

For workloads running in Azure, we prefer **managed/workload identity** where appropriate.

For automation that requires an application identity, we can use an appropriately secured **service principal or workload federation** rather than hardcoded credentials.

---

# 11.15 How Does AKS Access Key Vault?

A production-oriented flow is:

```text
Application Pod
      ↓
Workload Identity
      ↓
Microsoft Entra ID
      ↓
Authorization
      ↓
Azure Key Vault
      ↓
Secret / Certificate
```

The important principle is:

> The application authenticates using an identity instead of embedding credentials.

---

# 11.16 What is Azure Container Registry?

### Direct Answer

**Azure Container Registry (ACR)** is used to store our Docker container images.

Example:

```text
Source Code
    ↓
Azure DevOps CI
    ↓
Docker Build
    ↓
Security Scan
    ↓
ACR
    ↓
AKS
```

Example image lifecycle:

```text
rag-api:build-101
rag-api:build-102
rag-api:build-103
```

For stronger traceability, the deployment should also retain the **immutable image digest**.

---

# 11.17 Why Do We Need Application Gateway?

### Direct Answer

**Azure Application Gateway** acts as an application-layer entry point for HTTP/HTTPS traffic.

It can provide:

- Layer 7 routing
- TLS termination
- Web Application Firewall
- Host/path-based routing
- Integration with AKS ingress architecture

Our simplified request path is:

```text
User
 ↓
Application Gateway
 ↓
WAF
 ↓
AKS Ingress
 ↓
Kubernetes Service
 ↓
Pod
```

---

# 11.18 What is WAF?

### Direct Answer

**Web Application Firewall (WAF)** helps protect web applications from common web-layer attacks.

It provides an additional security layer before traffic reaches the application.

Architecture:

```text
Internet
   ↓
Application Gateway
   ↓
WAF
   ↓
Ingress
   ↓
Application
```

WAF is part of the **application security boundary** and does not replace Kubernetes NetworkPolicy or identity-based access controls.

---

# 11.19 What is Azure Monitor?

### Direct Answer

**Azure Monitor** provides monitoring and observability for Azure resources and applications.

In our platform, observability is split across multiple layers:

```text
Infrastructure
Application
ML
RAG / LLM
Business
```

We use Azure-native services such as:

- Azure Monitor
- Log Analytics
- Application Insights

alongside:

- Prometheus
- Grafana

---

# 11.20 How Would You Troubleshoot an Azure Connectivity Issue?

### Direct Answer

I would troubleshoot from the lower layers upward.

```text
1. DNS
   ↓
2. Private Endpoint
   ↓
3. NSG / Network Rules
   ↓
4. Routing
   ↓
5. Identity / RBAC
   ↓
6. Service Configuration
   ↓
7. Application
```

For example, if an AKS application cannot connect to MySQL:

```text
Check DNS
 ↓
Check MySQL private IP
 ↓
Check NSG / network connectivity
 ↓
Check MySQL firewall/network configuration
 ↓
Check identity/credentials
 ↓
Check application connection string
 ↓
Check application logs
```

This avoids immediately changing application code when the actual problem may be networking or authentication.

---

# 11.21 Azure Interview Answer Pattern

For Azure questions, use:

```text
What is it?
    ↓
Why do we need it?
    ↓
Where is it used in our architecture?
    ↓
How is it secured?
    ↓
What happens if it fails?
    ↓
How would I troubleshoot it?
```

This demonstrates **Azure knowledge + architecture understanding + production troubleshooting**.


# 11. Azure Interview Questions

## 11.1 Why Did We Choose Azure?

### Direct Answer

We chose **Azure** because the platform needs an integrated cloud environment for:

- Data storage
- Data orchestration
- Compute
- Kubernetes
- Identity
- Security
- Networking
- Monitoring
- CI/CD integration

Our major Azure services are:

```text
Azure
│
├── ADLS Gen2
├── Data Factory
├── MySQL Flexible Server
├── AKS
├── ACR
├── Key Vault
├── Application Gateway + WAF
├── Virtual Network
├── Private Endpoint
├── Private DNS
├── Entra ID
└── Azure Monitor
```

---

# 11.2 What is ADLS Gen2?

### Direct Answer

**Azure Data Lake Storage Gen2** is used as the central data storage layer for our ML platform.

It provides scalable storage for:

- Raw data
- Processed data
- Training datasets
- Feature data
- ML artifacts
- Historical data

### Project Architecture

```text
Data Sources
     ↓
Azure Data Factory
     ↓
ADLS Gen2
 ┌───────────────┐
 │ Raw           │
 │ Processed     │
 │ Curated       │
 │ Quarantine    │
 └───────────────┘
     ↓
Feature Engineering
     ↓
ML Training
```

---

# 11.3 Why Don't We Store Everything in MySQL?

### Direct Answer

**MySQL Flexible Server** and **ADLS Gen2** serve different purposes.

### MySQL

Used for operational/transactional data such as:

- Application data
- Request metadata
- Prediction metadata
- Operational records

### ADLS

Used for large-scale analytical and ML data:

- Raw datasets
- Historical data
- Training datasets
- Processed datasets
- Data versions

So:

```text
MySQL
   ↓
Operational / Transactional Data

ADLS
   ↓
Analytical / ML Data
```

---

# 11.4 Where Does Azure Database for MySQL Flexible Server Fit?

### Direct Answer

**Azure Database for MySQL Flexible Server** is part of our application/data infrastructure layer.

It is provisioned using **Terraform** and connected to the platform through private networking.

Architecture:

```text
Application
    ↓
AKS
    ↓
Private Network
    ↓
MySQL Flexible Server
```

The database is not a replacement for ADLS.

It complements ADLS by handling operational database workloads.

---

# 11.5 What is Azure Data Factory?

### Direct Answer

**Azure Data Factory (ADF)** is our **data ingestion and data orchestration layer**.

It is responsible for moving and preparing data before it enters the ML lifecycle.

Example:

```text
Source
  ↓
ADF Pipeline
  ↓
Validation
  ↓
ADLS Raw
  ↓
Processed / Quarantine
```

ADF can orchestrate:

- Data movement
- Scheduled ingestion
- Data transformation activities
- Pipeline dependencies
- Triggers
- Parameterized pipelines
- Failure handling

---

# 11.6 What is the Difference Between ADF, ML Workflow and Azure DevOps?

This is an important production architecture question.

### Azure Data Factory

Responsible for **data workflows**.

```text
Source
 ↓
Ingestion
 ↓
Validation
 ↓
Data Lake
```

### ML Workflow

Responsible for **machine-learning workflows**.

```text
Dataset
 ↓
Feature Engineering
 ↓
Training
 ↓
Evaluation
 ↓
Model Registration
```

### Azure DevOps

Responsible for **software delivery**.

```text
Git
 ↓
CI
 ↓
Testing
 ↓
Build
 ↓
ACR
 ↓
Deployment
```

### Simple Comparison

| Platform | Main Responsibility |
|---|---|
| ADF | Data orchestration |
| ML Workflow | ML lifecycle orchestration |
| Azure DevOps | Software CI/CD |

They work together but should not be treated as the same system.

---

# 11.7 What is a Virtual Network?

### Direct Answer

An **Azure Virtual Network (VNet)** provides private network connectivity for Azure resources.

Our platform uses a VNet such as:

```text
10.0.0.0/16
```

Example subnet structure:

```text
VNet
10.0.0.0/16
│
├── AKS Subnet
├── Application Gateway Subnet
├── Private Endpoint Subnet
└── Supporting Infrastructure Subnets
```

This provides network isolation and controlled communication between components.

---

# 11.8 What is a Private Endpoint?

### Direct Answer

A **Private Endpoint** provides private connectivity from a VNet to an Azure PaaS service using a private IP address.

Instead of:

```text
AKS
 ↓
Public Internet
 ↓
Azure Service
```

we aim for:

```text
AKS
 ↓
Private Network
 ↓
Private Endpoint
 ↓
Azure Service
```

We use private connectivity for services such as:

- ADLS
- ACR
- Key Vault
- MySQL Flexible Server

where supported by the architecture.

---

# 11.9 Private Endpoint vs Service Endpoint

### Private Endpoint

Uses a **private IP address** from the VNet.

```text
VNet
 ↓
Private IP
 ↓
Azure PaaS Service
```

### Service Endpoint

Extends VNet identity to the Azure service over the Azure backbone while the service continues to use its public endpoint.

### Simple Difference

```text
Private Endpoint
→ Private IP connectivity

Service Endpoint
→ VNet-based secure access to the service endpoint
```

For our production-oriented architecture, **Private Endpoint** is preferred where private connectivity is required.

---

# 11.10 Why Do We Need Private DNS?

### Direct Answer

When a service is accessed through a Private Endpoint, DNS must resolve its hostname to the correct **private IP address**.

Example:

```text
storage-account.azure.net
        ↓
DNS Resolution
        ↓
Private IP
        ↓
Private Endpoint
```

Without correct DNS configuration, the application may resolve the service to an incorrect/public endpoint or fail to connect as expected.

### Production Troubleshooting

We should verify:

```text
DNS Resolution
     ↓
Private IP
     ↓
Network Connectivity
     ↓
Authentication
     ↓
Application Connection
```

Commands such as `nslookup` can help during troubleshooting.

---

# 11.11 What is Azure Key Vault?

### Direct Answer

**Azure Key Vault** is used to securely store and manage sensitive information such as:

- Secrets
- Certificates
- Keys

We should avoid storing credentials directly in:

```text
Source Code
Dockerfile
Git Repository
Kubernetes YAML
Pipeline YAML
```

Instead:

```text
Application
    ↓
Identity
    ↓
Key Vault
    ↓
Secret / Certificate
```

---

# 11.12 Why Should We Avoid Hardcoded Secrets?

### Direct Answer

Hardcoded credentials create security and operational risks.

For example:

```text
password = "MyPassword123"
```

in source code can result in credential exposure through:

- Git history
- Logs
- Container images
- Developer machines
- Pull requests

Our architecture uses **Key Vault + identity-based access** instead.

---

# 11.13 What is Managed Identity?

### Direct Answer

**Managed Identity** allows an Azure resource to authenticate to supported Azure services without storing credentials in application code.

Example:

```text
AKS Workload
     ↓
Managed / Workload Identity
     ↓
Azure Entra ID
     ↓
Key Vault / Storage / Other Azure Service
```

The application does not need a hardcoded username/password.

---

# 11.14 Managed Identity vs Service Principal

### Service Principal

A service principal represents an application identity in Microsoft Entra ID.

It can authenticate using credentials such as:

- Secret
- Certificate
- Federated identity

### Managed Identity

Azure manages the identity lifecycle for the Azure resource.

This reduces the need to manually manage credentials.

### Project Approach

For workloads running in Azure, we prefer **managed/workload identity** where appropriate.

For automation that requires an application identity, we can use an appropriately secured **service principal or workload federation** rather than hardcoded credentials.

---

# 11.15 How Does AKS Access Key Vault?

A production-oriented flow is:

```text
Application Pod
      ↓
Workload Identity
      ↓
Microsoft Entra ID
      ↓
Authorization
      ↓
Azure Key Vault
      ↓
Secret / Certificate
```

The important principle is:

> The application authenticates using an identity instead of embedding credentials.

---

# 11.16 What is Azure Container Registry?

### Direct Answer

**Azure Container Registry (ACR)** is used to store our Docker container images.

Example:

```text
Source Code
    ↓
Azure DevOps CI
    ↓
Docker Build
    ↓
Security Scan
    ↓
ACR
    ↓
AKS
```

Example image lifecycle:

```text
rag-api:build-101
rag-api:build-102
rag-api:build-103
```

For stronger traceability, the deployment should also retain the **immutable image digest**.

---

# 11.17 Why Do We Need Application Gateway?

### Direct Answer

**Azure Application Gateway** acts as an application-layer entry point for HTTP/HTTPS traffic.

It can provide:

- Layer 7 routing
- TLS termination
- Web Application Firewall
- Host/path-based routing
- Integration with AKS ingress architecture

Our simplified request path is:

```text
User
 ↓
Application Gateway
 ↓
WAF
 ↓
AKS Ingress
 ↓
Kubernetes Service
 ↓
Pod
```

---

# 11.18 What is WAF?

### Direct Answer

**Web Application Firewall (WAF)** helps protect web applications from common web-layer attacks.

It provides an additional security layer before traffic reaches the application.

Architecture:

```text
Internet
   ↓
Application Gateway
   ↓
WAF
   ↓
Ingress
   ↓
Application
```

WAF is part of the **application security boundary** and does not replace Kubernetes NetworkPolicy or identity-based access controls.

---

# 11.19 What is Azure Monitor?

### Direct Answer

**Azure Monitor** provides monitoring and observability for Azure resources and applications.

In our platform, observability is split across multiple layers:

```text
Infrastructure
Application
ML
RAG / LLM
Business
```

We use Azure-native services such as:

- Azure Monitor
- Log Analytics
- Application Insights

alongside:

- Prometheus
- Grafana

---

# 11.20 How Would You Troubleshoot an Azure Connectivity Issue?

### Direct Answer

I would troubleshoot from the lower layers upward.

```text
1. DNS
   ↓
2. Private Endpoint
   ↓
3. NSG / Network Rules
   ↓
4. Routing
   ↓
5. Identity / RBAC
   ↓
6. Service Configuration
   ↓
7. Application
```

For example, if an AKS application cannot connect to MySQL:

```text
Check DNS
 ↓
Check MySQL private IP
 ↓
Check NSG / network connectivity
 ↓
Check MySQL firewall/network configuration
 ↓
Check identity/credentials
 ↓
Check application connection string
 ↓
Check application logs
```

This avoids immediately changing application code when the actual problem may be networking or authentication.

---

# 11.21 Azure Interview Answer Pattern

For Azure questions, use:

```text
What is it?
    ↓
Why do we need it?
    ↓
Where is it used in our architecture?
    ↓
How is it secured?
    ↓
What happens if it fails?
    ↓
How would I troubleshoot it?
```

This demonstrates **Azure knowledge + architecture understanding + production troubleshooting**.

# 12. Kubernetes Interview Questions

## 12.1 What is Kubernetes?

### Direct Answer

**Kubernetes** is a container orchestration platform used to deploy, scale, manage, and recover containerized applications.

In our project, **AKS** provides the Kubernetes platform for running:

- ML inference API
- RAG API
- Health services
- Supporting workloads

Basic architecture:

```text
Docker Image
     ↓
ACR
     ↓
AKS
     ↓
Pod
     ↓
Application
```

---

# 12.2 What is a Pod?

### Direct Answer

A **Pod** is the smallest deployable unit in Kubernetes.

A Pod contains one or more containers that share:

- Network namespace
- IP address
- Storage volumes where configured

For our application:

```text
AKS
 ↓
Pod
 └── ML API Container
```

Normally, we run application containers through a **Deployment** rather than creating individual Pods manually.

---

# 12.3 What is a Deployment?

### Direct Answer

A **Deployment** manages the desired state of stateless application Pods.

It provides:

- Replica management
- Rolling updates
- Rollback
- Self-healing through ReplicaSets
- Declarative configuration

Example:

```text
Deployment
     ↓
ReplicaSet
     ↓
┌─────────┬─────────┬─────────┐
│ Pod 1   │ Pod 2   │ Pod 3   │
└─────────┴─────────┴─────────┘
```

If one Pod fails, Kubernetes can create another Pod to maintain the desired replica count.

---

# 12.4 What is a Kubernetes Service?

### Direct Answer

A **Service** provides a stable network endpoint for a set of Pods.

Pods are temporary and their IP addresses can change.

Instead of connecting directly to:

```text
Pod IP
```

applications connect through:

```text
Service
   ↓
Pods
```

Example:

```text
RAG API Service
      ↓
┌─────────┬─────────┬─────────┐
│ Pod 1   │ Pod 2   │ Pod 3   │
└─────────┴─────────┴─────────┘
```

The Service also provides load balancing across matching Pods.

---

# 12.5 What is Ingress?

### Direct Answer

**Ingress** provides HTTP/HTTPS routing into Kubernetes services.

Example:

```text
User
 ↓
Application Gateway / WAF
 ↓
Ingress
 ├── /ml    → ML API Service
 └── /rag   → RAG API Service
```

Ingress allows us to route requests based on:

- Host
- Path
- HTTP/HTTPS configuration

---

# 12.6 Service vs Ingress

### Service

Provides networking to Pods.

```text
Service
 ↓
Pods
```

### Ingress

Provides HTTP/HTTPS routing to Services.

```text
Ingress
 ├── Service A
 └── Service B
```

Simple rule:

> **Service connects to Pods; Ingress routes external HTTP/HTTPS traffic to Services.**

---

# 12.7 Explain the Request Flow in Our AKS Platform

```text
User
 ↓
Application Gateway
 ↓
WAF
 ↓
AKS Ingress
 ↓
Kubernetes Service
 ↓
Pod
 ↓
Application
 ↓
Model / RAG Pipeline
```

For ML inference:

```text
Request
 ↓
Ingress
 ↓
ML API Service
 ↓
ML API Pod
 ↓
Model
 ↓
Prediction
```

For RAG:

```text
Request
 ↓
Ingress
 ↓
RAG API Service
 ↓
RAG API Pod
 ↓
Qdrant
 ↓
Reranker
 ↓
LLM
 ↓
Response
```

---

# 12.8 What is HPA?

### Direct Answer

**Horizontal Pod Autoscaler (HPA)** automatically changes the number of Pod replicas based on configured metrics.

Example:

```text
Low Traffic
   ↓
2 Pods

High Traffic
   ↓
5 Pods
```

In our inference services, HPA helps handle changing workloads.

However, CPU utilization alone may not represent actual application load, so production monitoring should also consider metrics such as:

- Request rate
- Latency
- Error rate
- Queue depth where applicable

---

# 12.9 What are Resource Requests and Limits?

### Resource Requests

The amount of CPU/memory Kubernetes uses when scheduling a Pod.

Example:

```yaml
resources:
  requests:
    cpu: "500m"
    memory: "512Mi"
```

### Resource Limits

The maximum CPU/memory the container is allowed to consume.

Example:

```yaml
resources:
  limits:
    cpu: "1"
    memory: "1Gi"
```

Simple explanation:

```text
Request → Used for scheduling
Limit   → Maximum allowed resource
```

Correct requests and limits are important for:

- Scheduling
- Stability
- Autoscaling
- Capacity planning

---

# 12.10 What is a Readiness Probe?

### Direct Answer

A **readiness probe** tells Kubernetes whether a Pod is ready to receive traffic.

Example:

```text
Pod starts
   ↓
Application initializing
   ↓
Not Ready
   ↓
Model loaded
   ↓
Ready
   ↓
Traffic allowed
```

This is especially important for ML services because loading a model can take time.

---

# 12.11 What is a Liveness Probe?

### Direct Answer

A **liveness probe** checks whether the application is still functioning.

If the container repeatedly fails the liveness check, Kubernetes can restart it.

Simple difference:

```text
Readiness
→ Can this Pod receive traffic?

Liveness
→ Is this container still functioning?
```

---

# 12.12 What is a Startup Probe?

### Direct Answer

A **startup probe** is useful when an application takes a long time to start.

For example, an ML service may need time to:

```text
Start container
 ↓
Initialize dependencies
 ↓
Load model
 ↓
Initialize application
 ↓
Become ready
```

Startup probes can prevent liveness checks from restarting the application prematurely during initialization.

---

# 12.13 What is a Pod Disruption Budget?

### Direct Answer

A **Pod Disruption Budget (PDB)** helps maintain a minimum level of application availability during voluntary disruptions.

For example:

```text
Application
3 replicas

PDB:
minimumAvailable = 2
```

This helps protect availability during operations such as node maintenance or voluntary Pod eviction.

PDB does not protect against every type of failure.

---

# 12.14 What is NetworkPolicy?

### Direct Answer

**NetworkPolicy** controls which network traffic is allowed between Kubernetes Pods and namespaces, depending on the cluster networking implementation.

Without appropriate restrictions:

```text
Pod A ─────→ Pod B
Pod A ─────→ Pod C
Pod A ─────→ Pod D
```

With NetworkPolicy:

```text
RAG API
   │
   ├──→ Qdrant ✓
   │
   ├──→ LLM Service ✓
   │
   └──→ Unrelated Service ✗
```

The principle is:

> **Allow only the communication that is required.**

This is part of our defense-in-depth security model.

---

# 12.15 DaemonSet vs StatefulSet

## DaemonSet

A **DaemonSet** ensures that a Pod runs on each eligible node, or on each node matching its scheduling rules.

Common use cases:

- Node-level monitoring agents
- Log collection agents
- Networking components

Example:

```text
Node 1 → Agent
Node 2 → Agent
Node 3 → Agent
```

## StatefulSet

A **StatefulSet** is designed for applications that need stable identity and/or persistent storage characteristics.

Common use cases:

- Databases
- Stateful distributed systems

Example:

```text
Pod-0
Pod-1
Pod-2
```

The Pods have stable identities.

### Simple Difference

```text
DaemonSet
→ One Pod per eligible node

StatefulSet
→ Stable identity for stateful workloads
```

Our stateless ML/RAG APIs are generally better represented by **Deployments**.

---

# 12.16 What is kubelet?

### Direct Answer

**kubelet** is the Kubernetes node agent.

It runs on each worker node and is responsible for ensuring that the Pods assigned to that node are running as specified.

Simplified:

```text
Kubernetes Control Plane
        ↓
     kubelet
        ↓
Worker Node
        ↓
Containers
```

---

# 12.17 What is kube-proxy?

### Direct Answer

**kube-proxy** is a node-level networking component that helps implement Kubernetes Service networking.

It helps direct network traffic destined for Services toward the appropriate backend Pods, according to the cluster's networking implementation.

Simplified:

```text
Client
 ↓
Service
 ↓
kube-proxy / service networking
 ↓
Pod
```

In modern Kubernetes environments, the exact packet-processing implementation can vary depending on the networking technology and dataplane.

---

# 12.18 What is etcd?

### Direct Answer

**etcd** is a distributed key-value store used by Kubernetes to store cluster state and configuration data.

Examples of information represented in Kubernetes state include:

- Pods
- Deployments
- Services
- Configurations
- Secrets
- Cluster metadata

Simplified:

```text
kubectl
   ↓
API Server
   ↓
etcd
```

The Kubernetes API Server is the primary interface for interacting with cluster state.

---

# 12.19 What Happens When a Pod Crashes?

### Direct Answer

If the Pod is managed by a Deployment and the desired replica count is not satisfied, Kubernetes attempts to create a replacement.

Example:

```text
Deployment
Desired replicas = 3

Current:
Pod 1 ✓
Pod 2 ✗
Pod 3 ✓

Kubernetes
    ↓
Creates replacement
    ↓
Pod 4 ✓
```

However, if the application repeatedly fails during startup, we may see:

```text
CrashLoopBackOff
```

---

# 12.20 How Would You Troubleshoot CrashLoopBackOff?

### Direct Answer

I would investigate systematically:

```text
1. Check Pod status
        ↓
2. Describe Pod
        ↓
3. Check current logs
        ↓
4. Check previous container logs
        ↓
5. Check events
        ↓
6. Check configuration
        ↓
7. Check secrets
        ↓
8. Check environment variables
        ↓
9. Check probes
        ↓
10. Check resource limits
```

Useful commands:

```bash
kubectl get pods -n <namespace>

kubectl describe pod <pod-name> -n <namespace>

kubectl logs <pod-name> -n <namespace>

kubectl logs <pod-name> -n <namespace> --previous

kubectl get events -n <namespace> --sort-by=.lastTimestamp
```

Possible causes include:

- Application startup failure
- Missing configuration
- Missing secret
- Incorrect environment variable
- Failed dependency connection
- Failed health probe
- Insufficient memory
- Incorrect container command

---

# 12.21 How Would You Troubleshoot 502 Bad Gateway?

### Direct Answer

A **502 Bad Gateway** generally means a gateway or proxy could not successfully obtain a valid response from its upstream.

I would trace the request path:

```text
Client
 ↓
Application Gateway
 ↓
Ingress
 ↓
Service
 ↓
Pod
 ↓
Application
```

Then check each layer.

```text
1. Application Gateway
2. Ingress
3. Service
4. Endpoints
5. Pod health
6. Application logs
7. Network connectivity
8. Backend response
```

Useful commands:

```bash
kubectl get ingress -n <namespace>

kubectl describe ingress <ingress-name> -n <namespace>

kubectl get svc -n <namespace>

kubectl get endpoints -n <namespace>

kubectl get pods -n <namespace>

kubectl logs <pod-name> -n <namespace>
```

Possible causes include:

- No healthy backend Pods
- Incorrect Service selector
- Incorrect target port
- Ingress configuration issue
- Application not listening on expected port
- Readiness probe failure
- NetworkPolicy blocking traffic
- Application failure

---

# 12.22 How Would You Troubleshoot High Inference Latency?

### Direct Answer

I would first identify **where the latency is being introduced**.

```text
Request
 ↓
Gateway
 ↓
Ingress
 ↓
Service
 ↓
Pod
 ↓
Feature retrieval
 ↓
Model inference
 ↓
Response
```

I would check:

- p50 latency
- p95 latency
- p99 latency
- CPU
- Memory
- Pod restarts
- HPA behavior
- Model loading
- Feature retrieval latency
- Network latency
- Dependency latency

For RAG:

```text
Request
 ↓
Embedding
 ↓
Qdrant retrieval
 ↓
Reranking
 ↓
LLM generation
 ↓
Response
```

Each stage should be measured separately where possible.

---

# 12.23 How Would You Debug a Kubernetes Service That Cannot Reach Another Service?

Use a layered approach:

```text
1. Check Pod status
       ↓
2. Check Service
       ↓
3. Check Service selector
       ↓
4. Check Endpoints / EndpointSlices
       ↓
5. Check DNS
       ↓
6. Check NetworkPolicy
       ↓
7. Check ports
       ↓
8. Test connectivity
       ↓
9. Check application logs
```

Example:

```bash
kubectl get svc -n <namespace>

kubectl get endpoints -n <namespace>

kubectl get pods -n <namespace> --show-labels

kubectl get networkpolicy -n <namespace>
```

For DNS troubleshooting:

```bash
nslookup <service-name>
```

from an appropriate test Pod.

---

# 12.24 Kubernetes Production Checklist

For our application workloads, we should consider:

```text
✓ Deployment
✓ Multiple replicas
✓ Resource requests
✓ Resource limits
✓ Readiness probe
✓ Liveness probe
✓ Startup probe where needed
✓ HPA
✓ PDB
✓ NetworkPolicy
✓ ConfigMap
✓ Secret / Key Vault integration
✓ Proper Service
✓ Ingress
✓ Logging
✓ Metrics
✓ Tracing
✓ Security scanning
✓ Rollback strategy
```

---

# 12.25 Kubernetes Interview Answer Pattern

For Kubernetes questions, explain:

```text
What is it?
    ↓
Why do we need it?
    ↓
Where is it used?
    ↓
How does traffic flow?
    ↓
What happens when it fails?
    ↓
How would I troubleshoot it?
```

The goal is to demonstrate **Kubernetes concepts + AKS implementation + production troubleshooting**.

# 13. DevOps Interview Questions

## 13.1 What is CI/CD?

### Direct Answer

**CI/CD** is a software delivery practice that automates the process from code changes to testing, packaging, and deployment.

In our platform:

```text
Developer
   ↓
Git
   ↓
Azure DevOps CI
   ↓
Tests + Security Checks
   ↓
Docker Build
   ↓
ACR
   ↓
Continuous Testing
   ↓
Staging
   ↓
Approval
   ↓
Production AKS
```

### CI — Continuous Integration

CI validates code changes through activities such as:

- Build
- Unit tests
- Integration tests
- Static analysis
- Dependency scanning
- Secret scanning
- Container build

### CD — Continuous Delivery/Deployment

CD takes a validated artifact and deploys it to the target environment.

---

# 13.2 What Happens When a Developer Pushes Code?

### Direct Answer

The pipeline starts from the Git repository and validates the change before deployment.

Example:

```text
Git Push
   ↓
Pipeline Trigger
   ↓
Checkout Code
   ↓
Unit Tests
   ↓
Integration Tests
   ↓
SAST
   ↓
Dependency Scan
   ↓
Secret Scan
   ↓
Docker Build
   ↓
Container Scan
   ↓
SBOM
   ↓
Push Image to ACR
   ↓
Continuous Testing
   ↓
Staging
   ↓
Approval
   ↓
Production
```

The exact stages can vary depending on the workload.

---

# 13.3 What is Continuous Testing?

### Direct Answer

**Continuous Testing** means continuously validating the software and ML system throughout the delivery lifecycle rather than testing only at the end.

For our platform, testing includes:

```text
Code
 ↓
Unit Testing
 ↓
Integration Testing
 ↓
Data Testing
 ↓
Model Testing
 ↓
RAG Testing
 ↓
API Testing
 ↓
Performance Testing
 ↓
Security Testing
```

### ML-Specific Testing

We can validate:

- Input schema
- Data quality
- Model metrics
- Prediction behavior
- Model compatibility
- Inference latency

### RAG-Specific Testing

We can validate:

- Retrieval quality
- Context relevance
- Groundedness
- Answer relevance
- Safety
- Prompt behavior

---

# 13.4 Why Should CI/CD and ML Training Not Be Treated as the Same Pipeline?

### Direct Answer

They have different responsibilities.

### CI/CD

Responsible for **software delivery**:

```text
Code
 ↓
Test
 ↓
Build
 ↓
Package
 ↓
Deploy
```

### ML Workflow

Responsible for **model lifecycle**:

```text
Data
 ↓
Features
 ↓
Training
 ↓
Evaluation
 ↓
Registration
 ↓
Model Candidate
```

They interact through controlled artifacts and approvals.

```text
ML Workflow
     ↓
Validated Model
     ↓
Model Registry
     ↓
Deployment Pipeline
     ↓
AKS
```

---

# 13.5 Why Do We Build a Docker Image?

### Direct Answer

We package the application and its runtime dependencies into a **Docker container image**.

This provides consistency between environments.

Example:

```text
Source Code
+
Python Runtime
+
Dependencies
+
Application
        ↓
   Docker Image
        ↓
       ACR
        ↓
       AKS
```

The same validated image can then be promoted through environments.

---

# 13.6 ADD vs COPY in Docker

### COPY

Copies files or directories from the build context into the image.

```dockerfile
COPY . /app
```

### ADD

Can also copy files, and Docker provides additional behavior such as handling local tar archives.

For predictable Dockerfiles, **COPY is generally preferred when those extra ADD behaviors are not required**.

Simple interview answer:

> COPY is the straightforward file-copy instruction, while ADD has additional behavior. I prefer COPY unless I specifically need ADD functionality.

---

# 13.7 What is Azure Container Registry?

### Direct Answer

**ACR** is the private container registry used to store our Docker images.

Flow:

```text
Azure DevOps
      ↓
Docker Build
      ↓
Security Scan
      ↓
ACR
      ↓
AKS
```

We should maintain traceability between:

```text
Git Commit
   ↓
Pipeline Run
   ↓
Docker Image
   ↓
Image Digest
   ↓
AKS Deployment
```

---

# 13.8 Why Should We Use Image Digests?

### Direct Answer

A mutable image tag can potentially point to a different image later.

An **image digest** identifies a specific image content.

Example:

```text
rag-api:production
       ↓
Current digest
       ↓
sha256:...
```

For stronger production traceability, we record the digest associated with the deployed artifact.

This helps answer:

> Exactly which container image is running in production?

---

# 13.9 What Security Checks Should Be Present in CI/CD?

A production-oriented pipeline can include:

```text
Source Code
    ↓
SAST
    ↓
Dependency / License Scan
    ↓
Secret Scan
    ↓
Docker Build
    ↓
Container Scan
    ↓
SBOM
    ↓
Image Signing
    ↓
Deployment Verification
```

### Examples

**SAST**

Finds security issues in source code.

**Dependency Scan**

Checks third-party dependencies for known vulnerabilities and policy issues.

**Secret Scan**

Detects accidentally committed credentials.

**Container Scan**

Checks container images for known vulnerabilities.

**SBOM**

Provides a software component inventory.

**Image Signing**

Provides a mechanism to verify that an image came from an expected trusted build process.

---

# 13.10 What is Terraform?

### Direct Answer

**Terraform** is an Infrastructure as Code tool used to define and provision infrastructure declaratively.

In our project Terraform manages resources such as:

- Resource Groups
- VNet
- Subnets
- NSGs
- AKS
- ADLS
- ACR
- Key Vault
- Application Gateway
- Private Endpoints
- Private DNS
- MySQL Flexible Server
- Monitoring resources

Example:

```text
Terraform Code
      ↓
Terraform Plan
      ↓
Review
      ↓
Terraform Apply
      ↓
Azure Infrastructure
```

---

# 13.11 Why Use Terraform Instead of Creating Azure Resources Manually?

### Direct Answer

Terraform provides:

- Repeatability
- Version control
- Reusable modules
- Consistent environments
- Change visibility
- Infrastructure drift detection
- Automated provisioning

For example:

```text
Terraform
   ↓
Dev
Staging
Prod
```

The same reusable modules can be configured differently for each environment.

---

# 13.12 What is Terraform State?

### Direct Answer

Terraform state keeps track of the relationship between the **Terraform configuration and the infrastructure Terraform manages**.

Simplified:

```text
Terraform Code
      ↕
Terraform State
      ↕
Azure Resources
```

Terraform uses this information when determining what changes are required.

---

# 13.13 Why Use a Remote Terraform Backend?

### Direct Answer

A remote backend allows Terraform state to be stored centrally rather than on an individual developer's machine.

Benefits include:

- Team collaboration
- Centralized state
- Better access control
- State protection
- Consistent execution

For Azure, an Azure Storage-based backend can be used for Terraform state.

---

# 13.14 What is Terraform Drift?

### Direct Answer

**Drift** occurs when the actual infrastructure differs from what Terraform configuration and state expect.

Example:

```text
Terraform Configuration
        ↓
Expected Infrastructure

Azure Portal / Manual Change
        ↓
Actual Infrastructure

Expected ≠ Actual
        ↓
Drift
```

Example:

> Someone manually changes an NSG rule in Azure Portal even though the configuration is managed by Terraform.

We can detect changes using:

```bash
terraform plan
```

The plan shows Terraform's proposed changes based on the current configuration, state, and observed infrastructure.

---

# 13.15 What is `count` vs `for_each`?

### `count`

Useful when resources are naturally represented by an indexed collection.

Example:

```hcl
count = var.vm_count
```

Resources are addressed using indexes.

```text
VM[0]
VM[1]
VM[2]
```

### `for_each`

Useful when resources are naturally represented by unique keys.

Example:

```hcl
for_each = var.vms
```

Resources can be addressed using meaningful keys.

```text
vm["app"]
vm["worker"]
vm["monitoring"]
```

### Simple Interview Answer

> I use `count` when index-based repetition is sufficient and `for_each` when stable meaningful keys make resource management clearer.

---

# 13.16 What are Terraform Modules?

### Direct Answer

A **Terraform module** is a reusable collection of Terraform configuration.

Our structure contains modules such as:

```text
modules/
├── resource-group/
├── vnet/
├── aks/
├── adls/
├── acr/
├── key-vault/
├── app-gateway/
├── private-endpoint/
├── private-dns/
├── monitoring/
└── mysql-flexible-server/
```

This avoids duplicating infrastructure code across environments.

---

# 13.17 How Would You Structure Terraform Environments?

Our architecture separates environments:

```text
infrastructure/
└── terraform/
    ├── modules/
    │   ├── vnet/
    │   ├── aks/
    │   └── ...
    │
    └── environments/
        ├── dev/
        ├── staging/
        └── prod/
```

The modules contain reusable infrastructure logic.

The environments provide environment-specific configuration.

---

# 13.18 How Do You Handle Git Merge vs Rebase?

### Merge

Combines branches and preserves the branch history.

```text
A──B──C
     \
      D──E
          \
           M
```

### Rebase

Moves commits onto a new base.

```text
A──B──C──D──E
```

Rebase can create a cleaner linear history, but it rewrites commit history.

### Interview Rule

> I avoid rebasing shared branches because rewriting shared history can affect other developers.

---

# 13.19 What is Git Cherry-Pick?

### Direct Answer

**Cherry-pick** applies a specific commit from one branch onto another branch.

Example:

```text
Feature Branch
      ↓
Commit ABC
      ↓
Cherry-pick
      ↓
Release Branch
```

It is useful when we need a specific fix without merging the entire branch.

---

# 13.20 How Would You Roll Back a Bad Application Deployment?

### Direct Answer

First, I would verify whether the issue is caused by the new application version.

If rollback is required:

```text
Production
   ↓
New Version
   ↓
Issue Detected
   ↓
Rollback
   ↓
Previous Validated Version
```

In Kubernetes, a Deployment can retain rollout history that can be used for rollback.

Example:

```bash
kubectl rollout history deployment/<deployment-name> -n <namespace>

kubectl rollout undo deployment/<deployment-name> -n <namespace>
```

After rollback, I would verify:

- Pod health
- Readiness
- Error rate
- Latency
- Application functionality
- Business impact

---

# 13.21 Rolling vs Canary vs Blue-Green Deployment

## Rolling Deployment

Gradually replaces old Pods with new Pods.

```text
Old:  █████
New:     █████
```

There may be a period where old and new versions coexist.

---

## Canary Deployment

Sends a small percentage of traffic to the new version.

```text
90% → V1
10% → V2
```

We monitor the candidate before increasing traffic.

---

## Blue-Green Deployment

Maintains two environments:

```text
Blue  → Current Production
Green → New Version
```

After validation, traffic can be switched to Green.

If necessary, traffic can be switched back to Blue.

---

# 13.22 How Do You Choose a Deployment Strategy?

The choice depends on:

- Risk
- Traffic
- Rollback requirements
- Infrastructure cost
- Validation time
- Application architecture
- State management

For our platform, we document and support:

```text
Rolling
Canary
Blue-Green
```

The strategy should be selected according to the specific workload and release risk.

---

# 13.23 What Happens If CI Passes but Deployment Fails?

### Direct Answer

I separate the pipeline into stages and identify the failed boundary.

```text
Code
 ↓
CI ✓
 ↓
Build ✓
 ↓
Security ✓
 ↓
ACR ✓
 ↓
Deployment ✗
```

Then investigate:

```text
Kubernetes
 ↓
Deployment
 ↓
ReplicaSet
 ↓
Pod
 ↓
Container
 ↓
Configuration
 ↓
Secret / Identity
 ↓
Network
```

Possible causes include:

- Invalid Kubernetes manifest
- Image pull failure
- Authentication failure
- Missing configuration
- Missing secret
- Insufficient resources
- Failed readiness probe
- NetworkPolicy issue

---

# 13.24 What Happens If the Docker Image Cannot Be Pulled?

I would check:

```text
1. Image name
2. Image tag/digest
3. Image existence in ACR
4. AKS → ACR authorization
5. Identity configuration
6. Network connectivity
7. Pod events
```

Useful command:

```bash
kubectl describe pod <pod-name> -n <namespace>
```

Look for events such as:

```text
ErrImagePull
ImagePullBackOff
```

The important point is to distinguish:

```text
Image doesn't exist
vs
Authentication failed
vs
Network connectivity failed
```

---

# 13.25 DevOps Production Flow

Our complete delivery model is:

```text
Developer
    ↓
Git
    ↓
Azure DevOps CI
    ↓
Unit Tests
    ↓
Integration Tests
    ↓
Security Checks
    ↓
Docker Build
    ↓
Container Scan
    ↓
SBOM / Signing
    ↓
ACR
    ↓
Continuous Testing
    ↓
Staging
    ↓
Approval
    ↓
Production AKS
    ↓
Monitoring
    ↓
Rollback if Required
```

---

# 13.26 DevOps Interview Answer Pattern

For DevOps questions, explain:

```text
Concept
   ↓
Why we use it
   ↓
Pipeline position
   ↓
Security consideration
   ↓
Failure scenario
   ↓
Troubleshooting
   ↓
Rollback / Recovery
```

The objective is to demonstrate **automation + security + reliability + production troubleshooting**.

# 14. GenAI / RAG Interview Questions

## 14.1 What is an LLM?

### Direct Answer

An **LLM (Large Language Model)** is a machine learning model trained on large amounts of text to understand and generate natural language.

In our platform, LLMs are used as the **generation layer** of the RAG system.

Examples:

- Llama 3.1 8B
- Mistral 7B

The LLM does not directly act as our enterprise knowledge database.

Instead, we provide relevant retrieved context to the model.

---

# 14.2 What is RAG?

### Direct Answer

**RAG (Retrieval-Augmented Generation)** combines information retrieval with an LLM.

Instead of asking the LLM to answer only from its internal knowledge:

```text
User Question
      ↓
LLM
      ↓
Answer
```

we retrieve relevant information first:

```text
User Question
      ↓
Embedding
      ↓
Vector Search
      ↓
Relevant Documents
      ↓
Reranking
      ↓
LLM
      ↓
Grounded Answer
```

This allows the system to use an external knowledge base.

---

# 14.3 Why Do We Need RAG?

### Direct Answer

An LLM's internal knowledge may not contain our latest or private enterprise information.

For example, suppose our knowledge base contains:

```text
HR Leave Policy
IT Access Policy
Security Policy
Expense Policy
Incident Management Policy
```

A user asks:

> How many leave days can an employee carry forward?

Instead of relying only on the LLM's general knowledge:

```text
Question
 ↓
LLM
```

we use:

```text
Question
 ↓
Retrieve relevant policy
 ↓
Provide policy as context
 ↓
LLM
 ↓
Answer
```

This improves the ability to provide answers grounded in the supplied documents.

---

# 14.4 Explain Our RAG Architecture

Our RAG flow is:

```text
User
 ↓
RAG API
 ↓
Query Processing
 ↓
Embedding Model
 ↓
Qdrant
 ↓
Candidate Documents
 ↓
Reranker
 ↓
Relevant Context
 ↓
Prompt
 ↓
LLM
 ↓
Response
```

Our selected components are:

```text
Embeddings
→ BGE-small-en-v1.5

Vector Database
→ Qdrant

Reranker
→ BGE-reranker-base

Framework
→ LangChain

LLMs
→ Llama 3.1 8B / Mistral 7B
```

---

# 14.5 What is an Embedding?

### Direct Answer

An **embedding** is a numerical representation of text.

Text:

```text
"How many vacation days are available?"
```

is converted into a vector:

```text
[0.12, -0.34, 0.87, ...]
```

Texts with similar meaning tend to have vectors that are closer according to the selected similarity method.

This allows semantic search.

---

# 14.6 Why Do We Need Embeddings?

Traditional keyword search may depend heavily on exact words.

For example:

```text
Question:
"How many vacation days do I get?"
```

Document:

```text
"Employees are entitled to annual leave..."
```

The words are different, but the meaning is related.

Embeddings allow us to search based on **semantic similarity** rather than only exact keyword matching.

---

# 14.7 What is Chunking?

### Direct Answer

**Chunking** means splitting large documents into smaller pieces before creating embeddings.

Example:

```text
Large Policy Document
        ↓
┌───────────────┐
│ Chunk 1       │
├───────────────┤
│ Chunk 2       │
├───────────────┤
│ Chunk 3       │
├───────────────┤
│ Chunk 4       │
└───────────────┘
```

Each chunk can then be:

```text
Chunk
 ↓
Embedding
 ↓
Qdrant
```

---

# 14.8 Why Not Embed the Entire Document?

Very large documents can reduce retrieval precision because the retrieved context may contain too much unrelated information.

Chunking allows us to retrieve smaller, more relevant pieces.

However, chunk size should be selected based on the document structure and evaluated rather than assuming one fixed size works for every dataset.

Important factors include:

- Chunk size
- Chunk overlap
- Document structure
- Metadata
- Retrieval performance
- Context window
- Evaluation results

---

# 14.9 What Metadata Should We Store With a Chunk?

Useful metadata can include:

```text
Document ID
Document name
Document version
Department
Document type
Section
Access classification
Created date
Updated date
Chunk ID
Embedding version
```

This metadata can support:

- Filtering
- Traceability
- Access control
- Debugging
- Re-indexing
- Evaluation

---

# 14.10 What is Qdrant?

### Direct Answer

**Qdrant** is the vector database used in our RAG architecture.

It stores:

```text
Vector
+
Document Content / Reference
+
Metadata
```

Example:

```text
User Question
      ↓
Embedding
      ↓
Qdrant Search
      ↓
Top-K Candidates
```

---

# 14.11 What is Top-K Retrieval?

### Direct Answer

**Top-K retrieval** means returning the K most relevant candidate documents or chunks for a query.

Example:

```text
Query
 ↓
Qdrant
 ↓
Top 5 chunks
```

If:

```text
K = 5
```

the retriever returns the five highest-scoring candidates according to the configured similarity/search strategy.

K is a tuning parameter and should be evaluated.

---

# 14.12 What is Reranking?

### Direct Answer

A **reranker** takes the initial retrieved candidates and scores them more carefully to determine which context is most relevant.

Our flow is:

```text
Query
 ↓
Qdrant
 ↓
Top-K Candidates
 ↓
BGE Reranker
 ↓
Best Relevant Chunks
 ↓
LLM
```

This creates a two-stage retrieval system:

```text
Stage 1
Fast candidate retrieval

        ↓

Stage 2
More precise reranking
```

---

# 14.13 Why Do We Need a Reranker If Vector Search Already Works?

Vector search is optimized for efficiently finding candidate results.

The reranker provides an additional relevance-ranking stage.

For example:

```text
Qdrant
 ↓
20 candidates
 ↓
Reranker
 ↓
Top 5 relevant chunks
 ↓
LLM
```

This can improve context selection, but it also adds latency and compute cost.

Therefore, the final architecture should be evaluated using:

- Retrieval quality
- Answer quality
- Latency
- Cost

---

# 14.14 What is LangChain?

### Direct Answer

**LangChain** is a framework that helps build applications around LLMs and related components.

In our project, it can coordinate components such as:

```text
Prompt
 ↓
Retriever
 ↓
Qdrant
 ↓
Reranker
 ↓
LLM
 ↓
Response
```

The important architectural principle is that the framework should orchestrate components rather than hide production concerns such as security, observability, evaluation, and versioning.

---

# 14.15 What is Prompt Versioning?

### Direct Answer

A production RAG system should treat prompts as **versioned configuration**, not as untracked strings inside application code.

Example:

```text
Prompt V1
Prompt V2
Prompt V3
```

Each production request should be traceable to the prompt version used.

Example lineage:

```text
Request ID
   ↓
Prompt V7
   ↓
RAG Config V4
   ↓
Embedding V3
   ↓
Retrieved Documents
   ↓
Reranker V2
   ↓
LLM Version
   ↓
Response
```

This helps us reproduce and investigate changes in answer quality.

---

# 14.16 What is RAG Configuration Versioning?

RAG behavior depends on more than the prompt.

Configuration can include:

```text
Chunk size
Chunk overlap
Top-K
Similarity settings
Reranker configuration
Prompt
Model
Temperature
Retrieval filters
```

These should be version controlled.

Example:

```text
RAG Config V1
    ↓
Chunk = X
Top-K = 10
Reranker = V1
Prompt = V3
```

If answer quality changes after a deployment, we can identify which configuration was used.

---

# 14.17 What is Hallucination?

### Direct Answer

A **hallucination** occurs when an LLM produces information that is unsupported, incorrect, or not grounded in the available evidence.

For a RAG system:

```text
Question
 ↓
Retrieved Context
 ↓
LLM
 ↓
Answer
```

The answer should be grounded in the retrieved context when the application requires grounded responses.

We should evaluate this rather than assuming that RAG eliminates hallucination.

---

# 14.18 How Do You Reduce Hallucinations in RAG?

A production approach can include:

```text
Good Document Ingestion
        ↓
Good Chunking
        ↓
Good Embeddings
        ↓
Good Retrieval
        ↓
Reranking
        ↓
Strong Prompt
        ↓
Groundedness Evaluation
        ↓
Monitoring
```

Additional controls can include:

- Require answers to be based on retrieved context
- Return citations/references where appropriate
- Define fallback behavior when evidence is insufficient
- Evaluate unsupported answers
- Monitor retrieval quality
- Version prompts and retrieval configuration

---

# 14.19 What Happens If No Relevant Document Is Found?

The system should not blindly generate an answer.

Example:

```text
Question
 ↓
Retrieval
 ↓
No sufficiently relevant context
 ↓
Fallback
```

Possible application behavior:

```text
"I don't have enough information in the available documents to answer this."
```

The exact fallback should be defined as part of application requirements.

---

# 14.20 What is Prompt Injection?

### Direct Answer

**Prompt injection** is an attack where untrusted input attempts to manipulate the instructions given to an LLM.

For example, a document or user input may contain instructions such as:

```text
Ignore previous instructions...
```

A production RAG system must treat retrieved documents and user content as **untrusted data**, not automatically as trusted instructions.

---

# 14.21 How Do We Protect the RAG System From Prompt Injection?

A defense-in-depth approach includes:

```text
Input Validation
      ↓
Document Trust Boundaries
      ↓
Prompt Separation
      ↓
Instruction Hierarchy
      ↓
Output Validation
      ↓
Security Testing
      ↓
Monitoring
```

We should also test malicious examples as part of continuous security/evaluation testing.

---

# 14.22 How Do We Handle PII in RAG?

### Direct Answer

We should identify and control sensitive information throughout the RAG lifecycle.

Potential controls include:

- Data classification
- Access control
- PII detection/redaction where required
- Encryption
- Private networking
- Least-privilege identity
- Audit logging
- Document-level access filtering

A key principle is:

> A user should retrieve only the documents they are authorized to access.

---

# 14.23 How Do We Evaluate a RAG System?

RAG evaluation should cover multiple dimensions.

### Retrieval

```text
Did we retrieve relevant context?
```

### Context Relevance

```text
Is the retrieved context relevant to the question?
```

### Groundedness / Faithfulness

```text
Is the generated answer supported by the retrieved context?
```

### Answer Relevance

```text
Does the answer actually answer the user's question?
```

### Safety

```text
Did the system avoid unsafe or unauthorized behavior?
```

### Operational Metrics

Also monitor:

- Latency
- Error rate
- Token usage
- Cost
- Throughput

---

# 14.24 Why Can't We Evaluate RAG Only by Looking at the Final Answer?

Because a poor answer can originate from different stages.

```text
Question
   ↓
Embedding
   ↓
Retrieval
   ↓
Reranking
   ↓
Prompt
   ↓
LLM
   ↓
Answer
```

If the answer is wrong, we need to determine whether:

```text
Retrieval failed
       OR
Reranking failed
       OR
Prompt failed
       OR
LLM generation failed
       OR
Source document was incorrect
```

Therefore, we should evaluate individual stages where possible.

---

# 14.25 What Should We Monitor in a RAG System?

### API

- Request rate
- Error rate
- Latency
- Availability

### Retrieval

- Retrieval latency
- Top-K results
- Similarity/relevance signals
- Empty retrieval rate

### Reranking

- Reranking latency
- Candidate count
- Selected context

### LLM

- Generation latency
- Token usage
- Model errors
- Request volume
- Cost

### Quality

- Groundedness
- Context relevance
- Answer relevance
- Evaluation scores

---

# 14.26 How Do You Troubleshoot a RAG Quality Drop?

### Direct Answer

I would investigate the pipeline stage by stage.

```text
Quality Drop
     ↓
Check Source Documents
     ↓
Check Document Version
     ↓
Check Chunking
     ↓
Check Embedding Version
     ↓
Check Qdrant Index
     ↓
Check Retrieval Results
     ↓
Check Reranker
     ↓
Check Prompt Version
     ↓
Check LLM Version
     ↓
Check Evaluation Results
```

The goal is to identify the **specific stage responsible for the degradation** rather than immediately changing the LLM.

---

# 14.27 How Do You Trace One RAG Request?

Every request should have a **Request ID / Correlation ID**.

Example:

```text
Request ID: RAG-2026-001
       ↓
Prompt Version: V7
       ↓
RAG Config: V4
       ↓
Embedding: V3
       ↓
Retrieved Chunks
       ↓
Reranker: V2
       ↓
LLM: Llama 3.1 8B
       ↓
Response
```

This provides production traceability.

It allows us to answer:

> Why did the system produce this response?

---

# 14.28 How Do You Control LLM Cost?

LLM cost can be affected by:

- Number of requests
- Input tokens
- Output tokens
- Model size
- Context size
- Retrieval count
- Reranking compute
- Infrastructure utilization

A production optimization flow is:

```text
Measure
 ↓
Identify Cost Driver
 ↓
Optimize
 ↓
Evaluate Quality
 ↓
Deploy
 ↓
Monitor
```

Possible optimizations include:

- Reduce unnecessary context
- Tune Top-K
- Use appropriate model size
- Cache suitable requests
- Control maximum output tokens
- Optimize retrieval
- Scale compute based on demand

Cost optimization must not reduce quality below defined acceptance criteria.

---

# 14.29 Llama 3.1 8B vs Mistral 7B

Both are candidate LLM workloads in our architecture.

The selection should be based on measured requirements such as:

- Response quality
- Latency
- Memory requirements
- Throughput
- Cost
- Supported workload
- Deployment constraints

We should benchmark the models against the same evaluation dataset rather than selecting one based only on parameter count.

---

# 14.30 End-to-End RAG Interview Answer

### Question

> Explain your RAG architecture.

### Answer

> We use a production-oriented RAG architecture where documents are first ingested and processed into chunks. Each chunk is converted into an embedding using BGE-small-en-v1.5 and stored in Qdrant along with metadata. When a user sends a query, we generate its embedding and retrieve candidate chunks from Qdrant. We then use BGE-reranker-base to improve the relevance ordering. The selected context is passed to an LLM such as Llama 3.1 8B or Mistral 7B through our RAG application. We use LangChain to orchestrate the retrieval and generation flow. For production, we also version prompts and RAG configuration, evaluate retrieval and answer quality, monitor latency and cost, and maintain request-level traceability so we can understand which configuration and documents were used for a response.

---

# 14.31 RAG Interview Answer Pattern

For RAG questions, explain:

```text
User Question
     ↓
Embedding
     ↓
Retrieval
     ↓
Reranking
     ↓
Context
     ↓
Prompt
     ↓
LLM
     ↓
Response
     ↓
Evaluation + Monitoring
```

Then connect it to:

```text
Security
+
Versioning
+
Observability
+
Evaluation
+
Cost
+
Production Reliability
```

# 15. Production Incident Interview Questions

This section focuses on answering incidents like a real production engineer.

The approach is:

```text
Detect
  ↓
Understand Impact
  ↓
Stabilize
  ↓
Investigate
  ↓
Fix
  ↓
Verify
  ↓
Prevent Recurrence
```

---

# 15.1 Production Incident Answer Framework

When an interviewer gives a production issue, use:

```text
1. What is the symptom?
2. What is the business impact?
3. What changed recently?
4. Which layer could be responsible?
5. How would I investigate?
6. What is the immediate mitigation?
7. What is the root cause?
8. How do I verify the fix?
9. How do I prevent recurrence?
```

Do not immediately assume the root cause.

First collect evidence.

---

# 15.2 Incident: Pod is in CrashLoopBackOff

### Question

> Your ML inference Pod is in CrashLoopBackOff. How will you troubleshoot it?

### Direct Answer

I would first determine why the container is repeatedly exiting.

```text
Pod
 ↓
Container starts
 ↓
Container exits
 ↓
Kubernetes restarts it
 ↓
Container exits again
 ↓
CrashLoopBackOff
```

### Investigation

```bash
kubectl get pods -n <namespace>

kubectl describe pod <pod-name> -n <namespace>

kubectl logs <pod-name> -n <namespace>

kubectl logs <pod-name> -n <namespace> --previous

kubectl get events -n <namespace> --sort-by=.lastTimestamp
```

### Things I Check

```text
Application startup
Environment variables
ConfigMap
Secrets
Key Vault integration
Container command
Dependencies
Health probes
CPU / memory
Network connectivity
```

### Possible Root Causes

- Application startup exception
- Missing configuration
- Missing secret
- Incorrect environment variable
- Failed dependency connection
- Incorrect probe
- Memory exhaustion
- Incorrect container command

### Stabilization

If a recent deployment caused the issue, I can roll back to the last known-good version while continuing the root-cause investigation.

### Verification

```text
Pod Running
   ↓
Ready
   ↓
No repeated restarts
   ↓
Application health check passes
   ↓
Traffic succeeds
```

---

# 15.3 Incident: 502 Bad Gateway

### Question

> Users are getting 502 Bad Gateway from your ML API. What will you check?

### Direct Answer

I would trace the request path layer by layer.

```text
User
 ↓
Application Gateway
 ↓
WAF
 ↓
Ingress
 ↓
Service
 ↓
Pod
 ↓
Application
```

### Investigation

```bash
kubectl get ingress -n <namespace>

kubectl describe ingress <ingress-name> -n <namespace>

kubectl get svc -n <namespace>

kubectl get endpoints -n <namespace>

kubectl get pods -n <namespace>

kubectl logs <pod-name> -n <namespace>
```

### Questions to Answer

```text
Is Application Gateway healthy?
        ↓
Is Ingress configured correctly?
        ↓
Does Service have endpoints?
        ↓
Are Pods Ready?
        ↓
Is the target port correct?
        ↓
Is the application listening?
        ↓
Is NetworkPolicy blocking traffic?
```

### Possible Root Causes

- No healthy backend Pods
- Incorrect Service selector
- Incorrect target port
- Ingress configuration error
- Application not listening on expected port
- Readiness failure
- NetworkPolicy restriction
- Backend application failure

---

# 15.4 Incident: High ML Inference Latency

### Question

> Your model API was responding in 100 ms but now takes 2 seconds. How will you investigate?

### Direct Answer

I would identify where the additional latency was introduced instead of immediately scaling the Pods.

```text
Request
 ↓
Gateway
 ↓
Ingress
 ↓
Service
 ↓
Pod
 ↓
Feature Retrieval
 ↓
Model
 ↓
Response
```

### Check

```text
p50 latency
p95 latency
p99 latency
CPU
Memory
Pod restarts
HPA
Model loading
Feature retrieval
Network latency
Dependency latency
```

### Possible Root Causes

- Increased traffic
- CPU throttling
- Memory pressure
- Insufficient replicas
- Slow feature retrieval
- Dependency latency
- Network issue
- Inefficient model inference
- New application version

### Action

```text
Identify bottleneck
      ↓
Mitigate
      ↓
Fix root cause
      ↓
Verify latency
```

---

# 15.5 Incident: Model Regression After Deployment

### Question

> A new model was deployed and business performance dropped. What will you do?

### Direct Answer

First, I would confirm whether the degradation correlates with the new model version.

```text
Production Model V7
       ↓
New Model V8
       ↓
Performance Drop
```

### Investigation

Check:

```text
Model version
Training run
Evaluation metrics
Input distribution
Feature quality
Feature freshness
Prediction distribution
Business metrics
Application errors
```

### Immediate Mitigation

If production impact is significant and rollback criteria are met:

```text
Model V8
   ↓
Rollback
   ↓
Model V7
```

### Root Cause Investigation

Possible causes:

- Training data problem
- Feature problem
- Distribution change
- Incorrect model configuration
- Training-serving skew
- Deployment configuration issue
- Evaluation gap

### Prevention

Improve:

- Evaluation gates
- Continuous testing
- Canary deployment
- Model monitoring
- Data validation
- Feature monitoring

---

# 15.6 Incident: Data Drift Detected

### Question

> Your monitoring system reports significant data drift. Will you immediately retrain the model?

### Direct Answer

**No.**

Drift is a signal that requires investigation.

```text
Drift Detected
      ↓
Validate Drift
      ↓
Investigate Cause
      ↓
Check Model Performance
      ↓
Check Business Impact
      ↓
Decide Whether Retraining Is Required
```

### Possible Causes

- Customer behavior changed
- New data source
- Data pipeline change
- Business process change
- Seasonal behavior
- Data quality issue

### Important Principle

> **Drift does not automatically mean the model is bad.**

We need to connect drift with actual model and business performance.

---

# 15.7 Incident: Feature Freshness Problem

### Question

> Your model uses a feature that has not been updated for several hours. What do you check?

### Investigation

```text
Feature
 ↓
Source Data
 ↓
ADF
 ↓
Processing
 ↓
Feature Engineering
 ↓
Feast
 ↓
Online Store
 ↓
Inference
```

Check:

- Source data freshness
- ADF pipeline status
- Transformation jobs
- Feature computation
- Feast materialization
- Online feature availability
- Feature timestamps
- Training-serving consistency

### Impact

Stale features can result in poor predictions even when the model itself has not changed.

---

# 15.8 Incident: Identity / RBAC Failure

### Question

> Your AKS application suddenly cannot access Key Vault. How do you troubleshoot it?

### Direct Answer

I would separate the investigation into:

```text
Identity
 ↓
Authentication
 ↓
Authorization
 ↓
Network
 ↓
Application
```

### Check

```text
Workload Identity configuration
Service account
Entra ID identity
Role assignment
Key Vault permissions
Private Endpoint
Private DNS
Network connectivity
Application logs
```

### Important Distinction

Authentication answers:

> Who are you?

Authorization answers:

> What are you allowed to access?

---

# 15.9 Incident: DNS Failure

### Question

> An AKS Pod cannot connect to a private Azure service. What will you check?

### Direct Answer

I would check DNS before assuming the service itself is unavailable.

```text
Application
 ↓
DNS Resolution
 ↓
Private IP
 ↓
Private Endpoint
 ↓
Network
 ↓
Azure Service
```

Example:

```bash
nslookup <service-hostname>
```

I would verify that the hostname resolves to the expected private IP.

Then check:

```text
Private DNS Zone
DNS Link
Private Endpoint
VNet
Routing
NSG
NetworkPolicy
Authentication
```

### Key Principle

> A connectivity problem can be caused by DNS, networking, identity, or the service itself. We need to isolate the layer.

---

# 15.10 Incident: Secret or Certificate Expiration

### Question

> Your application suddenly cannot authenticate because a certificate or secret expired. What do you do?

### Immediate Action

```text
Detect
 ↓
Confirm expiration
 ↓
Rotate credential / certificate
 ↓
Update dependent configuration
 ↓
Restart/reload application if required
 ↓
Verify authentication
```

### Prevention

Use:

- Key Vault
- Expiration monitoring
- Alerts
- Rotation procedures
- Avoid hardcoded credentials

The goal is to detect expiration **before** it becomes a production outage.

---

# 15.11 Incident: Qdrant Failure

### Question

> Your RAG application cannot retrieve documents from Qdrant. What will you check?

### Request Flow

```text
RAG API
 ↓
Embedding
 ↓
Qdrant
 ↓
Retrieved Documents
 ↓
Reranker
 ↓
LLM
```

### Investigation

Check:

```text
Qdrant health
Network connectivity
DNS
Authentication
Collection availability
Index status
Query errors
Latency
Resource utilization
Application logs
```

### Important Question

Determine whether the problem is:

```text
Qdrant unavailable
        OR
Network failure
        OR
Application configuration
        OR
Collection/index issue
```

---

# 15.12 Incident: RAG Quality Drop

### Question

> Users report that the RAG answers have become less relevant. What will you investigate?

### Direct Answer

I would trace the entire RAG pipeline.

```text
Question
 ↓
Embedding
 ↓
Retrieval
 ↓
Reranking
 ↓
Prompt
 ↓
LLM
 ↓
Answer
```

### Investigation

Check:

```text
Source documents
Document versions
Chunking
Embedding version
Qdrant index
Top-K retrieval
Reranker
Prompt version
RAG configuration
LLM version
Evaluation results
```

### Important Principle

Do not immediately replace the LLM.

First identify which stage changed or degraded.

---

# 15.13 Incident: CI/CD Pipeline Failure

### Question

> Your deployment pipeline suddenly fails. How do you troubleshoot it?

### Direct Answer

I first identify the exact failed stage.

```text
Source
 ↓
Build
 ↓
Unit Tests
 ↓
Security
 ↓
Docker
 ↓
ACR
 ↓
Continuous Testing
 ↓
Deployment
```

### Investigation

If the failure occurs during Docker build:

```text
Dockerfile
Dependencies
Build context
Base image
```

If ACR push fails:

```text
ACR availability
Identity
Authorization
Network
Image configuration
```

If AKS deployment fails:

```text
Manifest
Image
Identity
Resources
Secrets
Probes
Network
```

The key is to troubleshoot based on the **first failing stage**.

---

# 15.14 Incident: Model Rollback

### Question

> When would you roll back a model?

### Direct Answer

I would roll back when the deployed model violates predefined production acceptance criteria or creates unacceptable impact.

Example:

```text
Model V8
   ↓
Canary
   ↓
Quality / Error / Business Threshold Violated
   ↓
Rollback
   ↓
Model V7
```

Rollback is a stabilization mechanism.

After rollback:

```text
Stabilize
 ↓
Investigate
 ↓
Fix
 ↓
Retrain / Re-evaluate if required
 ↓
New Candidate
```

We should preserve the failed model version and its deployment/evaluation information for traceability.

---

# 15.15 Incident: Disaster Recovery

### Question

> What happens if a critical Azure component becomes unavailable?

### Direct Answer

We follow the documented **disaster recovery plan** based on the affected component and its RTO/RPO requirements.

The recovery process includes:

```text
Detect Failure
     ↓
Assess Impact
     ↓
Activate Recovery Procedure
     ↓
Restore Required Infrastructure/Data
     ↓
Restore Application
     ↓
Restore Model / Configuration
     ↓
Validate
     ↓
Return to Service
```

Recovery planning must cover:

- Application
- Infrastructure
- Data
- Model artifacts
- Container images
- Configuration
- RAG documents/indexes
- Secrets/configuration dependencies

---

# 15.16 Incident: Complete Production Debugging Example

### Scenario

> Users are getting 502 errors from the RAG API after a deployment.

### Investigation

I would follow:

```text
502
 ↓
Application Gateway
 ↓
Ingress
 ↓
Service
 ↓
Endpoints
 ↓
Pods
 ↓
Readiness
 ↓
Application Logs
```

Suppose we discover:

```text
Pods = Running
Pods = Not Ready
```

Then:

```text
Check readiness probe
        ↓
Probe returns failure
        ↓
Application logs
        ↓
Application cannot connect to Qdrant
        ↓
DNS resolution fails
        ↓
Private DNS configuration issue
```

### Root Cause

The RAG application cannot resolve the Qdrant endpoint because of a DNS configuration problem.

### Fix

Correct the relevant DNS configuration and verify connectivity.

### Verification

```text
DNS ✓
 ↓
Qdrant connectivity ✓
 ↓
Pod Ready ✓
 ↓
Service endpoints ✓
 ↓
Ingress ✓
 ↓
502 resolved ✓
```

### Prevention

Add:

- DNS integration testing
- Connectivity health checks
- Deployment smoke tests
- Monitoring
- Alerting
- Incident runbook

---

# 15.17 Production Incident Checklist

When an incident occurs:

```text
✓ Confirm the symptom
✓ Determine business impact
✓ Identify recent changes
✓ Check monitoring
✓ Check logs
✓ Check metrics
✓ Check traces
✓ Check dependencies
✓ Stabilize service
✓ Identify root cause
✓ Apply fix
✓ Verify recovery
✓ Document incident
✓ Add prevention
```

---

# 15.18 Interview Rule for Production Incidents

Never answer:

> "I will restart the Pod."

Instead explain:

```text
Symptom
   ↓
Evidence
   ↓
Root Cause
   ↓
Mitigation
   ↓
Permanent Fix
   ↓
Verification
   ↓
Prevention
```

A strong production engineer does not only **fix the immediate symptom**.

They also determine **why it happened and how to prevent it from happening again**.

# 16. System Design Interview Questions

## 16.1 Design a Production-Grade Azure MLOps + GenAI/RAG Platform

### Question

> Design a production-grade Azure platform that supports machine learning model training, deployment, monitoring, and an LLM/RAG application.

---

## 16.2 Start With Requirements

Before designing the architecture, clarify:

### ML Requirements

```text
What type of model?
Batch or real-time?
Prediction latency?
Expected traffic?
Retraining frequency?
Model accuracy requirements?
Rollback requirements?
```

### RAG Requirements

```text
What documents?
How frequently do documents change?
Expected number of users?
Response latency?
Required answer quality?
Access-control requirements?
LLM model?
Expected token usage?
```

### Platform Requirements

```text
Availability
Scalability
Security
Observability
Disaster Recovery
Cost
Compliance
```

---

# 16.3 High-Level Architecture

Our platform can be represented as:

```text
                         USERS
                           │
                           ▼
                 Application Gateway
                       + WAF
                           │
                           ▼
                      AKS Ingress
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
          ML API                    RAG API
              │                         │
              ▼                         ▼
        ML Inference              RAG Pipeline
              │                         │
              │                ┌────────┼────────┐
              │                │        │        │
              │                ▼        ▼        ▼
              │             Qdrant  Reranker   LLM
              │
              ▼
          Prediction
```

Data and ML lifecycle:

```text
Data Sources
     ↓
ADF
     ↓
ADLS Gen2
     ↓
Validation
     ↓
Feature Engineering
     ↓
Feast
     ↓
Training
     ↓
MLflow
     ↓
Model Registry
     ↓
Evaluation
     ↓
Deployment
     ↓
AKS
```

---

# 16.4 Explain the Data Layer

The data architecture is:

```text
Data Sources
      ↓
Azure Data Factory
      ↓
ADLS Gen2
 ┌────────────────┐
 │ Raw            │
 │ Processed      │
 │ Curated        │
 │ Quarantine     │
 └────────────────┘
      ↓
Feature Engineering
      ↓
Feast
```

### Why ADLS?

ADLS provides scalable storage for large ML datasets and historical data.

### Why Quarantine?

Invalid data should not silently enter the ML pipeline.

Example:

```text
Incoming Data
     ↓
Validation
   ┌─┴─────────────┐
   │               │
Valid           Invalid
   │               │
   ▼               ▼
Processed       Quarantine
```

---

# 16.5 Explain the ML Lifecycle

```text
Data
 ↓
Validation
 ↓
Feature Engineering
 ↓
Feast
 ↓
Training
 ↓
MLflow Tracking
 ↓
Evaluation
 ↓
Model Registry
 ↓
Approval
 ↓
Deployment
 ↓
Monitoring
```

The model should not be deployed simply because training completed.

It must pass predefined evaluation criteria.

---

# 16.6 Why Do We Need MLflow?

MLflow provides:

```text
Experiment Tracking
       +
Artifact Management
       +
Model Registry
       +
Model Versioning
```

Example:

```text
Dataset V12
     ↓
Training Run 145
     ↓
Model V7
     ↓
Evaluation Report
     ↓
Production
```

This creates traceability across the ML lifecycle.

---

# 16.7 How Would You Deploy the ML Model?

The model is packaged into an application container.

```text
Model
 ↓
Inference Code
 ↓
Docker
 ↓
ACR
 ↓
AKS
```

The inference service should include:

- Input validation
- Model loading
- Prediction logic
- Output validation
- Health endpoints
- Logging
- Metrics
- Correlation/request ID

Example:

```text
API Request
     ↓
Input Validation
     ↓
Feature Processing
     ↓
Model
     ↓
Output Validation
     ↓
Response
```

---

# 16.8 Why Do We Need `inference.py`?

`inference.py` contains the production inference logic.

A simplified responsibility flow is:

```text
Request
 ↓
Validate Input
 ↓
Load / Access Model
 ↓
Preprocess
 ↓
Predict
 ↓
Validate Output
 ↓
Return Response
```

It should not contain hardcoded production secrets.

Configuration should come from controlled configuration mechanisms and identity-based access where applicable.

---

# 16.9 How Would You Design the RAG Architecture?

The RAG system has two major flows.

## Offline Ingestion

```text
Documents
    ↓
Parsing
    ↓
Chunking
    ↓
Metadata
    ↓
Embedding
    ↓
Qdrant
```

## Online Query

```text
User Question
      ↓
RAG API
      ↓
Embedding
      ↓
Qdrant
      ↓
Top-K Candidates
      ↓
Reranker
      ↓
Relevant Context
      ↓
Prompt
      ↓
LLM
      ↓
Response
```

---

# 16.10 How Would You Scale the Platform?

Scaling must happen at different layers.

## Application Layer

Use multiple Pod replicas.

```text
ML API
 ├── Pod 1
 ├── Pod 2
 └── Pod 3
```

Use **HPA** to adjust replicas based on appropriate metrics.

## AKS Node Layer

Add/remove nodes according to workload and capacity requirements.

## RAG Layer

Scale independently:

```text
RAG API
Qdrant
Reranker
LLM
```

This is important because each component has different resource requirements.

---

# 16.11 How Would You Handle High Availability?

Use multiple replicas for stateless services.

```text
ML API
 ├── Pod 1
 ├── Pod 2
 └── Pod 3
```

If one Pod fails:

```text
Pod 1 ✗
     ↓
Kubernetes
     ↓
Replacement Pod
```

Additional considerations:

- Multiple AKS nodes
- Pod anti-affinity where appropriate
- PDB
- HPA
- Highly available supporting services where required
- Application Gateway availability
- Backup and recovery strategy

---

# 16.12 How Would You Secure the Platform?

Use defense in depth.

```text
Internet
   ↓
Application Gateway
   ↓
WAF
   ↓
Private AKS / VNet
   ↓
NetworkPolicy
   ↓
Identity / RBAC
   ↓
Application
```

Azure security components include:

```text
Entra ID
Key Vault
Private Endpoints
Private DNS
NSGs
Managed / Workload Identity
Azure Policy
```

Application security includes:

```text
SAST
Dependency Scan
Secret Scan
Container Scan
SBOM
Image Signing
```

---

# 16.13 Why Use Private Endpoints?

Private Endpoints allow supported Azure services to be accessed through private IP connectivity from the VNet.

Example:

```text
AKS
 ↓
Private Network
 ↓
Private Endpoint
 ↓
ADLS / ACR / Key Vault / MySQL
```

This reduces reliance on public network paths for service connectivity.

Private Endpoint configuration must be accompanied by appropriate DNS and access controls.

---

# 16.14 How Would You Manage Secrets?

Never hardcode:

```text
Passwords
API Keys
Tokens
Certificates
```

Use:

```text
Azure Key Vault
      ↓
Identity
      ↓
Application
```

For workloads running on AKS, use appropriate **workload/managed identity** mechanisms.

---

# 16.15 How Would You Design CI/CD?

Application delivery:

```text
Developer
    ↓
Git
    ↓
Azure DevOps
    ↓
Unit Tests
    ↓
Integration Tests
    ↓
Security Tests
    ↓
Docker Build
    ↓
Container Scan
    ↓
SBOM
    ↓
Image Signing
    ↓
ACR
    ↓
Continuous Testing
    ↓
Staging
    ↓
Approval
    ↓
Production AKS
```

Infrastructure delivery is handled separately:

```text
Terraform
    ↓
Plan
    ↓
Review
    ↓
Apply
    ↓
Azure Infrastructure
```

---

# 16.16 How Would You Deploy a New Model Safely?

Use a controlled promotion process.

```text
Training
   ↓
Evaluation
   ↓
Model Registry
   ↓
Approval
   ↓
Staging
   ↓
Continuous Testing
   ↓
Canary
```

Example:

```text
Production Traffic

90% → Model V7
10% → Model V8
```

Monitor:

```text
Error Rate
Latency
Model Metrics
Prediction Distribution
Business Metrics
```

If the candidate meets the defined criteria:

```text
10%
 ↓
25%
 ↓
50%
 ↓
100%
```

If it fails:

```text
V8
 ↓
Rollback
 ↓
V7
```

---

# 16.17 How Would You Roll Back?

Rollback should be fast and predictable.

```text
Production
     ↓
New Version
     ↓
Problem
     ↓
Rollback
     ↓
Previous Validated Version
```

For ML:

```text
Model V8
   ↓
Rollback
   ↓
Model V7
```

For Kubernetes application deployment:

```bash
kubectl rollout history deployment/<deployment-name> -n <namespace>

kubectl rollout undo deployment/<deployment-name> -n <namespace>
```

Previous versions should remain available for operational recovery and auditability.

---

# 16.18 How Would You Monitor the Platform?

Monitoring should cover multiple layers.

```text
Infrastructure
      ↓
Application
      ↓
ML
      ↓
RAG / LLM
      ↓
Business
```

### Infrastructure

```text
CPU
Memory
Nodes
Pods
Restarts
```

### Application

```text
Request Rate
Error Rate
Latency
Availability
```

### ML

```text
Data Drift
Feature Drift
Prediction Distribution
Model Performance
Feature Freshness
Training-Serving Skew
```

### RAG

```text
Retrieval Quality
Groundedness
Answer Relevance
Latency
Token Usage
Cost
```

Tools:

```text
Prometheus
Grafana
Azure Monitor
Log Analytics
Application Insights
```

---

# 16.19 How Would You Design Observability?

Use:

```text
Metrics
Logs
Traces
```

Every request should have a correlation/request ID.

Example:

```text
Request ID
    ↓
Gateway
    ↓
Ingress
    ↓
API
    ↓
Model / RAG
    ↓
Dependencies
```

For an ML request:

```text
Request ID
 ↓
Dataset Version
 ↓
Feature Version
 ↓
Code Commit
 ↓
MLflow Run
 ↓
Model Version
 ↓
Image Digest
 ↓
AKS Revision
```

For RAG:

```text
Request ID
 ↓
Prompt Version
 ↓
RAG Config
 ↓
Embedding Version
 ↓
Retrieved Documents
 ↓
Reranker
 ↓
LLM Version
 ↓
Response
```

---

# 16.20 How Would You Handle Data Drift?

```text
Production Data
      ↓
Drift Detection
      ↓
Drift Alert
      ↓
Investigation
      ↓
Check Model Performance
      ↓
Check Business Impact
```

Drift should not automatically trigger retraining.

If retraining is justified:

```text
Retraining
    ↓
Evaluation
    ↓
Comparison
    ↓
Approval
    ↓
Deployment
```

---

# 16.21 How Would You Handle a Bad Dataset?

Use data validation before training.

Validation can include:

```text
Schema
Types
Nulls
Duplicates
Ranges
Allowed Categories
Business Rules
Row Count
```

Invalid records go to:

```text
Quarantine
```

rather than silently entering the training pipeline.

Validation rules should be version controlled.

---

# 16.22 How Would You Handle Disaster Recovery?

First define:

```text
RTO
RPO
```

### RTO

How quickly the service should be restored.

### RPO

How much data loss is acceptable according to the recovery objective.

Recovery must consider:

```text
Infrastructure
Data
Models
Container Images
Configuration
RAG Documents
Vector Indexes
Secrets / Identity Configuration
```

Example:

```text
Disaster
   ↓
Recover Infrastructure
   ↓
Restore Data
   ↓
Restore Model Artifacts
   ↓
Restore Application
   ↓
Restore RAG Components
   ↓
Validate
   ↓
Resume Service
```

Recovery procedures should be tested rather than existing only as documentation.

---

# 16.23 How Would You Control Cost?

Track cost by:

```text
Environment
Application
Team / Project
Resource Type
LLM Workload
```

Use resource tags and appropriate Azure cost-management capabilities.

For LLM workloads, monitor:

```text
Requests
Input Tokens
Output Tokens
Model Size
Compute
Retrieval Cost
Reranking Cost
```

Optimization should be based on measurements.

Example:

```text
Measure Cost
     ↓
Find Expensive Component
     ↓
Optimize
     ↓
Evaluate Quality
     ↓
Deploy
     ↓
Monitor
```

---

# 16.24 What Are the Main Trade-Offs?

A strong system-design answer should discuss trade-offs.

### Managed vs Self-Managed

Managed Azure services can reduce operational overhead.

Self-managed components can provide more control but increase operational responsibility.

### Real-Time vs Batch

Real-time:

```text
Low latency
Higher operational complexity
```

Batch:

```text
Higher throughput
Lower real-time requirements
```

### Canary vs Blue-Green

Canary:

```text
Gradual traffic exposure
Lower initial blast radius
```

Blue-Green:

```text
Fast traffic switching
Requires additional environment capacity
```

### Larger vs Smaller LLM

Larger model:

```text
Potentially higher capability
Higher compute/cost requirements
```

Smaller model:

```text
Lower resource requirements
May have different quality characteristics
```

The final choice should be based on measured requirements and evaluation.

---

# 16.25 How Would You Design for Failure?

Assume components will fail.

Examples:

```text
Pod Failure
Node Failure
Database Failure
Qdrant Failure
Network Failure
DNS Failure
Identity Failure
Secret Expiration
Deployment Failure
Model Regression
Data Pipeline Failure
```

For every critical component ask:

```text
How do we detect failure?
        ↓
How do we mitigate it?
        ↓
How do we recover?
        ↓
How do we prevent recurrence?
```

---

# 16.26 Complete System Design Answer

### Interview Answer

> I would design the platform in separate data, ML, application, GenAI, infrastructure, security, and observability layers. Data would be ingested through Azure Data Factory into ADLS Gen2, validated, and processed before feature engineering and model training. Feast would provide feature management, while MLflow would handle experiment tracking and model registry. After evaluation and approval, the model would be packaged into a Docker image, stored in ACR, and deployed to AKS through Azure DevOps.
>
> For the GenAI workload, documents would be processed into chunks, embedded using BGE-small-en-v1.5, and stored in Qdrant. User queries would retrieve relevant candidates, pass through BGE-reranker-base, and then provide context to an LLM such as Llama 3.1 8B or Mistral 7B. Prompt and RAG configuration versions would be tracked for reproducibility.
>
> For security, I would use a private VNet architecture with NSGs, Kubernetes NetworkPolicy, Private Endpoints, Private DNS, Entra ID, workload identity, and Key Vault. Application Gateway and WAF would provide the external application entry point.
>
> CI/CD would include unit, integration, security, container, model, RAG, and performance testing before production deployment. Model deployments could use canary or blue-green strategies with predefined rollback criteria.
>
> Observability would cover infrastructure, application, ML, RAG, and business metrics using Prometheus, Grafana, Azure Monitor, Log Analytics, and Application Insights. I would also maintain request-level lineage so we can trace a prediction or RAG response back to its model, data, code, container, and configuration versions.
>
> Finally, I would design for high availability, disaster recovery, defined RTO/RPO, SLOs, cost monitoring, and production incident response. The important principle is that the platform should not only deploy models but also safely operate, monitor, troubleshoot, and recover them in production.

---

# 16.27 System Design Interview Checklist

Before finishing the answer, verify that you covered:

```text
✓ Requirements
✓ Architecture
✓ Data
✓ ML lifecycle
✓ Model registry
✓ Model serving
✓ RAG
✓ Kubernetes
✓ CI/CD
✓ Security
✓ Networking
✓ Identity
✓ Monitoring
✓ Scaling
✓ High availability
✓ Deployment strategy
✓ Rollback
✓ Data drift
✓ RAG evaluation
✓ Disaster recovery
✓ RTO / RPO
✓ SLO
✓ Cost
✓ Trade-offs
✓ Failure handling
```

---

# 16.28 Final System Design Principle

A production ML/GenAI platform is not simply:

```text
Train Model
     ↓
Deploy Model
```

It is:

```text
Data
 ↓
Validation
 ↓
Features
 ↓
Training
 ↓
Evaluation
 ↓
Governance
 ↓
Deployment
 ↓
Inference
 ↓
Monitoring
 ↓
Drift / Quality Detection
 ↓
Incident Response
 ↓
Rollback / Recovery
 ↓
Retraining
 ↓
Continuous Improvement
```

The same production mindset applies to the RAG workload:

```text
Documents
 ↓
Ingestion
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retrieval
 ↓
Reranking
 ↓
LLM
 ↓
Evaluation
 ↓
Monitoring
 ↓
Security
 ↓
Continuous Improvement
```

# 17. Final Interview Cheat Sheet

This section is for **last-minute interview revision**.

The goal is to quickly remember:

```text
Concept
→ Purpose
→ Architecture
→ Command
→ Troubleshooting
```

---

# 17.1 MLOps — One-Line Answers

| Question | Short Answer |
|---|---|
| What is MLOps? | DevOps practices applied to the ML lifecycle. |
| Why MLOps? | To reliably build, deploy, monitor, govern, and retrain ML systems. |
| What is MLflow? | Experiment tracking, artifact management, and model lifecycle management. |
| What is Model Registry? | Centralized management of model versions and lifecycle. |
| What is Data Drift? | Change in production data distribution compared with reference/training data. |
| Does drift mean retraining? | No. Drift is a signal that requires investigation. |
| What is Feature Store? | Centralized management and serving of ML features. |
| What is Training-Serving Skew? | Difference between feature generation during training and production serving. |
| What is Batch Inference? | Generating predictions for many records periodically or on demand. |
| What is Real-Time Inference? | Generating a prediction in response to an API request. |
| What is SHAP? | A method for explaining feature contributions to model predictions. |
| Why model versioning? | Reproducibility, traceability, deployment, comparison, and rollback. |

---

# 17.2 ML Lifecycle

Remember:

```text
Data
 ↓
Validation
 ↓
Feature Engineering
 ↓
Feature Store
 ↓
Training
 ↓
Experiment Tracking
 ↓
Evaluation
 ↓
Model Registry
 ↓
Deployment
 ↓
Inference
 ↓
Monitoring
 ↓
Drift
 ↓
Retraining
```

---

# 17.3 MLflow Flow

```text
Training Run
     ↓
Parameters
     ↓
Metrics
     ↓
Artifacts
     ↓
Model
     ↓
MLflow Registry
     ↓
Model Version
     ↓
Approval
     ↓
Deployment
```

---

# 17.4 Model Deployment

```text
Model
 ↓
Evaluation
 ↓
Registry
 ↓
Docker
 ↓
ACR
 ↓
AKS
 ↓
Staging
 ↓
Continuous Testing
 ↓
Canary / Blue-Green / Rolling
 ↓
Production
```

---

# 17.5 Model Rollback

```text
V8
 ↓
Production Problem
 ↓
Investigate
 ↓
Rollback
 ↓
V7
 ↓
Verify
```

Remember:

> Never delete the previous validated model simply because a new model was promoted.

---

# 17.6 Azure — One-Line Answers

| Question | Short Answer |
|---|---|
| ADLS Gen2 | Scalable data lake storage for analytical and ML data. |
| ADF | Data ingestion and data workflow orchestration. |
| MySQL Flexible Server | Managed MySQL database for operational/transactional workloads. |
| ACR | Private registry for container images. |
| AKS | Managed Kubernetes service. |
| Key Vault | Secure management of secrets, keys, and certificates. |
| VNet | Private network boundary for Azure resources. |
| NSG | Controls network traffic using security rules. |
| Private Endpoint | Private IP-based connectivity to supported Azure services. |
| Private DNS | Resolves private service names to private IP addresses. |
| Application Gateway | Layer 7 application traffic gateway. |
| WAF | Web application security layer. |
| Entra ID | Identity and access management service. |
| Managed Identity | Azure-managed identity for resource authentication. |
| Azure Monitor | Azure-native monitoring and observability platform. |

---

# 17.7 Azure Architecture

```text
                    Azure
                      │
       ┌──────────────┼───────────────┐
       │              │               │
       ▼              ▼               ▼
     Data            Compute        Security
       │              │               │
     ADLS            AKS          Key Vault
     ADF             ACR          Entra ID
     MySQL                         Private Endpoint
                                   Private DNS
```

---

# 17.8 ADF vs ML Workflow vs CI/CD

Remember this:

```text
ADF
→ Data

ML Workflow
→ Machine Learning

Azure DevOps
→ Software Delivery
```

Detailed:

```text
ADF
Source → Raw → Processed

ML Workflow
Data → Features → Training → Evaluation

Azure DevOps
Code → Test → Build → Package → Deploy
```

---

# 17.9 Private Endpoint vs Service Endpoint

```text
Private Endpoint
→ Private IP connectivity

Service Endpoint
→ VNet-based access to the service endpoint
```

Interview phrase:

> Private Endpoint provides private IP connectivity, while Service Endpoint extends VNet identity to an Azure service over the Azure backbone.

---

# 17.10 Managed Identity

Remember:

```text
Application
 ↓
Managed / Workload Identity
 ↓
Entra ID
 ↓
Azure Resource
```

Main advantage:

> Avoid storing long-lived credentials in application code.

---

# 17.11 Kubernetes — One-Line Answers

| Question | Short Answer |
|---|---|
| Pod | Smallest deployable Kubernetes unit. |
| Deployment | Manages stateless application Pods and rollout history. |
| Service | Stable network endpoint for Pods. |
| Ingress | HTTP/HTTPS routing to Kubernetes Services. |
| HPA | Automatically adjusts Pod replicas based on configured metrics. |
| PDB | Helps maintain availability during voluntary disruptions. |
| ConfigMap | Stores non-sensitive configuration. |
| Secret | Stores sensitive configuration data in Kubernetes, subject to appropriate security controls. |
| NetworkPolicy | Controls allowed network communication between workloads. |
| DaemonSet | Runs a Pod on each eligible node according to its scheduling rules. |
| StatefulSet | Manages stateful workloads with stable identities and storage characteristics. |
| kubelet | Node agent responsible for managing Pods on a node. |
| kube-proxy | Helps implement Kubernetes Service networking. |
| etcd | Distributed key-value store containing Kubernetes cluster state. |

---

# 17.12 Kubernetes Traffic Flow

```text
User
 ↓
Application Gateway
 ↓
WAF
 ↓
Ingress
 ↓
Service
 ↓
Pod
 ↓
Application
```

---

# 17.13 Kubernetes Scaling

```text
Traffic
 ↓
Metrics
 ↓
HPA
 ↓
More Pods
```

If cluster capacity is insufficient:

```text
Pod Scheduling Demand
 ↓
Node Capacity
 ↓
Cluster Scaling Mechanism
 ↓
Additional Node Capacity
```

---

# 17.14 Kubernetes Troubleshooting Commands

### Check Pods

```bash
kubectl get pods -n <namespace>
```

### Detailed Pod Information

```bash
kubectl describe pod <pod-name> -n <namespace>
```

### Logs

```bash
kubectl logs <pod-name> -n <namespace>
```

### Previous Container Logs

```bash
kubectl logs <pod-name> -n <namespace> --previous
```

### Services

```bash
kubectl get svc -n <namespace>
```

### Endpoints

```bash
kubectl get endpoints -n <namespace>
```

### Ingress

```bash
kubectl get ingress -n <namespace>
```

### Events

```bash
kubectl get events -n <namespace> --sort-by=.lastTimestamp
```

### Deployment History

```bash
kubectl rollout history deployment/<deployment-name> -n <namespace>
```

### Rollback

```bash
kubectl rollout undo deployment/<deployment-name> -n <namespace>
```

---

# 17.15 CrashLoopBackOff Quick Flow

```text
CrashLoopBackOff
 ↓
kubectl describe pod
 ↓
kubectl logs
 ↓
kubectl logs --previous
 ↓
Events
 ↓
Config
 ↓
Secrets
 ↓
Probes
 ↓
Resources
 ↓
Dependencies
```

---

# 17.16 502 Quick Flow

```text
502
 ↓
Application Gateway
 ↓
Ingress
 ↓
Service
 ↓
Endpoints
 ↓
Pod Ready?
 ↓
Target Port
 ↓
Application
 ↓
NetworkPolicy
```

---

# 17.17 DNS Troubleshooting

```text
Hostname
 ↓
DNS Resolution
 ↓
Expected Private IP?
 ↓
Private DNS Zone
 ↓
DNS Link
 ↓
Private Endpoint
 ↓
Network
 ↓
Authentication
```

Useful command:

```bash
nslookup <hostname>
```

---

# 17.18 DevOps — One-Line Answers

| Question | Short Answer |
|---|---|
| CI | Automatically validates code changes. |
| CD | Delivers validated artifacts to environments. |
| Continuous Testing | Testing continuously throughout the delivery lifecycle. |
| Docker | Packages application and dependencies into a container image. |
| ACR | Stores container images. |
| Terraform | Infrastructure as Code tool. |
| Terraform State | Tracks infrastructure managed by Terraform. |
| Terraform Drift | Difference between expected and actual infrastructure state. |
| Terraform Module | Reusable Terraform configuration. |
| `count` | Repeats resources using indexes. |
| `for_each` | Repeats resources using collection keys. |
| Git Merge | Combines branch histories. |
| Git Rebase | Replays commits onto a new base and rewrites history. |
| Cherry-pick | Applies a specific commit to another branch. |
| SBOM | Inventory of software components in an artifact. |

---

# 17.19 CI/CD Flow

```text
Git
 ↓
CI
 ↓
Unit Tests
 ↓
Integration Tests
 ↓
SAST
 ↓
Dependency Scan
 ↓
Secret Scan
 ↓
Docker Build
 ↓
Container Scan
 ↓
SBOM
 ↓
Image Signing
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

---

# 17.20 Terraform Flow

```text
Terraform Code
 ↓
terraform init
 ↓
terraform validate
 ↓
terraform plan
 ↓
Review
 ↓
terraform apply
 ↓
Azure
```

---

# 17.21 RAG — One-Line Answers

| Question | Short Answer |
|---|---|
| RAG | Retrieval-Augmented Generation. |
| Embedding | Numerical representation of text used for semantic comparison/search. |
| Chunking | Splitting documents into smaller pieces. |
| Vector DB | Stores vectors and associated metadata/content references for similarity search. |
| Qdrant | Vector database used in our RAG platform. |
| Top-K | Number of highest-ranked retrieval candidates returned. |
| Reranker | Re-scores retrieved candidates for better relevance ordering. |
| LangChain | Framework for orchestrating LLM application components. |
| Hallucination | Unsupported or incorrect generated information. |
| Groundedness | Whether an answer is supported by the available context/evidence. |
| Prompt Injection | Attempt to manipulate LLM behavior through untrusted input. |
| Prompt Versioning | Tracking different versions of prompts used by the application. |

---

# 17.22 RAG Architecture

```text
Documents
 ↓
Parsing
 ↓
Chunking
 ↓
Metadata
 ↓
Embeddings
 ↓
Qdrant
```

Query:

```text
User Question
 ↓
Embedding
 ↓
Qdrant
 ↓
Top-K
 ↓
Reranker
 ↓
Relevant Context
 ↓
Prompt
 ↓
LLM
 ↓
Response
```

---

# 17.23 RAG Troubleshooting

```text
Wrong Answer
 ↓
Check Source Document
 ↓
Check Chunking
 ↓
Check Embedding
 ↓
Check Qdrant
 ↓
Check Retrieval
 ↓
Check Reranker
 ↓
Check Prompt
 ↓
Check LLM
```

Do not immediately blame the LLM.

---

# 17.24 RAG Evaluation

Evaluate:

```text
Retrieval Quality
      +
Context Relevance
      +
Groundedness
      +
Answer Relevance
      +
Safety
      +
Latency
      +
Cost
```

---

# 17.25 Production Monitoring

Remember five layers:

```text
1. Infrastructure
2. Application
3. Data / ML
4. RAG / LLM
5. Business
```

### Infrastructure

```text
CPU
Memory
Nodes
Pods
Restarts
```

### Application

```text
Requests
Errors
Latency
Availability
```

### ML

```text
Drift
Feature Freshness
Prediction Distribution
Model Performance
Training-Serving Skew
```

### RAG / LLM

```text
Retrieval Quality
Groundedness
Answer Quality
LLM Latency
Token Usage
Cost
```

---

# 17.26 Important Latency Metrics

```text
p50
 ↓
Median latency

p95
 ↓
95% of requests are at or below this latency

p99
 ↓
99% of requests are at or below this latency
```

Production systems should not rely only on average latency.

---

# 17.27 SLI vs SLO vs SLA

### SLI

**Service Level Indicator**

The measured value.

Example:

```text
Request success rate = 99.95%
```

### SLO

**Service Level Objective**

The target.

Example:

```text
99.9% successful requests
```

### SLA

**Service Level Agreement**

A formal agreement with defined service commitments.

Simple:

```text
SLI → What we measure
SLO → What we target
SLA → What we commit to contractually
```

---

# 17.28 RTO vs RPO

### RTO

**Recovery Time Objective**

How quickly the service should be restored.

### RPO

**Recovery Point Objective**

How much data loss is acceptable according to the recovery objective.

Remember:

```text
RTO → Time
RPO → Data
```

---

# 17.29 Security Quick Revision

```text
Entra ID
   ↓
Identity

Key Vault
   ↓
Secrets / Certificates / Keys

Private Endpoint
   ↓
Private Connectivity

NSG
   ↓
Network Access Control

NetworkPolicy
   ↓
Pod-to-Pod Access Control

Azure Policy
   ↓
Governance

SAST
   ↓
Source Security

Container Scan
   ↓
Image Security

SBOM
   ↓
Software Inventory

Image Signing
   ↓
Artifact Integrity / Provenance Verification
```

---

# 17.30 Production Incident Golden Pattern

For almost every incident:

```text
Detect
 ↓
Confirm
 ↓
Assess Impact
 ↓
Check Recent Changes
 ↓
Collect Evidence
 ↓
Mitigate
 ↓
Find Root Cause
 ↓
Fix
 ↓
Verify
 ↓
Prevent Recurrence
```

---

# 17.31 The Most Important Interview Sentence

When you don't know the root cause immediately, say:

> "I would not assume the root cause initially. I would first collect evidence and isolate the problem layer by layer."

Then:

```text
Application
 ↓
Dependency
 ↓
Network
 ↓
Identity
 ↓
Infrastructure
```

This demonstrates a **production troubleshooting mindset**.

---

# 17.32 Final Architecture to Remember

```text
                         USER
                           │
                           ▼
                Application Gateway
                       + WAF
                           │
                           ▼
                     AKS Ingress
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
           ML API                    RAG API
              │                         │
              ▼                         ▼
          ML Model                  Qdrant
                                      │
                                      ▼
                                   Reranker
                                      │
                                      ▼
                                     LLM


DATA FLOW

Sources
   ↓
ADF
   ↓
ADLS Gen2
   ↓
Validation
   ↓
Feature Engineering
   ↓
Feast
   ↓
Training
   ↓
MLflow
   ↓
Model Registry
   ↓
Evaluation
   ↓
Deployment
   ↓
AKS


DEVOPS

Git
 ↓
Azure DevOps
 ↓
CI
 ↓
Security
 ↓
Docker
 ↓
ACR
 ↓
Continuous Testing
 ↓
Staging
 ↓
Production


SECURITY

Entra ID
Key Vault
Private Endpoint
Private DNS
NSG
NetworkPolicy
Azure Policy


OBSERVABILITY

Prometheus
Grafana
Azure Monitor
Log Analytics
Application Insights
```

---

# 17.33 Final Project Story

If the interviewer asks:

> "Tell me about your MLOps project."

Remember this sequence:

```text
Business Problem
      ↓
Data Platform
      ↓
ML Lifecycle
      ↓
Model Deployment
      ↓
AKS
      ↓
CI/CD
      ↓
Monitoring
      ↓
Drift
      ↓
Retraining
      ↓
RAG / LLM
      ↓
Security
      ↓
Governance
      ↓
Incident Management
      ↓
DR / Reliability
```

The strongest project explanation connects every technology to a **business or production requirement**.

---

# 17.34 Final Interview Mindset

Do not try to memorize every command.

Understand:

```text
WHY
 ↓
WHAT
 ↓
HOW
 ↓
FAILURE
 ↓
TROUBLESHOOTING
 ↓
RECOVERY
```

A production-grade MLOps engineer should be able to explain:

```text
How to build it
How to deploy it
How to secure it
How to monitor it
How to scale it
How to troubleshoot it
How to roll it back
How to recover it
Why each design decision was made
```

This is the foundation for the interview discussions in this project.