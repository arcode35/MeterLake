import pytest

from meterlake.config.validation import (
    validate_job_parameters,
    validate_trigger_parameters,
)
from meterlake.schemas.bronze import BRONZE_FEED_SCHEMAS


EXPECTED_FEEDS = {
    "usage_events",
    "billing_events",
    "invoice_line_items",
    "customer_subscriptions",
    "pricing_plans",
    "customers",
    "commercial_adjustments",
}


def test_bronze_schema_registry_contains_expected_feeds() -> None:
    assert set(BRONZE_FEED_SCHEMAS) == EXPECTED_FEEDS


@pytest.mark.parametrize("feed_name", sorted(EXPECTED_FEEDS))
def test_valid_job_parameters(feed_name: str) -> None:
    validate_job_parameters(
        catalog="meterlake_dev",
        feed_name=feed_name,
    )


def test_invalid_catalog_is_rejected() -> None:
    with pytest.raises(ValueError):
        validate_job_parameters(
            catalog="dev",
            feed_name="usage_events",
        )


def test_invalid_feed_is_rejected() -> None:
    with pytest.raises(ValueError):
        validate_job_parameters(
            catalog="meterlake_dev",
            feed_name="unknown_feed",
        )


def test_available_now_accepts_no_processing_time() -> None:
    validate_trigger_parameters(
        trigger_mode="available_now",
        processing_time=None,
    )


def test_processing_time_requires_interval() -> None:
    with pytest.raises(ValueError):
        validate_trigger_parameters(
            trigger_mode="processing_time",
            processing_time=None,
        )