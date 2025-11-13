
import pandas as pd
from pathlib import Path

SAMPLE = Path(__file__).parent/"sample_data"/"meter_sample.csv"

def anomaly_for_meter(meter_id: str):
    if not SAMPLE.exists():
        return {"meter_id": meter_id, "error": "sample data not found"}
    df = pd.read_csv(SAMPLE, parse_dates=["timestamp"])
    d = df[df["meter_id"]==meter_id].copy()
    if d.empty:
        return {"meter_id": meter_id, "status": "unknown_meter"}
    d["hour"] = d["timestamp"].dt.hour
    night = d[(d["hour"]>=1) & (d["hour"]<=5)]
    day   = d[(d["hour"]>=9) & (d["hour"]<=20)]
    night_avg = float(night["value"].tail(48).mean()) if not night.empty else 0.0
    day_avg   = float(day["value"].tail(48).mean()) if not day.empty else 0.0
    leak_score = max(0.0, (night_avg - 0.3))
    status, reason = "ok", "no anomaly"
    if leak_score > 0.2:
        status = "continuous_leak"
        reason = f"night average {night_avg:.2f} m3/h exceeds threshold"
    elif (day_avg > 1.5):
        status = "burst_or_high_usage"
        reason = f"day average {day_avg:.2f} m3/h unusually high"
    return {
        "meter_id": meter_id,
        "status": status,
        "metrics": {"night_avg": round(night_avg,2), "day_avg": round(day_avg,2), "leak_score": round(leak_score,2)},
        "reason": reason
    }
