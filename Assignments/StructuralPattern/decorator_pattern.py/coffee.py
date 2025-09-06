"""
This interface defines the contract for Coffee objects, requiring methods for obtaining the description and cost.
"""
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_cost(self):
        pass