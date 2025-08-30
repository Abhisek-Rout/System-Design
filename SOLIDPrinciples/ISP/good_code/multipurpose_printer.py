from printer import Printer
from copier import Copier
from scanner import Scanner

class MultiPurposePrinter(Printer, Copier, Scanner):
    def print_doc(doc):
        print("Printing a document")

    def scan_doc(doc):
        print("Scanning a document")

    def copy_doc(doc):
        print("Copying a document")