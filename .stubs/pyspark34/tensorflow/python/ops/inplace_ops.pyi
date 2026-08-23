from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_array_ops as gen_array_ops, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation

def alias_inplace_update(x, i, v):
    """Applies an inplace update on input x at index i with value v. Aliases x.

  If i is None, x and v must be the same shape. Computes
    x = v;
  If i is a scalar, x has a rank 1 higher than v's. Computes
    x[i, :] = v;
  Otherwise, x and v must have the same rank. Computes
    x[i, :] = v;

  Args:
    x: A Tensor.
    i: None, a scalar or a vector.
    v: A Tensor.

  Returns:
    Returns x.

  """
def alias_inplace_add(x, i, v):
    """Applies an inplace add on input x at index i with value v. Aliases x.

  If i is None, x and v must be the same shape. Computes
    x += v;
  If i is a scalar, x has a rank 1 higher than v's. Computes
    x[i, :] += v;
  Otherwise, x and v must have the same rank. Computes
    x[i, :] += v;

  Args:
    x: A Tensor.
    i: None, a scalar or a vector.
    v: A Tensor.

  Returns:
    Returns x.

  """
def alias_inplace_sub(x, i, v):
    """Applies an inplace sub on input x at index i with value v. Aliases x.

  If i is None, x and v must be the same shape. Computes
    x -= v;
  If i is a scalar, x has a rank 1 higher than v's. Computes
    x[i, :] -= v;
  Otherwise, x and v must have the same rank. Computes
    x[i, :] -= v;

  Args:
    x: A Tensor.
    i: None, a scalar or a vector.
    v: A Tensor.

  Returns:
    Returns x.

  """
def empty_like(x, init: Incomplete | None = None):
    """Returns a non-initialized tensor with the same shape and dtype as x.

  Args:
    x: A Tensor.
    init: Initialize the returned tensor with the default value of
      x.dtype(), if True. Otherwise, do not initialize. Defaults to
      None.

  Returns:
    A tensor y, whose dtype and shape are the same as those of x.
    y is guaranteed not to be an alias of x. Upon return, y may contain
    arbitrary data.

  """
def inplace_update(x, i, v):
    """Applies an inplace update on input x at index i with value v.

  Note that this function is not actually inplace - it allocates
  a copy of x.  The utility is not avoiding memory copies but rather
  specifying a sparse update.

  If i is None, x and v must be the same shape. Computes
    y = x; y = v;
  If i is a scalar, x has a rank 1 higher than v's. Computes
    y = x; y[i, :] = v;
  Otherwise, x and v must have the same rank. Computes
    y = x; y[i, :] = v;

  Args:
    x: A Tensor.
    i: None, a scalar or a vector.
    v: A Tensor.

  Returns:
    Returns y, which is guaranteed not to be an alias of x.

  """
def inplace_add(x, i, v):
    """Applies an inplace add on input x at index i with value v.

  Note that this function is not actually inplace - it allocates
  a copy of x.  The utility is not avoiding memory copies but rather
  specifying a sparse update.

  If i is None, x and v must be the same shape. Computes
    y = x; y += v;
  If i is a scalar, x has a rank 1 higher than v's. Computes
    y = x; y[i, :] += v;
  Otherwise, x and v must have the same rank. Computes
    y = x; y[i, :] += v;

  Args:
    x: A Tensor.
    i: None, a scalar or a vector.
    v: A Tensor.

  Returns:
    Returns y, which is guaranteed not to be an alias of x.

  """
def inplace_sub(x, i, v):
    """Applies an inplace sub on input x at index i with value v.

  Note that this function is not actually inplace - it allocates
  a copy of x.  The utility is not avoiding memory copies but rather
  specifying a sparse update.

  If i is None, x and v must be the same shape. Computes
    y = x; y -= v;
  If i is a scalar, x has a rank 1 higher than v's. Computes
    y = x; y[i, :] -= v;
  Otherwise, x and v must have the same rank. Computes
    y = x; y[i, :] -= v;

  Args:
    x: A Tensor.
    i: None, a scalar or a vector.
    v: A Tensor.

  Returns:
    Returns y, which is guaranteed not to be an alias of x.

  """

empty: Incomplete
