"""
This abstract class represents the structure for various document types.
"""
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def display_type(self):
        pass