from mypy.nodes import ArgKind, ClassDef as ClassDef, Decorator as Decorator, FuncDef, FuncItem as FuncItem, LambdaExpr, OverloadedFuncDef as OverloadedFuncDef, SymbolNode as SymbolNode, TypeInfo as TypeInfo
from mypyc.common import LAMBDA_NAME as LAMBDA_NAME, PROPSET_PREFIX as PROPSET_PREFIX, SELF_NAME as SELF_NAME
from mypyc.ir.class_ir import ClassIR as ClassIR, NonExtClassInfo as NonExtClassInfo
from mypyc.ir.func_ir import FUNC_CLASSMETHOD as FUNC_CLASSMETHOD, FUNC_NORMAL as FUNC_NORMAL, FUNC_STATICMETHOD as FUNC_STATICMETHOD, FuncDecl as FuncDecl, FuncIR as FuncIR, FuncSignature as FuncSignature, RuntimeArg as RuntimeArg
from mypyc.ir.ops import BasicBlock as BasicBlock, GetAttr as GetAttr, InitStatic as InitStatic, Integer as Integer, LoadAddress as LoadAddress, LoadLiteral as LoadLiteral, Register as Register, Return as Return, SetAttr as SetAttr, Unbox as Unbox, Unreachable as Unreachable, Value as Value
from mypyc.ir.rtypes import RInstance as RInstance, bool_rprimitive as bool_rprimitive, dict_rprimitive as dict_rprimitive, int_rprimitive as int_rprimitive, object_rprimitive as object_rprimitive
from mypyc.irbuild.builder import IRBuilder as IRBuilder, SymbolTarget as SymbolTarget, gen_arg_defaults as gen_arg_defaults
from mypyc.irbuild.callable_class import add_call_to_callable_class as add_call_to_callable_class, add_get_to_callable_class as add_get_to_callable_class, instantiate_callable_class as instantiate_callable_class, setup_callable_class as setup_callable_class
from mypyc.irbuild.context import FuncInfo as FuncInfo, ImplicitClass as ImplicitClass
from mypyc.irbuild.env_class import finalize_env_class as finalize_env_class, load_env_registers as load_env_registers, load_outer_envs as load_outer_envs, setup_env_class as setup_env_class, setup_func_for_recursive_call as setup_func_for_recursive_call
from mypyc.irbuild.generator import add_methods_to_generator_class as add_methods_to_generator_class, add_raise_exception_blocks_to_generator_class as add_raise_exception_blocks_to_generator_class, create_switch_for_generator_class as create_switch_for_generator_class, gen_generator_func as gen_generator_func, populate_switch_for_generator_class as populate_switch_for_generator_class, setup_env_for_generator_class as setup_env_for_generator_class
from mypyc.irbuild.targets import AssignmentTarget as AssignmentTarget
from mypyc.irbuild.util import is_constant as is_constant
from mypyc.primitives.dict_ops import dict_get_method_with_none as dict_get_method_with_none, dict_new_op as dict_new_op, dict_set_item_op as dict_set_item_op
from mypyc.primitives.generic_ops import py_setattr_op as py_setattr_op
from mypyc.primitives.misc_ops import register_function as register_function
from mypyc.primitives.registry import builtin_names as builtin_names
from mypyc.sametype import is_same_method_signature as is_same_method_signature, is_same_type as is_same_type
from typing import NamedTuple, Sequence

