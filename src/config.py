# config.py

# Bounding boxes for different countries/regions
COUNTRY_BBOX = {
    "USA": {
        "lamin": 24.396308,
        "lomin": -125.0,
        "lamax": 49.384358,
        "lomax": -66.93457,
        "center": [37.0902, -95.7129],
        "zoom": 4,
    },
    # Add more countries/regions as needed
}

DEFAULT_COUNTRY = "USA"
REFRESH_SECONDS = 60

# DataFrame columns for OpenSky API
COLUMNS = [
    "icao24", "callsign", "origin_country", "time_position", "last_contact",
    "longitude", "latitude", "baro_altitude", "on_ground", "velocity", "true_track",
    "vertical_rate", "sensors", "geo_altitude", "squawk", "spi", "position_source"
]