import io
import pandas as pd
import requests
from sodapy import Socrata
from pandas import DataFrame
# Import date and timedelta class from datetime module
from datetime import date
from datetime import timedelta

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(**kwargs) -> DataFrame:

    record_limit = 100000
    amonth_ago_data = date.today() - timedelta(days = 5)
    
    data_to_fetch = f"http://data.ny.gov/resource/h9gi-nx95.json?$limit={record_limit}&crash_date={amonth_ago_data}"
    data = requests.get(data_to_fetch).json()

    return pd.DataFrame.from_records(data)


@test
def test_output(df) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'
