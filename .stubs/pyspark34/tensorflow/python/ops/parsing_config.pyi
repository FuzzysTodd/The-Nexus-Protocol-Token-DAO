from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops, sparse_ops as sparse_ops
from tensorflow.python.ops.ragged import ragged_math_ops as ragged_math_ops, ragged_tensor as ragged_tensor
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class VarLenFeature(NamedTuple('VarLenFeature', [('dtype', Incomplete)])):
    """Configuration for parsing a variable-length input feature.

  Fields:
    dtype: Data type of input.
  """

class RaggedFeature(NamedTuple('RaggedFeature', [('dtype', Incomplete), ('value_key', Incomplete), ('partitions', Incomplete), ('row_splits_dtype', Incomplete), ('validate', Incomplete)])):
    '''Configuration for passing a RaggedTensor input feature.

  `value_key` specifies the feature key for a variable-length list of values;
  and `partitions` specifies zero or more feature keys for partitioning those
  values into higher dimensions.  Each element of `partitions` must be one of
  the following:

    * `tf.io.RaggedFeature.RowSplits(key: string)`
    * `tf.io.RaggedFeature.RowLengths(key: string)`
    * `tf.io.RaggedFeature.RowStarts(key: string)`
    * `tf.io.RaggedFeature.RowLimits(key: string)`
    * `tf.io.RaggedFeature.ValueRowIds(key: string)`
    * `tf.io.RaggedFeature.UniformRowLength(length: int)`.

  Where `key` is a feature key whose values are used to partition the values.
  Partitions are listed from outermost to innermost.

  * If `len(partitions) == 0` (the default), then:

    * A feature from a single `tf.Example` is parsed into a 1D `tf.Tensor`.
    * A feature from a batch of `tf.Example`s is parsed into a 2D
      `tf.RaggedTensor`, where the outer dimension is the batch dimension, and
      the inner (ragged) dimension is the feature length in each example.

  * If `len(partitions) == 1`, then:

    * A feature from a single `tf.Example` is parsed into a 2D
      `tf.RaggedTensor`, where the values taken from the `value_key` are
      separated into rows using the partition key.
    * A feature from a batch of `tf.Example`s is parsed into a 3D
      `tf.RaggedTensor`, where the outer dimension is the batch dimension,
      the two inner dimensions are formed by separating the `value_key` values
      from each example into rows using that example\'s partition key.

  * If `len(partitions) > 1`, then:

    * A feature from a single `tf.Example` is parsed into a `tf.RaggedTensor`
      whose rank is `len(partitions)+1`, and whose ragged_rank is
      `len(partitions)`.

    * A feature from a batch of `tf.Example`s is parsed into a `tf.RaggedTensor`
      whose rank is `len(partitions)+2` and whose ragged_rank is
      `len(partitions)+1`, where the outer dimension is the batch dimension.

  There is one exception: if the final (i.e., innermost) element(s) of
  `partitions` are `UniformRowLength`s, then the values are simply reshaped (as
  a higher-dimensional `tf.Tensor`), rather than being wrapped in a
  `tf.RaggedTensor`.

  #### Examples

  >>> import google.protobuf.text_format as pbtext
  >>> example_batch = [
  ...   pbtext.Merge(r\'\'\'
  ...     features {
  ...       feature {key: "v" value {int64_list {value: [3, 1, 4, 1, 5, 9]}}}
  ...       feature {key: "s1" value {int64_list {value: [0, 2, 3, 3, 6]}}}
  ...       feature {key: "s2" value {int64_list {value: [0, 2, 3, 4]}}}
  ...     }\'\'\', tf.train.Example()).SerializeToString(),
  ...   pbtext.Merge(r\'\'\'
  ...     features {
  ...       feature {key: "v" value {int64_list {value: [2, 7, 1, 8, 2, 8, 1]}}}
  ...       feature {key: "s1" value {int64_list {value: [0, 3, 4, 5, 7]}}}
  ...       feature {key: "s2" value {int64_list {value: [0, 1, 1, 4]}}}
  ...     }\'\'\', tf.train.Example()).SerializeToString()]

  >>> features = {
  ...     # Zero partitions: returns 1D tf.Tensor for each Example.
  ...     \'f1\': tf.io.RaggedFeature(value_key="v", dtype=tf.int64),
  ...     # One partition: returns 2D tf.RaggedTensor for each Example.
  ...     \'f2\': tf.io.RaggedFeature(value_key="v", dtype=tf.int64, partitions=[
  ...         tf.io.RaggedFeature.RowSplits("s1")]),
  ...     # Two partitions: returns 3D tf.RaggedTensor for each Example.
  ...     \'f3\': tf.io.RaggedFeature(value_key="v", dtype=tf.int64, partitions=[
  ...         tf.io.RaggedFeature.RowSplits("s2"),
  ...         tf.io.RaggedFeature.RowSplits("s1")])
  ... }

  >>> feature_dict = tf.io.parse_single_example(example_batch[0], features)
  >>> for (name, val) in sorted(feature_dict.items()):
  ...   print(\'%s: %s\' % (name, val))
  f1: tf.Tensor([3 1 4 1 5 9], shape=(6,), dtype=int64)
  f2: <tf.RaggedTensor [[3, 1], [4], [], [1, 5, 9]]>
  f3: <tf.RaggedTensor [[[3, 1], [4]], [[]], [[1, 5, 9]]]>

  >>> feature_dict = tf.io.parse_example(example_batch, features)
  >>> for (name, val) in sorted(feature_dict.items()):
  ...   print(\'%s: %s\' % (name, val))
  f1: <tf.RaggedTensor [[3, 1, 4, 1, 5, 9],
                        [2, 7, 1, 8, 2, 8, 1]]>
  f2: <tf.RaggedTensor [[[3, 1], [4], [], [1, 5, 9]],
                        [[2, 7, 1], [8], [2], [8, 1]]]>
  f3: <tf.RaggedTensor [[[[3, 1], [4]], [[]], [[1, 5, 9]]],
                        [[[2, 7, 1]], [], [[8], [2], [8, 1]]]]>

  Fields:
    dtype: Data type of the `RaggedTensor`.  Must be one of:
      `tf.dtypes.int64`, `tf.dtypes.float32`, `tf.dtypes.string`.
    value_key: (Optional.) Key for a `Feature` in the input `Example`, whose
      parsed `Tensor` will be the resulting `RaggedTensor.flat_values`.  If
      not specified, then it defaults to the key for this `RaggedFeature`.
    partitions: (Optional.) A list of objects specifying the row-partitioning
      tensors (from outermost to innermost).  Each entry in this list must be
      one of:
        * `tf.io.RaggedFeature.RowSplits(key: string)`
        * `tf.io.RaggedFeature.RowLengths(key: string)`
        * `tf.io.RaggedFeature.RowStarts(key: string)`
        * `tf.io.RaggedFeature.RowLimits(key: string)`
        * `tf.io.RaggedFeature.ValueRowIds(key: string)`
        * `tf.io.RaggedFeature.UniformRowLength(length: int)`.
      Where `key` is a key for a `Feature` in the input `Example`, whose parsed
      `Tensor` will be the resulting row-partitioning tensor.
    row_splits_dtype: (Optional.) Data type for the row-partitioning tensor(s).
      One of `int32` or `int64`.  Defaults to `int32`.
    validate: (Optional.) Boolean indicating whether or not to validate that
      the input values form a valid RaggedTensor.  Defaults to `False`.
  '''

    class RowSplits(NamedTuple):
        key: Incomplete

    class RowLengths(NamedTuple):
        key: Incomplete

    class RowStarts(NamedTuple):
        key: Incomplete

    class RowLimits(NamedTuple):
        key: Incomplete

    class ValueRowIds(NamedTuple):
        key: Incomplete

    class UniformRowLength(NamedTuple):
        length: Incomplete
    def __new__(cls, dtype, value_key: Incomplete | None = None, partitions=(), row_splits_dtype=..., validate: bool = False): ...

