from typing import Final

from pyspark.sql.types import (
    BooleanType,
    DateType,
    DecimalType,
    IntegerType,
    LongType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)


STRING = StringType()
BOOLEAN = BooleanType()
INTEGER = IntegerType()
LONG = LongType()
DATE = DateType()
TIMESTAMP = TimestampType()

# This configuration retains precision for gold billing calculations. 
# Round only when producing invoice facing or reporting outputs.
MONEY = DecimalType(20, 6)
RATE = DecimalType(20, 8)
QUANTITY = DecimalType(20, 6)
PERCENTAGE = DecimalType(9, 6)
SCORE = DecimalType(9, 4)


def _audit_fields() -> list[StructField]:
    return [
        StructField("_ingestion_timestamp", TIMESTAMP, True),
        StructField("_source_feed", STRING, True),
        StructField("_source_file_path", STRING, True),
        StructField("_source_file_name", STRING, True),
        StructField("_source_file_size", LONG, True),
        StructField(
            "_source_file_modification_time",
            TIMESTAMP,
            True,
        ),
        StructField("_silver_processed_at", TIMESTAMP, True),
    ]


PLAN_CHANGES_SILVER_SCHEMA: Final[StructType] = StructType([
    StructField("billing_frequency", STRING, True),
    StructField("change_type", STRING, True),
    StructField("customer_id", STRING, True),
    StructField("effective_end", TIMESTAMP, True),
    StructField("effective_start", TIMESTAMP, True),
    StructField("plan_code", STRING, True),
    StructField("plan_version", INTEGER, True),
    StructField("previous_plan_code", STRING, True),
    StructField("seats", INTEGER, True),
    StructField("source_system", STRING, True),
    StructField("status", STRING, True),
    StructField("subscription_id", STRING, True),
    StructField("updated_at", TIMESTAMP, True),
    *_audit_fields(),
])


PRICING_PLANS_SILVER_SCHEMA: Final[StructType] = StructType([
    StructField("additional_seat_monthly_fee", MONEY, True),
    StructField("base_monthly_fee", MONEY, True),
    StructField("currency", STRING, True),
    StructField("effective_end", TIMESTAMP, True),
    StructField("effective_start", TIMESTAMP, True),
    StructField("included_seats", INTEGER, True),
    StructField(
        "included_usage",
        StructType([
            StructField("api_calls", LONG, True),
            StructField("exports", LONG, True),
            StructField("minutes", QUANTITY, True),
            StructField("seats", LONG, True),
            StructField("storage_gb", QUANTITY, True),
            StructField("tokens", LONG, True),
        ]),
        True,
    ),
    StructField(
        "overage_rates",
        StructType([
            StructField("api_calls", RATE, True),
            StructField("exports", RATE, True),
            StructField("minutes", RATE, True),
            StructField("seats", RATE, True),
            StructField("storage_gb", RATE, True),
            StructField("tokens", RATE, True),
        ]),
        True,
    ),
    StructField("plan_code", STRING, True),
    StructField("plan_version", INTEGER, True),
    StructField("source_system", STRING, True),
    StructField("support_tier", STRING, True),
    *_audit_fields(),
])


CUSTOMERS_SILVER_SCHEMA: Final[StructType] = StructType([
    StructField("account_id", STRING, True),
    StructField("account_owner", STRING, True),
    StructField("billing_email", STRING, True),
    StructField("company_name", STRING, True),
    StructField("created_at", TIMESTAMP, True),
    StructField("crm_source", STRING, True),
    StructField("customer_health_score", SCORE, True),
    StructField("customer_id", STRING, True),
    StructField("industry", STRING, True),
    StructField("payment_terms_days", INTEGER, True),
    StructField("region", STRING, True),
    StructField("risk_score", SCORE, True),
    StructField("segment", STRING, True),
    StructField("status", STRING, True),
    StructField("tax_exempt", BOOLEAN, True),
    StructField("updated_at", TIMESTAMP, True),
    *_audit_fields(),
])


