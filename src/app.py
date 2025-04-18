# app.py

from dash import html
import dash_leaflet as dl
from dash_app import app  # This is the ONLY app instance!
from config import COUNTRY_BBOX, DEFAULT_COUNTRY, REFRESH_SECONDS
from layout import serve_layout
import callbacks  # Must be AFTER app is created, BEFORE run/debug

country = DEFAULT_COUNTRY
bbox = COUNTRY_BBOX[country]

# Compose the layout with the map
app.layout = serve_layout()

if __name__ == "__main__":
    app.run(debug=True)