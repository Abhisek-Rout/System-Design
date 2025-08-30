from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    
    @abstractmethod
    def pay(self):
        pass