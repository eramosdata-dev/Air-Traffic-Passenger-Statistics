import pandas as pd
import numpy as np
from air_traffic.modeling import train_sarima_model, make_predictions

def test_train_sarima_model():
    # Create synthetic time series data
    dates = pd.date_range(start='2020-01-01', periods=24, freq='M')
    values = np.arange(24) + np.random.normal(0, 1, 24)
    data = pd.Series(values, index=dates)

    # Train model
    model = train_sarima_model(data, order=(1, 0, 0), seasonal_order=(0, 0, 0, 12))

    # Assertions
    assert model is not None
    assert hasattr(model, 'params')

def test_make_predictions():
    # Create synthetic time series data
    dates = pd.date_range(start='2020-01-01', periods=24, freq='M')
    values = np.arange(24)
    data = pd.Series(values, index=dates)

    # Train model
    model = train_sarima_model(data, order=(1, 0, 0), seasonal_order=(0, 0, 0, 12))

    # Predict
    steps = 5
    predictions = make_predictions(model, steps=steps)

    # Assertions
    assert len(predictions) == steps
    assert isinstance(predictions, pd.Series)
