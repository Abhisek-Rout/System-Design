"""
This interface defines the behavior for cloning and displaying attributes of character objects.
"""
from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def clone(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass