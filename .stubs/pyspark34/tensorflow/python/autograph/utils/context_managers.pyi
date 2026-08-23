from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import tensor_array_ops as tensor_array_ops

def control_dependency_on_returns(return_value) -> Generator[None, None, Incomplete]:
    """Create a TF control dependency on the return values of a function.

  If the function had no return value, a no-op context is returned.

  Args:
    return_value: The return value to set as control dependency.

  Returns:
    A context manager.
  """
