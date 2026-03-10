import requests
from src.domain.models import AirQualityData

class WeatherClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/air_pollution"

    def get_data(self, city_name: str, lat: float, lon: float) -> AirQualityData:
        url = f"{self.base_url}?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()['list'][0]
        
        return AirQualityData(
            city=city_name,
            aqi=data['main']['aqi'],
            no2=data['components']['no2'],
            o3=data['components']['o3']
        )