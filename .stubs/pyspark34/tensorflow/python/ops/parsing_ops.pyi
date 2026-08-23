from tensorflow.python.ops.gen_parsing_ops import *
from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_parsing_ops as gen_parsing_ops, math_ops as math_ops, parsing_config as parsing_config
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

VarLenFeature = parsing_config.VarLenFeature
RaggedFeature = parsing_config.RaggedFeature
SparseFeature = parsing_config.SparseFeature
FixedLenFeature = parsing_config.FixedLenFeature
FixedLenSequenceFeature = parsing_config.FixedLenSequenceFeature

def parse_example_v2(serialized, features, example_names: Incomplete | None = None, name: Incomplete | None = None):
    '''Parses `Example` protos into a `dict` of tensors.

  Parses a number of serialized [`Example`](https://www.tensorflow.org/code/tensorflow/core/example/example.proto)
  protos given in `serialized`. We refer to `serialized` as a batch with
  `batch_size` many entries of individual `Example` protos.

  `example_names` may contain descriptive names for the corresponding serialized
  protos. These may be useful for debugging purposes, but they have no effect on
  the output. If not `None`, `example_names` must be the same length as
  `serialized`.

  This op parses serialized examples into a dictionary mapping keys to `Tensor`
  `SparseTensor`, and `RaggedTensor` objects. `features` is a dict from keys to
  `VarLenFeature`, `SparseFeature`, `RaggedFeature`, and `FixedLenFeature`
  objects. Each `VarLenFeature` and `SparseFeature` is mapped to a
  `SparseTensor`; each `FixedLenFeature` is mapped to a `Tensor`; and each
  `RaggedFeature` is mapped to a `RaggedTensor`.

  Each `VarLenFeature` maps to a `SparseTensor` of the specified type
  representing a ragged matrix. Its indices are `[batch, index]` where `batch`
  identifies the example in `serialized`, and `index` is the value\'s index in
  the list of values associated with that feature and example.

  Each `SparseFeature` maps to a `SparseTensor` of the specified type
  representing a Tensor of `dense_shape` `[batch_size] + SparseFeature.size`.
  Its `values` come from the feature in the examples with key `value_key`.
  A `values[i]` comes from a position `k` in the feature of an example at batch
  entry `batch`. This positional information is recorded in `indices[i]` as
  `[batch, index_0, index_1, ...]` where `index_j` is the `k-th` value of
  the feature in the example at with key `SparseFeature.index_key[j]`.
  In other words, we split the indices (except the first index indicating the
  batch entry) of a `SparseTensor` by dimension into different features of the
  `Example`. Due to its complexity a `VarLenFeature` should be preferred over a
  `SparseFeature` whenever possible.

  Each `FixedLenFeature` `df` maps to a `Tensor` of the specified type (or
  `tf.float32` if not specified) and shape `(serialized.size(),) + df.shape`.

  `FixedLenFeature` entries with a `default_value` are optional. With no default
  value, we will fail if that `Feature` is missing from any example in
  `serialized`.

  Each `FixedLenSequenceFeature` `df` maps to a `Tensor` of the specified type
  (or `tf.float32` if not specified) and shape
  `(serialized.size(), None) + df.shape`.
  All examples in `serialized` will be padded with `default_value` along the
  second dimension.

  Each `RaggedFeature` maps to a `RaggedTensor` of the specified type.  It
  is formed by stacking the `RaggedTensor` for each example, where the
  `RaggedTensor` for each individual example is constructed using the tensors
  specified by `RaggedTensor.values_key` and `RaggedTensor.partition`.  See
  the `tf.io.RaggedFeature` documentation for details and examples.

  Examples:

  For example, if one expects a `tf.float32` `VarLenFeature` `ft` and three
  serialized `Example`s are provided:

  ```
  serialized = [
    features
      { feature { key: "ft" value { float_list { value: [1.0, 2.0] } } } },
    features
      { feature []},
    features
      { feature { key: "ft" value { float_list { value: [3.0] } } }
  ]
  ```

  then the output will look like:

  ```python
  {"ft": SparseTensor(indices=[[0, 0], [0, 1], [2, 0]],
                      values=[1.0, 2.0, 3.0],
                      dense_shape=(3, 2)) }
  ```

  If instead a `FixedLenSequenceFeature` with `default_value = -1.0` and
  `shape=[]` is used then the output will look like:

  ```python
  {"ft": [[1.0, 2.0], [3.0, -1.0]]}
  ```

  Given two `Example` input protos in `serialized`:

  ```
  [
    features {
      feature { key: "kw" value { bytes_list { value: [ "knit", "big" ] } } }
      feature { key: "gps" value { float_list { value: [] } } }
    },
    features {
      feature { key: "kw" value { bytes_list { value: [ "emmy" ] } } }
      feature { key: "dank" value { int64_list { value: [ 42 ] } } }
      feature { key: "gps" value { } }
    }
  ]
  ```

  And arguments

  ```
  example_names: ["input0", "input1"],
  features: {
      "kw": VarLenFeature(tf.string),
      "dank": VarLenFeature(tf.int64),
      "gps": VarLenFeature(tf.float32),
  }
  ```

  Then the output is a dictionary:

  ```python
  {
    "kw": SparseTensor(
        indices=[[0, 0], [0, 1], [1, 0]],
        values=["knit", "big", "emmy"]
        dense_shape=[2, 2]),
    "dank": SparseTensor(
        indices=[[1, 0]],
        values=[42],
        dense_shape=[2, 1]),
    "gps": SparseTensor(
        indices=[],
        values=[],
        dense_shape=[2, 0]),
  }
  ```

  For dense results in two serialized `Example`s:

  ```
  [
    features {
      feature { key: "age" value { int64_list { value: [ 0 ] } } }
      feature { key: "gender" value { bytes_list { value: [ "f" ] } } }
     },
     features {
      feature { key: "age" value { int64_list { value: [] } } }
      feature { key: "gender" value { bytes_list { value: [ "f" ] } } }
    }
  ]
  ```

  We can use arguments:

  ```
  example_names: ["input0", "input1"],
  features: {
      "age": FixedLenFeature([], dtype=tf.int64, default_value=-1),
      "gender": FixedLenFeature([], dtype=tf.string),
  }
  ```

  And the expected output is:

  ```python
  {
    "age": [[0], [-1]],
    "gender": [["f"], ["f"]],
  }
  ```

  An alternative to `VarLenFeature` to obtain a `SparseTensor` is
  `SparseFeature`. For example, given two `Example` input protos in
  `serialized`:

  ```
  [
    features {
      feature { key: "val" value { float_list { value: [ 0.5, -1.0 ] } } }
      feature { key: "ix" value { int64_list { value: [ 3, 20 ] } } }
    },
    features {
      feature { key: "val" value { float_list { value: [ 0.0 ] } } }
      feature { key: "ix" value { int64_list { value: [ 42 ] } } }
    }
  ]
  ```

  And arguments

  ```
  example_names: ["input0", "input1"],
  features: {
      "sparse": SparseFeature(
          index_key="ix", value_key="val", dtype=tf.float32, size=100),
  }
  ```

  Then the output is a dictionary:

  ```python
  {
    "sparse": SparseTensor(
        indices=[[0, 3], [0, 20], [1, 42]],
        values=[0.5, -1.0, 0.0]
        dense_shape=[2, 100]),
  }
  ```

  See the `tf.io.RaggedFeature` documentation for examples showing how
  `RaggedFeature` can be used to obtain `RaggedTensor`s.

  Args:
    serialized: A vector (1-D Tensor) of strings, a batch of binary
      serialized `Example` protos.
    features: A `dict` mapping feature keys to `FixedLenFeature`,
      `VarLenFeature`, `SparseFeature`, and `RaggedFeature` values.
    example_names: A vector (1-D Tensor) of strings (optional), the names of
      the serialized protos in the batch.
    name: A name for this operation (optional).

  Returns:
    A `dict` mapping feature keys to `Tensor`, `SparseTensor`, and
    `RaggedTensor` values.

  Raises:
    ValueError: if any feature is invalid.
  '''
