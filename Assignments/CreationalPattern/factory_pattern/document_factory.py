"""
This factory class is responsible for creating instances of different document types.
"""
from document import Document
from pdf_document import PdfDocument
from html_document import HtmlDocument
from word_document import WordDocument

class DocumentFactory:
    @staticmethod
    def create_document(type: str) -> Document:
        match type.lower():
            case "pdf":
                return PdfDocument()
            case "word":
                return WordDocument()
            case "html":
                return HtmlDocument()
            case _:
                raise ValueError(f"Unsupported document type: {type}")