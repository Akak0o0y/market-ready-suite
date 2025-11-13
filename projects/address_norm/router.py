
from fastapi import APIRouter, Query
from .model import geocode_text

router = APIRouter(prefix="/api", tags=["address_norm"])

@router.get("/geocode")
def geocode(q: str = Query(..., description="Free-text Arabic/English address")):
    return geocode_text(q)
