import argparse

from pyspark.sql import SparkSession

from meterlake.bronze.ingestion import ingest_bronze
from meterlake.observability.logging import get_logger


logger = get_logger(__name__)


def normalize_optional_string(value: str | None) -> str | None:
    if value is None:
        return None

    normalized = value.strip()
    return normalized or None


def main(
    catalog: str,
    feed_name: str,
    trigger_mode: str = "available_now",
    processing_time: str | None = None,
) -> None:
    catalog = catalog.strip().lower()
    feed_name = feed_name.strip().lower()
    trigger_mode = trigger_mode.strip().lower()
    processing_time = normalize_optional_string(processing_time)

    logger.info(
        "Initializing Bronze ingestion job",
        job_name="bronze_ingestion",
        catalog=catalog,
        feed_name=feed_name,
        trigger_mode=trigger_mode,
        processing_time=processing_time,
    )

    spark = SparkSession.builder.getOrCreate()

    ingest_bronze(
        spark=spark,
        catalog=catalog,
        feed_name=feed_name,
        trigger_mode=trigger_mode,
        processing_time=processing_time,
    )


def cli() -> None:
    parser = argparse.ArgumentParser(
        description="Ingest one MeterLake Bronze feed"
    )
    parser.add_argument("--catalog", required=True)
    parser.add_argument(
        "--feed-name",
        "--feed_name",
        dest="feed_name",
        required=True,
    )
    parser.add_argument(
        "--trigger-mode",
        "--trigger_mode",
        dest="trigger_mode",
        choices=("available_now", "processing_time"),
        default="available_now",
    )
    parser.add_argument(
        "--processing-time",
        "--processing_time",
        dest="processing_time",
    )

    args = parser.parse_args()

    main(
        catalog=args.catalog,
        feed_name=args.feed_name,
        trigger_mode=args.trigger_mode,
        processing_time=args.processing_time,
    )

if __name__ == "__main__":
    cli()