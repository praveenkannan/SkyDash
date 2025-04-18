from dash import html, dcc
import dash_leaflet as dl

REFRESH_SECONDS = 10  # or import from config

def serve_layout():
    return html.Div([
        # Header (top menu bar)
        html.Div([
            html.Span([
                html.Span("Sky", style={"color": "#0074D9", "fontWeight": "bold"}),
                html.Span("Dash", style={"color": "#2ECC40", "fontWeight": "bold"}),
                html.Span(": Real-Time Flight Tracker", style={"color": "#111", "fontWeight": "normal", "fontSize": "1.3rem"})
            ], style={
                "fontFamily": "Segoe UI, Arial, sans-serif",
                "fontSize": "2rem",
                "verticalAlign": "middle"
            })
        ], style={
            'display': 'flex',
            'alignItems': 'center',
            'height': '64px',
            'padding': '0 32px',
            'background': '#f4f6fb',
            'borderBottom': '1px solid #e0e0e0',
            'boxSizing': 'border-box'
        }),

        # Main content (sidebars above, map below)
        html.Div([
            # Sidebars row (summary left, filters right)
            html.Div([
                # Left: Summary/details
                html.Div([
                    html.Div(id='summary-panel', style={
                        "background": "#fff",
                        "borderRadius": "12px",
                        "boxShadow": "0 4px 16px rgba(0,0,0,0.07)",
                        "padding": "20px",
                        "margin": "20px",
                        "minWidth": "250px",
                        "maxWidth": "320px"
                    }),
                    html.Div(id='flight-detail', style={
                        "background": "#fafbfc",
                        "borderRadius": "8px",
                        "border": "1px solid #eee",
                        "padding": "16px",
                        "margin": "20px",
                        "minWidth": "250px",
                        "maxWidth": "320px"
                    }),
                ], style={
                    'flex': '0 0 320px',
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'stretch',
                }),
                # Spacer (fills middle)
                html.Div(style={'flex': 1}),
                # Right: Filters
                html.Div([
                    dcc.Dropdown(id='origin-country', placeholder="Filter by country", multi=True, style={'marginBottom': 16, "borderRadius": "8px"}),
                    html.Div(
                        dcc.RangeSlider(
                            id='altitude-slider', min=0, max=45000, step=1000, value=[0, 45000],
                            marks={i: str(i) for i in range(0, 50000, 10000)},
                            tooltip={"placement": "bottom"},
                            allowCross=False,
                            pushable=1000,
                            updatemode="drag",
                        ),
                        style={"marginBottom": 16}
                    ),
                    html.Div(
                        dcc.RangeSlider(
                            id='speed-slider', min=0, max=1000, step=10, value=[0, 1000],
                            marks={i: str(i) for i in range(0, 1100, 200)},
                            tooltip={"placement": "bottom"},
                            allowCross=False,
                            pushable=10,
                            updatemode="drag"
                        ),
                        style={"marginBottom": 16}
                    ),
                    dcc.RadioItems(id='in-air', options=[
                        {'label': 'All', 'value': 'all'},
                        {'label': 'In Air', 'value': 'in_air'},
                        {'label': 'On Ground', 'value': 'on_ground'}
                    ], value='all', inline=True, style={'marginBottom': 16, "marginTop": 16}),
                    html.Div(
                        dcc.Slider(
                            id='max-flights-slider',
                            min=10, max=500, step=10, value=100,
                            marks={i: str(i) for i in range(10, 501, 50)},
                            tooltip={"placement": "bottom"},
                            updatemode="drag"
                        ),
                        style={"marginTop": 16}
                    ),
                    dcc.Interval(id='interval', interval=REFRESH_SECONDS * 1000, n_intervals=0),
                ], style={
                    "background": "#fff",
                    "borderRadius": "12px",
                    "boxShadow": "0 4px 16px rgba(0,0,0,0.07)",
                    "padding": "20px",
                    "margin": "20px",
                    "minWidth": "250px",
                    "maxWidth": "320px"
                }),
            ], style={
                'display': 'flex',
                'flexDirection': 'row',
                'width': '100%',
                'boxSizing': 'border-box',
                'marginBottom': '0'
            }),
        ], style={
            'width': '100vw',
            'boxSizing': 'border-box',
            'display': 'flex',
            'flexDirection': 'column'
        }),
        # Map (fills below both sidebars)
        dl.Map(
            id="flight-map",
            center=[37.0902, -95.7129],
            zoom=4,
            style={"width": "100vw", "height": "calc(100vh - 64px - 180px)"},
            children=[
                dl.TileLayer(),
                dl.LayerGroup(id="flight-layer")
            ]
        ),
    ], style={
        'height': '100vh',
        'minHeight': '100vh',
        'width': '100vw',
        'background': '#f8fafc'
    })