class SparseFeature(NamedTuple('SparseFeature', [('index_key', Incomplete), ('value_key', Incomplete), ('dtype', Incomplete), ('size', Incomplete), ('already_sorted', Incomplete)])):
    '''Configuration for parsing a sparse input feature from an `Example`.

  Note, preferably use `VarLenFeature` (possibly in combination with a
  `SequenceExample`) in order to parse out `SparseTensor`s instead of
  `SparseFeature` due to its simplicity.

  Closely mimicking the `SparseTensor` that will be obtained by parsing an
  `Example` with a `SparseFeature` config, a `SparseFeature` contains a

  * `value_key`: The name of key for a `Feature` in the `Example` whose parsed
    `Tensor` will be the resulting `SparseTensor.values`.

  * `index_key`: A list of names - one for each dimension in the resulting
    `SparseTensor` whose `indices[i][dim]` indicating the position of
    the `i`-th value in the `dim` dimension will be equal to the `i`-th value in
    the Feature with key named `index_key[dim]` in the `Example`.

  * `size`: A list of ints for the resulting `SparseTensor.dense_shape`.

  For example, we can represent the following 2D `SparseTensor`

  ```python
  SparseTensor(indices=[[3, 1], [20, 0]],
               values=[0.5, -1.0]
               dense_shape=[100, 3])
  ```

  with an `Example` input proto

  ```python
  features {
    feature { key: "val" value { float_list { value: [ 0.5, -1.0 ] } } }
    feature { key: "ix0" value { int64_list { value: [ 3, 20 ] } } }
    feature { key: "ix1" value { int64_list { value: [ 1, 0 ] } } }
  }
  ```

  and `SparseFeature` config with 2 `index_key`s

  ```python
  SparseFeature(index_key=["ix0", "ix1"],
                value_key="val",
                dtype=tf.float32,
                size=[100, 3])
  ```

  Fields:
    index_key: A single string name or a list of string names of index features.
      For each key the underlying feature\'s type must be `int64` and its length
      must always match that of the `value_key` feature.
      To represent `SparseTensor`s with a `dense_shape` of `rank` higher than 1
      a list of length `rank` should be used.
    value_key: Name of value feature.  The underlying feature\'s type must
      be `dtype` and its length must always match that of all the `index_key`s\'
      features.
    dtype: Data type of the `value_key` feature.
    size: A Python int or list thereof specifying the dense shape. Should be a
      list if and only if `index_key` is a list. In that case the list must be
      equal to the length of `index_key`. Each for each entry `i` all values in
      the `index_key`[i] feature must be in `[0, size[i])`.
    already_sorted: A Python boolean to specify whether the values in
      `value_key` are already sorted by their index position. If so skip
      sorting. False by default (optional).
  '''
    def __new__(cls, index_key, value_key, dtype, size, already_sorted: bool = False): ...

