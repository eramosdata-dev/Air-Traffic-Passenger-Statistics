import pandas as pd
import os

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """
    Loads the Air Traffic Passenger Statistics dataset and performs initial cleaning.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found at: {filepath}")

    df = pd.read_csv(filepath)

    # 1. Drop rows with critical missing values
    df.dropna(subset=['OperatingAirline', 'PassengerCount'], inplace=True)

    # 2. Fill missing IATA codes with 'Unknown'
    df['OperatingAirlineIATACode'] = df['OperatingAirlineIATACode'].fillna('Unknown')
    df['PublishedAirlineIATACode'] = df['PublishedAirlineIATACode'].fillna('Unknown')

    # 3. Convert ActivityPeriod to datetime (assuming format YYYYMM)
    # The original data is likely int like 200507. We convert to string then datetime.
    df['ActivityPeriod'] = pd.to_datetime(df['ActivityPeriod'].astype(str), format='%Y%m')

    return df

def aggregate_monthly_passengers(df: pd.DataFrame) -> pd.Series:
    """
    Aggregates passenger counts by month.

    Args:
        df (pd.DataFrame): Cleaned dataframe with 'ActivityPeriod' and 'PassengerCount'.

    Returns:
        pd.Series: Monthly passenger counts indexed by ActivityPeriod.
    """
    monthly_passengers = df.groupby('ActivityPeriod')['PassengerCount'].sum()
    return monthly_passengers
