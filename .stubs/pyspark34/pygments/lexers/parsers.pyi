from _typeshed import Incomplete
from pygments.lexer import DelegatingLexer, RegexLexer

__all__ = ['RagelLexer', 'RagelEmbeddedLexer', 'RagelCLexer', 'RagelDLexer', 'RagelCppLexer', 'RagelObjectiveCLexer', 'RagelRubyLexer', 'RagelJavaLexer', 'AntlrLexer', 'AntlrPythonLexer', 'AntlrPerlLexer', 'AntlrRubyLexer', 'AntlrCppLexer', 'AntlrCSharpLexer', 'AntlrObjectiveCLexer', 'AntlrJavaLexer', 'AntlrActionScriptLexer', 'TreetopLexer', 'EbnfLexer']

class RagelLexer(RegexLexer):
    """A pure `Ragel <www.colm.net/open-source/ragel>`_ lexer.  Use this
    for fragments of Ragel.  For ``.rl`` files, use
    :class:`RagelEmbeddedLexer` instead (or one of the
    language-specific subclasses).

    .. versionadded:: 1.1

    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class RagelEmbeddedLexer(RegexLexer):
    """
    A lexer for Ragel embedded in a host language file.

    This will only highlight Ragel statements. If you want host language
    highlighting then call the language-specific Ragel lexer.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class RagelRubyLexer(DelegatingLexer):
    """
    A lexer for Ragel in a Ruby host file.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class RagelCLexer(DelegatingLexer):
    """
    A lexer for Ragel in a C host file.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class RagelDLexer(DelegatingLexer):
    """
    A lexer for Ragel in a D host file.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class RagelCppLexer(DelegatingLexer):
    """
    A lexer for Ragel in a C++ host file.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class RagelObjectiveCLexer(DelegatingLexer):
    """
    A lexer for Ragel in an Objective C host file.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class RagelJavaLexer(DelegatingLexer):
    """
    A lexer for Ragel in a Java host file.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class AntlrLexer(RegexLexer):
    """
    Generic `ANTLR`_ Lexer.
    Should not be called directly, instead
    use DelegatingLexer for your target language.

    .. versionadded:: 1.1

    .. _ANTLR: http://www.antlr.org/
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class AntlrCppLexer(DelegatingLexer):
    """
    ANTLR with C++ Target

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class AntlrObjectiveCLexer(DelegatingLexer):
    """
    ANTLR with Objective-C Target

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class AntlrCSharpLexer(DelegatingLexer):
    """
    ANTLR with C# Target

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class AntlrPythonLexer(DelegatingLexer):
    """
    ANTLR with Python Target

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class AntlrJavaLexer(DelegatingLexer):
    """
    ANTLR with Java Target

    .. versionadded:: 1.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class AntlrRubyLexer(DelegatingLexer):
    """
    ANTLR with Ruby Target

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class AntlrPerlLexer(DelegatingLexer):
    """
    ANTLR with Perl Target

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class AntlrActionScriptLexer(DelegatingLexer):
    """
    ANTLR with ActionScript Target

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class TreetopBaseLexer(RegexLexer):
    """
    A base lexer for `Treetop <http://treetop.rubyforge.org/>`_ grammars.
    Not for direct use; use :class:`TreetopLexer` instead.

    .. versionadded:: 1.6
    """
    tokens: Incomplete

class TreetopLexer(DelegatingLexer):
    """
    A lexer for `Treetop <http://treetop.rubyforge.org/>`_ grammars.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...

class EbnfLexer(RegexLexer):
    """
    Lexer for `ISO/IEC 14977 EBNF
    <http://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_Form>`_
    grammars.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
