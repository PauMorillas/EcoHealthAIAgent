from pydantic import BaseModel
from typing import Optional

class AirQualityData(BaseModel):
    """
    Representa los datos técnicos de calidad del aire obtenidos de una API.
    Utilizamos estos parámetros para que la IA tenga contexto científico.
    """
    city: str
    aqi: int # Air Quality Index
    no2: float # Dióxido de Nitrógeno
    o3: float # Ozono Troposférico

class HealthReport(BaseModel):
    """
    Resultado procesado por la IA para el usuario final.
    """
    city: str
    aqi_description: str
    recommendation: str