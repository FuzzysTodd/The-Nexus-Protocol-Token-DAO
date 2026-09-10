from _typeshed import Incomplete
from tensorflow.core.protobuf import struct_pb2 as struct_pb2
from tensorflow.python import tf2 as tf2
from tensorflow.python.client import session as session
from tensorflow.python.framework import composite_tensor as composite_tensor, composite_tensor_gradient as composite_tensor_gradient, constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec, type_spec_registry as type_spec_registry
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_ragged_conversion_ops as gen_ragged_conversion_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_config as ragged_config, ragged_tensor_value as ragged_tensor_value, ragged_util as ragged_util
from tensorflow.python.ops.ragged.row_partition import RowPartition as RowPartition
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.types import internal as internal_types
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls

class RaggedTensor(composite_tensor.CompositeTensor, internal_types.NativeObject):
    '''Represents a ragged tensor.

  A `RaggedTensor` is a tensor with one or more *ragged dimensions*, which are
  dimensions whose slices may have different lengths.  For example, the inner
  (column) dimension of `rt=[[3, 1, 4, 1], [], [5, 9, 2], [6], []]` is ragged,
  since the column slices (`rt[0, :]`, ..., `rt[4, :]`) have different lengths.
  Dimensions whose slices all have the same length are called *uniform
  dimensions*.  The outermost dimension of a `RaggedTensor` is always uniform,
  since it consists of a single slice (and so there is no possibility for
  differing slice lengths).

  The total number of dimensions in a `RaggedTensor` is called its *rank*,
  and the number of ragged dimensions in a `RaggedTensor` is called its
  *ragged-rank*.  A `RaggedTensor`\'s ragged-rank is fixed at graph creation
  time: it can\'t depend on the runtime values of `Tensor`s, and can\'t vary
  dynamically for different session runs.

  Note that the `__init__` constructor is private. Please use one of the
  following methods to construct a `RaggedTensor`:

  * `tf.RaggedTensor.from_row_lengths`
  * `tf.RaggedTensor.from_value_rowids`
  * `tf.RaggedTensor.from_row_splits`
  * `tf.RaggedTensor.from_row_starts`
  * `tf.RaggedTensor.from_row_limits`
  * `tf.RaggedTensor.from_nested_row_splits`
  * `tf.RaggedTensor.from_nested_row_lengths`
  * `tf.RaggedTensor.from_nested_value_rowids`

  ### Potentially Ragged Tensors

  Many ops support both `Tensor`s and `RaggedTensor`s
  (see [tf.ragged](https://www.tensorflow.org/api_docs/python/tf/ragged) for a
  full listing). The term "potentially ragged tensor" may be used to refer to a
  tensor that might be either a `Tensor` or a `RaggedTensor`.  The ragged-rank
  of a `Tensor` is zero.

  ### Documenting RaggedTensor Shapes

  When documenting the shape of a RaggedTensor, ragged dimensions can be
  indicated by enclosing them in parentheses.  For example, the shape of
  a 3-D `RaggedTensor` that stores the fixed-size word embedding for each
  word in a sentence, for each sentence in a batch, could be written as
  `[num_sentences, (num_words), embedding_size]`.  The parentheses around
  `(num_words)` indicate that dimension is ragged, and that the length
  of each element list in that dimension may vary for each item.

  ### Component Tensors

  Internally, a `RaggedTensor` consists of a concatenated list of values that
  are partitioned into variable-length rows.  In particular, each `RaggedTensor`
  consists of:

    * A `values` tensor, which concatenates the variable-length rows into a
      flattened list.  For example, the `values` tensor for
      `[[3, 1, 4, 1], [], [5, 9, 2], [6], []]` is `[3, 1, 4, 1, 5, 9, 2, 6]`.

    * A `row_splits` vector, which indicates how those flattened values are
      divided into rows.  In particular, the values for row `rt[i]` are stored
      in the slice `rt.values[rt.row_splits[i]:rt.row_splits[i+1]]`.

  Example:

  >>> print(tf.RaggedTensor.from_row_splits(
  ...       values=[3, 1, 4, 1, 5, 9, 2, 6],
  ...       row_splits=[0, 4, 4, 7, 8, 8]))
  <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>

  ### Alternative Row-Partitioning Schemes

  In addition to `row_splits`, ragged tensors provide support for five other
  row-partitioning schemes:

    * `row_lengths`: a vector with shape `[nrows]`, which specifies the length
      of each row.

    * `value_rowids` and `nrows`: `value_rowids` is a vector with shape
      `[nvals]`, corresponding one-to-one with `values`, which specifies
      each value\'s row index.  In particular, the row `rt[row]` consists of the
      values `rt.values[j]` where `value_rowids[j]==row`.  `nrows` is an
      integer scalar that specifies the number of rows in the
      `RaggedTensor`. (`nrows` is used to indicate trailing empty rows.)

    * `row_starts`: a vector with shape `[nrows]`, which specifies the start
      offset of each row.  Equivalent to `row_splits[:-1]`.

    * `row_limits`: a vector with shape `[nrows]`, which specifies the stop
      offset of each row.  Equivalent to `row_splits[1:]`.

    * `uniform_row_length`: A scalar tensor, specifying the length of every
      row.  This row-partitioning scheme may only be used if all rows have
      the same length.

  Example: The following ragged tensors are equivalent, and all represent the
  nested list `[[3, 1, 4, 1], [], [5, 9, 2], [6], []]`.

  >>> values = [3, 1, 4, 1, 5, 9, 2, 6]
  >>> RaggedTensor.from_row_splits(values, row_splits=[0, 4, 4, 7, 8, 8])
  <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>
  >>> RaggedTensor.from_row_lengths(values, row_lengths=[4, 0, 3, 1, 0])
  <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>
  >>> RaggedTensor.from_value_rowids(
  ...     values, value_rowids=[0, 0, 0, 0, 2, 2, 2, 3], nrows=5)
  <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>
  >>> RaggedTensor.from_row_starts(values, row_starts=[0, 4, 4, 7, 8])
  <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>
  >>> RaggedTensor.from_row_limits(values, row_limits=[4, 4, 7, 8, 8])
  <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>
  >>> RaggedTensor.from_uniform_row_length(values, uniform_row_length=2)
  <tf.RaggedTensor [[3, 1], [4, 1], [5, 9], [2, 6]]>

  ### Multiple Ragged Dimensions

  `RaggedTensor`s with multiple ragged dimensions can be defined by using
  a nested `RaggedTensor` for the `values` tensor.  Each nested `RaggedTensor`
  adds a single ragged dimension.

  >>> inner_rt = RaggedTensor.from_row_splits(  # =rt1 from above
  ...     values=[3, 1, 4, 1, 5, 9, 2, 6], row_splits=[0, 4, 4, 7, 8, 8])
  >>> outer_rt = RaggedTensor.from_row_splits(
  ...     values=inner_rt, row_splits=[0, 3, 3, 5])
  >>> print(outer_rt.to_list())
  [[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]
  >>> print(outer_rt.ragged_rank)
  2

  The factory function `RaggedTensor.from_nested_row_splits` may be used to
  construct a `RaggedTensor` with multiple ragged dimensions directly, by
  providing a list of `row_splits` tensors:

  >>> RaggedTensor.from_nested_row_splits(
  ...     flat_values=[3, 1, 4, 1, 5, 9, 2, 6],
  ...     nested_row_splits=([0, 3, 3, 5], [0, 4, 4, 7, 8, 8])).to_list()
  [[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]

  ### Uniform Inner Dimensions

  `RaggedTensor`s with uniform inner dimensions can be defined
  by using a multidimensional `Tensor` for `values`.

  >>> rt = RaggedTensor.from_row_splits(values=tf.ones([5, 3], tf.int32),
  ...                                   row_splits=[0, 2, 5])
  >>> print(rt.to_list())
  [[[1, 1, 1], [1, 1, 1]],
   [[1, 1, 1], [1, 1, 1], [1, 1, 1]]]
  >>> print(rt.shape)
  (2, None, 3)

  ### Uniform Outer Dimensions

  `RaggedTensor`s with uniform outer dimensions can be defined by using
  one or more `RaggedTensor` with a `uniform_row_length` row-partitioning
  tensor.  For example, a `RaggedTensor` with shape `[2, 2, None]` can be
  constructed with this method from a `RaggedTensor` values with shape
  `[4, None]`:

  >>> values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
  >>> print(values.shape)
  (4, None)
  >>> rt6 = tf.RaggedTensor.from_uniform_row_length(values, 2)
  >>> print(rt6)
  <tf.RaggedTensor [[[1, 2, 3], [4]], [[5, 6], [7, 8, 9, 10]]]>
  >>> print(rt6.shape)
  (2, 2, None)

  Note that `rt6` only contains one ragged dimension (the innermost
  dimension). In contrast, if `from_row_splits` is used to construct a similar
  `RaggedTensor`, then that `RaggedTensor` will have two ragged dimensions:

  >>> rt7 = tf.RaggedTensor.from_row_splits(values, [0, 2, 4])
  >>> print(rt7.shape)
  (2, None, None)

  Uniform and ragged outer dimensions may be interleaved, meaning that a
  tensor with any combination of ragged and uniform dimensions may be created.
  For example, a RaggedTensor `t4` with shape `[3, None, 4, 8, None, 2]` could
  be constructed as follows:

  ```python
  t0 = tf.zeros([1000, 2])                           # Shape:         [1000, 2]
  t1 = RaggedTensor.from_row_lengths(t0, [...])      #           [160, None, 2]
  t2 = RaggedTensor.from_uniform_row_length(t1, 8)   #         [20, 8, None, 2]
  t3 = RaggedTensor.from_uniform_row_length(t2, 4)   #       [5, 4, 8, None, 2]
  t4 = RaggedTensor.from_row_lengths(t3, [...])      # [3, None, 4, 8, None, 2]
  ```

  '''
    def __init__(self, values, row_partition, internal: bool = False) -> None:
        """Creates a `RaggedTensor` with a specified partitioning for `values`.

    This constructor is private -- please use one of the following ops to
    build `RaggedTensor`s:

      * `tf.RaggedTensor.from_row_lengths`
      * `tf.RaggedTensor.from_value_rowids`
      * `tf.RaggedTensor.from_row_splits`
      * `tf.RaggedTensor.from_row_starts`
      * `tf.RaggedTensor.from_row_limits`
      * `tf.RaggedTensor.from_nested_row_splits`
      * `tf.RaggedTensor.from_nested_row_lengths`
      * `tf.RaggedTensor.from_nested_value_rowids`

    Args:
      values: A potentially ragged tensor of any dtype and shape `[nvals, ...]`.
      row_partition: A `RowPartition` object, representing the arrangement of
        the lists at the top level.
      internal: True if the constructor is being called by one of the factory
        methods.  If false, an exception will be raised.

    Raises:
      ValueError: If internal = False. Note that this method is intended only
                 for internal use.
      TypeError: If values is not a `RaggedTensor` or `Tensor`, or
                 row_partition is not a `RowPartition`.
    """
    @classmethod
    def from_value_rowids(cls, values, value_rowids, nrows: Incomplete | None = None, name: Incomplete | None = None, validate: bool = True):
        """Creates a `RaggedTensor` with rows partitioned by `value_rowids`.

    The returned `RaggedTensor` corresponds with the python list defined by:

    ```python
    result = [[values[i] for i in range(len(values)) if value_rowids[i] == row]
              for row in range(nrows)]
    ```

    Args:
      values: A potentially ragged tensor with shape `[nvals, ...]`.
      value_rowids: A 1-D integer tensor with shape `[nvals]`, which corresponds
        one-to-one with `values`, and specifies each value's row index.  Must be
        nonnegative, and must be sorted in ascending order.
      nrows: An integer scalar specifying the number of rows.  This should be
        specified if the `RaggedTensor` may containing empty training rows. Must
        be greater than `value_rowids[-1]` (or zero if `value_rowids` is empty).
        Defaults to `value_rowids[-1] + 1` (or zero if `value_rowids` is empty).
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor`.  `result.rank = values.rank + 1`.
      `result.ragged_rank = values.ragged_rank + 1`.

    Raises:
      ValueError: If `nrows` is incompatible with `value_rowids`.

    #### Example:

    >>> print(tf.RaggedTensor.from_value_rowids(
    ...     values=[3, 1, 4, 1, 5, 9, 2, 6],
    ...     value_rowids=[0, 0, 0, 0, 2, 2, 2, 3],
    ...     nrows=5))
    <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>

    """
    @classmethod
    def from_row_splits(cls, values, row_splits, name: Incomplete | None = None, validate: bool = True):
        """Creates a `RaggedTensor` with rows partitioned by `row_splits`.

    The returned `RaggedTensor` corresponds with the python list defined by:

    ```python
    result = [values[row_splits[i]:row_splits[i + 1]]
              for i in range(len(row_splits) - 1)]
    ```

    Args:
      values: A potentially ragged tensor with shape `[nvals, ...]`.
      row_splits: A 1-D integer tensor with shape `[nrows+1]`.  Must not be
        empty, and must be sorted in ascending order.  `row_splits[0]` must be
        zero and `row_splits[-1]` must be `nvals`.
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor`.  `result.rank = values.rank + 1`.
      `result.ragged_rank = values.ragged_rank + 1`.

    Raises:
      ValueError: If `row_splits` is an empty list.

    #### Example:

    >>> print(tf.RaggedTensor.from_row_splits(
    ...     values=[3, 1, 4, 1, 5, 9, 2, 6],
    ...     row_splits=[0, 4, 4, 7, 8, 8]))
    <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>

    """
    @classmethod
    def from_row_lengths(cls, values, row_lengths, name: Incomplete | None = None, validate: bool = True):
        """Creates a `RaggedTensor` with rows partitioned by `row_lengths`.

    The returned `RaggedTensor` corresponds with the python list defined by:

    ```python
    result = [[values.pop(0) for i in range(length)]
              for length in row_lengths]
    ```

    Args:
      values: A potentially ragged tensor with shape `[nvals, ...]`.
      row_lengths: A 1-D integer tensor with shape `[nrows]`.  Must be
        nonnegative.  `sum(row_lengths)` must be `nvals`.
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor`.  `result.rank = values.rank + 1`.
      `result.ragged_rank = values.ragged_rank + 1`.

    #### Example:

    >>> print(tf.RaggedTensor.from_row_lengths(
    ...     values=[3, 1, 4, 1, 5, 9, 2, 6],
    ...     row_lengths=[4, 0, 3, 1, 0]))
    <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>

    """
    @classmethod
    def from_row_starts(cls, values, row_starts, name: Incomplete | None = None, validate: bool = True):
        """Creates a `RaggedTensor` with rows partitioned by `row_starts`.

    Equivalent to: `from_row_splits(values, concat([row_starts, nvals]))`.

    Args:
      values: A potentially ragged tensor with shape `[nvals, ...]`.
      row_starts: A 1-D integer tensor with shape `[nrows]`.  Must be
        nonnegative and sorted in ascending order.  If `nrows>0`, then
        `row_starts[0]` must be zero.
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor`.  `result.rank = values.rank + 1`.
      `result.ragged_rank = values.ragged_rank + 1`.

    #### Example:

    >>> print(tf.RaggedTensor.from_row_starts(
    ...     values=[3, 1, 4, 1, 5, 9, 2, 6],
    ...     row_starts=[0, 4, 4, 7, 8]))
    <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>

    """
    @classmethod
    def from_row_limits(cls, values, row_limits, name: Incomplete | None = None, validate: bool = True):
        """Creates a `RaggedTensor` with rows partitioned by `row_limits`.

    Equivalent to: `from_row_splits(values, concat([0, row_limits]))`.

    Args:
      values: A potentially ragged tensor with shape `[nvals, ...]`.
      row_limits: A 1-D integer tensor with shape `[nrows]`.  Must be sorted in
        ascending order.  If `nrows>0`, then `row_limits[-1]` must be `nvals`.
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor`.  `result.rank = values.rank + 1`.
      `result.ragged_rank = values.ragged_rank + 1`.

    #### Example:

    >>> print(tf.RaggedTensor.from_row_limits(
    ...     values=[3, 1, 4, 1, 5, 9, 2, 6],
    ...     row_limits=[4, 4, 7, 8, 8]))
    <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>

    """
    @classmethod
    def from_uniform_row_length(cls, values, uniform_row_length, nrows: Incomplete | None = None, validate: bool = True, name: Incomplete | None = None):
        """Creates a `RaggedTensor` with rows partitioned by `uniform_row_length`.

    This method can be used to create `RaggedTensor`s with multiple uniform
    outer dimensions.  For example, a `RaggedTensor` with shape `[2, 2, None]`
    can be constructed with this method from a `RaggedTensor` values with shape
    `[4, None]`:

    >>> values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
    >>> print(values.shape)
    (4, None)
    >>> rt1 = tf.RaggedTensor.from_uniform_row_length(values, 2)
    >>> print(rt1)
    <tf.RaggedTensor [[[1, 2, 3], [4]], [[5, 6], [7, 8, 9, 10]]]>
    >>> print(rt1.shape)
    (2, 2, None)

    Note that `rt1` only contains one ragged dimension (the innermost
    dimension). In contrast, if `from_row_splits` is used to construct a similar
    `RaggedTensor`, then that `RaggedTensor` will have two ragged dimensions:

    >>> rt2 = tf.RaggedTensor.from_row_splits(values, [0, 2, 4])
    >>> print(rt2.shape)
    (2, None, None)

    Args:
      values: A potentially ragged tensor with shape `[nvals, ...]`.
      uniform_row_length: A scalar integer tensor.  Must be nonnegative. The
        size of the outer axis of `values` must be evenly divisible by
        `uniform_row_length`.
      nrows: The number of rows in the constructed RaggedTensor.  If not
        specified, then it defaults to `nvals/uniform_row_length` (or `0` if
        `uniform_row_length==0`).  `nrows` only needs to be specified if
        `uniform_row_length` might be zero.  `uniform_row_length*nrows` must be
        `nvals`.
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.
      name: A name prefix for the RaggedTensor (optional).

    Returns:
      A `RaggedTensor` that corresponds with the python list defined by:

      ```python
      result = [[values.pop(0) for i in range(uniform_row_length)]
                for _ in range(nrows)]
      ```

      `result.rank = values.rank + 1`.
      `result.ragged_rank = values.ragged_rank + 1`.
    """
    @classmethod
    def from_nested_value_rowids(cls, flat_values, nested_value_rowids, nested_nrows: Incomplete | None = None, name: Incomplete | None = None, validate: bool = True):
        """Creates a `RaggedTensor` from a nested list of `value_rowids` tensors.

    Equivalent to:

    ```python
    result = flat_values
    for (rowids, nrows) in reversed(zip(nested_value_rowids, nested_nrows)):
      result = from_value_rowids(result, rowids, nrows)
    ```

    Args:
      flat_values: A potentially ragged tensor.
      nested_value_rowids: A list of 1-D integer tensors.  The `i`th tensor is
        used as the `value_rowids` for the `i`th ragged dimension.
      nested_nrows: A list of integer scalars.  The `i`th scalar is used as the
        `nrows` for the `i`th ragged dimension.
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor` (or `flat_values` if `nested_value_rowids` is empty).

    Raises:
      ValueError: If `len(nested_values_rowids) != len(nested_nrows)`.
    """
    @classmethod
    def from_nested_row_splits(cls, flat_values, nested_row_splits, name: Incomplete | None = None, validate: bool = True):
        """Creates a `RaggedTensor` from a nested list of `row_splits` tensors.

    Equivalent to:

    ```python
    result = flat_values
    for row_splits in reversed(nested_row_splits):
      result = from_row_splits(result, row_splits)
    ```

    Args:
      flat_values: A potentially ragged tensor.
      nested_row_splits: A list of 1-D integer tensors.  The `i`th tensor is
        used as the `row_splits` for the `i`th ragged dimension.
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor` (or `flat_values` if `nested_row_splits` is empty).
    """
    @classmethod
    def from_nested_row_lengths(cls, flat_values, nested_row_lengths, name: Incomplete | None = None, validate: bool = True):
        """Creates a `RaggedTensor` from a nested list of `row_lengths` tensors.

    Equivalent to:

    ```python
    result = flat_values
    for row_lengths in reversed(nested_row_lengths):
      result = from_row_lengths(result, row_lengths)
    ```

    Args:
      flat_values: A potentially ragged tensor.
      nested_row_lengths: A list of 1-D integer tensors.  The `i`th tensor is
        used as the `row_lengths` for the `i`th ragged dimension.
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor` (or `flat_values` if `nested_row_lengths` is empty).
    """
    @property
    def dtype(self):
        """The `DType` of values in this tensor."""
    @property
    def shape(self):
        """The statically known shape of this ragged tensor.

    Returns:
      A `TensorShape` containing the statically known shape of this ragged
      tensor.  Ragged dimensions have a size of `None`.

    Examples:

    >>> tf.ragged.constant([[0], [1, 2]]).shape
    TensorShape([2, None])

    >>> tf.ragged.constant([[[0, 1]], [[1, 2], [3, 4]]], ragged_rank=1).shape
    TensorShape([2, None, 2])

    """
    def get_shape(self):
        """The statically known shape of this ragged tensor.

    Returns:
      A `TensorShape` containing the statically known shape of this ragged
      tensor.  Ragged dimensions have a size of `None`.

    Alias for `shape` property.

    Examples:

    >>> tf.ragged.constant([[0], [1, 2]]).get_shape()
    TensorShape([2, None])

    >>> tf.ragged.constant(
    ...    [[[0, 1]], [[1, 2], [3, 4]]], ragged_rank=1).get_shape()
    TensorShape([2, None, 2])

    """
    @property
    def ragged_rank(self):
        """The number of times the RaggedTensor's flat_values is partitioned.

    Examples:

    >>> values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
    >>> values.ragged_rank
    1

    >>> rt = tf.RaggedTensor.from_uniform_row_length(values, 2)
    >>> rt.ragged_rank
    2

    Returns:
      A Python `int` indicating the number of times the underlying `flat_values`
      Tensor has been partitioned to add a new dimension.
      I.e., `tf.rank(rt) = tf.rank(rt.flat_values) + rt.ragged_rank`.
    """
    @property
    def values(self):
        """The concatenated rows for this ragged tensor.

    `rt.values` is a potentially ragged tensor formed by flattening the two
    outermost dimensions of `rt` into a single dimension.

    `rt.values.shape = [nvals] + rt.shape[2:]` (where `nvals` is the
    number of items in the outer two dimensions of `rt`).

    `rt.ragged_rank = self.ragged_rank - 1`

    Returns:
      A potentially ragged tensor.

    #### Example:

    >>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
    >>> print(rt.values)
    tf.Tensor([3 1 4 1 5 9 2 6], shape=(8,), dtype=int32)

    """
    @property
    def row_splits(self):
        """The row-split indices for this ragged tensor's `values`.

    `rt.row_splits` specifies where the values for each row begin and end in
    `rt.values`.  In particular, the values for row `rt[i]` are stored in
    the slice `rt.values[rt.row_splits[i]:rt.row_splits[i+1]]`.

    Returns:
      A 1-D integer `Tensor` with shape `[self.nrows+1]`.
      The returned tensor is non-empty, and is sorted in ascending order.
      `self.row_splits[0]` is zero, and `self.row_splits[-1]` is equal to
      `self.values.shape[0]`.

    #### Example:

    >>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
    >>> print(rt.row_splits)  # indices of row splits in rt.values
    tf.Tensor([0 4 4 7 8 8], shape=(6,), dtype=int64)

    """
    @property
    def uniform_row_length(self):
        """The length of each row in this ragged tensor, or None if rows are ragged.

    >>> rt1 = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
    >>> print(rt1.uniform_row_length)  # rows are ragged.
    None

    >>> rt2 = tf.RaggedTensor.from_uniform_row_length(
    ...     values=rt1, uniform_row_length=2)
    >>> print(rt2)
    <tf.RaggedTensor [[[1, 2, 3], [4]], [[5, 6], [7, 8, 9, 10]]]>
    >>> print(rt2.uniform_row_length)  # rows are not ragged (all have size 2).
    tf.Tensor(2, shape=(), dtype=int64)

    A RaggedTensor's rows are only considered to be uniform (i.e. non-ragged)
    if it can be determined statically (at graph construction time) that the
    rows all have the same length.

    Returns:
      A scalar integer `Tensor`, specifying the length of every row in this
      ragged tensor (for ragged tensors whose rows are uniform); or `None`
      (for ragged tensors whose rows are ragged).
    """
    @property
    def flat_values(self):
        """The innermost `values` tensor for this ragged tensor.

    Concretely, if `rt.values` is a `Tensor`, then `rt.flat_values` is
    `rt.values`; otherwise, `rt.flat_values` is `rt.values.flat_values`.

    Conceptually, `flat_values` is the tensor formed by flattening the
    outermost dimension and all of the ragged dimensions into a single
    dimension.

    `rt.flat_values.shape = [nvals] + rt.shape[rt.ragged_rank + 1:]`
    (where `nvals` is the number of items in the flattened dimensions).

    Returns:
      A `Tensor`.

    #### Example:

    >>> rt = tf.ragged.constant([[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]])
    >>> print(rt.flat_values)
    tf.Tensor([3 1 4 1 5 9 2 6], shape=(8,), dtype=int32)

    """
    @property
    def nested_row_splits(self):
        """A tuple containing the row_splits for all ragged dimensions.

    `rt.nested_row_splits` is a tuple containing the `row_splits` tensors for
    all ragged dimensions in `rt`, ordered from outermost to innermost.  In
    particular, `rt.nested_row_splits = (rt.row_splits,) + value_splits` where:

        * `value_splits = ()` if `rt.values` is a `Tensor`.
        * `value_splits = rt.values.nested_row_splits` otherwise.

    Returns:
      A `tuple` of 1-D integer `Tensor`s.

    #### Example:

    >>> rt = tf.ragged.constant(
    ...     [[[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]])
    >>> for i, splits in enumerate(rt.nested_row_splits):
    ...   print('Splits for dimension %d: %s' % (i+1, splits.numpy()))
    Splits for dimension 1: [0 3]
    Splits for dimension 2: [0 3 3 5]
    Splits for dimension 3: [0 4 4 7 8 8]

    """
    def value_rowids(self, name: Incomplete | None = None):
        """Returns the row indices for the `values` in this ragged tensor.

    `rt.value_rowids()` corresponds one-to-one with the outermost dimension of
    `rt.values`, and specifies the row containing each value.  In particular,
    the row `rt[row]` consists of the values `rt.values[j]` where
    `rt.value_rowids()[j] == row`.

    Args:
      name: A name prefix for the returned tensor (optional).

    Returns:
      A 1-D integer `Tensor` with shape `self.values.shape[:1]`.
      The returned tensor is nonnegative, and is sorted in ascending order.

    #### Example:

    >>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
    >>> print(rt.values)
    tf.Tensor([3 1 4 1 5 9 2 6], shape=(8,), dtype=int32)
    >>> print(rt.value_rowids())  # corresponds 1:1 with rt.values
    tf.Tensor([0 0 0 0 2 2 2 3], shape=(8,), dtype=int64)

    """
    def nested_value_rowids(self, name: Incomplete | None = None):
        """Returns a tuple containing the value_rowids for all ragged dimensions.

    `rt.nested_value_rowids` is a tuple containing the `value_rowids` tensors
    for
    all ragged dimensions in `rt`, ordered from outermost to innermost.  In
    particular, `rt.nested_value_rowids = (rt.value_rowids(),) + value_ids`
    where:

    * `value_ids = ()` if `rt.values` is a `Tensor`.
    * `value_ids = rt.values.nested_value_rowids` otherwise.

    Args:
      name: A name prefix for the returned tensors (optional).

    Returns:
      A `tuple` of 1-D integer `Tensor`s.

    #### Example:

    >>> rt = tf.ragged.constant(
    ...     [[[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]])
    >>> for i, ids in enumerate(rt.nested_value_rowids()):
    ...   print('row ids for dimension %d: %s' % (i+1, ids.numpy()))
    row ids for dimension 1: [0 0 0]
    row ids for dimension 2: [0 0 0 2 2]
    row ids for dimension 3: [0 0 0 0 2 2 2 3]

    """
    def nrows(self, out_type: Incomplete | None = None, name: Incomplete | None = None):
        """Returns the number of rows in this ragged tensor.

    I.e., the size of the outermost dimension of the tensor.

    Args:
      out_type: `dtype` for the returned tensor.  Defaults to
        `self.row_splits.dtype`.
      name: A name prefix for the returned tensor (optional).

    Returns:
      A scalar `Tensor` with dtype `out_type`.

    #### Example:

    >>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
    >>> print(rt.nrows())  # rt has 5 rows.
    tf.Tensor(5, shape=(), dtype=int64)

    """
    def row_starts(self, name: Incomplete | None = None):
        """Returns the start indices for rows in this ragged tensor.

    These indices specify where the values for each row begin in
    `self.values`.  `rt.row_starts()` is equal to `rt.row_splits[:-1]`.

    Args:
      name: A name prefix for the returned tensor (optional).

    Returns:
      A 1-D integer Tensor with shape `[nrows]`.
      The returned tensor is nonnegative, and is sorted in ascending order.

    #### Example:

    >>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
    >>> print(rt.values)
    tf.Tensor([3 1 4 1 5 9 2 6], shape=(8,), dtype=int32)
    >>> print(rt.row_starts())  # indices of row starts in rt.values
    tf.Tensor([0 4 4 7 8], shape=(5,), dtype=int64)

    """
    def row_limits(self, name: Incomplete | None = None):
        """Returns the limit indices for rows in this ragged tensor.

    These indices specify where the values for each row end in
    `self.values`.  `rt.row_limits(self)` is equal to `rt.row_splits[:-1]`.

    Args:
      name: A name prefix for the returned tensor (optional).

    Returns:
      A 1-D integer Tensor with shape `[nrows]`.
      The returned tensor is nonnegative, and is sorted in ascending order.

    #### Example:

    >>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
    >>> print(rt.values)
    tf.Tensor([3 1 4 1 5 9 2 6], shape=(8,), dtype=int32)
    >>> print(rt.row_limits())  # indices of row limits in rt.values
    tf.Tensor([4 4 7 8 8], shape=(5,), dtype=int64)

    """
    def row_lengths(self, axis: int = 1, name: Incomplete | None = None):
        """Returns the lengths of the rows in this ragged tensor.

    `rt.row_lengths()[i]` indicates the number of values in the
    `i`th row of `rt`.

    Args:
      axis: An integer constant indicating the axis whose row lengths should be
        returned.
      name: A name prefix for the returned tensor (optional).

    Returns:
      A potentially ragged integer Tensor with shape `self.shape[:axis]`.

    Raises:
      ValueError: If `axis` is out of bounds.

    #### Example:

    >>> rt = tf.ragged.constant(
    ...     [[[3, 1, 4], [1]], [], [[5, 9], [2]], [[6]], []])
    >>> print(rt.row_lengths())  # lengths of rows in rt
    tf.Tensor([2 0 2 1 0], shape=(5,), dtype=int64)
    >>> print(rt.row_lengths(axis=2))  # lengths of axis=2 rows.
    <tf.RaggedTensor [[3, 1], [], [2, 1], [1], []]>

    """
    def nested_row_lengths(self, name: Incomplete | None = None):
        """Returns a tuple containing the row_lengths for all ragged dimensions.

    `rt.nested_row_lengths()` is a tuple containing the `row_lengths` tensors
    for all ragged dimensions in `rt`, ordered from outermost to innermost.

    Args:
      name: A name prefix for the returned tensors (optional).

    Returns:
      A `tuple` of 1-D integer `Tensors`.  The length of the tuple is equal to
      `self.ragged_rank`.
    """
    def bounding_shape(self, axis: Incomplete | None = None, name: Incomplete | None = None, out_type: Incomplete | None = None):
        """Returns the tight bounding box shape for this `RaggedTensor`.

    Args:
      axis: An integer scalar or vector indicating which axes to return the
        bounding box for.  If not specified, then the full bounding box is
        returned.
      name: A name prefix for the returned tensor (optional).
      out_type: `dtype` for the returned tensor.  Defaults to
        `self.row_splits.dtype`.

    Returns:
      An integer `Tensor` (`dtype=self.row_splits.dtype`).  If `axis` is not
      specified, then `output` is a vector with
      `output.shape=[self.shape.ndims]`.  If `axis` is a scalar, then the
      `output` is a scalar.  If `axis` is a vector, then `output` is a vector,
      where `output[i]` is the bounding size for dimension `axis[i]`.

    #### Example:

    >>> rt = tf.ragged.constant([[1, 2, 3, 4], [5], [], [6, 7, 8, 9], [10]])
    >>> rt.bounding_shape().numpy()
    array([5, 4])

    """
    def with_values(self, new_values):
        """Returns a copy of `self` with `values` replaced by `new_value`.

    Preserves cached row-partitioning tensors such as `self.cached_nrows` and
    `self.cached_value_rowids` if they have values.

    Args:
      new_values: Potentially ragged tensor to use as the `values` for the
        returned `RaggedTensor`.  Must have `rank > 0`, and must have the same
        number of rows as `self.values`.

    Returns:
      A `RaggedTensor`.  `result.rank = 1 + new_values.rank`.
      `result.ragged_rank = 1 + new_values.ragged_rank`
    """
    def with_flat_values(self, new_values):
        """Returns a copy of `self` with `flat_values` replaced by `new_value`.

    Preserves cached row-partitioning tensors such as `self.cached_nrows` and
    `self.cached_value_rowids` if they have values.

    Args:
      new_values: Potentially ragged tensor that should replace
        `self.flat_values`.  Must have `rank > 0`, and must have the same number
        of rows as `self.flat_values`.

    Returns:
      A `RaggedTensor`.
      `result.rank = self.ragged_rank + new_values.rank`.
      `result.ragged_rank = self.ragged_rank + new_values.ragged_rank`.
    """
    def with_row_splits_dtype(self, dtype):
        """Returns a copy of this RaggedTensor with the given `row_splits` dtype.

    For RaggedTensors with multiple ragged dimensions, the `row_splits` for all
    nested `RaggedTensor` objects are cast to the given dtype.

    Args:
      dtype: The dtype for `row_splits`.  One of `tf.int32` or `tf.int64`.

    Returns:
      A copy of this RaggedTensor, with the `row_splits` cast to the given
      type.
    """
    def merge_dims(self, outer_axis, inner_axis):
        """Merges outer_axis...inner_axis into a single dimension.

    Returns a copy of this RaggedTensor with the specified range of dimensions
    flattened into a single dimension, with elements in row-major order.

    #### Examples:

    >>> rt = tf.ragged.constant([[[1, 2], [3]], [[4, 5, 6]]])
    >>> print(rt.merge_dims(0, 1))
    <tf.RaggedTensor [[1, 2], [3], [4, 5, 6]]>
    >>> print(rt.merge_dims(1, 2))
    <tf.RaggedTensor [[1, 2, 3], [4, 5, 6]]>
    >>> print(rt.merge_dims(0, 2))
    tf.Tensor([1 2 3 4 5 6], shape=(6,), dtype=int32)

    To mimic the behavior of `np.flatten` (which flattens all dimensions), use
    `rt.merge_dims(0, -1).  To mimic the behavior of `tf.layers.Flatten` (which
    flattens all dimensions except the outermost batch dimension), use
    `rt.merge_dims(1, -1)`.

    Args:
      outer_axis: `int`: The first dimension in the range of dimensions to
        merge. May be negative if `self.shape.rank` is statically known.
      inner_axis: `int`: The last dimension in the range of dimensions to merge.
        May be negative if `self.shape.rank` is statically known.

    Returns:
      A copy of this tensor, with the specified dimensions merged into a
      single dimension.  The shape of the returned tensor will be
      `self.shape[:outer_axis] + [N] + self.shape[inner_axis + 1:]`, where `N`
      is the total number of slices in the merged dimensions.
    """
    @classmethod
    def from_tensor(cls, tensor, lengths: Incomplete | None = None, padding: Incomplete | None = None, ragged_rank: int = 1, name: Incomplete | None = None, row_splits_dtype=...):
        """Converts a `tf.Tensor` into a `RaggedTensor`.

    The set of absent/default values may be specified using a vector of lengths
    or a padding value (but not both).  If `lengths` is specified, then the
    output tensor will satisfy `output[row] = tensor[row][:lengths[row]]`. If
    'lengths' is a list of lists or tuple of lists, those lists will be used
    as nested row lengths. If `padding` is specified, then any row *suffix*
    consisting entirely of `padding` will be excluded from the returned
    `RaggedTensor`.  If neither `lengths` nor `padding` is specified, then the
    returned `RaggedTensor` will have no absent/default values.

    Examples:

    >>> dt = tf.constant([[5, 7, 0], [0, 3, 0], [6, 0, 0]])
    >>> tf.RaggedTensor.from_tensor(dt)
    <tf.RaggedTensor [[5, 7, 0], [0, 3, 0], [6, 0, 0]]>
    >>> tf.RaggedTensor.from_tensor(dt, lengths=[1, 0, 3])
    <tf.RaggedTensor [[5], [], [6, 0, 0]]>

    >>> tf.RaggedTensor.from_tensor(dt, padding=0)
    <tf.RaggedTensor [[5, 7], [0, 3], [6]]>

    >>> dt = tf.constant([[[5, 0], [7, 0], [0, 0]],
    ...                   [[0, 0], [3, 0], [0, 0]],
    ...                   [[6, 0], [0, 0], [0, 0]]])
    >>> tf.RaggedTensor.from_tensor(dt, lengths=([2, 0, 3], [1, 1, 2, 0, 1]))
    <tf.RaggedTensor [[[5], [7]], [], [[6, 0], [], [0]]]>

    Args:
      tensor: The `Tensor` to convert.  Must have rank `ragged_rank + 1` or
        higher.
      lengths: An optional set of row lengths, specified using a 1-D integer
        `Tensor` whose length is equal to `tensor.shape[0]` (the number of rows
        in `tensor`).  If specified, then `output[row]` will contain
        `tensor[row][:lengths[row]]`.  Negative lengths are treated as zero. You
          may optionally pass a list or tuple of lengths to this argument, which
          will be used as nested row lengths to construct a ragged tensor with
          multiple ragged dimensions.
      padding: An optional padding value.  If specified, then any row suffix
        consisting entirely of `padding` will be excluded from the returned
        RaggedTensor.  `padding` is a `Tensor` with the same dtype as `tensor`
        and with `shape=tensor.shape[ragged_rank + 1:]`.
      ragged_rank: Integer specifying the ragged rank for the returned
        `RaggedTensor`.  Must be greater than zero.
      name: A name prefix for the returned tensors (optional).
      row_splits_dtype: `dtype` for the returned `RaggedTensor`'s `row_splits`
        tensor.  One of `tf.int32` or `tf.int64`.

    Returns:
      A `RaggedTensor` with the specified `ragged_rank`.  The shape of the
      returned ragged tensor is compatible with the shape of `tensor`.

    Raises:
      ValueError: If both `lengths` and `padding` are specified.
      ValueError: If the rank of `tensor` is 0 or 1.
    """
    def to_tensor(self, default_value: Incomplete | None = None, name: Incomplete | None = None, shape: Incomplete | None = None):
        """Converts this `RaggedTensor` into a `tf.Tensor`.

    If `shape` is specified, then the result is padded and/or truncated to
    the specified shape.

    Examples:

    >>> rt = tf.ragged.constant([[9, 8, 7], [], [6, 5], [4]])
    >>> print(rt.to_tensor())
    tf.Tensor(
        [[9 8 7] [0 0 0] [6 5 0] [4 0 0]], shape=(4, 3), dtype=int32)
    >>> print(rt.to_tensor(shape=[5, 2]))
    tf.Tensor(
        [[9 8] [0 0] [6 5] [4 0] [0 0]], shape=(5, 2), dtype=int32)

    Args:
      default_value: Value to set for indices not specified in `self`. Defaults
        to zero.  `default_value` must be broadcastable to
        `self.shape[self.ragged_rank + 1:]`.
      name: A name prefix for the returned tensors (optional).
      shape: The shape of the resulting dense tensor.  In particular,
        `result.shape[i]` is `shape[i]` (if `shape[i]` is not None), or
        `self.bounding_shape(i)` (otherwise).`shape.rank` must be `None` or
        equal to `self.rank`.

    Returns:
      A `Tensor` with shape `ragged.bounding_shape(self)` and the
      values specified by the non-empty values in `self`.  Empty values are
      assigned `default_value`.
    """
    @classmethod
    def from_sparse(cls, st_input, name: Incomplete | None = None, row_splits_dtype=...):
        """Converts a 2D `tf.sparse.SparseTensor` to a `RaggedTensor`.

    Each row of the `output` `RaggedTensor` will contain the explicit values
    from the same row in `st_input`.  `st_input` must be ragged-right.  If not
    it is not ragged-right, then an error will be generated.

    Example:

    >>> indices = [[0, 0], [0, 1], [0, 2], [1, 0], [3, 0]]
    >>> st = tf.sparse.SparseTensor(indices=indices,
    ...                             values=[1, 2, 3, 4, 5],
    ...                             dense_shape=[4, 3])
    >>> tf.RaggedTensor.from_sparse(st).to_list()
    [[1, 2, 3], [4], [], [5]]

    Currently, only two-dimensional `SparseTensors` are supported.

    Args:
      st_input: The sparse tensor to convert.  Must have rank 2.
      name: A name prefix for the returned tensors (optional).
      row_splits_dtype: `dtype` for the returned `RaggedTensor`'s `row_splits`
        tensor.  One of `tf.int32` or `tf.int64`.

    Returns:
      A `RaggedTensor` with the same values as `st_input`.
      `output.ragged_rank = rank(st_input) - 1`.
      `output.shape = [st_input.dense_shape[0], None]`.
    Raises:
      ValueError: If the number of dimensions in `st_input` is not known
        statically, or is not two.
    """
    def to_sparse(self, name: Incomplete | None = None):
        """Converts this `RaggedTensor` into a `tf.sparse.SparseTensor`.

    Example:

    >>> rt = tf.ragged.constant([[1, 2, 3], [4], [], [5, 6]])
    >>> print(rt.to_sparse())
    SparseTensor(indices=tf.Tensor(
                     [[0 0] [0 1] [0 2] [1 0] [3 0] [3 1]],
                     shape=(6, 2), dtype=int64),
                 values=tf.Tensor([1 2 3 4 5 6], shape=(6,), dtype=int32),
                 dense_shape=tf.Tensor([4 3], shape=(2,), dtype=int64))

    Args:
      name: A name prefix for the returned tensors (optional).

    Returns:
      A SparseTensor with the same values as `self`.
    """
    def numpy(self):
        """Returns a numpy `array` with the values for this `RaggedTensor`.

    Requires that this `RaggedTensor` was constructed in eager execution mode.

    Ragged dimensions are encoded using numpy `arrays` with `dtype=object` and
    `rank=1`, where each element is a single row.

    #### Examples

    In the following example, the value returned by `RaggedTensor.numpy()`
    contains three numpy `array` objects: one for each row (with `rank=1` and
    `dtype=int64`), and one to combine them (with `rank=1` and `dtype=object`):

    >>> tf.ragged.constant([[1, 2, 3], [4, 5]], dtype=tf.int64).numpy()
    array([array([1, 2, 3]), array([4, 5])], dtype=object)

    Uniform dimensions are encoded using multidimensional numpy `array`s.  In
    the following example, the value returned by `RaggedTensor.numpy()` contains
    a single numpy `array` object, with `rank=2` and `dtype=int64`:

    >>> tf.ragged.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.int64).numpy()
    array([[1, 2, 3], [4, 5, 6]])

    Returns:
      A numpy `array`.
    """
    def to_list(self):
        """Returns a nested Python `list` with the values for this `RaggedTensor`.

    Requires that `rt` was constructed in eager execution mode.

    Returns:
      A nested Python `list`.
    """
    __getitem__: Incomplete
    __ge__: Incomplete
    __gt__: Incomplete
    __le__: Incomplete
    __lt__: Incomplete
    __and__: Incomplete
    __rand__: Incomplete
    __invert__: Incomplete
    __ror__: Incomplete
    __or__: Incomplete
    __xor__: Incomplete
    __rxor__: Incomplete
    __abs__: Incomplete
    __add__: Incomplete
    __radd__: Incomplete
    __div__: Incomplete
    __rdiv__: Incomplete
    __floordiv__: Incomplete
    __rfloordiv__: Incomplete
    __mod__: Incomplete
    __rmod__: Incomplete
    __mul__: Incomplete
    __rmul__: Incomplete
    __neg__: Incomplete
    __pow__: Incomplete
    __rpow__: Incomplete
    __sub__: Incomplete
    __rsub__: Incomplete
    __truediv__: Incomplete
    __rtruediv__: Incomplete
    def consumers(self): ...
    __composite_gradient__: Incomplete

