"""
The Subject interface defines methods for registering, removing, and notifying observers about stock price changes.
"""
from abc import ABC, abstractmethod

from observer import Observer

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass
    
    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self, stock_symbol: str, new_price: float):
        pass
