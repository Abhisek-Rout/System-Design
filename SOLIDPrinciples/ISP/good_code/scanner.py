from abc import ABC, abstractmethod

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self):
        pass