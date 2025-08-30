from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_doc(self):
        pass