"""
This class implements the TextFormatter interface to format the text as HTML.
"""

from text_formatter import TextFormatter

class HtmlTextFormatter(TextFormatter):
    def format(self, text: str) -> str:
        # Wrap the input text in HTML tags: "<html><body>" and "</body></html>".
        return f"<html><body>{text}</body></html>"