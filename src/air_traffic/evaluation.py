import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error

def evaluate_model(y_true: pd.Series, y_pred: pd.Series) -> dict:
    """
    Calculates evaluation metrics for the model.

    Args:
        y_true (pd.Series): Actual values.
        y_pred (pd.Series): Predicted values.

    Returns:
        dict: Dictionary containing RMSE, MAE, and MAPE.
    """
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    
    # Avoid division by zero for MAPE
    with np.errstate(divide='ignore', invalid='ignore'):
        mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
        if np.isinf(mape) or np.isnan(mape):
            mape = np.nan

    return {
        "RMSE": rmse,
        "MAE": mae,
        "MAPE": mape
    }
