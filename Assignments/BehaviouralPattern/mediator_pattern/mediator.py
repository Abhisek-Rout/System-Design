"""
This interface defines the contract for the mediator responsible for managing airplane communication and requests for takeoff and landing.
"""
from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def register_airplane(airplane):
        pass
    
    @abstractmethod
    def handle_take_off_request(airplane):
        pass
    
    @abstractmethod
    def handle_landing_request(airplane):
        pass
    
    @abstractmethod
    def notify_takeoff_complete(airplane):
        pass

    @abstractmethod
    def notify_landing_complete(airplane):
        pass