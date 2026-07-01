from tensorflow.python.autograph.operators import control_flow as control_flow, py_builtins as py_builtins
from tensorflow.python.data.ops import iterator_ops as iterator_ops
from tensorflow.python.framework import ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import control_flow_ops as control_flow_ops
from tensorflow.python.util import nest as nest

def register_overrides() -> None: ...
