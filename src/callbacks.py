# callbacks.py

from dash import Output, Input, State, html, ALL
from dash_app import app
from opensky_data import fetch_flight_data
from map_plot import make_markers
from config import COUNTRY_BBOX, DEFAULT_COUNTRY

country = DEFAULT_COUNTRY
bbox = COUNTRY_BBOX[country]

@app.callback(
    Output('origin-country', 'options'),
    Output('origin-country', 'value'),
    Input('interval', 'n_intervals'),
    Input('force-update-btn', 'n_clicks')
)
def update_country_options(n, force_update):
    df = fetch_flight_data(bbox)
    countries = sorted(df['origin_country'].dropna().unique())
    options = [{'label': c, 'value': c} for c in countries]
    return options, None

@app.callback(
    Output('flight-layer', 'children'),
    Output('summary-panel', 'children'),
    Input('interval', 'n_intervals'),
    Input('origin-country', 'value'),
    Input('altitude-slider', 'value'),
    Input('speed-slider', 'value'),
    Input('in-air', 'value'),
    Input('max-flights-slider', 'value'),
    Input('flight-map', 'bounds'),
)
def update_map(n, origin_country, altitude_range, speed_range, in_air, max_flights, bounds):
    df = fetch_flight_data(bbox)
    # Filter by map bounds (viewport)
    if bounds:
        sw_lat, sw_lng = bounds[0]
        ne_lat, ne_lng = bounds[1]
        df = df[
            (df['latitude'] >= sw_lat) & (df['latitude'] <= ne_lat) &
            (df['longitude'] >= sw_lng) & (df['longitude'] <= ne_lng)
        ]
    df['baro_altitude'] = df['baro_altitude'].fillna(0)
    df['velocity'] = df['velocity'].fillna(0)
    df['origin_country'] = df['origin_country'].fillna("Unknown")
    df = df.sort_values("baro_altitude", ascending=False).head(max_flights)
    if origin_country:
        df = df[df['origin_country'].isin(origin_country)]
    df = df[df['baro_altitude'].between(*altitude_range)]
    df = df[df['velocity'].between(*speed_range)]
    if in_air == 'in_air':
        df = df[df['on_ground'] == False]
    elif in_air == 'on_ground':
        df = df[df['on_ground'] == True]
    markers = make_markers(df)
    total = len(df)
    if not df.empty and df.iloc[0]['callsign'] == "RATE LIMITED":
        summary = html.Div([
            html.Span("⚠️ OpenSky API rate limit reached. Please wait and try again later.", style={"color": "red"})
        ])
        return [], summary
    if not df.empty:
        max_alt = int(df['baro_altitude'].max())
        min_alt = int(df['baro_altitude'].min())
        avg_alt = int(df['baro_altitude'].mean())
        busiest = df['origin_country'].value_counts().idxmax()
    else:
        max_alt = min_alt = avg_alt = busiest = "N/A"
    summary = html.Div([
        html.Span(f"Total Flights: {total}  |  "),
        html.Span(f"Max Altitude: {max_alt}  |  "),
        html.Span(f"Min Altitude: {min_alt}  |  "),
        html.Span(f"Avg Altitude: {avg_alt}  |  "),
        html.Span(f"Busiest Country: {busiest}")
    ])
    return markers, summary

@app.callback(
    Output('flight-detail', 'children'),
    Input({'type': 'flight-marker', 'index': ALL}, 'n_clicks'),
    State('flight-layer', 'children'),
    prevent_initial_call=True
)
def display_flight_details(n_clicks, children):
    return "Click an airplane icon for details."