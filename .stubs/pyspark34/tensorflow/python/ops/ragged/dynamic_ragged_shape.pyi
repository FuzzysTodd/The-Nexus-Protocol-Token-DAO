import abc
from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, extension_type as extension_type, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.ops.ragged.row_partition import RowPartition as RowPartition, RowPartitionSpec as RowPartitionSpec
from tensorflow.python.types import core as core
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional, Sequence, Tuple, Union

class _DynamicRaggedShapeBatchEncoder(extension_type.ExtensionTypeBatchEncoder):
    """A batch encoder for DynamicRaggedShape below."""
    def batch(self, spec: DynamicRaggedShape.Spec, batch_size) -> DynamicRaggedShape.Spec: ...
    def unbatch(self, spec: DynamicRaggedShape.Spec) -> DynamicRaggedShape.Spec: ...
    def decode(self, spec: DynamicRaggedShape.Spec, encoding) -> DynamicRaggedShape: ...
    def encode(self, spec: DynamicRaggedShape.Spec, value, minimum_rank: int = 0) -> Union[ragged_tensor.RaggedTensor, ops.Tensor]: ...
    def encoding_specs(self, spec: DynamicRaggedShape.Spec) -> Union[ragged_tensor.RaggedTensorSpec, tensor_spec.TensorSpec]: ...

