"""
This class handles the creation of document instances based on user input.
"""
from document_factory import DocumentFactory, Document

class Exercise:
    def main(self):
        document_type: str = input("Enter the document type: ")

        try:
            document: Document = DocumentFactory.create_document(document_type)
            document.display_type()
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()