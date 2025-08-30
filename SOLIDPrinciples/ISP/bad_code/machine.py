from abc import ABC, abstractmethod
from document import Document

class Machine(ABC):
    @abstractmethod
    def print_doc(doc: Document):
        pass

    @abstractmethod
    def scan_doc(doc: Document):
        pass

    @abstractmethod
    def copy_doc(doc: Document):
        pass