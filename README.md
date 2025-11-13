Market-Ready Suite

Small FastAPI project that exposes five independent services commonly needed in Riyadh/GCC use-cases. Each service has a simple HTTP API and a minimal web page for quick testing.

Services

Air Quality Nowcast – short-term PM2.5/PM10 with a coarse AQI band.

Flash-Flood Street Risk – per-segment flood risk score and band.

KSA Address Normalizer/Geocoder – parse free-text Arabic addresses into structured fields + lat/lon.

Water Leak / Abnormal Use – detect continuous night leaks or bursts from meter time-series.

School-Zone Safety (Vision) – image endpoint for traffic-violation detection near school gates.

Status: working APIs with baseline logic. Replace the model.py in each service when you add real models/data.

Quick start
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000


App: http://127.0.0.1:8000

API docs (OpenAPI/Swagger): http://127.0.0.1:8000/docs

API usage
1) Air Quality Nowcast

GET /api/nowcast?district=العقيق

curl "http://127.0.0.1:8000/api/nowcast?district=العقيق"


Response (example):

{
  "district": "العقيق",
  "nowcast": [
    {"hour_ahead": 0, "pm25": 22.3, "pm10": 71.2, "aqi_band": "Moderate"},
    ...
  ]
}

2) Flash-Flood Street Risk

GET /api/flood_risk?polyline_id=R123

curl "http://127.0.0.1:8000/api/flood_risk?polyline_id=R123"


Response:

{"polyline_id":"R123","risk_score":0.58,"band":"Yellow"}

3) KSA Address Normalizer / Geocoder

GET /api/geocode?q=الرياض، العقيق، شارع الامام

curl "http://127.0.0.1:8000/api/geocode?q=الرياض، العقيق، شارع الامام"


Response:

{
  "query":"الرياض، العقيق، شارع الامام",
  "city":"الرياض",
  "district":"العقيق",
  "street":"شارع الامام",
  "location":{"lat":24.72,"lon":46.69},
  "confidence":0.81
}

4) Water Leak / Abnormal Use

GET /api/water/anomaly?meter_id=A1

curl "http://127.0.0.1:8000/api/water/anomaly?meter_id=A1"


Response:

{
  "meter_id":"A1",
  "status":"continuous_leak",
  "metrics":{"night_avg":1.35,"day_avg":0.42,"leak_score":1.05},
  "reason":"night average 1.35 m3/h exceeds threshold"
}

5) School-Zone Safety (image upload)

POST /api/school/risk

curl -F "file=@demo/static/sample.jpg" http://127.0.0.1:8000/api/school/risk


Response:

{
  "filename":"sample.jpg",
  "violations":[{"type":"double_parking","count":1}],
  "note":"stub model — replace with real detector"
}

Tech stack

Backend: FastAPI, Uvicorn, Pydantic

Data/Utils: pandas, numpy

UI: Simple HTML/JS page under demo/ for manual calls

Project layout
app.py
common/
  utils.py
  eval.py
projects/
  aq_nowcast/      # /api/nowcast
    router.py
    model.py
  flood_risk/      # /api/flood_risk
    router.py
    model.py
  address_norm/    # /api/geocode
    router.py
    model.py
  water_leak/      # /api/water/anomaly
    router.py
    model.py
    sample_data/meter_sample.csv
  school_vision/   # /api/school/risk
    router.py
demo/
  templates/index.html
  static/{styles.css, main.js, sample.jpg}
requirements.txt
README.md

Replacing baselines with your logic

Swap projects/*/model.py with your model code and keep the same function signatures.

For school vision, add your detector and call it inside the route handler.

Notes

All endpoints are local by default (http://127.0.0.1:8000).

A sample image is included at demo/static/sample.jpg.

The water service ships with a small sample CSV (meter_id=A1) for quick tests.
