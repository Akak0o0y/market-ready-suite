
from common.utils import stable_hash_to_float, clamp
from common.eval import aqi_category

def nowcast_for_district(district: str):
    base_pm25 = 10 + 80 * stable_hash_to_float(district + "|pm25")
    base_pm10 = 30 + 250 * stable_hash_to_float(district + "|pm10")
    horizon = []
    for h in range(7):
        jitter = (stable_hash_to_float(f"{district}|{h}") - 0.5) * 10
        pm25 = clamp(base_pm25 + jitter, 5, 250)
        pm10 = clamp(base_pm10 + 2*jitter, 10, 500)
        horizon.append({
            "hour_ahead": h,
            "pm25": round(pm25, 1),
            "pm10": round(pm10, 1),
            "aqi_band": aqi_category(pm25, pm10)
        })
    return {"district": district, "nowcast": horizon}