def parse_example(serialized, features, name: Incomplete | None = None, example_names: Incomplete | None = None): ...
def parse_single_example(serialized, features, name: Incomplete | None = None, example_names: Incomplete | None = None):
    """Parses a single `Example` proto.

  Similar to `parse_example`, except:

  For dense tensors, the returned `Tensor` is identical to the output of
  `parse_example`, except there is no batch dimension, the output shape is the
  same as the shape given in `dense_shape`.

  For `SparseTensor`s, the first (batch) column of the indices matrix is removed
  (the indices matrix is a column vector), the values vector is unchanged, and
  the first (`batch_size`) entry of the shape vector is removed (it is now a
  single element vector).

  One might see performance advantages by batching `Example` protos with
  `parse_example` instead of using this function directly.

  Args:
    serialized: A scalar string Tensor, a single serialized Example.
    features: A `dict` mapping feature keys to `FixedLenFeature` or
      `VarLenFeature` values.
    name: A name for this operation (optional).
    example_names: (Optional) A scalar string Tensor, the associated name.

  Returns:
    A `dict` mapping feature keys to `Tensor` and `SparseTensor` values.

  Raises:
    ValueError: if any feature is invalid.
  """
def parse_single_example_v2(serialized, features, example_names: Incomplete | None = None, name: Incomplete | None = None):
    """Parses a single `Example` proto.

  Similar to `parse_example`, except:

  For dense tensors, the returned `Tensor` is identical to the output of
  `parse_example`, except there is no batch dimension, the output shape is the
  same as the shape given in `dense_shape`.

  For `SparseTensor`s, the first (batch) column of the indices matrix is removed
  (the indices matrix is a column vector), the values vector is unchanged, and
  the first (`batch_size`) entry of the shape vector is removed (it is now a
  single element vector).

  One might see performance advantages by batching `Example` protos with
  `parse_example` instead of using this function directly.

  Args:
    serialized: A scalar string Tensor, a single serialized Example.
    features: A `dict` mapping feature keys to `FixedLenFeature` or
      `VarLenFeature` values.
    example_names: (Optional) A scalar string Tensor, the associated name.
    name: A name for this operation (optional).

  Returns:
    A `dict` mapping feature keys to `Tensor` and `SparseTensor` values.

  Raises:
    ValueError: if any feature is invalid.
  """
