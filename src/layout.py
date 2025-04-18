# layout.py

from dash import html, dcc
from config import COUNTRY_BBOX, DEFAULT_COUNTRY, REFRESH_SECONDS

country = DEFAULT_COUNTRY
bbox = COUNTRY_BBOX[country]

def serve_layout():
    return html.Div([
        html.Div([
            html.H2("Flight Tracker Dashboard"),
            html.Div(id='summary-panel', style={'marginBottom': 20}),
            dcc.Dropdown(id='origin-country', placeholder="Filter by country", multi=True, style={'marginBottom': 10}),
            dcc.RangeSlider(id='altitude-slider', min=0, max=45000, step=1000, value=[0, 45000],
                            marks={i: str(i) for i in range(0, 50000, 10000)}, tooltip={"placement": "bottom"}),
            dcc.RangeSlider(id='speed-slider', min=0, max=1000, step=10, value=[0, 1000],
                            marks={i: str(i) for i in range(0, 1100, 200)}, tooltip={"placement": "bottom"}),
            dcc.RadioItems(id='in-air', options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'In Air', 'value': 'in_air'},
                {'label': 'On Ground', 'value': 'on_ground'}
            ], value='all', inline=True, style={'marginBottom': 10}),
            dcc.Slider(
                id='max-flights-slider',
                min=10, max=500, step=10, value=100,
                marks={i: str(i) for i in range(10, 501, 50)},
                tooltip={"placement": "bottom"},
                updatemode="drag"
            ),
            html.Div(id='flight-detail', style={'marginTop': 20, 'border': '1px solid #ccc', 'padding': 10}),
            dcc.Interval(id='interval', interval=REFRESH_SECONDS * 1000, n_intervals=0),
        ], style={'width': '25%', 'float': 'left', 'padding': 20, 'background': '#f9f9f9'}),
        html.Div([
            # Map with bounds for initial viewport
        ], style={'width': '70%', 'float': 'right', 'padding': 20}),
        html.Button("Force Update", id="force-update-btn"),
    ])