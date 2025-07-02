import pytest
import pandas as pd
import numpy as np
from unittest import mock
import sys
sys.path.append('../src')
# Import the feature_engineering_pipeline function from your script
from data_processed import feature_engineering_pipeline

@pytest.fixture
def mock_preprocessed_data(tmp_path):
    # Create a minimal DataFrame with required columns for the pipeline
    df = pd.DataFrame({
        'TransactionId': [1, 2],
        'CustomerId': [101, 102],
        'BatchId': [201, 202],
        'AccountId': [301, 302],
        'SubscriptionId': [401, 402],
        'ProductId': [501, 502],
        'ChannelId': [601, 602],
        'ProviderId': [701, 702],
        'Amount': [100.0, 200.0],
        'Value': [150.0, 250.0],
        'CurrencyCode': ['USD', 'EUR'],
        'ProductCategory': ['A', 'B'],
        'CountryCode': ['US', 'DE'],
        'PricingStrategy': [1, 2],
        'FraudResult': [0, 1],
        'TransactionStartTime': ['2023-01-01', '2023-02-01']
    })
    return df

def test_feature_engineering_pipeline(monkeypatch, mock_preprocessed_data):
    # Patch the global preprocessed_data variable in the module
    import data_processed
    monkeypatch.setattr(data_processed, "preprocessed_data", mock_preprocessed_data)
    
    result = data_processed.feature_engineering_pipeline()
    
    assert 'feature_processed_train' in result
    assert 'processed_data' in result
    # Check that processed_data is a DataFrame and has rows
    assert isinstance(result['processed_data'], pd.DataFrame)
    assert result['processed_data'].shape[0] == 2