def parse_sequence_example(serialized, context_features: Incomplete | None = None, sequence_features: Incomplete | None = None, example_names: Incomplete | None = None, name: Incomplete | None = None):
    """Parses a batch of `SequenceExample` protos.

  Parses a vector of serialized
  [`SequenceExample`](https://www.tensorflow.org/code/tensorflow/core/example/example.proto)
  protos given in `serialized`.

  This op parses serialized sequence examples into a tuple of dictionaries,
  each mapping keys to `Tensor` and `SparseTensor` objects.
  The first dictionary contains mappings for keys appearing in
  `context_features`, and the second dictionary contains mappings for keys
  appearing in `sequence_features`.

  At least one of `context_features` and `sequence_features` must be provided
  and non-empty.

  The `context_features` keys are associated with a `SequenceExample` as a
  whole, independent of time / frame.  In contrast, the `sequence_features` keys
  provide a way to access variable-length data within the `FeatureList` section
  of the `SequenceExample` proto.  While the shapes of `context_features` values
  are fixed with respect to frame, the frame dimension (the first dimension)
  of `sequence_features` values may vary between `SequenceExample` protos,
  and even between `feature_list` keys within the same `SequenceExample`.

  `context_features` contains `VarLenFeature`, `RaggedFeature`, and
  `FixedLenFeature`  objects. Each `VarLenFeature` is mapped to a
  `SparseTensor`; each `RaggedFeature` is  mapped to a `RaggedTensor`; and each
  `FixedLenFeature` is mapped to a `Tensor`, of the specified type, shape, and
  default value.

  `sequence_features` contains `VarLenFeature`, `RaggedFeature`, and
  `FixedLenSequenceFeature` objects. Each `VarLenFeature` is mapped to a
  `SparseTensor`; each `RaggedFeature` is mapped to a `RaggedTensor`; and
  each `FixedLenSequenceFeature` is mapped to a `Tensor`, each of the specified
  type. The shape will be `(B,T,) + df.dense_shape` for
  `FixedLenSequenceFeature` `df`, where `B` is the batch size, and `T` is the
  length of the associated `FeatureList` in the `SequenceExample`. For instance,
  `FixedLenSequenceFeature([])` yields a scalar 2-D `Tensor` of static shape
  `[None, None]` and dynamic shape `[B, T]`, while
  `FixedLenSequenceFeature([k])` (for `int k >= 1`) yields a 3-D matrix `Tensor`
  of static shape `[None, None, k]` and dynamic shape `[B, T, k]`.

  Like the input, the resulting output tensors have a batch dimension. This
  means that the original per-example shapes of `VarLenFeature`s and
  `FixedLenSequenceFeature`s can be lost. To handle that situation, this op also
  provides dicts of shape tensors as part of the output. There is one dict for
  the context features, and one for the feature_list features. Context features
  of type `FixedLenFeature`s will not be present, since their shapes are already
  known by the caller. In situations where the input `FixedLenSequenceFeature`s
  are of different sequence lengths across examples, the shorter examples will
  be padded with default datatype values: 0 for numeric types, and the empty
  string for string types.

  Each `SparseTensor` corresponding to `sequence_features` represents a ragged
  vector.  Its indices are `[time, index]`, where `time` is the `FeatureList`
  entry and `index` is the value's index in the list of values associated with
  that time.

  `FixedLenFeature` entries with a `default_value` and `FixedLenSequenceFeature`
  entries with `allow_missing=True` are optional; otherwise, we will fail if
  that `Feature` or `FeatureList` is missing from any example in `serialized`.

  `example_name` may contain a descriptive name for the corresponding serialized
  proto. This may be useful for debugging purposes, but it has no effect on the
  output. If not `None`, `example_name` must be a scalar.

  Args:
    serialized: A vector (1-D Tensor) of type string containing binary
      serialized `SequenceExample` protos.
    context_features: A `dict` mapping feature keys to `FixedLenFeature` or
      `VarLenFeature` or `RaggedFeature` values. These features are associated
      with a `SequenceExample` as a whole.
    sequence_features: A `dict` mapping feature keys to
      `FixedLenSequenceFeature` or `VarLenFeature` or `RaggedFeature` values.
      These features are associated with data within the `FeatureList` section
      of the `SequenceExample` proto.
    example_names: A vector (1-D Tensor) of strings (optional), the name of the
      serialized protos.
    name: A name for this operation (optional).

  Returns:
    A tuple of three `dict`s, each mapping keys to `Tensor`s,
    `SparseTensor`s, and `RaggedTensor`. The first dict contains the context
    key/values, the second dict contains the feature_list key/values, and the
    final dict contains the lengths of any dense feature_list features.

  Raises:
    ValueError: if any feature is invalid.
  """
