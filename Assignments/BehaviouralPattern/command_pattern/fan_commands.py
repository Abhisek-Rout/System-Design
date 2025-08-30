"""
This class contains command implementations for controlling the fan, including turning it on and off.
"""

from command import Command
from fan import Fan

class FanCommands:
    class FanOnCommands(Command):
        def __init__(self, fan):
            self.fan: Fan = fan

        def execute(self):
            # Override the execute() method from the Command interface and Implement the logic to turn on the fan when this command is executed.
            self.fan.turn_on()

    class FanOffCommans(Command):
        def __init__(self, fan):
            self.fan: Fan = fan

        def execute(self):
            # Override the execute() method from the Command interface and Implement the logic to turn off the fan when this command is executed.
            return self.fan.turn_off()