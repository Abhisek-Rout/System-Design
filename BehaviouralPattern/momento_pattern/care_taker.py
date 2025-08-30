from text_editor import TextEditor

class CareTaker:
    def __init__(self):
        self.__history = list()

    def save_state(self, editor: TextEditor):
        self.__history.append(editor.save())

    def undo(self, editor: TextEditor):
        if self.__history:
            self.__history.pop()
            editor.restore(self.__history[-1])