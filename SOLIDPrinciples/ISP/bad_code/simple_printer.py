from machine import Machine

class SimplePrinter(Machine):
    def print_doc(doc):
        print("Printing a document")

    def scan_doc(doc):
        raise NotImplementedError("Does not support document scan")
    
    def copy_doc(doc):
        raise NotImplementedError("Does not support copying of document")