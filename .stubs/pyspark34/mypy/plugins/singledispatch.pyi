from _typeshed import Incomplete
from mypy.messages import format_type as format_type
from mypy.nodes import ARG_POS as ARG_POS, Argument as Argument, Block as Block, ClassDef as ClassDef, Context as Context, SymbolTable as SymbolTable, TypeInfo as TypeInfo, Var as Var
from mypy.options import Options as Options
from mypy.plugin import CheckerPluginInterface as CheckerPluginInterface, FunctionContext as FunctionContext, MethodContext as MethodContext, MethodSigContext as MethodSigContext
from mypy.plugins.common import add_method_to_class as add_method_to_class
from mypy.subtypes import is_subtype as is_subtype
from mypy.types import AnyType as AnyType, CallableType as CallableType, FunctionLike as FunctionLike, Instance as Instance, NoneType as NoneType, Overloaded as Overloaded, Type as Type, TypeOfAny as TypeOfAny, get_proper_type as get_proper_type
from typing import NamedTuple, Sequence, TypeVar
from typing_extensions import Final, TypeAlias as _TypeAlias

class SingledispatchTypeVars(NamedTuple):
    return_type: Type
    fallback: CallableType

class RegisterCallableInfo(NamedTuple):
    register_type: Type
    singledispatch_obj: Instance

SINGLEDISPATCH_TYPE: Final[str]
SINGLEDISPATCH_REGISTER_METHOD: Final[Incomplete]
SINGLEDISPATCH_CALLABLE_CALL_METHOD: Final[Incomplete]

def get_singledispatch_info(typ: Instance) -> SingledispatchTypeVars | None: ...
T = TypeVar('T')

def get_first_arg(args: list[list[T]]) -> T | None:
    """Get the element that corresponds to the first argument passed to the function"""

REGISTER_RETURN_CLASS: Final[str]
REGISTER_CALLABLE_CALL_METHOD: Final[Incomplete]

def make_fake_register_class_instance(api: CheckerPluginInterface, type_args: Sequence[Type]) -> Instance: ...

PluginContext: _TypeAlias

def fail(ctx: PluginContext, msg: str, context: Context | None) -> None:
    """Emit an error message.

    This tries to emit an error message at the location specified by `context`, falling back to the
    location specified by `ctx.context`. This is helpful when the only context information about
    where you want to put the error message may be None (like it is for `CallableType.definition`)
    and falling back to the location of the calling function is fine."""
def create_singledispatch_function_callback(ctx: FunctionContext) -> Type:
    """Called for functools.singledispatch"""
def singledispatch_register_callback(ctx: MethodContext) -> Type:
    """Called for functools._SingleDispatchCallable.register"""
def register_function(ctx: PluginContext, singledispatch_obj: Instance, func: Type, options: Options, register_arg: Type | None = None) -> None:
    """Register a function"""
def get_dispatch_type(func: CallableType, register_arg: Type | None) -> Type | None: ...
def call_singledispatch_function_after_register_argument(ctx: MethodContext) -> Type:
    """Called on the function after passing a type to register"""
def call_singledispatch_function_callback(ctx: MethodSigContext) -> FunctionLike:
    """Called for functools._SingleDispatchCallable.__call__"""