class FixedLenFeature(NamedTuple('FixedLenFeature', [('shape', Incomplete), ('dtype', Incomplete), ('default_value', Incomplete)])):
    """Configuration for parsing a fixed-length input feature.

  To treat sparse input as dense, provide a `default_value`; otherwise,
  the parse functions will fail on any examples missing this feature.

  Fields:
    shape: Shape of input data.
    dtype: Data type of input.
    default_value: Value to be used if an example is missing this feature. It
        must be compatible with `dtype` and of the specified `shape`.
  """
    def __new__(cls, shape, dtype, default_value: Incomplete | None = None): ...

class FixedLenSequenceFeature(NamedTuple('FixedLenSequenceFeature', [('shape', Incomplete), ('dtype', Incomplete), ('allow_missing', Incomplete), ('default_value', Incomplete)])):
    '''Configuration for parsing a variable-length input feature into a `Tensor`.

  The resulting `Tensor` of parsing a single `SequenceExample` or `Example` has
  a static `shape` of `[None] + shape` and the specified `dtype`.
  The resulting `Tensor` of parsing a `batch_size` many `Example`s has
  a static `shape` of `[batch_size, None] + shape` and the specified `dtype`.
  The entries in the `batch` from different `Examples` will be padded with
  `default_value` to the maximum length present in the `batch`.

  To treat a sparse input as dense, provide `allow_missing=True`; otherwise,
  the parse functions will fail on any examples missing this feature.

  Fields:
    shape: Shape of input data for dimension 2 and higher. First dimension is
      of variable length `None`.
    dtype: Data type of input.
    allow_missing: Whether to allow this feature to be missing from a feature
      list item. Is available only for parsing `SequenceExample` not for
      parsing `Examples`.
    default_value: Scalar value to be used to pad multiple `Example`s to their
      maximum length. Irrelevant for parsing a single `Example` or
      `SequenceExample`. Defaults to "" for dtype string and 0 otherwise
      (optional).
  '''
    def __new__(cls, shape, dtype, allow_missing: bool = False, default_value: Incomplete | None = None): ...