class DynamicRaggedShape(extension_type.BatchableExtensionType):
    """The shape of a ragged or dense tensor.

  Ragged shapes are encoded using two fields:

  * `inner_shape`: An integer vector giving the shape of a dense tensor.
  * `row_partitions`: A list of `RowPartition` objects, describing how
    that flat shape should be partitioned to add ragged axes.

  If a DynamicRaggedShape is the shape of a RaggedTensor rt, then:
  1. row_partitions = rt._nested_row_partitions
     (and thus len(row_partitions) > 0)
  2. inner_shape is the shape of rt.flat_values

  If a DynamicRaggedShape is the shape of a dense tensor t, then:
  1. row_partitions = []
  2. inner_shape is the shape of t.

  Examples:

  The following table gives a few examples (where `RP(lengths)` is short
  for `RowPartition.from_lengths(lengths)`):

  Row Partitions              | Inner Shape  | Example Tensor
  --------------------------- | ------------ | ----------------------------
  []                          | [2, 3]       | `[[1, 2, 3], [4, 5, 6]]`
  [RP([2, 0, 3])]             | [5]          | `[[1, 2], [], [3, 4, 5]]`
  [RP([2, 1])]                | [3, 2]       | `[[[1, 2], [3, 4]], [[5, 6]]]`
  [RP([2, 1]), RP([2, 1, 2])] | [5]          | `[[[1, 2], [3]], [[4, 5]]]`
  """
    __batch_encoder__: Incomplete
    def __init__(self, row_partitions: Sequence[RowPartition], inner_shape: core.TensorLike, dtype: Optional[dtypes.DType] = None, validate: bool = False, static_inner_shape: Any = None) -> None:
        """Core constructor for a DynamicRaggedShape.

    Create a DynamicRaggedShape. This can be used to construct a
    DynamicRaggedShape representing a ragged or dense shape. If row_partitions
    is an empty list, then this is equivalent to a dense shape.

    If row_partitions is specified, then the num_row_partitions will be equal
    to len(row_partitions). There are several checks made.
    Specifically:
    1. Consecutive row_partitions must have consistent nvals and nrows.
    2. The last row_partitions must have nvals equal to the first element of
       inner_shape.

    The inner_shape is converted to a tensor.
    All row_partitions and the inner_shape are converted to the same dtype
    (int64 or int32).

    Args:
      row_partitions: the row_partitions of the shape.
      inner_shape: if len(row_partitions) > 0, the shape of the flat_values.
        Otherwise, the shape of the tensor.
      dtype: tf.int64, tf.int32, or None representing the preferred dtype.
      validate: if true, dynamic validation is applied to the shape.
      static_inner_shape: if len(row_partitions) > 0, the static shape of the
        flat_values. Otherwise, the static shape of the tensor. Should be
        convertible to a TensorShape.
    """
    @classmethod
    def from_lengths(cls, lengths: Sequence[Union[Sequence[int], int]], num_row_partitions: Incomplete | None = None, dtype=...):
        """Creates a shape with the given lengths and num_row_partitions.

    The lengths can either be a nonnegative int or a list of nonnegative ints.

    If num_row_partitions is None, then the minimal num_row_partitions is used.

    For example, [2, (3, 2)] is the shape of [[0, 0, 0], [0, 0]], and
    [2, 2] is the shape of [[0, 0], [0, 0]]

    This chooses the minimal num_row_partitions required (including zero).

    The following table gives a few examples (where `RP(lengths)` is short
    for `RowPartition.from_lengths(lengths)`):

    For example:
    from_lengths           | row_partitions            | inner_shape
    ---------------------- | --------------------------| -------------
    []                     | []                        | []
    [2, (3, 2)]            | [RP([3, 2])]              | [5]
    [2, 2]                 | []                        | [2, 2]
    [2, (3, 2), 7]         | [RP([3, 2])]              | [5, 7]
    [2, (2, 2), 3]         | [RP([2, 2])]              | [4, 3]
    [2, 2, 3]              | []                        | [2, 2, 3]
    [2, (2, 1), (2, 0, 3)] | [RP(2, 1), RP([2, 0, 3])] | [5]

    If we want the row partitions to end with uniform row partitions, then
    we can set num_row_partitions.

    For example,
    below URP(3, 12) is RowPartition.from_uniform_row_length(3, 12)

    from_lengths   | num_row_partitions | row_partitions           | inner_shape
    ---------------| -------------------|--------------------------|------------
    [2, (3, 2), 2] | 2                  | [RP([3, 2]), URP(2, 10)] | [10]
    [2, 2]         | 1                  | [URP(2, 4)]              | [4]
    [2, 2, 3]      | 0                  | []                       | [2, 2, 3]
    [2, 2, 3]      | 1                  | [URP(2, 4)]              | [4, 3]
    [2, 2, 3]      | 2                  | [URP(2, 4), URP(3, 12)]  | [12]



    Representing the shapes from init():

    from_lengths             | Tensor Example
    ------------------------ | ------------------------------
    `[2, 3]`                 | `[[1, 2, 3], [4, 5, 6]]`
    `[3, (2, 0, 3)]`         | `[[1, 2], [], [3, 4, 5]]`
    `[2, (2, 1), 2]`         | `[[[1, 2], [3, 4]], [[5, 6]]]`
    `[2, (2, 1), (2, 1, 2)]` | `[[[1, 2], [3]], [[4, 5]]]`

    Args:
      lengths: the lengths of sublists along each axis.
      num_row_partitions: the num_row_partitions of the result or None
        indicating the minimum number of row_partitions.
      dtype: the dtype of the shape (tf.int32 or tf.int64).

    Returns:
      a new DynamicRaggedShape
    """
    @classmethod
    def from_row_partitions(cls, row_partitions, dtype: Incomplete | None = None):
        """Create a shape from row_partitions.

    Args:
      row_partitions: a nonempty list of RowPartition objects.
      dtype: the dtype to use, or None to use the row_partitions dtype.

    Returns:
      a DynamicRaggedShape with inner_rank==1.
    """
    @classmethod
    def from_tensor(cls, t, dtype: Incomplete | None = None):
        """Constructs a ragged shape for a potentially ragged tensor."""
    @property
    def row_partitions(self):
        """The row_partitions of the shape."""
    @property
    def num_row_partitions(self):
        """The number of row_partitions of the shape."""
    @property
    def dtype(self):
        """The dtype of the shape -- one of tf.int32 or tf.int64."""
    def static_lengths(self, ragged_lengths: bool = True):
        """Returns a list of statically known axis lengths.

    This represents what values are known. For each row partition, it presents
    either the uniform row length (if statically known),
    the list of row lengths, or none if it is not statically known.
    For the inner shape, if the rank is known, then each dimension is reported
    if known, and None otherwise. If the rank of the inner shape is not known,
    then the returned list ends with an ellipsis.

    Args:
      ragged_lengths: If false, returns None for all ragged dimensions.

    Returns:
      A Sequence[Union[Sequence[int],int, None]] of lengths, with a possible
      Ellipsis at the end.
    """
    def __getitem__(self, index):
        """Returns a dimension or a slice of the shape.

    Ragged shapes can have ragged dimensions that depend upon other dimensions.
    Therefore, if you ask for a dimension that is ragged, this function returns
    a ValueError. For similar reasons, if a slice is selected that includes
    a ragged dimension without including the zero dimension, then this fails.

    Any slice that does not start at zero will return a shape
    with num_row_partitions == 0.

    Args:
      index: the index: can be an int or a slice.

    Raises:
      IndexError: if the index is not in range.
      ValueError: if the rank is unknown, or a ragged rank is requested
      incorrectly.
    """
    def is_uniform(self, axis):
        """Returns true if the indicated dimension is uniform."""
    @property
    def rank(self):
        """The number of dimensions in this shape, or None if unknown."""
    @property
    def inner_shape(self):
        """The inner dimension sizes for this shape.

    Returns:
      A 1-D integer `Tensor`.
    """
    @property
    def inner_rank(self):
        """The rank of inner_shape."""
    def with_dtype(self, dtype):
        """Change the dtype of the shape."""
    class Spec:
        """A Spec for DynamicRaggedShape: similar to a static shape."""
        def __init__(self, row_partitions: Tuple[RowPartitionSpec, ...], static_inner_shape: tensor_shape.TensorShape, dtype: dtypes.DType) -> None:
            """Create a Spec given row partitions, a static inner shape, and a dtype.

      Args:
        row_partitions: A sequence of `RowPartitionSpec`s describing how the
          ragged shape is partitioned.
        static_inner_shape: The static shape of the flat_values.
        dtype: The DType used to encode the shape (tf.int64 or tf.int32).
      """
        @classmethod
        def from_value(cls, value: Any) -> DynamicRaggedShape.Spec:
            """Create a Spec from a DynamicRaggedShape."""
        @property
        def dtype(self) -> dtypes.DType: ...
        @property
        def inner_rank(self) -> Optional[int]: ...
        @property
        def num_row_partitions(self) -> int: ...
        @property
        def rank(self) -> Optional[int]: ...
        def with_dtype(self, dtype: dtypes.DType) -> DynamicRaggedShape.Spec:
            """Return the same spec, but with a different DType."""

