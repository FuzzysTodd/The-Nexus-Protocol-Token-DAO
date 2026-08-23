from _typeshed import Incomplete
from tensorflow.python.ops import control_flow_ops as control_flow_ops, variables as variables

def convert_data_format(data_format, ndim): ...
def normalize_tuple(value, n, name):
    '''Transforms a single integer or iterable of integers into an integer tuple.

  Args:
    value: The value to validate and convert. Could an int, or any iterable
      of ints.
    n: The size of the tuple to be returned.
    name: The name of the argument being validated, e.g. "strides" or
      "kernel_size". This is only used to format error messages.

  Returns:
    A tuple of n integers.

  Raises:
    ValueError: If something else than an int/long or iterable thereof was
      passed.
  '''
def normalize_data_format(value): ...
def normalize_padding(value): ...
def conv_output_length(input_length, filter_size, padding, stride, dilation: int = 1):
    '''Determines output length of a convolution given input length.

  Args:
      input_length: integer.
      filter_size: integer.
      padding: one of "same", "valid", "full".
      stride: integer.
      dilation: dilation rate, integer.

  Returns:
      The output length (integer).
  '''
def conv_input_length(output_length, filter_size, padding, stride):
    '''Determines input length of a convolution given output length.

  Args:
      output_length: integer.
      filter_size: integer.
      padding: one of "same", "valid", "full".
      stride: integer.

  Returns:
      The input length (integer).
  '''
def deconv_output_length(input_length, filter_size, padding, stride):
    '''Determines output length of a transposed convolution given input length.

  Args:
      input_length: integer.
      filter_size: integer.
      padding: one of "same", "valid", "full".
      stride: integer.

  Returns:
      The output length (integer).
  '''
def smart_cond(pred, true_fn: Incomplete | None = None, false_fn: Incomplete | None = None, name: Incomplete | None = None):
    """Return either `true_fn()` if predicate `pred` is true else `false_fn()`.

  If `pred` is a bool or has a constant value, we return either `true_fn()`
  or `false_fn()`, otherwise we use `tf.cond` to dynamically route to both.

  Args:
    pred: A scalar determining whether to return the result of `true_fn` or
      `false_fn`.
    true_fn: The callable to be performed if pred is true.
    false_fn: The callable to be performed if pred is false.
    name: Optional name prefix when using `tf.cond`.

  Returns:
    Tensors returned by the call to either `true_fn` or `false_fn`.

  Raises:
    TypeError: If `true_fn` or `false_fn` is not callable.
  """
def constant_value(pred):
    """Return the bool value for `pred`, or None if `pred` had a dynamic value.

    Args:
      pred: A scalar, either a Python bool or a TensorFlow boolean variable
        or tensor, or the Python integer 1 or 0.

    Returns:
      True or False if `pred` has a constant boolean value, None otherwise.

    Raises:
      TypeError: If `pred` is not a Variable, Tensor or bool, or Python
        integer 1 or 0.
    """
