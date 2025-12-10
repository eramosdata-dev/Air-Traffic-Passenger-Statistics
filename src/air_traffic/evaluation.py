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
    
    # Avoid division by zero for MAPE by filtering out zero values
    non_zero_mask = y_true != 0
    y_true_filtered = y_true[non_zero_mask]
    y_pred_filtered = y_pred[non_zero_mask]

    if len(y_true_filtered) == 0:
        mape = np.nan  # Return NaN if all true values are zero
    else:
        mape = np.mean(np.abs((y_true_filtered - y_pred_filtered) / y_true_filtered)) * 100

    return {
        "RMSE": rmse,
        "MAE": mae,
        "MAPE": mape
    }
