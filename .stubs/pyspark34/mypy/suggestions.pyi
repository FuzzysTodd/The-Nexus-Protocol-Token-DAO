from _typeshed import Incomplete
from mypy.argmap import map_actuals_to_formals as map_actuals_to_formals
from mypy.build import Graph as Graph, State as State
from mypy.checkexpr import has_any_type as has_any_type
from mypy.find_sources import InvalidSourceList as InvalidSourceList, SourceFinder as SourceFinder
from mypy.join import join_type_list as join_type_list
from mypy.meet import meet_type_list as meet_type_list
from mypy.modulefinder import PYTHON_EXTENSIONS as PYTHON_EXTENSIONS
from mypy.nodes import ARG_STAR as ARG_STAR, ARG_STAR2 as ARG_STAR2, ArgKind as ArgKind, CallExpr as CallExpr, Decorator as Decorator, Expression as Expression, FuncDef as FuncDef, MypyFile as MypyFile, RefExpr as RefExpr, ReturnStmt as ReturnStmt, SymbolNode as SymbolNode, SymbolTable as SymbolTable, TypeInfo as TypeInfo, reverse_builtin_aliases as reverse_builtin_aliases
from mypy.options import Options as Options
from mypy.plugin import FunctionContext as FunctionContext, MethodContext as MethodContext, Plugin as Plugin
from mypy.server.update import FineGrainedBuildManager as FineGrainedBuildManager
from mypy.state import state as state
from mypy.traverser import TraverserVisitor as TraverserVisitor
from mypy.typeops import make_simplified_union as make_simplified_union
from mypy.types import AnyType as AnyType, CallableType as CallableType, FunctionLike as FunctionLike, Instance as Instance, NoneType as NoneType, ProperType as ProperType, TupleType as TupleType, Type as Type, TypeAliasType as TypeAliasType, TypeOfAny as TypeOfAny, TypeStrVisitor as TypeStrVisitor, TypeTranslator as TypeTranslator, TypeVarType as TypeVarType, TypedDictType as TypedDictType, UninhabitedType as UninhabitedType, UnionType as UnionType, get_proper_type as get_proper_type
from mypy.types_utils import is_optional as is_optional, remove_optional as remove_optional
from mypy.util import split_target as split_target
from typing import Callable, Iterator, NamedTuple, TypeVar
from typing_extensions import TypedDict

class PyAnnotateSignature(TypedDict):
    return_type: str
    arg_types: list[str]

class Callsite(NamedTuple):
    path: str
    line: int
    arg_kinds: list[list[ArgKind]]
    callee_arg_names: list[str | None]
    arg_names: list[list[str | None]]
    arg_types: list[list[Type]]

class SuggestionPlugin(Plugin):
    """Plugin that records all calls to a given target."""
    target: Incomplete
    mystery_hits: Incomplete
    def __init__(self, target: str) -> None: ...
    def get_function_hook(self, fullname: str) -> Callable[[FunctionContext], Type] | None: ...
    def get_method_hook(self, fullname: str) -> Callable[[MethodContext], Type] | None: ...
    def log(self, ctx: FunctionContext | MethodContext) -> Type: ...

class ReturnFinder(TraverserVisitor):
    """Visitor for finding all types returned from a function."""
    typemap: Incomplete
    return_types: Incomplete
    def __init__(self, typemap: dict[Expression, Type]) -> None: ...
    def visit_return_stmt(self, o: ReturnStmt) -> None: ...
    def visit_func_def(self, o: FuncDef) -> None: ...

def get_return_types(typemap: dict[Expression, Type], func: FuncDef) -> list[Type]:
    """Find all the types returned by return statements in func."""

class ArgUseFinder(TraverserVisitor):
    """Visitor for finding all the types of arguments that each arg is passed to.

    This is extremely simple minded but might be effective anyways.
    """
    typemap: Incomplete
    arg_types: Incomplete
    def __init__(self, func: FuncDef, typemap: dict[Expression, Type]) -> None: ...
    def visit_call_expr(self, o: CallExpr) -> None: ...

def get_arg_uses(typemap: dict[Expression, Type], func: FuncDef) -> list[list[Type]]:
    """Find all the types of arguments that each arg is passed to.

    For example, given
      def foo(x: int) -> None: ...
      def bar(x: str) -> None: ...
      def test(x, y):
          foo(x)
          bar(y)

    this will return [[int], [str]].
    """