def broadcast_dynamic_shape(shape_x: DynamicRaggedShape, shape_y: DynamicRaggedShape) -> DynamicRaggedShape:
    """Returns the shape formed by broadcasting two shapes to be compatible.

  1. If shape_x and shape_y both have row_partitions, then fail if their dtypes
     don't match.
  2. If neither has row_partitions and they have different dtypes,
     go with int64.
  3. If one has row_partitions, go with that dtype.

  Args:
    shape_x: A `DynamicRaggedShape`
    shape_y: A `DynamicRaggedShape`

  Returns:
    A `DynamicRaggedShape`.
  Raises:
    ValueError: If `shape_x` and `shape_y` are not broadcast-compatible.
  """
def broadcast_to(rt_input, shape: DynamicRaggedShape):
    """Broadcasts a potentially ragged tensor to a ragged shape.

  Tiles `rt_input` as necessary to match the given shape.

  Behavior is undefined if `rt_input` is not broadcast-compatible with `shape`.

  Args:
    rt_input: The potentially ragged tensor to broadcast.
    shape: A `DynamicRaggedShape`

  Returns:
    A potentially ragged tensor whose values are taken from
    `rt_input`, and whose shape matches `shape`.
  """
def broadcast_dynamic_shape_extended(a: DynamicRaggedShape, b: DynamicRaggedShape):
    """Gets the smallest shape to which a and b can broadcast.

  In order to create the smallest shape, one must also do most of the
  work to figure out how to transform from the shapes given. Thus, in addition
  to returning the shape, it also creates transformations from the
  original shapes to the result.

  This is the equivalent of:

  c = broadcast_dynamic_shape(a, b)
  ac = get_broadcaster(a, c)
  bc = get_broadcaster(b, c)
  return (c, ac, bc)

  Args:
    a: a DynamicRaggedShape
    b: a DynamicRaggedShape

  Returns:
    A triple of a shape and two broadcasters.
  """
