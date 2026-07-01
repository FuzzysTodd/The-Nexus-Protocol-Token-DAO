from _typeshed import Incomplete
from mypy import message_registry as message_registry
from mypy.errorcodes import ErrorCode as ErrorCode
from mypy.expandtype import expand_type as expand_type
from mypy.exprtotype import TypeTranslationError as TypeTranslationError, expr_to_unanalyzed_type as expr_to_unanalyzed_type
from mypy.messages import MessageBuilder as MessageBuilder
from mypy.nodes import ARG_NAMED as ARG_NAMED, ARG_POS as ARG_POS, AssignmentStmt as AssignmentStmt, CallExpr as CallExpr, ClassDef as ClassDef, Context as Context, DictExpr as DictExpr, EllipsisExpr as EllipsisExpr, Expression as Expression, ExpressionStmt as ExpressionStmt, IndexExpr as IndexExpr, NameExpr as NameExpr, PassStmt as PassStmt, RefExpr as RefExpr, Statement as Statement, StrExpr as StrExpr, TempNode as TempNode, TupleExpr as TupleExpr, TypeInfo as TypeInfo, TypedDictExpr as TypedDictExpr
from mypy.options import Options as Options
from mypy.semanal_shared import SemanticAnalyzerInterface as SemanticAnalyzerInterface, has_placeholder as has_placeholder, require_bool_literal_argument as require_bool_literal_argument
from mypy.typeanal import check_for_explicit_any as check_for_explicit_any, has_any_from_unimported_type as has_any_from_unimported_type
from mypy.types import AnyType as AnyType, RequiredType as RequiredType, TPDICT_NAMES as TPDICT_NAMES, Type as Type, TypeOfAny as TypeOfAny, TypeVarLikeType as TypeVarLikeType, TypedDictType as TypedDictType
from typing_extensions import Final

TPDICT_CLASS_ERROR: Final[str]

class TypedDictAnalyzer:
    options: Incomplete
    api: Incomplete
    msg: Incomplete
    def __init__(self, options: Options, api: SemanticAnalyzerInterface, msg: MessageBuilder) -> None: ...
    def analyze_typeddict_classdef(self, defn: ClassDef) -> tuple[bool, TypeInfo | None]:
        """Analyze a class that may define a TypedDict.

        Assume that base classes have been analyzed already.

        Note: Unlike normal classes, we won't create a TypeInfo until
        the whole definition of the TypeDict (including the body and all
        key names and types) is complete.  This is mostly because we
        store the corresponding TypedDictType in the TypeInfo.

        Return (is this a TypedDict, new TypeInfo). Specifics:
         * If we couldn't finish due to incomplete reference anywhere in
           the definition, return (True, None).
         * If this is not a TypedDict, return (False, None).
        """
    def add_keys_and_types_from_base(self, base: Expression, keys: list[str], types: list[Type], required_keys: set[str], ctx: Context) -> None: ...
    def analyze_base_args(self, base: IndexExpr, ctx: Context) -> list[Type] | None:
        """Analyze arguments of base type expressions as types.

        We need to do this, because normal base class processing happens after
        the TypedDict special-casing (plus we get a custom error message).
        """
    def map_items_to_base(self, valid_items: dict[str, Type], tvars: list[TypeVarLikeType], base_args: list[Type]) -> dict[str, Type]:
        """Map item types to how they would look in their base with type arguments applied.

        Note it is safe to use expand_type() during semantic analysis, because it should never
        (indirectly) call is_subtype().
        """
    def analyze_typeddict_classdef_fields(self, defn: ClassDef, oldfields: list[str] | None = None) -> tuple[list[str] | None, list[Type], list[Statement], set[str]]:
        """Analyze fields defined in a TypedDict class definition.

        This doesn't consider inherited fields (if any). Also consider totality,
        if given.

        Return tuple with these items:
         * List of keys (or None if found an incomplete reference --> deferral)
         * List of types for each key
         * List of statements from defn.defs.body that are legally allowed to be a
           part of a TypedDict definition
         * Set of required keys
        """
    def check_typeddict(self, node: Expression, var_name: str | None, is_func_scope: bool) -> tuple[bool, TypeInfo | None, list[TypeVarLikeType]]:
        """Check if a call defines a TypedDict.

        The optional var_name argument is the name of the variable to
        which this is assigned, if any.

        Return a pair (is it a typed dict, corresponding TypeInfo).

        If the definition is invalid but looks like a TypedDict,
        report errors but return (some) TypeInfo. If some type is not ready,
        return (True, None).
        """
    def parse_typeddict_args(self, call: CallExpr) -> tuple[str, list[str], list[Type], bool, list[TypeVarLikeType], bool] | None:
        """Parse typed dict call expression.

        Return names, types, totality, was there an error during parsing.
        If some type is not ready, return None.
        """
    def parse_typeddict_fields_with_types(self, dict_items: list[tuple[Expression | None, Expression]], context: Context) -> tuple[list[str], list[Type], bool] | None:
        """Parse typed dict items passed as pairs (name expression, type expression).

        Return names, types, was there an error. If some type is not ready, return None.
        """
    def fail_typeddict_arg(self, message: str, context: Context) -> tuple[str, list[str], list[Type], bool, list[TypeVarLikeType], bool]: ...
    def build_typeddict_typeinfo(self, name: str, items: list[str], types: list[Type], required_keys: set[str], line: int, existing_info: TypeInfo | None) -> TypeInfo: ...
    def is_typeddict(self, expr: Expression) -> bool: ...
    def fail(self, msg: str, ctx: Context, *, code: ErrorCode | None = None) -> None: ...
    def note(self, msg: str, ctx: Context) -> None: ...