INVOICE_LINE_ITEMS_SILVER_SCHEMA: Final[StructType] = StructType([
    StructField("amount", MONEY, True),
    StructField("billing_period_end", DATE, True),
    StructField("billing_period_start", DATE, True),
    StructField("billing_rule_version", STRING, True),
    StructField("billing_system", STRING, True),
    StructField("charge_type", STRING, True),
    StructField("commercial_adjustment_id", STRING, True),
    StructField("created_at", TIMESTAMP, True),
    StructField("currency", STRING, True),
    StructField("customer_id", STRING, True),
    StructField("description", STRING, True),
    StructField("expected_amount", MONEY, True),
    StructField("invoice_actual_total", MONEY, True),
    StructField("invoice_date", DATE, True),
    StructField("invoice_expected_total", MONEY, True),
    StructField("invoice_id", STRING, True),
    StructField("line_item_id", STRING, True),
    StructField("plan_code", STRING, True),
    StructField("plan_version", INTEGER, True),
    StructField("quantity", QUANTITY, True),
    StructField("subscription_id", STRING, True),
    StructField("unit", STRING, True),
    StructField("unit_price", RATE, True),
    *_audit_fields(),
])


USAGE_EVENTS_SILVER_SCHEMA: Final[StructType] = StructType([
    StructField("account_id", STRING, True),
    StructField("customer_id", STRING, True),
    StructField("event_id", STRING, True),
    StructField("event_timestamp", TIMESTAMP, True),
    StructField("event_date", DATE, True),
    StructField("idempotency_key", STRING, True),
    StructField("ingest_batch_id", STRING, True),
    StructField(
        "metadata",
        StructType([
            StructField("ip_country", STRING, True),
            StructField("sdk", STRING, True),
        ]),
        True,
    ),
    StructField("metering_version", STRING, True),
    StructField("plan_code", STRING, True),
    StructField("plan_version", INTEGER, True),
    StructField("product_area", STRING, True),
    StructField("quantity", QUANTITY, True),
    StructField("received_at", TIMESTAMP, True),
    StructField("region", STRING, True),
    StructField("request_id", STRING, True),
    StructField("source", STRING, True),
    StructField("source_app_version", STRING, True),
    StructField("subscription_id", STRING, True),
    StructField("unit", STRING, True),
    StructField("workspace_id", STRING, True),
    *_audit_fields(),
])


COMMERCIAL_ADJUSTMENTS_SILVER_SCHEMA: Final[StructType] = StructType([
    StructField("adjustment_id", STRING, True),
    StructField("adjustment_type", STRING, True),
    StructField("amount", MONEY, True),
    StructField("applies_to", STRING, True),
    StructField("created_at", TIMESTAMP, True),
    StructField("currency", STRING, True),
    StructField("customer_id", STRING, True),
    StructField("discount_code", STRING, True),
    StructField("discount_type", STRING, True),
    StructField("effective_end", TIMESTAMP, True),
    StructField("effective_start", TIMESTAMP, True),
    StructField("invoice_id", STRING, True),
    StructField("percent_off", PERCENTAGE, True),
    StructField("reason", STRING, True),
    StructField("source_system", STRING, True),
    StructField("status", STRING, True),
    *_audit_fields(),
])


BILLING_EVENTS_SILVER_SCHEMA: Final[StructType] = StructType([
    StructField("amount", MONEY, True),
    StructField("billing_event_id", STRING, True),
    StructField("currency", STRING, True),
    StructField("customer_id", STRING, True),
    StructField("event_timestamp", TIMESTAMP, True),
    StructField("event_date", DATE, True),
    StructField("event_type", STRING, True),
    StructField("failure_code", STRING, True),
    StructField("invoice_id", STRING, True),
    StructField("payment_provider", STRING, True),
    StructField("received_at", TIMESTAMP, True),
    StructField("source", STRING, True),
    *_audit_fields(),
])


SILVER_FEED_SCHEMAS: Final[dict[str, StructType]] = {
    "plan_changes": PLAN_CHANGES_SILVER_SCHEMA,
    "pricing_plans": PRICING_PLANS_SILVER_SCHEMA,
    "customers": CUSTOMERS_SILVER_SCHEMA,
    "invoice_line_items": INVOICE_LINE_ITEMS_SILVER_SCHEMA,
    "usage_events": USAGE_EVENTS_SILVER_SCHEMA,
    "commercial_adjustments": COMMERCIAL_ADJUSTMENTS_SILVER_SCHEMA,
    "billing_events": BILLING_EVENTS_SILVER_SCHEMA,
}