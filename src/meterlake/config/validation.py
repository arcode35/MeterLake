from typing import Final
from meterlake.schemas.bronze import BRONZE_FEED_SCHEMAS

VALID_ENVIRONMENTS: Final[frozenset[str]] = frozenset({"dev", "prod"})
VALID_FEEDS: Final[frozenset[str]] = frozenset(BRONZE_FEED_SCHEMAS)
VALID_TRIGGER_MODES: Final[frozenset[str]] = frozenset(
    {"available_now", "processing_time"}
)

def validate_job_parameters(catalog: str, feed_name: str) -> None:
    """
    Validates runtime parameters passed from Databricks widgets.
    Raises ValueError if parameters fall outside expected execution bounds.
    """
    if catalog not in VALID_ENVIRONMENTS:
        raise ValueError(
            f"Invalid environment '{catalog}'. "
            f"Expected one of: {sorted(VALID_ENVIRONMENTS)}"
        )

    if feed_name not in VALID_FEEDS:
        raise ValueError(
            f"Invalid feed name '{feed_name}'. "
            f"Expected one of: {sorted(VALID_FEEDS)}"
        )


def validate_trigger_parameters(
    trigger_mode: str,
    processing_time: str | None,
) -> None:
    """
    Validate Structured Streaming trigger configuration.

    Rules:
    - trigger_mode must be "available_now" or "processing_time".
    - processing_time is required for "processing_time".
    - processing_time must not be supplied for "available_now".
    """
    if trigger_mode not in VALID_TRIGGER_MODES:
        raise ValueError(
            f"Invalid trigger mode {trigger_mode!r}. "
            f"Expected one of: {sorted(VALID_TRIGGER_MODES)}"
        )

    if trigger_mode == "processing_time":
        if processing_time is None or not processing_time.strip():
            raise ValueError(
                "processing_time must be provided when "
                "trigger_mode='processing_time'."
            )

    elif processing_time is not None:
        raise ValueError(
            "processing_time must be None when "
            "trigger_mode='available_now'."
        )