def is_ragged(value):
    """Returns true if `value` is a ragged tensor or ragged tensor value."""
def match_row_splits_dtypes(*tensors, **kwargs):
    """Return a copy of `tensors` with row_splits all having the same dtype.

  Args:
    *tensors: A list of Tensors or RaggedTensors.
    **kwargs: If 'return_dtype=True', then return a tuple (dtype, tensors),
      where `dtype` is the data type used by row-splits, and `tensors` is the
      converted list of `Tensors` and `RaggedTensors`.

  Returns:
    The converted list of `Tensors` and `RaggedTensors`.
  """

class RaggedTensorSpec(type_spec.BatchableTypeSpec):
    """Type specification for a `tf.RaggedTensor`."""
    @property
    def dtype(self):
        '''The `tf.dtypes.DType` specified by this type for the RaggedTensor.

    Examples:

    >>> rt = tf.ragged.constant([["a"], ["b", "c"]], dtype=tf.string)
    >>> tf.type_spec_from_value(rt).dtype
    tf.string

    Returns:
      A `tf.dtypes.DType` of the values in the RaggedTensor.
    '''
    @property
    def shape(self):
        """The statically known shape of the RaggedTensor.

    Examples:

    >>> rt = tf.ragged.constant([[0], [1, 2]])
    >>> tf.type_spec_from_value(rt).shape
    TensorShape([2, None])

    >>> rt = tf.ragged.constant([[[0, 1]], [[1, 2], [3, 4]]], ragged_rank=1)
    >>> tf.type_spec_from_value(rt).shape
    TensorShape([2, None, 2])

    Returns:
      A `tf.TensorShape` containing the statically known shape of the
      RaggedTensor. Ragged dimensions have a size of `None`.
    """
    @property
    def ragged_rank(self):
        """The number of times the RaggedTensor's flat_values is partitioned.

    Defaults to `shape.ndims - 1`.

    Examples:

    >>> values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
    >>> tf.type_spec_from_value(values).ragged_rank
    1

    >>> rt1 = tf.RaggedTensor.from_uniform_row_length(values, 2)
    >>> tf.type_spec_from_value(rt1).ragged_rank
    2

    Returns:
      A Python `int` indicating the number of times the underlying `flat_values`
      Tensor has been partitioned to add a new dimension.
      I.e., `tf.rank(rt) = tf.rank(rt.flat_values) + rt.ragged_rank`.
    """
    @property
    def row_splits_dtype(self):
        """The `tf.dtypes.DType` of the RaggedTensor's `row_splits`.

    Examples:

    >>> rt = tf.ragged.constant([[1, 2, 3], [4]], row_splits_dtype=tf.int64)
    >>> tf.type_spec_from_value(rt).row_splits_dtype
    tf.int64

    Returns:
      A `tf.dtypes.DType` for the RaggedTensor's `row_splits` tensor. One
      of `tf.int32` or `tf.int64`.
    """
    @property
    def flat_values_spec(self):
        """The `TypeSpec` of the flat_values of RaggedTensor.

    Returns:
      - The TypeSpec of flat_values.
      - None when the flat_values is a Tensor.
    """
    @property
    def value_type(self): ...
    def __init__(self, shape: Incomplete | None = None, dtype=..., ragged_rank: Incomplete | None = None, row_splits_dtype=..., flat_values_spec: Incomplete | None = None) -> None:
        """Constructs a type specification for a `tf.RaggedTensor`.

    Args:
      shape: The shape of the RaggedTensor, or `None` to allow any shape.  If a
        shape is specified, then all ragged dimensions must have size `None`.
      dtype: `tf.DType` of values in the RaggedTensor.
      ragged_rank: Python integer, the number of times the RaggedTensor's
        flat_values is partitioned.  Defaults to `shape.ndims - 1`.
      row_splits_dtype: `dtype` for the RaggedTensor's `row_splits` tensor. One
        of `tf.int32` or `tf.int64`.
      flat_values_spec: TypeSpec for flat_value of the RaggedTensor. It shall be
        provided when the flat_values is a CompositeTensor rather then Tensor.
        If both `dtype` and `flat_values_spec` and  are provided, `dtype` must
        be the same as `flat_values_spec.dtype`. (experimental)
    """
    def is_compatible_with(self, spec_or_value): ...
    @classmethod
    def from_value(cls, value): ...

