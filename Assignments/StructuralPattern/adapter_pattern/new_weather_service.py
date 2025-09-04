"""
The New class that provides weather data in JSON format.
"""

class NewWeatherService:
    def __init__(self, temperature: str, condition: str):
        self.temperature = temperature
        self.condition = condition

    def fetch_weather(self):
        data = {
            "temperature": self.temperature,
            "condition": self.condition
        }
        return data