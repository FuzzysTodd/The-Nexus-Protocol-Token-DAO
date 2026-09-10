from _typeshed import Incomplete
from tensorflow.core.protobuf import struct_pb2 as struct_pb2
from tensorflow.python.framework import composite_tensor as composite_tensor, constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec, type_spec_registry as type_spec_registry
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_ragged_math_ops as gen_ragged_math_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import segment_id_ops as segment_id_ops
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.util.tf_export import tf_export as tf_export

class RowPartition(composite_tensor.CompositeTensor):
    '''Partitioning of a sequence of values into contiguous subsequences ("rows").

  A `RowPartition` describes how a sequence with `nvals` items should be
  divided into `nrows` contiguous subsequences ("rows").  For example, a
  `RowPartition` could be used to partition the vector `[1, 2, 3, 4, 5]` into
  subsequences `[[1, 2], [3], [], [4, 5]]`.  Note that `RowPartition` stores
  information about how values are partitioned, but does not include the
  partitioned values themselves.  `tf.RaggedTensor` is used to pair a `values`
  tensor with one or more `RowPartition`s, providing a complete encoding for a
  ragged tensor (i.e. a tensor with variable-length dimensions).

  `RowPartition`s may be defined using several different schemes:

    * `row_lengths`: an integer vector with shape `[nrows]`, which specifies
      the length of each row.

    * `row_splits`: an integer vector with shape `[nrows+1]`, specifying the
      "split points" between each row.

    * `row_starts`: an integer vector with shape `[nrows]`, which specifies
      the start offset for each row.  Equivalent to `row_splits[:-1]`.

    * `row_limits`: an integer vector with shape `[nrows]`, which specifies
      the stop offset for each row.  Equivalent to `row_splits[1:]`.

    * `value_rowids` is an integer vector with shape `[nvals]`, corresponding
      one-to-one with sequence values, which specifies the row that each value
      belongs to.  If the partition has empty trailing rows, then `nrows`
      must also be specified.

    * `uniform_row_length` is an integer scalar, specifying the length of every
      row.  This scheme may only be used if all rows have the same length.

  For example, the following `RowPartition`s all represent the partitioning of
  8 values into 5 sublists as follows: `[[*, *, *, *], [], [*, *, *], [*], []]`.

  >>> p1 = RowPartition.from_row_lengths([4, 0, 3, 1, 0])
  >>> p2 = RowPartition.from_row_splits([0, 4, 4, 7, 8, 8])
  >>> p3 = RowPartition.from_row_starts([0, 4, 4, 7, 8], nvals=8)
  >>> p4 = RowPartition.from_row_limits([4, 4, 7, 8, 8])
  >>> p5 = RowPartition.from_value_rowids([0, 0, 0, 0, 2, 2, 2, 3], nrows=5)

  For more information about each scheme, see the documentation for the
  its factory method.  For additional examples, see the documentation on
  `tf.RaggedTensor`.

  ### Precomputed Encodings

  `RowPartition` always stores at least one encoding of the partitioning, but
  it can be configured to cache additional encodings as well.  This can
  avoid unnecessary recomputation in eager mode.  (In graph mode, optimizations
  such as common subexpression elimination will typically prevent these
  unnecessary recomputations.)  To check which encodings are precomputed, use
  `RowPartition.has_precomputed_<encoding>`.  To cache an additional
  encoding, use `RowPartition.with_precomputed_<encoding>`.
  '''
    def __init__(self, row_splits, row_lengths: Incomplete | None = None, value_rowids: Incomplete | None = None, nrows: Incomplete | None = None, uniform_row_length: Incomplete | None = None, nvals: Incomplete | None = None, internal: bool = False) -> None:
        """Creates a `RowPartition` from the specified encoding tensor(s).

    This constructor is private -- please use one of the following ops to
    build `RowPartition`s:

      * `RowPartition.from_row_lengths`
      * `RowPartition.from_value_rowids`
      * `RowPartition.from_row_splits`
      * `RowPartition.from_row_starts`
      * `RowPartition.from_row_limits`
      * `RowPartition.from_uniform_row_length`

    If row_splits is has a constant value, then all other arguments should
    have a constant value.

    Args:
      row_splits: A 1-D integer tensor with shape `[nrows+1]`.
      row_lengths: A 1-D integer tensor with shape `[nrows]`
      value_rowids: A 1-D integer tensor with shape `[nvals]`.
      nrows: A 1-D integer scalar tensor.
      uniform_row_length: A scalar tensor.
      nvals: A scalar tensor.
      internal: Private key value, required to ensure that this private
        constructor is *only* called from the factory methods.

    Raises:
      TypeError: If a row partitioning tensor has an inappropriate dtype.
      TypeError: If exactly one row partitioning argument was not specified.
      ValueError: If a row partitioning tensor has an inappropriate shape.
      ValueError: If multiple partitioning arguments are specified.
      ValueError: If nrows is specified but value_rowids is not None.
    """
    @classmethod
    def from_value_rowids(cls, value_rowids, nrows: Incomplete | None = None, validate: bool = True, dtype: Incomplete | None = None, dtype_hint: Incomplete | None = None):
        """Creates a `RowPartition` with rows partitioned by `value_rowids`.

    This `RowPartition` divides a sequence `values` into rows by specifying
    which row each value should be added to:

    ```python
    partitioned_rows = [[] for _ in nrows]
    for (value, rowid) in zip(values, value_rowids):
      partitioned_rows[rowid].append(value)
    ```

    Args:
      value_rowids: A 1-D integer tensor with shape `[nvals]`, which corresponds
        one-to-one with `values`, and specifies each value's row index.  Must be
        nonnegative, and must be sorted in ascending order.
      nrows: An integer scalar specifying the number of rows.  This should be
        specified if the `RowPartition` may containing empty training rows. Must
        be greater than `value_rowids[-1]` (or greater than or equal to zero if
        `value_rowids` is empty). Defaults to `value_rowids[-1] + 1` (or zero if
        `value_rowids` is empty).
      validate: If true, then use assertions to check that the arguments form a
        valid `RowPartition`.
      dtype: Optional dtype for the RowPartition. If missing, the type
        is inferred from the type of `value_rowids`, dtype_hint, or tf.int64.
      dtype_hint: Optional dtype for the RowPartition, used when dtype
        is None. In some cases, a caller may not have a dtype in mind when
        converting to a tensor, so dtype_hint can be used as a soft preference.
        If the conversion to `dtype_hint` is not possible, this argument has no
        effect.

    Returns:
      A `RowPartition`.

    Raises:
      ValueError: If `nrows` is incompatible with `value_rowids`.

    #### Example:

    >>> print(RowPartition.from_value_rowids(
    ...     value_rowids=[0, 0, 0, 0, 2, 2, 2, 3],
    ...     nrows=4))
    tf.RowPartition(row_splits=[0 4 4 7 8])
    """
    @classmethod
    def from_row_splits(cls, row_splits, validate: bool = True, dtype: Incomplete | None = None, dtype_hint: Incomplete | None = None):
        """Creates a `RowPartition` with rows partitioned by `row_splits`.

    This `RowPartition` divides a sequence `values` into rows by indicating
    where each row begins and ends:

    ```python
    partitioned_rows = []
    for i in range(len(row_splits) - 1):
      row_start = row_splits[i]
      row_end = row_splits[i + 1]
      partitioned_rows.append(values[row_start:row_end])
    ```

    Args:
      row_splits: A 1-D integer tensor with shape `[nrows+1]`.  Must not be
        empty, and must be sorted in ascending order.  `row_splits[0]` must be
        zero.
      validate: If true, then use assertions to check that the arguments form a
        valid `RowPartition`.
      dtype: Optional dtype for the RowPartition. If missing, the type
        is inferred from the type of `row_splits`, dtype_hint, or tf.int64.
      dtype_hint: Optional dtype for the RowPartition, used when dtype
        is None. In some cases, a caller may not have a dtype in mind when
        converting to a tensor, so dtype_hint can be used as a soft preference.
        If the conversion to `dtype_hint` is not possible, this argument has no
        effect.

    Returns:
      A `RowPartition`.

    Raises:
      ValueError: If `row_splits` is an empty list.
    """
    @classmethod
    def from_row_lengths(cls, row_lengths, validate: bool = True, dtype: Incomplete | None = None, dtype_hint: Incomplete | None = None):
        """Creates a `RowPartition` with rows partitioned by `row_lengths`.

    This `RowPartition` divides a sequence `values` into rows by indicating
    the length of each row:

    ```python
    partitioned_rows = [[values.pop(0) for _ in range(length)]
                        for length in row_lengths]
    ```

    Args:
      row_lengths: A 1-D integer tensor with shape `[nrows]`.  Must be
        nonnegative.
      validate: If true, then use assertions to check that the arguments form a
        valid `RowPartition`.

      dtype: Optional dtype for the RowPartition. If missing, the type
        is inferred from the type of `row_lengths`, dtype_hint, or tf.int64.
      dtype_hint: Optional dtype for the RowPartition, used when dtype
        is None. In some cases, a caller may not have a dtype in mind when
        converting to a tensor, so dtype_hint can be used as a soft preference.
        If the conversion to `dtype_hint` is not possible, this argument has no
        effect.

    Returns:
      A `RowPartition`.
    """
    @classmethod
    def from_row_starts(cls, row_starts, nvals, validate: bool = True, dtype: Incomplete | None = None, dtype_hint: Incomplete | None = None):
        """Creates a `RowPartition` with rows partitioned by `row_starts`.

    Equivalent to: `from_row_splits(concat([row_starts, nvals], axis=0))`.

    Args:
      row_starts: A 1-D integer tensor with shape `[nrows]`.  Must be
        nonnegative and sorted in ascending order.  If `nrows>0`, then
        `row_starts[0]` must be zero.
      nvals: A scalar tensor indicating the number of values.
      validate: If true, then use assertions to check that the arguments form a
        valid `RowPartition`.
      dtype: Optional dtype for the RowPartition. If missing, the type
        is inferred from the type of `row_starts`, dtype_hint, or tf.int64.
      dtype_hint: Optional dtype for the RowPartition, used when dtype
        is None. In some cases, a caller may not have a dtype in mind when
        converting to a tensor, so dtype_hint can be used as a soft preference.
        If the conversion to `dtype_hint` is not possible, this argument has no
        effect.

    Returns:
      A `RowPartition`.
    """
    @classmethod
    def from_row_limits(cls, row_limits, validate: bool = True, dtype: Incomplete | None = None, dtype_hint: Incomplete | None = None):
        """Creates a `RowPartition` with rows partitioned by `row_limits`.

    Equivalent to: `from_row_splits(values, concat([0, row_limits], axis=0))`.

    Args:
      row_limits: A 1-D integer tensor with shape `[nrows]`.  Must be sorted in
        ascending order.
      validate: If true, then use assertions to check that the arguments form a
        valid `RowPartition`.
      dtype: Optional dtype for the RowPartition. If missing, the type
        is inferred from the type of `row_limits`, dtype_hint, or tf.int64.
      dtype_hint: Optional dtype for the RowPartition, used when dtype
        is None. In some cases, a caller may not have a dtype in mind when
        converting to a tensor, so dtype_hint can be used as a soft preference.
        If the conversion to `dtype_hint` is not possible, this argument has no
        effect.

    Returns:
      A `RowPartition`.
    """
    @classmethod
    def from_uniform_row_length(cls, uniform_row_length, nvals: Incomplete | None = None, nrows: Incomplete | None = None, validate: bool = True, dtype: Incomplete | None = None, dtype_hint: Incomplete | None = None):
        """Creates a `RowPartition` with rows partitioned by `uniform_row_length`.

    This `RowPartition` divides a sequence `values` into rows that all have
    the same length:

    ```python
    partitioned_rows = [[values.pop(0) for _ in range(uniform_row_length)]
             for _ in range(nrows)]
    ```

    Note that either or both of nvals and nrows must be specified.

    Args:
      uniform_row_length: A scalar integer tensor.  Must be nonnegative. The
        size of the outer axis of `values` must be evenly divisible by
        `uniform_row_length`.
      nvals: a non-negative scalar integer tensor for the number of values.
        Must be specified if nrows is not specified. If not specified,
        defaults to uniform_row_length*nrows
      nrows: The number of rows in the constructed RowPartition.  If not
        specified, then it defaults to `nvals/uniform_row_length` (or `0` if
        `uniform_row_length==0`).  `nrows` only needs to be specified if
        `uniform_row_length` might be zero.  `uniform_row_length*nrows` must be
        `nvals`.
      validate: If true, then use assertions to check that the arguments form a
        valid `RowPartition`.
      dtype: Optional dtype for the RowPartition. If missing, the type
        is inferred from the type of `uniform_row_length`, dtype_hint,
        or tf.int64.
      dtype_hint: Optional dtype for the RowPartition, used when dtype
        is None. In some cases, a caller may not have a dtype in mind when
        converting to a tensor, so dtype_hint can be used as a soft preference.
        If the conversion to `dtype_hint` is not possible, this argument has no
        effect.

    Returns:
      A `RowPartition`.
    """
    @property
    def dtype(self):
        """The `DType` used to encode the row partition (either int32 or int64)."""
    def row_splits(self):
        """Returns the row-split indices for this row partition.

    `row_splits` specifies where the values for each row begin and end.
    In particular, the values for row `i` are stored in the slice
    `values[row_splits[i]:row_splits[i+1]]`.

    Returns:
      A 1-D integer `Tensor` with shape `[self.nrows+1]`.
      The returned tensor is non-empty, and is sorted in ascending order.
      `self.row_splits()[0] == 0`.
      `self.row_splits()[-1] == self.nvals()`.
    """
    def value_rowids(self):
        """Returns the row indices for this row partition.

    `value_rowids` specifies the row index fo reach value.  In particular,
    `value_rowids[i]` is the row index for `values[i]`.

    Returns:
      A 1-D integer `Tensor` with shape `[self.nvals()]`.
      The returned tensor is nonnegative, and is sorted in ascending order.
    """
    def nvals(self):
        """Returns the number of values partitioned by this `RowPartition`.

    If the sequence partitioned by this `RowPartition` is a tensor, then
    `nvals` is the size of that tensor's outermost dimension -- i.e.,
    `nvals == values.shape[0]`.

    Returns:
      scalar integer Tensor
    """
    def nrows(self):
        """Returns the number of rows created by this `RowPartition`.

    Returns:
      scalar integer Tensor
    """
    def uniform_row_length(self):
        """Returns the length of each row in this partition, if rows are uniform.

    If all rows in this `RowPartition` have the same length, then this returns
    that length as a scalar integer `Tensor`.  Otherwise, it returns `None`.

    Returns:
      scalar Tensor with `type=self.dtype`, or `None`.
    """
    def row_starts(self):
        """Returns the start indices for rows in this row partition.

    These indices specify where the values for each row begin.
    `partition.row_starts()` is equal to `partition.row_splits()[:-1]`.

    Returns:
      A 1-D integer Tensor with shape `[self.nrows()]`.
      The returned tensor is nonnegative, and is sorted in ascending order.
      `self.row_starts()[0] == 0`.
      `self.row_starts()[-1] <= self.nvals()`.
    """
    def row_limits(self):
        """Returns the limit indices for rows in this row partition.

    These indices specify where the values for each row end.
    `partition.row_limits()` is equal to `partition.row_splits()[:-1]`.

    Returns:
      A 1-D integer Tensor with shape `[self.nrows]`.
      The returned tensor is nonnegative, and is sorted in ascending order.
      `self.row_limits()[-1] == self.nvals()`.
    """
    def row_lengths(self):
        """Returns the lengths of rows in this `RowPartition`.

    Returns:
      A 1-D integer Tensor with shape `[self.nrows]`.
      The returned tensor is nonnegative.
      `tf.reduce_sum(self.row_lengths) == self.nvals()`.
    """
    @property
    def static_nrows(self):
        """The number of rows in this partition, if statically known.

    ```python
    self.row_lengths().shape == [self.static_nrows]
    self.row_starts().shape == [self.static_nrows]
    self.row_limits().shape == [self.static_nrows]
    self.row_splits().shape == [self.static_nrows + 1]
    ```

    Returns:
      The number of rows in this partition as an `int` (if statically known);
      or `None` (otherwise).
    """
    @property
    def static_nvals(self):
        """The number of values in this partition, if statically known.

    ```python
    self.value_rowids().shape == [self.static_vals]
    ```

    Returns:
      The number of values in this partition as an `int` (if statically known);
      or `None` (otherwise).
    """
    @property
    def static_uniform_row_length(self):
        """The number of values in each row of this partition, if statically known.

    Returns:
      The number of values in each row of this partition as an `int` (if
      statically known); or `None` (otherwise).
    """
    def offsets_in_rows(self):
        """Return the offset of each value.

    RowPartition takes an array x and converts it into sublists.
    offsets[i] is the index of x[i] in its sublist.
    Given a shape, such as:
    [*,*,*],[*,*],[],[*,*]
    This returns:
    0,1,2,0,1,0,1

    Returns:
      an offset for every value.
    """
    def is_uniform(self):
        """Returns true if the partition is known to be uniform statically.

    This is based upon the existence of self._uniform_row_length. For example:
    RowPartition.from_row_lengths([3,3,3]).is_uniform()==false
    RowPartition.from_uniform_row_length(5, nvals=20).is_uniform()==true
    RowPartition.from_row_lengths([2,0,2]).is_uniform()==false

    Returns:
      Whether a RowPartition is known to be uniform statically.
    """
    def with_dtype(self, dtype):
        """Returns a copy of this RowPartition with the given encoding dtype.

    Args:
      dtype: The dtype for encoding tensors, such as `row_splits` and `nrows`.
      One of `tf.int32` or `tf.int64`.

    Returns:
      A copy of this RowPartition, with the encoding tensors cast to the given
      type.
    """

class RowPartitionSpec(type_spec.TypeSpec):
    """Type specification for a `tf.RowPartition`."""
    value_type: Incomplete
    def __init__(self, nrows: Incomplete | None = None, nvals: Incomplete | None = None, uniform_row_length: Incomplete | None = None, dtype=...) -> None:
        """Constructs a new RowPartitionSpec.

    Args:
      nrows: The number of rows in the RowPartition, or `None` if unspecified.
      nvals: The number of values partitioned by the RowPartition, or `None` if
        unspecified.
      uniform_row_length: The number of values in each row for this
        RowPartition, or `None` if rows are ragged or row length is unspecified.
      dtype: The data type used to encode the partition.  One of `tf.int64` or
        `tf.int32`.
    """
    def is_compatible_with(self, other): ...
    @property
    def nrows(self): ...
    @property
    def nvals(self): ...
    @property
    def uniform_row_length(self): ...
    @property
    def dtype(self): ...
    @classmethod
    def from_value(cls, value): ...
    def with_dtype(self, dtype): ...
    def __deepcopy__(self, memo): ...
