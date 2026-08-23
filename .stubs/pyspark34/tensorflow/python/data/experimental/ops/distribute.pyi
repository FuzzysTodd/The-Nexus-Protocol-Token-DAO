from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.ops.options import ExternalStatePolicy as ExternalStatePolicy
from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

SHARD_HINT: int

class _AutoShardDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that shards the `Dataset` automatically.

  This dataset takes in an existing dataset and tries to automatically figure
  out how to shard the dataset in a multi-worker scenario using graph rewrites.

  If the AutoShardPolicy is set to FILE, it walks up the dataset graph until
  it finds a reader dataset, then inserts a ShardDataset op before that node
  so that each worker only sees some files.

  If the AutoShardPolicy is set to DATA, it inserts a ShardDataset op at the
  end of the input pipeline, before any terminal PrefetchDataset if there is
  one. Additionally, if there is a RebatchDatasetV2 in the input pipeline, it
  is written to legacy RebatchDataset for correctness reasons, since
  RebatchDatasetV2 is incompatible with data sharding.

  If the AutoShardPolicy is set to AUTO, it tries to do file-based sharding.
  If it cannot find a reader dataset, it falls back to doing data-based
  sharding.

  If the AutoShardPolicy is set to OFF, it does nothing.

  Attributes:
    num_workers: Total number of workers to shard this dataset across.
    index: The current worker index (out of the total number of workers) this
      dataset is for.
    num_replicas: The total number of replicas across all workers. This is used
      only when sharding by data (either DATA or AUTO) in order to rewrite
      RebatchDatasetV2 to RebatchDataset.

  Raises:
    NotFoundError: If we cannot find a suitable reader dataset to begin
      automatically sharding the dataset.
  """
    def __init__(self, input_dataset, num_workers, index, num_replicas: Incomplete | None = None) -> None: ...
    @property
    def element_spec(self): ...

class _LegacyRebatchDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that divides its input batches into `num_replicas` sub-batches.

  For each batch in the input dataset, _LegacyRebatchDataset will produce
  `num_replicas` smaller batches whose sizes add up to the original batch size.

  For example:

  ```python
  ds = tf.data.Dataset.range(8)
  ds = ds.batch(4)
  ds = _LegacyRebatchDataset(ds, num_replicas=3)
  for elem in ds:
    print(elem)
  >> [0, 1], [2, 3], [], [4, 5], [6, 7], []
  ```
  """
    def __init__(self, input_dataset, num_replicas) -> None:
        """Creates a _LegacyRebatchDataset.

    Args:
      input_dataset: `Dataset` to rebatch.
      num_replicas: A `tf.int64` scalar, representing the number of sub-batches
        to split each batch from `input_dataset` into.
    """
    @property
    def element_spec(self): ...

class _RemoteDataset(dataset_ops.DatasetSource):
    """Creates a dataset on a given `device` given a graph def."""
    def __init__(self, graph_def, device, element_spec) -> None: ...
    @property
    def element_spec(self): ...

def replicate(dataset, devices):
    """A transformation that replicates `dataset` onto a list of devices.

  Args:
    dataset: A `tf.data.Dataset` object.
    devices: A list of devices to replicate the dataset on.

  Returns:
    A dictionary mapping device name to a dataset on that device.
  """
def batch_sizes_for_worker(global_batch_size, num_workers, num_replicas_per_worker, worker_index):
    '''Determines how to rebatch a dataset for the given worker.

  Given the global batch size, number of workers, number of replicas per worker,
  and worker index, returns the correct batch sizes for rebatching a dataset
  on worker `worker_index` of `num_workers`, such that each global step (across
  all workers and replicas) will consume global_batch_size elements. The
  returned value should be passed as the `batch_sizes` input parameter to
  `tf.data.experimental.rebatch()`. The returned batch sizes meet the following
  constraints:

  Let G = global_batch_size, W = num_workers, R = num_replicas_per_worker
  (A) for any worker, len(batch_sizes) = W * R
  (B) for any worker, sum(batch_sizes) == G
  (C) for any global step (i.e. R iterations on each worker), the sum of batches
      consumed by replicas across all workers is G.
  (D) any two batch sizes of any two replicas differs by at most one.

  For example, suppose we have G = 7, W = 2, R = 2, and suppose we have two
  files which each contain 7 elements:

  ```python
  # WORKER 0
  batch_sizes_0 = batch_sizes_for_worker(global_batch_size=global_batch_size,
                                         num_workers=2,
                                         num_replicas_per_worker=2,
                                         worker_index=0)
  print(batch_sizes_0)
  >> [2, 2, 2, 1]

  dataset_0 = tf.data.Dataset.from_tensor_slices(["file_a", "file_b"])
  dataset_0 = dataset_0.shard(num_shards, index=0)
  dataset_0 = dataset_0.batch(7)
  dataset_0 = dataset_0.apply(tf.data.experimental.rebatch(batch_sizes_0))
  for elem in dataset_0:
    print(elem)
  >> [[A0, A1], [A2, A3], [A4, A5], [A6]]

  # WORKER 1
  batch_sizes_1 = batch_sizes_for_worker(global_batch_size=global_batch_size,
                                         num_workers=2,
                                         num_replicas_per_worker=2,
                                         worker_index=1)
  print(batch_sizes_1)
  >> [2, 1, 2, 2]

  dataset_1 = tf.data.Dataset.from_tensor_slices(["file_a", "file_b"])
  dataset_1 = dataset_1.shard(num_shards, index=1)
  dataset_1 = dataset_1.batch(7)
  dataset_1 = dataset_1.apply(tf.data.experimental.rebatch(batch_sizes_1))
  for elem in dataset_1:
    print(elem)
  >> [[B0, B1], [B2], [B3, B4], [B5, B6]]
  ```

  The above example will produce the following elements:

  Step 1:
    Worker 0 Replica 0: [A0, A1]
    Worker 0 Replica 1: [A2, A3]
    Worker 1 Replica 0: [B0, B1]
    Worker 1 Replica 1: [B2]
  Total batch size = 7

  Step 2:
    Worker 0 Replica 0: [A4, A5]
    Worker 0 Replica 1: [A6]
    Worker 1 Replica 0: [B3, B4]
    Worker 1 Replica 1: [B5, B6]
  Total batch size = 7

  Args:
    global_batch_size: A `tf.int64` scalar, representing the global batch size.
    num_workers: An integer representing the number of workers the dataset will
      be distributed across.
    num_replicas_per_worker: An integer representing the number of replicas per
      worker. All workers are assumed to have the same number of replicas.
    worker_index: An integer index of the worker to be rebatched.

  Returns:
    A `tf.int64` vector, representing the batch sizes to rebatch the dataset
    into.
  '''
def compute_batch_size(dataset):
    """An operation that returns the batch size of the dataset.

  This op tries to infer the batch size statically by walking up the dataset
  tree from the final dataset node and returning the batch size of the first
  batching dataset (such as from .batch() and .padded_batch()) that it
  encounters. This differs from using the `element_spec` of a dataset in that it
  does not account for partial batches.

  This operation may fail if it encounters contradictory batch sizes (for
  example, if the dataset is created by zipping together two datasets with
  different batch sizes), if there are no explicit batching transformations, or
  if there are operations downstream from the batching transformation that may
  modify its batch size. In these cases, it returns a -1.

  Args:
    dataset: A `tf.data.Dataset` object.

  Returns:
    A `tf.int64` Tensor representing the batch size of the dataset sans partial
    batches. If this cannot be inferred statically, the value of this tensor
    will be -1.
  """
