"""
The PausedState class represents the playing state of the Media Player.
"""
from state import State

class PausedState(State):
    def press_play(self):
        print("Resuming playback")

    def press_stop(self):
        print("Stopping playback from pause")

    def press_pause(self):
        print("Pausing playback")

    def display(self):
        print("Current State: Paused")