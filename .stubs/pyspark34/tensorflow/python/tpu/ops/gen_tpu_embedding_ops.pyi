from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def collate_tpu_embedding_memory(memory_configs, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    memory_configs: A list of at least 1 `Tensor` objects with type `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

CollateTPUEmbeddingMemory: Incomplete

def collate_tpu_embedding_memory_eager_fallback(memory_configs, name, ctx): ...
def compute_dedup_data_tuple_mask(config, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    config: A `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

ComputeDedupDataTupleMask: Incomplete

def compute_dedup_data_tuple_mask_eager_fallback(config, name, ctx): ...
def configure_distributed_tpu(embedding_config: str = '', tpu_embedding_config: str = '', is_global_init: bool = False, enable_whole_mesh_compilations: bool = False, compilation_failure_closes_chips: bool = True, tpu_cancellation_closes_chips: int = 0, name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    embedding_config: An optional `string`. Defaults to `""`.
    tpu_embedding_config: An optional `string`. Defaults to `""`.
    is_global_init: An optional `bool`. Defaults to `False`.
    enable_whole_mesh_compilations: An optional `bool`. Defaults to `False`.
    compilation_failure_closes_chips: An optional `bool`. Defaults to `True`.
    tpu_cancellation_closes_chips: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

ConfigureDistributedTPU: Incomplete

def configure_distributed_tpu_eager_fallback(embedding_config, tpu_embedding_config, is_global_init, enable_whole_mesh_compilations, compilation_failure_closes_chips, tpu_cancellation_closes_chips, name, ctx): ...
def configure_tpu_embedding(config, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    config: A `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

ConfigureTPUEmbedding: Incomplete

def configure_tpu_embedding_eager_fallback(config, name, ctx): ...
def configure_tpu_embedding_host(common_config, memory_config, config, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    common_config: A `Tensor` of type `string`.
    memory_config: A `Tensor` of type `string`.
    config: A `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

ConfigureTPUEmbeddingHost: Incomplete

def configure_tpu_embedding_host_eager_fallback(common_config, memory_config, config, name, ctx): ...
def configure_tpu_embedding_memory(common_config, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    common_config: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

ConfigureTPUEmbeddingMemory: Incomplete

def configure_tpu_embedding_memory_eager_fallback(common_config, name, ctx): ...
def connect_tpu_embedding_hosts(network_configs, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    network_configs: A list of at least 1 `Tensor` objects with type `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

ConnectTPUEmbeddingHosts: Incomplete

def connect_tpu_embedding_hosts_eager_fallback(network_configs, name, ctx): ...
def dynamic_enqueue_tpu_embedding_arbitrary_tensor_batch(sample_indices_or_row_splits, embedding_indices, aggregation_weights, mode_override, device_ordinal, combiners=[], name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    sample_indices_or_row_splits: A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`.
    embedding_indices: A list with the same length as `sample_indices_or_row_splits` of `Tensor` objects with the same type in: `int32`, `int64`.
    aggregation_weights: A list with the same length as `sample_indices_or_row_splits` of `Tensor` objects with the same type in: `float32`, `float64`.
    mode_override: A `Tensor` of type `string`.
    device_ordinal: A `Tensor` of type `int32`.
    combiners: An optional list of `strings`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

DynamicEnqueueTPUEmbeddingArbitraryTensorBatch: Incomplete

def dynamic_enqueue_tpu_embedding_arbitrary_tensor_batch_eager_fallback(sample_indices_or_row_splits, embedding_indices, aggregation_weights, mode_override, device_ordinal, combiners, name, ctx): ...
def enqueue_tpu_embedding_arbitrary_tensor_batch(sample_indices_or_row_splits, embedding_indices, aggregation_weights, mode_override, device_ordinal: int = -1, combiners=[], name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    sample_indices_or_row_splits: A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`.
    embedding_indices: A list with the same length as `sample_indices_or_row_splits` of `Tensor` objects with the same type in: `int32`, `int64`.
    aggregation_weights: A list with the same length as `sample_indices_or_row_splits` of `Tensor` objects with the same type in: `float32`, `float64`.
    mode_override: A `Tensor` of type `string`.
    device_ordinal: An optional `int`. Defaults to `-1`.
    combiners: An optional list of `strings`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

EnqueueTPUEmbeddingArbitraryTensorBatch: Incomplete

def enqueue_tpu_embedding_arbitrary_tensor_batch_eager_fallback(sample_indices_or_row_splits, embedding_indices, aggregation_weights, mode_override, device_ordinal, combiners, name, ctx): ...
def enqueue_tpu_embedding_batch(batch, mode_override, device_ordinal: int = -1, combiners=[], name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    batch: A list of at least 1 `Tensor` objects with type `string`.
    mode_override: A `Tensor` of type `string`.
    device_ordinal: An optional `int`. Defaults to `-1`.
    combiners: An optional list of `strings`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

EnqueueTPUEmbeddingBatch: Incomplete

def enqueue_tpu_embedding_batch_eager_fallback(batch, mode_override, device_ordinal, combiners, name, ctx): ...
def enqueue_tpu_embedding_integer_batch(batch, mode_override, device_ordinal: int = -1, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    batch: A list of at least 1 `Tensor` objects with type `int32`.
    mode_override: A `Tensor` of type `string`.
    device_ordinal: An optional `int`. Defaults to `-1`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

EnqueueTPUEmbeddingIntegerBatch: Incomplete

def enqueue_tpu_embedding_integer_batch_eager_fallback(batch, mode_override, device_ordinal, name, ctx): ...
def enqueue_tpu_embedding_ragged_tensor_batch(sample_splits, embedding_indices, aggregation_weights, mode_override, table_ids, device_ordinal: int = -1, combiners=[], max_sequence_lengths=[], num_features=[], name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    sample_splits: A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`.
    embedding_indices: A list with the same length as `sample_splits` of `Tensor` objects with the same type in: `int32`, `int64`.
    aggregation_weights: A list with the same length as `sample_splits` of `Tensor` objects with the same type in: `float32`, `float64`.
    mode_override: A `Tensor` of type `string`.
    table_ids: A list of `ints`.
    device_ordinal: An optional `int`. Defaults to `-1`.
    combiners: An optional list of `strings`. Defaults to `[]`.
    max_sequence_lengths: An optional list of `ints`. Defaults to `[]`.
    num_features: An optional list of `ints`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

EnqueueTPUEmbeddingRaggedTensorBatch: Incomplete

def enqueue_tpu_embedding_ragged_tensor_batch_eager_fallback(sample_splits, embedding_indices, aggregation_weights, mode_override, table_ids, device_ordinal, combiners, max_sequence_lengths, num_features, name, ctx): ...
def enqueue_tpu_embedding_sparse_batch(sample_indices, embedding_indices, aggregation_weights, mode_override, device_ordinal: int = -1, combiners=[], name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    sample_indices: A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`.
    embedding_indices: A list with the same length as `sample_indices` of `Tensor` objects with the same type in: `int32`, `int64`.
    aggregation_weights: A list with the same length as `sample_indices` of `Tensor` objects with the same type in: `float32`, `float64`.
    mode_override: A `Tensor` of type `string`.
    device_ordinal: An optional `int`. Defaults to `-1`.
    combiners: An optional list of `strings`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

EnqueueTPUEmbeddingSparseBatch: Incomplete

def enqueue_tpu_embedding_sparse_batch_eager_fallback(sample_indices, embedding_indices, aggregation_weights, mode_override, device_ordinal, combiners, name, ctx): ...
def enqueue_tpu_embedding_sparse_tensor_batch(sample_indices, embedding_indices, aggregation_weights, mode_override, table_ids, device_ordinal: int = -1, combiners=[], max_sequence_lengths=[], num_features=[], name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    sample_indices: A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`.
    embedding_indices: A list with the same length as `sample_indices` of `Tensor` objects with the same type in: `int32`, `int64`.
    aggregation_weights: A list with the same length as `sample_indices` of `Tensor` objects with the same type in: `float32`, `float64`.
    mode_override: A `Tensor` of type `string`.
    table_ids: A list of `ints`.
    device_ordinal: An optional `int`. Defaults to `-1`.
    combiners: An optional list of `strings`. Defaults to `[]`.
    max_sequence_lengths: An optional list of `ints`. Defaults to `[]`.
    num_features: An optional list of `ints`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

EnqueueTPUEmbeddingSparseTensorBatch: Incomplete

def enqueue_tpu_embedding_sparse_tensor_batch_eager_fallback(sample_indices, embedding_indices, aggregation_weights, mode_override, table_ids, device_ordinal, combiners, max_sequence_lengths, num_features, name, ctx): ...
def execute_tpu_embedding_partitioner(config, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    config: A `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

ExecuteTPUEmbeddingPartitioner: Incomplete

def execute_tpu_embedding_partitioner_eager_fallback(config, name, ctx): ...
def finalize_tpu_embedding(common_config, memory_config, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    common_config: A `Tensor` of type `string`.
    memory_config: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

FinalizeTPUEmbedding: Incomplete

def finalize_tpu_embedding_eager_fallback(common_config, memory_config, name, ctx): ...
def is_tpu_embedding_initialized(config: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    config: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  '''

IsTPUEmbeddingInitialized: Incomplete

def is_tpu_embedding_initialized_eager_fallback(config, name, ctx): ...
def load_all_tpu_embedding_parameters(parameters, auxiliary1, auxiliary2, auxiliary3, auxiliary4, auxiliary5, auxiliary6, auxiliary7, config, num_shards, shard_id, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    parameters: A list of at least 1 `Tensor` objects with type `float32`.
    auxiliary1: A list with the same length as `parameters` of `Tensor` objects with type `float32`.
    auxiliary2: A list with the same length as `parameters` of `Tensor` objects with type `float32`.
    auxiliary3: A list with the same length as `parameters` of `Tensor` objects with type `float32`.
    auxiliary4: A list with the same length as `parameters` of `Tensor` objects with type `float32`.
    auxiliary5: A list with the same length as `parameters` of `Tensor` objects with type `float32`.
    auxiliary6: A list with the same length as `parameters` of `Tensor` objects with type `float32`.
    auxiliary7: A list with the same length as `parameters` of `Tensor` objects with type `float32`.
    config: A `string`.
    num_shards: An `int`.
    shard_id: An `int`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

LoadAllTPUEmbeddingParameters: Incomplete

def load_all_tpu_embedding_parameters_eager_fallback(parameters, auxiliary1, auxiliary2, auxiliary3, auxiliary4, auxiliary5, auxiliary6, auxiliary7, config, num_shards, shard_id, name, ctx): ...
def merge_dedup_data(integer_tensor, float_tensor, tuple_mask, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    integer_tensor: A `Tensor`. Must be one of the following types: `int32`, `int64`, `uint32`, `uint64`.
    float_tensor: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`.
    tuple_mask: A `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

MergeDedupData: Incomplete

def merge_dedup_data_eager_fallback(integer_tensor, float_tensor, tuple_mask, name, ctx): ...
def recv_tpu_embedding_activations(num_outputs, config, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    num_outputs: An `int` that is `>= 1`.
    config: A `string`.
    name: A name for the operation (optional).

  Returns:
    A list of `num_outputs` `Tensor` objects with type `float32`.
  """

RecvTPUEmbeddingActivations: Incomplete

def recv_tpu_embedding_activations_eager_fallback(num_outputs, config, name, ctx): ...

class _RetrieveAllTPUEmbeddingParametersOutput(NamedTuple):
    parameters: Incomplete
    auxiliary1: Incomplete
    auxiliary2: Incomplete
    auxiliary3: Incomplete
    auxiliary4: Incomplete
    auxiliary5: Incomplete
    auxiliary6: Incomplete
    auxiliary7: Incomplete

def retrieve_all_tpu_embedding_parameters(NumTables, config, num_shards, shard_id, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    NumTables: An `int` that is `>= 1`.
    config: A `string`.
    num_shards: An `int`.
    shard_id: An `int`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (parameters, auxiliary1, auxiliary2, auxiliary3, auxiliary4, auxiliary5, auxiliary6, auxiliary7).

    parameters: A list of `NumTables` `Tensor` objects with type `float32`.
    auxiliary1: A list of `NumTables` `Tensor` objects with type `float32`.
    auxiliary2: A list of `NumTables` `Tensor` objects with type `float32`.
    auxiliary3: A list of `NumTables` `Tensor` objects with type `float32`.
    auxiliary4: A list of `NumTables` `Tensor` objects with type `float32`.
    auxiliary5: A list of `NumTables` `Tensor` objects with type `float32`.
    auxiliary6: A list of `NumTables` `Tensor` objects with type `float32`.
    auxiliary7: A list of `NumTables` `Tensor` objects with type `float32`.
  """

RetrieveAllTPUEmbeddingParameters: Incomplete

def retrieve_all_tpu_embedding_parameters_eager_fallback(NumTables, config, num_shards, shard_id, name, ctx): ...
def send_tpu_embedding_gradients(inputs, learning_rates, config, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    inputs: A list of at least 1 `Tensor` objects with type `float32`.
    learning_rates: A list of `Tensor` objects with type `float32`.
    config: A `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

SendTPUEmbeddingGradients: Incomplete

def send_tpu_embedding_gradients_eager_fallback(inputs, learning_rates, config, name, ctx): ...
def shutdown_distributed_tpu(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

ShutdownDistributedTPU: Incomplete

def shutdown_distributed_tpu_eager_fallback(name, ctx): ...

class _SplitDedupDataOutput(NamedTuple):
    integer_tensor: Incomplete
    float_tensor: Incomplete

def split_dedup_data(input, integer_type, float_type, tuple_mask, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input: A `Tensor` of type `variant`.
    integer_type: A `tf.DType` from: `tf.int32, tf.int64, tf.uint32, tf.uint64`.
    float_type: A `tf.DType` from: `tf.half, tf.bfloat16, tf.float32`.
    tuple_mask: A `string`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (integer_tensor, float_tensor).

    integer_tensor: A `Tensor` of type `integer_type`.
    float_tensor: A `Tensor` of type `float_type`.
  """

SplitDedupData: Incomplete

def split_dedup_data_eager_fallback(input, integer_type, float_type, tuple_mask, name, ctx): ...
def tpu_embedding_activations(embedding_variable, sliced_activations, table_id, lookup_id, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    embedding_variable: A `Tensor` of type `float32`.
    sliced_activations: A `Tensor` of type `float32`.
    table_id: An `int` that is `>= 0`.
    lookup_id: An `int` that is `>= 0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """

TPUEmbeddingActivations: Incomplete

def tpu_embedding_activations_eager_fallback(embedding_variable, sliced_activations, table_id, lookup_id, name, ctx): ...
def xla_recv_tpu_embedding_activations(deduplication_data, num_tables, config, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    deduplication_data: A `Tensor` of type `variant`.
    num_tables: An `int` that is `>= 1`.
    config: A `string`.
    name: A name for the operation (optional).

  Returns:
    A list of `num_tables` `Tensor` objects with type `float32`.
  """

XlaRecvTPUEmbeddingActivations: Incomplete

def xla_recv_tpu_embedding_activations_eager_fallback(deduplication_data, num_tables, config, name, ctx): ...
def xla_recv_tpu_embedding_deduplication_data(config, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    config: A `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

XlaRecvTPUEmbeddingDeduplicationData: Incomplete

def xla_recv_tpu_embedding_deduplication_data_eager_fallback(config, name, ctx): ...
def xla_send_tpu_embedding_gradients(gradients, learning_rates, deduplication_data, config, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    gradients: A list of at least 1 `Tensor` objects with type `float32`.
    learning_rates: A list of `Tensor` objects with type `float32`.
    deduplication_data: A `Tensor` of type `variant`.
    config: A `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

XlaSendTPUEmbeddingGradients: Incomplete

def xla_send_tpu_embedding_gradients_eager_fallback(gradients, learning_rates, deduplication_data, config, name, ctx): ...
