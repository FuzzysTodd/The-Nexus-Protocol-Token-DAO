from tensorflow.python.checkpoint import saveable_compat as saveable_compat, tensor_callable as tensor_callable
from tensorflow.python.eager import def_function as def_function

def trace_save_and_restore(obj):
    """Traces `Trackable` serialize- and restore-from-tensors functions.

  Args:
    obj: A `Trackable` object.

  Returns:
    A concrete Function.
  """
