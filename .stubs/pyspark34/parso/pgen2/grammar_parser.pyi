from _typeshed import Incomplete
from parso.python.token import PythonTokenTypes as PythonTokenTypes
from parso.python.tokenize import tokenize as tokenize
from parso.utils import parse_version_string as parse_version_string
from typing import Iterator, Tuple

class NFAArc:
    next: Incomplete
    nonterminal_or_string: Incomplete
    def __init__(self, next_: NFAState, nonterminal_or_string: str | None) -> None: ...

class NFAState:
    from_rule: Incomplete
    arcs: Incomplete
    def __init__(self, from_rule: str) -> None: ...
    def add_arc(self, next_, nonterminal_or_string: Incomplete | None = None) -> None: ...

class GrammarParser:
    """
    The parser for Python grammar files.
    """
    generator: Incomplete
    def __init__(self, bnf_grammar: str) -> None: ...
    def parse(self) -> Iterator[Tuple[NFAState, NFAState]]: ...