def parse_single_sequence_example(serialized, context_features: Incomplete | None = None, sequence_features: Incomplete | None = None, example_name: Incomplete | None = None, name: Incomplete | None = None):
    """Parses a single `SequenceExample` proto.

  Parses a single serialized [`SequenceExample`](https://www.tensorflow.org/code/tensorflow/core/example/example.proto)
  proto given in `serialized`.

  This op parses a serialized sequence example into a tuple of dictionaries,
  each mapping keys to `Tensor` and `SparseTensor` objects.
  The first dictionary contains mappings for keys appearing in
  `context_features`, and the second dictionary contains mappings for keys
  appearing in `sequence_features`.

  At least one of `context_features` and `sequence_features` must be provided
  and non-empty.

  The `context_features` keys are associated with a `SequenceExample` as a
  whole, independent of time / frame.  In contrast, the `sequence_features` keys
  provide a way to access variable-length data within the `FeatureList` section
  of the `SequenceExample` proto.  While the shapes of `context_features` values
  are fixed with respect to frame, the frame dimension (the first dimension)
  of `sequence_features` values may vary between `SequenceExample` protos,
  and even between `feature_list` keys within the same `SequenceExample`.

  `context_features` contains `VarLenFeature`, `RaggedFeature`, and
  `FixedLenFeature` objects. Each `VarLenFeature` is mapped to a `SparseTensor`;
  each `RaggedFeature` is mapped to a `RaggedTensor`; and each `FixedLenFeature`
  is mapped to a `Tensor`, of the specified type, shape, and default value.

  `sequence_features` contains `VarLenFeature`, `RaggedFeature`, and
  `FixedLenSequenceFeature` objects. Each `VarLenFeature` is mapped to a
  `SparseTensor`; each `RaggedFeature` is mapped to a `RaggedTensor`; and each
  `FixedLenSequenceFeature` is mapped to a `Tensor`, each of the specified type.
  The shape will be `(T,) + df.dense_shape` for `FixedLenSequenceFeature` `df`,
  where `T` is the length of the associated `FeatureList` in the
  `SequenceExample`. For instance, `FixedLenSequenceFeature([])` yields a scalar
  1-D `Tensor` of static shape `[None]` and dynamic shape `[T]`, while
  `FixedLenSequenceFeature([k])` (for `int k >= 1`) yields a 2-D matrix `Tensor`
  of static shape `[None, k]` and dynamic shape `[T, k]`.

  Each `SparseTensor` corresponding to `sequence_features` represents a ragged
  vector.  Its indices are `[time, index]`, where `time` is the `FeatureList`
  entry and `index` is the value's index in the list of values associated with
  that time.

  `FixedLenFeature` entries with a `default_value` and `FixedLenSequenceFeature`
  entries with `allow_missing=True` are optional; otherwise, we will fail if
  that `Feature` or `FeatureList` is missing from any example in `serialized`.

  `example_name` may contain a descriptive name for the corresponding serialized
  proto. This may be useful for debugging purposes, but it has no effect on the
  output. If not `None`, `example_name` must be a scalar.

  Note that the batch version of this function, `tf.parse_sequence_example`,
  is written for better memory efficiency and will be faster on large
  `SequenceExample`s.

  Args:
    serialized: A scalar (0-D Tensor) of type string, a single binary
      serialized `SequenceExample` proto.
    context_features: A `dict` mapping feature keys to `FixedLenFeature` or
      `VarLenFeature` or `RaggedFeature` values. These features are associated
      with a `SequenceExample` as a whole.
    sequence_features: A `dict` mapping feature keys to
      `FixedLenSequenceFeature` or `VarLenFeature` or `RaggedFeature` values.
      These features are associated with data within the `FeatureList` section
      of the `SequenceExample` proto.
    example_name: A scalar (0-D Tensor) of strings (optional), the name of
      the serialized proto.
    name: A name for this operation (optional).

  Returns:
    A tuple of two `dict`s, each mapping keys to `Tensor`s and `SparseTensor`s
    and `RaggedTensor`s.

    * The first dict contains the context key/values.
    * The second dict contains the feature_list key/values.

  Raises:
    ValueError: if any feature is invalid.
  """
