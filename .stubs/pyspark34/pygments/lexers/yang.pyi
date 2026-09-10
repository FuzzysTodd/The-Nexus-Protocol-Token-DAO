from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['YangLexer']

class YangLexer(RegexLexer):
    """
    Lexer for YANG, based on RFC7950.

    .. versionadded:: 2.7
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    TOP_STMTS_KEYWORDS: Incomplete
    MODULE_HEADER_STMT_KEYWORDS: Incomplete
    META_STMT_KEYWORDS: Incomplete
    LINKAGE_STMTS_KEYWORDS: Incomplete
    BODY_STMT_KEYWORDS: Incomplete
    DATA_DEF_STMT_KEYWORDS: Incomplete
    TYPE_STMT_KEYWORDS: Incomplete
    LIST_STMT_KEYWORDS: Incomplete
    CONSTANTS_KEYWORDS: Incomplete
    TYPES: Incomplete
    suffix_re_pattern: str
    tokens: Incomplete
