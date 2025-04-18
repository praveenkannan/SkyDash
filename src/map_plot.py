# map_plot.py

import dash_leaflet as dl
from dash import html

def make_markers(df):
    """
    Creates a list of Dash Leaflet Markers for each flight in the DataFrame.
    """
    markers = [
       dl.Marker(
        id={'type': 'flight-marker', 'index': row['callsign']},  # <-- Add this line!
        position=[row["latitude"], row["longitude"]],
        children=[
            dl.Tooltip("✈️ " + str(row['callsign'])),
            dl.Popup([
                html.B(f"Callsign: {row['callsign']}"),
                html.Br(),
                f"Country: {row['origin_country']}",
                html.Br(),
                f"Altitude: {row['baro_altitude']}",
                html.Br(),
                f"Velocity: {row['velocity']}"
            ])
        ]
    ) for _, row in df.iterrows()
    ]
    return markers