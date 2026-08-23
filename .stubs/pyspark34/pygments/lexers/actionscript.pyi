from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ActionScriptLexer', 'ActionScript3Lexer', 'MxmlLexer']

class ActionScriptLexer(RegexLexer):
    """
    For ActionScript source code.

    .. versionadded:: 0.9
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """This is only used to disambiguate between ActionScript and
        ActionScript3. We return 0 here; the ActionScript3 lexer will match
        AS3 variable definitions and that will hopefully suffice."""

class ActionScript3Lexer(RegexLexer):
    """
    For ActionScript 3 source code.

    .. versionadded:: 0.11
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    identifier: str
    typeidentifier: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class MxmlLexer(RegexLexer):
    """
    For MXML markup.
    Nested AS3 in <script> tags is highlighted by the appropriate lexer.

    .. versionadded:: 1.1
    """
    flags: Incomplete
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetimes: Incomplete
    tokens: Incomplete
