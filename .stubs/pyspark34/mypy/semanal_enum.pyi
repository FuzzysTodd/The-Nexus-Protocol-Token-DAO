from _typeshed import Incomplete
from mypy.nodes import ARG_NAMED as ARG_NAMED, ARG_POS as ARG_POS, AssignmentStmt as AssignmentStmt, CallExpr as CallExpr, Context as Context, DictExpr as DictExpr, EnumCallExpr as EnumCallExpr, Expression as Expression, ListExpr as ListExpr, MDEF as MDEF, MemberExpr as MemberExpr, NameExpr as NameExpr, RefExpr as RefExpr, StrExpr as StrExpr, SymbolTableNode as SymbolTableNode, TupleExpr as TupleExpr, TypeInfo as TypeInfo, Var as Var, is_StrExpr_list as is_StrExpr_list
from mypy.options import Options as Options
from mypy.semanal_shared import SemanticAnalyzerInterface as SemanticAnalyzerInterface
from mypy.types import ENUM_REMOVED_PROPS as ENUM_REMOVED_PROPS, LiteralType as LiteralType, get_proper_type as get_proper_type
from typing_extensions import Final

ENUM_BASES: Final[Incomplete]
ENUM_SPECIAL_PROPS: Final[Incomplete]

class EnumCallAnalyzer:
    options: Incomplete
    api: Incomplete
    def __init__(self, options: Options, api: SemanticAnalyzerInterface) -> None: ...
    def process_enum_call(self, s: AssignmentStmt, is_func_scope: bool) -> bool:
        """Check if s defines an Enum; if yes, store the definition in symbol table.

        Return True if this looks like an Enum definition (but maybe with errors),
        otherwise return False.
        """
    def check_enum_call(self, node: Expression, var_name: str, is_func_scope: bool) -> TypeInfo | None:
        """Check if a call defines an Enum.

        Example:

          A = enum.Enum('A', 'foo bar')

        is equivalent to:

          class A(enum.Enum):
              foo = 1
              bar = 2
        """
    def build_enum_call_typeinfo(self, name: str, items: list[str], fullname: str, line: int) -> TypeInfo: ...
    def parse_enum_call_args(self, call: CallExpr, class_name: str) -> tuple[list[str], list[Expression | None], bool]:
        """Parse arguments of an Enum call.

        Return a tuple of fields, values, was there an error.
        """
    def fail_enum_call_arg(self, message: str, context: Context) -> tuple[list[str], list[Expression | None], bool]: ...
    def fail(self, msg: str, ctx: Context) -> None: ...
