from pydantic import BaseModel
from typing import Optional

class AirQualityData(BaseModel):
    city: str
    aqi: int
    no2: float
    o3: float

class HealthReport(BaseModel):
    city: str
    aqi_description: str
    recommendation: str