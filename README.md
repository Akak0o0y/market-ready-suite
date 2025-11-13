# Market-Ready Suite

Five small, practical backend services in one FastAPI repo. Each service exposes a real HTTP endpoint you can call right now. Logic is stubbed so demos never break; you can swap in real models later.

## What you get (benefits)
- **Real, callable APIs** for 5 use-cases: air quality nowcast, flood risk, KSA address normalize/geocode, water-leak detection, and school-zone safety.
- **Single command run** (no external services).
- **Deterministic responses** → stable demos, easy integration samples.
- **Simple replacement points** if you want to add ML later.

## Who this helps
- Students/engineers who want a repo that **looks active** and shows API skills.
- Early prototypes for Riyadh/GCC problems without over-engineering.

---

## Quickstart

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
