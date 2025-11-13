
from fastapi import APIRouter, Query
from .model import risk_for_segment

router = APIRouter(prefix="/api", tags=["flood_risk"])

@router.get("/flood_risk")
def flood_risk(polyline_id: str = Query(..., description="Road segment/polyline id")):
    return risk_for_segment(polyline_id)
