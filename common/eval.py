
def aqi_category(pm25: float, pm10: float) -> str:
    worst = max(pm25/35.0, pm10/154.0)
    if   worst < 1.0:  return "Good"
    elif worst < 1.5:  return "Moderate"
    elif worst < 2.0:  return "Unhealthy for Sensitive"
    elif worst < 3.0:  return "Unhealthy"
    else:              return "Very Unhealthy"

def flood_band(score: float) -> str:
    if score < 0.33: return "Green"
    if score < 0.66: return "Yellow"
    return "Red"
