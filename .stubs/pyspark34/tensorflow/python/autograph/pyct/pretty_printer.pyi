import gast
from _typeshed import Incomplete

class PrettyPrinter(gast.NodeVisitor):
    """Print AST nodes."""
    indent_lvl: int
    result: str
    color: Incomplete
    noanno: Incomplete
    def __init__(self, color, noanno) -> None: ...
    def generic_visit(self, node, name: Incomplete | None = None) -> None: ...

def fmt(node, color: bool = True, noanno: bool = False): ...
