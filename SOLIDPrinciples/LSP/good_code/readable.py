from abc import ABC, abstractmethod

class Readable:
    @abstractmethod
    def read(self):
        pass