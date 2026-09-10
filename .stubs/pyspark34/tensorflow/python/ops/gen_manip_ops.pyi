from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def roll(input, shift, axis, name: Incomplete | None = None):
    """Rolls the elements of a tensor along an axis.

  The elements are shifted positively (towards larger indices) by the offset of
  `shift` along the dimension of `axis`. Negative `shift` values will shift
  elements in the opposite direction. Elements that roll passed the last position
  will wrap around to the first and vice versa. Multiple shifts along multiple
  axes may be specified.

  For example:

  ```
  # 't' is [0, 1, 2, 3, 4]
  roll(t, shift=2, axis=0) ==> [3, 4, 0, 1, 2]

  # shifting along multiple dimensions
  # 't' is [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
  roll(t, shift=[1, -2], axis=[0, 1]) ==> [[7, 8, 9, 5, 6], [2, 3, 4, 0, 1]]

  # shifting along the same axis multiple times
  # 't' is [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
  roll(t, shift=[2, -3], axis=[1, 1]) ==> [[1, 2, 3, 4, 0], [6, 7, 8, 9, 5]]
  ```

  Args:
    input: A `Tensor`.
    shift: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Dimension must be 0-D or 1-D. `shift[i]` specifies the number of places by which
      elements are shifted positively (towards larger indices) along the dimension
      specified by `axis[i]`. Negative shifts will roll the elements in the opposite
      direction.
    axis: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Dimension must be 0-D or 1-D. `axis[i]` specifies the dimension that the shift
      `shift[i]` should occur. If the same axis is referenced more than once, the
      total shift for that axis will be the sum of all the shifts that belong to that
      axis.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

Roll: Incomplete

def roll_eager_fallback(input, shift, axis, name, ctx): ...
