import os
from dotenv import load_dotenv
from src.infrastructure.weather_client import WeatherClient
from src.application.agent import HealthAgent
import requests

load_dotenv()

def main():
    
    w_client = WeatherClient(os.getenv("OPENWEATHER_API_KEY"))
    agent = HealthAgent(os.getenv("GROQ_API_KEY"))
    # Prueba manual rápida
    prueba = requests.get(f"https://api.openweathermap.org/data/2.5/air_pollution?lat=39.46&lon=-0.37&appid={os.getenv('OPENWEATHER_API_KEY')}")
    print(f"DEBUG: Status Code recibido: {prueba.status_code}")
    print(f"DEBUG: Contenido crudo: {prueba.text}")
    # Valencia capital
    
    data = w_client.get_data("Valencia", 39.46, -0.37)
    report = agent.analyze(data)

    print(f"\n--- REPORTE PARA {report.city} ---")
    print(f"Estado: {report.aqi_description}")
    print(f"Consejo: {report.recommendation}")

if __name__ == "__main__":
    main()