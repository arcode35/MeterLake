import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.streaming import DataStreamWriter

from meterlake.config.resources import get_bronze_resources
from meterlake.config.validation import (
    validate_job_parameters,
    validate_trigger_parameters,
)
from meterlake.observability.logging import get_logger
from meterlake.schemas.bronze import BRONZE_FEED_SCHEMAS
from meterlake.streaming.triggers import configure_trigger

logger = get_logger(__name__)


def ingest_bronze(
    spark: SparkSession,
    catalog: str,
    feed_name: str,
    trigger_mode: str,
    processing_time: str | None,
) -> None:
    validate_job_parameters(
        catalog=catalog,
        feed_name=feed_name,
    )
    validate_trigger_parameters(
        trigger_mode=trigger_mode,
        processing_time=processing_time,
    )

    logger.info(
        "Starting Bronze ingestion",
        catalog=catalog,
        feed_name=feed_name,
        trigger_mode=trigger_mode,
        processing_time=processing_time,
    )

    resources = get_bronze_resources(
        catalog=catalog,
        feed_name=feed_name,
    )

    logger.info(
        "Resolved Bronze resources",
        catalog=catalog,
        feed_name=feed_name,
        source_path=resources.source_path,
        target_table=resources.target_table,
        checkpoint_path=resources.checkpoint_path,
    )

    try:
        bronze_df = (
            spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", "json")
            .option("cloudFiles.schemaEvolutionMode", "rescue")
            .option("rescuedDataColumn", "_rescued_data")
            .option("columnNameOfCorruptRecord", "_corrupt_json")
            .schema(BRONZE_FEED_SCHEMAS[feed_name])
            .load(resources.source_path)
            .select(
                "*",
                F.current_timestamp().alias("_ingestion_timestamp"),
                F.lit(feed_name).alias("_source_feed"),
                F.col("_metadata.file_path").alias("_source_file_path"),
                F.col("_metadata.file_name").alias("_source_file_name"),
                F.col("_metadata.file_size").alias("_source_file_size"),
                F.col("_metadata.file_modification_time").alias(
                    "_source_file_modification_time"
                ),
            )
        )

        writer = (
            bronze_df.writeStream
            .format("delta")
            .outputMode("append")
            .queryName(f"bronze_{catalog}_{feed_name}")
            .option(
                "checkpointLocation",
                resources.checkpoint_path,
            )
        )

        writer = configure_trigger(
            writer=writer,
            trigger_mode=trigger_mode,
            processing_time=processing_time,
        )

        query = writer.toTable(resources.target_table)

        logger.info(
            "Bronze streaming query started",
            catalog=catalog,
            feed_name=feed_name,
            query_id=str(query.id),
            query_name=query.name,
        )

        query.awaitTermination()

        logger.info(
            "Bronze ingestion completed",
            catalog=catalog,
            feed_name=feed_name,
            query_id=str(query.id),
        )

    except Exception:
        logger.exception(
            "Bronze ingestion failed",
            catalog=catalog,
            feed_name=feed_name,
            trigger_mode=trigger_mode,
        )
        raise