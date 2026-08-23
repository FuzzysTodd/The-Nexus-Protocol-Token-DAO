from tensorflow.python.ops.gen_tpu_ops import *
from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_tpu_ops as gen_tpu_ops
from tensorflow.python.tpu import tpu_function as tpu_function
from tensorflow.python.util.tf_export import tf_export as tf_export

def all_to_all(x, concat_dimension, split_dimension, split_count, group_assignment: Incomplete | None = None, name: Incomplete | None = None):
    """Exchange data across TPU replicas.

  Args:
    x: The local tensor.
    concat_dimension: The dimension number to concatenate.
    split_dimension: The dimension number to split.
    split_count: The number of splits, this number must equal to the sub-group
      size(group_assignment.get_shape()[1])
    group_assignment: Optional 2d int32 lists with shape [num_groups,
      num_replicas_per_group]. `group_assignment[i]` represents the replica ids
      in the ith subgroup.
    name: Optional op name.

  Returns:
    A `Tensor` which is concatenated by data from different replicas.
  """
def cross_replica_sum(x, group_assignment: Incomplete | None = None, name: Incomplete | None = None):
    """Sum the input tensor across replicas according to group_assignment.

  Args:
    x: The local tensor to the sum.
    group_assignment: Optional 2d int32 lists with shape [num_groups,
      num_replicas_per_group]. `group_assignment[i]` represents the replica ids
      in the ith subgroup.
    name: Optional op name.

  Returns:
    A `Tensor` which is summed across replicas.
  """
def collective_permute(x, source_target_pairs, name: Incomplete | None = None):
    """Permute the input tensor across replicas given source_target_pairs.

  For each source_target_pair <a, b>, we send replica a's input to replica b.
  Each replica id must only appear once in the source column. Also it must
  only appear once in the target column.
  For the replica id not in the target column, this op returns a zero tensor
  with the same shape and dtype of the input x.

  For example, suppose there are 4 TPU instances: `[A, B, C, D]`. Passing
  source_target_pairs=`[[0,1],[1,2],[2,3]]` gets the outputs:
  `[0, A, B, C]`.

  Args:
    x: The local tensor to be permuted.
    source_target_pairs: 2d int lists with shape [num_pairs, 2].
      source_target_pairs[i][0] represents the source replica id and
      source_target_pairs[i][1] represents the target replica id.
    name: Optional op name.

  Returns:
    A `Tensor` which is permuted.
  """
def infeed_dequeue(dtype, shape, name: Incomplete | None = None):
    """A placeholder op for a value that will be fed into the computation.

  Args:
    dtype: A `tf.DType`. The type of elements in the tensor.
    shape: A `tf.TensorShape` or list of `ints`. The shape of the tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
    A tensor that will be provided using the infeed mechanism.

  Raises:
    TypeError: If 'dtype` is not a supported infeed type.
  """
def infeed_dequeue_tuple(dtypes, shapes, name: Incomplete | None = None):
    """A placeholder op for values fed into the TPU simultaneously as a tuple.

  Args:
    dtypes: A list of `tf.DType`s that has length `>= 1`. The element types of
      each element in `outputs`.
    shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`). The
      shapes of each tensor in `outputs`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `dtypes`.
    A list of tensors that will be provided using the infeed mechanism.

  Raises:
    TypeError: If a type in 'dtypes` is not a supported infeed type.
  """
def send_tpu_embedding_gradients(inputs, config, learning_rates: Incomplete | None = None, name: Incomplete | None = None):
    """A placeholder op for feeding per-sample gradients to the embedding layer.

  Args:
    inputs: A TensorList of gradients with which to update embedding tables.
      This argument has the same length and shapes as the return value of
      RecvTPUEmbeddingActivations, but contains gradients of the model's loss
      with respect to the embedding activations. The embedding tables are
      updated from these gradients via the optimizers specified in the TPU
      embedding configuration given to tpu.initialize_system.
    config: Serialized TPUEmbeddingConfiguration proto.
    learning_rates: A TensorList of float32 scalars, one for each dynamic
        learning rate tag: see the comments in
          //third_party/tensorflow/core/protobuf/tpu/
          optimization_parameters.proto. Multiple tables can share the same
          dynamic learning rate tag as specified in the configuration. If the
          learning rates for all tables are constant, this list should be empty.
    name: A name for the operation (optional).

  Returns:
    A SendTPUEmbeddingGradients operation.
  """