def transform_func_def(builder: IRBuilder, fdef: FuncDef) -> None: ...
def transform_overloaded_func_def(builder: IRBuilder, o: OverloadedFuncDef) -> None: ...
def transform_decorator(builder: IRBuilder, dec: Decorator) -> None: ...
def transform_lambda_expr(builder: IRBuilder, expr: LambdaExpr) -> Value: ...
def gen_func_item(builder: IRBuilder, fitem: FuncItem, name: str, sig: FuncSignature, cdef: ClassDef | None = None) -> tuple[FuncIR, Value | None]:
    """Generate and return the FuncIR for a given FuncDef.

    If the given FuncItem is a nested function, then we generate a
    callable class representing the function and use that instead of
    the actual function. if the given FuncItem contains a nested
    function, then we generate an environment class so that inner
    nested functions can access the environment of the given FuncDef.

    Consider the following nested function:

        def a() -> None:
            def b() -> None:
                def c() -> None:
                    return None
                return None
            return None

    The classes generated would look something like the following.

                has pointer to        +-------+
        +-------------------------->  | a_env |
        |                             +-------+
        |                                 ^
        |                                 | has pointer to
    +-------+     associated with     +-------+
    | b_obj |   ------------------->  | b_env |
    +-------+                         +-------+
                                          ^
                                          |
    +-------+         has pointer to      |
    | c_obj |   --------------------------+
    +-------+
    """
def has_nested_func_self_reference(builder: IRBuilder, fitem: FuncItem) -> bool:
    """Does a nested function contain a self-reference in its body?

    If a nested function only has references in the surrounding function,
    we don't need to add it to the environment.
    """
def gen_func_ir(builder: IRBuilder, args: list[Register], blocks: list[BasicBlock], sig: FuncSignature, fn_info: FuncInfo, cdef: ClassDef | None, is_singledispatch_main_func: bool = False) -> tuple[FuncIR, Value | None]:
    """Generate the FuncIR for a function.

    This takes the basic blocks and function info of a particular
    function and returns the IR. If the function is nested,
    also returns the register containing the instance of the
    corresponding callable class.
    """
def handle_ext_method(builder: IRBuilder, cdef: ClassDef, fdef: FuncDef) -> None: ...
def handle_non_ext_method(builder: IRBuilder, non_ext: NonExtClassInfo, cdef: ClassDef, fdef: FuncDef) -> None: ...
def calculate_arg_defaults(builder: IRBuilder, fn_info: FuncInfo, func_reg: Value | None, symtable: dict[SymbolNode, SymbolTarget]) -> None:
    """Calculate default argument values and store them.

    They are stored in statics for top level functions and in
    the function objects for nested functions (while constants are
    still stored computed on demand).
    """
def gen_func_ns(builder: IRBuilder) -> str:
    """Generate a namespace for a nested function using its outer function names."""
def load_decorated_func(builder: IRBuilder, fdef: FuncDef, orig_func_reg: Value) -> Value:
    """Apply decorators to a function.

    Given a decorated FuncDef and an instance of the callable class
    representing that FuncDef, apply the corresponding decorator
    functions on that decorated FuncDef and return the decorated
    function.
    """
def is_decorated(builder: IRBuilder, fdef: FuncDef) -> bool: ...
def gen_glue(builder: IRBuilder, base_sig: FuncSignature, target: FuncIR, cls: ClassIR, base: ClassIR, fdef: FuncItem, *, do_py_ops: bool = False) -> FuncIR:
    '''Generate glue methods that mediate between different method types in subclasses.

    Works on both properties and methods. See gen_glue_methods below
    for more details.

    If do_py_ops is True, then the glue methods should use generic
    C API operations instead of direct calls, to enable generating
    "shadow" glue methods that work with interpreted subclasses.
    '''

class ArgInfo(NamedTuple):
    args: list[Value]
    arg_names: list[str | None]
    arg_kinds: list[ArgKind]

