from .base import StyleAndTextTuples
from _typeshed import Incomplete
from string import Formatter

__all__ = ['ANSI', 'ansi_escape']

class ANSI:
    """
    ANSI formatted text.
    Take something ANSI escaped text, for use as a formatted string. E.g.

    ::

        ANSI('\\x1b[31mhello \\x1b[32mworld')

    Characters between ``\\001`` and ``\\002`` are supposed to have a zero width
    when printed, but these are literally sent to the terminal output. This can
    be used for instance, for inserting Final Term prompt commands.  They will
    be translated into a prompt_toolkit '[ZeroWidthEscape]' fragment.
    """
    value: Incomplete
    def __init__(self, value: str) -> None: ...
    def __pt_formatted_text__(self) -> StyleAndTextTuples: ...
    def format(self, *args: str, **kwargs: str) -> ANSI:
        """
        Like `str.format`, but make sure that the arguments are properly
        escaped. (No ANSI escapes can be injected.)
        """
    def __mod__(self, value: object) -> ANSI:
        """
        ANSI('<b>%s</b>') % value
        """

def ansi_escape(text: object) -> str:
    """
    Replace characters with a special meaning.
    """

class ANSIFormatter(Formatter):
    def format_field(self, value: object, format_spec: str) -> str: ...
