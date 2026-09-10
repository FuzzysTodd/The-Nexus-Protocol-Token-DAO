from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def decode_csv(records, record_defaults, field_delim: str = ',', use_quote_delim: bool = True, na_value: str = '', select_cols=[], name: Incomplete | None = None):
    '''Convert CSV records to tensors. Each column maps to one tensor.

  RFC 4180 format is expected for the CSV records.
  (https://tools.ietf.org/html/rfc4180)
  Note that we allow leading and trailing spaces with int or float field.

  Args:
    records: A `Tensor` of type `string`.
      Each string is a record/row in the csv and all records should have
      the same format.
    record_defaults: A list of `Tensor` objects with types from: `float32`, `float64`, `int32`, `int64`, `string`.
      One tensor per column of the input record, with either a
      scalar default value for that column or an empty vector if the column is
      required.
    field_delim: An optional `string`. Defaults to `","`.
      char delimiter to separate fields in a record.
    use_quote_delim: An optional `bool`. Defaults to `True`.
      If false, treats double quotation marks as regular
      characters inside of the string fields (ignoring RFC 4180, Section 2,
      Bullet 5).
    na_value: An optional `string`. Defaults to `""`.
      Additional string to recognize as NA/NaN.
    select_cols: An optional list of `ints`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects. Has the same type as `record_defaults`.
  '''

DecodeCSV: Incomplete

