import requests
import pandas as pd

COLUMNS = [
    "icao24", "callsign", "origin_country", "time_position", "last_contact",
    "longitude", "latitude", "baro_altitude", "on_ground", "velocity", "true_track",
    "vertical_rate", "sensors", "geo_altitude", "squawk", "spi", "position_source"
]

def fetch_flight_data(bbox):
    """
    Fetch and parse flight data from OpenSky within the given bounding box.
    bbox: dict with keys 'lamin', 'lomin', 'lamax', 'lomax'
    Returns: pandas DataFrame
    """
    url = (
        "https://opensky-network.org/api/states/all?"
        f"lamin={bbox['lamin']}&lomin={bbox['lomin']}&lamax={bbox['lamax']}&lomax={bbox['lomax']}"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        try:
            data = response.json()
        except Exception as e:
            return pd.DataFrame([], columns=COLUMNS)
    except Exception as e:
        if "429" in str(e):
            return pd.DataFrame([{"callsign": "RATE LIMITED"}], columns=COLUMNS)
        return pd.DataFrame([], columns=COLUMNS)

    df = pd.DataFrame(data.get("states", []), columns=COLUMNS)
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    df['baro_altitude'] = pd.to_numeric(df['baro_altitude'], errors='coerce')
    df['velocity'] = pd.to_numeric(df['velocity'], errors='coerce')
    df['origin_country'] = df['origin_country'].fillna("Unknown")
    df = df.dropna(subset=["latitude", "longitude"])
    return df 