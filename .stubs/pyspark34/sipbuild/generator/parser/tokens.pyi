from ..specification import CodeBlock as CodeBlock
from _typeshed import Incomplete

states: Incomplete
literals: str
directives: Incomplete
code_directives: Incomplete
keywords: Incomplete
directive_keywords: Incomplete
tokens: Incomplete

def t_eof(t): ...
def t_ANY_error(t) -> None: ...

t_ANY_ignore: str
t_code_ignore: str

def t_newline(t) -> None:
    """\\n"""
def t_LPAREN(t):
    """\\("""
def t_RPAREN(t):
    """\\)"""
def t_DIRECTIVE(t):
    """%[a-zA-Z][a-zA-Z]*"""
def t_code_END(t):
    """%End"""
def t_needeol_newline(t):
    """\\n"""
def t_code_newline(t) -> None:
    """\\n"""
def t_code_CH(t) -> None:
    """."""

ambiguous: str

def t_AMBIGUOUS(t): ...
def t_directive_AMBIGUOUS(t): ...
def t_CPPCOMMENT(t) -> None:
    """//.*"""
def t_COMMENTSTART(t) -> None:
    """/\\*"""
def t_ccomment_COMMENTEND(t) -> None:
    """\\*/"""
def t_ccomment_newline(t) -> None:
    """\\n"""
def t_ccomment_CH(t) -> None:
    """."""
def t_HEXNUMBER(t):
    """0x[\\da-fA-F]+"""
def t_NUMBER(t):
    """-?(\\d+(\\.\\d*)?|\\.\\d+)([eE][-+]?\\d+)?[fFlLuU]?"""
def t_STRING(t):
    '''"(\\\\.|[^\\\\"])*"'''
def t_QHEXCH(t):
    """'\\\\x[\\da-fA-F]+'"""
def t_QCH(t):
    """'[^'\\n]*['\\n]"""

t_LOGICAL_OR: str
t_SCOPE: str
t_NAME: str