def decode_raw(input_bytes, out_type, little_endian: bool = True, fixed_length: Incomplete | None = None, name: Incomplete | None = None):
    '''Convert raw bytes from input tensor into numeric tensors.

  Every component of the input tensor is interpreted as a sequence of bytes.
  These bytes are then decoded as numbers in the format specified by `out_type`.

  >>> tf.io.decode_raw(tf.constant("1"), tf.uint8)
  <tf.Tensor: shape=(1,), dtype=uint8, numpy=array([49], dtype=uint8)>
  >>> tf.io.decode_raw(tf.constant("1,2"), tf.uint8)
  <tf.Tensor: shape=(3,), dtype=uint8, numpy=array([49, 44, 50], dtype=uint8)>

  Note that the rank of the output tensor is always one more than the input one:

  >>> tf.io.decode_raw(tf.constant(["1","2"]), tf.uint8).shape
  TensorShape([2, 1])
  >>> tf.io.decode_raw(tf.constant([["1"],["2"]]), tf.uint8).shape
  TensorShape([2, 1, 1])

  This is because each byte in the input is converted to a new value on the
  output (if output type is `uint8` or `int8`, otherwise chunks of inputs get
  coverted to a new value):

  >>> tf.io.decode_raw(tf.constant("123"), tf.uint8)
  <tf.Tensor: shape=(3,), dtype=uint8, numpy=array([49, 50, 51], dtype=uint8)>
  >>> tf.io.decode_raw(tf.constant("1234"), tf.uint8)
  <tf.Tensor: shape=(4,), dtype=uint8, numpy=array([49, 50, 51, 52], ...
  >>> # chuncked output
  >>> tf.io.decode_raw(tf.constant("12"), tf.uint16)
  <tf.Tensor: shape=(1,), dtype=uint16, numpy=array([12849], dtype=uint16)>
  >>> tf.io.decode_raw(tf.constant("1234"), tf.uint16)
  <tf.Tensor: shape=(2,), dtype=uint16, numpy=array([12849, 13363], ...
  >>> # int64 output
  >>> tf.io.decode_raw(tf.constant("12345678"), tf.int64)
  <tf.Tensor: ... numpy=array([4050765991979987505])>
  >>> tf.io.decode_raw(tf.constant("1234567887654321"), tf.int64)
  <tf.Tensor: ... numpy=array([4050765991979987505, 3544952156018063160])>

  The operation allows specifying endianness via the `little_endian` parameter.

  >>> tf.io.decode_raw(tf.constant("\\x0a\\x0b"), tf.int16)
  <tf.Tensor: shape=(1,), dtype=int16, numpy=array([2826], dtype=int16)>
  >>> hex(2826)
  \'0xb0a\'
  >>> tf.io.decode_raw(tf.constant("\\x0a\\x0b"), tf.int16, little_endian=False)
  <tf.Tensor: shape=(1,), dtype=int16, numpy=array([2571], dtype=int16)>
  >>> hex(2571)
  \'0xa0b\'

  If the elements of `input_bytes` are of different length, you must specify
  `fixed_length`:

  >>> tf.io.decode_raw(tf.constant([["1"],["23"]]), tf.uint8, fixed_length=4)
  <tf.Tensor: shape=(2, 1, 4), dtype=uint8, numpy=
  array([[[49,  0,  0,  0]],
         [[50, 51,  0,  0]]], dtype=uint8)>

  If the `fixed_length` value is larger that the length of the `out_type` dtype,
  multiple values are generated:

  >>> tf.io.decode_raw(tf.constant(["1212"]), tf.uint16, fixed_length=4)
  <tf.Tensor: shape=(1, 2), dtype=uint16, numpy=array([[12849, 12849]], ...

  If the input value is larger than `fixed_length`, it is truncated:

  >>> x=\'\'.join([chr(1), chr(2), chr(3), chr(4)])
  >>> tf.io.decode_raw(x, tf.uint16, fixed_length=2)
  <tf.Tensor: shape=(1,), dtype=uint16, numpy=array([513], dtype=uint16)>
  >>> hex(513)
  \'0x201\'

  If `little_endian` and `fixed_length` are specified, truncation to the fixed
  length occurs before endianness conversion:

  >>> x=\'\'.join([chr(1), chr(2), chr(3), chr(4)])
  >>> tf.io.decode_raw(x, tf.uint16, fixed_length=2, little_endian=False)
  <tf.Tensor: shape=(1,), dtype=uint16, numpy=array([258], dtype=uint16)>
  >>> hex(258)
  \'0x102\'

  If input values all have the same length, then specifying `fixed_length`
  equal to the size of the strings should not change output:

  >>> x = ["12345678", "87654321"]
  >>> tf.io.decode_raw(x, tf.int16)
  <tf.Tensor: shape=(2, 4), dtype=int16, numpy=
  array([[12849, 13363, 13877, 14391],
         [14136, 13622, 13108, 12594]], dtype=int16)>
  >>> tf.io.decode_raw(x, tf.int16, fixed_length=len(x[0]))
  <tf.Tensor: shape=(2, 4), dtype=int16, numpy=
  array([[12849, 13363, 13877, 14391],
         [14136, 13622, 13108, 12594]], dtype=int16)>

  Args:
    input_bytes:
      Each element of the input Tensor is converted to an array of bytes.

      Currently, this must be a tensor of strings (bytes), although semantically
      the operation should support any input.
    out_type:
      `DType` of the output. Acceptable types are `half`, `float`, `double`,
      `int32`, `uint16`, `uint8`, `int16`, `int8`, `int64`.
    little_endian:
      Whether the `input_bytes` data is in little-endian format. Data will be
      converted into host byte order if necessary.
    fixed_length:
      If set, the first `fixed_length` bytes of each element will be converted.
      Data will be zero-padded or truncated to the specified length.

      `fixed_length` must be a multiple of the size of `out_type`.

      `fixed_length` must be specified if the elements of `input_bytes` are of
      variable length.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` object storing the decoded bytes.
  '''
