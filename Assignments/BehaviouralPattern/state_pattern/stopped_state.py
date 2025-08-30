"""
The StoppedState class represents the playing state of the Media Player. 
"""

from state import State

class StoppedState(State):
    def press_play(self):
        print("Starting playback")

    def press_stop(self):
        print("Stopping playback")

    def press_pause(self):
        print("Can't pause. Media is already stopped")

    def display(self):
        print("Curent State: Stopped")