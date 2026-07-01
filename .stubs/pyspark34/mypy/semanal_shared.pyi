import abc
from _typeshed import Incomplete
from abc import abstractmethod
from mypy import join as join
from mypy.errorcodes import ErrorCode as ErrorCode, LITERAL_REQ as LITERAL_REQ
from mypy.nodes import CallExpr as CallExpr, ClassDef as ClassDef, Context as Context, DataclassTransformSpec as DataclassTransformSpec, Decorator as Decorator, Expression as Expression, FuncDef as FuncDef, NameExpr as NameExpr, Node as Node, OverloadedFuncDef as OverloadedFuncDef, RefExpr as RefExpr, SymbolNode as SymbolNode, SymbolTable as SymbolTable, SymbolTableNode as SymbolTableNode, TypeInfo as TypeInfo
from mypy.plugin import SemanticAnalyzerPluginInterface as SemanticAnalyzerPluginInterface
from mypy.tvar_scope import TypeVarLikeScope as TypeVarLikeScope
from mypy.type_visitor import ANY_STRATEGY as ANY_STRATEGY, BoolTypeQuery as BoolTypeQuery
from mypy.types import AnyType as AnyType, FunctionLike as FunctionLike, Instance as Instance, ParamSpecFlavor as ParamSpecFlavor, ParamSpecType as ParamSpecType, Parameters as Parameters, PlaceholderType as PlaceholderType, ProperType as ProperType, TPDICT_FB_NAMES as TPDICT_FB_NAMES, TupleType as TupleType, Type as Type, TypeOfAny as TypeOfAny, TypeVarId as TypeVarId, TypeVarLikeType as TypeVarLikeType, get_proper_type as get_proper_type
from typing import Callable, overload
from typing_extensions import Final, Literal, Protocol

ALLOW_INCOMPATIBLE_OVERRIDE: Final[Incomplete]
PRIORITY_FALLBACKS: Final[int]

class SemanticAnalyzerCoreInterface(metaclass=abc.ABCMeta):
    """A core abstract interface to generic semantic analyzer functionality.

    This is implemented by both semantic analyzer passes 2 and 3.
    """
    @abstractmethod
    def lookup_qualified(self, name: str, ctx: Context, suppress_errors: bool = False) -> SymbolTableNode | None: ...
    @abstractmethod
    def lookup_fully_qualified(self, name: str) -> SymbolTableNode: ...
    @abstractmethod
    def lookup_fully_qualified_or_none(self, name: str) -> SymbolTableNode | None: ...
    @abstractmethod
    def fail(self, msg: str, ctx: Context, serious: bool = False, *, blocker: bool = False, code: ErrorCode | None = None) -> None: ...
    @abstractmethod
    def note(self, msg: str, ctx: Context, *, code: ErrorCode | None = None) -> None: ...
    @abstractmethod
    def incomplete_feature_enabled(self, feature: str, ctx: Context) -> bool: ...
    @abstractmethod
    def record_incomplete_ref(self) -> None: ...
    @abstractmethod
    def defer(self, debug_context: Context | None = None, force_progress: bool = False) -> None: ...
    @abstractmethod
    def is_incomplete_namespace(self, fullname: str) -> bool:
        """Is a module or class namespace potentially missing some definitions?"""
    @property
    @abstractmethod
    def final_iteration(self) -> bool:
        """Is this the final iteration of semantic analysis?"""
    @abstractmethod
    def is_future_flag_set(self, flag: str) -> bool:
        """Is the specific __future__ feature imported"""
    @property
    @abstractmethod
    def is_stub_file(self) -> bool: ...
    @abstractmethod
    def is_func_scope(self) -> bool: ...
    @property
    @abstractmethod
    def type(self) -> TypeInfo | None: ...

