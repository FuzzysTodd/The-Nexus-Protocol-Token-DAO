from tensorflow.core.function.polymorphism import function_cache as function_cache
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops
from tensorflow.python.saved_model import save_context as save_context
from typing import Any, NamedTuple

class EagerContext(NamedTuple):
    parent_graph: Any
    device_functions: Any
    colocation_stack: Any
    in_cross_replica_context: Any
    variable_policy: Any
    xla_context_id: Any

def make_function_context() -> function_cache.FunctionContext:
    """Generates a FunctionContext based on current contextual info."""
