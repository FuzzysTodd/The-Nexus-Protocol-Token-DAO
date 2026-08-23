from _typeshed import Incomplete
from mypy.nodes import ArgKind as ArgKind
from mypyc.common import BITMAP_BITS as BITMAP_BITS, FAST_ISINSTANCE_MAX_SUBCLASSES as FAST_ISINSTANCE_MAX_SUBCLASSES, MAX_LITERAL_SHORT_INT as MAX_LITERAL_SHORT_INT, MAX_SHORT_INT as MAX_SHORT_INT, MIN_LITERAL_SHORT_INT as MIN_LITERAL_SHORT_INT, MIN_SHORT_INT as MIN_SHORT_INT, PLATFORM_SIZE as PLATFORM_SIZE, use_method_vectorcall as use_method_vectorcall, use_vectorcall as use_vectorcall
from mypyc.errors import Errors as Errors
from mypyc.ir.class_ir import ClassIR as ClassIR, all_concrete_classes as all_concrete_classes
from mypyc.ir.func_ir import FuncDecl as FuncDecl, FuncSignature as FuncSignature
from mypyc.ir.ops import Assign as Assign, AssignMulti as AssignMulti, BasicBlock as BasicBlock, Box as Box, Branch as Branch, Call as Call, CallC as CallC, Cast as Cast, ComparisonOp as ComparisonOp, ERR_FALSE as ERR_FALSE, ERR_NEVER as ERR_NEVER, Extend as Extend, Float as Float, FloatComparisonOp as FloatComparisonOp, FloatNeg as FloatNeg, FloatOp as FloatOp, GetAttr as GetAttr, GetElementPtr as GetElementPtr, Goto as Goto, IntOp as IntOp, Integer as Integer, KeepAlive as KeepAlive, LoadAddress as LoadAddress, LoadErrorValue as LoadErrorValue, LoadLiteral as LoadLiteral, LoadMem as LoadMem, LoadStatic as LoadStatic, MethodCall as MethodCall, NAMESPACE_MODULE as NAMESPACE_MODULE, NAMESPACE_STATIC as NAMESPACE_STATIC, NAMESPACE_TYPE as NAMESPACE_TYPE, Op as Op, RaiseStandardError as RaiseStandardError, Register as Register, SetMem as SetMem, Truncate as Truncate, TupleGet as TupleGet, TupleSet as TupleSet, Unbox as Unbox, Unreachable as Unreachable, Value as Value, float_comparison_op_to_id as float_comparison_op_to_id, float_op_to_id as float_op_to_id, int_op_to_id as int_op_to_id
from mypyc.ir.rtypes import PyListObject as PyListObject, PyObject as PyObject, PySetObject as PySetObject, PyVarObject as PyVarObject, RArray as RArray, RInstance as RInstance, RPrimitive as RPrimitive, RTuple as RTuple, RType as RType, RUnion as RUnion, bit_rprimitive as bit_rprimitive, bitmap_rprimitive as bitmap_rprimitive, bool_rprimitive as bool_rprimitive, bytes_rprimitive as bytes_rprimitive, c_int_rprimitive as c_int_rprimitive, c_pointer_rprimitive as c_pointer_rprimitive, c_pyssize_t_rprimitive as c_pyssize_t_rprimitive, c_size_t_rprimitive as c_size_t_rprimitive, check_native_int_range as check_native_int_range, dict_rprimitive as dict_rprimitive, float_rprimitive as float_rprimitive, int_rprimitive as int_rprimitive, is_bit_rprimitive as is_bit_rprimitive, is_bool_rprimitive as is_bool_rprimitive, is_bytes_rprimitive as is_bytes_rprimitive, is_dict_rprimitive as is_dict_rprimitive, is_fixed_width_rtype as is_fixed_width_rtype, is_float_rprimitive as is_float_rprimitive, is_int16_rprimitive as is_int16_rprimitive, is_int32_rprimitive as is_int32_rprimitive, is_int64_rprimitive as is_int64_rprimitive, is_int_rprimitive as is_int_rprimitive, is_list_rprimitive as is_list_rprimitive, is_none_rprimitive as is_none_rprimitive, is_set_rprimitive as is_set_rprimitive, is_short_int_rprimitive as is_short_int_rprimitive, is_str_rprimitive as is_str_rprimitive, is_tagged as is_tagged, is_tuple_rprimitive as is_tuple_rprimitive, is_uint8_rprimitive as is_uint8_rprimitive, list_rprimitive as list_rprimitive, none_rprimitive as none_rprimitive, object_pointer_rprimitive as object_pointer_rprimitive, object_rprimitive as object_rprimitive, optional_value_type as optional_value_type, pointer_rprimitive as pointer_rprimitive, short_int_rprimitive as short_int_rprimitive, str_rprimitive as str_rprimitive
from mypyc.irbuild.mapper import Mapper as Mapper
from mypyc.irbuild.util import concrete_arg_kind as concrete_arg_kind
from mypyc.options import CompilerOptions as CompilerOptions
from mypyc.primitives.bytes_ops import bytes_compare as bytes_compare
from mypyc.primitives.dict_ops import dict_build_op as dict_build_op, dict_new_op as dict_new_op, dict_ssize_t_size_op as dict_ssize_t_size_op, dict_update_in_display_op as dict_update_in_display_op
from mypyc.primitives.exc_ops import err_occurred_op as err_occurred_op, keep_propagating_op as keep_propagating_op
from mypyc.primitives.float_ops import copysign_op as copysign_op, int_to_float_op as int_to_float_op
from mypyc.primitives.generic_ops import generic_len_op as generic_len_op, generic_ssize_t_len_op as generic_ssize_t_len_op, py_call_op as py_call_op, py_call_with_kwargs_op as py_call_with_kwargs_op, py_getattr_op as py_getattr_op, py_method_call_op as py_method_call_op, py_vectorcall_method_op as py_vectorcall_method_op, py_vectorcall_op as py_vectorcall_op
from mypyc.primitives.int_ops import int16_divide_op as int16_divide_op, int16_mod_op as int16_mod_op, int16_overflow as int16_overflow, int32_divide_op as int32_divide_op, int32_mod_op as int32_mod_op, int32_overflow as int32_overflow, int64_divide_op as int64_divide_op, int64_mod_op as int64_mod_op, int64_to_int_op as int64_to_int_op, int_comparison_op_mapping as int_comparison_op_mapping, int_to_int32_op as int_to_int32_op, int_to_int64_op as int_to_int64_op, ssize_t_to_int_op as ssize_t_to_int_op, uint8_overflow as uint8_overflow
from mypyc.primitives.list_ops import list_build_op as list_build_op, list_extend_op as list_extend_op, new_list_op as new_list_op
from mypyc.primitives.misc_ops import bool_op as bool_op, fast_isinstance_op as fast_isinstance_op, none_object_op as none_object_op
from mypyc.primitives.registry import CFunctionDescription as CFunctionDescription, ERR_NEG_INT as ERR_NEG_INT, binary_ops as binary_ops, method_call_ops as method_call_ops, unary_ops as unary_ops
from mypyc.primitives.set_ops import new_set_op as new_set_op
from mypyc.primitives.str_ops import str_check_if_true as str_check_if_true, str_ssize_t_size_op as str_ssize_t_size_op, unicode_compare as unicode_compare
from mypyc.primitives.tuple_ops import list_tuple_op as list_tuple_op, new_tuple_op as new_tuple_op, new_tuple_with_length_op as new_tuple_with_length_op
from mypyc.rt_subtype import is_runtime_subtype as is_runtime_subtype
from mypyc.sametype import is_same_type as is_same_type
from mypyc.subtype import is_subtype as is_subtype
from typing import Callable, Final, Sequence, Tuple

