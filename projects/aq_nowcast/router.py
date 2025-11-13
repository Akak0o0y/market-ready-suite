
from fastapi import APIRouter, Query
from .model import nowcast_for_district

router = APIRouter(prefix="/api", tags=["aq_nowcast"])

@router.get("/nowcast")
def nowcast(district: str = Query(..., description="District name")):
    return nowcast_for_district(district)
