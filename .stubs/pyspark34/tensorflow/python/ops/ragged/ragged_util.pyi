from _typeshed import Incomplete
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, gen_ragged_math_ops as gen_ragged_math_ops, math_ops as math_ops

def assert_splits_match(nested_splits_lists):
    """Checks that the given splits lists are identical.

  Performs static tests to ensure that the given splits lists are identical,
  and returns a list of control dependency op tensors that check that they are
  fully identical.

  Args:
    nested_splits_lists: A list of nested_splits_lists, where each split_list is
      a list of `splits` tensors from a `RaggedTensor`, ordered from outermost
      ragged dimension to innermost ragged dimension.

  Returns:
    A list of control dependency op tensors.
  Raises:
    ValueError: If the splits are not identical.
  """

get_positive_axis: Incomplete
convert_to_int_tensor: Incomplete
repeat: Incomplete

def lengths_to_splits(lengths):
    """Returns splits corresponding to the given lengths."""
def repeat_ranges(params, splits, repeats):
    """Repeats each range of `params` (as specified by `splits`) `repeats` times.

  Let the `i`th range of `params` be defined as
  `params[splits[i]:splits[i + 1]]`.  Then this function returns a tensor
  containing range 0 repeated `repeats[0]` times, followed by range 1 repeated
  `repeats[1]`, ..., followed by the last range repeated `repeats[-1]` times.

  Args:
    params: The `Tensor` whose values should be repeated.
    splits: A splits tensor indicating the ranges of `params` that should be
      repeated.
    repeats: The number of times each range should be repeated.  Supports
      broadcasting from a scalar value.

  Returns:
    A `Tensor` with the same rank and type as `params`.

  #### Example:

  >>> print(repeat_ranges(
  ...     params=tf.constant(['a', 'b', 'c']),
  ...     splits=tf.constant([0, 2, 3]),
  ...     repeats=tf.constant(3)))
  tf.Tensor([b'a' b'b' b'a' b'b' b'a' b'b' b'c' b'c' b'c'],
      shape=(9,), dtype=string)
  """
