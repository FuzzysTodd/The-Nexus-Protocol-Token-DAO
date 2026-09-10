from tensorflow.python.autograph.operators import control_flow as control_flow, py_builtins as py_builtins
from tensorflow.python.data.experimental.ops import take_while_ops as take_while_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_string_ops as gen_string_ops, math_ops as math_ops
from tensorflow.python.util import nest as nest

def register_overrides() -> None:
    """Registers the autograph specific overrides for dataset_ops."""
