import requests

class GeoClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/geo/1.0/direct"

    def get_coords(self, city_name: str):
        params = {"q": city_name, "limit": 1, "appid": self.api_key}
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()
        if not data:
            raise ValueError("Ciudad no encontrada")
        return data[0]['lat'], data[0]['lon']