DictEntry = Tuple[Value | None, Value]
LIST_BUILDING_EXPANSION_THRESHOLD: int
PY_VECTORCALL_ARGUMENTS_OFFSET: Final[Incomplete]
FIXED_WIDTH_INT_BINARY_OPS: Final[Incomplete]
BOOL_BINARY_OPS: Final[Incomplete]

class LowLevelIRBuilder:
    current_module: Incomplete
    errors: Incomplete
    mapper: Incomplete
    options: Incomplete
    args: Incomplete
    blocks: Incomplete
    error_handlers: Incomplete
    keep_alives: Incomplete
    def __init__(self, current_module: str, errors: Errors, mapper: Mapper, options: CompilerOptions) -> None: ...
    module_name: Incomplete
    module_path: Incomplete
    def set_module(self, module_name: str, module_path: str) -> None:
        """Set the name and path of the current module."""
    def add(self, op: Op) -> Value:
        """Add an op."""
    def goto(self, target: BasicBlock) -> None:
        """Add goto to a basic block."""
    def activate_block(self, block: BasicBlock) -> None:
        """Add a basic block and make it the active one (target of adds)."""
    def goto_and_activate(self, block: BasicBlock) -> None:
        """Add goto a block and make it the active block."""
    def keep_alive(self, values: list[Value], *, steal: bool = False) -> None: ...
    def push_error_handler(self, handler: BasicBlock | None) -> None: ...
    def pop_error_handler(self) -> BasicBlock | None: ...
    def self(self) -> Register:
        """Return reference to the 'self' argument.

        This only works in a method.
        """
    def flush_keep_alives(self) -> None: ...
    def box(self, src: Value) -> Value: ...
    def unbox_or_cast(self, src: Value, target_type: RType, line: int, *, can_borrow: bool = False) -> Value: ...
    def coerce(self, src: Value, target_type: RType, line: int, force: bool = False, *, can_borrow: bool = False) -> Value:
        """Generate a coercion/cast from one type to other (only if needed).

        For example, int -> object boxes the source int; int -> int emits nothing;
        object -> int unboxes the object. All conversions preserve object value.

        If force is true, always generate an op (even if it is just an assignment) so
        that the result will have exactly target_type as the type.

        Returns the register with the converted value (may be same as src).
        """
    def coerce_int_to_fixed_width(self, src: Value, target_type: RType, line: int) -> Value: ...
    def coerce_short_int_to_fixed_width(self, src: Value, target_type: RType, line: int) -> Value: ...
    def coerce_fixed_width_to_int(self, src: Value, line: int) -> Value: ...
    def coerce_nullable(self, src: Value, target_type: RType, line: int) -> Value:
        """Generate a coercion from a potentially null value."""
    def get_attr(self, obj: Value, attr: str, result_type: RType, line: int, *, borrow: bool = False) -> Value:
        """Get a native or Python attribute of an object."""
    def union_get_attr(self, obj: Value, rtype: RUnion, attr: str, result_type: RType, line: int) -> Value:
        """Get an attribute of an object with a union type."""
    def py_get_attr(self, obj: Value, attr: str, line: int) -> Value:
        """Get a Python attribute (slow).

        Prefer get_attr() which generates optimized code for native classes.
        """
    def isinstance_helper(self, obj: Value, class_irs: list[ClassIR], line: int) -> Value:
        """Fast path for isinstance() that checks against a list of native classes."""
    def get_type_of_obj(self, obj: Value, line: int) -> Value: ...
    def type_is_op(self, obj: Value, type_obj: Value, line: int) -> Value: ...
    def isinstance_native(self, obj: Value, class_ir: ClassIR, line: int) -> Value:
        """Fast isinstance() check for a native class.

        If there are three or fewer concrete (non-trait) classes among the class
        and all its children, use even faster type comparison checks `type(obj)
        is typ`.
        """
    def py_call(self, function: Value, arg_values: list[Value], line: int, arg_kinds: list[ArgKind] | None = None, arg_names: Sequence[str | None] | None = None) -> Value:
        """Call a Python function (non-native and slow).

        Use py_call_op or py_call_with_kwargs_op for Python function call.
        """
    def py_method_call(self, obj: Value, method_name: str, arg_values: list[Value], line: int, arg_kinds: list[ArgKind] | None, arg_names: Sequence[str | None] | None) -> Value:
        """Call a Python method (non-native and slow)."""
    def call(self, decl: FuncDecl, args: Sequence[Value], arg_kinds: list[ArgKind], arg_names: Sequence[str | None], line: int, *, bitmap_args: list[Register] | None = None) -> Value:
        """Call a native function.

        If bitmap_args is given, they override the values of (some) of the bitmap
        arguments used to track the presence of values for certain arguments. By
        default, the values of the bitmap arguments are inferred from args.
        """
    def native_args_to_positional(self, args: Sequence[Value], arg_kinds: list[ArgKind], arg_names: Sequence[str | None], sig: FuncSignature, line: int, *, bitmap_args: list[Register] | None = None) -> list[Value]:
        """Prepare arguments for a native call.

        Given args/kinds/names and a target signature for a native call, map
        keyword arguments to their appropriate place in the argument list,
        fill in error values for unspecified default arguments,
        package arguments that will go into *args/**kwargs into a tuple/dict,
        and coerce arguments to the appropriate type.
        """
    def gen_method_call(self, base: Value, name: str, arg_values: list[Value], result_type: RType | None, line: int, arg_kinds: list[ArgKind] | None = None, arg_names: list[str | None] | None = None, can_borrow: bool = False) -> Value:
        """Generate either a native or Python method call."""
    def union_method_call(self, base: Value, obj_type: RUnion, name: str, arg_values: list[Value], return_rtype: RType | None, line: int, arg_kinds: list[ArgKind] | None, arg_names: list[str | None] | None) -> Value:
        """Generate a method call with a union type for the object."""
    def none(self) -> Value:
        """Load unboxed None value (type: none_rprimitive)."""
    def true(self) -> Value:
        """Load unboxed True value (type: bool_rprimitive)."""
    def false(self) -> Value:
        """Load unboxed False value (type: bool_rprimitive)."""
    def none_object(self) -> Value:
        """Load Python None value (type: object_rprimitive)."""
    def load_int(self, value: int) -> Value:
        """Load a tagged (Python) integer literal value."""
    def load_float(self, value: float) -> Value:
        """Load a float literal value."""
    def load_str(self, value: str) -> Value:
        """Load a str literal value.

        This is useful for more than just str literals; for example, method calls
        also require a PyObject * form for the name of the method.
        """
    def load_bytes(self, value: bytes) -> Value:
        """Load a bytes literal value."""
    def load_complex(self, value: complex) -> Value:
        """Load a complex literal value."""
    def load_static_checked(self, typ: RType, identifier: str, module_name: str | None = None, namespace: str = ..., line: int = -1, error_msg: str | None = None) -> Value: ...
    def load_module(self, name: str) -> Value: ...
    def get_native_type(self, cls: ClassIR) -> Value:
        """Load native type object."""
    def load_native_type_object(self, fullname: str) -> Value: ...
    def binary_op(self, lreg: Value, rreg: Value, op: str, line: int) -> Value:
        """Perform a binary operation.

        Generate specialized operations based on operand types, with a fallback
        to generic operations.
        """
    def check_tagged_short_int(self, val: Value, line: int, negated: bool = False) -> Value:
        """Check if a tagged integer is a short integer.

        Return the result of the check (value of type 'bit').
        """
    def compare_tagged(self, lhs: Value, rhs: Value, op: str, line: int) -> Value:
        """Compare two tagged integers using given operator (value context)."""
    def compare_tagged_condition(self, lhs: Value, rhs: Value, op: str, true: BasicBlock, false: BasicBlock, line: int) -> None:
        """Compare two tagged integers using given operator (conditional context).

        Assume lhs and rhs are tagged integers.

        Args:
            lhs: Left operand
            rhs: Right operand
            op: Operation, one of '==', '!=', '<', '<=', '>', '<='
            true: Branch target if comparison is true
            false: Branch target if comparison is false
        """
    def compare_strings(self, lhs: Value, rhs: Value, op: str, line: int) -> Value:
        """Compare two strings"""
    def compare_bytes(self, lhs: Value, rhs: Value, op: str, line: int) -> Value: ...
    def compare_tuples(self, lhs: Value, rhs: Value, op: str, line: int = -1) -> Value:
        """Compare two tuples item by item"""
    def translate_instance_contains(self, inst: Value, item: Value, op: str, line: int) -> Value: ...
    def bool_bitwise_op(self, lreg: Value, rreg: Value, op: str, line: int) -> Value: ...
    def bool_comparison_op(self, lreg: Value, rreg: Value, op: str, line: int) -> Value: ...
    def unary_not(self, value: Value, line: int) -> Value: ...
    def unary_op(self, value: Value, expr_op: str, line: int) -> Value: ...
    def make_dict(self, key_value_pairs: Sequence[DictEntry], line: int) -> Value: ...
    def new_list_op_with_length(self, length: Value, line: int) -> Value:
        """This function returns an uninitialized list.

        If the length is non-zero, the caller must initialize the list, before
        it can be made visible to user code -- otherwise the list object is broken.
        You might need further initialization with `new_list_set_item_op` op.

        Args:
            length: desired length of the new list. The rtype should be
                    c_pyssize_t_rprimitive
            line: line number
        """
    def new_list_op(self, values: list[Value], line: int) -> Value: ...
    def new_set_op(self, values: list[Value], line: int) -> Value: ...
    def setup_rarray(self, item_type: RType, values: Sequence[Value], *, object_ptr: bool = False) -> Value:
        """Declare and initialize a new RArray, returning its address."""
    def shortcircuit_helper(self, op: str, expr_type: RType, left: Callable[[], Value], right: Callable[[], Value], line: int) -> Value: ...
    def bool_value(self, value: Value) -> Value:
        """Return bool(value).

        The result type can be bit_rprimitive or bool_rprimitive.
        """
    def add_bool_branch(self, value: Value, true: BasicBlock, false: BasicBlock) -> None: ...
    def call_c(self, desc: CFunctionDescription, args: list[Value], line: int, result_type: RType | None = None) -> Value:
        """Call function using C/native calling convention (not a Python callable)."""
    def matching_call_c(self, candidates: list[CFunctionDescription], args: list[Value], line: int, result_type: RType | None = None, can_borrow: bool = False) -> Value | None: ...
    def int_op(self, type: RType, lhs: Value, rhs: Value, op: int, line: int = -1) -> Value:
        """Generate a native integer binary op.

        Use native/C semantics, which sometimes differ from Python
        semantics.

        Args:
            type: Either int64_rprimitive or int32_rprimitive
            op: IntOp.* constant (e.g. IntOp.ADD)
        """
    def float_op(self, lhs: Value, rhs: Value, op: str, line: int) -> Value:
        """Generate a native float binary arithmetic operation.

        This follows Python semantics (e.g. raise exception on division by zero).
        Add a FloatOp directly if you want low-level semantics.

        Args:
            op: Binary operator (e.g. '+' or '*')
        """
    def float_mod(self, lhs: Value, rhs: Value, line: int) -> Value:
        """Perform x % y on floats using Python semantics."""
    def compare_floats(self, lhs: Value, rhs: Value, op: int, line: int) -> Value: ...
    def fixed_width_int_op(self, type: RPrimitive, lhs: Value, rhs: Value, op: int, line: int) -> Value:
        """Generate a binary op using Python fixed-width integer semantics.

        These may differ in overflow/rounding behavior from native/C ops.

        Args:
            type: Either int64_rprimitive or int32_rprimitive
            op: IntOp.* constant (e.g. IntOp.ADD)
        """
    def check_for_zero_division(self, rhs: Value, type: RType, line: int) -> None: ...
    def inline_fixed_width_divide(self, type: RType, lhs: Value, rhs: Value, line: int) -> Value: ...
    def inline_fixed_width_mod(self, type: RType, lhs: Value, rhs: Value, line: int) -> Value: ...
    def is_same_native_int_signs(self, type: RType, a: Value, b: Value, line: int) -> Value: ...
    def is_same_float_signs(self, a: Value, b: Value, line: int) -> Value: ...
    def comparison_op(self, lhs: Value, rhs: Value, op: int, line: int) -> Value: ...
    def builtin_len(self, val: Value, line: int, use_pyssize_t: bool = False) -> Value:
        """Generate len(val).

        Return short_int_rprimitive by default.
        Return c_pyssize_t if use_pyssize_t is true (unshifted).
        """
    def new_tuple(self, items: list[Value], line: int) -> Value: ...
    def new_tuple_with_length(self, length: Value, line: int) -> Value:
        """This function returns an uninitialized tuple.

        If the length is non-zero, the caller must initialize the tuple, before
        it can be made visible to user code -- otherwise the tuple object is broken.
        You might need further initialization with `new_tuple_set_item_op` op.

        Args:
            length: desired length of the new tuple. The rtype should be
                    c_pyssize_t_rprimitive
            line: line number
        """
    def int_to_float(self, n: Value, line: int) -> Value: ...
    def decompose_union_helper(self, obj: Value, rtype: RUnion, result_type: RType, process_item: Callable[[Value], Value], line: int) -> Value:
        """Generate isinstance() + specialized operations for union items.

        Say, for Union[A, B] generate ops resembling this (pseudocode):

            if isinstance(obj, A):
                result = <result of process_item(cast(A, obj)>
            else:
                result = <result of process_item(cast(B, obj)>

        Args:
            obj: value with a union type
            rtype: the union type
            result_type: result of the operation
            process_item: callback to generate op for a single union item (arg is coerced
                to union item type)
            line: line number
        """
    def translate_special_method_call(self, base_reg: Value, name: str, args: list[Value], result_type: RType | None, line: int, can_borrow: bool = False) -> Value | None:
        """Translate a method call which is handled nongenerically.

        These are special in the sense that we have code generated specifically for them.
        They tend to be method calls which have equivalents in C that are more direct
        than calling with the PyObject api.

        Return None if no translation found; otherwise return the target register.
        """
    def translate_eq_cmp(self, lreg: Value, rreg: Value, expr_op: str, line: int) -> Value | None:
        """Add a equality comparison operation.

        Args:
            expr_op: either '==' or '!='
        """
    def translate_is_op(self, lreg: Value, rreg: Value, expr_op: str, line: int) -> Value:
        """Create equality comparison operation between object identities

        Args:
            expr_op: either 'is' or 'is not'
        """
    def error(self, msg: str, line: int) -> None: ...

def num_positional_args(arg_values: list[Value], arg_kinds: list[ArgKind] | None) -> int: ...
