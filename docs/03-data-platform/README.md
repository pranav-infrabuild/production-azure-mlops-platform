# Data Platform

This section defines the data platform used by the Production Azure MLOps Platform.

The goal is to build a production-oriented data flow that is reliable, validated, versioned, traceable, and ready for machine learning.

## Data Platform Architecture

```text
Source Data
    |
    v
Azure Data Factory
    |
    v
ADLS Gen2 - Raw
    |
    v
Data Validation
    |
    +---- Invalid ----> Quarantine
    |
    v
ADLS Gen2 - Processed
    |
    v
Delta Lake
    |
    v
Feature Engineering
    |
    v
Feature Store
    |
    v
ML Training / Inference


## Core Components

### Azure Data Factory

Azure Data Factory is used for:

* Data ingestion
* Pipeline orchestration
* Scheduling
* Parameterized data movement
* Pipeline monitoring
* Failure handling and retry
* Triggering downstream processing

ADF is responsible for **data orchestration**.

It is different from:

* Azure DevOps CI/CD
* ML training workflow orchestration

### ADLS Gen2

Azure Data Lake Storage Gen2 is the primary storage layer.

The data lake is organized into logical zones:

```text
ADLS Gen2
├── raw/
├── processed/
├── quarantine/
└── curated/
```

### Delta Lake

Delta Lake provides a reliable table layer over the data lake.

It will be used for:

* ACID transactions
* Schema enforcement
* Schema evolution
* Time travel
* Data versioning
* Reliable ML datasets

## Data Validation

Before data is used for machine learning, it must pass validation.

Validation includes:

* Schema validation
* Data type validation
* Null checks
* Duplicate checks
* Range validation
* Allowed category validation
* Row count validation
* Business rule validation

Invalid records are moved to the **quarantine** area instead of being silently accepted.

Validation rules will be stored in version-controlled YAML files.

## Data Versioning

Every important ML dataset should be traceable to a specific version.

Example:

```text
Dataset V12
    |
    v
Training Run 145
    |
    v
Model V7
    |
    v
Docker Image V7
    |
    v
AKS Production
```

This allows us to understand exactly which data produced a production model.

## Data Lineage

The platform maintains lineage across the ML lifecycle.

Example:

```text
Request ID
    |
Dataset Version
    |
Feature Version
    |
Code Commit
    |
MLflow Run
    |
Model Version
    |
Container Image
    |
AKS Deployment Revision
```

## Data Quality and Monitoring

The platform monitors:

* Missing values
* Duplicate records
* Invalid records
* Schema changes
* Data volume
* Data distribution
* Feature freshness
* Data drift

Data quality failures should prevent bad data from silently reaching model training or production inference.

## Production Incident Scenarios

The project will demonstrate real-world data incidents including:

1. Data validation failure
2. Schema change
3. Duplicate data
4. Missing data
5. Invalid business values
6. Data drift
7. Feature freshness failure
8. ADF pipeline failure
9. ADF retry and recovery

## Design Principle

The data platform follows:

**Ingest → Validate → Quarantine → Process → Version → Feature → Monitor → Trace**

The objective is not only to move data, but to make every important dataset **reliable, reproducible, observable, and traceable**.




# ADLS Gen2 Data Lake Design

## Purpose

Azure Data Lake Storage Gen2 is the central storage layer for the platform.

It stores incoming data, validated data, quarantined records, and curated datasets used by machine learning workflows.

## Data Lake Structure

```text
ADLS Gen2
│
├── raw/
│   └── customer-churn/
│
├── processed/
│   └── customer-churn/
│
├── quarantine/
│   └── customer-churn/
│
└── curated/
    └── customer-churn/
```

## 1. Raw Zone

The Raw zone contains data exactly as received from the source.

Example:

```text
raw/customer-churn/2026/09/18/batch-001/
```

Characteristics:

* Original source data
* Minimal transformation
* Immutable where possible
* Used for replay and investigation
* Retained according to the data retention policy

The Raw zone allows us to reproduce downstream processing if a problem occurs.

## 2. Processed Zone

The Processed zone contains data that has passed validation and basic transformations.

Example:

```text
processed/customer-churn/2026/09/18/batch-001/
```

Typical processing includes:

* Data type normalization
* Column standardization
* Duplicate handling
* Required transformations
* Data quality checks

Only validated records should move into this zone.

## 3. Quarantine Zone

The Quarantine zone contains records that failed validation.

Example:

```text
quarantine/customer-churn/2026/09/18/batch-001/
```

Examples of failures:

* Invalid data type
* Missing required field
* Invalid category
* Out-of-range value
* Duplicate record
* Business rule violation

Quarantined data should not be used for ML training or production inference until the issue is investigated and resolved.

## 4. Curated Zone

The Curated zone contains data prepared specifically for downstream ML and analytical workloads.

Example:

```text
curated/customer-churn/features/2026/09/18/
```

It may contain:

* Feature-ready datasets
* Aggregated datasets
* ML training datasets
* ML evaluation datasets

## Data Flow

```text
Source
  |
  v
ADF
  |
  v
Raw
  |
  v
Validation
  |
  +------------------+
  |                  |
Valid              Invalid
  |                  |
  v                  v
Processed        Quarantine
  |
  v
Curated
  |
  v
Feature Engineering
  |
  v
Feature Store
```

## Why We Separate the Zones

Separating the zones gives us:

### Reproducibility

We can reproduce processing from the original Raw data.

### Data Quality

Invalid records are prevented from silently entering ML workflows.

### Traceability

We can identify which source batch produced a processed dataset.

### Recovery

If a downstream pipeline fails, we can replay processing without requesting the source data again.

### Security

Different zones can have different access permissions.

For example:

```text
Raw        → restricted write/read access
Processed  → processing services
Quarantine → data engineering/operations
Curated    → ML and analytics workloads
```

## Batch Identification

Every ingestion batch should have a unique identifier.

Example:

```text
batch-20260918-001
```

Useful metadata includes:

* Batch ID
* Source
* Ingestion timestamp
* File name
* Record count
* Validation status
* Schema version
* Pipeline run ID

## Example Lineage

```text
Source File
    |
    v
Batch: 20260918-001
    |
    v
Raw Dataset
    |
    v
Validation Run
    |
    v
Processed Dataset
    |
    v
Curated Dataset
    |
    v
Training Dataset
    |
    v
MLflow Training Run
```

## Design Principle

The data lake should make it possible to answer:

> Where did this data come from?

> Which validation rules were applied?

> Which records failed?

> Which dataset version was used for training?

> Which model was created from that dataset?

This is the foundation for production-grade **data lineage and ML reproducibility**.

```

