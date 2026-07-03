from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import ExtendedRegexLexer, Lexer, RegexLexer

__all__ = ['RubyLexer', 'RubyConsoleLexer', 'FancyLexer']

class RubyLexer(ExtendedRegexLexer):
    """
    For Ruby source code.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    def heredoc_callback(self, match, ctx) -> Generator[Incomplete, Incomplete, None]: ...
    def gen_rubystrings_rules(): ...
    tokens: Incomplete
    def analyse_text(text): ...

class RubyConsoleLexer(Lexer):
    """
    For Ruby interactive console (**irb**) output.
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...

class FancyLexer(RegexLexer):
    """
    Pygments Lexer For Fancy.

    Fancy is a self-hosted, pure object-oriented, dynamic,
    class-based, concurrent general-purpose programming language
    running on Rubinius, the Ruby VM.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
