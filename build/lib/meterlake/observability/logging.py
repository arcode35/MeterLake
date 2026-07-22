import logging

from pyspark.logger import PySparkLogger


def get_logger(
    name: str,
    level: int = logging.INFO,
) -> PySparkLogger:
    logger = PySparkLogger.getLogger(name)
    logger.setLevel(level)
    return logger