"""
This class acts as a remote control, allowing the execution of commands for controlling devices like lights and fans.
"""
from command import Command

class RemoteControl:
    def set_light_on_command(self, command: Command):
        self.light_on_command: Command = command

    def set_light_off_command(self, command: Command):
        self.light_off_command: Command = command

    def set_fan_on_command(self, command: Command):
        self.fan_on_command: Command = command

    def set_fan_off_command(self, command: Command):
        self.fan_off_command: Command = command

    def press_light_on_button(self):
        if self.light_on_command:
            self.light_on_command.execute()

    def press_light_off_button(self):
        if self.light_off_command:
            self.light_off_command.execute()

    def press_fan_on_button(self):
        if self.fan_on_command:
            self.fan_on_command.execute()

    def press_fan_off_button(self):
        if self.fan_off_command:
            self.fan_off_command.execute()