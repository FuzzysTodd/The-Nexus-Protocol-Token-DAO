from _typeshed import Incomplete
from mypy.nodes import Expression as Expression, FloatExpr as FloatExpr, IntExpr as IntExpr, NameExpr as NameExpr, OpExpr as OpExpr, StrExpr as StrExpr, UnaryExpr as UnaryExpr, Var as Var
from typing import Union
from typing_extensions import Final

ConstantValue = Union[int, bool, float, str]
CONST_TYPES: Final[Incomplete]

def constant_fold_expr(expr: Expression, cur_mod_id: str) -> ConstantValue | None:
    """Return the constant value of an expression for supported operations.

    Among other things, support int arithmetic and string
    concatenation. For example, the expression 3 + 5 has the constant
    value 8.

    Also bind simple references to final constants defined in the
    current module (cur_mod_id). Binding to references is best effort
    -- we don't bind references to other modules. Mypyc trusts these
    to be correct in compiled modules, so that it can replace a
    constant expression (or a reference to one) with the statically
    computed value. We don't want to infer constant values based on
    stubs, in particular, as these might not match the implementation
    (due to version skew, for example).

    Return None if unsuccessful.
    """
def constant_fold_binary_int_op(op: str, left: int, right: int) -> int | None: ...
def constant_fold_unary_int_op(op: str, value: int) -> int | None: ...
def constant_fold_unary_float_op(op: str, value: float) -> float | None: ...
def constant_fold_binary_str_op(op: str, left: str, right: str) -> str | None: ...
