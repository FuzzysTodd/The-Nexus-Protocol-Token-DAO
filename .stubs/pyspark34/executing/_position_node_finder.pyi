import ast
import dis
from ._exceptions import KnownIssue as KnownIssue, VerifierFailure as VerifierFailure
from .executing import EnhancedAST as EnhancedAST, NotOneValueFound as NotOneValueFound, Source as Source, assert_ as assert_, function_node_types as function_node_types, only as only
from _typeshed import Incomplete
from types import CodeType, FrameType
from typing import Iterator, Sequence, Set, Type

def parents(node: EnhancedAST) -> Iterator[EnhancedAST]: ...
def node_and_parents(node: EnhancedAST) -> Iterator[EnhancedAST]: ...
def mangled_name(node: EnhancedAST) -> str:
    """

    Parameters:
        node: the node which should be mangled
        name: the name of the node

    Returns:
        The mangled name of `node`
    """
def get_instructions(code: CodeType) -> list[dis.Instruction]: ...

types_cmp_issue_fix: Incomplete
types_cmp_issue: Incomplete
op_type_map: Incomplete

class PositionNodeFinder:
    """
    Mapping bytecode to ast-node based on the source positions, which where introduced in pyhon 3.11.
    In general every ast-node can be exactly referenced by its begin/end line/col_offset, which is stored in the bytecode.
    There are only some exceptions for methods and attributes.
    """
    bc_list: Incomplete
    source: Incomplete
    decorator: Incomplete
    result: Incomplete
    def __init__(self, frame: FrameType, stmts: Set[EnhancedAST], tree: ast.Module, lasti: int, source: Source) -> None: ...
    def test_for_decorator(self, node: EnhancedAST, index: int) -> None: ...
    def known_issues(self, node: EnhancedAST, instruction: dis.Instruction) -> None: ...
    @staticmethod
    def is_except_cleanup(inst: dis.Instruction, node: EnhancedAST) -> bool: ...
    def verify(self, node: EnhancedAST, instruction: dis.Instruction) -> None:
        """
        checks if this node could gererate this instruction
        """
    def instruction(self, index: int) -> dis.Instruction: ...
    def opname(self, index: int) -> str: ...
    def find_node(self, index: int, match_positions: Sequence[str] = ('lineno', 'end_lineno', 'col_offset', 'end_col_offset'), typ: tuple[Type, ...] = ...) -> EnhancedAST: ...
