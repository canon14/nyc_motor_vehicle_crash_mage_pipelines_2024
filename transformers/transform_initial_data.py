import pandas as pd
from pandas import DataFrame
import datetime as dt

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def transform_data(df: DataFrame) -> DataFrame:
    # rename columns to align with data from API
    df = df.rename(columns=
            {   
                "COLLISION_ID": "collision_id",
                "CRASH DATE": "crash_date", 
                "CRASH TIME": "crash_time", 
                "ON STREET NAME": "on_street_name",
                "BOROUGH": "borough",
                "ZIP CODE": "zip_code",
                "NUMBER OF PERSONS INJURED": "number_of_persons_injured",
                "NUMBER OF PERSONS KILLED": "number_of_persons_killed",
                "CONTRIBUTING FACTOR VEHICLE 1": "contributing_factor_vehicle_1",
                "CONTRIBUTING FACTOR VEHICLE 2": "contributing_factor_vehicle_2",
                "VEHICLE TYPE CODE 1": "vehicle_type_code1",
                "VEHICLE TYPE CODE 2": "vehicle_type_code2",

            }, errors="raise")
    
    # # create timestamp col by combining crash date and crash time cols
    df['crash_date'] = pd.to_datetime(df.crash_date)
    df['crash_time'] = df['crash_time'].apply(lambda t: dt.datetime.strptime(t.replace(':', ''),'%H%M').time())
    df['crash_timestamp'] = df.apply(lambda col: dt.datetime.combine(col['crash_date'], col['crash_time']), axis=1)

    
    # # convert crash_date from string to date
    # df['crash_date'] = df['crash_timestamp'].dt.date

    return df 

# SELECT ONLY NECESSARY COLUMNS FOR OUR FUTURE ANALYSIS
def select_number_columns(df: DataFrame) -> DataFrame:
    return df[['collision_id', 'crash_timestamp', 'crash_date', 'on_street_name', 'borough', 'zip_code', 
    'number_of_persons_injured', 'number_of_persons_killed', 'contributing_factor_vehicle_1', 
    'contributing_factor_vehicle_2', 'vehicle_type_code1', 'vehicle_type_code2'
        ]]


@transformer
def transform_df(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        df (DataFrame): Data frame from parent block.

    Returns:
        DataFrame: Transformed data frame
    """
    # Specify your transformation logic here

    return select_number_columns(transform_data(df))


@test
def test_output(df) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'
