# RealTimeFlightTracker

A real-time, interactive flight tracker built with Dash, Dash Leaflet, and the OpenSky Network API.

## Features

- Live-updating map of flights (emoji airplane markers)
- Filter by country, altitude, speed, and flight status
- Dynamic summary and sidebar
- Responsive to map viewport and user controls

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
    or with Poetry:
    ```sh
    poetry install
    ```

2. Place your airplane icon in `assets/airplane.png` (or use the default emoji marker).

3. Run the app:
    ```sh
    python src/app.py
    ```

4. Open your browser to [http://127.0.0.1:8050](http://127.0.0.1:8050)

## Configuration

- Edit [src/config.py](cci:7://file:///Users/praveen/Documents/Code/RealTimeFlightTracker/src/config.py:0:0-0:0) to change bounding boxes, refresh intervals, or default country.

## Project Structure
```
src/
├── callbacks.py
├── config.py
├── layout.py
├── map_plot.py
├── opensky_data.py
├── app.py
└── assets
    └── airplane.png
```

## Notes

- The app uses the free OpenSky API, which is rate-limited. If you see a rate limit warning, wait a few minutes before retrying.
- For custom icons, upgrade dash-leaflet and use PNG/SVG in `assets/`.

---