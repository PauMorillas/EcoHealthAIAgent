from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from src.infrastructure.weather_client import WeatherClient
from src.infrastructure.geo_client import GeoClient
from src.application.agent import HealthAgent
import os
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles



load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Inicializamos una vez al arrancar la web
geo_service = GeoClient(os.getenv("OPENWEATHER_API_KEY"))
weather_service = WeatherClient(os.getenv("OPENWEATHER_API_KEY"))
ai_agent = HealthAgent(os.getenv("GROQ_API_KEY"))

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/report")
def get_report(city: str):
    lat, lon = geo_service.get_coords(city) 
    data = weather_service.get_data(city, lat, lon)
    report = ai_agent.analyze(data)
    return report # FastAPI convierte el modelo a JSON automáticamente