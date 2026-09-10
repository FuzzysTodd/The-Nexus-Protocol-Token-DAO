from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_array_ops as ragged_array_ops, ragged_config as ragged_config, ragged_tensor as ragged_tensor, ragged_util as ragged_util

class RaggedTensorDynamicShape:
    '''A collection of tensors encoding the shape of a potentially ragged tensor.

  Each `RaggedTensorDynamicShape` consists of an ordered list of dimension
  sizes.  There are two dimension types:

    * "Uniform dimensions" are dimensions where all slices have the same
      length.  `RaggedTensorDynamicShape` records the size of each uniform
      dimension using a single scalar integer.

    * "Ragged dimensions" are dimensions whose slices may have different
      lengths.  `RaggedTensorDynamicShape` records the size of each ragged
      dimension using an integer vector containing the slice lengths for all
      the slices across that dimension.

  Furthermore, there are two ways a dimension might be encoded:

    * "Partitioned dimensions" are dimensions that are encoded using a
      `RaggedTensor`\'s `nested_row_splits`.  The outermostmost partitioned
      dimension must be uniform, and the innermost partitioned dimension must
      be ragged.

    * "Inner dimensions" are dimensions that are encoded using a
      `RaggedTensor`\'s `flat_values`.  Inner dimensions are always uniform.

  The sizes of partitioned dimensions are recorded using `partitioned_dim_sizes`
  and `inner_dim_sizes`:

    * `partitioned_dim_sizes` is a list of tensors (one for each partitioned
      dimension).

      * For uniform dimensions, the tensor is an integer scalar specifying the
        size of all slices across that dimension.
      * For ragged dimensions, the tensor is an integer vector specifying the
        size of each slice across that dimension.

    * `inner_dim_sizes` is a single integer vector, where each element
      specifies the size of a single inner dimension.

  Examples:

  Tensor                         | Ragged | Partitioned Dim Sizes  | Inner Dim
                                 : Rank   :                        : Sizes
  ------------------------------ | ------ | ---------------------- | ----------
  `[[1, 2, 3], [4, 5, 6]]`       |      0 |                        | `2, 3`
  `[[1, 2], [], [3, 4, 5]]`      |      1 | `3, (2, 0, 3)`         |
  `[[[1, 2], [3, 4]], [[5, 6]]]` |      1 | `2, (2, 1)`            | 2
  `[[[1, 2], [3]], [[4, 5]]]`    |      2 | `2, (2, 1), (2, 1, 2)` |
  '''
    def __init__(self, partitioned_dim_sizes, inner_dim_sizes, dim_size_dtype: Incomplete | None = None) -> None:
        """Creates a RaggedTensorDynamicShape.

    Args:
      partitioned_dim_sizes: A `list` of 0-D or 1-D integer `Tensor`, one for
        each partitioned dimension.  If dimension `d` is uniform, then
        `partitioned_dim_sizes[d]` must be an integer scalar, specifying the
        size of all slices across dimension `d`.  If dimension `d` is ragged,
        then `partitioned_dim_sizes[d]` must be an integer vector, specifying
        the size of each slice across dimension `d`.
      inner_dim_sizes: A 1-D integer `Tensor`, whose length is equal to the
        number of inner dimensions.  `inner_dim_sizes[n]` is the size of all
        slices across the `n`th inner dimension (which is the
        `(len(partitioned_dim_sizes)+n)`th dimension in the overall tensor.
      dim_size_dtype: dtype for dimension sizes.  If not specified, then it
        is chosen based on the dtypes of `partitioned_dim_sizes` and
        `inner_dim_sizes`.
    """
    @staticmethod
    def from_dim_sizes(dim_sizes):
        """Constructs a ragged shape from a list of dimension sizes.

    This list contains a single tensor for each dimension, where the tensor
    is a scalar if the dimension is uniform, or a vector if the dimension is
    ragged.

    Args:
      dim_sizes: List of int32 or int64 scalars or vectors.

    Returns:
      A RaggedTensorDynamicShape.
    """
    @classmethod
    def from_tensor(cls, rt_input, dim_size_dtype: Incomplete | None = None):
        """Constructs a ragged shape for a potentially ragged tensor."""
    def dimension_size(self, axis):
        """Returns the size of slices across the specified dimension."""
    def is_ragged(self, axis):
        """Returns true if the indicated dimension is ragged."""
    @property
    def rank(self):
        """The number of dimensions in this shape, or None if unknown."""
    @property
    def partitioned_dim_sizes(self):
        """The partitioned dimension sizes for this shape.

    Returns:
      A `list` of 0-D or 1-D integer `Tensor`.
    """
    @property
    def inner_dim_sizes(self):
        """The inner dimension sizes for this shape.

    Returns:
      A 1-D integer `Tensor`.
    """
    @property
    def num_partitioned_dimensions(self):
        """The number of partitioned dimensions in this shape."""
    @property
    def num_inner_dimensions(self):
        """The number of inner dimensions, or `None` if not statically known."""
    @property
    def dim_size_dtype(self):
        """DType used by this shape for dimension sizes."""
    def broadcast_to_rank(self, rank):
        """Adds leading size-1 dimensions to broadcast `self` to the given rank.

    E.g., if `shape1` is `[3, (D2), 4]`, then `shape1.broadcast_to_rank(5)`
    is `[1, 1, 3, (D2), 4]`.

    Args:
      rank: The rank for the returned shape.

    Returns:
      A RaggedTensorDynamicShape with `rank` dimensions, whose inner dimensions
      have the same size as `self` and whose outer dimensions have size `1`.

    Raises:
      ValueError: If `self.rank` is unknown or greater than `rank`.
    """
    def broadcast_dimension(self, axis, lengths):
        """Returns a shape that is broadcast-compatible with self & lengths.

    * If dimension[axis] is uniform and lengths is a scalar, the check
      that either lengths==1 or axis==1 or lengths==axis, and tile
      dimension[axis] with tf.where(lengths==axis, 1, axis) repeats.

    * If dimension[axis] is uniform and lengths is a vector, then check
      that dimension[axis]==1, and raggedly tile dimension[axis] with
      lengths repeats.  (we can skip tiling if we statically know that
      slice_lengths == 1??)

    * If dimension[axis] is ragged and lengths is a scalar, then check
      that lengths==1.

    * If dimension[axis] is ragged and lengths is a vector, then check
      that self.dimension_size(axis) == lengths.

    Args:
      axis: `int`.  The dimension to broadcast.
      lengths: 0-D or 1-D integer `Tensor`.

    Returns:
      A `RaggedTensorDynamicShape`.
    """
    def num_slices_in_dimension(self, axis):
        """Returns the total number of slices across the indicated dimension."""
    def with_dim_size_dtype(self, dtype): ...

def broadcast_dynamic_shape(shape_x, shape_y):
    """Returns the shape formed by broadcasting two shapes to be compatible.

  Args:
    shape_x: A `RaggedTensorDynamicShape`
    shape_y: A `RaggedTensorDynamicShape`

  Returns:
    A `RaggedTensorDynamicShape`.
  Raises:
    ValueError: If `shape_x` and `shape_y` are not broadcast-compatible.
  """
def broadcast_to(rt_input, shape, broadcast_inner_dimensions: bool = True):
    """Broadcasts a potentially ragged tensor to a ragged shape.

  Tiles `rt_input` as necessary to match the given shape.

  Behavior is undefined if `rt_input` is not broadcast-compatible with `shape`.

  Args:
    rt_input: The potentially ragged tensor to broadcast.
    shape: A `RaggedTensorDynamicShape`
    broadcast_inner_dimensions: If false, then inner dimensions will not be
      tiled.

  Returns:
    A potentially ragged tensor whose values are taken from
    `rt_input`, and whose shape matches `shape`.
  """
