
from common.utils import stable_hash_to_float
from common.eval import flood_band

def risk_for_segment(polyline_id: str):
    score = stable_hash_to_float(polyline_id, 0.0, 1.0)
    band = flood_band(score)
    return {"polyline_id": polyline_id, "risk_score": round(score, 3), "band": band}
