"""
This class represents a Word document type.
"""
from document import Document

class WordDocument(Document):
    def display_type(self):
        print("Creating a Word document")