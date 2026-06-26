from tensorflow.python.framework import dtypes as dtypes, tensor_shape as tensor_shape
from tensorflow.python.util.compat import collections_abc as collections_abc

def get_json_type(obj):
    """Serializes any object to a JSON-serializable structure.

  Args:
      obj: the object to serialize

  Returns:
      JSON-serializable structure representing `obj`.

  Raises:
      TypeError: if `obj` cannot be serialized.
  """
