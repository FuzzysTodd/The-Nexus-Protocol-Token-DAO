import abc
from _typeshed import Incomplete
from abc import abstractmethod
from parso.utils import split_lines as split_lines
from typing import List, Tuple

def search_ancestor(node: NodeOrLeaf, *node_types: str) -> BaseNode | None:
    """
    Recursively looks at the parents of a node and returns the first found node
    that matches ``node_types``. Returns ``None`` if no matching node is found.

    This function is deprecated, use :meth:`NodeOrLeaf.search_ancestor` instead.

    :param node: The ancestors of this node will be checked.
    :param node_types: type names that are searched for.
    """

class NodeOrLeaf(metaclass=abc.ABCMeta):
    """
    The base class for nodes and leaves.
    """
    type: str
    parent: BaseNode | None
    def get_root_node(self):
        """
        Returns the root node of a parser tree. The returned node doesn't have
        a parent node like all the other nodes/leaves.
        """
    def get_next_sibling(self):
        """
        Returns the node immediately following this node in this parent's
        children list. If this node does not have a next sibling, it is None
        """
    def get_previous_sibling(self):
        """
        Returns the node immediately preceding this node in this parent's
        children list. If this node does not have a previous sibling, it is
        None.
        """
    def get_previous_leaf(self):
        """
        Returns the previous leaf in the parser tree.
        Returns `None` if this is the first element in the parser tree.
        """
    def get_next_leaf(self):
        """
        Returns the next leaf in the parser tree.
        Returns None if this is the last element in the parser tree.
        """
    @property
    @abc.abstractmethod
    def start_pos(self) -> Tuple[int, int]:
        """
        Returns the starting position of the prefix as a tuple, e.g. `(3, 4)`.

        :return tuple of int: (line, column)
        """
    @property
    @abc.abstractmethod
    def end_pos(self) -> Tuple[int, int]:
        """
        Returns the end position of the prefix as a tuple, e.g. `(3, 4)`.

        :return tuple of int: (line, column)
        """
    @abstractmethod
    def get_start_pos_of_prefix(self):
        """
        Returns the start_pos of the prefix. This means basically it returns
        the end_pos of the last prefix. The `get_start_pos_of_prefix()` of the
        prefix `+` in `2 + 1` would be `(1, 1)`, while the start_pos is
        `(1, 2)`.

        :return tuple of int: (line, column)
        """
    @abstractmethod
    def get_first_leaf(self):
        """
        Returns the first leaf of a node or itself if this is a leaf.
        """
    @abstractmethod
    def get_last_leaf(self):
        """
        Returns the last leaf of a node or itself if this is a leaf.
        """
    @abstractmethod
    def get_code(self, include_prefix: bool = True):
        """
        Returns the code that was the input for the parser for this node.

        :param include_prefix: Removes the prefix (whitespace and comments) of
            e.g. a statement.
        """
    def search_ancestor(self, *node_types: str) -> BaseNode | None:
        """
        Recursively looks at the parents of this node or leaf and returns the
        first found node that matches ``node_types``. Returns ``None`` if no
        matching node is found.

        :param node_types: type names that are searched for.
        """
    def dump(self, *, indent: int | str | None = 4) -> str:
        '''
        Returns a formatted dump of the parser tree rooted at this node or leaf. This is
        mainly useful for debugging purposes.

        The ``indent`` parameter is interpreted in a similar way as :py:func:`ast.dump`.
        If ``indent`` is a non-negative integer or string, then the tree will be
        pretty-printed with that indent level. An indent level of 0, negative, or ``""``
        will only insert newlines. ``None`` selects the single line representation.
        Using a positive integer indent indents that many spaces per level. If
        ``indent`` is a string (such as ``"\\t"``), that string is used to indent each
        level.

        :param indent: Indentation style as described above. The default indentation is
            4 spaces, which yields a pretty-printed dump.

        >>> import parso
        >>> print(parso.parse("lambda x, y: x + y").dump())
        Module([
            Lambda([
                Keyword(\'lambda\', (1, 0)),
                Param([
                    Name(\'x\', (1, 7), prefix=\' \'),
                    Operator(\',\', (1, 8)),
                ]),
                Param([
                    Name(\'y\', (1, 10), prefix=\' \'),
                ]),
                Operator(\':\', (1, 11)),
                PythonNode(\'arith_expr\', [
                    Name(\'x\', (1, 13), prefix=\' \'),
                    Operator(\'+\', (1, 15), prefix=\' \'),
                    Name(\'y\', (1, 17), prefix=\' \'),
                ]),
            ]),
            EndMarker(\'\', (1, 18)),
        ])
        '''

class Leaf(NodeOrLeaf):
    """
    Leafs are basically tokens with a better API. Leafs exactly know where they
    were defined and what text preceeds them.
    """
    prefix: str
    value: Incomplete
    parent: Incomplete
    def __init__(self, value: str, start_pos: Tuple[int, int], prefix: str = '') -> None: ...
    @property
    def start_pos(self) -> Tuple[int, int]: ...
    line: Incomplete
    column: Incomplete
    @start_pos.setter
    def start_pos(self, value: Tuple[int, int]) -> None: ...
    def get_start_pos_of_prefix(self): ...
    def get_first_leaf(self): ...
    def get_last_leaf(self): ...
    def get_code(self, include_prefix: bool = True): ...
    @property
    def end_pos(self) -> Tuple[int, int]: ...

class TypedLeaf(Leaf):
    type: Incomplete
    def __init__(self, type, value, start_pos, prefix: str = '') -> None: ...

class BaseNode(NodeOrLeaf):
    """
    The super class for all nodes.
    A node has children, a type and possibly a parent node.
    """
    children: Incomplete
    parent: Incomplete
    def __init__(self, children: List[NodeOrLeaf]) -> None: ...
    @property
    def start_pos(self) -> Tuple[int, int]: ...
    def get_start_pos_of_prefix(self): ...
    @property
    def end_pos(self) -> Tuple[int, int]: ...
    def get_code(self, include_prefix: bool = True): ...
    def get_leaf_for_position(self, position, include_prefixes: bool = False):
        """
        Get the :py:class:`parso.tree.Leaf` at ``position``

        :param tuple position: A position tuple, row, column. Rows start from 1
        :param bool include_prefixes: If ``False``, ``None`` will be returned if ``position`` falls
            on whitespace or comments before a leaf
        :return: :py:class:`parso.tree.Leaf` at ``position``, or ``None``
        """
    def get_first_leaf(self): ...
    def get_last_leaf(self): ...

class Node(BaseNode):
    """Concrete implementation for interior nodes."""
    type: Incomplete
    def __init__(self, type, children) -> None: ...

class ErrorNode(BaseNode):
    """
    A node that contains valid nodes/leaves that we're follow by a token that
    was invalid. This basically means that the leaf after this node is where
    Python would mark a syntax error.
    """
    type: str

class ErrorLeaf(Leaf):
    """
    A leaf that is either completely invalid in a language (like `$` in Python)
    or is invalid at that position. Like the star in `1 +* 1`.
    """
    type: str
    token_type: Incomplete
    def __init__(self, token_type, value, start_pos, prefix: str = '') -> None: ...
