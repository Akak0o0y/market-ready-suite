
import re
from common.utils import stable_hash_to_float

CITIES = ["الرياض", "جدة", "الدمام", "مكة", "المدينة"]
RIYADH_DISTRICTS = ["العقيق", "الملقا", "الياسمين", "النرجس", "عرقة", "قرطبة", "المونسية", "النسيم", "المروة"]

def geocode_text(q: str):
    text = re.sub(r"\s+", " ", q).strip()
    parts = re.split(r"[،,؛;|-]", text)
    parts = [p.strip() for p in parts if p.strip()]
    city = next((c for c in CITIES if c in text), "الرياض")
    district = next((d for d in RIYADH_DISTRICTS if d in text), (parts[1] if len(parts) > 1 else None))
    street = parts[2] if len(parts) > 2 else (parts[0] if parts else None)
    lat = 24.7136 + stable_hash_to_float(text, -0.05, 0.05)
    lon = 46.6753 + stable_hash_to_float(text[::-1], -0.05, 0.05)
    confidence = 0.6 + 0.4 * stable_hash_to_float(text, 0.0, 1.0)
    return {
        "query": q,
        "city": city,
        "district": district,
        "street": street,
        "location": {"lat": round(lat, 6), "lon": round(lon, 6)},
        "confidence": round(confidence, 2)
    }
