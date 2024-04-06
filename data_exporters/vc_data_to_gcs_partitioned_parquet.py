import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/default_repo/gcp_credentials.json'

bucket_name = 'nyc-vehicle-data-bc'
project_id = 'zoomcamp-final-project'
table_name = 'nyc_vc_data'

root_path = f'{bucket_name}/{table_name}'


@data_exporter
def export_data(data, *args, **kwargs):
    
    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table, 
        root_path=root_path,
        partition_cols=['crash_date'],
        filesystem = gcs,
        coerce_timestamps='us'
    )