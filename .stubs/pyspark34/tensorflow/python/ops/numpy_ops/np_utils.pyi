from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, indexed_slices as indexed_slices, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.ops.numpy_ops import np_arrays as np_arrays, np_dtypes as np_dtypes, np_export as np_export
from tensorflow.python.types import core as core
from tensorflow.python.util import nest as nest

def isscalar(val):
    """Returns whether `val` is a scalar value or scalar Tensor."""
def get_np_doc_form():
    """Gets the form of the original numpy docstrings.

  Returns:
    See `set_np_doc_form` for the list of valid values.
  """
def set_np_doc_form(value) -> None:
    """Selects the form of the original numpy docstrings.

  This function sets a global variable that controls how a tf-numpy symbol's
  docstring should refer to the original numpy docstring. If `value` is
  `'inlined'`, the numpy docstring will be verbatim copied into the tf-numpy
  docstring. Otherwise, a link to the original numpy docstring will be
  added. Which numpy version the link points to depends on `value`:
  * `'stable'`: the current stable version;
  * `'dev'`: the current development version;
  * pattern `\\d+(\\.\\d+(\\.\\d+)?)?`: `value` will be treated as a version number,
    e.g. '1.16'.

  Args:
    value: the value to set the global variable to.
  """

class Link:
    value: Incomplete
    def __init__(self, v) -> None: ...

class AliasOf:
    value: Incomplete
    def __init__(self, v) -> None: ...

class NoLink: ...

def generate_link(flag, np_fun_name):
    """Generates link from numpy function name.

  Args:
    flag: the flag to control link form. See `set_np_doc_form`.
    np_fun_name: the numpy function name.

  Returns:
    A string.
  """
def is_check_link(): ...
def set_check_link(value) -> None: ...
def is_sig_mismatch_an_error(): ...
def set_is_sig_mismatch_an_error(value) -> None: ...
def np_doc(np_fun_name, np_fun: Incomplete | None = None, export: bool = True, unsupported_params: Incomplete | None = None, link: Incomplete | None = None):
    """Attachs numpy docstring to a function.

  Args:
    np_fun_name: name for the np_fun symbol. At least one of np_fun or
      np_fun_name shoud be set.
    np_fun: (optional) the numpy function whose docstring will be used.
    export: whether to export this symbol under module
      `tf.experimental.numpy`. Note that if `export` is `True`, `np_fun` must be
      a function directly under the `numpy` module, not under any submodule of
      `numpy` (e.g. `numpy.random`).
    unsupported_params: (optional) the list of parameters not supported
      by tf.numpy.
    link: (optional) which link to use. If `None`, a default link generated from
      `np_fun_name` will be used. If an instance of `AliasOf`, `link.value` will
      be used in place of `np_fun_name` for the link generation. If an instance
      of `Link`, `link.value` will be used as the whole link. If an instance of
      `NoLink`, no link will be added.

  Returns:
    A function decorator that attaches the docstring from `np_fun` to the
    decorated function.
  """
def np_doc_only(np_fun_name, np_fun: Incomplete | None = None, export: bool = True):
    """Attachs numpy docstring to a function.

  This differs from np_doc in that it doesn't check for a match in signature.

  Args:
    np_fun_name: name for the np_fun symbol. At least one of np_fun or
      np_fun_name shoud be set.
    np_fun: (optional) the numpy function whose docstring will be used.
    export: whether to export this symbol under module
      `tf.experimental.numpy`. Note that if `export` is `True`, `np_f` must be a
      function directly under the `numpy` module, not under any submodule of
      `numpy` (e.g. `numpy.random`).

  Returns:
    A function decorator that attaches the docstring from `np_fun` to the
    decorated function.
  """
def finfo(dtype):
    """Note that currently it just forwards to the numpy namesake, while
  tensorflow and numpy dtypes may have different properties."""
def result_type(*arrays_and_dtypes): ...
def result_type_unary(a, dtype):
    """Find the result type from a single input and a dtype."""
def promote_types(type1, type2): ...
def tf_broadcast(*args):
    """Broadcast tensors.

  Args:
    *args: a list of tensors whose shapes are broadcastable against each other.

  Returns:
    Tensors broadcasted to the common shape.
  """
def get_static_value(x):
    """A version of tf.get_static_value that returns None on float dtypes.

  It returns None on float dtypes in order to avoid breaking gradients.

  Args:
    x: a tensor.

  Returns:
    Same as `tf.get_static_value`, except that it returns None when `x` has a
    float dtype.
  """
def cond(pred, true_fn, false_fn):
    """A version of tf.cond that tries to evaluate the condition."""
def add(a, b):
    """A version of tf.add that eagerly evaluates if possible."""
def subtract(a, b):
    """A version of tf.subtract that eagerly evaluates if possible."""
def greater(a, b):
    """A version of tf.greater that eagerly evaluates if possible."""
def greater_equal(a, b):
    """A version of tf.greater_equal that eagerly evaluates if possible."""
def less_equal(a, b):
    """A version of tf.less_equal that eagerly evaluates if possible."""
def logical_and(a, b):
    """A version of tf.logical_and that eagerly evaluates if possible."""
def logical_or(a, b):
    """A version of tf.logical_or that eagerly evaluates if possible."""
def getitem(a, slice_spec):
    """A version of __getitem__ that eagerly evaluates if possible."""
def reduce_all(input_tensor, axis: Incomplete | None = None, keepdims: bool = False):
    """A version of tf.reduce_all that eagerly evaluates if possible."""
def reduce_any(input_tensor, axis: Incomplete | None = None, keepdims: bool = False):
    """A version of tf.reduce_any that eagerly evaluates if possible."""
def tf_rank(t): ...
