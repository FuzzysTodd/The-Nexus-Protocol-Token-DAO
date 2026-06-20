from _typeshed import Incomplete
from mypy.nodes import ArgKind
from mypyc.codegen.emit import AssignHandler as AssignHandler, Emitter as Emitter, ErrorHandler as ErrorHandler, GotoHandler as GotoHandler, ReturnHandler as ReturnHandler
from mypyc.common import BITMAP_BITS as BITMAP_BITS, BITMAP_TYPE as BITMAP_TYPE, DUNDER_PREFIX as DUNDER_PREFIX, NATIVE_PREFIX as NATIVE_PREFIX, PREFIX as PREFIX, bitmap_name as bitmap_name, use_vectorcall as use_vectorcall
from mypyc.ir.class_ir import ClassIR as ClassIR
from mypyc.ir.func_ir import FUNC_STATICMETHOD as FUNC_STATICMETHOD, FuncIR as FuncIR, RuntimeArg as RuntimeArg
from mypyc.ir.rtypes import RInstance as RInstance, RType as RType, is_bool_rprimitive as is_bool_rprimitive, is_int_rprimitive as is_int_rprimitive, is_object_rprimitive as is_object_rprimitive, object_rprimitive as object_rprimitive
from mypyc.namegen import NameGenerator as NameGenerator
from typing import Sequence

def wrapper_function_header(fn: FuncIR, names: NameGenerator) -> str:
    """Return header of a vectorcall wrapper function.

    See comment above for a summary of the arguments.
    """
def generate_traceback_code(fn: FuncIR, emitter: Emitter, source_path: str, module_name: str) -> str: ...
def make_arg_groups(args: list[RuntimeArg]) -> dict[ArgKind, list[RuntimeArg]]:
    """Group arguments by kind."""
def reorder_arg_groups(groups: dict[ArgKind, list[RuntimeArg]]) -> list[RuntimeArg]:
    """Reorder argument groups to match their order in a format string."""
def make_static_kwlist(args: list[RuntimeArg]) -> str: ...
def make_format_string(func_name: str | None, groups: dict[ArgKind, list[RuntimeArg]]) -> str:
    """Return a format string that specifies the accepted arguments.

    The format string is an extended subset of what is supported by
    PyArg_ParseTupleAndKeywords(). Only the type 'O' is used, and we
    also support some extensions:

    - Required keyword-only arguments are introduced after '@'
    - If the function receives *args or **kwargs, we add a '%' prefix

    Each group requires the previous groups' delimiters to be present
    first.

    These are used by both vectorcall and legacy wrapper functions.
    """
def generate_wrapper_function(fn: FuncIR, emitter: Emitter, source_path: str, module_name: str) -> None:
    """Generate a CPython-compatible vectorcall wrapper for a native function.

    In particular, this handles unboxing the arguments, calling the native function, and
    then boxing the return value.
    """
def legacy_wrapper_function_header(fn: FuncIR, names: NameGenerator) -> str: ...
def generate_legacy_wrapper_function(fn: FuncIR, emitter: Emitter, source_path: str, module_name: str) -> None:
    """Generates a CPython-compatible legacy wrapper for a native function.

    In particular, this handles unboxing the arguments, calling the native function, and
    then boxing the return value.
    """
