import pandas as pd
from air_traffic.data_processing import load_and_clean_data, aggregate_monthly_passengers

def test_load_and_clean_data(tmp_path):
    # Create a dummy CSV file
    d = {
        'ActivityPeriod': [200507, 200508, 200509],
        'OperatingAirline': ['ATA Airlines', 'ATA Airlines', None], # One missing airline to be dropped
        'OperatingAirlineIATACode': ['TZ', None, 'TZ'], # One missing code to be filled
        'PublishedAirline': ['ATA Airlines', 'ATA Airlines', 'ATA Airlines'],
        'PublishedAirlineIATACode': ['TZ', 'TZ', None], # One missing code to be filled
        'GEO Summary': ['Domestic', 'Domestic', 'Domestic'],
        'GEO Region': ['US', 'US', 'US'],
        'Activity Type Code': ['Deplaned', 'Deplaned', 'Deplaned'],
        'Price Category Code': ['Low Fare', 'Low Fare', 'Low Fare'],
        'Terminal': ['Terminal 1', 'Terminal 1', 'Terminal 1'],
        'BoardingArea': ['B', 'B', 'B'],
        'PassengerCount': [27271, 29131, 100]
    }
    df = pd.DataFrame(data=d)
    filepath = tmp_path / "test_data.csv"
    df.to_csv(filepath, index=False)

    # Run the function
    cleaned_df = load_and_clean_data(str(filepath))

    # Assertions
    assert len(cleaned_df) == 2 # Should have dropped the row with missing OperatingAirline
    assert cleaned_df['OperatingAirlineIATACode'].iloc[1] == 'Unknown' # Should have filled missing IATA code
    assert pd.api.types.is_datetime64_any_dtype(cleaned_df['ActivityPeriod']) # Should be datetime

def test_aggregate_monthly_passengers():
    # Create a dummy dataframe
    d = {
        'ActivityPeriod': pd.to_datetime(['2005-07-01', '2005-07-01', '2005-08-01']),
        'PassengerCount': [100, 200, 300]
    }
    df = pd.DataFrame(data=d)

    # Run the function
    monthly_passengers = aggregate_monthly_passengers(df)

    # Assertions
    assert len(monthly_passengers) == 2
    assert monthly_passengers.loc[pd.Timestamp('2005-07-01')] == 300
    assert monthly_passengers.loc[pd.Timestamp('2005-08-01')] == 300
