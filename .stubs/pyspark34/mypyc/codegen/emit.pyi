from _typeshed import Incomplete
from mypyc.codegen.literals import Literals as Literals
from mypyc.common import ATTR_PREFIX as ATTR_PREFIX, BITMAP_BITS as BITMAP_BITS, FAST_ISINSTANCE_MAX_SUBCLASSES as FAST_ISINSTANCE_MAX_SUBCLASSES, NATIVE_PREFIX as NATIVE_PREFIX, REG_PREFIX as REG_PREFIX, STATIC_PREFIX as STATIC_PREFIX, TYPE_PREFIX as TYPE_PREFIX, use_vectorcall as use_vectorcall
from mypyc.ir.class_ir import ClassIR as ClassIR, all_concrete_classes as all_concrete_classes
from mypyc.ir.func_ir import FuncDecl as FuncDecl
from mypyc.ir.ops import BasicBlock as BasicBlock, Value as Value
from mypyc.ir.rtypes import RInstance as RInstance, RPrimitive as RPrimitive, RTuple as RTuple, RType as RType, RUnion as RUnion, int_rprimitive as int_rprimitive, is_bit_rprimitive as is_bit_rprimitive, is_bool_rprimitive as is_bool_rprimitive, is_bytes_rprimitive as is_bytes_rprimitive, is_dict_rprimitive as is_dict_rprimitive, is_fixed_width_rtype as is_fixed_width_rtype, is_float_rprimitive as is_float_rprimitive, is_int16_rprimitive as is_int16_rprimitive, is_int32_rprimitive as is_int32_rprimitive, is_int64_rprimitive as is_int64_rprimitive, is_int_rprimitive as is_int_rprimitive, is_list_rprimitive as is_list_rprimitive, is_none_rprimitive as is_none_rprimitive, is_object_rprimitive as is_object_rprimitive, is_optional_type as is_optional_type, is_range_rprimitive as is_range_rprimitive, is_set_rprimitive as is_set_rprimitive, is_short_int_rprimitive as is_short_int_rprimitive, is_str_rprimitive as is_str_rprimitive, is_tuple_rprimitive as is_tuple_rprimitive, is_uint8_rprimitive as is_uint8_rprimitive, object_rprimitive as object_rprimitive, optional_value_type as optional_value_type
from mypyc.namegen import NameGenerator as NameGenerator, exported_name as exported_name
from mypyc.sametype import is_same_type as is_same_type
from typing import Callable, Final

DEBUG_ERRORS: Final[bool]

class HeaderDeclaration:
    """A representation of a declaration in C.

    This is used to generate declarations in header files and
    (optionally) definitions in source files.

    Attributes:
      decl: C source code for the declaration.
      defn: Optionally, C source code for a definition.
      dependencies: The names of any objects that must be declared prior.
      is_type: Whether the declaration is of a C type. (C types will be declared in
               external header files and not marked 'extern'.)
      needs_export: Whether the declared object needs to be exported to
                    other modules in the linking table.
    """
    decl: Incomplete
    defn: Incomplete
    dependencies: Incomplete
    is_type: Incomplete
    needs_export: Incomplete
    def __init__(self, decl: str | list[str], defn: list[str] | None = None, *, dependencies: set[str] | None = None, is_type: bool = False, needs_export: bool = False) -> None: ...

class EmitterContext:
    """Shared emitter state for a compilation group."""
    temp_counter: int
    names: Incomplete
    group_name: Incomplete
    group_map: Incomplete
    group_deps: Incomplete
    declarations: Incomplete
    literals: Incomplete
    def __init__(self, names: NameGenerator, group_name: str | None = None, group_map: dict[str, str | None] | None = None) -> None:
        """Setup shared emitter state.

        Args:
            names: The name generator to use
            group_map: Map from module names to group name
            group_name: Current group name
        """

class ErrorHandler:
    """Describes handling errors in unbox/cast operations."""
class AssignHandler(ErrorHandler):
    """Assign an error value on error."""

class GotoHandler(ErrorHandler):
    """Goto label on error."""
    label: Incomplete
    def __init__(self, label: str) -> None: ...

class TracebackAndGotoHandler(ErrorHandler):
    """Add traceback item and goto label on error."""
    label: Incomplete
    source_path: Incomplete
    module_name: Incomplete
    traceback_entry: Incomplete
    def __init__(self, label: str, source_path: str, module_name: str, traceback_entry: tuple[str, int]) -> None: ...

class ReturnHandler(ErrorHandler):
    """Return a constant value on error."""
    value: Incomplete
    def __init__(self, value: str) -> None: ...

