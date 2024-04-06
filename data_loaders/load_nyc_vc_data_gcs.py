import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/default_repo/gcp_credentials.json'

    bucket_name = 'nyc-vehicle-data-bc'
    folder_name = 'nyc_vc_data'

    root_path = f'{bucket_name}/{folder_name}'

    gcs = pa.fs.GcsFileSystem()
    df = pq.ParquetDataset(root_path, filesystem=gcs)

    return df.read_pandas().to_pandas()


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