def decode_raw_v1(input_bytes: Incomplete | None = None, out_type: Incomplete | None = None, little_endian: bool = True, name: Incomplete | None = None, bytes: Incomplete | None = None):
    """Convert raw byte strings into tensors.

  Args:
    input_bytes:
      Each element of the input Tensor is converted to an array of bytes.
    out_type:
      `DType` of the output. Acceptable types are `half`, `float`, `double`,
      `int32`, `uint16`, `uint8`, `int16`, `int8`, `int64`.
    little_endian:
      Whether the `input_bytes` data is in little-endian format. Data will be
      converted into host byte order if necessary.
    name: A name for the operation (optional).
    bytes: Deprecated parameter. Use `input_bytes` instead.

  Returns:
    A `Tensor` object storing the decoded bytes.
  """
def decode_csv(records, record_defaults, field_delim: str = ',', use_quote_delim: bool = True, name: Incomplete | None = None, na_value: str = '', select_cols: Incomplete | None = None):
    '''Convert CSV records to tensors. Each column maps to one tensor.

  RFC 4180 format is expected for the CSV records.
  (https://tools.ietf.org/html/rfc4180)
  Note that we allow leading and trailing spaces with int or float field.

  Args:
    records: A `Tensor` of type `string`.
      Each string is a record/row in the csv and all records should have
      the same format.
    record_defaults: A list of `Tensor` objects with specific types.
      Acceptable types are `float32`, `float64`, `int32`, `int64`, `string`.
      One tensor per column of the input record, with either a
      scalar default value for that column or an empty vector if the column is
      required.
    field_delim: An optional `string`. Defaults to `","`.
      char delimiter to separate fields in a record.
    use_quote_delim: An optional `bool`. Defaults to `True`.
      If false, treats double quotation marks as regular
      characters inside of the string fields (ignoring RFC 4180, Section 2,
      Bullet 5).
    name: A name for the operation (optional).
    na_value: Additional string to recognize as NA/NaN.
    select_cols: Optional sorted list of column indices to select. If specified,
      only this subset of columns will be parsed and returned.

  Returns:
    A list of `Tensor` objects. Has the same type as `record_defaults`.
    Each tensor will have the same shape as records.

  Raises:
    ValueError: If any of the arguments is malformed.
  '''
