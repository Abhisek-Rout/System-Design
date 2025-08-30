"""
This class implements the TextFormatter interface to format text as plain text.
"""

from text_formatter import TextFormatter

class PlainTextFormatter(TextFormatter):
    def format(self, text: str) -> str:
        # Return the input text without any formatting.
        return text