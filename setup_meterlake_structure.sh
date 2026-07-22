#!/usr/bin/env bash
set -euo pipefail

echo "Creating professional MeterLake project structure..."

# -----------------------------
# Resource YAML directories
# -----------------------------
mkdir -p resources/jobs
mkdir -p resources/pipelines

touch resources/jobs/bronze_ingestion.job.yml
touch resources/jobs/gold_refresh.job.yml
touch resources/jobs/quality_checks.job.yml

touch resources/pipelines/silver_transformations.pipeline.yml

# -----------------------------
# Source package directories
# -----------------------------
mkdir -p src/meterlake/common
mkdir -p src/meterlake/bronze
mkdir -p src/meterlake/silver
mkdir -p src/meterlake/gold
mkdir -p src/meterlake/ops

# Python package markers
touch src/meterlake/__init__.py
touch src/meterlake/common/__init__.py
touch src/meterlake/bronze/__init__.py
touch src/meterlake/silver/__init__.py
touch src/meterlake/gold/__init__.py
touch src/meterlake/ops/__init__.py

# Common utilities
touch src/meterlake/common/config.py
touch src/meterlake/common/paths.py
touch src/meterlake/common/schemas.py
touch src/meterlake/common/quality_rules.py
touch src/meterlake/common/logging.py

# Bronze ingestion modules
touch src/meterlake/bronze/ingest_usage_events.py
touch src/meterlake/bronze/ingest_billing_events.py
touch src/meterlake/bronze/ingest_customers.py
touch src/meterlake/bronze/ingest_pricing_plans.py
touch src/meterlake/bronze/ingest_plan_changes.py
touch src/meterlake/bronze/ingest_invoice_line_items.py
touch src/meterlake/bronze/ingest_customer_subscriptions.py
touch src/meterlake/bronze/ingest_commercial_adjustments.py

# Silver transformation modules
touch src/meterlake/silver/usage_events_clean.py
touch src/meterlake/silver/billing_events_clean.py
touch src/meterlake/silver/customers_clean.py
touch src/meterlake/silver/pricing_plans_clean.py
touch src/meterlake/silver/plan_changes_clean.py
touch src/meterlake/silver/invoice_line_items_clean.py
touch src/meterlake/silver/customer_subscriptions_clean.py
touch src/meterlake/silver/commercial_adjustments_clean.py

# Gold analytics modules
touch src/meterlake/gold/account_usage_daily.py
touch src/meterlake/gold/customer_revenue_daily.py
touch src/meterlake/gold/invoice_revenue_summary.py
touch src/meterlake/gold/product_usage_metrics.py
touch src/meterlake/gold/mrr_movements.py

# Ops modules
touch src/meterlake/ops/audit_log.py
touch src/meterlake/ops/quarantine_report.py
touch src/meterlake/ops/pipeline_health.py
touch src/meterlake/ops/reprocess_quarantine.py

# -----------------------------
# Tests
# -----------------------------
mkdir -p tests

touch tests/conftest.py
touch tests/test_bronze_validation.py
touch tests/test_silver_dedup.py
touch tests/test_quality_rules.py
touch tests/test_path_config.py
touch tests/test_gold_metrics.py

# -----------------------------
# Fixtures / sample data
# -----------------------------
mkdir -p fixtures/usage_events
mkdir -p fixtures/billing_events
mkdir -p fixtures/customers
mkdir -p fixtures/pricing_plans
mkdir -p fixtures/plan_changes
mkdir -p fixtures/invoice_line_items
mkdir -p fixtures/customer_subscriptions
mkdir -p fixtures/commercial_adjustments
mkdir -p fixtures/malformed_records

touch fixtures/usage_events/.gitkeep
touch fixtures/billing_events/.gitkeep
touch fixtures/customers/.gitkeep
touch fixtures/pricing_plans/.gitkeep
touch fixtures/plan_changes/.gitkeep
touch fixtures/invoice_line_items/.gitkeep
touch fixtures/customer_subscriptions/.gitkeep
touch fixtures/commercial_adjustments/.gitkeep
touch fixtures/malformed_records/.gitkeep

# -----------------------------
# Docs
# -----------------------------
mkdir -p docs

touch docs/architecture.md
touch docs/data_contracts.md
touch docs/orchestration.md
touch docs/operations_runbook.md
touch docs/data_quality.md

# -----------------------------
# Optional: notebooks for exploration only
# -----------------------------
mkdir -p notebooks/exploration
touch notebooks/exploration/.gitkeep

# -----------------------------
# Add placeholder README if missing
# -----------------------------
if [ ! -f README.md ]; then
  cat > README.md <<'README'
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
README
fi

echo
echo "Done. Current structure:"
find . \
  -path './.git' -prune -o \
  -path './.venv' -prune -o \
  -path './.databricks' -prune -o \
  -maxdepth 4 \
  -print | sort
