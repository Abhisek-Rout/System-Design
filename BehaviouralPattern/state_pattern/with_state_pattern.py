from abc import ABC, abstractmethod

# Create a contract
class TransportationMode(ABC):
    def calc_eta(self) -> int:
        pass

    def get_directions(self) -> str:
        pass

# Here are the concrete classes that implements above contract
class Walking(TransportationMode):
    def calc_eta(self)->int:
        print("Calculating the ETA for walking")
        return 10
    
    def get_directions(self)->str:
        return "Directions for walking"
    

class Cycling(TransportationMode):
    def calc_eta(self)->int:
        print("Calculating the ETA for cycling")
        return 5
    
    def get_directions(self)->str:
        return "Directions for cycling"
    

class Train(TransportationMode):
    def calc_eta(self)->int:
        print("Calculating the ETA for train")
        return 12
    
    def get_directions(self)->str:
        return "Directions for train"
    

class Car(TransportationMode):
    def calc_eta(self)->int:
        print("Calculating the ETA for Car")
        return 15
    
    def get_directions(self)->str:
        return "Directions for Car"
    

class DirectionService:
    def __init__(self, transportation_mode: TransportationMode):
        self.__transportation_mode: TransportationMode = transportation_mode
    
    @property
    def transportation_mode(self):
        return self.__transportation_mode
    
    @transportation_mode.setter
    def transportation_mode(self, mode: TransportationMode):
        self.__transportation_mode = mode

    # Delegating the work to the current state concrete class
    def get_eta(self)->int:
        return self.transportation_mode.calc_eta()
    
    # Delegating the work to the current state concrete class
    def get_directions(self)->str:
        return self.transportation_mode.get_directions()
    

class WithStatePattern:
    def main(self):
        service: DirectionService = DirectionService(Car())
        service.transportation_mode = Cycling()

        print(f"ETA {service.get_eta()}")
        print(f"Direction {service.get_directions()}")

if __name__ == "__main__":
    obj: WithStatePattern = WithStatePattern()
    obj.main()