from _typeshed import Incomplete
from parso import tree as tree
from parso.pgen2.generator import ReservedString as ReservedString
from typing import Dict, Type

class ParserSyntaxError(Exception):
    """
    Contains error information about the parser tree.

    May be raised as an exception.
    """
    message: Incomplete
    error_leaf: Incomplete
    def __init__(self, message, error_leaf) -> None: ...

class InternalParseError(Exception):
    """
    Exception to signal the parser is stuck and error recovery didn't help.
    Basically this shouldn't happen. It's a sign that something is really
    wrong.
    """
    msg: Incomplete
    type: Incomplete
    value: Incomplete
    start_pos: Incomplete
    def __init__(self, msg, type_, value, start_pos) -> None: ...

class Stack(list): ...

class StackNode:
    dfa: Incomplete
    nodes: Incomplete
    def __init__(self, dfa) -> None: ...
    @property
    def nonterminal(self): ...

class BaseParser:
    """Parser engine.

    A Parser instance contains state pertaining to the current token
    sequence, and should not be used concurrently by different threads
    to parse separate token sequences.

    See python/tokenize.py for how to get input tokens by a string.

    When a syntax error occurs, error_recovery() is called.
    """
    node_map: Dict[str, Type[tree.BaseNode]]
    default_node = tree.Node
    leaf_map: Dict[str, Type[tree.Leaf]]
    default_leaf = tree.Leaf
    def __init__(self, pgen_grammar, start_nonterminal: str = 'file_input', error_recovery: bool = False) -> None: ...
    stack: Incomplete
    def parse(self, tokens): ...
    def error_recovery(self, token) -> None: ...
    def convert_node(self, nonterminal, children): ...
    def convert_leaf(self, type_, value, prefix, start_pos): ...