def enqueue_tpu_embedding_integer_batch(batch, device_ordinal, mode_override: Incomplete | None = None, name: Incomplete | None = None):
    """A placeholder op for enqueueing embedding IDs to the TPU.

  Args:
    batch: A list of 1D tensors, one for each embedding table, containing the
      indices into the tables.
    device_ordinal: The TPU device to use. Should be >= 0 and less than the
      number of TPU cores in the task on which the node is placed.
    mode_override: A string input that overrides the mode specified in the
      TPUEmbeddingConfiguration. Supported values are {'unspecified',
      'inference', 'train', 'backward_pass_only'}. When set to 'unspecified',
      the mode set in TPUEmbeddingConfiguration is used, otherwise mode_override
      is used (optional).
    name: A name for the operation (optional).

  Returns:
    An EnqueueTPUEmbeddingIntegerBatch operation.
  """
def enqueue_tpu_embedding_sparse_batch(sample_indices, embedding_indices, aggregation_weights, device_ordinal, combiners: Incomplete | None = None, mode_override: Incomplete | None = None, name: Incomplete | None = None):
    """A placeholder op for enqueueing embedding IDs to the TPU.

  Args:
    sample_indices: A list of rank 1 Tensors specifying the training example and
      feature to which the corresponding embedding_indices and
      aggregation_weights values belong. sample_indices[i] must equal b * nf +
      f, where nf is the number of features from the corresponding table, f is
      in [0, nf), and b is in [0, batch size). Both int32 and int64 are allowed,
      and will be converted to int32 internally.
    embedding_indices: A list of rank 1 Tensors, indices into the embedding
      tables. Both int32 and int64 are allowed and will be converted to int32
      internally.
    aggregation_weights: A list of rank 1 Tensors containing per sample -- i.e.,
      per (training example, feature) -- aggregation weights. Both float32 and
      float64 are allowed and will be converted to float32 internally.
    device_ordinal: The TPU device to use. Should be >= 0 and less than the
      number of TPU cores in the task on which the node is placed.
    combiners: A list of string scalars, one for each embedding table that
      specify how to normalize the embedding activations after weighted
      summation. Supported combiners are 'mean', 'sum', or 'sqrtn'. It is
      invalid to have the sum of the weights be 0 for 'mean' or the sum of the
      squared weights be 0 for 'sqrtn'. If combiners isn't passed, the default
      is to use 'sum' for all tables (optional).
    mode_override: A string input that overrides the mode specified in the
      TPUEmbeddingConfiguration. Supported values are {'unspecified',
      'inference', 'train', 'backward_pass_only'}. When set to 'unspecified',
      the mode set in TPUEmbeddingConfiguration is used, otherwise mode_override
      is used (optional).
    name: A name for the operation (optional).

  Returns:
    An EnqueueTPUEmbeddingSparseBatch operation.
  """
