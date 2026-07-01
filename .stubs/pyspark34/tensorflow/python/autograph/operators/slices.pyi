from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, tensor_util as tensor_util
from tensorflow.python.ops import gen_array_ops as gen_array_ops, gen_string_ops as gen_string_ops, list_ops as list_ops, tensor_array_ops as tensor_array_ops
from typing import NamedTuple

class GetItemOpts(NamedTuple('GetItemOpts', [('element_dtype', Incomplete)])): ...

def get_item(target, i, opts):
    """The slice read operator (i.e. __getitem__).

  Note: it is unspecified whether target will be mutated or not. In general,
  if target is mutable (like Python lists), it will be mutated.

  Args:
    target: An entity that supports getitem semantics.
    i: Index to read from.
    opts: A GetItemOpts object.

  Returns:
    The read element.

  Raises:
    ValueError: if target is not of a supported type.
  """
def set_item(target, i, x):
    """The slice write operator (i.e. __setitem__).

  Note: it is unspecified whether target will be mutated or not. In general,
  if target is mutable (like Python lists), it will be mutated.

  Args:
    target: An entity that supports setitem semantics.
    i: Index to modify.
    x: The new element value.

  Returns:
    Same as target, after the update was performed.

  Raises:
    ValueError: if target is not of a supported type.
  """
