"""
The Legacy class that provides weather data in XML format.
"""
from weather_service import WeatherSerivce

class LegacyWeatherService(WeatherSerivce):
    def __init__(self, temperature, condititon):
        self.temperature = temperature
        self.condition = condititon

    def get_weather_data(self):
        data = f"""
            <weather>
                <temperature>{self.temperature}</temperature>
                <condition>{self.condition}</condition>
            </weather>
        """.strip()
        return data