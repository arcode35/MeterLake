# src/meterlake/silver/registry.py

from collections.abc import Callable
from dataclasses import dataclass
from types import MappingProxyType

from pyspark.sql import DataFrame

from meterlake.silver.feeds.usage_events import transform_usage_events



@dataclass(frozen=True, slots=True)
class SilverFeedConfig:
    primary_keys: tuple[str, ...]
    sequence_column: str
    transform: Callable[[DataFrame], DataFrame]


SILVER_FEEDS = MappingProxyType(
    {
        "usage_events": SilverFeedConfig(
            primary_keys=("event_id",),
            sequence_column="event_timestamp",
            transform=transform_usage_events,
        ),
    }
)


def get_silver_feed_config(feed_name: str) -> SilverFeedConfig:
    normalized_feed_name = feed_name.strip().lower()

    try:
        return SILVER_FEEDS[normalized_feed_name]
    except KeyError as exc:
        supported_feeds = ", ".join(sorted(SILVER_FEEDS))
        raise ValueError(
            f"Unsupported Silver feed: {feed_name!r}. "
            f"Supported feeds: {supported_feeds}"
        ) from exc

from pyspark.sql import DataFrame, functions as F
from pyspark.sql.types import StructType


def apply_silver_schema(
    df: DataFrame,
    schema: StructType,
) -> DataFrame:
    source_columns = set(df.columns)

    casted_columns = []
    cast_errors = []
    required_errors = []

    for field in schema.fields:
        exists = field.name in source_columns

        source = (
            F.col(field.name)
            if exists
            else F.lit(None).cast(field.dataType)
        )

        casted = (
            source.try_cast(field.dataType)
            if exists
            else source
        )

        casted_columns.append(
            casted.alias(field.name)
        )

        if exists:
            cast_errors.append(
                F.when(
                    source.isNotNull() & casted.isNull(),
                    F.lit(field.name),
                )
            )

        if not field.nullable:
            required_errors.append(
                F.when(
                    casted.isNull(),
                    F.lit(field.name),
                )
            )

    return df.select(
        *casted_columns,
        F.array_compact(
            F.array(*cast_errors)
        ).alias("_cast_errors"),
        F.array_compact(
            F.array(*required_errors)
        ).alias("_required_errors"),
    )