def ragged_binary_elementwise_op_impl(op, x, y):
    """Binary elementwise api handler for RaggedTensors."""
def ragged_binary_elementwise_assert_op_impl(op, x, y):
    """Binary elementwise assert api handler for RaggedTensors.

  This handles binary assert operations for ragged tensors. Compared with
  `ragged_binary_elementwise_op_impl`, this handler does not compute a ragged
  tensor as output. Instead, it applies the assert operation `op` to input
  tensors based on their ragged shapes and flat_values, and returns the result
  of the assertion operation.

  Args:
    op: a binary assert operation on Tensors.
    x: something that can be coerced to a Tensor or RaggedTensor.
    y: something that can be coerced to a Tensor or RaggedTensor.

  Returns:
    the result of the assertion operation.

  """

class _LayerBroadcaster(abc.ABC, metaclass=abc.ABCMeta):
    """A broadcaster of a single layer.

  Although this class does not literally contain a gather_index, the reference
  implementation is defined through a gather_index. Thus, any subclasses should
  first define the gather_index property. Other functions can be overridden
  for optimization, but it should not change the behavior.
  """
    @property
    @abc.abstractmethod
    def gather_index(self):
        """Returns a 1D tensor.

    The size of the 1D tensor is equal to the destination size.

    The ith element of the result is the index of the source of the ith element.
    """
    @property
    def dtype(self):
        """Returns the dtype of the broadcast."""
    @abc.abstractmethod
    def with_dtype(self, dtype):
        """Returns an identical _LayerBroadcaster with a different dtype."""
    @classmethod
    def from_gather_index(cls, gather_index):
        """Create a broadcaster from a gather_index."""
    @classmethod
    def first_layer(cls, nrows_source, nrows_target):
        """Create a broadcaster from a gather_index."""
    @classmethod
    def get_singleton_broadcaster(cls, target_size):
        """Broadcast from 1 element to target_size elements."""
    @abc.abstractmethod
    def with_dependencies(self, checks):
        """Add dependencies to a _LayerBroadcaster.

    Args:
      checks: a list of ops that need to be run before any tensors from the
        Broadcaster are used.

    Returns:
      a copy of this _LayerBroadcaster with dependencies added.
    """
    @classmethod
    def get_identity_broadcaster(cls, nvals, dtype: Incomplete | None = None):
        """Create an identity broadcaster.

    TODO(martinz): an identity broadcaster can be far more efficient than a
    generic broadcaster. Add an optimized implementation.
    Args:
      nvals: the number of values for the broadcaster.
      dtype: the dtype of the broadcaster, or None to use the dtype of nvals.

    Returns:
      an identity broadcaster from [0....nvals-1] to [0...nvals-1]
    """
    def broadcast_tensor(self, tensor):
        """Broadcast from a dense tensor.

    It is assumed that the first axis of the dense tensor is indexed by the
    source shape, and at the end, the first axis of the dense tensor is
    indexed by the destination shape.

    Args:
      tensor: a dense tensor.

    Returns:
      A dense tensor.
    """
    def dest_nrows(self):
        """Return the number of rows in the resulting gather, or None if tiling."""
    def broadcast_row_partition(self, rp):
        """Return a new shape where the rows are broadcasted.

        *--self--->*
        |          |
        rp       result
        |          |
        V          V
        *--------->*

    This is equivalent to:
      return RowPartition.from_row_lengths(self.broadcast(rp.row_lengths()))

    However, if the shape has uniform row length, then that property is
    maintained.

    Args:
      rp: a row partition.

    Returns:
      a RowPartition representing a broadcast version of this row partition.
    """
    def next_layer(self, original_rp, broadcast_rp):
        """Create the next layer gather_index whether or not a broadcast happens.

       *---------self------->*
       |                     |
    original_rp           broadcast_rp
       |                     |
      \\|/                   \\|/
       *--next_broadcaster-->*
    Args:
      original_rp: the original row partition.
      broadcast_rp: the target row partition.

    Returns:
      the gather_index for next_broadcaster.

    """

