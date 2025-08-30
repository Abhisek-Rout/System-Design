# This is a relationship where one class relies on another in some way, oftn through method
# parameters, return types or temporary associations.

class Document:
    def __init__(self, content):
        self.__content = content

    @property
    def content(self):
        return self.__content
    
class Printer:
    def print_doc(self, doc: Document):
        print(f"Printing content: {doc.content}")

class DependencyExample:
    def main(self):
        doc: Document = Document("Hi! I'm learning system design")
        printer: Printer = Printer()

        # Here the method parameters has been used to create an association between Printer and Docuement
        printer.print_doc(doc)

if __name__ == "__main__":
    depend_example: DependencyExample = DependencyExample()
    depend_example.main()