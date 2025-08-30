"""
A text editor where the user can undo changes, such as text addition, deletion,
or formatting. The editor stores snapshots of its state (text content)
after each change, enabling the user to revert to previous states.
"""
from editor_momento  import EditorMomento

class TextEditor:
    def write(self, text:str):
        self.__content = text

    def get_content(self) -> str:
        return self.__content
    
    def save(self) -> EditorMomento:
        return EditorMomento(self.__content)
    
    def restore(self, momento: EditorMomento):
        self.__content = momento.get_content()