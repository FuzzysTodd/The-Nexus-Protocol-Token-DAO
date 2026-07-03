from mypy.nodes import Decorator as Decorator, FakeInfo as FakeInfo, FuncDef as FuncDef, SymbolNode as SymbolNode, Var as Var
from mypy.server.objgraph import get_path as get_path, get_reachable_graph as get_reachable_graph
from typing_extensions import Final

DUMP_MISMATCH_NODES: Final[bool]

def check_consistency(o: object) -> None:
    """Fail if there are two AST nodes with the same fullname reachable from 'o'.

    Raise AssertionError on failure and print some debugging output.
    """
def path_to_str(path: list[tuple[object, object]]) -> str: ...
