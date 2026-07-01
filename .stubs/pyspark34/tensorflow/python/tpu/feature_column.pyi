from _typeshed import Incomplete
from tensorflow.python.feature_column import feature_column as fc
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, variable_scope as variable_scope
from tensorflow.python.tpu import tpu as tpu, tpu_function as tpu_function

def embedding_column(categorical_column, dimension, combiner: str = 'mean', initializer: Incomplete | None = None, max_sequence_length: int = 0, learning_rate_fn: Incomplete | None = None, use_safe_embedding_lookup: bool = True):
    """TPU embedding_column for `tf.feature_column.embedding_column`.

  Note that the interface for TPU embedding_column is different from the non-TPU
  version. The following args available for the non-TPU version are NOT
  supported: ckpt_to_load_from, tensor_name_in_ckp, max_norm and trainable.

  Args:
    categorical_column: A categorical_column returned from
        categorical_column_with_identity, weighted_categorical_column,
        categorical_column_with_vocabulary_file,
        categorical_column_with_vocabulary_list,
        sequence_categorical_column_with_identity,
        sequence_categorical_column_with_vocabulary_file,
        sequence_categorical_column_with_vocabulary_list
    dimension: An integer specifying dimension of the embedding, must be > 0.
    combiner: A string specifying how to reduce if there are multiple entries
      in a single row for a non-sequence column. For more information, see
      `tf.feature_column.embedding_column`.
    initializer: A variable initializer function to be used in embedding
      variable initialization. If not specified, defaults to
      `tf.compat.v1.truncated_normal_initializer` with mean `0.0` and
      standard deviation `1/sqrt(dimension)`.
    max_sequence_length: An non-negative integer specifying the max sequence
      length. Any sequence shorter then this will be padded with 0 embeddings
      and any sequence longer will be truncated. This must be positive for
      sequence features and 0 for non-sequence features.
    learning_rate_fn: A function that takes global step and returns learning
      rate for the embedding table. If you intend to use the same learning rate
      for multiple embedding tables, please ensure that you pass the exact same
      python function to all calls of embedding_column, otherwise performence
      may suffer.
    use_safe_embedding_lookup: If true, uses safe_embedding_lookup_sparse
      instead of embedding_lookup_sparse. safe_embedding_lookup_sparse ensures
      there are no empty rows and all weights and ids are positive at the
      expense of extra compute cost. This only applies to rank 2 (NxM) shaped
      input tensors. Defaults to true, consider turning off if the above checks
      are not needed. Note that having empty rows will not trigger any error
      though the output result might be 0 or omitted.

  Returns:
    A  _TPUEmbeddingColumn.

  Raises:
    ValueError: if `dimension` not > 0.
    ValueError: if `initializer` is specified but not callable.
    TypeError: if categorical_column is not a supported type.
  """
def shared_embedding_columns(categorical_columns, dimension, combiner: str = 'mean', initializer: Incomplete | None = None, shared_embedding_collection_name: Incomplete | None = None, max_sequence_lengths: Incomplete | None = None, learning_rate_fn: Incomplete | None = None, use_safe_embedding_lookup: bool = True):
    """List of dense columns that convert from sparse, categorical input.

  Note that the interface for TPU embedding_column is different from the non-TPU
  version. The following args available for the non-TPU version are NOT
  supported: ckpt_to_load_from, tensor_name_in_ckp, max_norm and trainable.

  Args:
    categorical_columns: A list of categorical_columns returned from
        categorical_column_with_identity, weighted_categorical_column,
        categorical_column_with_vocabulary_file,
        categorical_column_with_vocabulary_list,
        sequence_categorical_column_with_identity,
        sequence_categorical_column_with_vocabulary_file,
        sequence_categorical_column_with_vocabulary_list
    dimension: An integer specifying dimension of the embedding, must be > 0.
    combiner: A string specifying how to reduce if there are multiple entries
      in a single row for a non-sequence column. For more information, see
      `tf.feature_column.embedding_column`.
    initializer: A variable initializer function to be used in embedding
      variable initialization. If not specified, defaults to
      `tf.truncated_normal_initializer` with mean `0.0` and standard deviation
      `1/sqrt(dimension)`.
    shared_embedding_collection_name: Optional name of the collection where
      shared embedding weights are added. If not given, a reasonable name will
      be chosen based on the names of `categorical_columns`. This is also used
      in `variable_scope` when creating shared embedding weights.
    max_sequence_lengths: An list of non-negative integers, either None or
      empty or the same length as the argument categorical_columns. Entries
      corresponding to non-sequence columns must be 0 and entries corresponding
      to sequence columns specify the max sequence length for the column. Any
      sequence shorter then this will be padded with 0 embeddings and any
      sequence longer will be truncated.
    learning_rate_fn: A function that takes global step and returns learning
      rate for the embedding table. If you intend to use the same learning rate
      for multiple embedding tables, please ensure that you pass the exact same
      python function to all calls of shared_embedding_columns, otherwise
      performence may suffer.
    use_safe_embedding_lookup: If true, uses safe_embedding_lookup_sparse
      instead of embedding_lookup_sparse. safe_embedding_lookup_sparse ensures
      there are no empty rows and all weights and ids are positive at the
      expense of extra compute cost. This only applies to rank 2 (NxM) shaped
      input tensors. Defaults to true, consider turning off if the above checks
      are not needed. Note that having empty rows will not trigger any error
      though the output result might be 0 or omitted.

  Returns:
    A  _TPUEmbeddingColumn.

  Raises:
    ValueError: if `dimension` not > 0.
    ValueError: if `initializer` is specified but not callable.
    ValueError: if `max_sequence_lengths` is specified and not the same length
      as `categorical_columns`.
    ValueError: if `max_sequence_lengths` is positive for a non sequence column
      or 0 for a sequence column.
  """

