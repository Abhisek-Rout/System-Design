from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Car(Transport):
    def deliver(self):
        print("Deliver by Car")

class Bike(Transport):
    def deliver(self):
        print("Deliver by bike")

# Add new transport
class Bus(Transport):
    def deliver(self):
        print("Deliver by Bus")

class TransportFactory:
    @staticmethod
    def create_transport(type: str):
        match type.lower():
            case "car":
                return Car()
            case "bike":
                return Bike()
            case "bus":
                return Bus()
            case _:
                raise ValueError("Unsupported transport type")


class TransportService:
    def main(self):
        # Direct create objects
        # Factory objects here can change dynamically at runtime just by changing the parameter like car, bike and bus
        car: Transport = TransportFactory.create_transport("car")
        bike: Transport = TransportFactory.create_transport("bike")
        bus: Bus = TransportFactory.create_transport("bus")

        car.deliver()
        bike.deliver()
        bus.deliver()

if __name__ == "__main__":
    obj: TransportService = TransportService()
    obj.main()

