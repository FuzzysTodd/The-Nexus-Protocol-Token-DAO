from .color import Color as Color
from .console import Console as Console
from .style import Style as Style
from .text import Text as Text
from _typeshed import Incomplete
from typing import Iterable, NamedTuple

re_ansi: Incomplete

class _AnsiToken(NamedTuple):
    """Result of ansi tokenized string."""
    plain: str = ...
    sgr: str | None = ...
    osc: str | None = ...

SGR_STYLE_MAP: Incomplete

class AnsiDecoder:
    """Translate ANSI code in to styled Text."""
    style: Incomplete
    def __init__(self) -> None: ...
    def decode(self, terminal_text: str) -> Iterable[Text]:
        """Decode ANSI codes in an iterable of lines.

        Args:
            lines (Iterable[str]): An iterable of lines of terminal output.

        Yields:
            Text: Marked up Text.
        """
    def decode_line(self, line: str) -> Text:
        """Decode a line containing ansi codes.

        Args:
            line (str): A line of terminal output.

        Returns:
            Text: A Text instance marked up according to ansi codes.
        """

decoder: Incomplete
stdout: Incomplete

def read(fd: int) -> bytes: ...

console: Incomplete
stdout_result: Incomplete
