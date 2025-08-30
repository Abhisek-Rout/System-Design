"""
This class implements the TextFormatter interface to format text using Markdown syntax.
"""

from text_formatter import TextFormatter

class MarkdownTextFormatter(TextFormatter):
    def format(self, text: str) -> str:
        # Wrap the input text in Markdown syntax: "**" and "**".
        return f"**{text}**"