class SemanticAnalyzerInterface(SemanticAnalyzerCoreInterface, metaclass=abc.ABCMeta):
    """A limited abstract interface to some generic semantic analyzer pass 2 functionality.

    We use this interface for various reasons:

    * Looser coupling
    * Cleaner import graph
    * Less need to pass around callback functions
    """
    tvar_scope: TypeVarLikeScope
    @abstractmethod
    def lookup(self, name: str, ctx: Context, suppress_errors: bool = False) -> SymbolTableNode | None: ...
    @abstractmethod
    def named_type(self, fullname: str, args: list[Type] | None = None) -> Instance: ...
    @abstractmethod
    def named_type_or_none(self, fullname: str, args: list[Type] | None = None) -> Instance | None: ...
    @abstractmethod
    def accept(self, node: Node) -> None: ...
    @abstractmethod
    def anal_type(self, t: Type, *, tvar_scope: TypeVarLikeScope | None = None, allow_tuple_literal: bool = False, allow_unbound_tvars: bool = False, allow_required: bool = False, allow_placeholder: bool = False, report_invalid_types: bool = True, prohibit_self_type: str | None = None) -> Type | None: ...
    @abstractmethod
    def get_and_bind_all_tvars(self, type_exprs: list[Expression]) -> list[TypeVarLikeType]: ...
    @abstractmethod
    def basic_new_typeinfo(self, name: str, basetype_or_fallback: Instance, line: int) -> TypeInfo: ...
    @abstractmethod
    def schedule_patch(self, priority: int, fn: Callable[[], None]) -> None: ...
    @abstractmethod
    def add_symbol_table_node(self, name: str, stnode: SymbolTableNode) -> bool:
        """Add node to the current symbol table."""
    @abstractmethod
    def current_symbol_table(self) -> SymbolTable:
        """Get currently active symbol table.

        May be module, class, or local namespace.
        """
    @abstractmethod
    def add_symbol(self, name: str, node: SymbolNode, context: Context, module_public: bool = True, module_hidden: bool = False, can_defer: bool = True) -> bool:
        """Add symbol to the current symbol table."""
    @abstractmethod
    def add_symbol_skip_local(self, name: str, node: SymbolNode) -> None:
        """Add symbol to the current symbol table, skipping locals.

        This is used to store symbol nodes in a symbol table that
        is going to be serialized (local namespaces are not serialized).
        See implementation docstring for more details.
        """
    @abstractmethod
    def parse_bool(self, expr: Expression) -> bool | None: ...
    @abstractmethod
    def qualified_name(self, n: str) -> str: ...
    @property
    @abstractmethod
    def is_typeshed_stub_file(self) -> bool: ...
    @abstractmethod
    def process_placeholder(self, name: str | None, kind: str, ctx: Context, force_progress: bool = False) -> None: ...

def set_callable_name(sig: Type, fdef: FuncDef) -> ProperType: ...
def calculate_tuple_fallback(typ: TupleType) -> None:
    """Calculate a precise item type for the fallback of a tuple type.

    This must be called only after the main semantic analysis pass, since joins
    aren't available before that.

    Note that there is an apparent chicken and egg problem with respect
    to verifying type arguments against bounds. Verifying bounds might
    require fallbacks, but we might use the bounds to calculate the
    fallbacks. In practice this is not a problem, since the worst that
    can happen is that we have invalid type argument values, and these
    can happen in later stages as well (they will generate errors, but
    we don't prevent their existence).
    """

class _NamedTypeCallback(Protocol):
    def __call__(self, fully_qualified_name: str, args: list[Type] | None = None) -> Instance: ...

def paramspec_args(name: str, fullname: str, id: TypeVarId | int, *, named_type_func: _NamedTypeCallback, line: int = -1, column: int = -1, prefix: Parameters | None = None) -> ParamSpecType: ...
def paramspec_kwargs(name: str, fullname: str, id: TypeVarId | int, *, named_type_func: _NamedTypeCallback, line: int = -1, column: int = -1, prefix: Parameters | None = None) -> ParamSpecType: ...

class HasPlaceholders(BoolTypeQuery):
    def __init__(self) -> None: ...
    def visit_placeholder_type(self, t: PlaceholderType) -> bool: ...

def has_placeholder(typ: Type) -> bool:
    """Check if a type contains any placeholder types (recursively)."""
def find_dataclass_transform_spec(node: Node | None) -> DataclassTransformSpec | None:
    """
    Find the dataclass transform spec for the given node, if any exists.

    Per PEP 681 (https://peps.python.org/pep-0681/#the-dataclass-transform-decorator), dataclass
    transforms can be specified in multiple ways, including decorator functions and
    metaclasses/base classes. This function resolves the spec from any of these variants.
    """
@overload
def require_bool_literal_argument(api: SemanticAnalyzerInterface | SemanticAnalyzerPluginInterface, expression: Expression, name: str, default: Literal[True] | Literal[False]) -> bool: ...
@overload
def require_bool_literal_argument(api: SemanticAnalyzerInterface | SemanticAnalyzerPluginInterface, expression: Expression, name: str, default: None = None) -> bool | None: ...
def parse_bool(expr: Expression) -> bool | None: ...
