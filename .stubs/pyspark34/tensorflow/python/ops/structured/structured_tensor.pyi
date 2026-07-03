from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, extension_type as extension_type, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import dynamic_ragged_shape as dynamic_ragged_shape, ragged_factory_ops as ragged_factory_ops, ragged_tensor as ragged_tensor
from tensorflow.python.ops.ragged.row_partition import RowPartition as RowPartition
from tensorflow.python.util import compat as compat, nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Dict, Mapping, Optional, Sequence, Union

class StructuredTensor(extension_type.BatchableExtensionType):
    '''A multidimensional collection of structures with the same schema.

  A **`StructuredTensor`** is a multi-dimensional collection of ***structures***
  with the same ***schema***, where:

  * A ***schema*** is a collection of fields, each of which has a name and type.
  * A ***structure*** maps each field in the schema to a tensor value (which
    could be a nested StructuredTensor).

  As an important special case, a 1D `StructuredTensor` encodes a 2D table,
  where columns are heterogeneous `Tensor`s, and rows are the aligned elements
  in each of those `Tensor`s.

  Internally, StructuredTensors use a "field-major" encoding: for each leaf
  field, there is a single tensor that stores the value of that field for all
  structures in the `StructuredTensor`.

  ### Examples

  >>> # A scalar StructuredTensor describing a single person.
  >>> s1 = tf.experimental.StructuredTensor.from_pyval(
  ...     {"age": 82, "nicknames": ["Bob", "Bobby"]})
  >>> s1.shape
  TensorShape([])
  >>> s1["age"]
  <tf.Tensor: shape=(), dtype=int32, numpy=82>

  >>> # A vector StructuredTensor describing three people.
  >>> s2 = tf.experimental.StructuredTensor.from_pyval([
  ...     {"age": 12, "nicknames": ["Josaphine"]},
  ...     {"age": 82, "nicknames": ["Bob", "Bobby"]},
  ...     {"age": 42, "nicknames": ["Elmo"]}])
  >>> s2.shape
  TensorShape([3])
  >>> s2[0]["age"]
  <tf.Tensor: shape=(), dtype=int32, numpy=12>


  ### Field Paths

  A *field path* is a tuple of field names, specifying the path to a nested
  field.
  '''
    FieldName = Union[str, Sequence[str]]
    def __init__(self, fields: Mapping[str, _FieldValue], ragged_shape: dynamic_ragged_shape.DynamicRaggedShape) -> None: ...
    @classmethod
    def from_shape(cls, ragged_shape: dynamic_ragged_shape.DynamicRaggedShape) -> StructuredTensor:
        """Creates a `StructuredTensor` with no fields and ragged_shape.

    Args:
      ragged_shape: the shape of the structured tensor.

    Returns:
      a StructuredTensor with no fields and ragged_shape.
    """
    @classmethod
    def from_fields(cls, fields, shape=(), nrows: Incomplete | None = None, row_partitions: Incomplete | None = None, validate: bool = False):
        '''Creates a `StructuredTensor` from a dictionary of fields.

    Args:
      fields: A dictionary mapping from string to `Tensor`, `RaggedTensor`, or
        `StructuredTensor`, providing the values for individual fields in each
        structure.  If `shape.rank > 0`, then every tensor in `fields` must have
        the same shape in the first `shape.rank` dimensions; and that shape must
        be compatible with `shape`; and `result[i1...iN][key] =
        fields[key][i1...iN]` (where `N==shape.rank`).
      shape: A `TensorShape`: static information about the shape of the
        `StructuredTensor`.  Must have a known `rank`.  Defaults to scalar shape
        (i.e. `rank=0`).
      nrows: scalar integer tensor containing the number of rows in this
        `StructuredTensor`.  Should only be specified if `shape.rank > 0`.
        Default value is inferred from the `fields` values.  If `fields` is
        empty, then this must be specified.
      row_partitions: A list of `RowPartition`s describing the (possibly ragged)
        shape of this `StructuredTensor`.  Should only be specified if
        `shape.rank > 1`.  Default value is inferred from the `fields` values.
        If `fields` is empty, then this must be specified.
      validate: If true, then add runtime validation ops that check that the
        field values all have compatible shapes in the outer `shape.rank`
        dimensions.

    Returns:
      A `StructuredTensor`.

    Examples:

      >>> tf.experimental.StructuredTensor.from_fields({\'x\': 1, \'y\': [1, 2, 3]})
      <StructuredTensor(
        fields={
          "x": tf.Tensor(1, shape=(), dtype=int32),
          "y": tf.Tensor([1 2 3], shape=(3,), dtype=int32)},
        shape=())>

      >>> tf.experimental.StructuredTensor.from_fields(
      ...     {\'foo\': [1, 2], \'bar\': [3, 4]}, shape=[2])
      <StructuredTensor(
        fields={
          "bar": tf.Tensor([3 4], shape=(2,), dtype=int32),
          "foo": tf.Tensor([1 2], shape=(2,), dtype=int32)},
        shape=(2,))>
    '''
    @classmethod
    def from_fields_and_rank(cls, fields: Mapping[str, _FieldValue], rank: int, validate: bool = False, dtype: Optional[dtypes.DType] = None) -> StructuredTensor:
        '''Creates a `StructuredTensor` from a nonempty dictionary of fields.

    Note that if the shape dtype is not specified, the shape dtype will be
    inferred from any fields that have a shape dtype. If fields differ, then
    int64 will be preferred to int32, because coercing from int32 to int64 is
    safer than coercing from int64 to int32.

    If there are no ragged fields, then it will be int64 by default, but this
    will be changed to int32 in the future.

    Args:
      fields: A dictionary mapping from string to `Tensor`, `RaggedTensor`, or
        `StructuredTensor`, providing the values for individual fields in each
        structure.  If `rank > 0`, then every tensor in `fields` must have the
        same shape in the first `rank` dimensions. Cannot be empty.
      rank: The rank of the resulting structured tensor.
      validate: If true, then add runtime validation ops that check that the
        field values all have compatible shapes in the outer `rank` dimensions.
      dtype: If specified, then forces dtype of the shape to be this.

    Returns:
      A `StructuredTensor`.
    Examples:
      >>> tf.experimental.StructuredTensor.from_fields_and_rank(
      ...     {\'x\': 1, \'y\': [1, 2, 3]}, 0)
      <StructuredTensor(
        fields={
          "x": tf.Tensor(1, shape=(), dtype=int32),
          "y": tf.Tensor([1 2 3], shape=(3,), dtype=int32)},
        shape=())>
      >>> StructuredTensor.from_fields_and_rank({\'foo\': [1, 2], \'bar\': [3, 4]},
      ...                              1)
      <StructuredTensor(
        fields={
          "bar": tf.Tensor([3 4], shape=(2,), dtype=int32),
          "foo": tf.Tensor([1 2], shape=(2,), dtype=int32)},
        shape=(2,))>
    '''
    def with_updates(self, updates: Dict[FieldName, Union[_FieldValue, _FieldFn, None]], validate: bool = False) -> StructuredTensor:
        '''Creates a new `StructuredTensor` with the updated fields.

    If this `StructuredTensor` is a scalar, and `k` is the `FieldName` being
    updated and `v` the new value, then:

    ```
    result[k] = v              # If (k, v) is in updates and v is a FieldValue
    result[k] = f(self[k])     # If (k, f) is in updates and f is a FieldFn
    result[k] = self[k]        # If k is in self.field_names but not in updates
    ```

    If this `StructuredTensor` has rank `N` and shape `[D1...DN]`, then each
    FieldValue `v` in `updates` must have shape `[D1...DN, ...]`, that is,
    prefixed with the same shape as the `StructuredTensor`. Then the resulting
    `StructuredTensor` will have:

    ```
    result[i1...iN][k] = v[i1...iN]                        # (k, v) in updates
    result[i1...iN][k] = f(self.field_value(k))[i1...iN]   # (k, f) in updates
    result[i1...iN][k] = self[i1...iN][k]                  # k not in updates
    ```

    Note that `result.shape` is always equal to `self.shape` (but the shapes
    of nested StructuredTensors may be changed if they are updated with new
    values).

    Args:
      updates: A dictionary mapping `FieldName` to either a `FieldValue` to be
        used to update, or a `FieldFn` that will transform the value for the
        given `FieldName`. `FieldName` can be a string for a direct field, or a
        sequence of strings to refer to a nested sub-field. `FieldFn` is a
        function that takes a `FieldValue` as input and should return a
        `FieldValue`. All other fields are copied over to the new
        `StructuredTensor`. New `FieldName` can be given (to add new fields),
        but only to existing `StructuredTensor`, it won\'t automatically create
        new nested structures -- but one can create a whole `StructureTensor`
        sub-structure and set that into an existing structure. If the new value
        is set to `None`, it is removed.
      validate: If true, then add runtime validation ops that check that the
        field values all have compatible shapes in the outer `shape.rank`
        dimensions.

    Returns:
      A `StructuredTensor`.

    Raises:
      `ValueError`: If the any of the `FieldName` keys points to non-existent
        sub-structures, if parent and child nodes are updated, if shapes
        change, if a delete update is given for a non-existent field, or if a
        `FieldFn` transforming function is given for a `FieldName` that doesn\'t
        yet exist.

    Examples:

    >>> shoes_us = tf.experimental.StructuredTensor.from_pyval([
    ...    {"age": 12, "nicknames": ["Josaphine"],
    ...       "shoes": {"sizes": [8.0, 7.5, 7.5]}},
    ...    {"age": 82, "nicknames": ["Bob", "Bobby"],
    ...        "shoes": {"sizes": [11.0, 11.5, 12.0]}},
    ...    {"age": 42, "nicknames": ["Elmo"],
    ...        "shoes": {"sizes": [9.0, 9.5, 10.0]}}])
    >>> def us_to_europe(t):
    ...   return tf.round(t * 2.54 + 17.0)  # Rough approximation.
    >>> shoe_sizes_key = ("shoes", "sizes")
    >>> shoes_eu = shoes_us.with_updates({shoe_sizes_key: us_to_europe})
    >>> shoes_eu.field_value(shoe_sizes_key)
    <tf.RaggedTensor [[37.0, 36.0, 36.0], [45.0, 46.0, 47.0],
    [40.0, 41.0, 42.0]]>
    '''
    def promote(self, source_path, new_name):
        """Promotes a field, merging dimensions between grandparent and parent.

    >>> d = [
    ...  {'docs': [{'tokens':[1, 2]}, {'tokens':[3]}]},
    ...  {'docs': [{'tokens':[7]}]}]
    >>> st = tf.experimental.StructuredTensor.from_pyval(d)
    >>> st2 =st.promote(('docs','tokens'), 'docs_tokens')
    >>> st2[0]['docs_tokens']
    <tf.Tensor: shape=(3,), dtype=int32, numpy=array([1, 2, 3], dtype=int32)>
    >>> st2[1]['docs_tokens']
    <tf.Tensor: shape=(1,), dtype=int32, numpy=array([7], dtype=int32)>

    Args:
      source_path: the path of the field or substructure to promote; must have
        length at least 2.
      new_name: the name of the new field (must be a string).

    Returns:
      a modified structured tensor with the new field as a child of the
      grandparent of the source_path.

    Raises:
      ValueError: if source_path is not a list or a tuple or has a length
        less than two, or new_name is not a string, or the rank
        of source_path is unknown and it is needed.
    """
    @property
    def rank(self):
        """The rank of this StructuredTensor.  Guaranteed not to be `None`."""
    @property
    def shape(self):
        """The static shape of this StructuredTensor.

    The returned `TensorShape` is guaranteed to have a known rank, but the
    individual dimension sizes may be unknown.

    Returns:
      `tf.TensorShape`
    """
    @property
    def row_partitions(self):
        """A tuple of `RowPartition`s defining the shape of this `StructuredTensor`.

    When `self.rank <= 1`, this tuple will be empty.

    When `self.rank > 1`, these `RowPartitions` define the shape of the
    `StructuredTensor` by describing how a flat (1D) list of structures can be
    repeatedly partitioned to form a higher-dimensional object.  In particular,
    the flat list is first partitioned into sublists using `row_partitions[-1]`,
    and then those sublists are further partitioned using `row_partitions[-2]`,
    etc.  The following examples show the row partitions used to describe
    several different `StructuredTensor`, each of which contains 8 copies of
    the same structure (`x`):

    >>> x = {'a': 1, 'b': ['foo', 'bar', 'baz']}       # shape = [] (scalar)

    >>> s1 = [[x, x, x, x], [x, x, x, x]]              # shape = [2, 4]
    >>> tf.experimental.StructuredTensor.from_pyval(s1).row_partitions
    (tf.RowPartition(row_splits=[0 4 8]),)

    >>> s2 = [[x, x], [x, x], [x, x], [x, x]]          # shape = [4, 2]
    >>> tf.experimental.StructuredTensor.from_pyval(s2).row_partitions
    (tf.RowPartition(row_splits=[0 2 4 6 8]),)

    >>> s3 = [[x, x, x], [], [x, x, x, x], [x]]        # shape = [2, None]
    >>> tf.experimental.StructuredTensor.from_pyval(s3).row_partitions
    (tf.RowPartition(row_splits=[0 3 3 7 8]),)

    >>> s4 = [[[x, x], [x, x]], [[x, x], [x, x]]]      # shape = [2, 2, 2]
    >>> tf.experimental.StructuredTensor.from_pyval(s4).row_partitions
    (tf.RowPartition(row_splits=[0 2 4]),
     tf.RowPartition(row_splits=[0 2 4 6 8]))


    >>> s5 = [[[x, x], [x]], [[x, x]], [[x, x], [x]]]  # shape = [3, None, None]
    >>> tf.experimental.StructuredTensor.from_pyval(s5).row_partitions
    (tf.RowPartition(row_splits=[0 2 3 5]),
     tf.RowPartition(row_splits=[0 2 3 5 7 8]))

    Note that shapes for nested fields (such as `x['b']` in the above example)
    are not considered part of the shape of a `StructuredTensor`, and are not
    included in `row_partitions`.

    If this `StructuredTensor` has a ragged shape (i.e., if any of the
    `row_partitions` is not uniform in size), then all fields will be encoded
    as either `RaggedTensor`s or `StructuredTensor`s with these `RowPartition`s
    used to define their outermost `self.rank` dimensions.

    Returns:
      A `tuple` of `RowPartition` objects with length `self.rank - 1`
      (or `0` if `self.rank < 2`)

    """
    def nrows(self):
        """The number of rows in this StructuredTensor (if rank>0).

    This means the length of the outer-most dimension of the StructuredTensor.

    Notice that if `self.rank > 1`, then this equals the number of rows
    of the first row partition. That is,
    `self.nrows() == self.row_partitions[0].nrows()`.

    Otherwise `self.nrows()` will be the first dimension of the field values.

    Returns:
      A scalar integer `Tensor` (or `None` if `self.rank == 0`).
    """
    def with_shape_dtype(self, dtype: dtypes.DType) -> StructuredTensor: ...
    def field_names(self):
        """Returns the string field names for this `StructuredTensor`."""
    def field_value(self, field_name):
        """Returns the tensor value for the specified field or path.

    If `field_name` is a `string`, then it names a field directly owned by this
    `StructuredTensor`.  If this `StructuredTensor` has shape `[D1...DN]`, then
    the returned tensor will have shape `[D1...DN, V1...VM]`, where the slice
    `result[d1...dN]` contains the field value for the structure at
    `self[d1...dN]`.

    If `field_name` is a `tuple` of `string`, then it specifies a path to a
    field owned by nested `StructuredTensor`.  In particular,
    `struct.field_value((f1, f2, ..., fN))` is equivalent to
    `struct.field_value(f1).field_value(f2)....field_value(fN)`

    Args:
      field_name: `string` or `tuple` of `string`: The field whose values should
        be returned.

    Returns:
      `Tensor`, `StructuredTensor`, or `RaggedTensor`.

    Raises:
      KeyError: If the given field_name is not found.
    """
    def __getitem__(self, key):
        """Returns the specified piece of this StructuredTensor.

    * If `struct_tensor` is scalar (i.e., a single structure), then
      `struct_tensor[f]` returns the value of field `f` (where `f` must be a
      string).

    * If `struct_tensor` is non-scalar (i.e., a vector or higher-dimensional
      tensor of structures), `struct_tensor[i]` selects an element or slice of
      the tensor using standard Python semantics (e.g., negative values index
      from the end).  `i` may have any of the following types:

      * `int` constant
      * `string` constant
      * scalar integer `Tensor`
      * `slice` containing integer constants and/or scalar integer
        `Tensor`s

    #### Multidimensional indexing

    `StructuredTensor` supports multidimensional indexing.  I.e., `key` may be a
    `tuple` of values, indexing or slicing multiple dimensions at once.  For
    example, if `people` is a vector of structures, each of which has a vector-
    valued `names` field, then `people[3, 'names', 0]` is equivalent to
    `people[3]['names'][0]`; and `people[:, 'names', :]` will return a (possibly
    ragged) matrix of names, with shape `[num_people, num_names_per_person]`.

    Args:
      key: Indicates which piece of the StructuredTensor to return.

    Returns:
      A `Tensor`, `StructuredTensor`, or `RaggedTensor`.
    """
    def to_pyval(self):
        """Returns this StructuredTensor as a nested Python dict or list of dicts.

    Converts this `StructuredTensor` to a nested python value:

    * `StructTensors` with `rank=0` are converted into a dictionary, with an
      entry for each field.  Field names are used as keys and field values are
      converted to python values.  In particular:

      * Scalar Tensor fields are converted to simple values (such as
        `int` or `float` or `string`)
      * Non-scalar Tensor fields and RaggedTensor fields are converted to
        nested lists of simple values.
      * StructuredTensor fields are converted recursively using `to_pyval`.

    * `StructTensors` with `rank>0` are converted to nested python `list`s,
      containing one dictionary for each structure (where each structure's
      dictionary is defined as described above).

    Requires that all fields are Eager tensors.

    >>> tf.experimental.StructuredTensor.from_fields(
    ...     {'a': [1, 2, 3]}, [3]).to_pyval()
    [{'a': 1}, {'a': 2}, {'a': 3}]

    Note that `StructuredTensor.from_pyval(pyval).to_pyval() == pyval`.

    Returns:
      A nested Python dict or list of dicts.
    """
    @classmethod
    def from_pyval(cls, pyval, typespec: Incomplete | None = None):
        '''Constructs a StructuredTensor from a nested Python structure.

    >>> tf.experimental.StructuredTensor.from_pyval(
    ...     {\'a\': [1, 2, 3], \'b\': [[4, 5], [6, 7]]})
    <StructuredTensor(
        fields={
          "a": tf.Tensor([1 2 3], shape=(3,), dtype=int32),
          "b": <tf.RaggedTensor [[4, 5], [6, 7]]>},
        shape=())>

    Note that `StructuredTensor.from_pyval(pyval).to_pyval() == pyval`.

    Args:
      pyval: The nested Python structure that should be used to create the new
        `StructuredTensor`.
      typespec: A `StructuredTensor.Spec` specifying the expected type for each
        field. If not specified, then all nested dictionaries are turned into
        StructuredTensors, and all nested lists are turned into Tensors (if
        rank<2) or RaggedTensors (if rank>=2).

    Returns:
      A `StructuredTensor`.
    '''
    def partition_outer_dimension(self, row_partition):
        '''Partitions the outer dimension of this StructuredTensor.

    Returns a new `StructuredTensor` with the same values as `self`, where
    the outer dimension is partitioned into two (possibly ragged) dimensions.
    Requires that this StructuredTensor have an outer dimension (i.e.,
    `self.shape.rank > 0`).

    >>> st = tf.experimental.StructuredTensor.from_pyval(
    ...     [{\'foo\': 12}, {\'foo\': 33}, {\'foo\': 99}])
    >>> partition = RowPartition.from_row_lengths([2, 0, 1])
    >>> st.partition_outer_dimension(partition)
    <StructuredTensor(
      fields={
        "foo": <tf.RaggedTensor [[12, 33], [], [99]]>},
      shape=(3, None))>

    Args:
      row_partition: A `RowPartition`.

    Returns:
      A `StructuredTensor` with rank `values.rank + 1`.
    '''
    def merge_dims(self, outer_axis, inner_axis):
        '''Merges outer_axis...inner_axis into a single dimension.

    Returns a copy of this RaggedTensor with the specified range of dimensions
    flattened into a single dimension, with elements in row-major order.

    >>> st = tf.experimental.StructuredTensor.from_pyval(
    ...     [[{\'foo\': 12}, {\'foo\': 33}], [], [{\'foo\': 99}]])
    >>> st.merge_dims(0, 1)
    <StructuredTensor(
      fields={
        "foo": tf.Tensor([12 33 99], shape=(3,), dtype=int32)},
      shape=(3,))>

    Args:
      outer_axis: `int`: The first dimension in the range of dimensions to
        merge. May be negative (to index from the last dimension).
      inner_axis: `int`: The last dimension in the range of dimensions to merge.
        May be negative (to index from the last dimension).

    Returns:
      A copy of this tensor, with the specified dimensions merged into a
      single dimension.  The shape of the returned tensor will be
      `self.shape[:outer_axis] + [N] + self.shape[inner_axis + 1:]`, where `N`
      is the total number of slices in the merged dimensions.
    '''
    class Spec:
        """A spec for StructuredTensor."""
        def __validate__(self) -> None: ...
        @property
        def shape(self) -> tensor_shape.TensorShape: ...
        @property
        def rank(self): ...

def StructuredTensorSpec(shape, field_specs):
    """A placeholder for the old StructuredTensorSpec."""
