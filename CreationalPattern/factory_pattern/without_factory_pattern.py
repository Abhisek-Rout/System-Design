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


class TransportService:
    def main(self):
        # Direct create objects
        car: Car = Car()
        bike: Bike = Bike()

        # Add a bus object
        bus: Bus = Bus()  # This is tight coupling between the transport and transport service

        car.deliver()
        bike.deliver()
        bus.deliver()

if __name__ == "__main__":
    obj: TransportService = TransportService()
    obj.main()

