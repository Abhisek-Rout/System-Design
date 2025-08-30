from light import Light
from fan import Fan
from command import Command
from light_commands import LightCommands
from fan_commands import FanCommands
from remote_control import RemoteControl

class Exercise:
    def main(self):
        light: Light = Light()
        fan: Fan = Fan()

        # Create the commands
        light_on: Command = LightCommands.LightOnCommands(light)
        light_off: Command = LightCommands.LightOffCommands(light)

        fan_on: Command = FanCommands.FanOnCommands(fan)
        fan_off: Command = FanCommands.FanOffCommans(fan)

        # Create remote control
        # Instantiate the RemoteControl object to manage commands.
        remote_control: RemoteControl = RemoteControl()

        # Set the command for turning the light on using the LightOnCommand using remoteControl object.
        remote_control.set_light_on_command(light_on)
        
        # Set the command for turning off the light using LightOffCommand using remoteControl object.
        remote_control.set_light_off_command(light_off)
        
        # Set the command for turning on the fan using FanOnCommand using remoteControl object.
        remote_control.set_fan_on_command(fan_on)
        
        # Set the command for turning off the fan using FanOffCommand using remoteControl object.
        remote_control.set_fan_off_command(fan_off)


        # Test the functionality
        # Press the button to turn on the light and verify the output.
        remote_control.press_light_on_button()
        
        # Press the button to turn off the light and verify the output.
        remote_control.press_light_off_button()
        
        # Press the button to turn on the fan and verify the output.
        remote_control.press_fan_on_button()
        
        # Press the button to turn off the fan and verify the output.
        remote_control.press_fan_off_button()


if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()
