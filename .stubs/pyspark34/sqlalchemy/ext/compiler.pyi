from .. import exc as exc
from ..sql import sqltypes as sqltypes
from _typeshed import Incomplete

def compiles(class_, *specs):
    """Register a function as a compiler for a
    given :class:`_expression.ClauseElement` type."""
def deregister(class_) -> None:
    """Remove all custom compilers associated with a given
    :class:`_expression.ClauseElement` type.

    """

class _dispatcher:
    specs: Incomplete
    def __init__(self) -> None: ...
    def __call__(self, element, compiler, **kw): ...
