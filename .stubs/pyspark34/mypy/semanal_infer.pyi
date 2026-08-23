from mypy.nodes import ARG_POS as ARG_POS, CallExpr as CallExpr, Decorator as Decorator, Expression as Expression, FuncDef as FuncDef, RefExpr as RefExpr, Var as Var
from mypy.semanal_shared import SemanticAnalyzerInterface as SemanticAnalyzerInterface
from mypy.typeops import function_type as function_type
from mypy.types import AnyType as AnyType, CallableType as CallableType, ProperType as ProperType, Type as Type, TypeOfAny as TypeOfAny, TypeVarType as TypeVarType, get_proper_type as get_proper_type
from mypy.typevars import has_no_typevars as has_no_typevars

def infer_decorator_signature_if_simple(dec: Decorator, analyzer: SemanticAnalyzerInterface) -> None:
    """Try to infer the type of the decorated function.

    This lets us resolve additional references to decorated functions
    during type checking. Otherwise the type might not be available
    when we need it, since module top levels can't be deferred.

    This basically uses a simple special-purpose type inference
    engine just for decorators.
    """
def is_identity_signature(sig: Type) -> bool:
    """Is type a callable of form T -> T (where T is a type variable)?"""
def calculate_return_type(expr: Expression) -> ProperType | None:
    """Return the return type if we can calculate it.

    This only uses information available during semantic analysis so this
    will sometimes return None because of insufficient information (as
    type inference hasn't run yet).
    """
def find_fixed_callable_return(expr: Expression) -> CallableType | None:
    """Return the return type, if expression refers to a callable that returns a callable.

    But only do this if the return type has no type variables. Return None otherwise.
    This approximates things a lot as this is supposed to be called before type checking
    when full type information is not available yet.
    """
