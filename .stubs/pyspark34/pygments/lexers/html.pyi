from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import ExtendedRegexLexer, RegexLexer

__all__ = ['HtmlLexer', 'DtdLexer', 'XmlLexer', 'XsltLexer', 'HamlLexer', 'ScamlLexer', 'PugLexer', 'UrlEncodedLexer']

class HtmlLexer(RegexLexer):
    """
    For HTML 4 and XHTML 1 markup. Nested JavaScript and CSS is highlighted
    by the appropriate lexer.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class DtdLexer(RegexLexer):
    """
    A lexer for DTDs (Document Type Definitions).

    .. versionadded:: 1.5
    """
    flags: Incomplete
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class XmlLexer(RegexLexer):
    """
    Generic lexer for XML (eXtensible Markup Language).
    """
    flags: Incomplete
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class XsltLexer(XmlLexer):
    """
    A lexer for XSLT.

    .. versionadded:: 0.10
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    EXTRA_KEYWORDS: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
    def analyse_text(text): ...

class HamlLexer(ExtendedRegexLexer):
    """
    For Haml markup.

    .. versionadded:: 1.3
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class ScamlLexer(ExtendedRegexLexer):
    """
    For `Scaml markup <http://scalate.fusesource.org/>`_.  Scaml is Haml for Scala.

    .. versionadded:: 1.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class PugLexer(ExtendedRegexLexer):
    """
    For Pug markup.
    Pug is a variant of Scaml, see:
    http://scalate.fusesource.org/documentation/scaml-reference.html

    .. versionadded:: 1.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
JadeLexer = PugLexer

class UrlEncodedLexer(RegexLexer):
    """
    Lexer for urlencoded data

    .. versionadded:: 2.16
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
