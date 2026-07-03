from _typeshed import Incomplete
from mypyc.ir.ops import ERR_MAGIC as ERR_MAGIC, ERR_NEVER as ERR_NEVER
from mypyc.ir.rtypes import RType as RType, bit_rprimitive as bit_rprimitive, bool_rprimitive as bool_rprimitive, bytes_rprimitive as bytes_rprimitive, c_int_rprimitive as c_int_rprimitive, c_pyssize_t_rprimitive as c_pyssize_t_rprimitive, int_rprimitive as int_rprimitive, list_rprimitive as list_rprimitive, object_rprimitive as object_rprimitive, pointer_rprimitive as pointer_rprimitive, str_rprimitive as str_rprimitive
from mypyc.primitives.registry import ERR_NEG_INT as ERR_NEG_INT, binary_op as binary_op, custom_op as custom_op, function_op as function_op, load_address_op as load_address_op, method_op as method_op

str_op: Incomplete
unicode_compare: Incomplete
str_slice_op: Incomplete
str_build_op: Incomplete
str_split_types: list[RType]
str_split_functions: Incomplete
str_split_constants: list[list[tuple[int, RType]]]
str_check_if_true: Incomplete
str_ssize_t_size_op: Incomplete