def generate_dunder_wrapper(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str:
    """Generates a wrapper for native __dunder__ methods to be able to fit into the mapping
    protocol slot. This specifically means that the arguments are taken as *PyObjects and returned
    as *PyObjects.
    """
def generate_ipow_wrapper(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str:
    """Generate a wrapper for native __ipow__.

    Since __ipow__ fills a ternary slot, but almost no one defines __ipow__ to take three
    arguments, the wrapper needs to tweaked to force it to accept three arguments.
    """
def generate_bin_op_wrapper(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str:
    """Generates a wrapper for a native binary dunder method.

    The same wrapper that handles the forward method (e.g. __add__) also handles
    the corresponding reverse method (e.g. __radd__), if defined.

    Both arguments and the return value are PyObject *.
    """
def generate_bin_op_forward_only_wrapper(fn: FuncIR, emitter: Emitter, gen: WrapperGenerator) -> None: ...
def generate_bin_op_reverse_only_wrapper(fn: FuncIR, emitter: Emitter, gen: WrapperGenerator) -> None: ...
def generate_bin_op_both_wrappers(cl: ClassIR, fn: FuncIR, fn_rev: FuncIR, emitter: Emitter, gen: WrapperGenerator) -> None: ...
def generate_bin_op_reverse_dunder_call(fn: FuncIR, emitter: Emitter, rmethod: str) -> None: ...
def handle_third_pow_argument(fn: FuncIR, emitter: Emitter, gen: WrapperGenerator, *, if_unsupported: list[str]) -> None: ...

RICHCOMPARE_OPS: Incomplete

def generate_richcompare_wrapper(cl: ClassIR, emitter: Emitter) -> str | None:
    """Generates a wrapper for richcompare dunder methods."""
def generate_get_wrapper(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str:
    """Generates a wrapper for native __get__ methods."""
def generate_hash_wrapper(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str:
    """Generates a wrapper for native __hash__ methods."""
def generate_len_wrapper(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str:
    """Generates a wrapper for native __len__ methods."""
def generate_bool_wrapper(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str:
    """Generates a wrapper for native __bool__ methods."""
def generate_del_item_wrapper(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str:
    """Generates a wrapper for native __delitem__.

    This is only called from a combined __delitem__/__setitem__ wrapper.
    """
def generate_set_del_item_wrapper(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str:
    """Generates a wrapper for native __setitem__ method (also works for __delitem__).

    This is used with the mapping protocol slot. Arguments are taken as *PyObjects and we
    return a negative C int on error.

    Create a separate wrapper function for __delitem__ as needed and have the
    __setitem__ wrapper call it if the value is NULL. Return the name
    of the outer (__setitem__) wrapper.
    """
def generate_set_del_item_wrapper_inner(fn: FuncIR, emitter: Emitter, args: Sequence[RuntimeArg]) -> None: ...
def generate_contains_wrapper(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str:
    """Generates a wrapper for a native __contains__ method."""
def generate_wrapper_core(fn: FuncIR, emitter: Emitter, optional_args: list[RuntimeArg] | None = None, arg_names: list[str] | None = None, cleanups: list[str] | None = None, traceback_code: str | None = None) -> None:
    """Generates the core part of a wrapper function for a native function.

    This expects each argument as a PyObject * named obj_{arg} as a precondition.
    It converts the PyObject *s to the necessary types, checking and unboxing if necessary,
    makes the call, then boxes the result if necessary and returns it.
    """
def generate_arg_check(name: str, typ: RType, emitter: Emitter, error: ErrorHandler | None = None, *, optional: bool = False, raise_exception: bool = True, bitmap_arg_index: int = 0) -> None:
    """Insert a runtime check for argument and unbox if necessary.

    The object is named PyObject *obj_{}. This is expected to generate
    a value of name arg_{} (unboxed if necessary). For each primitive a runtime
    check ensures the correct type.
    """

class WrapperGenerator:
    """Helper that simplifies the generation of wrapper functions."""
    cl: Incomplete
    emitter: Incomplete
    cleanups: Incomplete
    optional_args: Incomplete
    traceback_code: str
    def __init__(self, cl: ClassIR | None, emitter: Emitter) -> None: ...
    target_name: Incomplete
    target_cname: Incomplete
    num_bitmap_args: Incomplete
    args: Incomplete
    arg_names: Incomplete
    ret_type: Incomplete
    def set_target(self, fn: FuncIR) -> None:
        """Set the wrapped function.

        It's fine to modify the attributes initialized here later to customize
        the wrapper function.
        """
    def wrapper_name(self) -> str:
        """Return the name of the wrapper function."""
    def use_goto(self) -> bool:
        """Do we use a goto for error handling (instead of straight return)?"""
    def emit_header(self) -> None:
        """Emit the function header of the wrapper implementation."""
    def emit_arg_processing(self, error: ErrorHandler | None = None, raise_exception: bool = True) -> None:
        """Emit validation and unboxing of arguments."""
    def emit_call(self, not_implemented_handler: str = '') -> None:
        """Emit call to the wrapper function.

        If not_implemented_handler is non-empty, use this C code to handle
        a NotImplemented return value (if it's possible based on the return type).
        """
    def error(self) -> ErrorHandler:
        """Figure out how to deal with errors in the wrapper."""
    def emit_error_handling(self) -> None:
        """Emit error handling block at the end of the wrapper, if needed."""
    def finish(self) -> None: ...
