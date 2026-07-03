from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['ArturoLexer']

class ArturoLexer(RegexLexer):
    """
    For Arturo source code.

    See `Arturo's Github <https://github.com/arturo-lang/arturo>`_
    and `Arturo's Website <https://arturo-lang.io/>`_.

    .. versionadded:: 2.14.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    url: str
    handle_annotateds: Incomplete
    def __init__(self, **options) -> None: ...
    def handle_annotated_strings(self, match) -> Generator[Incomplete, Incomplete, None]:
        """Adds syntax from another languages inside annotated strings

        match args:
            1:open_string,
            2:exclamation_mark,
            3:lang_name,
            4:space_or_newline,
            5:code,
            6:close_string
        """
    tokens: Incomplete