class SuggestionFailure(Exception): ...

def is_explicit_any(typ: AnyType) -> bool: ...
def is_implicit_any(typ: Type) -> bool: ...

class SuggestionEngine:
    """Engine for finding call sites and suggesting signatures."""
    fgmanager: Incomplete
    manager: Incomplete
    plugin: Incomplete
    graph: Incomplete
    finder: Incomplete
    give_json: Incomplete
    no_errors: Incomplete
    flex_any: Incomplete
    max_guesses: Incomplete
    use_fixme: Incomplete
    def __init__(self, fgmanager: FineGrainedBuildManager, *, json: bool, no_errors: bool = False, no_any: bool = False, flex_any: float | None = None, use_fixme: str | None = None, max_guesses: int | None = None) -> None: ...
    def suggest(self, function: str) -> str:
        """Suggest an inferred type for function."""
    def suggest_callsites(self, function: str) -> str:
        """Find a list of call sites of function."""
    def restore_after(self, module: str) -> Iterator[None]:
        """Context manager that reloads a module after executing the body.

        This should undo any damage done to the module state while mucking around.
        """
    def with_export_types(self) -> Iterator[None]:
        """Context manager that enables the export_types flag in the body.

        This causes type information to be exported into the manager's all_types variable.
        """
    def get_trivial_type(self, fdef: FuncDef) -> CallableType:
        """Generate a trivial callable type from a func def, with all Anys"""
    def get_starting_type(self, fdef: FuncDef) -> CallableType: ...
    def get_args(self, is_method: bool, base: CallableType, defaults: list[Type | None], callsites: list[Callsite], uses: list[list[Type]]) -> list[list[Type]]:
        """Produce a list of type suggestions for each argument type."""
    def get_default_arg_types(self, fdef: FuncDef) -> list[Type | None]: ...
    def get_guesses(self, is_method: bool, base: CallableType, defaults: list[Type | None], callsites: list[Callsite], uses: list[list[Type]]) -> list[CallableType]:
        """Compute a list of guesses for a function's type.

        This focuses just on the argument types, and doesn't change the provided return type.
        """
    def get_callsites(self, func: FuncDef) -> tuple[list[Callsite], list[str]]:
        """Find all call sites of a function."""
    def filter_options(self, guesses: list[CallableType], is_method: bool, ignore_return: bool) -> list[CallableType]:
        """Apply any configured filters to the possible guesses.

        Currently the only option is filtering based on Any prevalance."""
    def find_best(self, func: FuncDef, guesses: list[CallableType]) -> tuple[CallableType, int]:
        '''From a list of possible function types, find the best one.

        For best, we want the fewest errors, then the best "score" from score_callable.
        '''
    def get_guesses_from_parent(self, node: FuncDef) -> list[CallableType]:
        """Try to get a guess of a method type from a parent class."""
    def get_suggestion(self, mod: str, node: FuncDef) -> PyAnnotateSignature:
        """Compute a suggestion for a function.

        Return the type and whether the first argument should be ignored.
        """
    def format_args(self, arg_kinds: list[list[ArgKind]], arg_names: list[list[str | None]], arg_types: list[list[Type]]) -> str: ...
    def find_node(self, key: str) -> tuple[str, str, FuncDef]:
        """From a target name, return module/target names and the func def.

        The 'key' argument can be in one of two formats:
        * As the function full name, e.g., package.module.Cls.method
        * As the function location as file and line separated by column,
          e.g., path/to/file.py:42
        """
    def find_node_by_module_and_name(self, modname: str, tail: str) -> SymbolNode | None:
        """Find symbol node by module id and qualified name.

        Raise SuggestionFailure if can't find one.
        """
    def find_node_by_file_and_line(self, file: str, line: int) -> tuple[str, SymbolNode]:
        """Find symbol node by path to file and line number.

        Find the first function declared *before or on* the line number.

        Return module id and the node found. Raise SuggestionFailure if can't find one.
        """
    def extract_from_decorator(self, node: Decorator) -> FuncDef | None: ...
    def try_type(self, func: FuncDef, typ: ProperType) -> list[str]:
        """Recheck a function while assuming it has type typ.

        Return all error messages.
        """
    def reload(self, state: State) -> list[str]:
        """Recheck the module given by state."""
    def ensure_loaded(self, state: State, force: bool = False) -> MypyFile:
        """Make sure that the module represented by state is fully loaded."""
    def named_type(self, s: str) -> Instance: ...
    def json_suggestion(self, mod: str, func_name: str, node: FuncDef, suggestion: PyAnnotateSignature) -> str:
        """Produce a json blob for a suggestion suitable for application by pyannotate."""
    def pyannotate_signature(self, cur_module: str | None, is_method: bool, typ: CallableType) -> PyAnnotateSignature:
        """Format a callable type as a pyannotate dict"""
    def format_signature(self, sig: PyAnnotateSignature) -> str:
        """Format a callable type in a way suitable as an annotation... kind of"""
    def format_type(self, cur_module: str | None, typ: Type) -> str: ...
    def score_type(self, t: Type, arg_pos: bool) -> int:
        """Generate a score for a type that we use to pick which type to use.

        Lower is better, prefer non-union/non-any types. Don't penalize optionals.
        """
    def score_callable(self, t: CallableType) -> int: ...

