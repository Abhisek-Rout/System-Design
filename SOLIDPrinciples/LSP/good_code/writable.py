from abc import ABC, abstractmethod

class Writable:
    @abstractmethod
    def write(self):
        pass