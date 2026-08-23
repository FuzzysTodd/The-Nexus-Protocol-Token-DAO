from _typeshed import Incomplete
from mypy.nodes import ArgKind as ArgKind, CallExpr, ClassDef as ClassDef, Decorator, Expression as Expression, FuncDef as FuncDef, OverloadedFuncDef
from typing import Any

DATACLASS_DECORATORS: Incomplete

def is_trait_decorator(d: Expression) -> bool: ...
def is_trait(cdef: ClassDef) -> bool: ...
def dataclass_decorator_type(d: Expression) -> str | None: ...
def is_dataclass_decorator(d: Expression) -> bool: ...
def is_dataclass(cdef: ClassDef) -> bool: ...
def dataclass_type(cdef: ClassDef) -> str | None: ...
def get_mypyc_attr_literal(e: Expression) -> Any:
    """Convert an expression from a mypyc_attr decorator to a value.

    Supports a pretty limited range."""
def get_mypyc_attr_call(d: Expression) -> CallExpr | None:
    """Check if an expression is a call to mypyc_attr and return it if so."""
def get_mypyc_attrs(stmt: ClassDef | Decorator) -> dict[str, Any]:
    """Collect all the mypyc_attr attributes on a class definition or a function."""
def is_extension_class(cdef: ClassDef) -> bool: ...
def get_func_def(op: FuncDef | Decorator | OverloadedFuncDef) -> FuncDef: ...
def concrete_arg_kind(kind: ArgKind) -> ArgKind:
    """Find the concrete version of an arg kind that is being passed."""
def is_constant(e: Expression) -> bool:
    """Check whether we allow an expression to appear as a default value.

    We don't currently properly support storing the evaluated
    values for default arguments and default attribute values, so
    we restrict what expressions we allow.  We allow literals of
    primitives types, None, and references to Final global
    variables.
    """
def bytes_from_str(value: str) -> bytes:
    """Convert a string representing bytes into actual bytes.

    This is needed because the literal characters of BytesExpr (the
    characters inside b'') are stored in BytesExpr.value, whose type is
    'str' not 'bytes'.
    """