def enqueue_tpu_embedding_sparse_tensor_batch(sample_indices, embedding_indices, aggregation_weights, table_ids, device_ordinal, max_sequence_lengths: Incomplete | None = None, num_features: Incomplete | None = None, combiners: Incomplete | None = None, mode_override: Incomplete | None = None, name: Incomplete | None = None):
    """A placeholder op for enqueueing embedding IDs to the TPU.

  Args:
    sample_indices: A list of rank 2 Tensors specifying the training example to
      which the corresponding embedding_indices and aggregation_weights values
      belong. It corresponds to sp_ids.indices in embedding_lookup_sparse(). If
      the size of its first dimension is 0, we assume each embedding_indices
      belongs to a different sample. Both int32 and int64 are allowed and will
      be converted to int32 internally.
    embedding_indices: A list of rank 1 Tensors, indices into the embedding
      tables. It corresponds to sp_ids.values in embedding_lookup_sparse(). Both
      int32 and int64 are allowed and will be converted to int32 internally.
    aggregation_weights: A list of rank 1 Tensors containing per training
      example aggregation weights. It corresponds to sp_weights.values in
      embedding_lookup_sparse(). If the size of its first dimension is 0, we
      assume all weights are 1. Both float32 and float64 are allowed and will be
      converted to float32 internally.
    table_ids: A list of integers specifying the identifier of the embedding
      table (offset of TableDescriptor in the TPUEmbeddingConfiguration) to
      lookup the corresponding input. The ith input is looked up using
      table_ids[i]. The size of the table_ids list must be equal to that of
      sample_indices, embedding_indices and aggregation_weights.
    device_ordinal: The TPU device to use. Should be >= 0 and less than the
      number of TPU cores in the task on which the node is placed.
    max_sequence_lengths: A list of integers, the size of which is equal to
      sample_indices. If equal to 0, the corresponding feature is considered to
      be a non-sequence feature, If greater than 0, the corresponding feature is
      a sequence feature with the given maximal length. If None, then we assume
      a list of all zeroes.
    num_features: A list of integers, the size of which is equal to
      sample_indices. If non-empty, entries in this list must be at least 1. For
      each batch element, we will take num_features rows of the input tensor for
      embedding lookup. E.g., when sample_indices is empty, the embedding
      indices must be of shape (batch_size*num_features).
    combiners: A list of string scalars, one for each embedding table that
      specify how to normalize the embedding activations after weighted
      summation. Supported combiners are 'mean', 'sum', or 'sqrtn'. It is
      invalid to have the sum of the weights be 0 for 'mean' or the sum of the
      squared weights be 0 for 'sqrtn'. If combiners isn't passed, the default
      is to use 'sum' for all tables (optional).
    mode_override: A string input that overrides the mode specified in the
      TPUEmbeddingConfiguration. Supported values are {'unspecified',
      'inference', 'train', 'backward_pass_only'}. When set to 'unspecified',
      the mode set in TPUEmbeddingConfiguration is used, otherwise mode_override
      is used (optional).
    name: A name for the operation (optional).

  Returns:
    An EnqueueTPUEmbeddingSparseTensorBatch operation.
  """