def get_args(builder: IRBuilder, rt_args: Sequence[RuntimeArg], line: int) -> ArgInfo: ...
def gen_glue_method(builder: IRBuilder, base_sig: FuncSignature, target: FuncIR, cls: ClassIR, base: ClassIR, line: int, do_pycall: bool) -> FuncIR:
    """Generate glue methods that mediate between different method types in subclasses.

    For example, if we have:

    class A:
        def f(builder: IRBuilder, x: int) -> object: ...

    then it is totally permissible to have a subclass

    class B(A):
        def f(builder: IRBuilder, x: object) -> int: ...

    since '(object) -> int' is a subtype of '(int) -> object' by the usual
    contra/co-variant function subtyping rules.

    The trickiness here is that int and object have different
    runtime representations in mypyc, so A.f and B.f have
    different signatures at the native C level. To deal with this,
    we need to generate glue methods that mediate between the
    different versions by coercing the arguments and return
    values.

    If do_pycall is True, then make the call using the C API
    instead of a native call.
    """
def check_native_override(builder: IRBuilder, base_sig: FuncSignature, sub_sig: FuncSignature, line: int) -> None:
    """Report an error if an override changes signature in unsupported ways.

    Glue methods can work around many signature changes but not all of them.
    """
def gen_glue_property(builder: IRBuilder, sig: FuncSignature, target: FuncIR, cls: ClassIR, base: ClassIR, line: int, do_pygetattr: bool) -> FuncIR:
    """Generate glue methods for properties that mediate between different subclass types.

    Similarly to methods, properties of derived types can be covariantly subtyped. Thus,
    properties also require glue. However, this only requires the return type to change.
    Further, instead of a method call, an attribute get is performed.

    If do_pygetattr is True, then get the attribute using the Python C
    API instead of a native call.
    """
def get_func_target(builder: IRBuilder, fdef: FuncDef) -> AssignmentTarget:
    """Given a FuncDef, return the target for the instance of its callable class.

    If the function was not already defined somewhere, then define it
    and add it to the current environment.
    """
def load_type(builder: IRBuilder, typ: TypeInfo, line: int) -> Value: ...
def load_func(builder: IRBuilder, func_name: str, fullname: str | None, line: int) -> Value: ...
def generate_singledispatch_dispatch_function(builder: IRBuilder, main_singledispatch_function_name: str, fitem: FuncDef) -> None: ...
def gen_calls_to_correct_impl(builder: IRBuilder, impl_to_use: Value, arg_info: ArgInfo, fitem: FuncDef, line: int) -> None: ...
def gen_dispatch_func_ir(builder: IRBuilder, fitem: FuncDef, main_func_name: str, dispatch_name: str, sig: FuncSignature) -> tuple[FuncIR, Value]:
    """Create a dispatch function (a function that checks the first argument type and dispatches
    to the correct implementation)
    """
def generate_dispatch_glue_native_function(builder: IRBuilder, fitem: FuncDef, callable_class_decl: FuncDecl, dispatch_name: str) -> FuncIR: ...
def generate_singledispatch_callable_class_ctor(builder: IRBuilder) -> None:
    """Create an __init__ that sets registry and dispatch_cache to empty dicts"""
def add_register_method_to_callable_class(builder: IRBuilder, fn_info: FuncInfo) -> None: ...
def load_singledispatch_registry(builder: IRBuilder, dispatch_func_obj: Value, line: int) -> Value: ...
def singledispatch_main_func_name(orig_name: str) -> str: ...
def get_registry_identifier(fitem: FuncDef) -> str: ...
def maybe_insert_into_registry_dict(builder: IRBuilder, fitem: FuncDef) -> None: ...
def get_native_impl_ids(builder: IRBuilder, singledispatch_func: FuncDef) -> dict[FuncDef, int]:
    """Return a dict of registered implementation to native implementation ID for all
    implementations
    """
def gen_property_getter_ir(builder: IRBuilder, func_decl: FuncDecl, cdef: ClassDef, is_trait: bool) -> FuncIR:
    """Generate an implicit trivial property getter for an attribute.

    These are used if an attribute can also be accessed as a property.
    """
def gen_property_setter_ir(builder: IRBuilder, func_decl: FuncDecl, cdef: ClassDef, is_trait: bool) -> FuncIR:
    """Generate an implicit trivial property setter for an attribute.

    These are used if an attribute can also be accessed as a property.
    """
