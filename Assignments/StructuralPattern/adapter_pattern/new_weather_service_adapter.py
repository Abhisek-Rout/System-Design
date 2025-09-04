"""
The Adapter class that adapts the new weather service to the WeatherService interface.
"""
from weather_service import WeatherSerivce
from new_weather_service import NewWeatherService

class NewWeatherServiceAdapter(WeatherSerivce):
    def __init__(self, new_weather_service: NewWeatherService):
        self.weather_service = new_weather_service

    def get_weather_data(self):
        weather_data = self.weather_service.fetch_weather()
        weather_data_formatted = f"""
            <weather>
                <temperature>{weather_data.get('temperature')}</temperature>
                <condition>{weather_data.get('condition')}</condition>
            </weather>
        """.strip()
        return weather_data_formatted