def decode_csv_v2(records, record_defaults, field_delim: str = ',', use_quote_delim: bool = True, na_value: str = '', select_cols: Incomplete | None = None, name: Incomplete | None = None):
    '''Convert CSV records to tensors. Each column maps to one tensor.

  RFC 4180 format is expected for the CSV records.
  (https://tools.ietf.org/html/rfc4180)
  Note that we allow leading and trailing spaces with int or float field.

  Args:
    records: A `Tensor` of type `string`.
      Each string is a record/row in the csv and all records should have
      the same format.
    record_defaults: A list of `Tensor` objects with specific types.
      Acceptable types are `float32`, `float64`, `int32`, `int64`, `string`.
      One tensor per column of the input record, with either a
      scalar default value for that column or an empty vector if the column is
      required.
    field_delim: An optional `string`. Defaults to `","`.
      char delimiter to separate fields in a record.
    use_quote_delim: An optional `bool`. Defaults to `True`.
      If false, treats double quotation marks as regular
      characters inside of the string fields (ignoring RFC 4180, Section 2,
      Bullet 5).
    na_value: Additional string to recognize as NA/NaN.
    select_cols: Optional sorted list of column indices to select. If specified,
      only this subset of columns will be parsed and returned.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects. Has the same type as `record_defaults`.
    Each tensor will have the same shape as records.

  Raises:
    ValueError: If any of the arguments is malformed.
  '''
