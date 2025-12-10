import pandas as pd
import numpy as np
from air_traffic.evaluation import evaluate_model

def test_evaluate_model():
    y_true = pd.Series([100, 200, 300])
    y_pred = pd.Series([110, 190, 300])

    metrics = evaluate_model(y_true, y_pred)

    assert "RMSE" in metrics
    assert "MAE" in metrics
    assert "MAPE" in metrics
    
    # Expected values
    # Error: [10, -10, 0]
    # Abs Error: [10, 10, 0]
    # Squared Error: [100, 100, 0]
    
    # RMSE: sqrt(200/3) = 8.16...
    assert np.isclose(metrics["RMSE"], np.sqrt(200/3))
    
    # MAE: 20/3 = 6.66...
    assert np.isclose(metrics["MAE"], 20/3)
    
    # MAPE: (10/100 + 10/200 + 0/300) / 3 * 100 = (0.1 + 0.05) / 3 * 100 = 5%
    assert np.isclose(metrics["MAPE"], 5.0)

def test_evaluate_model_with_zero_in_true_values():
    """
    Test that MAPE is calculated correctly when y_true contains zeros.
    The zero values should be ignored.
    """
    y_true = pd.Series([0, 100, 200])
    y_pred = pd.Series([10, 110, 220])

    metrics = evaluate_model(y_true, y_pred)

    # MAPE should be calculated only on non-zero values:
    # MAPE = mean(|(100-110)/100|, |(200-220)/200|) * 100
    #      = mean(0.1, 0.1) * 100 = 10%
    assert np.isclose(metrics["MAPE"], 10.0)

def test_evaluate_model_with_all_zeros_in_true_values():
    """
    Test that MAPE is NaN when all y_true values are zero.
    """
    y_true = pd.Series([0, 0, 0])
    y_pred = pd.Series([10, 20, 30])
    
    metrics = evaluate_model(y_true, y_pred)
    
    assert np.isnan(metrics["MAPE"])