class Emitter:
    """Helper for C code generation."""
    context: Incomplete
    capi_version: Incomplete
    names: Incomplete
    value_names: Incomplete
    fragments: Incomplete
    def __init__(self, context: EmitterContext, value_names: dict[Value, str] | None = None, capi_version: tuple[int, int] | None = None) -> None: ...
    def indent(self) -> None: ...
    def dedent(self) -> None: ...
    def label(self, label: BasicBlock) -> str: ...
    def reg(self, reg: Value) -> str: ...
    def attr(self, name: str) -> str: ...
    def object_annotation(self, obj: object, line: str) -> str:
        """Build a C comment with an object's string represention.

        If the comment exceeds the line length limit, it's wrapped into a
        multiline string (with the extra lines indented to be aligned with
        the first line's comment).

        If it contains illegal characters, an empty string is returned."""
    def emit_line(self, line: str = '', *, ann: object = None) -> None: ...
    def emit_lines(self, *lines: str) -> None: ...
    def emit_label(self, label: BasicBlock | str) -> None: ...
    def emit_from_emitter(self, emitter: Emitter) -> None: ...
    def emit_printf(self, fmt: str, *args: str) -> None: ...
    def temp_name(self) -> str: ...
    def new_label(self) -> str: ...
    def get_module_group_prefix(self, module_name: str) -> str:
        """Get the group prefix for a module (relative to the current group).

        The prefix should be prepended to the object name whenever
        accessing an object from this module.

        If the module lives is in the current compilation group, there is
        no prefix.  But if it lives in a different group (and hence a separate
        extension module), we need to access objects from it indirectly via an
        export table.

        For example, for code in group `a` to call a function `bar` in group `b`,
        it would need to do `exports_b.CPyDef_bar(...)`, while code that is
        also in group `b` can simply do `CPyDef_bar(...)`.

        Thus the prefix for a module in group `b` is 'exports_b.' if the current
        group is *not* b and just '' if it is.
        """
    def get_group_prefix(self, obj: ClassIR | FuncDecl) -> str:
        """Get the group prefix for an object."""
    def static_name(self, id: str, module: str | None, prefix: str = ...) -> str:
        """Create name of a C static variable.

        These are used for literals and imported modules, among other
        things.

        The caller should ensure that the (id, module) pair cannot
        overlap with other calls to this method within a compilation
        group.
        """
    def type_struct_name(self, cl: ClassIR) -> str: ...
    def ctype(self, rtype: RType) -> str: ...
    def ctype_spaced(self, rtype: RType) -> str:
        """Adds a space after ctype for non-pointers."""
    def c_undefined_value(self, rtype: RType) -> str: ...
    def c_error_value(self, rtype: RType) -> str: ...
    def native_function_name(self, fn: FuncDecl) -> str: ...
    def tuple_c_declaration(self, rtuple: RTuple) -> list[str]: ...
    def bitmap_field(self, index: int) -> str:
        """Return C field name used for attribute bitmap."""
    def attr_bitmap_expr(self, obj: str, cl: ClassIR, index: int) -> str:
        """Return reference to the attribute definedness bitmap."""
    def emit_attr_bitmap_set(self, value: str, obj: str, rtype: RType, cl: ClassIR, attr: str) -> None:
        """Mark an attribute as defined in the attribute bitmap.

        Assumes that the attribute is tracked in the bitmap (only some attributes
        use the bitmap). If 'value' is not equal to the error value, do nothing.
        """
    def emit_attr_bitmap_clear(self, obj: str, rtype: RType, cl: ClassIR, attr: str) -> None:
        """Mark an attribute as undefined in the attribute bitmap.

        Unlike emit_attr_bitmap_set, clear unconditionally.
        """
    def use_vectorcall(self) -> bool: ...
    def emit_undefined_attr_check(self, rtype: RType, attr_expr: str, compare: str, obj: str, attr: str, cl: ClassIR, *, unlikely: bool = False) -> None: ...
    def error_value_check(self, rtype: RType, value: str, compare: str) -> str: ...
    def tuple_undefined_check_cond(self, rtuple: RTuple, tuple_expr_in_c: str, c_type_compare_val: Callable[[RType], str], compare: str, *, check_exception: bool = True) -> str: ...
    def tuple_undefined_value(self, rtuple: RTuple) -> str:
        """Undefined tuple value suitable in an expression."""
    def c_initializer_undefined_value(self, rtype: RType) -> str:
        """Undefined value represented in a form suitable for variable initialization."""
    def declare_tuple_struct(self, tuple_type: RTuple) -> None: ...
    def emit_inc_ref(self, dest: str, rtype: RType, *, rare: bool = False) -> None:
        """Increment reference count of C expression `dest`.

        For composite unboxed structures (e.g. tuples) recursively
        increment reference counts for each component.

        If rare is True, optimize for code size and compilation speed.
        """
    def emit_dec_ref(self, dest: str, rtype: RType, *, is_xdec: bool = False, rare: bool = False) -> None:
        """Decrement reference count of C expression `dest`.

        For composite unboxed structures (e.g. tuples) recursively
        decrement reference counts for each component.

        If rare is True, optimize for code size and compilation speed.
        """
    def pretty_name(self, typ: RType) -> str: ...
    def emit_cast(self, src: str, dest: str, typ: RType, *, declare_dest: bool = False, error: ErrorHandler | None = None, raise_exception: bool = True, optional: bool = False, src_type: RType | None = None, likely: bool = True) -> None:
        """Emit code for casting a value of given type.

        Somewhat strangely, this supports unboxed types but only
        operates on boxed versions.  This is necessary to properly
        handle types such as Optional[int] in compatibility glue.

        By default, assign NULL (error value) to dest if the value has
        an incompatible type and raise TypeError. These can be customized
        using 'error' and 'raise_exception'.

        Always copy/steal the reference in 'src'.

        Args:
            src: Name of source C variable
            dest: Name of target C variable
            typ: Type of value
            declare_dest: If True, also declare the variable 'dest'
            error: What happens on error
            raise_exception: If True, also raise TypeError on failure
            likely: If the cast is likely to succeed (can be False for unions)
        """
    def emit_cast_error_handler(self, error: ErrorHandler, src: str, dest: str, typ: RType, raise_exception: bool) -> None: ...
    def emit_union_cast(self, src: str, dest: str, typ: RUnion, declare_dest: bool, error: ErrorHandler, optional: bool, src_type: RType | None, raise_exception: bool) -> None:
        """Emit cast to a union type.

        The arguments are similar to emit_cast.
        """
    def emit_tuple_cast(self, src: str, dest: str, typ: RTuple, declare_dest: bool, error: ErrorHandler, src_type: RType | None) -> None:
        """Emit cast to a tuple type.

        The arguments are similar to emit_cast.
        """
    def emit_arg_check(self, src: str, dest: str, typ: RType, check: str, optional: bool) -> None: ...
    def emit_unbox(self, src: str, dest: str, typ: RType, *, declare_dest: bool = False, error: ErrorHandler | None = None, raise_exception: bool = True, optional: bool = False, borrow: bool = False) -> None:
        """Emit code for unboxing a value of given type (from PyObject *).

        By default, assign error value to dest if the value has an
        incompatible type and raise TypeError. These can be customized
        using 'error' and 'raise_exception'.

        Generate a new reference unless 'borrow' is True.

        Args:
            src: Name of source C variable
            dest: Name of target C variable
            typ: Type of value
            declare_dest: If True, also declare the variable 'dest'
            error: What happens on error
            raise_exception: If True, also raise TypeError on failure
            borrow: If True, create a borrowed reference

        """
    def emit_box(self, src: str, dest: str, typ: RType, declare_dest: bool = False, can_borrow: bool = False) -> None:
        """Emit code for boxing a value of given type.

        Generate a simple assignment if no boxing is needed.

        The source reference count is stolen for the result (no need to decref afterwards).
        """
    def emit_error_check(self, value: str, rtype: RType, failure: str) -> None:
        """Emit code for checking a native function return value for uncaught exception."""
    def emit_gc_visit(self, target: str, rtype: RType) -> None:
        """Emit code for GC visiting a C variable reference.

        Assume that 'target' represents a C expression that refers to a
        struct member, such as 'self->x'.
        """
    def emit_gc_clear(self, target: str, rtype: RType) -> None:
        """Emit code for clearing a C attribute reference for GC.

        Assume that 'target' represents a C expression that refers to a
        struct member, such as 'self->x'.
        """
    def emit_traceback(self, source_path: str, module_name: str, traceback_entry: tuple[str, int]) -> None: ...
    def emit_type_error_traceback(self, source_path: str, module_name: str, traceback_entry: tuple[str, int], *, typ: RType, src: str) -> None: ...
    def emit_unbox_failure_with_overlapping_error_value(self, dest: str, typ: RType, failure: str) -> None: ...

def c_array_initializer(components: list[str], *, indented: bool = False) -> str:
    '''Construct an initializer for a C array variable.

    Components are C expressions valid in an initializer.

    For example, if components are ["1", "2"], the result
    would be "{1, 2}", which can be used like this:

        int a[] = {1, 2};

    If the result is long, split it into multiple lines.
    '''
