"""
This class serves as the mediator, managing communication and runway allocation between airplanes for takeoff and landing.
"""
from typing import List

from mediator import Mediator
from airplane import Airplane

class ControlTower(Mediator):
    def __init__(self):
        self.__airplanes: List[Airplane] = list()
        self.__takeoff_runways = 2
        self.__landing_runways = 2

    def register_airplane(self, airplane: Airplane):
        self.__airplanes.append(airplane)
        airplane.set_mediator(self)

    def notify_airplane(self, airplane: Airplane, message: str):
        airplane.receive_notification(message)

    def handle_take_off_request(self, airplane: Airplane):
        if self.__takeoff_runways > 0:
            self.__takeoff_runways -= 1
            self.notify_airplane(airplane, f"Takeoff approved. Runways available: {self.__takeoff_runways}")
        else:
            self.notify_airplane(airplane, "Takeoff denied. No runways available. Please wait")

    def handle_landing_request(self, airplane: Airplane):
        if self.__landing_runways > 0:
            self.__landing_runways -= 1
            self.notify_airplane(airplane, f"Landing approved. Runways available: {self.__landing_runways}")
        else:
            self.notify_airplane(airplane, "Landing denied. No runways available. Please wait")

    # Simulate the completion of takeoff and free the runway
    def notify_takeoff_complete(self, airplane: Airplane):
        self.__takeoff_runways += 1
        print(f"Runway freed. Available takeoff runways: {self.__takeoff_runways}")

    # Simulate the completion of landing and free the runway
    def notify_landing_complete(self, airplane: Airplane):
        self.__landing_runways += 1
        print(f"Runway freed. Available landing runways: {self.__landing_runways}")
        