def decode_json_example(json_examples, name: Incomplete | None = None):
    '''Convert JSON-encoded Example records to binary protocol buffer strings.

  Note: This is **not** a general purpose JSON parsing op.

  This op converts JSON-serialized `tf.train.Example` (maybe created with
  `json_format.MessageToJson`, following the
  [standard JSON mapping](
  https://developers.google.com/protocol-buffers/docs/proto3#json))
  to a binary-serialized `tf.train.Example` (equivalent to
  `Example.SerializeToString()`) suitable for conversion to tensors with
  `tf.io.parse_example`.

  Here is a `tf.train.Example` proto:

  >>> example = tf.train.Example(
  ...   features=tf.train.Features(
  ...       feature={
  ...           "a": tf.train.Feature(
  ...               int64_list=tf.train.Int64List(
  ...                   value=[1, 1, 3]))}))

  Here it is converted to JSON:

  >>> from google.protobuf import json_format
  >>> example_json = json_format.MessageToJson(example)
  >>> print(example_json)
  {
    "features": {
      "feature": {
        "a": {
          "int64List": {
            "value": [
              "1",
              "1",
              "3"
            ]
          }
        }
      }
    }
  }

  This op converts the above json string to a binary proto:

  >>> example_binary = tf.io.decode_json_example(example_json)
  >>> example_binary.numpy()
  b\'\\n\\x0f\\n\\r\\n\\x01a\\x12\\x08\\x1a\\x06\\x08\\x01\\x08\\x01\\x08\\x03\'

  The OP works on string tensors of andy shape:

  >>> tf.io.decode_json_example([
  ...     [example_json, example_json],
  ...     [example_json, example_json]]).shape.as_list()
  [2, 2]

  This resulting binary-string is equivalent to `Example.SerializeToString()`,
  and can be converted to Tensors using `tf.io.parse_example` and related
  functions:

  >>> tf.io.parse_example(
  ...   serialized=[example_binary.numpy(),
  ...              example.SerializeToString()],
  ...   features = {\'a\': tf.io.FixedLenFeature(shape=[3], dtype=tf.int64)})
  {\'a\': <tf.Tensor: shape=(2, 3), dtype=int64, numpy=
   array([[1, 1, 3],
          [1, 1, 3]])>}

  Args:
    json_examples: A string tensor containing json-serialized `tf.Example`
      protos.
    name: A name for the op.

  Returns:
    A string Tensor containing the binary-serialized `tf.Example` protos.

  Raises:
     `tf.errors.InvalidArgumentError`: If the JSON could not be converted to a
     `tf.Example`
  '''
