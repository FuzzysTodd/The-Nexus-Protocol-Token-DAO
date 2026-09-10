from _typeshed import Incomplete
from dataclasses import dataclass

operators: Incomplete

def eval_expr(expr):
    """
    >>> eval_expr('2*6')
    12
    >>> eval_expr('2**6')
    64
    >>> eval_expr('1 + 2*3**(4) / (6 + -7)')
    -161.0
    """
def eval_(node): ...

@dataclass(frozen=True)
class _Sentinel:
    """A sentinel to mark a parameter as not explicitly set"""
    default_value: object
    def __init__(self, default_value) -> None: ...
