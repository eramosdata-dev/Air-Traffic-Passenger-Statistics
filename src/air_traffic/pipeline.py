from prefect import flow, task
import pandas as pd
from air_traffic.data_processing import load_and_clean_data, aggregate_monthly_passengers
from air_traffic.modeling import train_sarima_model, make_predictions
from air_traffic.evaluation import evaluate_model

@task
def load_data(filepath: str):
    print(f"Loading data from {filepath}...")
    df = load_and_clean_data(filepath)
    monthly_passengers = aggregate_monthly_passengers(df)
    return monthly_passengers

@task
def split_data(data: pd.Series, test_size: int = 12):
    print("Splitting data...")
    train = data.iloc[:-test_size]
    test = data.iloc[-test_size:]
    return train, test

@task
def train_model(train_data: pd.Series):
    print("Training SARIMA model...")
    # Using the optimal order found in exploration
    model = train_sarima_model(train_data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    return model

@task
def forecast(model, steps: int):
    print(f"Forecasting {steps} steps ahead...")
    predictions = make_predictions(model, steps)
    return predictions

@task
def evaluate(y_true, y_pred):
    print("Evaluating model...")
    metrics = evaluate_model(y_true, y_pred)
    print(f"Metrics: {metrics}")
    return metrics

@flow(name="Air Traffic Forecasting Pipeline")
def air_traffic_flow(data_path: str = "Data/Air_Traffic_Passenger_Statistics.csv"):
    data = load_data(data_path)
    train, test = split_data(data)
    model = train_model(train)
    predictions = forecast(model, steps=len(test))
    metrics = evaluate(test, predictions)
    return metrics

if __name__ == "__main__":
    air_traffic_flow()
