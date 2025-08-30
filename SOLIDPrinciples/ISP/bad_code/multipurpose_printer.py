from machine import Machine

class MultiPurposePrinter(Machine):
    def print_doc(doc):
        print("Printing a document")

    def scan_doc(doc):
        print("Scanning a document")

    def copy_doc(doc):
        print("Copying a document")