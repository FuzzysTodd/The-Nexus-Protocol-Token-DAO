from _typeshed import Incomplete
from mypy.nodes import CallExpr, Expression as Expression, GeneratorExpr, MemberExpr, RefExpr
from mypyc.ir.ops import BasicBlock as BasicBlock, Extend as Extend, Integer as Integer, RaiseStandardError as RaiseStandardError, Register as Register, Truncate as Truncate, Unreachable as Unreachable, Value as Value
from mypyc.ir.rtypes import RInstance as RInstance, RPrimitive as RPrimitive, RTuple as RTuple, RType as RType, bool_rprimitive as bool_rprimitive, c_int_rprimitive as c_int_rprimitive, dict_rprimitive as dict_rprimitive, int16_rprimitive as int16_rprimitive, int32_rprimitive as int32_rprimitive, int64_rprimitive as int64_rprimitive, int_rprimitive as int_rprimitive, is_bool_rprimitive as is_bool_rprimitive, is_dict_rprimitive as is_dict_rprimitive, is_fixed_width_rtype as is_fixed_width_rtype, is_float_rprimitive as is_float_rprimitive, is_int16_rprimitive as is_int16_rprimitive, is_int32_rprimitive as is_int32_rprimitive, is_int64_rprimitive as is_int64_rprimitive, is_int_rprimitive as is_int_rprimitive, is_list_rprimitive as is_list_rprimitive, is_uint8_rprimitive as is_uint8_rprimitive, list_rprimitive as list_rprimitive, set_rprimitive as set_rprimitive, str_rprimitive as str_rprimitive, uint8_rprimitive as uint8_rprimitive
from mypyc.irbuild.builder import IRBuilder as IRBuilder
from mypyc.irbuild.for_helpers import comprehension_helper as comprehension_helper, sequence_from_generator_preallocate_helper as sequence_from_generator_preallocate_helper, translate_list_comprehension as translate_list_comprehension, translate_set_comprehension as translate_set_comprehension
from mypyc.irbuild.format_str_tokenizer import FormatOp as FormatOp, convert_format_expr_to_str as convert_format_expr_to_str, join_formatted_strings as join_formatted_strings, tokenizer_format_call as tokenizer_format_call
from mypyc.primitives.dict_ops import dict_items_op as dict_items_op, dict_keys_op as dict_keys_op, dict_setdefault_spec_init_op as dict_setdefault_spec_init_op, dict_values_op as dict_values_op
from mypyc.primitives.list_ops import new_list_set_item_op as new_list_set_item_op
from mypyc.primitives.tuple_ops import new_tuple_set_item_op as new_tuple_set_item_op
from typing import Callable

Specializer: Incomplete
specializers: dict[tuple[str, RType | None], list[Specializer]]

def apply_function_specialization(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None:
    """Invoke the Specializer callback for a function if one has been registered"""
def apply_method_specialization(builder: IRBuilder, expr: CallExpr, callee: MemberExpr, typ: RType | None = None) -> Value | None:
    """Invoke the Specializer callback for a method if one has been registered"""
def specialize_function(name: str, typ: RType | None = None) -> Callable[[Specializer], Specializer]:
    """Decorator to register a function as being a specializer.

    There may exist multiple specializers for one function. When
    translating method calls, the earlier appended specializer has
    higher priority.
    """
def translate_globals(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def translate_builtins_with_unary_dunder(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None:
    """Specialize calls on native classes that implement the associated dunder.

    E.g. i64(x) gets specialized to x.__int__() if x is a native instance.
    """
def translate_len(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def dict_methods_fast_path(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None:
    """Specialize a common case when list() is called on a dictionary
    view method call.

    For example:
        foo = list(bar.keys())
    """
def translate_list_from_generator_call(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None:
    """Special case for simplest list comprehension.

    For example:
        list(f(x) for x in some_list/some_tuple/some_str)
    'translate_list_comprehension()' would take care of other cases
    if this fails.
    """
def translate_tuple_from_generator_call(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None:
    """Special case for simplest tuple creation from a generator.

    For example:
        tuple(f(x) for x in some_list/some_tuple/some_str)
    'translate_safe_generator_call()' would take care of other cases
    if this fails.
    """
def translate_set_from_generator_call(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None:
    """Special case for set creation from a generator.

    For example:
        set(f(...) for ... in iterator/nested_generators...)
    """
def faster_min_max(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def translate_safe_generator_call(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None:
    """Special cases for things that consume iterators where we know we
    can safely compile a generator into a list.
    """
def translate_any_call(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def translate_all_call(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def any_all_helper(builder: IRBuilder, gen: GeneratorExpr, initial_value: Callable[[], Value], modify: Callable[[Value], Value], new_value: Callable[[], Value]) -> Value: ...
def translate_sum_call(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def translate_dataclasses_field_call(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None:
    """Special case for 'dataclasses.field', 'attr.attrib', and 'attr.Factory'
    function calls because the results of such calls are type-checked
    by mypy using the types of the arguments to their respective
    functions, resulting in attempted coercions by mypyc that throw a
    runtime error.
    """
def translate_next_call(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None:
    """Special case for calling next() on a generator expression, an
    idiom that shows up some in mypy.

    For example, next(x for x in l if x.id == 12, None) will
    generate code that searches l for an element where x.id == 12
    and produce the first such object, or None if no such element
    exists.
    """
def translate_isinstance(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None:
    """Special case for builtins.isinstance.

    Prevent coercions on the thing we are checking the instance of -
    there is no need to coerce something to a new type before checking
    what type it is, and the coercion could lead to bugs.
    """
def translate_dict_setdefault(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None:
    """Special case for 'dict.setdefault' which would only construct
    default empty collection when needed.

    The dict_setdefault_spec_init_op checks whether the dict contains
    the key and would construct the empty collection only once.

    For example, this specializer works for the following cases:
         d.setdefault(key, set()).add(value)
         d.setdefault(key, []).append(value)
         d.setdefault(key, {})[inner_key] = inner_val
    """
def translate_str_format(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def translate_fstring(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None:
    """Special case for f-string, which is translated into str.join()
    in mypy AST.

    This specializer optimizes simplest f-strings which don't contain
    any format operation.
    """
def translate_i64(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def translate_i32(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def translate_i16(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def translate_u8(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def truncate_literal(value: Value, rtype: RPrimitive) -> Value:
    """If value is an integer literal value, truncate it to given native int rtype.

    For example, truncate 256 into 0 if rtype is u8.
    """
def translate_int(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def translate_bool(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
def translate_float(builder: IRBuilder, expr: CallExpr, callee: RefExpr) -> Value | None: ...
