"""
The GrpahicEditor class manages the properties of shapes and provides functionality to save and restore their state using the Momento pattern
"""
from editor_momento import EditorMomento

class GraphicEditor:
    def save(self) -> EditorMomento:
        """
        Create and return a new momento that captures the current state of the shape attribute
        """
        momento: EditorMomento = EditorMomento(
                                    self.__shape_type,
                                    self.__x,
                                    self.__y,
                                    self.__color,
                                    self.__size
                                )
        return momento

    def restore(self, momento: EditorMomento):
        """
        Restore the shape attributes from the provided momento, updating the graphic editor's state
        """
        self.set_shape(
            momento.shape_type,
            momento.x,
            momento.y,
            momento.color,
            momento.size
        )

    def get_shape(self):
        return f"""Shape: {self.__shape_type}
                , Position: ({self.__x}, {self.__y})
                , Color: {self.__color}
                , Size: {self.__size}
                """
    
    def set_shape(self, shape_type: str, x: int, y: int, color: str, size: int):
        self.__shape_type = shape_type
        self.__x = x
        self.__y = y
        self.__color = color
        self.__size = size