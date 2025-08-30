from abc import ABC, abstractmethod

class Copier(ABC):
    @abstractmethod
    def copy_doc(self):
        pass