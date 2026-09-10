from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import handle_data_util as handle_data_util, resource_variable_ops as resource_variable_ops
from tensorflow.python.saved_model import registration as registration
from tensorflow.python.trackable import asset as asset, base as trackable, resource as resource

class TrackableConstant(trackable.Trackable):
    """Trackable class for captured constants."""
    capture: Incomplete
    function: Incomplete
    def __init__(self, capture, function) -> None: ...

def get_tensor_from_node(node):
    """Resolves a saved model graph node into a tensor to be captured.

  Args:
    node: a tensor, variable, or resource to be resolved into a capturable
      tensor

  Returns:
    A list of tensors.
  Raises:
    ValueError: if the node cannot be converted into a tensor.
  """
def restore_captures(concrete_function, inputs) -> None:
    """Restore captures for the concrete function.

  Used at deserialization time.  For functions that are being deserialized,
  saved model restores objects that tensors were captured from, but functions
  only know about their tensors -- object information is destroyed by tracing.
  This additional logic extracts the tensors which the function originally
  captured.

  Args:
    concrete_function: the concrete function for which to restore captures
    inputs: a list tensors or other Python objects (such as variables) which
      contain tensors that were originally captured by the function
  """