def any_score_type(ut: Type, arg_pos: bool) -> float:
    """Generate a very made up number representing the Anyness of a type.

    Higher is better, 1.0 is max
    """
def any_score_callable(t: CallableType, is_method: bool, ignore_return: bool) -> float: ...
def is_tricky_callable(t: CallableType) -> bool:
    """Is t a callable that we need to put a ... in for syntax reasons?"""

class TypeFormatter(TypeStrVisitor):
    """Visitor used to format types"""
    module: Incomplete
    graph: Incomplete
    def __init__(self, module: str | None, graph: Graph, options: Options) -> None: ...
    def visit_any(self, t: AnyType) -> str: ...
    def visit_instance(self, t: Instance) -> str: ...
    def visit_tuple_type(self, t: TupleType) -> str: ...
    def visit_uninhabited_type(self, t: UninhabitedType) -> str: ...
    def visit_typeddict_type(self, t: TypedDictType) -> str: ...
    def visit_union_type(self, t: UnionType) -> str: ...
    def visit_callable_type(self, t: CallableType) -> str: ...
TType = TypeVar('TType', bound=Type)

def make_suggestion_anys(t: TType) -> TType:
    """Make all anys in the type as coming from the suggestion engine.

    This keeps those Anys from influencing constraint generation,
    which allows us to do better when refining types.
    """

class MakeSuggestionAny(TypeTranslator):
    def visit_any(self, t: AnyType) -> Type: ...
    def visit_type_alias_type(self, t: TypeAliasType) -> Type: ...

def generate_type_combinations(types: list[Type]) -> list[Type]:
    """Generate possible combinations of a list of types.

    mypy essentially supports two different ways to do this: joining the types
    and unioning the types. We try both.
    """
def count_errors(msgs: list[str]) -> int: ...
def refine_type(ti: Type, si: Type) -> Type:
    """Refine `ti` by replacing Anys in it with information taken from `si`

    This basically works by, when the types have the same structure,
    traversing both of them in parallel and replacing Any on the left
    with whatever the type on the right is. If the types don't have the
    same structure (or aren't supported), the left type is chosen.

    For example:
      refine(Any, T) = T,  for all T
      refine(float, int) = float
      refine(List[Any], List[int]) = List[int]
      refine(Dict[int, Any], Dict[Any, int]) = Dict[int, int]
      refine(Tuple[int, Any], Tuple[Any, int]) = Tuple[int, int]

      refine(Callable[[Any], Any], Callable[[int], int]) = Callable[[int], int]
      refine(Callable[..., int], Callable[[int, float], Any]) = Callable[[int, float], int]

      refine(Optional[Any], int) = Optional[int]
      refine(Optional[Any], Optional[int]) = Optional[int]
      refine(Optional[Any], Union[int, str]) = Optional[Union[int, str]]
      refine(Optional[List[Any]], List[int]) = List[int]

    """
def refine_union(t: UnionType, s: ProperType) -> Type:
    """Refine a union type based on another type.

    This is done by refining every component of the union against the
    right hand side type (or every component of its union if it is
    one). If an element of the union is successfully refined, we drop it
    from the union in favor of the refined versions.
    """
def refine_callable(t: CallableType, s: CallableType) -> CallableType:
    """Refine a callable based on another.

    See comments for refine_type.
    """
T = TypeVar('T')

def dedup(old: list[T]) -> list[T]: ...
