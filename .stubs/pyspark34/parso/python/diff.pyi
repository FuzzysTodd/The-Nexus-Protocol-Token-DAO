from _typeshed import Incomplete
from parso.python.parser import Parser as Parser
from parso.python.token import PythonTokenTypes as PythonTokenTypes
from parso.python.tokenize import BOM_UTF8_STRING as BOM_UTF8_STRING, PythonToken as PythonToken
from parso.python.tree import EndMarker as EndMarker
from parso.utils import split_lines as split_lines
from typing import NamedTuple

LOG: Incomplete
DEBUG_DIFF_PARSER: bool
NEWLINE: Incomplete
DEDENT: Incomplete
NAME: Incomplete
ERROR_DEDENT: Incomplete
ENDMARKER: Incomplete

class _PositionUpdatingFinished(Exception): ...

class DiffParser:
    """
    An advanced form of parsing a file faster. Unfortunately comes with huge
    side effects. It changes the given module.
    """
    def __init__(self, pgen_grammar, tokenizer, module) -> None: ...
    def update(self, old_lines, new_lines):
        """
        The algorithm works as follows:

        Equal:
            - Assure that the start is a newline, otherwise parse until we get
              one.
            - Copy from parsed_until_line + 1 to max(i2 + 1)
            - Make sure that the indentation is correct (e.g. add DEDENT)
            - Add old and change positions
        Insert:
            - Parse from parsed_until_line + 1 to min(j2 + 1), hopefully not
              much more.

        Returns the new module node.
        """

class _NodesTreeNode:

    class _ChildrenGroup(NamedTuple):
        prefix: Incomplete
        children: Incomplete
        line_offset: Incomplete
        last_line_offset_leaf: Incomplete
    tree_node: Incomplete
    parent: Incomplete
    indentation: Incomplete
    def __init__(self, tree_node, parent: Incomplete | None = None, indentation: int = 0) -> None: ...
    def finish(self) -> None: ...
    def add_child_node(self, child_node) -> None: ...
    def add_tree_nodes(self, prefix, children, line_offset: int = 0, last_line_offset_leaf: Incomplete | None = None) -> None: ...
    def get_last_line(self, suffix): ...

class _NodesTree:
    prefix: str
    indents: Incomplete
    def __init__(self, module) -> None: ...
    @property
    def parsed_until_line(self): ...
    def add_parsed_nodes(self, tree_nodes, keyword_token_indents) -> None: ...
    def copy_nodes(self, tree_nodes, until_line, line_offset):
        """
        Copies tree nodes from the old parser tree.

        Returns the number of tree nodes that were copied.
        """
    def close(self) -> None: ...
