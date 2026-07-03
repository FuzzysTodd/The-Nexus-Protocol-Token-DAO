from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.distribute import input_lib as input_lib

def get_distributed_dataset(dataset, input_workers, strategy, num_replicas_in_sync: Incomplete | None = None, input_context: Incomplete | None = None, options: Incomplete | None = None, build: bool = True):
    """Returns a distributed dataset from the given tf.data.Dataset instance.

  This is a common function that is used by all strategies to return a
  distributed dataset. The distributed dataset instance returned is different
  depending on if we are in a TF 1 or TF 2 context. The distributed dataset
  instances returned differ from each other in the APIs supported by each of
  them.

  Args:
    dataset: a tf.data.Dataset instance.
    input_workers: an InputWorkers object which specifies devices on which
      iterators should be created.
    strategy: a `tf.distribute.Strategy` object, used to run all-reduce to
      handle last partial batch.
    num_replicas_in_sync: Optional integer. If this is not None, the value is
      used to decide how to rebatch datasets into smaller batches so that the
      total batch size for each step (across all workers and replicas) adds up
      to `dataset`'s batch size.
    input_context: `InputContext` for sharding. Only pass this in for between
      graph multi-worker cases where there is only one `input_worker`. In these
      cases, we will shard based on the `input_pipeline_id` and
      `num_input_pipelines` in the `InputContext`.
    options: Default is None. `tf.distribute.InputOptions` used to control
      options on how this dataset is distributed.
    build: whether to build underlying datasets when a DistributedDataset is
      created. This is only useful for `ParameterServerStrategy` now.

  Returns:
    A distributed dataset instance.
  """
def get_distributed_datasets_from_function(dataset_fn, input_workers, input_contexts, strategy, options: Incomplete | None = None, build: bool = True):
    """Returns a distributed dataset from the given input function.

  This is a common function that is used by all strategies to return a
  distributed dataset. The distributed dataset instance returned is different
  depending on if we are in a TF 1 or TF 2 context. The distributed dataset
  instances returned differ from each other in the APIs supported by each of
  them.

  Args:
    dataset_fn: a function that returns a tf.data.Dataset instance.
    input_workers: an InputWorkers object which specifies devices on which
      iterators should be created.
    input_contexts: A list of `InputContext` instances to be passed to call(s)
      to `dataset_fn`. Length and order should match worker order in
      `worker_device_pairs`.
    strategy: a `tf.distribute.Strategy` object, used to run all-reduce to
      handle last partial batch.
    options: Default is None. `tf.distribute.InputOptions` used to control
      options on how this dataset is distributed.
    build: whether to build underlying datasets when a
      `DistributedDatasetFromFunction` is created. This is only useful for
      `ParameterServerStrategy` now.

  Returns:
    A distributed dataset instance.

  Raises:
    ValueError: if `options.experimental_replication_mode` and
    `options.experimental_place_dataset_on_device` are not consistent
  """
