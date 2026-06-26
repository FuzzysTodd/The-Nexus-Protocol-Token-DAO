from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_getitem as ragged_getitem, ragged_tensor as ragged_tensor
from tensorflow.python.util import tf_decorator as tf_decorator

def ragged_eq(self, other):
    """Returns result of elementwise `==` or False if not broadcast-compatible.

  Compares two ragged tensors elemewise for equality if they are
  broadcast-compatible; or returns False if they are not
  [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

  Note that this behavior differs from `tf.math.equal`, which raises an
  exception if the two ragged tensors are not broadcast-compatible.

  For example:

  >>> rt1 = tf.ragged.constant([[1, 2], [3]])
  >>> rt1 == rt1
  <tf.RaggedTensor [[True, True], [True]]>

  >>> rt2 = tf.ragged.constant([[1, 2], [4]])
  >>> rt1 == rt2
  <tf.RaggedTensor [[True, True], [False]]>

  >>> rt3 = tf.ragged.constant([[1, 2], [3, 4]])
  >>> # rt1 and rt3 are not broadcast-compatible.
  >>> rt1 == rt3
  False

  >>> # You can also compare a `tf.RaggedTensor` to a `tf.Tensor`.
  >>> t = tf.constant([[1, 2], [3, 4]])
  >>> rt1 == t
  False
  >>> t == rt1
  False
  >>> rt4 = tf.ragged.constant([[1, 2], [3, 4]])
  >>> rt4 == t
  <tf.RaggedTensor [[True, True], [True, True]]>
  >>> t == rt4
  <tf.RaggedTensor [[True, True], [True, True]]>

  Args:
    other: The right-hand side of the `==` operator.

  Returns:
    The ragged tensor result of the elementwise `==` operation, or `False` if
    the arguments are not broadcast-compatible.
  """
def ragged_ge(self, other):
    """Elementwise `>=` comparison of two convertible-to-ragged-tensor values.

  Computes the elemewise `>=` comparison of two values that are convertible to
  ragged tenors, with [broadcasting]
  (http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) support.
  Raises an exception if two values are not broadcast-compatible.

  For example:

  >>> rt1 = tf.ragged.constant([[1, 2], [3]])
  >>> rt1 >= rt1
  <tf.RaggedTensor [[True, True], [True]]>

  >>> rt2 = tf.ragged.constant([[2, 1], [3]])
  >>> rt1 >= rt2
  <tf.RaggedTensor [[False, True], [True]]>

  >>> rt3 = tf.ragged.constant([[1, 2], [3, 4]])
  >>> # rt1 and rt3 are not broadcast-compatible.
  >>> rt1 >= rt3
  Traceback (most recent call last):
  ...
  InvalidArgumentError: ...

  >>> # You can also compare a `tf.RaggedTensor` to a `tf.Tensor`.
  >>> rt4 = tf.ragged.constant([[1, 2],[3, 4]])
  >>> t1 = tf.constant([[2, 1], [4, 3]])
  >>> rt4 >= t1
  <tf.RaggedTensor [[False, True],
   [False, True]]>
  >>> t1 >= rt4
  <tf.RaggedTensor [[True, False],
   [True, False]]>

  >>> # Compares a `tf.RaggedTensor` to a `tf.Tensor` with broadcasting.
  >>> t2 = tf.constant([[2]])
  >>> rt4 >= t2
  <tf.RaggedTensor [[False, True],
   [True, True]]>
  >>> t2 >= rt4
  <tf.RaggedTensor [[True, True],
   [False, False]]>

  Args:
    other: The right-hand side of the `>=` operator.

  Returns:
    A `tf.RaggedTensor` of dtype `tf.bool` with the shape that `self` and
    `other` broadcast to.

  Raises:
    InvalidArgumentError: If `self` and `other` are not broadcast-compatible.
  """
