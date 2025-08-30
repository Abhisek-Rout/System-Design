"""
This class manages the formatting process of a document using various text formatting strategies.
"""
from document import Document
from plain_text_formatter import PlainTextFormatter
from html_formatter import HtmlTextFormatter
from markdown_formatter  import MarkdownTextFormatter

class Exercise:
    def main(self):
        # Initialise a document
        document: Document = Document()
        
        # Enter the content
        text = input("Write your text: ")

        # Set the content
        document.content = text

        # Set the formatter to Plaintext
        document.set_formatter(PlainTextFormatter())
        print("Plain text:")
        document.display()

        # Set the formatter to HTML
        document.set_formatter(HtmlTextFormatter())
        print("HTML text:")
        document.display()

        # Set the formatter to Markdown
        document.set_formatter(MarkdownTextFormatter())
        print("Markdown text:")
        document.display()


if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()