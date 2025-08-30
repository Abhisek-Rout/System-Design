"""
This Interface defines a contract for text formatting strategies.
"""
from abc import ABC, abstractmethod

class TextFormatter:
    @abstractmethod
    def format(self, text: str):
        pass