def ragged_abs(self, name: Incomplete | None = None):
    """Computes the absolute value of a ragged tensor.

  Given a ragged tensor of integer or floating-point values, this operation
  returns a ragged tensor of the same type, where each element contains the
  absolute value of the corresponding element in the input.

  Given a ragged tensor `x` of complex numbers, this operation returns a tensor
  of type `float32` or `float64` that is the absolute value of each element in
  `x`. For a complex number \\\\(a + bj\\\\), its absolute value is computed as
  \\\\(\\sqrt{a^2 + b^2}\\\\).

  For example:

  >>> # real number
  >>> x = tf.ragged.constant([[-2.2, 3.2], [-4.2]])
  >>> tf.abs(x)
  <tf.RaggedTensor [[2.2, 3.2], [4.2]]>

  >>> # complex number
  >>> x = tf.ragged.constant([[-2.2 + 4.7j], [-3.2 + 5.7j], [-4.2 + 6.7j]])
  >>> tf.abs(x)
  <tf.RaggedTensor [[5.189412298131649],
   [6.536818798161687],
   [7.907591289387685]]>

  Args:
    name: A name for the operation (optional).

  Returns:
    A `RaggedTensor` of the same size and type as `x`, with absolute values.
    Note, for `complex64` or `complex128` input, the returned `RaggedTensor`
    will be of type `float32` or `float64`, respectively.
  """
def ragged_and(self, y, name: Incomplete | None = None):
    """Returns the truth value of elementwise `x & y`.

  Logical AND function.

  Requires that `x` and `y` have the same shape or have
  [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
  shapes. For example, `y` can be:

    - A single Python boolean, where the result will be calculated by applying
      logical AND with the single element to each element in `x`.
    - A `tf.Tensor` object of dtype `tf.bool` of the same shape or
      [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
      shape. In this case, the result will be the element-wise logical AND of
      `x` and `y`.
    - A `tf.RaggedTensor` object of dtype `tf.bool` of the same shape or
      [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
      shape. In this case, the result will be the element-wise logical AND of
      `x` and `y`.

  For example:

  >>> # `y` is a Python boolean
  >>> x = tf.ragged.constant([[True, False], [True]])
  >>> y = True
  >>> x & y
  <tf.RaggedTensor [[True, False], [True]]>
  >>> tf.math.logical_and(x, y)  # Equivalent of x & y
  <tf.RaggedTensor [[True, False], [True]]>
  >>> y & x
  <tf.RaggedTensor [[True, False], [True]]>
  >>> tf.math.reduce_all(x & y)  # Reduce to a scalar bool Tensor.
  <tf.Tensor: shape=(), dtype=bool, numpy=False>

  >>> # `y` is a tf.Tensor of the same shape.
  >>> x = tf.ragged.constant([[True, False], [True, False]])
  >>> y = tf.constant([[True, False], [False, True]])
  >>> x & y
  <tf.RaggedTensor [[True, False], [False, False]]>

  >>> # `y` is a tf.Tensor of a broadcast-compatible shape.
  >>> x = tf.ragged.constant([[True, False], [True]])
  >>> y = tf.constant([[True], [False]])
  >>> x & y
  <tf.RaggedTensor [[True, False], [False]]>

  >>> # `y` is a `tf.RaggedTensor` of the same shape.
  >>> x = tf.ragged.constant([[True, False], [True]])
  >>> y = tf.ragged.constant([[False, True], [True]])
  >>> x & y
  <tf.RaggedTensor [[False, False], [True]]>

  >>> # `y` is a `tf.RaggedTensor` of a broadcast-compatible shape.
  >>> x = tf.ragged.constant([[[True, True, False]], [[]], [[True, False]]])
  >>> y = tf.ragged.constant([[[True]], [[True]], [[False]]], ragged_rank=1)
  >>> x & y
  <tf.RaggedTensor [[[True, True, False]], [[]], [[False, False]]]>

  Args:
    y: A Python boolean or a `tf.Tensor` or `tf.RaggedTensor` of dtype
      `tf.bool`.
    name: A name for the operation (optional).

  Returns:
    A `tf.RaggedTensor` of dtype `tf.bool` with the shape that `x` and `y`
    broadcast to.
  """
def ragged_hash(self):
    """The operation invoked by the `RaggedTensor.__hash__` operator."""
def ragged_bool(self) -> None:
    """Raises TypeError when a RaggedTensor is used as a Python bool.

  To prevent RaggedTensor from being used as a bool, this function always raise
  TypeError when being called.

  For example:

  >>> x = tf.ragged.constant([[1, 2], [3]])
  >>> result = True if x else False  # Evaluate x as a bool value.
  Traceback (most recent call last):
  ...
  TypeError: RaggedTensor may not be used as a boolean.

  >>> x = tf.ragged.constant([[1]])
  >>> r = (x == 1)  # tf.RaggedTensor [[True]]
  >>> if r:  # Evaluate r as a bool value.
  ...   pass
  Traceback (most recent call last):
  ...
  TypeError: RaggedTensor may not be used as a boolean.
  """
