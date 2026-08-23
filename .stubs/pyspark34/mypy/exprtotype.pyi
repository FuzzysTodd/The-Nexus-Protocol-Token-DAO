from mypy.fastparse import parse_type_string as parse_type_string
from mypy.nodes import BytesExpr as BytesExpr, CallExpr as CallExpr, ComplexExpr as ComplexExpr, EllipsisExpr as EllipsisExpr, Expression as Expression, FloatExpr as FloatExpr, IndexExpr as IndexExpr, IntExpr as IntExpr, ListExpr as ListExpr, MemberExpr as MemberExpr, NameExpr as NameExpr, OpExpr as OpExpr, RefExpr as RefExpr, StrExpr as StrExpr, TupleExpr as TupleExpr, UnaryExpr as UnaryExpr, get_member_expr_fullname as get_member_expr_fullname
from mypy.options import Options as Options
from mypy.types import ANNOTATED_TYPE_NAMES as ANNOTATED_TYPE_NAMES, AnyType as AnyType, CallableArgument as CallableArgument, EllipsisType as EllipsisType, ProperType as ProperType, RawExpressionType as RawExpressionType, Type as Type, TypeList as TypeList, TypeOfAny as TypeOfAny, UnboundType as UnboundType, UnionType as UnionType

class TypeTranslationError(Exception):
    """Exception raised when an expression is not valid as a type."""

def expr_to_unanalyzed_type(expr: Expression, options: Options | None = None, allow_new_syntax: bool = False, _parent: Expression | None = None) -> ProperType:
    """Translate an expression to the corresponding type.

    The result is not semantically analyzed. It can be UnboundType or TypeList.
    Raise TypeTranslationError if the expression cannot represent a type.

    If allow_new_syntax is True, allow all type syntax independent of the target
    Python version (used in stubs).
    """
