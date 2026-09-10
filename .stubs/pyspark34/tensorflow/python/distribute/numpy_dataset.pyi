from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, variable_scope as variable_scope
from tensorflow.python.util import nest as nest

def init_var_from_numpy(input_var, numpy_input, session) -> None:
    """Initialize `input_var` to `numpy_input` using `session` in graph mode."""
def one_host_numpy_dataset(numpy_input, colocate_with, session):
    """Create a dataset on `colocate_with` from `numpy_input`."""

class SingleDevice:
    """Used with `colocate_with` to create a non-mirrored variable."""
    device: Incomplete
    def __init__(self, device) -> None: ...
