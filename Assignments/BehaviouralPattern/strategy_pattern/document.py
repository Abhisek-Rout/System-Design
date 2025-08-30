"""
This class represents a document that can have its content formatted using different strategies.
"""
from text_formatter import TextFormatter

class Document:
    def __init__(self):
        self.__content: str = ""

    @property
    def content(self):
        return self.__content
    
    @content.setter
    def content(self, incoming_content: str):
        self.__content = incoming_content

    def set_formatter(self, formatter: TextFormatter):
        self.__formatter: TextFormatter = formatter


    def display(self):
        # Print the formatted content using the chosen formatter.
        print(self.__formatter.format(self.content))