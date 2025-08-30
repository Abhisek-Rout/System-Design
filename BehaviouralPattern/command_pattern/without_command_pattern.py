class TextEditor:
    def bold_text(self):
        print("Text has been bolded")

    def italicize_text(self):
        print("Text has been itlicized")

    def underine_text(self):
        print("Text has been underlined")


# UI Button class
class BoldButton:
    def __init__(self, editor: TextEditor):
        self.editor: TextEditor = editor

    def click(self):
        self.editor.bold_text()

class ItalicButton:
    def __init__(self, editor: TextEditor):
        self.editor: TextEditor = editor

    def click(self):
        self.editor.italicize_text()


class UnderLineButton:
    def __init__(self, editor: TextEditor):
        self.editor:TextEditor = editor

    def click(self):
        self.editor.underine_text()


class WithoutCommandPattern:
    def main(self):
        # Inititalize the text editor
        text_editor: TextEditor = TextEditor()

        # Initialize all the buttom
        # Here u can observe tight coupling between editor and the button
        bold_button: BoldButton = BoldButton(text_editor)
        bold_button.click()

        italic_button: ItalicButton = ItalicButton(text_editor)
        italic_button.click()

        underline_button: UnderLineButton = UnderLineButton(text_editor)
        underline_button.click()


if __name__ == "__main__":
    obj: WithoutCommandPattern = WithoutCommandPattern()
    obj.main()
