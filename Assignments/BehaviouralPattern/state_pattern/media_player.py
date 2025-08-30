"""
The MediaPlayer class manages the current state of the Media Player using the State Design Pattern.
"""
from playing_state import PlayingState
from state import State

class MediaPlayer:
    def __init__(self):
        # Set the initial state of the Media Player to PlayingState
        self.__state = PlayingState()

    @property
    def state(self) -> State:
        return self.__state
    
    @state.setter
    def state(self, state_value: State):
        self.__state = state_value

    def play(self):
        # Implement the functionality for pressing play
        self.state.press_play()

    def stop(self):
        # Implement the functionality for pressing stop
        self.state.press_stop()

    def pause(self):
        # Implement the functionality for pressing pause
        self.state.press_pause()

    def display_sate(self):
        # Implement the functionality to display the current state
        self.state.display()
