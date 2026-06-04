from _typeshed import Incomplete
from mypy.errorcodes import ErrorCode as ErrorCode
from mypy.exprtotype import TypeTranslationError as TypeTranslationError, expr_to_unanalyzed_type as expr_to_unanalyzed_type
from mypy.messages import MessageBuilder as MessageBuilder, format_type as format_type
from mypy.nodes import ARG_POS as ARG_POS, Argument as Argument, AssignmentStmt as AssignmentStmt, Block as Block, CallExpr as CallExpr, Context as Context, FuncDef as FuncDef, MDEF as MDEF, NameExpr as NameExpr, NewTypeExpr as NewTypeExpr, PlaceholderNode as PlaceholderNode, RefExpr as RefExpr, StrExpr as StrExpr, SymbolTableNode as SymbolTableNode, TypeInfo as TypeInfo, Var as Var
from mypy.options import Options as Options
from mypy.semanal_shared import SemanticAnalyzerInterface as SemanticAnalyzerInterface, has_placeholder as has_placeholder
from mypy.typeanal import check_for_explicit_any as check_for_explicit_any, has_any_from_unimported_type as has_any_from_unimported_type
from mypy.types import AnyType as AnyType, CallableType as CallableType, Instance as Instance, NoneType as NoneType, PlaceholderType as PlaceholderType, TupleType as TupleType, Type as Type, TypeOfAny as TypeOfAny, get_proper_type as get_proper_type

class NewTypeAnalyzer:
    options: Incomplete
    api: Incomplete
    msg: Incomplete
    def __init__(self, options: Options, api: SemanticAnalyzerInterface, msg: MessageBuilder) -> None: ...
    def process_newtype_declaration(self, s: AssignmentStmt) -> bool:
        """Check if s declares a NewType; if yes, store it in symbol table.

        Return True if it's a NewType declaration. The current target may be
        deferred as a side effect if the base type is not ready, even if
        the return value is True.

        The logic in this function mostly copies the logic for visit_class_def()
        with a single (non-Generic) base.
        """
    def analyze_newtype_declaration(self, s: AssignmentStmt) -> tuple[str | None, CallExpr | None]:
        """Return the NewType call expression if `s` is a newtype declaration or None otherwise."""
    def check_newtype_args(self, name: str, call: CallExpr, context: Context) -> tuple[Type | None, bool]:
        """Ananlyze base type in NewType call.

        Return a tuple (type, should defer).
        """
    def build_newtype_typeinfo(self, name: str, old_type: Type, base_type: Instance, line: int, existing_info: TypeInfo | None) -> TypeInfo: ...
    def make_argument(self, name: str, type: Type) -> Argument: ...
    def fail(self, msg: str, ctx: Context, *, code: ErrorCode | None = None) -> None: ...
