from _typeshed import Incomplete
from tensorflow.python.eager import backprop as backprop, context as context
from tensorflow.python.framework import dtypes as dtypes, indexed_slices as indexed_slices, ops as ops
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

def compute_gradient(f, x, delta: Incomplete | None = None):
    '''Computes the theoretical and numeric Jacobian of `f`.

  With y = f(x), computes the theoretical and numeric Jacobian dy/dx.

  Args:
    f: the function.
    x: the arguments for the function as a list or tuple of values convertible
      to a Tensor.
    delta: (optional) perturbation used to compute numeric Jacobian.

  Returns:
    A pair of lists, where the first is a list of 2-d numpy arrays representing
    the theoretical Jacobians for each argument, and the second list is the
    numerical ones. Each 2-d array has "y_size" rows
    and "x_size" columns where "x_size" is the number of elements in the
    corresponding argument and "y_size" is the number of elements in f(x).

  Raises:
    ValueError: If result is empty but the gradient is nonzero.
    ValueError: If x is not list, but any other type.

  Example:

  >>> @tf.function
  ... def test_func(x):
  ...   return x*x
  ...
  >>>
  >>> class MyTest(tf.test.TestCase):
  ...
  ...   def test_gradient_of_test_func(self):
  ...     theoretical, numerical = tf.test.compute_gradient(test_func, [1.0])
  ...     # ((array([[2.]], dtype=float32),),
  ...     #  (array([[2.000004]], dtype=float32),))
  ...     self.assertAllClose(theoretical, numerical)

  '''
def max_error(grad1, grad2):
    """Computes maximum elementwise gap.

  Computes the maximum elementwise gap between two lists of tensors of the same
  shape.

  Args:
    grad1: a lists of tensors.
    grad2: a lists of tensors with the same shape as grad1.

  Returns:
    The maximum elementwise gap between the two.
  """
