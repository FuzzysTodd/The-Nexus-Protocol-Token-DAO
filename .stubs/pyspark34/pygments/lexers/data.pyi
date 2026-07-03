from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import ExtendedRegexLexer, Lexer, LexerContext

__all__ = ['YamlLexer', 'JsonLexer', 'JsonBareObjectLexer', 'JsonLdLexer']

class YamlLexerContext(LexerContext):
    """Indentation context for the YAML lexer."""
    indent_stack: Incomplete
    indent: int
    next_indent: int
    block_scalar_indent: Incomplete
    def __init__(self, *args, **kwds) -> None: ...

class YamlLexer(ExtendedRegexLexer):
    """
    Lexer for YAML, a human-friendly data serialization
    language.

    .. versionadded:: 0.11
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def something(token_class):
        """Do not produce empty tokens."""
    def reset_indent(token_class):
        """Reset the indentation levels."""
    def save_indent(token_class, start: bool = False):
        """Save a possible indentation level."""
    def set_indent(token_class, implicit: bool = False):
        """Set the previously saved indentation level."""
    def set_block_scalar_indent(token_class):
        """Set an explicit indentation level for a block scalar."""
    def parse_block_scalar_empty_line(indent_token_class, content_token_class):
        """Process an empty line in a block scalar."""
    def parse_block_scalar_indent(token_class):
        """Process indentation spaces in a block scalar."""
    def parse_plain_scalar_indent(token_class):
        """Process indentation spaces in a plain scalar."""
    tokens: Incomplete
    def get_tokens_unprocessed(self, text: Incomplete | None = None, context: Incomplete | None = None): ...

class JsonLexer(Lexer):
    """
    For JSON data structures.

    Javascript-style comments are supported (like ``/* */`` and ``//``),
    though comments are not part of the JSON specification.
    This allows users to highlight JSON as it is used in the wild.

    No validation is performed on the input JSON document.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    integers: Incomplete
    floats: Incomplete
    constants: Incomplete
    hexadecimals: Incomplete
    punctuations: Incomplete
    whitespaces: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]:
        """Parse JSON data."""

class JsonBareObjectLexer(JsonLexer):
    """
    For JSON data structures (with missing object curly braces).

    .. versionadded:: 2.2

    .. deprecated:: 2.8.0

       Behaves the same as `JsonLexer` now.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete

class JsonLdLexer(JsonLexer):
    """
    For JSON-LD linked data.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    json_ld_keywords: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
