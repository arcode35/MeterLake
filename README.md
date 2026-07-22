# MeterLake

Production-style Databricks lakehouse project for SaaS metering, billing, and usage analytics.

## Architecture

Raw files land in Unity Catalog external volumes, Bronze ingestion captures source fidelity, Silver transformations clean and conform entities, and Gold tables serve analytics-ready billing and usage metrics.

## Stack

- Azure Databricks
- Unity Catalog
- Delta Lake
- Auto Loader
- Lakeflow Declarative Pipelines
- Databricks Asset Bundles
- PySpark
- pytest
