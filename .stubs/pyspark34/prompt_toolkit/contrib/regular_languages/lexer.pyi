from .compiler import _CompiledGrammar
from _typeshed import Incomplete
from prompt_toolkit.document import Document
from prompt_toolkit.formatted_text.base import StyleAndTextTuples
from prompt_toolkit.lexers import Lexer
from typing import Callable

__all__ = ['GrammarLexer']

class GrammarLexer(Lexer):
    """
    Lexer which can be used for highlighting of fragments according to variables in the grammar.

    (It does not actual lexing of the string, but it exposes an API, compatible
    with the Pygments lexer class.)

    :param compiled_grammar: Grammar as returned by the `compile()` function.
    :param lexers: Dictionary mapping variable names of the regular grammar to
                   the lexers that should be used for this part. (This can
                   call other lexers recursively.) If you wish a part of the
                   grammar to just get one fragment, use a
                   `prompt_toolkit.lexers.SimpleLexer`.
    """
    compiled_grammar: Incomplete
    default_style: Incomplete
    lexers: Incomplete
    def __init__(self, compiled_grammar: _CompiledGrammar, default_style: str = '', lexers: dict[str, Lexer] | None = None) -> None: ...
    def lex_document(self, document: Document) -> Callable[[int], StyleAndTextTuples]: ...
