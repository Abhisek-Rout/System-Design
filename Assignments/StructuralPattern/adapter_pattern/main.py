"""
This class demonstrates the usage of different weather services through the Adapter pattern.
"""
from weather_service import WeatherSerivce
from legacy_weather_service import LegacyWeatherService
from new_weather_service_adapter import NewWeatherServiceAdapter
from new_weather_service import NewWeatherService

class Exercise:
    def main(self):
        legacy_temp = input("Enter legacy temp: ")
        legacy_condtion = input("Enter legacy condition: ")
        legacy_service: WeatherSerivce = LegacyWeatherService(legacy_temp, legacy_condtion)
        print("Legacy Weather Service Data: ")
        print(legacy_service.get_weather_data())

        new_temp = input("Enter new temp: ")
        new_condtion = input("Enter new condition: ")
        adapted_service = NewWeatherServiceAdapter(NewWeatherService(new_temp, new_condtion))
        print("New Weather Service Data: ")
        print(adapted_service.get_weather_data())


if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()