class _GatherLayerBroadcaster(_LayerBroadcaster):
    """Implements _LayerBroadcaster with an explicit gather_index.

  For example, suppose that the source shape is:
  [*],[*,*]
  And the target shape is:
  [*],[*,*],[*],[*,*]
  Then, this can be represented with a map:
  [0,1,2,0,1,2]

  """
    def __init__(self, gather_index) -> None: ...
    @property
    def gather_index(self): ...
    def with_dtype(self, dtype): ...
    def with_dependencies(self, checks): ...

class _Broadcaster:
    """A _Broadcaster represents a transformation from one shape to another.

  It provides a transform for each axis of the source shape to the
  corresponding axis of the destination shape.

  """
    def __init__(self, source_shape, target_shape, layer_broadcasters, dtype: Incomplete | None = None) -> None:
        """Create a broadcaster.

    Do not call directly.
    The source_shape, target_shape, and layer_broadcasters are converted
    to have the same dtype.

    Note: source_shape.rank and target_shape.rank must be known.
    Args:
      source_shape: the source DynamicRaggedShape
      target_shape: the target DynamicRaggedShape
      layer_broadcasters: List[_LayerBroadcaster] of length source_shape.rank.
      dtype: the preferred dtype of the broadcaster.

    Raises:
      TypeError: if the input types don't match.
    """
    def with_dtype(self, dtype):
        """Return a copy of this Broadcaster with a different dtype."""
    @property
    def source_shape(self): ...
    @property
    def target_shape(self): ...
    @property
    def dtype(self): ...
    def broadcast_flat_values(self, rt, inner_dimensions: bool = True):
        """flat_values of a ragged tensor broadcast to target_shape.

    If inner_dimensions==True, then the result is a dense tensor with shape
    target_shape.inner_shape, the flat values of the broadcasted shape.

    If you add target_shape.row_partitions, you will get the full broadcasted
    shape.

    If inner_dimensions==False, the result is a dense tensor that satsifies
    certain properties:
    1. broadcast_to(result, target_shape.inner_shape) will give the result
       if inner_dimensions==True.
    2. Either (a) (result.rank < target_shape.inner_rank)
       or (b) (result.shape[0] == target_shape.inner_shape[0]).
    3. result.rank = min(target_shape.inner_rank, rt.rank)
    4. For i < target_shape.inner_rank - 1, and i < rt.rank,
       and if rt.shape[-i]!=1, then result.shape[-i]=target_shape[-i].
    Args:
      rt: a ragged or dense tensor.
      inner_dimensions: if true, broadcast the inner dimensions as well.

    Returns:
      a dense tensor
    """
    def broadcast(self, rt):
        """Broadcast a tensor of source_shape to target_shape."""

DenseOrRaggedShape: Incomplete

def ones(shape: DynamicRaggedShape, dtype=..., name: Optional[str] = None) -> ragged_tensor.RaggedOrDense:
    """Returns ones shaped like x."""
