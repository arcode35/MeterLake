from dataclasses import dataclass

@dataclass(frozen=True)
class BronzeResources:
    catalog: str
    source_path: str
    checkpoint_path: str
    target_table: str


def get_bronze_resources(
    catalog: str,
    feed_name: str,
) -> BronzeResources:
    return BronzeResources(
        catalog=catalog,
        source_path=(
            f"/Volumes/{catalog}/raw_files/landing/{feed_name}"
        ),
        checkpoint_path=(
            f"/Volumes/{catalog}/ops/checkpoints/autoloader/{feed_name}"
        ),
        target_table=f"{catalog}.bronze.{feed_name}",
    )
