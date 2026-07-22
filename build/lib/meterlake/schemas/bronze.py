from typing import Final

from pyspark.sql.types import StringType, StructField, StructType

# Define the individual StructType schemas above this dictionary.

STRING = StringType()

CUSTOMER_SUBSCRIPTIONS_SCHEMA: Final[StructType] = StructType([
    StructField("billing_frequency", STRING, True),
    StructField("change_type", STRING, True),
    StructField("customer_id", STRING, True),
    StructField("effective_end", STRING, True),
    StructField("effective_start", STRING, True),
    StructField("plan_code", STRING, True),
    StructField("plan_version", STRING, True),
    StructField("previous_plan_code", STRING, True),
    StructField("seats", STRING, True),
    StructField("source_system", STRING, True),
    StructField("status", STRING, True),
    StructField("subscription_id", STRING, True),
    StructField("updated_at", STRING, True),
    StructField("_corrupt_json", StringType(), True)
])


PRICING_PLANS_SCHEMA: Final[StructType] = StructType([
    StructField("additional_seat_monthly_fee", STRING, True),
    StructField("base_monthly_fee", STRING, True),
    StructField("currency", STRING, True),
    StructField("effective_end", STRING, True),
    StructField("effective_start", STRING, True),
    StructField("included_seats", STRING, True),

    StructField(
        "included_usage",
        StructType([
            StructField("api_calls", STRING, True),
            StructField("exports", STRING, True),
            StructField("minutes", STRING, True),
            StructField("seats", STRING, True),
            StructField("storage_gb", STRING, True),
            StructField("tokens", STRING, True),
        ]),
        True,
    ),

    StructField(
        "overage_rates",
        StructType([
            StructField("api_calls", STRING, True),
            StructField("exports", STRING, True),
            StructField("minutes", STRING, True),
            StructField("seats", STRING, True),
            StructField("storage_gb", STRING, True),
            StructField("tokens", STRING, True),
        ]),
        True,
    ),

    StructField("plan_code", STRING, True),
    StructField("plan_version", STRING, True),
    StructField("source_system", STRING, True),
    StructField("support_tier", STRING, True),
    StructField("_corrupt_json", StringType(), True)
])


CUSTOMERS_SCHEMA: Final[StructType] = StructType([
    StructField("_synthetic_anomaly", STRING, True),
    StructField("account_id", STRING, True),
    StructField("account_owner", STRING, True),
    StructField("billing_email", STRING, True),
    StructField("company_name", STRING, True),
    StructField("created_at", STRING, True),
    StructField("crm_source", STRING, True),
    StructField("customer_health_score", STRING, True),
    StructField("customer_id", STRING, True),
    StructField("industry", STRING, True),
    StructField("payment_terms_days", STRING, True),
    StructField("region", STRING, True),
    StructField("risk_score", STRING, True),
    StructField("segment", STRING, True),
    StructField("status", STRING, True),
    StructField("tax_exempt", STRING, True),
    StructField("updated_at", STRING, True),
    StructField("_corrupt_json", StringType(), True)
])


INVOICE_LINE_ITEMS_SCHEMA: Final[StructType] = StructType([
    StructField("amount", STRING, True),
    StructField("billing_period_end", STRING, True),
    StructField("billing_period_start", STRING, True),
    StructField("billing_rule_version", STRING, True),
    StructField("billing_system", STRING, True),
    StructField("charge_type", STRING, True),
    StructField("commercial_adjustment_id", STRING, True),
    StructField("created_at", STRING, True),
    StructField("currency", STRING, True),
    StructField("customer_id", STRING, True),
    StructField("description", STRING, True),
    StructField("expected_amount", STRING, True),
    StructField("invoice_actual_total", STRING, True),
    StructField("invoice_date", STRING, True),
    StructField("invoice_expected_total", STRING, True),
    StructField("invoice_id", STRING, True),
    StructField("line_item_id", STRING, True),
    StructField("plan_code", STRING, True),
    StructField("plan_version", STRING, True),
    StructField("quantity", STRING, True),
    StructField("subscription_id", STRING, True),
    StructField("synthetic_billing_issue", STRING, True),
    StructField("unit", STRING, True),
    StructField("unit_price", STRING, True),
    StructField("_corrupt_json", StringType(), True)
])


USAGE_EVENTS_SCHEMA: Final[StructType] = StructType([
    StructField("_corrupt_record", STRING, True),
    StructField("_synthetic_anomaly", STRING, True),
    StructField("account_id", STRING, True),
    StructField("customer_id", STRING, True),
    StructField("duplicate_marker", STRING, True),
    StructField("event_id", STRING, True),
    StructField("event_timestamp", STRING, True),
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
    StructField("plan_version", STRING, True),
    StructField("product_area", STRING, True),
    StructField("quantity", STRING, True),
    StructField("received_at", STRING, True),
    StructField("region", STRING, True),
    StructField("request_id", STRING, True),
    StructField("source", STRING, True),
    StructField("source_app_version", STRING, True),
    StructField("subscription_id", STRING, True),
    StructField("unit", STRING, True),
    StructField("workspace_id", STRING, True),
    StructField("_corrupt_json", StringType(), True)
])


COMMERCIAL_ADJUSTMENTS_SCHEMA: Final[StructType] = StructType([
    StructField("adjustment_id", STRING, True),
    StructField("adjustment_type", STRING, True),
    StructField("amount", STRING, True),
    StructField("applies_to", STRING, True),
    StructField("created_at", STRING, True),
    StructField("currency", STRING, True),
    StructField("customer_id", STRING, True),
    StructField("discount_code", STRING, True),
    StructField("discount_type", STRING, True),
    StructField("effective_end", STRING, True),
    StructField("effective_start", STRING, True),
    StructField("invoice_id", STRING, True),
    StructField("percent_off", STRING, True),
    StructField("reason", STRING, True),
    StructField("source_system", STRING, True),
    StructField("status", STRING, True),
    StructField("synthetic_adjustment_issue", STRING, True),
    StructField("_corrupt_json", StringType(), True)
])


BILLING_EVENTS_SCHEMA: Final[StructType] = StructType([
    StructField("amount", STRING, True),
    StructField("billing_event_id", STRING, True),
    StructField("currency", STRING, True),
    StructField("customer_id", STRING, True),
    StructField("duplicate_marker", STRING, True),
    StructField("event_timestamp", STRING, True),
    StructField("event_type", STRING, True),
    StructField("failure_code", STRING, True),
    StructField("invoice_id", STRING, True),
    StructField("payment_provider", STRING, True),
    StructField("received_at", STRING, True),
    StructField("source", STRING, True),
    StructField("synthetic_billing_issue", STRING, True),
    StructField("_corrupt_json", StringType(), True)
])

BRONZE_FEED_SCHEMAS: Final[dict[str, StructType]] = {
    "customer_subscriptions": CUSTOMER_SUBSCRIPTIONS_SCHEMA,
    "pricing_plans": PRICING_PLANS_SCHEMA,
    "customers": CUSTOMERS_SCHEMA,
    "invoice_line_items": INVOICE_LINE_ITEMS_SCHEMA,
    "usage_events": USAGE_EVENTS_SCHEMA,
    "commercial_adjustments": COMMERCIAL_ADJUSTMENTS_SCHEMA,
    "billing_events": BILLING_EVENTS_SCHEMA,
}