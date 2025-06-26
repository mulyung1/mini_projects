# main.py
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from math import radians, sin, cos, sqrt, asin
import uvicorn

app = FastAPI()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Geofence configuration (lat, lng, radius_m)
GEOFENCES = [
    (-1.2615, 36.85744, 100),   # Juja (100m)
    (34.0522, -118.2437, 500),   # Los Angeles (500m)
    (40.7128, -74.0060, 200),    # New York (200m)
]

class LocationRequest(BaseModel):
    latitude: float
    longitude: float

def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """Calculate great-circle distance in meters"""
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    return 2 * 6371000 * asin(sqrt(a))  # Earth radius in meters

#radius = 100
def check_in_geofence(user_lat: float, user_lon: float) -> bool:
    """Check if user is within any geofence"""
    for lat, lng, radius in GEOFENCES:
        if haversine(user_lon, user_lat, lng, lat) <= radius:
            return True
    return False

@app.post("/verify-location")
async def verify_location(location: LocationRequest):
    """Verify if user is in allowed zone"""
    access = check_in_geofence(location.latitude, location.longitude)
    return {"access_granted": access}

@app.get("/", response_class=HTMLResponse)
async def map_page(request: Request):
    """Serve map page with geofencing"""
    # Pass geofence data to frontend
    geojson_zones = [
        {
            "type": "circle",
            "lat": lat,
            "lng": lng,
            "radius": radius,
            "color": "#3388ff"
        } for lat, lng, radius in GEOFENCES
    ]
    return templates.TemplateResponse(
        "map.html",
        {
            "request": request,
            "geojson_zones": geojson_zones,
            "initial_center": GEOFENCES[0][0:2] if GEOFENCES else [0, 0]
        }
    )


# Add this route to handle the missing file request
@app.get("/installHook.js.map")
async def ignore_install_hook():
    """Handle missing source map requests from React DevTools"""
    return {'resp':'status_code=204'}  # No Content response

