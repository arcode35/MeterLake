from meterlake.config.resources import get_bronze_resources


def test_bronze_resources_use_catalog_directly() -> None:
    resources = get_bronze_resources(
        catalog="meterlake_dev",
        feed_name="billing_events",
    )

    assert resources.catalog == "meterlake_dev"
    assert resources.source_path == (
        "/Volumes/meterlake_dev/raw_files/landing/billing_events"
    )
    assert resources.checkpoint_path == (
        "/Volumes/meterlake_dev/ops/checkpoints/"
        "autoloader/billing_events"
    )
    assert resources.target_table == (
        "meterlake_dev.bronze.billing_events"
    )