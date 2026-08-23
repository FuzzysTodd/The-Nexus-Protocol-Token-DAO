from _typeshed import Incomplete
from mypy.nodes import Expression as Expression
from mypyc.irbuild.builder import IRBuilder as IRBuilder
from mypyc.irbuild.util import bytes_from_str as bytes_from_str
from typing import Final

ConstantValue = int | float | complex | str | bytes
CONST_TYPES: Final[Incomplete]

def constant_fold_expr(builder: IRBuilder, expr: Expression) -> ConstantValue | None:
    """Return the constant value of an expression for supported operations.

    Return None otherwise.
    """
def constant_fold_binary_op_extended(op: str, left: ConstantValue, right: ConstantValue) -> ConstantValue | None:
    """Like mypy's constant_fold_binary_op(), but includes bytes support.

    mypy cannot use constant folded bytes easily so it's simpler to only support them in mypyc.
    """