def decode_csv_eager_fallback(records, record_defaults, field_delim, use_quote_delim, na_value, select_cols, name, ctx): ...
def decode_compressed(bytes, compression_type: str = '', name: Incomplete | None = None):
    '''Decompress strings.

  This op decompresses each element of the `bytes` input `Tensor`, which
  is assumed to be compressed using the given `compression_type`.

  The `output` is a string `Tensor` of the same shape as `bytes`,
  each element containing the decompressed data from the corresponding
  element in `bytes`.

  Args:
    bytes: A `Tensor` of type `string`.
      A Tensor of string which is compressed.
    compression_type: An optional `string`. Defaults to `""`.
      A scalar containing either (i) the empty string (no
      compression), (ii) "ZLIB", or (iii) "GZIP".
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

DecodeCompressed: Incomplete

def decode_compressed_eager_fallback(bytes, compression_type, name, ctx): ...
def decode_json_example(json_examples, name: Incomplete | None = None):
    """Convert JSON-encoded Example records to binary protocol buffer strings.

  
  Note: This is **not** a general purpose JSON parsing op.

  This op converts JSON-serialized
  `tf.train.Example` (created with `json_format.MessageToJson`, following the
  [standard JSON mapping](https://developers.google.com/protocol-buffers/docs/proto3#json))
  to a binary-serialized `tf.train.Example` (equivalent to
  `Example.SerializeToString()`) suitable for conversion to tensors with
  `tf.io.parse_example`.

  Args:
    json_examples: A `Tensor` of type `string`.
      Each string is a JSON object serialized according to the JSON
      mapping of the Example proto.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

DecodeJSONExample: Incomplete

def decode_json_example_eager_fallback(json_examples, name, ctx): ...
def decode_padded_raw(input_bytes, fixed_length, out_type, little_endian: bool = True, name: Incomplete | None = None):
    """Reinterpret the bytes of a string as a vector of numbers.

  Args:
    input_bytes: A `Tensor` of type `string`. Tensor of string to be decoded.
    fixed_length: A `Tensor` of type `int32`.
      Length in bytes for each element of the decoded output. Must be a multiple
      of the size of the output type.
    out_type: A `tf.DType` from: `tf.half, tf.float32, tf.float64, tf.int32, tf.uint16, tf.uint8, tf.int16, tf.int8, tf.int64, tf.bfloat16`.
    little_endian: An optional `bool`. Defaults to `True`.
      Whether the input `input_bytes` is in little-endian order. Ignored for
      `out_type` values that are stored in a single byte, like `uint8`
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `out_type`.
  """

DecodePaddedRaw: Incomplete

def decode_padded_raw_eager_fallback(input_bytes, fixed_length, out_type, little_endian, name, ctx): ...
def decode_raw(bytes, out_type, little_endian: bool = True, name: Incomplete | None = None):
    """Reinterpret the bytes of a string as a vector of numbers.

  Args:
    bytes: A `Tensor` of type `string`.
      All the elements must have the same length.
    out_type: A `tf.DType` from: `tf.half, tf.float32, tf.float64, tf.int32, tf.uint16, tf.uint8, tf.int16, tf.int8, tf.int64, tf.complex64, tf.complex128, tf.bool, tf.bfloat16`.
    little_endian: An optional `bool`. Defaults to `True`.
      Whether the input `bytes` are in little-endian order.
      Ignored for `out_type` values that are stored in a single byte like
      `uint8`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `out_type`.
  """

DecodeRaw: Incomplete

def decode_raw_eager_fallback(bytes, out_type, little_endian, name, ctx): ...

class _ParseExampleOutput(NamedTuple):
    sparse_indices: Incomplete
    sparse_values: Incomplete
    sparse_shapes: Incomplete
    dense_values: Incomplete

def parse_example(serialized, names, sparse_keys, dense_keys, dense_defaults, sparse_types, dense_shapes, name: Incomplete | None = None):
    '''Transforms a vector of brain.Example protos (as strings) into typed tensors.

  Args:
    serialized: A `Tensor` of type `string`.
      A vector containing a batch of binary serialized Example protos.
    names: A `Tensor` of type `string`.
      A vector containing the names of the serialized protos.
      May contain, for example, table key (descriptive) names for the
      corresponding serialized protos.  These are purely useful for debugging
      purposes, and the presence of values here has no effect on the output.
      May also be an empty vector if no names are available.
      If non-empty, this vector must be the same length as "serialized".
    sparse_keys: A list of `Tensor` objects with type `string`.
      A list of Nsparse string Tensors (scalars).
      The keys expected in the Examples\' features associated with sparse values.
    dense_keys: A list of `Tensor` objects with type `string`.
      A list of Ndense string Tensors (scalars).
      The keys expected in the Examples\' features associated with dense values.
    dense_defaults: A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
      A list of Ndense Tensors (some may be empty).
      dense_defaults[j] provides default values
      when the example\'s feature_map lacks dense_key[j].  If an empty Tensor is
      provided for dense_defaults[j], then the Feature dense_keys[j] is required.
      The input type is inferred from dense_defaults[j], even when it\'s empty.
      If dense_defaults[j] is not empty, and dense_shapes[j] is fully defined,
      then the shape of dense_defaults[j] must match that of dense_shapes[j].
      If dense_shapes[j] has an undefined major dimension (variable strides dense
      feature), dense_defaults[j] must contain a single element:
      the padding element.
    sparse_types: A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
      A list of Nsparse types; the data types of data in each Feature
      given in sparse_keys.
      Currently the ParseExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    dense_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`).
      A list of Ndense shapes; the shapes of data in each Feature
      given in dense_keys.
      The number of elements in the Feature corresponding to dense_key[j]
      must always equal dense_shapes[j].NumEntries().
      If dense_shapes[j] == (D0, D1, ..., DN) then the shape of output
      Tensor dense_values[j] will be (|serialized|, D0, D1, ..., DN):
      The dense outputs are just the inputs row-stacked by batch.
      This works for dense_shapes[j] = (-1, D1, ..., DN).  In this case
      the shape of the output Tensor dense_values[j] will be
      (|serialized|, M, D1, .., DN), where M is the maximum number of blocks
      of elements of length D1 * .... * DN, across all minibatch entries
      in the input.  Any minibatch entry with less than M blocks of elements of
      length D1 * ... * DN will be padded with the corresponding default_value
      scalar element along the second dimension.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sparse_indices, sparse_values, sparse_shapes, dense_values).

    sparse_indices: A list with the same length as `sparse_keys` of `Tensor` objects with type `int64`.
    sparse_values: A list of `Tensor` objects of type `sparse_types`.
    sparse_shapes: A list with the same length as `sparse_keys` of `Tensor` objects with type `int64`.
    dense_values: A list of `Tensor` objects. Has the same type as `dense_defaults`.
  '''

ParseExample: Incomplete

def parse_example_eager_fallback(serialized, names, sparse_keys, dense_keys, dense_defaults, sparse_types, dense_shapes, name, ctx): ...

class _ParseExampleV2Output(NamedTuple):
    sparse_indices: Incomplete
    sparse_values: Incomplete
    sparse_shapes: Incomplete
    dense_values: Incomplete
    ragged_values: Incomplete
    ragged_row_splits: Incomplete

def parse_example_v2(serialized, names, sparse_keys, dense_keys, ragged_keys, dense_defaults, num_sparse, sparse_types, ragged_value_types, ragged_split_types, dense_shapes, name: Incomplete | None = None):
    '''Transforms a vector of tf.Example protos (as strings) into typed tensors.

  Args:
    serialized: A `Tensor` of type `string`.
      A scalar or vector containing binary serialized Example protos.
    names: A `Tensor` of type `string`.
      A tensor containing the names of the serialized protos.
      Corresponds 1:1 with the `serialized` tensor.
      May contain, for example, table key (descriptive) names for the
      corresponding serialized protos.  These are purely useful for debugging
      purposes, and the presence of values here has no effect on the output.
      May also be an empty vector if no names are available.
      If non-empty, this tensor must have the same shape as "serialized".
    sparse_keys: A `Tensor` of type `string`. Vector of strings.
      The keys expected in the Examples\' features associated with sparse values.
    dense_keys: A `Tensor` of type `string`. Vector of strings.
      The keys expected in the Examples\' features associated with dense values.
    ragged_keys: A `Tensor` of type `string`. Vector of strings.
      The keys expected in the Examples\' features associated with ragged values.
    dense_defaults: A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
      A list of Tensors (some may be empty).  Corresponds 1:1 with `dense_keys`.
      dense_defaults[j] provides default values
      when the example\'s feature_map lacks dense_key[j].  If an empty Tensor is
      provided for dense_defaults[j], then the Feature dense_keys[j] is required.
      The input type is inferred from dense_defaults[j], even when it\'s empty.
      If dense_defaults[j] is not empty, and dense_shapes[j] is fully defined,
      then the shape of dense_defaults[j] must match that of dense_shapes[j].
      If dense_shapes[j] has an undefined major dimension (variable strides dense
      feature), dense_defaults[j] must contain a single element:
      the padding element.
    num_sparse: An `int` that is `>= 0`. The number of sparse keys.
    sparse_types: A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
      A list of `num_sparse` types; the data types of data in each Feature
      given in sparse_keys.
      Currently the ParseExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    ragged_value_types: A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
      A list of `num_ragged` types; the data types of data in each Feature
      given in ragged_keys (where `num_ragged = sparse_keys.size()`).
      Currently the ParseExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    ragged_split_types: A list of `tf.DTypes` from: `tf.int32, tf.int64`.
      A list of `num_ragged` types; the data types of row_splits in each Feature
      given in ragged_keys (where `num_ragged = sparse_keys.size()`).
      May be DT_INT32 or DT_INT64.
    dense_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`).
      A list of `num_dense` shapes; the shapes of data in each Feature
      given in dense_keys (where `num_dense = dense_keys.size()`).
      The number of elements in the Feature corresponding to dense_key[j]
      must always equal dense_shapes[j].NumEntries().
      If dense_shapes[j] == (D0, D1, ..., DN) then the shape of output
      Tensor dense_values[j] will be (|serialized|, D0, D1, ..., DN):
      The dense outputs are just the inputs row-stacked by batch.
      This works for dense_shapes[j] = (-1, D1, ..., DN).  In this case
      the shape of the output Tensor dense_values[j] will be
      (|serialized|, M, D1, .., DN), where M is the maximum number of blocks
      of elements of length D1 * .... * DN, across all minibatch entries
      in the input.  Any minibatch entry with less than M blocks of elements of
      length D1 * ... * DN will be padded with the corresponding default_value
      scalar element along the second dimension.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sparse_indices, sparse_values, sparse_shapes, dense_values, ragged_values, ragged_row_splits).

    sparse_indices: A list of `num_sparse` `Tensor` objects with type `int64`.
    sparse_values: A list of `Tensor` objects of type `sparse_types`.
    sparse_shapes: A list of `num_sparse` `Tensor` objects with type `int64`.
    dense_values: A list of `Tensor` objects. Has the same type as `dense_defaults`.
    ragged_values: A list of `Tensor` objects of type `ragged_value_types`.
    ragged_row_splits: A list of `Tensor` objects of type `ragged_split_types`.
  '''

ParseExampleV2: Incomplete

def parse_example_v2_eager_fallback(serialized, names, sparse_keys, dense_keys, ragged_keys, dense_defaults, num_sparse, sparse_types, ragged_value_types, ragged_split_types, dense_shapes, name, ctx): ...

class _ParseSequenceExampleOutput(NamedTuple):
    context_sparse_indices: Incomplete
    context_sparse_values: Incomplete
    context_sparse_shapes: Incomplete
    context_dense_values: Incomplete
    feature_list_sparse_indices: Incomplete
    feature_list_sparse_values: Incomplete
    feature_list_sparse_shapes: Incomplete
    feature_list_dense_values: Incomplete
    feature_list_dense_lengths: Incomplete

def parse_sequence_example(serialized, debug_name, context_dense_defaults, feature_list_dense_missing_assumed_empty, context_sparse_keys, context_dense_keys, feature_list_sparse_keys, feature_list_dense_keys, Ncontext_sparse: int = 0, Ncontext_dense: int = 0, Nfeature_list_sparse: int = 0, Nfeature_list_dense: int = 0, context_sparse_types=[], feature_list_dense_types=[], context_dense_shapes=[], feature_list_sparse_types=[], feature_list_dense_shapes=[], name: Incomplete | None = None):
    """Transforms a vector of brain.SequenceExample protos (as strings) into typed tensors.

  Args:
    serialized: A `Tensor` of type `string`.
      A vector containing binary serialized SequenceExample protos.
    debug_name: A `Tensor` of type `string`.
      A vector containing the names of the serialized protos.
      May contain, for example, table key (descriptive) name for the
      corresponding serialized proto.  This is purely useful for debugging
      purposes, and the presence of values here has no effect on the output.
      May also be an empty vector if no name is available.
    context_dense_defaults: A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
      A list of Ncontext_dense Tensors (some may be empty).
      context_dense_defaults[j] provides default values
      when the SequenceExample's context map lacks context_dense_key[j].
      If an empty Tensor is provided for context_dense_defaults[j],
      then the Feature context_dense_keys[j] is required.
      The input type is inferred from context_dense_defaults[j], even when it's
      empty.  If context_dense_defaults[j] is not empty, its shape must match
      context_dense_shapes[j].
    feature_list_dense_missing_assumed_empty: A list of `strings`.
      A vector listing the
      FeatureList keys which may be missing from the SequenceExamples.  If the
      associated FeatureList is missing, it is treated as empty.  By default,
      any FeatureList not listed in this vector must exist in the SequenceExamples.
    context_sparse_keys: A list of `strings`.
      A list of Ncontext_sparse string Tensors (scalars).
      The keys expected in the Examples' features associated with context_sparse
      values.
    context_dense_keys: A list of `strings`.
      A list of Ncontext_dense string Tensors (scalars).
      The keys expected in the SequenceExamples' context features associated with
      dense values.
    feature_list_sparse_keys: A list of `strings`.
      A list of Nfeature_list_sparse string Tensors
      (scalars).  The keys expected in the FeatureLists associated with sparse
      values.
    feature_list_dense_keys: A list of `strings`.
      A list of Nfeature_list_dense string Tensors (scalars).
      The keys expected in the SequenceExamples' feature_lists associated
      with lists of dense values.
    Ncontext_sparse: An optional `int` that is `>= 0`. Defaults to `0`.
    Ncontext_dense: An optional `int` that is `>= 0`. Defaults to `0`.
    Nfeature_list_sparse: An optional `int` that is `>= 0`. Defaults to `0`.
    Nfeature_list_dense: An optional `int` that is `>= 0`. Defaults to `0`.
    context_sparse_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      A list of Ncontext_sparse types; the data types of data in
      each context Feature given in context_sparse_keys.
      Currently the ParseSingleSequenceExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    feature_list_dense_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
    context_dense_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
      A list of Ncontext_dense shapes; the shapes of data in
      each context Feature given in context_dense_keys.
      The number of elements in the Feature corresponding to context_dense_key[j]
      must always equal context_dense_shapes[j].NumEntries().
      The shape of context_dense_values[j] will match context_dense_shapes[j].
    feature_list_sparse_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      A list of Nfeature_list_sparse types; the data types
      of data in each FeatureList given in feature_list_sparse_keys.
      Currently the ParseSingleSequenceExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    feature_list_dense_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
      A list of Nfeature_list_dense shapes; the shapes of
      data in each FeatureList given in feature_list_dense_keys.
      The shape of each Feature in the FeatureList corresponding to
      feature_list_dense_key[j] must always equal
      feature_list_dense_shapes[j].NumEntries().
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (context_sparse_indices, context_sparse_values, context_sparse_shapes, context_dense_values, feature_list_sparse_indices, feature_list_sparse_values, feature_list_sparse_shapes, feature_list_dense_values, feature_list_dense_lengths).

    context_sparse_indices: A list of `Ncontext_sparse` `Tensor` objects with type `int64`.
    context_sparse_values: A list of `Tensor` objects of type `context_sparse_types`.
    context_sparse_shapes: A list of `Ncontext_sparse` `Tensor` objects with type `int64`.
    context_dense_values: A list of `Tensor` objects. Has the same type as `context_dense_defaults`.
    feature_list_sparse_indices: A list of `Nfeature_list_sparse` `Tensor` objects with type `int64`.
    feature_list_sparse_values: A list of `Tensor` objects of type `feature_list_sparse_types`.
    feature_list_sparse_shapes: A list of `Nfeature_list_sparse` `Tensor` objects with type `int64`.
    feature_list_dense_values: A list of `Tensor` objects of type `feature_list_dense_types`.
    feature_list_dense_lengths: A list of `Nfeature_list_dense` `Tensor` objects with type `int64`.
  """

ParseSequenceExample: Incomplete

def parse_sequence_example_eager_fallback(serialized, debug_name, context_dense_defaults, feature_list_dense_missing_assumed_empty, context_sparse_keys, context_dense_keys, feature_list_sparse_keys, feature_list_dense_keys, Ncontext_sparse, Ncontext_dense, Nfeature_list_sparse, Nfeature_list_dense, context_sparse_types, feature_list_dense_types, context_dense_shapes, feature_list_sparse_types, feature_list_dense_shapes, name, ctx): ...

class _ParseSequenceExampleV2Output(NamedTuple):
    context_sparse_indices: Incomplete
    context_sparse_values: Incomplete
    context_sparse_shapes: Incomplete
    context_dense_values: Incomplete
    context_ragged_values: Incomplete
    context_ragged_row_splits: Incomplete
    feature_list_sparse_indices: Incomplete
    feature_list_sparse_values: Incomplete
    feature_list_sparse_shapes: Incomplete
    feature_list_dense_values: Incomplete
    feature_list_dense_lengths: Incomplete
    feature_list_ragged_values: Incomplete
    feature_list_ragged_outer_splits: Incomplete
    feature_list_ragged_inner_splits: Incomplete

def parse_sequence_example_v2(serialized, debug_name, context_sparse_keys, context_dense_keys, context_ragged_keys, feature_list_sparse_keys, feature_list_dense_keys, feature_list_ragged_keys, feature_list_dense_missing_assumed_empty, context_dense_defaults, Ncontext_sparse: int = 0, context_sparse_types=[], context_ragged_value_types=[], context_ragged_split_types=[], context_dense_shapes=[], Nfeature_list_sparse: int = 0, Nfeature_list_dense: int = 0, feature_list_dense_types=[], feature_list_sparse_types=[], feature_list_ragged_value_types=[], feature_list_ragged_split_types=[], feature_list_dense_shapes=[], name: Incomplete | None = None):
    """Transforms a vector of tf.io.SequenceExample protos (as strings) into
typed tensors.

  Args:
    serialized: A `Tensor` of type `string`.
      A scalar or vector containing binary serialized SequenceExample protos.
    debug_name: A `Tensor` of type `string`.
      A scalar or vector containing the names of the serialized protos.
      May contain, for example, table key (descriptive) name for the
      corresponding serialized proto.  This is purely useful for debugging
      purposes, and the presence of values here has no effect on the output.
      May also be an empty vector if no name is available.
    context_sparse_keys: A `Tensor` of type `string`.
      The keys expected in the Examples' features associated with context_sparse
      values.
    context_dense_keys: A `Tensor` of type `string`.
      The keys expected in the SequenceExamples' context features associated with
      dense values.
    context_ragged_keys: A `Tensor` of type `string`.
      The keys expected in the Examples' features associated with context_ragged
      values.
    feature_list_sparse_keys: A `Tensor` of type `string`.
      The keys expected in the FeatureLists associated with sparse values.
    feature_list_dense_keys: A `Tensor` of type `string`.
      The keys expected in the SequenceExamples' feature_lists associated
      with lists of dense values.
    feature_list_ragged_keys: A `Tensor` of type `string`.
      The keys expected in the FeatureLists associated with ragged values.
    feature_list_dense_missing_assumed_empty: A `Tensor` of type `bool`.
      A vector corresponding 1:1 with feature_list_dense_keys, indicating which
      features may be missing from the SequenceExamples.  If the associated
      FeatureList is missing, it is treated as empty.
    context_dense_defaults: A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
      A list of Ncontext_dense Tensors (some may be empty).
      context_dense_defaults[j] provides default values
      when the SequenceExample's context map lacks context_dense_key[j].
      If an empty Tensor is provided for context_dense_defaults[j],
      then the Feature context_dense_keys[j] is required.
      The input type is inferred from context_dense_defaults[j], even when it's
      empty.  If context_dense_defaults[j] is not empty, its shape must match
      context_dense_shapes[j].
    Ncontext_sparse: An optional `int` that is `>= 0`. Defaults to `0`.
    context_sparse_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      A list of Ncontext_sparse types; the data types of data in
      each context Feature given in context_sparse_keys.
      Currently the ParseSingleSequenceExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    context_ragged_value_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      RaggedTensor.value dtypes for the ragged context features.
    context_ragged_split_types: An optional list of `tf.DTypes` from: `tf.int32, tf.int64`. Defaults to `[]`.
      RaggedTensor.row_split dtypes for the ragged context features.
    context_dense_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
      A list of Ncontext_dense shapes; the shapes of data in
      each context Feature given in context_dense_keys.
      The number of elements in the Feature corresponding to context_dense_key[j]
      must always equal context_dense_shapes[j].NumEntries().
      The shape of context_dense_values[j] will match context_dense_shapes[j].
    Nfeature_list_sparse: An optional `int` that is `>= 0`. Defaults to `0`.
    Nfeature_list_dense: An optional `int` that is `>= 0`. Defaults to `0`.
    feature_list_dense_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
    feature_list_sparse_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      A list of Nfeature_list_sparse types; the data types
      of data in each FeatureList given in feature_list_sparse_keys.
      Currently the ParseSingleSequenceExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    feature_list_ragged_value_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      RaggedTensor.value dtypes for the ragged FeatureList features.
    feature_list_ragged_split_types: An optional list of `tf.DTypes` from: `tf.int32, tf.int64`. Defaults to `[]`.
      RaggedTensor.row_split dtypes for the ragged FeatureList features.
    feature_list_dense_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
      A list of Nfeature_list_dense shapes; the shapes of
      data in each FeatureList given in feature_list_dense_keys.
      The shape of each Feature in the FeatureList corresponding to
      feature_list_dense_key[j] must always equal
      feature_list_dense_shapes[j].NumEntries().
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (context_sparse_indices, context_sparse_values, context_sparse_shapes, context_dense_values, context_ragged_values, context_ragged_row_splits, feature_list_sparse_indices, feature_list_sparse_values, feature_list_sparse_shapes, feature_list_dense_values, feature_list_dense_lengths, feature_list_ragged_values, feature_list_ragged_outer_splits, feature_list_ragged_inner_splits).

    context_sparse_indices: A list of `Ncontext_sparse` `Tensor` objects with type `int64`.
    context_sparse_values: A list of `Tensor` objects of type `context_sparse_types`.
    context_sparse_shapes: A list of `Ncontext_sparse` `Tensor` objects with type `int64`.
    context_dense_values: A list of `Tensor` objects. Has the same type as `context_dense_defaults`.
    context_ragged_values: A list of `Tensor` objects of type `context_ragged_value_types`.
    context_ragged_row_splits: A list of `Tensor` objects of type `context_ragged_split_types`.
    feature_list_sparse_indices: A list of `Nfeature_list_sparse` `Tensor` objects with type `int64`.
    feature_list_sparse_values: A list of `Tensor` objects of type `feature_list_sparse_types`.
    feature_list_sparse_shapes: A list of `Nfeature_list_sparse` `Tensor` objects with type `int64`.
    feature_list_dense_values: A list of `Tensor` objects of type `feature_list_dense_types`.
    feature_list_dense_lengths: A list of `Nfeature_list_dense` `Tensor` objects with type `int64`.
    feature_list_ragged_values: A list of `Tensor` objects of type `feature_list_ragged_value_types`.
    feature_list_ragged_outer_splits: A list of `Tensor` objects of type `feature_list_ragged_split_types`.
    feature_list_ragged_inner_splits: A list of `Tensor` objects of type `feature_list_ragged_split_types`.
  """

ParseSequenceExampleV2: Incomplete

def parse_sequence_example_v2_eager_fallback(serialized, debug_name, context_sparse_keys, context_dense_keys, context_ragged_keys, feature_list_sparse_keys, feature_list_dense_keys, feature_list_ragged_keys, feature_list_dense_missing_assumed_empty, context_dense_defaults, Ncontext_sparse, context_sparse_types, context_ragged_value_types, context_ragged_split_types, context_dense_shapes, Nfeature_list_sparse, Nfeature_list_dense, feature_list_dense_types, feature_list_sparse_types, feature_list_ragged_value_types, feature_list_ragged_split_types, feature_list_dense_shapes, name, ctx): ...

class _ParseSingleExampleOutput(NamedTuple):
    sparse_indices: Incomplete
    sparse_values: Incomplete
    sparse_shapes: Incomplete
    dense_values: Incomplete

def parse_single_example(serialized, dense_defaults, num_sparse, sparse_keys, dense_keys, sparse_types, dense_shapes, name: Incomplete | None = None):
    """Transforms a tf.Example proto (as a string) into typed tensors.

  Args:
    serialized: A `Tensor` of type `string`.
      A vector containing a batch of binary serialized Example protos.
    dense_defaults: A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
      A list of Tensors (some may be empty), whose length matches
      the length of `dense_keys`. dense_defaults[j] provides default values
      when the example's feature_map lacks dense_key[j].  If an empty Tensor is
      provided for dense_defaults[j], then the Feature dense_keys[j] is required.
      The input type is inferred from dense_defaults[j], even when it's empty.
      If dense_defaults[j] is not empty, and dense_shapes[j] is fully defined,
      then the shape of dense_defaults[j] must match that of dense_shapes[j].
      If dense_shapes[j] has an undefined major dimension (variable strides dense
      feature), dense_defaults[j] must contain a single element:
      the padding element.
    num_sparse: An `int` that is `>= 0`.
      The number of sparse features to be parsed from the example. This
      must match the lengths of `sparse_keys` and `sparse_types`.
    sparse_keys: A list of `strings`. A list of `num_sparse` strings.
      The keys expected in the Examples' features associated with sparse values.
    dense_keys: A list of `strings`.
      The keys expected in the Examples' features associated with dense
      values.
    sparse_types: A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
      A list of `num_sparse` types; the data types of data in each
      Feature given in sparse_keys.
      Currently the ParseSingleExample op supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    dense_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`).
      The shapes of data in each Feature given in dense_keys.
      The length of this list must match the length of `dense_keys`.  The
      number of elements in the Feature corresponding to dense_key[j] must
      always equal dense_shapes[j].NumEntries().  If dense_shapes[j] ==
      (D0, D1, ..., DN) then the shape of output Tensor dense_values[j]
      will be (D0, D1, ..., DN): In the case dense_shapes[j] = (-1, D1,
      ..., DN), the shape of the output Tensor dense_values[j] will be (M,
      D1, .., DN), where M is the number of blocks of elements of length
      D1 * .... * DN, in the input.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sparse_indices, sparse_values, sparse_shapes, dense_values).

    sparse_indices: A list of `num_sparse` `Tensor` objects with type `int64`.
    sparse_values: A list of `Tensor` objects of type `sparse_types`.
    sparse_shapes: A list of `num_sparse` `Tensor` objects with type `int64`.
    dense_values: A list of `Tensor` objects. Has the same type as `dense_defaults`.
  """

ParseSingleExample: Incomplete

def parse_single_example_eager_fallback(serialized, dense_defaults, num_sparse, sparse_keys, dense_keys, sparse_types, dense_shapes, name, ctx): ...

class _ParseSingleSequenceExampleOutput(NamedTuple):
    context_sparse_indices: Incomplete
    context_sparse_values: Incomplete
    context_sparse_shapes: Incomplete
    context_dense_values: Incomplete
    feature_list_sparse_indices: Incomplete
    feature_list_sparse_values: Incomplete
    feature_list_sparse_shapes: Incomplete
    feature_list_dense_values: Incomplete

def parse_single_sequence_example(serialized, feature_list_dense_missing_assumed_empty, context_sparse_keys, context_dense_keys, feature_list_sparse_keys, feature_list_dense_keys, context_dense_defaults, debug_name, context_sparse_types=[], feature_list_dense_types=[], context_dense_shapes=[], feature_list_sparse_types=[], feature_list_dense_shapes=[], name: Incomplete | None = None):
    """Transforms a scalar brain.SequenceExample proto (as strings) into typed tensors.

  Args:
    serialized: A `Tensor` of type `string`.
      A scalar containing a binary serialized SequenceExample proto.
    feature_list_dense_missing_assumed_empty: A `Tensor` of type `string`.
      A vector listing the
      FeatureList keys which may be missing from the SequenceExample.  If the
      associated FeatureList is missing, it is treated as empty.  By default,
      any FeatureList not listed in this vector must exist in the SequenceExample.
    context_sparse_keys: A list of `Tensor` objects with type `string`.
      A list of Ncontext_sparse string Tensors (scalars).
      The keys expected in the Examples' features associated with context_sparse
      values.
    context_dense_keys: A list of `Tensor` objects with type `string`.
      A list of Ncontext_dense string Tensors (scalars).
      The keys expected in the SequenceExamples' context features associated with
      dense values.
    feature_list_sparse_keys: A list of `Tensor` objects with type `string`.
      A list of Nfeature_list_sparse string Tensors
      (scalars).  The keys expected in the FeatureLists associated with sparse
      values.
    feature_list_dense_keys: A list of `Tensor` objects with type `string`.
      A list of Nfeature_list_dense string Tensors (scalars).
      The keys expected in the SequenceExamples' feature_lists associated
      with lists of dense values.
    context_dense_defaults: A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
      A list of Ncontext_dense Tensors (some may be empty).
      context_dense_defaults[j] provides default values
      when the SequenceExample's context map lacks context_dense_key[j].
      If an empty Tensor is provided for context_dense_defaults[j],
      then the Feature context_dense_keys[j] is required.
      The input type is inferred from context_dense_defaults[j], even when it's
      empty.  If context_dense_defaults[j] is not empty, its shape must match
      context_dense_shapes[j].
    debug_name: A `Tensor` of type `string`.
      A scalar containing the name of the serialized proto.
      May contain, for example, table key (descriptive) name for the
      corresponding serialized proto.  This is purely useful for debugging
      purposes, and the presence of values here has no effect on the output.
      May also be an empty scalar if no name is available.
    context_sparse_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      A list of Ncontext_sparse types; the data types of data in
      each context Feature given in context_sparse_keys.
      Currently the ParseSingleSequenceExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    feature_list_dense_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
    context_dense_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
      A list of Ncontext_dense shapes; the shapes of data in
      each context Feature given in context_dense_keys.
      The number of elements in the Feature corresponding to context_dense_key[j]
      must always equal context_dense_shapes[j].NumEntries().
      The shape of context_dense_values[j] will match context_dense_shapes[j].
    feature_list_sparse_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      A list of Nfeature_list_sparse types; the data types
      of data in each FeatureList given in feature_list_sparse_keys.
      Currently the ParseSingleSequenceExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    feature_list_dense_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
      A list of Nfeature_list_dense shapes; the shapes of
      data in each FeatureList given in feature_list_dense_keys.
      The shape of each Feature in the FeatureList corresponding to
      feature_list_dense_key[j] must always equal
      feature_list_dense_shapes[j].NumEntries().
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (context_sparse_indices, context_sparse_values, context_sparse_shapes, context_dense_values, feature_list_sparse_indices, feature_list_sparse_values, feature_list_sparse_shapes, feature_list_dense_values).

    context_sparse_indices: A list with the same length as `context_sparse_keys` of `Tensor` objects with type `int64`.
    context_sparse_values: A list of `Tensor` objects of type `context_sparse_types`.
    context_sparse_shapes: A list with the same length as `context_sparse_keys` of `Tensor` objects with type `int64`.
    context_dense_values: A list of `Tensor` objects. Has the same type as `context_dense_defaults`.
    feature_list_sparse_indices: A list with the same length as `feature_list_sparse_keys` of `Tensor` objects with type `int64`.
    feature_list_sparse_values: A list of `Tensor` objects of type `feature_list_sparse_types`.
    feature_list_sparse_shapes: A list with the same length as `feature_list_sparse_keys` of `Tensor` objects with type `int64`.
    feature_list_dense_values: A list of `Tensor` objects of type `feature_list_dense_types`.
  """

ParseSingleSequenceExample: Incomplete

def parse_single_sequence_example_eager_fallback(serialized, feature_list_dense_missing_assumed_empty, context_sparse_keys, context_dense_keys, feature_list_sparse_keys, feature_list_dense_keys, context_dense_defaults, debug_name, context_sparse_types, feature_list_dense_types, context_dense_shapes, feature_list_sparse_types, feature_list_dense_shapes, name, ctx): ...
def parse_tensor(serialized, out_type, name: Incomplete | None = None):
    """Transforms a serialized tensorflow.TensorProto proto into a Tensor.

  Args:
    serialized: A `Tensor` of type `string`.
      A scalar string containing a serialized TensorProto proto.
    out_type: A `tf.DType`.
      The type of the serialized tensor.  The provided type must match the
      type of the serialized tensor and no implicit conversion will take place.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `out_type`.
  """

ParseTensor: Incomplete

def parse_tensor_eager_fallback(serialized, out_type, name, ctx): ...
def serialize_tensor(tensor, name: Incomplete | None = None):
    """Transforms a Tensor into a serialized TensorProto proto.

  Args:
    tensor: A `Tensor`. A Tensor of type `T`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

SerializeTensor: Incomplete

def serialize_tensor_eager_fallback(tensor, name, ctx): ...
def string_to_number(string_tensor, out_type=..., name: Incomplete | None = None):
    '''Converts each string in the input Tensor to the specified numeric type.

  (Note that int32 overflow results in an error while float overflow
  results in a rounded value.)

  Example:

  >>> strings = ["5.0", "3.0", "7.0"]
  >>> tf.strings.to_number(strings)
  <tf.Tensor: shape=(3,), dtype=float32, numpy=array([5., 3., 7.], dtype=float32)>

  Args:
    string_tensor: A `Tensor` of type `string`.
    out_type: An optional `tf.DType` from: `tf.float32, tf.float64, tf.int32, tf.int64`. Defaults to `tf.float32`.
      The numeric type to interpret each string in `string_tensor` as.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `out_type`.
  '''

StringToNumber: Incomplete

def string_to_number_eager_fallback(string_tensor, out_type, name, ctx): ...
