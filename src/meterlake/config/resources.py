from dataclasses import dataclass


@dataclass(frozen=True)
class BronzeResources:
    catalog: str
    source_path: str
    checkpoint_path: str
    target_table: str


@dataclass(frozen=True)
class SilverResources:
    catalog: str
    source_table: str
    target_table: str
    quarantine_table: str
    checkpoint_path: str
    quarantine_checkpoint_path: str


def get_bronze_resources(
    catalog: str,
    feed_name: str,
) -> BronzeResources:
    return BronzeResources(
        catalog=catalog,
        source_path=f"/Volumes/{catalog}/raw_files/landing/{feed_name}",
        checkpoint_path=(
            f"/Volumes/{catalog}/ops/checkpoints/autoloader/{feed_name}"
        ),
        target_table=f"{catalog}.bronze.{feed_name}",
    )


def get_silver_resources(
    catalog: str,
    feed_name: str,
) -> SilverResources:
    checkpoint_root = (
        f"/Volumes/{catalog}/ops/checkpoints/silver/{feed_name}"
    )

    return SilverResources(
        catalog=catalog,
        source_table=f"{catalog}.bronze.{feed_name}",
        target_table=f"{catalog}.silver.{feed_name}",
        quarantine_table=(
            f"{catalog}.data_quality.{feed_name}_quarantine"
        ),
        checkpoint_path=f"{checkpoint_root}/valid",
        quarantine_checkpoint_path=f"{checkpoint_root}/quarantine",
    )