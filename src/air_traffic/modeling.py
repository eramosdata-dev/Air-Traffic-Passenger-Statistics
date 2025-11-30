import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.statespace.sarimax import SARIMAXResultsWrapper

def train_sarima_model(
    data: pd.Series, 
    order: tuple = (1, 1, 1), 
    seasonal_order: tuple = (1, 1, 1, 12)
) -> SARIMAXResultsWrapper:
    """
    Trains a SARIMA model on the provided time series data.

    Args:
        data (pd.Series): The time series data to train on.
        order (tuple): The (p, d, q) order of the model.
        seasonal_order (tuple): The (P, D, Q, s) seasonal order of the model.

    Returns:
        SARIMAXResultsWrapper: The fitted SARIMA model.
    """
    model = sm.tsa.statespace.SARIMAX(
        data,
        order=order,
        seasonal_order=seasonal_order,
        enforce_stationarity=False,
        enforce_invertibility=False
    )
    results = model.fit(disp=False)
    return results

def make_predictions(model: SARIMAXResultsWrapper, steps: int) -> pd.Series:
    """
    Generates forecasts using the trained SARIMA model.

    Args:
        model (SARIMAXResultsWrapper): The fitted model.
        steps (int): Number of steps to forecast.

    Returns:
        pd.Series: The predicted mean values.
    """
    forecast = model.get_forecast(steps=steps)
    return forecast.predicted_mean
