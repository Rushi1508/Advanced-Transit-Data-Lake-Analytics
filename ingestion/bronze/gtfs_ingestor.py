from ingestion.utils.spark_utils import create_spark_session
from ingestion.utils.data_ingestor import DataIngestor
from ingestion.utils.config_loader import ConfigLoader
from ingestion.utils.file_path_manager import FilePathManager

if __name__ == "__main__":
    config = ConfigLoader()
    spark = create_spark_session()
    ingestor = DataIngestor(spark)
    path_manager = FilePathManager(config.base_data_dir, config.lakehouse_s3_path)

    # GTFS Files to Ingest
    gtfs_files = [
        ("calendar", "csv"),
        ("calendar_dates", "csv"),
        ("routes", "csv"),
        ("shapes", "csv"),
        ("stops", "csv"),
        ("stop_times", "csv"),
        ("trips", "csv")
    ]

    for table_name, file_format in gtfs_files:
        file_path = path_manager.get_local_file_path(table_name, file_format)
        ingestor.ingest_file_to_bronze(file_path, "gtfs", table_name, file_format)
        print(f"Ingested {table_name} to Bronze layer.")
