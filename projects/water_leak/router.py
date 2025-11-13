
from fastapi import APIRouter, Query
from .model import anomaly_for_meter

router = APIRouter(prefix="/api", tags=["water_leak"])

@router.get("/water/anomaly")
def water_anomaly(meter_id: str = Query(..., description="Meter ID in sample data")):
    return anomaly_for_meter(meter_id)