class _TPUBaseEmbeddingColumn:
    """Base class for TPU Embedding Column."""
    def __init__(self, categorical_column, max_sequence_length: int = 0, learning_rate_fn: Incomplete | None = None) -> None: ...
    def get_combiner(self) -> None:
        """Returns the embedding combiner."""
    def get_embedding_table_size(self) -> None:
        """Returns the embedding table size, tuple of vocab size and dimension."""
    def get_feature_key_name(self) -> None:
        """Returns the feature key name in the features dict."""
    def get_weight_key_name(self) -> None:
        """Return the key name for weights."""
    def get_embedding_var_name(self) -> None:
        """Returns the embedding variable name.

    Feature key name and embedding variable name are usually one-to-one mapping.
    But for shared embedding columns, it is many-to-one mapping.
    """
    def get_initializer(self) -> None:
        """Returns the initializer."""
    def is_categorical_column_weighted(self) -> None:
        """Check if the categorical column of the embedding column is weighted."""
    def is_sequence_column(self): ...
    def get_max_sequence_length(self): ...
    def get_learning_rate_fn(self): ...
    def get_sequence_length_feature_key_name(self):
        """Get the key for the associated sequence length feature."""

class _TPUEmbeddingColumn(_TPUBaseEmbeddingColumn, fc._EmbeddingColumn):
    """Core Embedding Column."""
    def __new__(cls, categorical_column, dimension, combiner: str = 'mean', layer_creator: Incomplete | None = None, ckpt_to_load_from: Incomplete | None = None, tensor_name_in_ckpt: Incomplete | None = None, max_norm: Incomplete | None = None, trainable: bool = True, max_sequence_length: int = 0, learning_rate_fn: Incomplete | None = None, use_safe_embedding_lookup: bool = True, bypass_scope_validation: bool = False): ...
    def __init__(self, categorical_column, dimension, combiner: str = 'mean', layer_creator: Incomplete | None = None, ckpt_to_load_from: Incomplete | None = None, tensor_name_in_ckpt: Incomplete | None = None, max_norm: Incomplete | None = None, trainable: bool = True, max_sequence_length: int = 0, learning_rate_fn: Incomplete | None = None, use_safe_embedding_lookup: bool = True, bypass_scope_validation: bool = False) -> None: ...
    def get_combiner(self): ...
    def get_embedding_table_size(self):
        """Returns num_ids and width."""
    def get_feature_key_name(self):
        """get_feature_key_name."""
    def get_weight_key_name(self):
        """get_weight_key_name."""
    def get_embedding_var_name(self):
        """get_embedding_var_name."""
    def get_initializer(self): ...
    def is_categorical_column_weighted(self):
        """Check if the categorical column of the embedding column is weighted."""

class _TPUSharedEmbeddingColumn(_TPUBaseEmbeddingColumn, fc._SharedEmbeddingColumn):
    """Core Shared Embedding Column."""
    def __new__(cls, categorical_column, dimension, combiner: str = 'mean', initializer: Incomplete | None = None, shared_embedding_collection_name: Incomplete | None = None, ckpt_to_load_from: Incomplete | None = None, tensor_name_in_ckpt: Incomplete | None = None, max_norm: Incomplete | None = None, trainable: bool = True, max_sequence_length: int = 0, learning_rate_fn: Incomplete | None = None, use_safe_embedding_lookup: bool = True): ...
    def __init__(self, categorical_column, dimension, combiner: str = 'mean', initializer: Incomplete | None = None, shared_embedding_collection_name: Incomplete | None = None, ckpt_to_load_from: Incomplete | None = None, tensor_name_in_ckpt: Incomplete | None = None, max_norm: Incomplete | None = None, trainable: bool = True, max_sequence_length: int = 0, learning_rate_fn: Incomplete | None = None, use_safe_embedding_lookup: bool = True) -> None: ...
    def get_combiner(self): ...
    def get_embedding_table_size(self):
        """Returns num_ids and width."""
    def get_feature_key_name(self):
        """get_feature_key_name."""
    def get_weight_key_name(self):
        """get_weight_key_name."""
    def get_embedding_var_name(self):
        """get_embedding_var_name."""
    def get_initializer(self): ...
    def is_categorical_column_weighted(self):
        """Check if the categorical column of the embedding column is weighted."""

def get_sequence_length_feature_key_name_from_feature_key_name(feature_name):
    """Gets the name of the sequence length feature from that of the base feature.

  Args:
    feature_name: The feature key of a sequence column.

  Returns:
    A string which is the feature key for the associated feature length column.
  """
def split_sequence_columns(feature_columns):
    """Split a list of _TPUEmbeddingColumn into sequence and non-sequence columns.

  For use in a TPUEstimator model_fn function. E.g.

  def model_fn(features):
    sequence_columns, feature_columns = (
        tf.tpu.feature_column.split_sequence_columns(feature_columns))
    input = tf.feature_column.input_layer(
        features=features, feature_columns=feature_columns)
    sequence_features, sequence_lengths = (
        tf.contrib.feature_column.sequence_input_layer(
            features=features, feature_columns=sequence_columns))

  Args:
    feature_columns: A list of _TPUEmbeddingColumns to split.

  Returns:
    Two lists of _TPUEmbeddingColumns, the first is the sequence columns and the
    second is the non-sequence columns.
  """
