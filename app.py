
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from projects.aq_nowcast.router import router as aq_router
from projects.flood_risk.router import router as flood_router
from projects.address_norm.router import router as addr_router
from projects.water_leak.router import router as water_router
from projects.school_vision.router import router as school_router

app = FastAPI(title="Market-Ready Suite", version="0.1.0")

app.mount("/static", StaticFiles(directory="demo/static"), name="static")
templates = Jinja2Templates(directory="demo/templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(aq_router)
app.include_router(flood_router)
app.include_router(addr_router)
app.include_router(water_router)
app.include_router(school_router)
