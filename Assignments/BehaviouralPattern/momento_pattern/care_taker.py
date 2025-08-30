"""
The CareTaker class manages the history of shape states, allowing for saving and undoing changes in the Momento pattern
"""
from typing import List

from editor_momento import EditorMomento
from graphic_editor import GraphicEditor

class CareTaker:
    def __init__(self):
        self.__history: List[EditorMomento] = list()

    def save_state(self, momento: EditorMomento):
        """
        Save the current state of the graphic editor by pushing its momento into the history stack
        """
        self.__history.append(momento)

    def undo(self, graphic_editor: GraphicEditor):
        """
        Restore the last saved state of the graphic editor if history is not empty.
        """
        if len(self.__history) != 0:
            self.__history.pop()
            graphic_editor.restore(self.__history[-1])