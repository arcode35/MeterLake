from typing import cast

from pyspark.sql.streaming import DataStreamWriter


def configure_trigger(
    writer: DataStreamWriter,
    trigger_mode: str,
    processing_time: str | None,
) -> DataStreamWriter:
    if trigger_mode == "available_now":
        return writer.trigger(availableNow=True)

    return writer.trigger(
        processingTime=cast(str, processing_time)
    )