from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.util import tf_decorator as tf_decorator, tf_inspect as tf_inspect

def fn_args(fn):
    """Get argument names for function-like object.

  Args:
    fn: Function, or function-like object (e.g., result of `functools.partial`).

  Returns:
    `tuple` of string argument names.

  Raises:
    ValueError: if partial function has positionally bound arguments
  """
def has_kwargs(fn):
    """Returns whether the passed callable has **kwargs in its signature.

  Args:
    fn: Function, or function-like object (e.g., result of `functools.partial`).

  Returns:
    `bool`: if `fn` has **kwargs in its signature.

  Raises:
     `TypeError`: If fn is not a Function, or function-like object.
  """
def get_func_name(func):
    """Returns name of passed callable."""
def get_func_code(func):
    """Returns func_code of passed callable, or None if not available."""
def get_disabled_rewriter_config(): ...
