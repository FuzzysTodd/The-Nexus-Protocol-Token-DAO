from _typeshed import Incomplete
from mypyc.ir.ops import ComparisonOp as ComparisonOp, ERR_ALWAYS as ERR_ALWAYS, ERR_MAGIC as ERR_MAGIC, ERR_MAGIC_OVERLAPPING as ERR_MAGIC_OVERLAPPING, ERR_NEVER as ERR_NEVER
from mypyc.ir.rtypes import RType as RType, bit_rprimitive as bit_rprimitive, bool_rprimitive as bool_rprimitive, c_pyssize_t_rprimitive as c_pyssize_t_rprimitive, float_rprimitive as float_rprimitive, int16_rprimitive as int16_rprimitive, int32_rprimitive as int32_rprimitive, int64_rprimitive as int64_rprimitive, int_rprimitive as int_rprimitive, object_rprimitive as object_rprimitive, str_rprimitive as str_rprimitive, void_rtype as void_rtype
from mypyc.primitives.registry import CFunctionDescription as CFunctionDescription, binary_op as binary_op, custom_op as custom_op, function_op as function_op, load_address_op as load_address_op, unary_op as unary_op
from typing import NamedTuple

int_to_str_op: Incomplete

def int_binary_op(name: str, c_function_name: str, return_type: RType = ..., error_kind: int = ...) -> None: ...
def int_unary_op(name: str, c_function_name: str) -> CFunctionDescription: ...

int_neg_op: Incomplete
int_invert_op: Incomplete

class IntComparisonOpDescription(NamedTuple):
    binary_op_variant: int
    c_func_description: CFunctionDescription
    c_func_negated: bool
    c_func_swap_operands: bool

int_equal_: Incomplete
int_less_than_: Incomplete
int_comparison_op_mapping: dict[str, IntComparisonOpDescription]
int64_divide_op: Incomplete
int64_mod_op: Incomplete
int32_divide_op: Incomplete
int32_mod_op: Incomplete
int16_divide_op: Incomplete
int16_mod_op: Incomplete
int_to_int64_op: Incomplete
ssize_t_to_int_op: Incomplete
int64_to_int_op: Incomplete
int_to_int32_op: Incomplete
int32_overflow: Incomplete
int16_overflow: Incomplete
uint8_overflow: Incomplete
