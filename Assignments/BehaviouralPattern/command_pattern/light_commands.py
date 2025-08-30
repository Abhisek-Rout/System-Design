"""
This class contains command implementations for controlling the light, including turning it on and off.
"""
from command import Command
from light import Light

class LightCommands:
    class LightOnCommands(Command):
        def __init__(self, light):
            self.light: Light =  light

        def execute(self):
            return self.light.turn_on()
        

    class LightOffCommands(Command):
        def __init__(self, light):
            self.light: Light = light

        def execute(self):
            return self.light.turn_off()