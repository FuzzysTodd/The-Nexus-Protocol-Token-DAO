from tensorflow.core.function import trace_type as trace_type
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, tensor_spec as tensor_spec
from tensorflow.python.ops import random_ops as random_ops
from tensorflow.python.util import nest as nest
from typing import List, Optional

def maybe_get_device_name(device_name): ...
def make_handledata_tensor_specs(resource_vars):
    """Convert tf.Variable list to its corresponding TensorSpec list."""
def from_concrete_function(concrete_fn, specialized_flat_specs: Optional[List[tensor_spec.TensorSpec]] = None):
    '''Generate the Compiler Ir from tf concrete function with TensorSpec.

  Args:
    concrete_fn: returned by using get_concrete_function.
    specialized_flat_specs: specialized flat tf.TensorSpecs for function args.

  Returns:
    Function callable that generate the HLO text.

  Raises:
      ValueError: if concrete_fn is not "compilable" without concrete
      inputs.
  '''
