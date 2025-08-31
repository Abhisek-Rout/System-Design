"""
This class represents a PDF document type.
"""
from document import Document

class PdfDocument(Document):
    def display_type(self):
        print("Creating a PDF document.")