def enqueue_tpu_embedding_ragged_tensor_batch(sample_splits, embedding_indices, aggregation_weights, table_ids, device_ordinal, max_sequence_lengths: Incomplete | None = None, num_features: Incomplete | None = None, combiners: Incomplete | None = None, mode_override: Incomplete | None = None, name: Incomplete | None = None):
    """A placeholder op for enqueueing embedding IDs to the TPU.

  Args:
    sample_splits: A list of rank 1 Tensors specifying the break points for
      splitting embedding_indices and aggregation_weights into rows. It
      corresponds to ids.row_splits in embedding_lookup(), when ids is a
      RaggedTensor. Both int32 and int64 are allowed and will be converted to
      int32 internally.
    embedding_indices: A list of rank 1 Tensors, indices into the embedding
      tables. It corresponds to ids.values in embedding_lookup(), when ids is a
      RaggedTensor. Both int32 and int64 are allowed and will be converted to
      int32 internally.
    aggregation_weights: A list of rank 1 Tensors containing per training
      example aggregation weights. It corresponds to the values field of a
      RaggedTensor with the same row_splits as ids in embedding_lookup(), when
      ids is a RaggedTensor. Both float32 and float64 are allowed and will be
      converted to float32 internally.
    table_ids: A list of integers specifying the identifier of the embedding
      table (offset of TableDescriptor in the TPUEmbeddingConfiguration) to
      lookup the corresponding input. The ith input is looked up using
      table_ids[i]. The size of the table_ids list must be equal to that of
      sample_indices, embedding_indices and aggregation_weights.
    device_ordinal: The TPU device to use. Should be >= 0 and less than the
      number of TPU cores in the task on which the node is placed.
    max_sequence_lengths: A list of integers, the size of which is equal to
      sample_indices. If equal to 0, the corresponding feature is considered to
      be a non-sequence feature, If greater than 0, the corresponding feature is
      a sequence feature with the given maximal length. If None, then we assume
      a list of all zeroes.
    num_features: A list of integers, the size of which must be equal to
      sample_indices. If non-empty, entries in this list must be at least 1. For
      each batch element, we will take num_features rows of the input tensor for
      embedding lookup. E.g., when sample_indices is empty, the embedding
      indices must be of shape (batch_size*num_features).
    combiners: A list of string scalars, one for each embedding table that
      specify how to normalize the embedding activations after weighted
      summation. Supported combiners are 'mean', 'sum', or 'sqrtn'. It is
      invalid to have the sum of the weights be 0 for 'mean' or the sum of the
      squared weights be 0 for 'sqrtn'. If combiners isn't passed, the default
      is to use 'sum' for all tables (optional).
    mode_override: A string input that overrides the mode specified in the
      TPUEmbeddingConfiguration. Supported values are {'unspecified',
      'inference', 'training', 'backward_pass_only'}. When set to 'unspecified',
      the mode set in TPUEmbeddingConfiguration is used, otherwise mode_override
      is used (optional).
    name: A name for the operation (optional).

  Returns:
    An EnqueueTPUEmbeddingRaggedTensorBatch operation.
  """
def enqueue_tpu_embedding_arbitrary_tensor_batch(sample_indices_or_row_splits, embedding_indices, aggregation_weights, device_ordinal, combiners: Incomplete | None = None, mode_override: Incomplete | None = None, name: Incomplete | None = None):
    """A placeholder op for enqueueing embedding IDs to the TPU.

  Args:
    sample_indices_or_row_splits: A list of rank 1 or 2 Tensors. When rank 2,
      the tensors specify the training example to which the corresponding
      embedding_indices and aggregation_weights values belong. If the size of
      its first dimension is 0, we assume each embedding_indices belongs to a
      different sample. Both int32 and int64 are allowed and will be converted
      to int32 internally. When rank 1, the tensors specify the row splits for
      splitting embedding_indices and aggregation_weights into rows. It
      corresponds to ids.row_splits in embedding_lookup(), when ids is a
      RaggedTensor. When enqueuing N-D ragged tensor, only the last dimension is
      allowed to be ragged. the row splits is 1-D dense tensor. When empty, we
      assume a dense tensor is passed to the op. Both int32 and int64 are
      allowed and will be converted to int32 internally.
    embedding_indices: A list of rank 1 Tensors, indices into the embedding
      tables. Both int32 and int64 are allowed and will be converted to int32
      internally.
    aggregation_weights: A list of rank 1 Tensors containing per training
      example aggregation weights. Both float32 and float64 are allowed and will
      be converted to float32 internally.
    device_ordinal: The TPU device to use. Should be >= 0 and less than the
      number of TPU cores in the task on which the node is placed.
    combiners: A list of string scalars, one for each embedding table that
      specify how to normalize the embedding activations after weighted
      summation. Supported combiners are 'mean', 'sum', or 'sqrtn'. It is
      invalid to have the sum of the weights be 0 for 'mean' or the sum of the
      squared weights be 0 for 'sqrtn'. If combiners isn't passed, the default
      is to use 'sum' for all tables (optional).
    mode_override: A string input that overrides the mode specified in the
      TPUEmbeddingConfiguration. Supported values are {'unspecified',
      'inference', 'training', 'backward_pass_only'}. When set to 'unspecified',
      the mode set in TPUEmbeddingConfiguration is used, otherwise mode_override
      is used (optional).
    name: A name for the operation (optional).

  Returns:
    An EnqueueTPUEmbeddingArbitraryTensorBatch operation.
  """
