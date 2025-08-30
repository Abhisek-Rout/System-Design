from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temp: float):
        pass


class Subject(ABC):
    @abstractmethod
    def attach_observer(self, obs: Observer):
        pass
    
    @abstractmethod
    def detach_observer(self, obs: Observer):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass


class WeatherStation(Subject):
    def __init__(self):
        self.__observer_list: list = list()

    def attach_observer(self, obs: Observer):
        self.__observer_list.append(obs)

    def detach_observer(self, obs: Observer):
        self.__observer_list.remove(obs)

    def set_temperature(self, temp: float):
        self.__temperature: float = temp
        self.notify_observers(self.__temperature)

    def notify_observers(self, temperature: float):
        for observer in self.__observer_list:
            observer.update(temperature)


class DisplayDevice(Observer):
    def __init__(self, device_name: str):
        self.name = device_name

    def update(self, temp):
        print(f"Temperatue on {self.name} is {temp}")


class MobileDevice(Observer):
    def __init__(self, device_name: str):
        self.name = device_name

    def update(self, temp):
        print(f"Temperatue on {self.name} is {temp}")


class ObserverPatternExample:
    def main(self):
        # Create a publisher
        weather_station: WeatherStation = WeatherStation()

        # Create subscribers
        display_device: DisplayDevice = DisplayDevice('LG Display LCD')
        mobile_device: MobileDevice = MobileDevice('Redmi mobile')

        # Attach the devices
        weather_station.attach_observer(display_device)
        weather_station.attach_observer(mobile_device)

        # set the temperature
        weather_station.set_temperature(20)
        weather_station.set_temperature(38)

if __name__ == "__main__":
    obj: ObserverPatternExample = ObserverPatternExample()
    obj.main()