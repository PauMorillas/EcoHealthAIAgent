from groq import Groq
from src.domain.models import AirQualityData, HealthReport

class HealthAgent:
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

    def analyze(self, data: AirQualityData) -> HealthReport:
        descriptions = {1: "Excelente", 2: "Aceptable", 3: "Baja", 4: "Mala", 5: "Muy peligrosa"}
        status = descriptions.get(data.aqi, "Desconocido")

        prompt = f"Calidad del aire en {data.city}: {status}. NO2: {data.no2}. Da un consejo de salud corto para asmáticos."
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        
        return HealthReport(
            city=data.city,
            aqi_description=status,
            recommendation=completion.choices[0].message.content
        )