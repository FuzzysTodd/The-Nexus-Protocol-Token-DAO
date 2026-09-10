from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['BlitzBasicLexer', 'BlitzMaxLexer', 'MonkeyLexer', 'CbmBasicV2Lexer', 'QBasicLexer', 'VBScriptLexer', 'BBCBasicLexer']

class BlitzMaxLexer(RegexLexer):
    """
    For BlitzMax source code.

    .. versionadded:: 1.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    bmax_vopwords: str
    bmax_sktypes: str
    bmax_lktypes: str
    bmax_name: str
    bmax_var: Incomplete
    bmax_func: Incomplete
    flags: Incomplete
    tokens: Incomplete

class BlitzBasicLexer(RegexLexer):
    """
    For BlitzBasic source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    bb_sktypes: str
    bb_name: str
    bb_var: Incomplete
    flags: Incomplete
    tokens: Incomplete

class MonkeyLexer(RegexLexer):
    """
    For
    `Monkey <https://en.wikipedia.org/wiki/Monkey_(programming_language)>`_
    source code.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    name_variable: str
    name_function: str
    name_constant: str
    name_class: str
    name_module: str
    keyword_type: str
    keyword_type_special: str
    flags: Incomplete
    tokens: Incomplete

class CbmBasicV2Lexer(RegexLexer):
    """
    For CBM BASIC V2 sources.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class QBasicLexer(RegexLexer):
    """
    For
    `QBasic <http://en.wikipedia.org/wiki/QBasic>`_
    source code.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    declarations: Incomplete
    functions: Incomplete
    metacommands: Incomplete
    operators: Incomplete
    statements: Incomplete
    keywords: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class VBScriptLexer(RegexLexer):
    """
    VBScript is scripting language that is modeled on Visual Basic.

    .. versionadded:: 2.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete

class BBCBasicLexer(RegexLexer):
    """
    BBC Basic was supplied on the BBC Micro, and later Acorn RISC OS.
    It is also used by BBC Basic For Windows.

    .. versionadded:: 2.4
    """
    base_keywords: Incomplete
    basic5_keywords: Incomplete
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
