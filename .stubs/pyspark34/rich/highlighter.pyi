import abc
from .text import Span as Span, Text as Text
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import List

class Highlighter(ABC, metaclass=abc.ABCMeta):
    """Abstract base class for highlighters."""
    def __call__(self, text: str | Text) -> Text:
        """Highlight a str or Text instance.

        Args:
            text (Union[str, ~Text]): Text to highlight.

        Raises:
            TypeError: If not called with text or str.

        Returns:
            Text: A test instance with highlighting applied.
        """
    @abstractmethod
    def highlight(self, text: Text) -> None:
        """Apply highlighting in place to text.

        Args:
            text (~Text): A text object highlight.
        """

class NullHighlighter(Highlighter):
    """A highlighter object that doesn't highlight.

    May be used to disable highlighting entirely.

    """
    def highlight(self, text: Text) -> None:
        """Nothing to do"""

class RegexHighlighter(Highlighter):
    """Applies highlighting from a list of regular expressions."""
    highlights: List[str]
    base_style: str
    def highlight(self, text: Text) -> None:
        """Highlight :class:`rich.text.Text` using regular expressions.

        Args:
            text (~Text): Text to highlighted.

        """

class ReprHighlighter(RegexHighlighter):
    """Highlights the text typically produced from ``__repr__`` methods."""
    base_style: str
    highlights: Incomplete

class JSONHighlighter(RegexHighlighter):
    """Highlights JSON"""
    JSON_STR: str
    JSON_WHITESPACE: Incomplete
    base_style: str
    highlights: Incomplete
    def highlight(self, text: Text) -> None: ...

class ISO8601Highlighter(RegexHighlighter):
    """Highlights the ISO8601 date time strings.
    Regex reference: https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s07.html
    """
    base_style: str
    highlights: Incomplete
