from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, indexed_slices as indexed_slices, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gradients as gradients, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

def compute_gradient(x, x_shape, y, y_shape, x_init_value: Incomplete | None = None, delta: float = 0.001, init_targets: Incomplete | None = None, extra_feed_dict: Incomplete | None = None):
    '''Computes and returns the theoretical and numerical Jacobian.

  If `x` or `y` is complex, the Jacobian will still be real but the
  corresponding Jacobian dimension(s) will be twice as large.  This is required
  even if both input and output is complex since TensorFlow graphs are not
  necessarily holomorphic, and may have gradients not expressible as complex
  numbers.  For example, if `x` is complex with shape `[m]` and `y` is complex
  with shape `[n]`, each Jacobian `J` will have shape `[m * 2, n * 2]` with

      J[:m, :n] = d(Re y)/d(Re x)
      J[:m, n:] = d(Im y)/d(Re x)
      J[m:, :n] = d(Re y)/d(Im x)
      J[m:, n:] = d(Im y)/d(Im x)

  Args:
    x: a tensor or list of tensors
    x_shape: the dimensions of x as a tuple or an array of ints. If x is a list,
    then this is the list of shapes.
    y: a tensor
    y_shape: the dimensions of y as a tuple or an array of ints.
    x_init_value: (optional) a numpy array of the same shape as "x"
      representing the initial value of x. If x is a list, this should be a list
      of numpy arrays.  If this is none, the function will pick a random tensor
      as the initial value.
    delta: (optional) the amount of perturbation.
    init_targets: list of targets to run to initialize model params.
    extra_feed_dict: dict that allows fixing specified tensor values
      during the Jacobian calculation.

  Returns:
    Two 2-d numpy arrays representing the theoretical and numerical
    Jacobian for dy/dx. Each has "x_size" rows and "y_size" columns
    where "x_size" is the number of elements in x and "y_size" is the
    number of elements in y. If x is a list, returns a list of two numpy arrays.
  '''
def compute_gradient_error(x, x_shape, y, y_shape, x_init_value: Incomplete | None = None, delta: float = 0.001, init_targets: Incomplete | None = None, extra_feed_dict: Incomplete | None = None):
    '''Computes the gradient error.

  Computes the maximum error for dy/dx between the computed Jacobian and the
  numerically estimated Jacobian.

  This function will modify the tensors passed in as it adds more operations
  and hence changing the consumers of the operations of the input tensors.

  This function adds operations to the current session. To compute the error
  using a particular device, such as a GPU, use the standard methods for
  setting a device (e.g. using with sess.graph.device() or setting a device
  function in the session constructor).

  Args:
    x: a tensor or list of tensors
    x_shape: the dimensions of x as a tuple or an array of ints. If x is a list,
    then this is the list of shapes.
    y: a tensor
    y_shape: the dimensions of y as a tuple or an array of ints.
    x_init_value: (optional) a numpy array of the same shape as "x"
      representing the initial value of x. If x is a list, this should be a list
      of numpy arrays.  If this is none, the function will pick a random tensor
      as the initial value.
    delta: (optional) the amount of perturbation.
    init_targets: list of targets to run to initialize model params.
    extra_feed_dict: dict that allows fixing specified tensor values
      during the Jacobian calculation.

  Returns:
    The maximum error in between the two Jacobians.
  '''
