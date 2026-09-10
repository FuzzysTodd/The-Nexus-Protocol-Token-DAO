from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def assert_cardinality_dataset(input_dataset, cardinality, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    cardinality: A `Tensor` of type `int64`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

AssertCardinalityDataset: Incomplete

def assert_cardinality_dataset_eager_fallback(input_dataset, cardinality, output_types, output_shapes, name, ctx): ...
def assert_next_dataset(input_dataset, transformations, output_types, output_shapes, name: Incomplete | None = None):
    '''A transformation that asserts which transformations happen next.

  This transformation checks whether the camel-case names (i.e. "FlatMap", not
  "flat_map") of the transformations following this transformation match the list
  of names in the `transformations` argument. If there is a mismatch, the
  transformation raises an exception.

  The check occurs when iterating over the contents of the dataset, which
  means that the check happens *after* any static optimizations are applied
  to the dataset graph.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
      `AssertNextDataset` passes through the outputs of its input dataset.
    transformations: A `Tensor` of type `string`.
      A `tf.string` vector `tf.Tensor` identifying the transformations that are
      expected to happen next.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

AssertNextDataset: Incomplete

def assert_next_dataset_eager_fallback(input_dataset, transformations, output_types, output_shapes, name, ctx): ...
def assert_prev_dataset(input_dataset, transformations, output_types, output_shapes, name: Incomplete | None = None):
    """A transformation that asserts which transformations happened previously.

  This transformation checks the names and, optionally, the attribute name-value
  pairs in the `transformations` argument against those of the transformations
  that preceded this transformation.  If there is a mismatch, the transformation
  raises an exception.

  The check occurs when iterating over the contents of the dataset, which
  means that the check happens *after* any static optimizations are applied
  to the dataset graph.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
      `AssertPrevDataset` passes through the outputs of its input dataset.
    transformations: A `Tensor` of type `string`.
      A `tf.string` vector `tf.Tensor` identifying the transformations, with optional
      attribute name-value pairs, that are expected to have happened previously.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

AssertPrevDataset: Incomplete

def assert_prev_dataset_eager_fallback(input_dataset, transformations, output_types, output_shapes, name, ctx): ...
def auto_shard_dataset(input_dataset, num_workers, index, output_types, output_shapes, auto_shard_policy: int = 0, num_replicas: int = 0, name: Incomplete | None = None):
    """Creates a dataset that shards the input dataset.

  Creates a dataset that shards the input dataset by num_workers, returning a
  sharded dataset for the index-th worker. This attempts to automatically shard
  a dataset by examining the Dataset graph and inserting a shard op before the
  inputs to a reader Dataset (e.g. CSVDataset, TFRecordDataset).

  This dataset will throw a NotFound error if we cannot shard the dataset
  automatically.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    num_workers: A `Tensor` of type `int64`.
      A scalar representing the number of workers to distribute this dataset across.
    index: A `Tensor` of type `int64`.
      A scalar representing the index of the current worker out of num_workers.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    auto_shard_policy: An optional `int`. Defaults to `0`.
    num_replicas: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

AutoShardDataset: Incomplete

def auto_shard_dataset_eager_fallback(input_dataset, num_workers, index, output_types, output_shapes, auto_shard_policy, num_replicas, name, ctx): ...
def bytes_produced_stats_dataset(input_dataset, tag, output_types, output_shapes, name: Incomplete | None = None):
    """Records the bytes size of each element of `input_dataset` in a StatsAggregator.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    tag: A `Tensor` of type `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

BytesProducedStatsDataset: Incomplete

def bytes_produced_stats_dataset_eager_fallback(input_dataset, tag, output_types, output_shapes, name, ctx): ...
def csv_dataset(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    filenames: A `Tensor` of type `string`.
    compression_type: A `Tensor` of type `string`.
    buffer_size: A `Tensor` of type `int64`.
    header: A `Tensor` of type `bool`.
    field_delim: A `Tensor` of type `string`.
    use_quote_delim: A `Tensor` of type `bool`.
    na_value: A `Tensor` of type `string`.
    select_cols: A `Tensor` of type `int64`.
    record_defaults: A list of `Tensor` objects with types from: `float32`, `float64`, `int32`, `int64`, `string`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

CSVDataset: Incomplete

def csv_dataset_eager_fallback(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, output_shapes, name, ctx): ...
def csv_dataset_v2(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, exclude_cols, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    filenames: A `Tensor` of type `string`.
    compression_type: A `Tensor` of type `string`.
    buffer_size: A `Tensor` of type `int64`.
    header: A `Tensor` of type `bool`.
    field_delim: A `Tensor` of type `string`.
    use_quote_delim: A `Tensor` of type `bool`.
    na_value: A `Tensor` of type `string`.
    select_cols: A `Tensor` of type `int64`.
    record_defaults: A list of `Tensor` objects with types from: `float32`, `float64`, `int32`, `int64`, `string`.
    exclude_cols: A `Tensor` of type `int64`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

CSVDatasetV2: Incomplete

def csv_dataset_v2_eager_fallback(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, exclude_cols, output_shapes, name, ctx): ...
def choose_fastest_branch_dataset(input_dataset, ratio_numerator, ratio_denominator, other_arguments, num_elements_per_branch, branches, other_arguments_lengths, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    ratio_numerator: A `Tensor` of type `int64`.
    ratio_denominator: A `Tensor` of type `int64`.
    other_arguments: A list of `Tensor` objects.
    num_elements_per_branch: An `int` that is `>= 1`.
    branches: A list of functions decorated with @Defun that has length `>= 1`.
    other_arguments_lengths: A list of `ints` that has length `>= 1`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ChooseFastestBranchDataset: Incomplete

def choose_fastest_branch_dataset_eager_fallback(input_dataset, ratio_numerator, ratio_denominator, other_arguments, num_elements_per_branch, branches, other_arguments_lengths, output_types, output_shapes, name, ctx): ...
def choose_fastest_dataset(input_datasets, num_experiments, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_datasets: A list of at least 2 `Tensor` objects with type `variant`.
    num_experiments: An `int`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ChooseFastestDataset: Incomplete

def choose_fastest_dataset_eager_fallback(input_datasets, num_experiments, output_types, output_shapes, name, ctx): ...
def compress_element(components, name: Incomplete | None = None):
    """Compresses a dataset element.

  Args:
    components: A list of `Tensor` objects.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

CompressElement: Incomplete

def compress_element_eager_fallback(components, name, ctx): ...
def compute_batch_size(input_dataset, name: Incomplete | None = None):
    """Computes the static batch size of a dataset sans partial batches.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """

ComputeBatchSize: Incomplete

def compute_batch_size_eager_fallback(input_dataset, name, ctx): ...
def data_service_dataset(dataset_id, processing_mode, address, protocol, job_name, max_outstanding_requests, iteration_counter, output_types, output_shapes, task_refresh_interval_hint_ms: int = -1, data_transfer_protocol: str = '', target_workers: str = 'AUTO', cross_trainer_cache_options: str = '', name: Incomplete | None = None):
    '''Creates a dataset that reads data from the tf.data service.

  Args:
    dataset_id: A `Tensor` of type `int64`.
    processing_mode: A `Tensor` of type `string`.
    address: A `Tensor` of type `string`.
    protocol: A `Tensor` of type `string`.
    job_name: A `Tensor` of type `string`.
    max_outstanding_requests: A `Tensor` of type `int64`.
    iteration_counter: A `Tensor` of type `resource`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    task_refresh_interval_hint_ms: An optional `int`. Defaults to `-1`.
    data_transfer_protocol: An optional `string`. Defaults to `""`.
    target_workers: An optional `string`. Defaults to `"AUTO"`.
    cross_trainer_cache_options: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

DataServiceDataset: Incomplete

def data_service_dataset_eager_fallback(dataset_id, processing_mode, address, protocol, job_name, max_outstanding_requests, iteration_counter, output_types, output_shapes, task_refresh_interval_hint_ms, data_transfer_protocol, target_workers, cross_trainer_cache_options, name, ctx): ...
def data_service_dataset_v2(dataset_id, processing_mode, address, protocol, job_name, consumer_index, num_consumers, max_outstanding_requests, iteration_counter, output_types, output_shapes, task_refresh_interval_hint_ms: int = -1, data_transfer_protocol: str = '', target_workers: str = 'AUTO', cross_trainer_cache_options: str = '', name: Incomplete | None = None):
    '''Creates a dataset that reads data from the tf.data service.

  Args:
    dataset_id: A `Tensor` of type `int64`.
    processing_mode: A `Tensor` of type `string`.
    address: A `Tensor` of type `string`.
    protocol: A `Tensor` of type `string`.
    job_name: A `Tensor` of type `string`.
    consumer_index: A `Tensor` of type `int64`.
    num_consumers: A `Tensor` of type `int64`.
    max_outstanding_requests: A `Tensor` of type `int64`.
    iteration_counter: A `Tensor` of type `resource`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    task_refresh_interval_hint_ms: An optional `int`. Defaults to `-1`.
    data_transfer_protocol: An optional `string`. Defaults to `""`.
    target_workers: An optional `string`. Defaults to `"AUTO"`.
    cross_trainer_cache_options: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

DataServiceDatasetV2: Incomplete

def data_service_dataset_v2_eager_fallback(dataset_id, processing_mode, address, protocol, job_name, consumer_index, num_consumers, max_outstanding_requests, iteration_counter, output_types, output_shapes, task_refresh_interval_hint_ms, data_transfer_protocol, target_workers, cross_trainer_cache_options, name, ctx): ...
def data_service_dataset_v3(dataset_id, processing_mode, address, protocol, job_name, consumer_index, num_consumers, max_outstanding_requests, iteration_counter, output_types, output_shapes, uncompress_fn, task_refresh_interval_hint_ms: int = -1, data_transfer_protocol: str = '', target_workers: str = 'AUTO', uncompress: bool = False, cross_trainer_cache_options: str = '', name: Incomplete | None = None):
    '''Creates a dataset that reads data from the tf.data service.

  Args:
    dataset_id: A `Tensor` of type `int64`.
    processing_mode: A `Tensor` of type `string`.
    address: A `Tensor` of type `string`.
    protocol: A `Tensor` of type `string`.
    job_name: A `Tensor` of type `string`.
    consumer_index: A `Tensor` of type `int64`.
    num_consumers: A `Tensor` of type `int64`.
    max_outstanding_requests: A `Tensor` of type `int64`.
    iteration_counter: A `Tensor` of type `resource`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    uncompress_fn: A function decorated with @Defun.
    task_refresh_interval_hint_ms: An optional `int`. Defaults to `-1`.
    data_transfer_protocol: An optional `string`. Defaults to `""`.
    target_workers: An optional `string`. Defaults to `"AUTO"`.
    uncompress: An optional `bool`. Defaults to `False`.
    cross_trainer_cache_options: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

DataServiceDatasetV3: Incomplete

def data_service_dataset_v3_eager_fallback(dataset_id, processing_mode, address, protocol, job_name, consumer_index, num_consumers, max_outstanding_requests, iteration_counter, output_types, output_shapes, uncompress_fn, task_refresh_interval_hint_ms, data_transfer_protocol, target_workers, uncompress, cross_trainer_cache_options, name, ctx): ...
def data_service_dataset_v4(dataset_id, processing_mode, address, protocol, job_name, consumer_index, num_consumers, max_outstanding_requests, iteration_counter, output_types, output_shapes, uncompress_fn, task_refresh_interval_hint_ms: int = -1, data_transfer_protocol: str = '', target_workers: str = 'AUTO', uncompress: bool = False, cross_trainer_cache_options: str = '', name: Incomplete | None = None):
    '''Creates a dataset that reads data from the tf.data service.

  Args:
    dataset_id: A `Tensor` of type `string`.
    processing_mode: A `Tensor` of type `string`.
    address: A `Tensor` of type `string`.
    protocol: A `Tensor` of type `string`.
    job_name: A `Tensor` of type `string`.
    consumer_index: A `Tensor` of type `int64`.
    num_consumers: A `Tensor` of type `int64`.
    max_outstanding_requests: A `Tensor` of type `int64`.
    iteration_counter: A `Tensor` of type `resource`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    uncompress_fn: A function decorated with @Defun.
    task_refresh_interval_hint_ms: An optional `int`. Defaults to `-1`.
    data_transfer_protocol: An optional `string`. Defaults to `""`.
    target_workers: An optional `string`. Defaults to `"AUTO"`.
    uncompress: An optional `bool`. Defaults to `False`.
    cross_trainer_cache_options: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

DataServiceDatasetV4: Incomplete

def data_service_dataset_v4_eager_fallback(dataset_id, processing_mode, address, protocol, job_name, consumer_index, num_consumers, max_outstanding_requests, iteration_counter, output_types, output_shapes, uncompress_fn, task_refresh_interval_hint_ms, data_transfer_protocol, target_workers, uncompress, cross_trainer_cache_options, name, ctx): ...
def dataset_from_graph(graph_def, name: Incomplete | None = None):
    """Creates a dataset from the given `graph_def`.

  Creates a dataset from the provided `graph_def`.

  Args:
    graph_def: A `Tensor` of type `string`.
      The graph representation of the dataset (as serialized GraphDef).
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

DatasetFromGraph: Incomplete

def dataset_from_graph_eager_fallback(graph_def, name, ctx): ...
def dataset_to_tf_record(input_dataset, filename, compression_type, name: Incomplete | None = None):
    '''Writes the given dataset to the given file using the TFRecord format.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the dataset to write.
    filename: A `Tensor` of type `string`.
      A scalar string tensor representing the filename to use.
    compression_type: A `Tensor` of type `string`.
      A scalar string tensor containing either (i) the empty string (no
      compression), (ii) "ZLIB", or (iii) "GZIP".
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

DatasetToTFRecord: Incomplete

def dataset_to_tf_record_eager_fallback(input_dataset, filename, compression_type, name, ctx): ...
def dense_to_sparse_batch_dataset(input_dataset, batch_size, row_shape, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that batches input elements into a SparseTensor.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A handle to an input dataset. Must have a single component.
    batch_size: A `Tensor` of type `int64`.
      A scalar representing the number of elements to accumulate in a
      batch.
    row_shape: A `Tensor` of type `int64`.
      A vector representing the dense shape of each row in the produced
      SparseTensor. The shape may be partially specified, using `-1` to indicate
      that a particular dimension should use the maximum size of all batch elements.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

DenseToSparseBatchDataset: Incomplete

def dense_to_sparse_batch_dataset_eager_fallback(input_dataset, batch_size, row_shape, output_types, output_shapes, name, ctx): ...
def directed_interleave_dataset(selector_input_dataset, data_input_datasets, output_types, output_shapes, stop_on_empty_dataset: bool = False, name: Incomplete | None = None):
    """A substitute for `InterleaveDataset` on a fixed list of `N` datasets.

  Args:
    selector_input_dataset: A `Tensor` of type `variant`.
      A dataset of scalar `DT_INT64` elements that determines which of the
      `N` data inputs should produce the next output element.
    data_input_datasets: A list of at least 1 `Tensor` objects with type `variant`.
      `N` datasets with the same type that will be interleaved according to
      the values of `selector_input_dataset`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    stop_on_empty_dataset: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

DirectedInterleaveDataset: Incomplete

def directed_interleave_dataset_eager_fallback(selector_input_dataset, data_input_datasets, output_types, output_shapes, stop_on_empty_dataset, name, ctx): ...
def distributed_save(dataset, directory, address, metadata: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    dataset: A `Tensor` of type `variant`.
    directory: A `Tensor` of type `string`.
    address: A `Tensor` of type `string`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

DistributedSave: Incomplete

def distributed_save_eager_fallback(dataset, directory, address, metadata, name, ctx): ...
def dummy_iteration_counter(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

DummyIterationCounter: Incomplete

def dummy_iteration_counter_eager_fallback(name, ctx): ...
def experimental_assert_next_dataset(input_dataset, transformations, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    transformations: A `Tensor` of type `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalAssertNextDataset: Incomplete

def experimental_assert_next_dataset_eager_fallback(input_dataset, transformations, output_types, output_shapes, name, ctx): ...
def experimental_auto_shard_dataset(input_dataset, num_workers, index, output_types, output_shapes, auto_shard_policy: int = 0, name: Incomplete | None = None):
    """Creates a dataset that shards the input dataset.

  Creates a dataset that shards the input dataset by num_workers, returning a
  sharded dataset for the index-th worker. This attempts to automatically shard
  a dataset by examining the Dataset graph and inserting a shard op before the
  inputs to a reader Dataset (e.g. CSVDataset, TFRecordDataset).

  This dataset will throw a NotFound error if we cannot shard the dataset
  automatically.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    num_workers: A `Tensor` of type `int64`.
      A scalar representing the number of workers to distribute this dataset across.
    index: A `Tensor` of type `int64`.
      A scalar representing the index of the current worker out of num_workers.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    auto_shard_policy: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalAutoShardDataset: Incomplete

def experimental_auto_shard_dataset_eager_fallback(input_dataset, num_workers, index, output_types, output_shapes, auto_shard_policy, name, ctx): ...
def experimental_bytes_produced_stats_dataset(input_dataset, tag, output_types, output_shapes, name: Incomplete | None = None):
    """Records the bytes size of each element of `input_dataset` in a StatsAggregator.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    tag: A `Tensor` of type `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalBytesProducedStatsDataset: Incomplete

def experimental_bytes_produced_stats_dataset_eager_fallback(input_dataset, tag, output_types, output_shapes, name, ctx): ...
def experimental_csv_dataset(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    filenames: A `Tensor` of type `string`.
    compression_type: A `Tensor` of type `string`.
    buffer_size: A `Tensor` of type `int64`.
    header: A `Tensor` of type `bool`.
    field_delim: A `Tensor` of type `string`.
    use_quote_delim: A `Tensor` of type `bool`.
    na_value: A `Tensor` of type `string`.
    select_cols: A `Tensor` of type `int64`.
    record_defaults: A list of `Tensor` objects with types from: `float32`, `float64`, `int32`, `int64`, `string`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalCSVDataset: Incomplete

def experimental_csv_dataset_eager_fallback(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, output_shapes, name, ctx): ...
def experimental_choose_fastest_dataset(input_datasets, num_experiments, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_datasets: A list of at least 2 `Tensor` objects with type `variant`.
    num_experiments: An `int`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalChooseFastestDataset: Incomplete

def experimental_choose_fastest_dataset_eager_fallback(input_datasets, num_experiments, output_types, output_shapes, name, ctx): ...
def experimental_dataset_cardinality(input_dataset, name: Incomplete | None = None):
    """Returns the cardinality of `input_dataset`.

  Returns the cardinality of `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the dataset to return cardinality for.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """

ExperimentalDatasetCardinality: Incomplete

def experimental_dataset_cardinality_eager_fallback(input_dataset, name, ctx): ...
def experimental_dataset_to_tf_record(input_dataset, filename, compression_type, name: Incomplete | None = None):
    '''Writes the given dataset to the given file using the TFRecord format.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the dataset to write.
    filename: A `Tensor` of type `string`.
      A scalar string tensor representing the filename to use.
    compression_type: A `Tensor` of type `string`.
      A scalar string tensor containing either (i) the empty string (no
      compression), (ii) "ZLIB", or (iii) "GZIP".
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

ExperimentalDatasetToTFRecord: Incomplete

def experimental_dataset_to_tf_record_eager_fallback(input_dataset, filename, compression_type, name, ctx): ...
def experimental_dense_to_sparse_batch_dataset(input_dataset, batch_size, row_shape, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that batches input elements into a SparseTensor.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A handle to an input dataset. Must have a single component.
    batch_size: A `Tensor` of type `int64`.
      A scalar representing the number of elements to accumulate in a
      batch.
    row_shape: A `Tensor` of type `int64`.
      A vector representing the dense shape of each row in the produced
      SparseTensor. The shape may be partially specified, using `-1` to indicate
      that a particular dimension should use the maximum size of all batch elements.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalDenseToSparseBatchDataset: Incomplete

def experimental_dense_to_sparse_batch_dataset_eager_fallback(input_dataset, batch_size, row_shape, output_types, output_shapes, name, ctx): ...
def experimental_directed_interleave_dataset(selector_input_dataset, data_input_datasets, output_types, output_shapes, name: Incomplete | None = None):
    """A substitute for `InterleaveDataset` on a fixed list of `N` datasets.

  Args:
    selector_input_dataset: A `Tensor` of type `variant`.
      A dataset of scalar `DT_INT64` elements that determines which of the
      `N` data inputs should produce the next output element.
    data_input_datasets: A list of at least 1 `Tensor` objects with type `variant`.
      `N` datasets with the same type that will be interleaved according to
      the values of `selector_input_dataset`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalDirectedInterleaveDataset: Incomplete

def experimental_directed_interleave_dataset_eager_fallback(selector_input_dataset, data_input_datasets, output_types, output_shapes, name, ctx): ...
def experimental_group_by_reducer_dataset(input_dataset, key_func_other_arguments, init_func_other_arguments, reduce_func_other_arguments, finalize_func_other_arguments, key_func, init_func, reduce_func, finalize_func, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that computes a group-by on `input_dataset`.

  Creates a dataset that computes a group-by on `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    key_func_other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when
      building a closure for `key_func`.
    init_func_other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when
      building a closure for `init_func`.
    reduce_func_other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when
      building a closure for `reduce_func`.
    finalize_func_other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when
      building a closure for `finalize_func`.
    key_func: A function decorated with @Defun.
      A function mapping an element of `input_dataset`, concatenated
      with `key_func_other_arguments` to a scalar value of type DT_INT64.
    init_func: A function decorated with @Defun.
      A function mapping a key of type DT_INT64, concatenated with
      `init_func_other_arguments` to the initial reducer state.
    reduce_func: A function decorated with @Defun.
      A function mapping the current reducer state and an element of `input_dataset`,
      concatenated with `reduce_func_other_arguments` to a new reducer state.
    finalize_func: A function decorated with @Defun.
      A function mapping the final reducer state to an output element.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalGroupByReducerDataset: Incomplete

def experimental_group_by_reducer_dataset_eager_fallback(input_dataset, key_func_other_arguments, init_func_other_arguments, reduce_func_other_arguments, finalize_func_other_arguments, key_func, init_func, reduce_func, finalize_func, output_types, output_shapes, name, ctx): ...
def experimental_group_by_window_dataset(input_dataset, key_func_other_arguments, reduce_func_other_arguments, window_size_func_other_arguments, key_func, reduce_func, window_size_func, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that computes a windowed group-by on `input_dataset`.

  // TODO(mrry): Support non-int64 keys.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    key_func_other_arguments: A list of `Tensor` objects.
    reduce_func_other_arguments: A list of `Tensor` objects.
    window_size_func_other_arguments: A list of `Tensor` objects.
    key_func: A function decorated with @Defun.
      A function mapping an element of `input_dataset`, concatenated
      with `key_func_other_arguments` to a scalar value of type DT_INT64.
    reduce_func: A function decorated with @Defun.
    window_size_func: A function decorated with @Defun.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalGroupByWindowDataset: Incomplete

def experimental_group_by_window_dataset_eager_fallback(input_dataset, key_func_other_arguments, reduce_func_other_arguments, window_size_func_other_arguments, key_func, reduce_func, window_size_func, output_types, output_shapes, name, ctx): ...
def experimental_ignore_errors_dataset(input_dataset, output_types, output_shapes, log_warning: bool = False, name: Incomplete | None = None):
    """Creates a dataset that contains the elements of `input_dataset` ignoring errors.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    log_warning: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalIgnoreErrorsDataset: Incomplete

def experimental_ignore_errors_dataset_eager_fallback(input_dataset, output_types, output_shapes, log_warning, name, ctx): ...
def experimental_iterator_get_device(resource, name: Incomplete | None = None):
    """Returns the name of the device on which `resource` has been placed.

  Args:
    resource: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

ExperimentalIteratorGetDevice: Incomplete

def experimental_iterator_get_device_eager_fallback(resource, name, ctx): ...
def experimental_lmdb_dataset(filenames, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    filenames: A `Tensor` of type `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalLMDBDataset: Incomplete

def experimental_lmdb_dataset_eager_fallback(filenames, output_types, output_shapes, name, ctx): ...
def experimental_latency_stats_dataset(input_dataset, tag, output_types, output_shapes, name: Incomplete | None = None):
    """Records the latency of producing `input_dataset` elements in a StatsAggregator.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    tag: A `Tensor` of type `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalLatencyStatsDataset: Incomplete

def experimental_latency_stats_dataset_eager_fallback(input_dataset, tag, output_types, output_shapes, name, ctx): ...
def experimental_map_and_batch_dataset(input_dataset, other_arguments, batch_size, num_parallel_calls, drop_remainder, f, output_types, output_shapes, preserve_cardinality: bool = False, name: Incomplete | None = None):
    '''Creates a dataset that fuses mapping with batching.

  Creates a dataset that applies `f` to the outputs of `input_dataset` and then
  batches `batch_size` of them.

  Unlike a "MapDataset", which applies `f` sequentially, this dataset invokes up
  to `batch_size * num_parallel_batches` copies of `f` in parallel.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when building a closure
      for `f`.
    batch_size: A `Tensor` of type `int64`.
      A scalar representing the number of elements to accumulate in a
      batch. It determines the number of concurrent invocations of `f` that process
      elements from `input_dataset` in parallel.
    num_parallel_calls: A `Tensor` of type `int64`.
      A scalar representing the maximum number of parallel invocations of the `map_fn`
      function. Applying the `map_fn` on consecutive input elements in parallel has
      the potential to improve input pipeline throughput.
    drop_remainder: A `Tensor` of type `bool`.
      A scalar representing whether the last batch should be dropped in case its size
      is smaller than desired.
    f: A function decorated with @Defun.
      A function to apply to the outputs of `input_dataset`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    preserve_cardinality: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ExperimentalMapAndBatchDataset: Incomplete

def experimental_map_and_batch_dataset_eager_fallback(input_dataset, other_arguments, batch_size, num_parallel_calls, drop_remainder, f, output_types, output_shapes, preserve_cardinality, name, ctx): ...
def experimental_map_dataset(input_dataset, other_arguments, f, output_types, output_shapes, use_inter_op_parallelism: bool = True, preserve_cardinality: bool = False, name: Incomplete | None = None):
    """Creates a dataset that applies `f` to the outputs of `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    other_arguments: A list of `Tensor` objects.
    f: A function decorated with @Defun.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    use_inter_op_parallelism: An optional `bool`. Defaults to `True`.
    preserve_cardinality: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalMapDataset: Incomplete

def experimental_map_dataset_eager_fallback(input_dataset, other_arguments, f, output_types, output_shapes, use_inter_op_parallelism, preserve_cardinality, name, ctx): ...
def experimental_matching_files_dataset(patterns, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    patterns: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalMatchingFilesDataset: Incomplete

def experimental_matching_files_dataset_eager_fallback(patterns, name, ctx): ...
def experimental_max_intra_op_parallelism_dataset(input_dataset, max_intra_op_parallelism, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that overrides the maximum intra-op parallelism.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    max_intra_op_parallelism: A `Tensor` of type `int64`.
      Identifies the maximum intra-op parallelism to use.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalMaxIntraOpParallelismDataset: Incomplete

def experimental_max_intra_op_parallelism_dataset_eager_fallback(input_dataset, max_intra_op_parallelism, output_types, output_shapes, name, ctx): ...
def experimental_non_serializable_dataset(input_dataset, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalNonSerializableDataset: Incomplete

def experimental_non_serializable_dataset_eager_fallback(input_dataset, output_types, output_shapes, name, ctx): ...
def experimental_parallel_interleave_dataset(input_dataset, other_arguments, cycle_length, block_length, sloppy, buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that applies `f` to the outputs of `input_dataset`.

  The resulting dataset is similar to the `InterleaveDataset`, with the exception
  that if retrieving the next value from a dataset would cause the requester to
  block, it will skip that input dataset. This dataset is especially useful
  when loading data from a variable-latency datastores (e.g. HDFS, GCS), as it
  allows the training step to proceed so long as some data is available.

  !! WARNING !! This dataset is not deterministic!

  Args:
    input_dataset: A `Tensor` of type `variant`.
    other_arguments: A list of `Tensor` objects.
    cycle_length: A `Tensor` of type `int64`.
    block_length: A `Tensor` of type `int64`.
    sloppy: A `Tensor` of type `bool`.
    buffer_output_elements: A `Tensor` of type `int64`.
    prefetch_input_elements: A `Tensor` of type `int64`.
    f: A function decorated with @Defun.
      A function mapping elements of `input_dataset`, concatenated with
      `other_arguments`, to a Dataset variant that contains elements matching
      `output_types` and `output_shapes`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalParallelInterleaveDataset: Incomplete

def experimental_parallel_interleave_dataset_eager_fallback(input_dataset, other_arguments, cycle_length, block_length, sloppy, buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes, name, ctx): ...
def experimental_parse_example_dataset(input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys, sparse_types, dense_shapes, output_types, output_shapes, sloppy: bool = False, name: Incomplete | None = None):
    """Transforms `input_dataset` containing `Example` protos as vectors of DT_STRING into a dataset of `Tensor` or `SparseTensor` objects representing the parsed features.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    num_parallel_calls: A `Tensor` of type `int64`.
    dense_defaults: A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
      A dict mapping string keys to `Tensor`s.
      The keys of the dict must match the dense_keys of the feature.
    sparse_keys: A list of `strings`.
      A list of string keys in the examples features.
      The results for these keys will be returned as `SparseTensor` objects.
    dense_keys: A list of `strings`.
      A list of Ndense string Tensors (scalars).
      The keys expected in the Examples features associated with dense values.
    sparse_types: A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
      A list of `DTypes` of the same length as `sparse_keys`.
      Only `tf.float32` (`FloatList`), `tf.int64` (`Int64List`),
      and `tf.string` (`BytesList`) are supported.
    dense_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`).
      List of tuples with the same length as `dense_keys`.
      The shape of the data for each dense feature referenced by `dense_keys`.
      Required for any input tensors identified by `dense_keys`.  Must be
      either fully defined, or may contain an unknown first dimension.
      An unknown first dimension means the feature is treated as having
      a variable number of blocks, and the output shape along this dimension
      is considered unknown at graph build time.  Padding is applied for
      minibatch elements smaller than the maximum number of blocks for the
      given feature along this dimension.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
      The type list for the return values.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
      The list of shapes being produced.
    sloppy: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalParseExampleDataset: Incomplete

def experimental_parse_example_dataset_eager_fallback(input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys, sparse_types, dense_shapes, output_types, output_shapes, sloppy, name, ctx): ...
def experimental_private_thread_pool_dataset(input_dataset, num_threads, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that uses a custom thread pool to compute `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    num_threads: A `Tensor` of type `int64`.
      Identifies the number of threads to use for the private threadpool.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalPrivateThreadPoolDataset: Incomplete

def experimental_private_thread_pool_dataset_eager_fallback(input_dataset, num_threads, output_types, output_shapes, name, ctx): ...
def experimental_random_dataset(seed, seed2, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a Dataset that returns pseudorandom numbers.

  Args:
    seed: A `Tensor` of type `int64`.
      A scalar seed for the random number generator. If either seed or
      seed2 is set to be non-zero, the random number generator is seeded
      by the given seed.  Otherwise, a random seed is used.
    seed2: A `Tensor` of type `int64`.
      A second scalar seed to avoid seed collision.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalRandomDataset: Incomplete

def experimental_random_dataset_eager_fallback(seed, seed2, output_types, output_shapes, name, ctx): ...
def experimental_rebatch_dataset(input_dataset, num_replicas, output_types, output_shapes, use_fallback: bool = True, name: Incomplete | None = None):
    """Creates a dataset that changes the batch size.

  Creates a dataset that changes the batch size of the dataset to current batch
  size // num_replicas.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    num_replicas: A `Tensor` of type `int64`.
      A scalar representing the number of replicas to distribute this batch across. As
      a result of this transformation the current batch size would end up being
      divided  by this parameter.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    use_fallback: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalRebatchDataset: Incomplete

def experimental_rebatch_dataset_eager_fallback(input_dataset, num_replicas, output_types, output_shapes, use_fallback, name, ctx): ...
def experimental_scan_dataset(input_dataset, initial_state, other_arguments, f, output_types, output_shapes, preserve_cardinality: bool = False, name: Incomplete | None = None):
    """Creates a dataset successively reduces `f` over the elements of `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    initial_state: A list of `Tensor` objects.
    other_arguments: A list of `Tensor` objects.
    f: A function decorated with @Defun.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    preserve_cardinality: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalScanDataset: Incomplete

def experimental_scan_dataset_eager_fallback(input_dataset, initial_state, other_arguments, f, output_types, output_shapes, preserve_cardinality, name, ctx): ...
def experimental_set_stats_aggregator_dataset(input_dataset, stats_aggregator, tag, counter_prefix, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    stats_aggregator: A `Tensor` of type `resource`.
    tag: A `Tensor` of type `string`.
    counter_prefix: A `Tensor` of type `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalSetStatsAggregatorDataset: Incomplete

def experimental_set_stats_aggregator_dataset_eager_fallback(input_dataset, stats_aggregator, tag, counter_prefix, output_types, output_shapes, name, ctx): ...
def experimental_sleep_dataset(input_dataset, sleep_microseconds, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    sleep_microseconds: A `Tensor` of type `int64`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalSleepDataset: Incomplete

def experimental_sleep_dataset_eager_fallback(input_dataset, sleep_microseconds, output_types, output_shapes, name, ctx): ...
def experimental_sliding_window_dataset(input_dataset, window_size, window_shift, window_stride, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that passes a sliding window over `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    window_size: A `Tensor` of type `int64`.
      A scalar representing the number of elements in the
      sliding window.
    window_shift: A `Tensor` of type `int64`.
      A scalar representing the steps moving the sliding window
      forward in one iteration. It must be positive.
    window_stride: A `Tensor` of type `int64`.
      A scalar representing the stride of the input elements of the sliding window.
      It must be positive.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalSlidingWindowDataset: Incomplete

def experimental_sliding_window_dataset_eager_fallback(input_dataset, window_size, window_shift, window_stride, output_types, output_shapes, name, ctx): ...
def experimental_sql_dataset(driver_name, data_source_name, query, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that executes a SQL query and emits rows of the result set.

  Args:
    driver_name: A `Tensor` of type `string`.
      The database type. Currently, the only supported type is 'sqlite'.
    data_source_name: A `Tensor` of type `string`.
      A connection string to connect to the database.
    query: A `Tensor` of type `string`. A SQL query to execute.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalSqlDataset: Incomplete

def experimental_sql_dataset_eager_fallback(driver_name, data_source_name, query, output_types, output_shapes, name, ctx): ...
def experimental_stats_aggregator_handle(container: str = '', shared_name: str = '', name: Incomplete | None = None):
    '''Creates a statistics manager resource.

  Args:
    container: An optional `string`. Defaults to `""`.
    shared_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

ExperimentalStatsAggregatorHandle: Incomplete

def experimental_stats_aggregator_handle_eager_fallback(container, shared_name, name, ctx): ...
def experimental_stats_aggregator_summary(iterator, name: Incomplete | None = None):
    """Produces a summary of any statistics recorded by the given statistics manager.

  Args:
    iterator: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

ExperimentalStatsAggregatorSummary: Incomplete

def experimental_stats_aggregator_summary_eager_fallback(iterator, name, ctx): ...
def experimental_take_while_dataset(input_dataset, other_arguments, predicate, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that stops iteration when predicate` is false.

  The `predicate` function must return a scalar boolean and accept the
  following arguments:

  * One tensor for each component of an element of `input_dataset`.
  * One tensor for each value in `other_arguments`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when
      building a closure for `predicate`.
    predicate: A function decorated with @Defun.
      A function returning a scalar boolean.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalTakeWhileDataset: Incomplete

def experimental_take_while_dataset_eager_fallback(input_dataset, other_arguments, predicate, output_types, output_shapes, name, ctx): ...
def experimental_thread_pool_dataset(input_dataset, thread_pool, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that uses a custom thread pool to compute `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    thread_pool: A `Tensor` of type `resource`.
      A resource produced by the ThreadPoolHandle op.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalThreadPoolDataset: Incomplete

def experimental_thread_pool_dataset_eager_fallback(input_dataset, thread_pool, output_types, output_shapes, name, ctx): ...
def experimental_thread_pool_handle(num_threads, display_name, max_intra_op_parallelism: int = 1, container: str = '', shared_name: str = '', name: Incomplete | None = None):
    '''Creates a dataset that uses a custom thread pool to compute `input_dataset`.

  Args:
    num_threads: An `int`. The number of threads in the thread pool.
    display_name: A `string`.
      A human-readable name for the threads that may be visible in some
      visualizations.
      threadpool.
    max_intra_op_parallelism: An optional `int`. Defaults to `1`.
      The maximum degree of parallelism to use within operations that execute on this
      threadpool.
    container: An optional `string`. Defaults to `""`.
    shared_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

ExperimentalThreadPoolHandle: Incomplete

def experimental_thread_pool_handle_eager_fallback(num_threads, display_name, max_intra_op_parallelism, container, shared_name, name, ctx): ...
def experimental_unbatch_dataset(input_dataset, output_types, output_shapes, name: Incomplete | None = None):
    """A dataset that splits the elements of its input into multiple elements.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalUnbatchDataset: Incomplete

def experimental_unbatch_dataset_eager_fallback(input_dataset, output_types, output_shapes, name, ctx): ...
def experimental_unique_dataset(input_dataset, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that contains the unique elements of `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ExperimentalUniqueDataset: Incomplete

def experimental_unique_dataset_eager_fallback(input_dataset, output_types, output_shapes, name, ctx): ...
def get_element_at_index(dataset, index, output_types, output_shapes, name: Incomplete | None = None):
    """Gets the element at the specified index in a dataset.

  Args:
    dataset: A `Tensor` of type `variant`.
    index: A `Tensor` of type `int64`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `output_types`.
  """

GetElementAtIndex: Incomplete

def get_element_at_index_eager_fallback(dataset, index, output_types, output_shapes, name, ctx): ...
def group_by_reducer_dataset(input_dataset, key_func_other_arguments, init_func_other_arguments, reduce_func_other_arguments, finalize_func_other_arguments, key_func, init_func, reduce_func, finalize_func, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that computes a group-by on `input_dataset`.

  Creates a dataset that computes a group-by on `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    key_func_other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when
      building a closure for `key_func`.
    init_func_other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when
      building a closure for `init_func`.
    reduce_func_other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when
      building a closure for `reduce_func`.
    finalize_func_other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when
      building a closure for `finalize_func`.
    key_func: A function decorated with @Defun.
      A function mapping an element of `input_dataset`, concatenated
      with `key_func_other_arguments` to a scalar value of type DT_INT64.
    init_func: A function decorated with @Defun.
      A function mapping a key of type DT_INT64, concatenated with
      `init_func_other_arguments` to the initial reducer state.
    reduce_func: A function decorated with @Defun.
      A function mapping the current reducer state and an element of `input_dataset`,
      concatenated with `reduce_func_other_arguments` to a new reducer state.
    finalize_func: A function decorated with @Defun.
      A function mapping the final reducer state to an output element.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

GroupByReducerDataset: Incomplete

def group_by_reducer_dataset_eager_fallback(input_dataset, key_func_other_arguments, init_func_other_arguments, reduce_func_other_arguments, finalize_func_other_arguments, key_func, init_func, reduce_func, finalize_func, output_types, output_shapes, name, ctx): ...
def group_by_window_dataset(input_dataset, key_func_other_arguments, reduce_func_other_arguments, window_size_func_other_arguments, key_func, reduce_func, window_size_func, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that computes a windowed group-by on `input_dataset`.

  // TODO(mrry): Support non-int64 keys.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    key_func_other_arguments: A list of `Tensor` objects.
    reduce_func_other_arguments: A list of `Tensor` objects.
    window_size_func_other_arguments: A list of `Tensor` objects.
    key_func: A function decorated with @Defun.
      A function mapping an element of `input_dataset`, concatenated
      with `key_func_other_arguments` to a scalar value of type DT_INT64.
    reduce_func: A function decorated with @Defun.
    window_size_func: A function decorated with @Defun.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

GroupByWindowDataset: Incomplete

def group_by_window_dataset_eager_fallback(input_dataset, key_func_other_arguments, reduce_func_other_arguments, window_size_func_other_arguments, key_func, reduce_func, window_size_func, output_types, output_shapes, metadata, name, ctx): ...
def ignore_errors_dataset(input_dataset, output_types, output_shapes, log_warning: bool = False, name: Incomplete | None = None):
    """Creates a dataset that contains the elements of `input_dataset` ignoring errors.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    log_warning: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

IgnoreErrorsDataset: Incomplete

def ignore_errors_dataset_eager_fallback(input_dataset, output_types, output_shapes, log_warning, name, ctx): ...
def initialize_table_from_dataset(table_handle, dataset, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    table_handle: A `Tensor` of type `resource`.
    dataset: A `Tensor` of type `variant`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

InitializeTableFromDataset: Incomplete

def initialize_table_from_dataset_eager_fallback(table_handle, dataset, name, ctx): ...
def iterator_get_device(resource, name: Incomplete | None = None):
    """Returns the name of the device on which `resource` has been placed.

  Args:
    resource: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

IteratorGetDevice: Incomplete

def iterator_get_device_eager_fallback(resource, name, ctx): ...
def lmdb_dataset(filenames, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that emits the key-value pairs in one or more LMDB files.

  The Lightning Memory-Mapped Database Manager, or LMDB, is an embedded binary
  key-value database. This dataset can read the contents of LMDB database files,
  the names of which generally have the `.mdb` suffix.

  Each output element consists of a key-value pair represented as a pair of
  scalar string `Tensor`s, where the first `Tensor` contains the key and the
  second `Tensor` contains the value.

  LMDB uses different file formats on big- and little-endian machines.
  `LMDBDataset` can only read files in the format of the host machine.

  Args:
    filenames: A `Tensor` of type `string`.
      A scalar or a vector containing the name(s) of the binary file(s) to be
      read.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

LMDBDataset: Incomplete

def lmdb_dataset_eager_fallback(filenames, output_types, output_shapes, name, ctx): ...
def latency_stats_dataset(input_dataset, tag, output_types, output_shapes, name: Incomplete | None = None):
    """Records the latency of producing `input_dataset` elements in a StatsAggregator.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    tag: A `Tensor` of type `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

LatencyStatsDataset: Incomplete

def latency_stats_dataset_eager_fallback(input_dataset, tag, output_types, output_shapes, name, ctx): ...
def legacy_parallel_interleave_dataset_v2(input_dataset, other_arguments, cycle_length, block_length, buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes, deterministic: str = 'default', metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that applies `f` to the outputs of `input_dataset`.

  The resulting dataset is similar to the `InterleaveDataset`, with the exception
  that if retrieving the next value from a dataset would cause the requester to
  block, it will skip that input dataset. This dataset is especially useful
  when loading data from a variable-latency datastores (e.g. HDFS, GCS), as it
  allows the training step to proceed so long as some data is available.

  !! WARNING !! This dataset is not deterministic!

  Args:
    input_dataset: A `Tensor` of type `variant`.
    other_arguments: A list of `Tensor` objects.
    cycle_length: A `Tensor` of type `int64`.
    block_length: A `Tensor` of type `int64`.
    buffer_output_elements: A `Tensor` of type `int64`.
    prefetch_input_elements: A `Tensor` of type `int64`.
    f: A function decorated with @Defun.
      A function mapping elements of `input_dataset`, concatenated with
      `other_arguments`, to a Dataset variant that contains elements matching
      `output_types` and `output_shapes`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    deterministic: An optional `string`. Defaults to `"default"`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

LegacyParallelInterleaveDatasetV2: Incomplete

def legacy_parallel_interleave_dataset_v2_eager_fallback(input_dataset, other_arguments, cycle_length, block_length, buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes, deterministic, metadata, name, ctx): ...
def list_dataset(tensors, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that emits each of `tensors` once.

  Args:
    tensors: A list of `Tensor` objects.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ListDataset: Incomplete

def list_dataset_eager_fallback(tensors, output_types, output_shapes, metadata, name, ctx): ...
def load_dataset(path, reader_func_other_args, output_types, output_shapes, reader_func, compression: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    path: A `Tensor` of type `string`.
    reader_func_other_args: A list of `Tensor` objects.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    reader_func: A function decorated with @Defun.
    compression: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

LoadDataset: Incomplete

def load_dataset_eager_fallback(path, reader_func_other_args, output_types, output_shapes, reader_func, compression, name, ctx): ...
def map_and_batch_dataset(input_dataset, other_arguments, batch_size, num_parallel_calls, drop_remainder, f, output_types, output_shapes, preserve_cardinality: bool = False, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that fuses mapping with batching.

  Creates a dataset that applies `f` to the outputs of `input_dataset` and then
  batches `batch_size` of them.

  Unlike a "MapDataset", which applies `f` sequentially, this dataset invokes up
  to `batch_size * num_parallel_batches` copies of `f` in parallel.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when building a closure
      for `f`.
    batch_size: A `Tensor` of type `int64`.
      A scalar representing the number of elements to accumulate in a
      batch. It determines the number of concurrent invocations of `f` that process
      elements from `input_dataset` in parallel.
    num_parallel_calls: A `Tensor` of type `int64`.
      A scalar representing the maximum number of parallel invocations of the `map_fn`
      function. Applying the `map_fn` on consecutive input elements in parallel has
      the potential to improve input pipeline throughput.
    drop_remainder: A `Tensor` of type `bool`.
      A scalar representing whether the last batch should be dropped in case its size
      is smaller than desired.
    f: A function decorated with @Defun.
      A function to apply to the outputs of `input_dataset`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    preserve_cardinality: An optional `bool`. Defaults to `False`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

MapAndBatchDataset: Incomplete

def map_and_batch_dataset_eager_fallback(input_dataset, other_arguments, batch_size, num_parallel_calls, drop_remainder, f, output_types, output_shapes, preserve_cardinality, metadata, name, ctx): ...
def matching_files_dataset(patterns, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    patterns: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

MatchingFilesDataset: Incomplete

def matching_files_dataset_eager_fallback(patterns, name, ctx): ...
def max_intra_op_parallelism_dataset(input_dataset, max_intra_op_parallelism, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that overrides the maximum intra-op parallelism.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    max_intra_op_parallelism: A `Tensor` of type `int64`.
      Identifies the maximum intra-op parallelism to use.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

MaxIntraOpParallelismDataset: Incomplete

def max_intra_op_parallelism_dataset_eager_fallback(input_dataset, max_intra_op_parallelism, output_types, output_shapes, name, ctx): ...
def non_serializable_dataset(input_dataset, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

NonSerializableDataset: Incomplete

def non_serializable_dataset_eager_fallback(input_dataset, output_types, output_shapes, name, ctx): ...
def parallel_interleave_dataset(input_dataset, other_arguments, cycle_length, block_length, sloppy, buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that applies `f` to the outputs of `input_dataset`.

  The resulting dataset is similar to the `InterleaveDataset`, with the exception
  that if retrieving the next value from a dataset would cause the requester to
  block, it will skip that input dataset. This dataset is especially useful
  when loading data from a variable-latency datastores (e.g. HDFS, GCS), as it
  allows the training step to proceed so long as some data is available.

  !! WARNING !! If the `sloppy` parameter is set to `True`, the operation of this
  dataset will not be deterministic!

  This dataset has been superseded by `ParallelInterleaveDatasetV2`.  New code
  should use `ParallelInterleaveDatasetV2`.

  The Python API `tf.data.experimental.parallel_interleave` creates instances of
  this op. `tf.data.experimental.parallel_interleave` is a deprecated API.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      Dataset that produces a stream of arguments for the function `f`.
    other_arguments: A list of `Tensor` objects.
      Additional arguments to pass to `f` beyond those produced by `input_dataset`.
      Evaluated once when the dataset is instantiated.
    cycle_length: A `Tensor` of type `int64`.
      Number of datasets (each created by applying `f` to the elements of
      `input_dataset`) among which the `ParallelInterleaveDataset` will cycle in a
      round-robin fashion.
    block_length: A `Tensor` of type `int64`.
      Number of elements at a time to produce from each interleaved invocation of a
      dataset returned by `f`.
    sloppy: A `Tensor` of type `bool`.
      If `True`, return elements as they become available, even if that means returning
      these elements in a non-deterministic order. Sloppy operation may result in better
      performance in the presence of stragglers, but the dataset will still block if
      all of its open streams are blocked.
      If `False`, always return elements in a deterministic order.
    buffer_output_elements: A `Tensor` of type `int64`.
      The number of elements each iterator being interleaved should buffer (similar
      to the `.prefetch()` transformation for each interleaved iterator).
    prefetch_input_elements: A `Tensor` of type `int64`.
      Determines the number of iterators to prefetch, allowing buffers to warm up and
      data to be pre-fetched without blocking the main thread.
    f: A function decorated with @Defun.
      A function mapping elements of `input_dataset`, concatenated with
      `other_arguments`, to a Dataset variant that contains elements matching
      `output_types` and `output_shapes`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ParallelInterleaveDataset: Incomplete

def parallel_interleave_dataset_eager_fallback(input_dataset, other_arguments, cycle_length, block_length, sloppy, buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes, metadata, name, ctx): ...
def parse_example_dataset(input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys, sparse_types, dense_shapes, output_types, output_shapes, sloppy: bool = False, ragged_keys=[], ragged_value_types=[], ragged_split_types=[], name: Incomplete | None = None):
    """Transforms `input_dataset` containing `Example` protos as vectors of DT_STRING into a dataset of `Tensor` or `SparseTensor` objects representing the parsed features.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    num_parallel_calls: A `Tensor` of type `int64`.
    dense_defaults: A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
      A dict mapping string keys to `Tensor`s.
      The keys of the dict must match the dense_keys of the feature.
    sparse_keys: A list of `strings`.
      A list of string keys in the examples features.
      The results for these keys will be returned as `SparseTensor` objects.
    dense_keys: A list of `strings`.
      A list of Ndense string Tensors (scalars).
      The keys expected in the Examples features associated with dense values.
    sparse_types: A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
      A list of `DTypes` of the same length as `sparse_keys`.
      Only `tf.float32` (`FloatList`), `tf.int64` (`Int64List`),
      and `tf.string` (`BytesList`) are supported.
    dense_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`).
      List of tuples with the same length as `dense_keys`.
      The shape of the data for each dense feature referenced by `dense_keys`.
      Required for any input tensors identified by `dense_keys`.  Must be
      either fully defined, or may contain an unknown first dimension.
      An unknown first dimension means the feature is treated as having
      a variable number of blocks, and the output shape along this dimension
      is considered unknown at graph build time.  Padding is applied for
      minibatch elements smaller than the maximum number of blocks for the
      given feature along this dimension.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
      The type list for the return values.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
      The list of shapes being produced.
    sloppy: An optional `bool`. Defaults to `False`.
    ragged_keys: An optional list of `strings`. Defaults to `[]`.
    ragged_value_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
    ragged_split_types: An optional list of `tf.DTypes` from: `tf.int32, tf.int64`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ParseExampleDataset: Incomplete

def parse_example_dataset_eager_fallback(input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys, sparse_types, dense_shapes, output_types, output_shapes, sloppy, ragged_keys, ragged_value_types, ragged_split_types, name, ctx): ...
def parse_example_dataset_v2(input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys, sparse_types, dense_shapes, output_types, output_shapes, deterministic: str = 'default', ragged_keys=[], ragged_value_types=[], ragged_split_types=[], name: Incomplete | None = None):
    '''Transforms `input_dataset` containing `Example` protos as vectors of DT_STRING into a dataset of `Tensor` or `SparseTensor` objects representing the parsed features.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    num_parallel_calls: A `Tensor` of type `int64`.
    dense_defaults: A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
      A dict mapping string keys to `Tensor`s.
      The keys of the dict must match the dense_keys of the feature.
    sparse_keys: A list of `strings`.
      A list of string keys in the examples features.
      The results for these keys will be returned as `SparseTensor` objects.
    dense_keys: A list of `strings`.
      A list of Ndense string Tensors (scalars).
      The keys expected in the Examples features associated with dense values.
    sparse_types: A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
      A list of `DTypes` of the same length as `sparse_keys`.
      Only `tf.float32` (`FloatList`), `tf.int64` (`Int64List`),
      and `tf.string` (`BytesList`) are supported.
    dense_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`).
      List of tuples with the same length as `dense_keys`.
      The shape of the data for each dense feature referenced by `dense_keys`.
      Required for any input tensors identified by `dense_keys`.  Must be
      either fully defined, or may contain an unknown first dimension.
      An unknown first dimension means the feature is treated as having
      a variable number of blocks, and the output shape along this dimension
      is considered unknown at graph build time.  Padding is applied for
      minibatch elements smaller than the maximum number of blocks for the
      given feature along this dimension.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
      The type list for the return values.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
      The list of shapes being produced.
    deterministic: An optional `string`. Defaults to `"default"`.
      A string indicating the op-level determinism to use. Deterministic controls
      whether the dataset is allowed to return elements out of order if the next
      element to be returned isn\'t available, but a later element is. Options are
      "true", "false", and "default". "default" indicates that determinism should be
      decided by the `experimental_deterministic` parameter of `tf.data.Options`.
    ragged_keys: An optional list of `strings`. Defaults to `[]`.
    ragged_value_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
    ragged_split_types: An optional list of `tf.DTypes` from: `tf.int32, tf.int64`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ParseExampleDatasetV2: Incomplete

def parse_example_dataset_v2_eager_fallback(input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys, sparse_types, dense_shapes, output_types, output_shapes, deterministic, ragged_keys, ragged_value_types, ragged_split_types, name, ctx): ...
def private_thread_pool_dataset(input_dataset, num_threads, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that uses a custom thread pool to compute `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    num_threads: A `Tensor` of type `int64`.
      Identifies the number of threads to use for the private threadpool.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

PrivateThreadPoolDataset: Incomplete

def private_thread_pool_dataset_eager_fallback(input_dataset, num_threads, output_types, output_shapes, name, ctx): ...
def random_dataset(seed, seed2, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a Dataset that returns pseudorandom numbers.

  Creates a Dataset that returns a stream of uniformly distributed
  pseudorandom 64-bit signed integers.

  In the TensorFlow Python API, you can instantiate this dataset via the
  class `tf.data.experimental.RandomDataset`.

  Instances of this dataset are also created as a result of the
  `hoist_random_uniform` static optimization. Whether this optimization is
  performed is determined by the `experimental_optimization.hoist_random_uniform`
  option of `tf.data.Options`.

  Args:
    seed: A `Tensor` of type `int64`.
      A scalar seed for the random number generator. If either seed or
      seed2 is set to be non-zero, the random number generator is seeded
      by the given seed.  Otherwise, a random seed is used.
    seed2: A `Tensor` of type `int64`.
      A second scalar seed to avoid seed collision.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

RandomDataset: Incomplete

def random_dataset_eager_fallback(seed, seed2, output_types, output_shapes, metadata, name, ctx): ...
def random_dataset_v2(seed, seed2, seed_generator, output_types, output_shapes, rerandomize_each_iteration: bool = False, metadata: str = '', name: Incomplete | None = None):
    '''Creates a Dataset that returns pseudorandom numbers.

  Creates a Dataset that returns a stream of uniformly distributed
  pseudorandom 64-bit signed integers. It accepts a boolean attribute that
  determines if the random number generators are re-applied at each epoch. The
  default value is True which means that the seeds are applied and the same
  sequence of random numbers are generated at each epoch. If set to False, the
  seeds are not re-applied and a different sequence of random numbers are
  generated at each epoch.

  In the TensorFlow Python API, you can instantiate this dataset via the
  class `tf.data.experimental.RandomDatasetV2`.

  Args:
    seed: A `Tensor` of type `int64`.
      A scalar seed for the random number generator. If either seed or
      seed2 is set to be non-zero, the random number generator is seeded
      by the given seed.  Otherwise, a random seed is used.
    seed2: A `Tensor` of type `int64`.
      A second scalar seed to avoid seed collision.
    seed_generator: A `Tensor` of type `resource`.
      A resource for the random number seed generator.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    rerandomize_each_iteration: An optional `bool`. Defaults to `False`.
      A boolean attribute to rerandomize the sequence of random numbers generated
      at each epoch.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

RandomDatasetV2: Incomplete

def random_dataset_v2_eager_fallback(seed, seed2, seed_generator, output_types, output_shapes, rerandomize_each_iteration, metadata, name, ctx): ...
def rebatch_dataset(input_dataset, num_replicas, output_types, output_shapes, use_fallback: bool = True, name: Incomplete | None = None):
    """Creates a dataset that changes the batch size.

  Creates a dataset that changes the batch size of the dataset to current batch
  size // num_workers.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    num_replicas: A `Tensor` of type `int64`.
      A scalar representing the number of replicas to distribute this batch across. As
      a result of this transformation the current batch size would end up being
      divided  by this parameter.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    use_fallback: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

RebatchDataset: Incomplete

def rebatch_dataset_eager_fallback(input_dataset, num_replicas, output_types, output_shapes, use_fallback, name, ctx): ...
def rebatch_dataset_v2(input_dataset, batch_sizes, drop_remainder, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that changes the batch size.

  Creates a dataset that rebatches elements from `input_dataset` into new batch
  sizes.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    batch_sizes: A `Tensor` of type `int64`.
      A vector of integers representing the size of batches to produce. These values
      are cycled through in order.
    drop_remainder: A `Tensor` of type `bool`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

RebatchDatasetV2: Incomplete

def rebatch_dataset_v2_eager_fallback(input_dataset, batch_sizes, drop_remainder, output_types, output_shapes, name, ctx): ...
def register_dataset(dataset, address, protocol, external_state_policy, element_spec: str = '', metadata: str = '', name: Incomplete | None = None):
    '''Registers a dataset with the tf.data service.

  Args:
    dataset: A `Tensor` of type `variant`.
    address: A `Tensor` of type `string`.
    protocol: A `Tensor` of type `string`.
    external_state_policy: An `int`.
    element_spec: An optional `string`. Defaults to `""`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  '''

RegisterDataset: Incomplete

def register_dataset_eager_fallback(dataset, address, protocol, external_state_policy, element_spec, metadata, name, ctx): ...
def register_dataset_v2(dataset, address, protocol, external_state_policy, element_spec: str = '', requested_dataset_id: str = '', metadata: str = '', name: Incomplete | None = None):
    '''Registers a dataset with the tf.data service.

  Args:
    dataset: A `Tensor` of type `variant`.
    address: A `Tensor` of type `string`.
    protocol: A `Tensor` of type `string`.
    external_state_policy: An `int`.
    element_spec: An optional `string`. Defaults to `""`.
    requested_dataset_id: An optional `string`. Defaults to `""`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

RegisterDatasetV2: Incomplete

def register_dataset_v2_eager_fallback(dataset, address, protocol, external_state_policy, element_spec, requested_dataset_id, metadata, name, ctx): ...
def sampling_dataset(input_dataset, rate, seed, seed2, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that takes a Bernoulli sample of the contents of another dataset.

  There is no transformation in the `tf.data` Python API for creating this dataset.
  Instead, it is created as a result of the `filter_with_random_uniform_fusion`
  static optimization. Whether this optimization is performed is determined by the
  `experimental_optimization.filter_with_random_uniform_fusion` option of
  `tf.data.Options`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    rate: A `Tensor` of type `float32`.
      A scalar representing the sample rate. Each element of `input_dataset` is
      retained with this probability, independent of all other elements.
    seed: A `Tensor` of type `int64`.
      A scalar representing seed of random number generator.
    seed2: A `Tensor` of type `int64`.
      A scalar representing seed2 of random number generator.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

SamplingDataset: Incomplete

def sampling_dataset_eager_fallback(input_dataset, rate, seed, seed2, output_types, output_shapes, name, ctx): ...
def save_dataset(input_dataset, path, shard_func_other_args, shard_func, compression: str = '', use_shard_func: bool = True, name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    path: A `Tensor` of type `string`.
    shard_func_other_args: A list of `Tensor` objects.
    shard_func: A function decorated with @Defun.
    compression: An optional `string`. Defaults to `""`.
    use_shard_func: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

SaveDataset: Incomplete

def save_dataset_eager_fallback(input_dataset, path, shard_func_other_args, shard_func, compression, use_shard_func, name, ctx): ...
def save_dataset_v2(input_dataset, path, shard_func_other_args, shard_func, output_types, output_shapes, compression: str = '', use_shard_func: bool = True, name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    path: A `Tensor` of type `string`.
    shard_func_other_args: A list of `Tensor` objects.
    shard_func: A function decorated with @Defun.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    compression: An optional `string`. Defaults to `""`.
    use_shard_func: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

SaveDatasetV2: Incomplete

def save_dataset_v2_eager_fallback(input_dataset, path, shard_func_other_args, shard_func, output_types, output_shapes, compression, use_shard_func, name, ctx): ...
def scan_dataset(input_dataset, initial_state, other_arguments, f, output_types, output_shapes, preserve_cardinality: bool = False, use_default_device: bool = True, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset successively reduces `f` over the elements of `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    initial_state: A list of `Tensor` objects.
    other_arguments: A list of `Tensor` objects.
    f: A function decorated with @Defun.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    preserve_cardinality: An optional `bool`. Defaults to `False`.
    use_default_device: An optional `bool`. Defaults to `True`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

ScanDataset: Incomplete

def scan_dataset_eager_fallback(input_dataset, initial_state, other_arguments, f, output_types, output_shapes, preserve_cardinality, use_default_device, metadata, name, ctx): ...
def set_stats_aggregator_dataset(input_dataset, stats_aggregator, tag, counter_prefix, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    stats_aggregator: A `Tensor` of type `resource`.
    tag: A `Tensor` of type `string`.
    counter_prefix: A `Tensor` of type `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

SetStatsAggregatorDataset: Incomplete

def set_stats_aggregator_dataset_eager_fallback(input_dataset, stats_aggregator, tag, counter_prefix, output_types, output_shapes, name, ctx): ...
def sleep_dataset(input_dataset, sleep_microseconds, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    sleep_microseconds: A `Tensor` of type `int64`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

SleepDataset: Incomplete

def sleep_dataset_eager_fallback(input_dataset, sleep_microseconds, output_types, output_shapes, name, ctx): ...
def sliding_window_dataset(input_dataset, window_size, window_shift, window_stride, output_types, output_shapes, drop_remainder: bool = True, name: Incomplete | None = None):
    """Creates a dataset that passes a sliding window over `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    window_size: A `Tensor` of type `int64`.
      A scalar representing the number of elements in the
      sliding window.
    window_shift: A `Tensor` of type `int64`.
      A scalar representing the steps moving the sliding window
      forward in one iteration. It must be positive.
    window_stride: A `Tensor` of type `int64`.
      A scalar representing the stride of the input elements of the sliding window.
      It must be positive.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    drop_remainder: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

SlidingWindowDataset: Incomplete

def sliding_window_dataset_eager_fallback(input_dataset, window_size, window_shift, window_stride, output_types, output_shapes, drop_remainder, name, ctx): ...
def snapshot_dataset(input_dataset, path, output_types, output_shapes, compression: str = '', reader_path_prefix: str = '', writer_path_prefix: str = '', shard_size_bytes: int = 10737418240, pending_snapshot_expiry_seconds: int = 86400, num_reader_threads: int = 1, reader_buffer_size: int = 1, num_writer_threads: int = 1, writer_buffer_size: int = 1, shuffle_on_read: bool = False, seed: int = 0, seed2: int = 0, mode: str = 'auto', snapshot_name: str = '', name: Incomplete | None = None):
    '''Creates a dataset that will write to / read from a snapshot.

  This dataset attempts to determine whether a valid snapshot exists at the
  `snapshot_path`, and reads from the snapshot in lieu of using `input_dataset`.
  If not, it will run the preprocessing pipeline as usual, and write out a
  snapshot of the data processed for future use.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    path: A `Tensor` of type `string`.
      The path we should write snapshots to / read snapshots from.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    compression: An optional `string`. Defaults to `""`.
    reader_path_prefix: An optional `string`. Defaults to `""`.
    writer_path_prefix: An optional `string`. Defaults to `""`.
    shard_size_bytes: An optional `int`. Defaults to `10737418240`.
    pending_snapshot_expiry_seconds: An optional `int`. Defaults to `86400`.
    num_reader_threads: An optional `int`. Defaults to `1`.
    reader_buffer_size: An optional `int`. Defaults to `1`.
    num_writer_threads: An optional `int`. Defaults to `1`.
    writer_buffer_size: An optional `int`. Defaults to `1`.
    shuffle_on_read: An optional `bool`. Defaults to `False`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    mode: An optional `string`. Defaults to `"auto"`.
    snapshot_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

SnapshotDataset: Incomplete

def snapshot_dataset_eager_fallback(input_dataset, path, output_types, output_shapes, compression, reader_path_prefix, writer_path_prefix, shard_size_bytes, pending_snapshot_expiry_seconds, num_reader_threads, reader_buffer_size, num_writer_threads, writer_buffer_size, shuffle_on_read, seed, seed2, mode, snapshot_name, name, ctx): ...
def snapshot_dataset_reader(shard_dir, start_index, output_types, output_shapes, version, compression: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    shard_dir: A `Tensor` of type `string`.
    start_index: A `Tensor` of type `int64`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    version: An `int`.
    compression: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

SnapshotDatasetReader: Incomplete

def snapshot_dataset_reader_eager_fallback(shard_dir, start_index, output_types, output_shapes, version, compression, name, ctx): ...
def snapshot_dataset_v2(input_dataset, path, reader_func_other_args, shard_func_other_args, output_types, output_shapes, reader_func, shard_func, compression: str = '', reader_prefix: str = '', writer_prefix: str = '', hash_valid: bool = False, hash: int = 0, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that will write to / read from a snapshot.

  This dataset attempts to determine whether a valid snapshot exists at the
  `snapshot_path`, and reads from the snapshot in lieu of using `input_dataset`.
  If not, it will run the preprocessing pipeline as usual, and write out a
  snapshot of the data processed for future use.

  Args:
    input_dataset: A `Tensor` of type `variant`.
      A variant tensor representing the input dataset.
    path: A `Tensor` of type `string`.
      The path we should write snapshots to / read snapshots from.
    reader_func_other_args: A list of `Tensor` objects.
    shard_func_other_args: A list of `Tensor` objects.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    reader_func: A function decorated with @Defun.
      Optional. A function to control how to read data from snapshot shards.
    shard_func: A function decorated with @Defun.
      Optional. A function to control how to shard data when writing a snapshot.
    compression: An optional `string`. Defaults to `""`.
      The type of compression to be applied to the saved snapshot files.
    reader_prefix: An optional `string`. Defaults to `""`.
    writer_prefix: An optional `string`. Defaults to `""`.
    hash_valid: An optional `bool`. Defaults to `False`.
    hash: An optional `int`. Defaults to `0`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

SnapshotDatasetV2: Incomplete

def snapshot_dataset_v2_eager_fallback(input_dataset, path, reader_func_other_args, shard_func_other_args, output_types, output_shapes, reader_func, shard_func, compression, reader_prefix, writer_prefix, hash_valid, hash, metadata, name, ctx): ...
def snapshot_nested_dataset_reader(inputs, output_types, output_shapes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    inputs: A list of at least 1 `Tensor` objects with type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

SnapshotNestedDatasetReader: Incomplete

def snapshot_nested_dataset_reader_eager_fallback(inputs, output_types, output_shapes, name, ctx): ...
def sql_dataset(driver_name, data_source_name, query, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that executes a SQL query and emits rows of the result set.

  Args:
    driver_name: A `Tensor` of type `string`.
      The database type. Currently, the only supported type is 'sqlite'.
    data_source_name: A `Tensor` of type `string`.
      A connection string to connect to the database.
    query: A `Tensor` of type `string`. A SQL query to execute.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

SqlDataset: Incomplete

def sql_dataset_eager_fallback(driver_name, data_source_name, query, output_types, output_shapes, name, ctx): ...
def stats_aggregator_handle(container: str = '', shared_name: str = '', name: Incomplete | None = None):
    '''Creates a statistics manager resource.

  Args:
    container: An optional `string`. Defaults to `""`.
    shared_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

StatsAggregatorHandle: Incomplete

def stats_aggregator_handle_eager_fallback(container, shared_name, name, ctx): ...
def stats_aggregator_handle_v2(container: str = '', shared_name: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    container: An optional `string`. Defaults to `""`.
    shared_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

StatsAggregatorHandleV2: Incomplete

def stats_aggregator_handle_v2_eager_fallback(container, shared_name, name, ctx): ...
def stats_aggregator_set_summary_writer(stats_aggregator, summary, name: Incomplete | None = None):
    """Set a summary_writer_interface to record statistics using given stats_aggregator.

  Args:
    stats_aggregator: A `Tensor` of type `resource`.
    summary: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

StatsAggregatorSetSummaryWriter: Incomplete

def stats_aggregator_set_summary_writer_eager_fallback(stats_aggregator, summary, name, ctx): ...
def stats_aggregator_summary(iterator, name: Incomplete | None = None):
    """Produces a summary of any statistics recorded by the given statistics manager.

  Args:
    iterator: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

StatsAggregatorSummary: Incomplete

def stats_aggregator_summary_eager_fallback(iterator, name, ctx): ...
def take_while_dataset(input_dataset, other_arguments, predicate, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that stops iteration when predicate` is false.

  The `predicate` function must return a scalar boolean and accept the
  following arguments:

  * One tensor for each component of an element of `input_dataset`.
  * One tensor for each value in `other_arguments`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    other_arguments: A list of `Tensor` objects.
      A list of tensors, typically values that were captured when
      building a closure for `predicate`.
    predicate: A function decorated with @Defun.
      A function returning a scalar boolean.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

TakeWhileDataset: Incomplete

def take_while_dataset_eager_fallback(input_dataset, other_arguments, predicate, output_types, output_shapes, metadata, name, ctx): ...
def thread_pool_dataset(input_dataset, thread_pool, output_types, output_shapes, name: Incomplete | None = None):
    """Creates a dataset that uses a custom thread pool to compute `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    thread_pool: A `Tensor` of type `resource`.
      A resource produced by the ThreadPoolHandle op.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

ThreadPoolDataset: Incomplete

def thread_pool_dataset_eager_fallback(input_dataset, thread_pool, output_types, output_shapes, name, ctx): ...
def thread_pool_handle(num_threads, display_name, max_intra_op_parallelism: int = 1, container: str = '', shared_name: str = '', name: Incomplete | None = None):
    '''Creates a dataset that uses a custom thread pool to compute `input_dataset`.

  Args:
    num_threads: An `int`. The number of threads in the thread pool.
    display_name: A `string`.
      A human-readable name for the threads that may be visible in some
      visualizations.
      threadpool.
    max_intra_op_parallelism: An optional `int`. Defaults to `1`.
      The maximum degree of parallelism to use within operations that execute on this
      threadpool.
    container: An optional `string`. Defaults to `""`.
    shared_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

ThreadPoolHandle: Incomplete

def thread_pool_handle_eager_fallback(num_threads, display_name, max_intra_op_parallelism, container, shared_name, name, ctx): ...
def unbatch_dataset(input_dataset, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''A dataset that splits the elements of its input into multiple elements.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

UnbatchDataset: Incomplete

def unbatch_dataset_eager_fallback(input_dataset, output_types, output_shapes, metadata, name, ctx): ...
def uncompress_element(compressed, output_types, output_shapes, name: Incomplete | None = None):
    """Uncompresses a compressed dataset element.

  Args:
    compressed: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `output_types`.
  """

UncompressElement: Incomplete

def uncompress_element_eager_fallback(compressed, output_types, output_shapes, name, ctx): ...
def unique_dataset(input_dataset, output_types, output_shapes, metadata: str = '', name: Incomplete | None = None):
    '''Creates a dataset that contains the unique elements of `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    metadata: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  '''

UniqueDataset: Incomplete

def unique_dataset_eager_fallback(input_dataset, output_types, output_shapes, metadata, name, ctx): ...
