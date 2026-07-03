from .emoji import EmojiVariant as EmojiVariant
from .errors import MarkupError as MarkupError
from .style import Style as Style
from .text import Span as Span, Text as Text
from _typeshed import Incomplete
from typing import NamedTuple

RE_TAGS: Incomplete
RE_HANDLER: Incomplete

class Tag(NamedTuple):
    """A tag in console markup."""
    name: str
    parameters: str | None
    @property
    def markup(self) -> str:
        """Get the string representation of this tag."""

def escape(markup: str, _escape: _EscapeSubMethod = ...) -> str:
    """Escapes text so that it won't be interpreted as markup.

    Args:
        markup (str): Content to be inserted in to markup.

    Returns:
        str: Markup with square brackets escaped.
    """
def render(markup: str, style: str | Style = '', emoji: bool = True, emoji_variant: EmojiVariant | None = None) -> Text:
    """Render console markup in to a Text instance.

    Args:
        markup (str): A string containing console markup.
        emoji (bool, optional): Also render emoji code. Defaults to True.

    Raises:
        MarkupError: If there is a syntax error in the markup.

    Returns:
        Text: A test instance.
    """
