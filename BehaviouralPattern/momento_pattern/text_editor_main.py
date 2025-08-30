from text_editor import TextEditor
from care_taker import CareTaker

class TextEditorMain:
    def main(self):
        editor: TextEditor = TextEditor()
        care_taker: CareTaker = CareTaker()

        editor.write("A")
        care_taker.save_state(editor)

        editor.write("B")
        care_taker.save_state(editor)

        editor.write("C")
        care_taker.save_state(editor)

        care_taker.undo(editor)

        print(editor.get_content())

if __name__ == "__main__":
    text_editor_main: TextEditorMain = TextEditorMain()
    text_editor_main.main()

