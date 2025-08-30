from abc import ABC, abstractmethod

# Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class TextEditor:
    def bold_text(self):
        print("Text has been bolded")

    def italicize_text(self):
        print("Text has been itlicized")

    def underine_text(self):
        print("Text has been underlined")

# Concrete classes for commands
class BoldCommand(Command):
    def __init__(self, editor: TextEditor):
        self.editor = editor

    def execute(self):
        return self.editor.bold_text()

class ItalicCommand(Command):
    def __init__(self, editor: TextEditor):
        self.editor = editor

    def execute(self):
        return self.editor.italicize_text()
    
class UnderlineCommand(Command):
    def __init__(self, editor: TextEditor):
        self.editor = editor

    def execute(self):
        return self.editor.underine_text()


class Button:
    def __init__(self):
        self.__command = None

    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, input_command):
        self.__command = input_command

    def click(self):
        self.command.execute()

    
class CommandPattern:
    def main(self):
        # Initialize text editor
        editor = TextEditor()

        # Initialize the commands
        button: Button = Button()
        button.command = BoldCommand(editor)
        button.click()

        button.command = ItalicCommand(editor)
        button.click()

        button.command = UnderlineCommand(editor)
        button.click()


if __name__ == "__main__":
    obj: CommandPattern = CommandPattern()
    obj.main()
