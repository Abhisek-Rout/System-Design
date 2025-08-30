"""
The PlayingState class represents the playing state of the Media Player. 
"""
from state import State

class PlayingState(State):
    def press_play(self):
        print("Starting playback")

    def press_stop(self):
        print("Stopping playback")

    def press_pause(self):
        print("Pausing playback")

    def display(self):
        print("Current State: Playing")
