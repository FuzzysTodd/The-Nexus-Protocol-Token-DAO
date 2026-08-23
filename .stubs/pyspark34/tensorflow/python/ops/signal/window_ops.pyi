from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, special_math_ops as special_math_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

def kaiser_window(window_length, beta: float = 12.0, dtype=..., name: Incomplete | None = None):
    """Generate a [Kaiser window][kaiser].

  Args:
    window_length: A scalar `Tensor` indicating the window length to generate.
    beta: Beta parameter for Kaiser window, see reference below.
    dtype: The data type to produce. Must be a floating point type.
    name: An optional name for the operation.

  Returns:
    A `Tensor` of shape `[window_length]` of type `dtype`.

  [kaiser]:
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.kaiser.html
  """
def kaiser_bessel_derived_window(window_length, beta: float = 12.0, dtype=..., name: Incomplete | None = None):
    """Generate a [Kaiser Bessel derived window][kbd].

  Args:
    window_length: A scalar `Tensor` indicating the window length to generate.
    beta: Beta parameter for Kaiser window.
    dtype: The data type to produce. Must be a floating point type.
    name: An optional name for the operation.

  Returns:
    A `Tensor` of shape `[window_length]` of type `dtype`.

  [kbd]:
    https://en.wikipedia.org/wiki/Kaiser_window#Kaiser%E2%80%93Bessel-derived_(KBD)_window
  """
def vorbis_window(window_length, dtype=..., name: Incomplete | None = None):
    """Generate a [Vorbis power complementary window][vorbis].

  Args:
    window_length: A scalar `Tensor` indicating the window length to generate.
    dtype: The data type to produce. Must be a floating point type.
    name: An optional name for the operation.

  Returns:
    A `Tensor` of shape `[window_length]` of type `dtype`.

  [vorbis]:
    https://en.wikipedia.org/wiki/Modified_discrete_cosine_transform#Window_functions
  """
def hann_window(window_length, periodic: bool = True, dtype=..., name: Incomplete | None = None):
    """Generate a [Hann window][hann].

  Args:
    window_length: A scalar `Tensor` indicating the window length to generate.
    periodic: A bool `Tensor` indicating whether to generate a periodic or
      symmetric window. Periodic windows are typically used for spectral
      analysis while symmetric windows are typically used for digital
      filter design.
    dtype: The data type to produce. Must be a floating point type.
    name: An optional name for the operation.

  Returns:
    A `Tensor` of shape `[window_length]` of type `dtype`.

  Raises:
    ValueError: If `dtype` is not a floating point type.

  [hann]: https://en.wikipedia.org/wiki/Window_function#Hann_and_Hamming_windows
  """
def hamming_window(window_length, periodic: bool = True, dtype=..., name: Incomplete | None = None):
    """Generate a [Hamming][hamming] window.

  Args:
    window_length: A scalar `Tensor` indicating the window length to generate.
    periodic: A bool `Tensor` indicating whether to generate a periodic or
      symmetric window. Periodic windows are typically used for spectral
      analysis while symmetric windows are typically used for digital
      filter design.
    dtype: The data type to produce. Must be a floating point type.
    name: An optional name for the operation.

  Returns:
    A `Tensor` of shape `[window_length]` of type `dtype`.

  Raises:
    ValueError: If `dtype` is not a floating point type.

  [hamming]:
    https://en.wikipedia.org/wiki/Window_function#Hann_and_Hamming_windows
  """
