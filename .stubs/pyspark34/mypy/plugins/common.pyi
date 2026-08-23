from mypy.argmap import map_actuals_to_formals as map_actuals_to_formals
from mypy.fixup import TypeFixer as TypeFixer
from mypy.nodes import ARG_POS as ARG_POS, Argument as Argument, Block as Block, CallExpr as CallExpr, ClassDef as ClassDef, Decorator as Decorator, Expression as Expression, FuncDef as FuncDef, JsonDict as JsonDict, MDEF as MDEF, NameExpr as NameExpr, Node as Node, PassStmt as PassStmt, RefExpr as RefExpr, SYMBOL_FUNCBASE_TYPES as SYMBOL_FUNCBASE_TYPES, SymbolTableNode as SymbolTableNode, Var as Var
from mypy.plugin import CheckerPluginInterface as CheckerPluginInterface, ClassDefContext as ClassDefContext, SemanticAnalyzerPluginInterface as SemanticAnalyzerPluginInterface
from mypy.semanal_shared import ALLOW_INCOMPATIBLE_OVERRIDE as ALLOW_INCOMPATIBLE_OVERRIDE, parse_bool as parse_bool, require_bool_literal_argument as require_bool_literal_argument, set_callable_name as set_callable_name
from mypy.types import AnyType as AnyType, CallableType as CallableType, Instance as Instance, LiteralType as LiteralType, NoneType as NoneType, Overloaded as Overloaded, Type as Type, TypeOfAny as TypeOfAny, TypeType as TypeType, TypeVarType as TypeVarType, deserialize_type as deserialize_type, get_proper_type as get_proper_type
from mypy.types_utils import is_optional as is_optional
from mypy.typevars import fill_typevars as fill_typevars
from mypy.util import get_unique_redefinition_name as get_unique_redefinition_name

def find_shallow_matching_overload_item(overload: Overloaded, call: CallExpr) -> CallableType:
    '''Perform limited lookup of a matching overload item.

    Full overload resolution is only supported during type checking, but plugins
    sometimes need to resolve overloads. This can be used in some such use cases.

    Resolve overloads based on these things only:

    * Match using argument kinds and names
    * If formal argument has type None, only accept the "None" expression in the callee
    * If formal argument has type Literal[True] or Literal[False], only accept the
      relevant bool literal

    Return the first matching overload item, or the last one if nothing matches.
    '''
def add_method(ctx: ClassDefContext, name: str, args: list[Argument], return_type: Type, self_type: Type | None = None, tvar_def: TypeVarType | None = None, is_classmethod: bool = False, is_staticmethod: bool = False) -> None:
    """
    Adds a new method to a class.
    Deprecated, use add_method_to_class() instead.
    """
def add_method_to_class(api: SemanticAnalyzerPluginInterface | CheckerPluginInterface, cls: ClassDef, name: str, args: list[Argument], return_type: Type, self_type: Type | None = None, tvar_def: TypeVarType | None = None, is_classmethod: bool = False, is_staticmethod: bool = False) -> None:
    """Adds a new method to a class definition."""
def add_attribute_to_class(api: SemanticAnalyzerPluginInterface, cls: ClassDef, name: str, typ: Type, final: bool = False, no_serialize: bool = False, override_allow_incompatible: bool = False, fullname: str | None = None, is_classvar: bool = False) -> None:
    """
    Adds a new attribute to a class definition.
    This currently only generates the symbol table entry and no corresponding AssignmentStatement
    """
def deserialize_and_fixup_type(data: str | JsonDict, api: SemanticAnalyzerPluginInterface) -> Type: ...
