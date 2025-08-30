"""
This class represents an airplane that interacts with the Control Tower mediator for takeoff and landing requests.
"""
from mediator import Mediator

class Airplane:
    def __init__(self, id: str):
        self.__id: str = id

    def set_mediator(self, mediator: Mediator):
        self.__mediator = mediator

    @property
    def id(self):
        return self.__id
    
    @property
    def mediator(self):
        return self.__mediator

    def request_take_off(self):
        print(f"Airplane {self.id} requesting takeoff")
        # Notify the mediator to handle the takeoff request for this airplane
        self.mediator.handle_take_off_request(self)

    def request_landing(self):
        print(f"Airplane {self.id} requesting landing")
        # Notify the mediator to handle the landing request for this airplane
        self.mediator.handle_landing_request(self)

    def complete_takeoff(self):
        print(f"Airplane {self.id} has taken off")
        self.mediator.notify_takeoff_complete(self)

    def complete_landing(self):
        print(f"Airplane {self.id} has landed")

    def receive_notification(self, message: str):
        print(f"Airplane {self.id} : {message}")

    