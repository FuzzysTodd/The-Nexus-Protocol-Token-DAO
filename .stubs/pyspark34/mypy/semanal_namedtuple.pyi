from _typeshed import Incomplete
from mypy.exprtotype import TypeTranslationError as TypeTranslationError, expr_to_unanalyzed_type as expr_to_unanalyzed_type
from mypy.nodes import ARG_NAMED_OPT as ARG_NAMED_OPT, ARG_OPT as ARG_OPT, ARG_POS as ARG_POS, Argument as Argument, AssignmentStmt as AssignmentStmt, Block as Block, CallExpr as CallExpr, ClassDef as ClassDef, Context as Context, Decorator as Decorator, EllipsisExpr as EllipsisExpr, Expression as Expression, ExpressionStmt as ExpressionStmt, FuncBase as FuncBase, FuncDef as FuncDef, ListExpr as ListExpr, MDEF as MDEF, NameExpr as NameExpr, NamedTupleExpr as NamedTupleExpr, PassStmt as PassStmt, RefExpr as RefExpr, Statement as Statement, StrExpr as StrExpr, SymbolTable as SymbolTable, SymbolTableNode as SymbolTableNode, TempNode as TempNode, TupleExpr as TupleExpr, TypeInfo as TypeInfo, TypeVarExpr as TypeVarExpr, Var as Var, is_StrExpr_list as is_StrExpr_list
from mypy.options import Options as Options
from mypy.semanal_shared import PRIORITY_FALLBACKS as PRIORITY_FALLBACKS, SemanticAnalyzerInterface as SemanticAnalyzerInterface, calculate_tuple_fallback as calculate_tuple_fallback, has_placeholder as has_placeholder, set_callable_name as set_callable_name
from mypy.types import AnyType as AnyType, CallableType as CallableType, LiteralType as LiteralType, TYPED_NAMEDTUPLE_NAMES as TYPED_NAMEDTUPLE_NAMES, TupleType as TupleType, Type as Type, TypeOfAny as TypeOfAny, TypeType as TypeType, TypeVarLikeType as TypeVarLikeType, TypeVarType as TypeVarType, UnboundType as UnboundType, has_type_vars as has_type_vars
from mypy.util import get_unique_redefinition_name as get_unique_redefinition_name
from typing import Iterator, Mapping
from typing_extensions import Final

NAMEDTUPLE_PROHIBITED_NAMES: Final[Incomplete]
NAMEDTUP_CLASS_ERROR: Final[str]
SELF_TVAR_NAME: Final[str]

class NamedTupleAnalyzer:
    options: Incomplete
    api: Incomplete
    def __init__(self, options: Options, api: SemanticAnalyzerInterface) -> None: ...
    def analyze_namedtuple_classdef(self, defn: ClassDef, is_stub_file: bool, is_func_scope: bool) -> tuple[bool, TypeInfo | None]:
        """Analyze if given class definition can be a named tuple definition.

        Return a tuple where first item indicates whether this can possibly be a named tuple,
        and the second item is the corresponding TypeInfo (may be None if not ready and should be
        deferred).
        """
    def check_namedtuple_classdef(self, defn: ClassDef, is_stub_file: bool) -> tuple[list[str], list[Type], dict[str, Expression], list[Statement]] | None:
        """Parse and validate fields in named tuple class definition.

        Return a four tuple:
          * field names
          * field types
          * field default values
          * valid statements
        or None, if any of the types are not ready.
        """
    def check_namedtuple(self, node: Expression, var_name: str | None, is_func_scope: bool) -> tuple[str | None, TypeInfo | None, list[TypeVarLikeType]]:
        """Check if a call defines a namedtuple.

        The optional var_name argument is the name of the variable to
        which this is assigned, if any.

        Return a tuple of two items:
          * Internal name of the named tuple (e.g. the name passed as an argument to namedtuple)
            or None if it is not a valid named tuple
          * Corresponding TypeInfo, or None if not ready.

        If the definition is invalid but looks like a namedtuple,
        report errors but return (some) TypeInfo.
        """
    def store_namedtuple_info(self, info: TypeInfo, name: str, call: CallExpr, is_typed: bool) -> None: ...
    def parse_namedtuple_args(self, call: CallExpr, fullname: str) -> None | tuple[list[str], list[Type], list[Expression], str, list[TypeVarLikeType], bool]:
        """Parse a namedtuple() call into data needed to construct a type.

        Returns a 6-tuple:
        - List of argument names
        - List of argument types
        - List of default values
        - First argument of namedtuple
        - All typevars found in the field definition
        - Whether all types are ready.

        Return None if the definition didn't typecheck.
        """
    def parse_namedtuple_fields_with_types(self, nodes: list[Expression], context: Context) -> tuple[list[str], list[Type], list[Expression], bool] | None:
        """Parse typed named tuple fields.

        Return (names, types, defaults, whether types are all ready), or None if error occurred.
        """
    def build_namedtuple_typeinfo(self, name: str, items: list[str], types: list[Type], default_items: Mapping[str, Expression], line: int, existing_info: TypeInfo | None) -> TypeInfo: ...
    def save_namedtuple_body(self, named_tuple_info: TypeInfo) -> Iterator[None]:
        """Preserve the generated body of class-based named tuple and then restore it.

        Temporarily clear the names dict so we don't get errors about duplicate names
        that were already set in build_namedtuple_typeinfo (we already added the tuple
        field names while generating the TypeInfo, and actual duplicates are
        already reported).
        """
    def fail(self, msg: str, ctx: Context) -> None: ...
