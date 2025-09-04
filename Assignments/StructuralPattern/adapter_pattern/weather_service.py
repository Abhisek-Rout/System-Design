"""
This interface defines a consistent contract for retrieving weather data from various weather services.
"""
from abc import ABC, abstractmethod

class WeatherSerivce:
    @abstractmethod
    def get_weather_data(self):
        pass