def convert_to_tensor_or_ragged_tensor(value, dtype: Incomplete | None = None, preferred_dtype: Incomplete | None = None, name: Incomplete | None = None):
    """Converts value to a `RaggedTensor` or `Tensor`.

  * If `value` is a `RaggedTensor`, then return it as-is.
  * If `value` is a `RaggedTensorValue`, return a corresponding constant
    `RaggedTensor`.
  * Otherwise, use `convert_to_tensor` to convert `value` to a `Tensor`.

  Args:
    value: A `RaggedTensor`, a `RaggedTensorValue`, or an object whose type has
      a registered `Tensor` conversion function.
    dtype: Optional element type for the returned tensor.  If missing the type
      is inferred from the type of `value`.
    preferred_dtype: Optional element type for the returned tensor, used when
      dtype is None.  This argument has no effect if `value` is already a
      tensor, or when conversion is not possible.
    name: Optional name to use if a new `Tensor` is created.

  Returns:
    A `Tensor` or `RaggedTensor`.
  """

class RaggedTensorType:
    """Encoding of a static type for a `RaggedTensor`.

  Use this type to express/declare that an output must have the type of
  `RaggedTensor`.
  """
    def __init__(self, dtype, ragged_rank, row_splits_dtype=...) -> None:
        """Initializes a RaggedTensorType object.

    Args:
      dtype: data type of the `RaggedTensor`'s inner values.
      ragged_rank: ragged_rank of the declared `RaggedTensor`.
      row_splits_dtype: data type for the `RaggedTensor`'s row splits.
        One of: `tf.int32` or `tf.int64`.
    """
    dtype: Incomplete
    ragged_rank: Incomplete
    row_splits_dtype: Incomplete

def merge_dims(value, outer_axis, inner_axis):
    """Merges value[outer_axis...inner_axis] into a single dimension.

  See `RaggedTensor.merge_dims()` for more details.  This helper differs from
  `RaggedTensor.merge_dims()` in that `value` may be a dense or ragged tensor.

  Args:
    value: A `RaggedTensor` or `Tensor`
    outer_axis: `int`
    inner_axis: `int`

  Returns:
    A flattened `RaggedTensor` or `Tensor`.
  """

Ragged: Incomplete
RaggedOrDense: Incomplete
