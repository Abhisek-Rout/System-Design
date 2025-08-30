"""
The State interface defines the methods for different states of the Media Player. 
"""
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def press_play(self):
        pass
    
    @abstractmethod
    def press_stop(self):
        pass
    
    @abstractmethod
    def press_pause(self):
        pass
    
    @abstractmethod
    def display(self):
        pass