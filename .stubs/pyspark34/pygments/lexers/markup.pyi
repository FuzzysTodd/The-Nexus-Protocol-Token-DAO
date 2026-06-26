from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import DelegatingLexer, RegexLexer

__all__ = ['BBCodeLexer', 'MoinWikiLexer', 'RstLexer', 'TexLexer', 'GroffLexer', 'MozPreprocHashLexer', 'MozPreprocPercentLexer', 'MozPreprocXulLexer', 'MozPreprocJavascriptLexer', 'MozPreprocCssLexer', 'MarkdownLexer', 'TiddlyWiki5Lexer', 'WikitextLexer']

class BBCodeLexer(RegexLexer):
    """
    A lexer that highlights BBCode(-like) syntax.

    .. versionadded:: 0.6
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class MoinWikiLexer(RegexLexer):
    """
    For MoinMoin (and Trac) Wiki markup.

    .. versionadded:: 0.7
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class RstLexer(RegexLexer):
    """
    For reStructuredText markup.

    .. versionadded:: 0.7

    Additional options accepted:

    `handlecodeblocks`
        Highlight the contents of ``.. sourcecode:: language``,
        ``.. code:: language`` and ``.. code-block:: language``
        directives with a lexer for the given language (default:
        ``True``).

        .. versionadded:: 0.8
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    closers: str
    unicode_delimiters: str
    end_string_suffix: Incomplete
    tokens: Incomplete
    handlecodeblocks: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class TexLexer(RegexLexer):
    """
    Lexer for the TeX and LaTeX typesetting languages.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class GroffLexer(RegexLexer):
    """
    Lexer for the (g)roff typesetting language, supporting groff
    extensions. Mainly useful for highlighting manpage sources.

    .. versionadded:: 0.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class MozPreprocHashLexer(RegexLexer):
    """
    Lexer for Mozilla Preprocessor files (with '#' as the marker).

    Other data is left untouched.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class MozPreprocPercentLexer(MozPreprocHashLexer):
    """
    Lexer for Mozilla Preprocessor files (with '%' as the marker).

    Other data is left untouched.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class MozPreprocXulLexer(DelegatingLexer):
    """
    Subclass of the `MozPreprocHashLexer` that highlights unlexed data with the
    `XmlLexer`.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class MozPreprocJavascriptLexer(DelegatingLexer):
    """
    Subclass of the `MozPreprocHashLexer` that highlights unlexed data with the
    `JavascriptLexer`.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class MozPreprocCssLexer(DelegatingLexer):
    """
    Subclass of the `MozPreprocHashLexer` that highlights unlexed data with the
    `CssLexer`.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class MarkdownLexer(RegexLexer):
    """
    For Markdown markup.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    handlecodeblocks: Incomplete
    def __init__(self, **options) -> None: ...

class TiddlyWiki5Lexer(RegexLexer):
    """
    For TiddlyWiki5 markup.

    .. versionadded:: 2.7
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    handlecodeblocks: Incomplete
    def __init__(self, **options) -> None: ...

class WikitextLexer(RegexLexer):
    """
    For MediaWiki Wikitext.

    Parsing Wikitext is tricky, and results vary between different MediaWiki
    installations, so we only highlight common syntaxes (built-in or from
    popular extensions), and also assume templates produce no unbalanced
    syntaxes.

    .. versionadded:: 2.15
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    def nowiki_tag_rules(tag_name): ...
    def plaintext_tag_rules(tag_name): ...
    def delegate_tag_rules(tag_name, lexer): ...
    def text_rules(token): ...
    def handle_syntaxhighlight(self, match, ctx) -> Generator[Incomplete, Incomplete, None]: ...
    def handle_score(self, match, ctx) -> Generator[Incomplete, Incomplete, None]: ...
    title_char: str
    nbsp_char: str
    link_address: str
    link_char_class: str
    double_slashes_i: Incomplete
    double_slashes: Incomplete
    protocols: Incomplete
    non_relative_protocols: Incomplete
    html_tags: Incomplete
    parser_tags: Incomplete
    variant_langs: Incomplete
    magic_vars_i: Incomplete
    magic_vars: Incomplete
    parser_functions_i: Incomplete
    parser_functions: Incomplete
    tokens: Incomplete
