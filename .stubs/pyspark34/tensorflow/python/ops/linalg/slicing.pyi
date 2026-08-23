__all__ = ['batch_slice']

def batch_slice(linop, params_overrides, slices):
    """Slices `linop` along its batch dimensions.

  Args:
    linop: A `LinearOperator` instance.
    params_overrides: A `dict` of parameter overrides.
    slices: A `slice` or `int` or `int` `Tensor` or `tf.newaxis` or `tuple`
      thereof. (e.g. the argument of a `__getitem__` method).

  Returns:
    new_linop: A batch-sliced `LinearOperator`.
  """
