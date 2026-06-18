from IPython.core.completer import cursor_to_position as cursor_to_position, provisionalcompleter as provisionalcompleter
from _typeshed import Incomplete
from collections.abc import Generator
from prompt_toolkit.completion import Completer
from prompt_toolkit.lexers import Lexer

class IPythonPTCompleter(Completer):
    """Adaptor to provide IPython completions to prompt_toolkit"""
    shell: Incomplete
    def __init__(self, ipy_completer: Incomplete | None = None, shell: Incomplete | None = None) -> None: ...
    @property
    def ipy_completer(self): ...
    def get_completions(self, document, complete_event) -> Generator[Incomplete, Incomplete, None]: ...

class IPythonPTLexer(Lexer):
    """
    Wrapper around PythonLexer and BashLexer.
    """
    python_lexer: Incomplete
    shell_lexer: Incomplete
    magic_lexers: Incomplete
    def __init__(self) -> None: ...
    def lex_document(self, document): ...
