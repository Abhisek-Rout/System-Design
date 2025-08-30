"""
This interface defines a command that can be executed, requiring an implementation of the execute method.
"""

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass