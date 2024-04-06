import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data['zip'] = pd.to_numeric(data['zip'], errors='coerce')
    data = data[data['zip'].between(10001, 11697)]

    # select only necessary columns
    data = data[['zip', 'pop2018']]
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
