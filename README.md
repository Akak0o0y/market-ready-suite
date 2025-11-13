
# Market-Ready Suite (Riyadh)
Five sellable AI product MVPs in one FastAPI mono-repo. Straightforward, minimal, and ready to extend.

## Projects
1) **AQ Nowcast (Dust/AQI)** — `/api/nowcast?district=<name>`
2) **Flash-Flood Street Risk** — `/api/flood_risk?polyline_id=<id>`
3) **KSA Address Normalizer & Geocoder** — `/api/geocode?q=<free text>`
4) **Water Leak & Abnormal Use** — `/api/water/anomaly?meter_id=<id>`
5) **School-Zone Vision Safety** — `/api/school/risk` (POST image)

> NOTE: These are working **stubs** with deterministic baselines to prove wiring, API, and demo UI. Replace `model.py` logic per project with real models when ready.

## Quickstart
```bash
python -m venv .venv && . .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
# Open http://127.0.0.1:8000
```

## cURL smoke tests
```bash
# AQ
curl "http://127.0.0.1:8000/api/nowcast?district=Al%20Masaif"
# Flood
curl "http://127.0.0.1:8000/api/flood_risk?polyline_id=R123"
# Geocode
curl "http://127.0.0.1:8000/api/geocode?q=الرياض، العقيق، شارع الامام"
# Water Anomaly (uses sample meter 'A1')
curl "http://127.0.0.1:8000/api/water/anomaly?meter_id=A1"
# School Vision (image)
curl -F "file=@demo/static/sample.jpg" http://127.0.0.1:8000/api/school/risk
```

## Structure
```
common/
  utils.py
  eval.py
projects/
  aq_nowcast/{router.py, model.py}
  flood_risk/{router.py, model.py}
  address_norm/{router.py, model.py}
  water_leak/{router.py, model.py, sample_data/meter_sample.csv}
  school_vision/{router.py}
demo/
  templates/index.html
  static/{main.js, styles.css, sample.jpg}
app.py
requirements.txt
```

## Next steps
- Replace stubs with real models/data.
- Add DB + auth when piloting.
- Build metrics & logs in `common/eval.py`.
