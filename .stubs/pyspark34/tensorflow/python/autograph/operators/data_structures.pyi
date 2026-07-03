from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, list_ops as list_ops, tensor_array_ops as tensor_array_ops
from typing import NamedTuple

def new_list(iterable: Incomplete | None = None):
    """The list constructor.

  Args:
    iterable: Optional elements to fill the list with.

  Returns:
    A list-like object. The exact return value depends on the initial elements.
  """
def tf_tensor_array_new(elements, element_dtype: Incomplete | None = None, element_shape: Incomplete | None = None):
    """Overload of new_list that stages a Tensor list creation."""
def tf_tensor_list_new(elements, element_dtype: Incomplete | None = None, element_shape: Incomplete | None = None):
    """Overload of new_list that stages a Tensor list creation."""
def list_append(list_, x):
    """The list append function.

  Note: it is unspecified where list_ will be mutated or not. If list_ is
  a TensorFlow entity, it will not be typically mutated. If list_ is a plain
  list, it will be. In general, if the list is mutated then the return value
  should point to the original entity.

  Args:
    list_: An entity that supports append semantics.
    x: The element to append.

  Returns:
    Same as list_, after the append was performed.

  Raises:
    ValueError: if list_ is not of a known list-like type.
  """

class ListPopOpts(NamedTuple('ListPopOpts', [('element_dtype', Incomplete), ('element_shape', Incomplete)])): ...

def list_pop(list_, i, opts):
    """The list pop function.

  Note: it is unspecified where list_ will be mutated or not. If list_ is
  a TensorFlow entity, it will not be typically mutated. If list_ is a plain
  list, it will be. In general, if the list is mutated then the return value
  should point to the original entity.

  Args:
    list_: An entity that supports pop semantics.
    i: Optional index to pop from. May be None.
    opts: A ListPopOpts.

  Returns:
    Tuple (x, out_list_):
      out_list_: same as list_, after the removal was performed.
      x: the removed element value.

  Raises:
    ValueError: if list_ is not of a known list-like type or the operation is
    not supported for that type.
  """

class ListStackOpts(NamedTuple('ListStackOpts', [('element_dtype', Incomplete), ('original_call', Incomplete)])): ...

def list_stack(list_, opts):
    """The list stack function.

  This does not have a direct correspondent in Python. The closest idiom to
  this is tf.append or np.stack. It's different from those in the sense that it
  accepts a Tensor list, rather than a list of tensors. It can also accept
  TensorArray. When the target is anything else, the dispatcher will rely on
  ctx.original_call for fallback.

  Args:
    list_: An entity that supports append semantics.
    opts: A ListStackOpts object.

  Returns:
    The output of the stack operation, typically a Tensor.
  """
