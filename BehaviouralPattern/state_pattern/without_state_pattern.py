from enum import Enum, auto

class TransportationMode(Enum):
    WALKING = auto()
    CYCLING = auto()
    CAR = auto()
    TRAIN = auto()

class DirectionService:
    def __init__(self, transport_mode: TransportationMode):
        self.__transport_mode: TransportationMode = transport_mode

    @property
    def transport_mode(self):
        return self.__transport_mode

    @transport_mode.setter
    def transport_mode(self, transport_mode: TransportationMode):
        self.__transport_mode: TransportationMode = transport_mode

    

    # Method to calculate ETA based upon transportation Mode
    def get_eta(self) -> int:
        match self.transport_mode:
            case TransportationMode.WALKING:
                print("Calc ETA for walking")
                return 20
            case TransportationMode.CYCLING:
                print("Calc ETA for cycling")
                return 15
            case TransportationMode.CAR:
                print("Calc ETA for car")
                return 10
            case TransportationMode.TRAIN:
                print("Calc ETA for train")
                return 13
            case _:
                raise ValueError("Invalid operation")
            
    def get_directions(self) -> str:
        match self.transport_mode:
            case TransportationMode.WALKING:
                return "Directions for walking: Head north for 500 meters"
            case TransportationMode.CYCLING:
                return "Directions for cycling: Take the lane on Elm Street"
            case TransportationMode.CAR:
                return "Directions for driving: Use highway 50 towards downtown"
            case TransportationMode.TRAIN:
                return "Directions for train: Board the Red Line at Central Station"
            case _:
                return "No directions available for the selected mode."
            
class WithoutStatePattern:
    def main(self):
        direction_service: DirectionService = DirectionService(TransportationMode.TRAIN)
        direction_service.transport_mode = TransportationMode.CYCLING

        print(direction_service.get_directions())
        print(direction_service.get_eta())

if __name__ == "__main__":
    WithoutStatePattern().main()

