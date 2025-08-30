"""
The EditorMomento class stores the state of a shape, allowing for the preservation and restoration of its attributes in the moemento pattern
"""

class EditorMomento:
    def __init__(self, shape_type: str, x: int, y: int, color: str, size: int):
        self.__shape_type = shape_type
        self.__x = x
        self.__y = y
        self.__color = color
        self.__size = size

    @property
    def shape_type(self):
        return self.__shape_type
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def color(self):
        return self.__color
    
    @property
    def size(self):
        return self.__size

