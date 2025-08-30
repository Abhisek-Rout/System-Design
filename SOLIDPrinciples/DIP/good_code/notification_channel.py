from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    def send(self, msg: str):
        pass