class _ParseOpParams:
    """Raw parameters used by `gen_parsing_ops`.

  Attributes:
    sparse_keys: A list of string keys in the examples' features. The results
      for these keys will be returned as `SparseTensor` objects.
    sparse_types: A list of `DTypes` of the same length as `sparse_keys`. Only
      `tf.float32` (`FloatList`), `tf.int64` (`Int64List`), and `tf.string`
      (`BytesList`) are supported.
    dense_keys: A list of string keys in the examples' features. The results for
      these keys will be returned as `Tensor`s
    dense_types: A list of DTypes of the same length as `dense_keys`. Only
      `tf.float32` (`FloatList`), `tf.int64` (`Int64List`), and `tf.string`
      (`BytesList`) are supported.
    dense_defaults: A dict mapping string keys to `Tensor`s. The keys of the
      dict must match the dense_keys of the feature.
    dense_shapes: A list of tuples with the same length as `dense_keys`. The
      shape of the data for each dense feature referenced by `dense_keys`.
      Required for any input tensors identified by `dense_keys`.  Must be either
      fully defined, or may contain an unknown first dimension. An unknown first
      dimension means the feature is treated as having a variable number of
      blocks, and the output shape along this dimension is considered unknown at
      graph build time.  Padding is applied for minibatch elements smaller than
      the maximum number of blocks for the given feature along this dimension.
    ragged_keys: A list of string keys in the examples' features.  The
      results for these keys will be returned as `RaggedTensor` objects.
    ragged_value_types: A list of `DTypes` of the same length as `ragged_keys`,
      specifying the value type for each ragged feature.  Must be one of:
      `tf.float32`, `tf.int64`, `tf.string`.
    ragged_split_types: A list of `DTypes` of the same length as `ragged_keys`,
      specifying the row_splits type for each ragged feature.  Must be one of:
      `tf.int32`, `tf.int64`.
    dense_shapes_as_proto: dense_shapes converted to TensorShapeProto.
    dense_defaults_vec: A vector of `Tensor`s containing the default values,
      corresponding 1:1 with `dense_keys`.
    num_features: The total number of feature keys.
  """
    sparse_keys: Incomplete
    sparse_types: Incomplete
    dense_keys: Incomplete
    dense_types: Incomplete
    dense_shapes: Incomplete
    dense_defaults: Incomplete
    ragged_keys: Incomplete
    ragged_value_types: Incomplete
    ragged_split_types: Incomplete
    def __init__(self, sparse_keys: Incomplete | None = None, sparse_types: Incomplete | None = None, dense_keys: Incomplete | None = None, dense_types: Incomplete | None = None, dense_defaults: Incomplete | None = None, dense_shapes: Incomplete | None = None, ragged_keys: Incomplete | None = None, ragged_value_types: Incomplete | None = None, ragged_split_types: Incomplete | None = None) -> None: ...
    @classmethod
    def from_features(cls, features, types):
        """Builds _ParseOpParams for a given set of features and allowed types.

    Args:
      features: A `dict` mapping feature keys to objects of a type in `types`.
      types: Type of features to allow, among `FixedLenFeature`,
        `VarLenFeature`, `SparseFeature`, and `FixedLenSequenceFeature`.

    Returns:
      A `_ParseOpParams` containing the raw parameters for `gen_parsing_ops`.

    Raises:
      ValueError: if `features` contains an item not in `types`, or an invalid
          feature.
      ValueError: if sparse and dense key sets intersect.
      ValueError: if input lengths do not match up.
    """
    @property
    def dense_shapes_as_proto(self): ...
    @property
    def num_features(self): ...
    @property
    def dense_defaults_vec(self): ...
