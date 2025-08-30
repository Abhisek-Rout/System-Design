class DisplayDevice:
    def show_temp(self, temp: float):
        print(f"Current temp: {temp} C")


class WeatherStation:
    def __init__(self, display_device: DisplayDevice):
        self.__temp = 0.0  # Initialize with default
        self.__display_device = display_device

    @property
    def temp(self):
        return self.__temp

    @temp.setter
    def temp(self, value):
        self.__temp = value
        self.notify_devices()
    
    def notify_devices(self):
        self.__display_device.show_temp(self.temp)


class WithoutObserverPattern:
    def main(self):
        self.device = DisplayDevice()
        self.station = WeatherStation(self.device)

        # Here there is tight coupling between the station and the device
        self.station.temp = 30
        self.station.temp = 40 # Temp set


if __name__ == "__main__":
    obj = WithoutObserverPattern()
    obj.main()
