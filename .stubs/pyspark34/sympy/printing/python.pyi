from .repr import ReprPrinter as ReprPrinter
from .str import StrPrinter as StrPrinter
from _typeshed import Incomplete

STRPRINT: Incomplete

class PythonPrinter(ReprPrinter, StrPrinter):
    """A printer which converts an expression into its Python interpretation."""
    symbols: Incomplete
    functions: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...

def python(expr, **settings):
    """Return Python interpretation of passed expression
    (can be passed to the exec() function without any modifications)"""
def print_python(expr, **settings) -> None:
    """Print output of python() function"""
