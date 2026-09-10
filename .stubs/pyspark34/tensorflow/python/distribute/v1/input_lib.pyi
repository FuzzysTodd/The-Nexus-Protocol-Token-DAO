from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, multi_device_iterator_ops as multi_device_iterator_ops, optional_ops as optional_ops
from tensorflow.python.distribute import input_lib as input_lib
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops
from tensorflow.python.util.deprecation import deprecated as deprecated

class DistributedDatasetV1(input_lib.DistributedDataset):
    """Distributed dataset that supports prefetching to multiple devices."""
    def __init__(self, dataset, input_workers, strategy, num_replicas_in_sync: Incomplete | None = None, input_context: Incomplete | None = None, options: Incomplete | None = None) -> None: ...
    def make_one_shot_iterator(self):
        """Get a one time use iterator for DistributedDatasetV1.

    Note: This API is deprecated. Please use `for ... in dataset:` to iterate
    over the dataset or `iter` to create an iterator.

    Returns:
      A DistributedIteratorV1 instance.
    """
    def make_initializable_iterator(self):
        """Get an initializable iterator for DistributedDatasetV1.

    Note: This API is deprecated. Please use
    `tf.compat.v1.data.make_initializable_iterator(dataset)` to create an
    initializable iterator.

    Returns:
      A DistributedIteratorV1 instance.
    """
    def __iter__(self): ...

class DistributedDatasetsFromFunctionV1(input_lib.DistributedDatasetsFromFunction):
    """Inputs created from dataset function."""
    def __iter__(self): ...

class DistributedIteratorV1(input_lib.DistributedIteratorBase):
    """Input Iterator for a distributed dataset."""
    def initialize(self):
        """Initialize underlying iterators.

    Returns:
      A list of any initializer ops that should be run.
    """
    @property
    def initializer(self):
        """Returns a list of ops that initialize the iterator."""
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
    def get_iterator(self, worker): ...
    @property
    def element_spec(self):
        """The type specification of an element of this iterator."""

class DatasetIterator(DistributedIteratorV1):
    """Iterator created from input dataset."""
    def __init__(self, dataset, input_workers, strategy, num_replicas_in_sync: Incomplete | None = None, input_context: Incomplete | None = None) -> None:
        """Make an iterator for the dataset on given devices.

    If `num_replicas_in_sync` is not None, we split each batch of the dataset
    into `num_replicas_in_sync` smaller batches, to be distributed among that
    worker's replicas, so that the batch size for a global step (across all
    workers and replicas) is as expected.

    Args:
      dataset: `tf.data.Dataset` that will be used as the input source.
      input_workers: an `InputWorkers` object.
      strategy: a `tf.distribute.Strategy` object, used to run all-reduce to
        handle last partial batch.
      num_replicas_in_sync: Optional integer. If this is not None, the value is
        used to decide how to rebatch datasets into smaller batches so that the
        total batch size for each step (across all workers and replicas) adds up
        to `dataset`'s batch size.
      input_context: `InputContext` for sharding. Only pass this in for between
        graph multi-worker cases where there is only one `input_worker`. In
        these cases, we will shard based on the `input_pipeline_id` and
        `num_input_pipelines` in the `InputContext`.
    """

class InputFunctionIterator(DistributedIteratorV1):
    """Iterator created from input function."""
    def __init__(self, input_fn, input_workers, input_contexts, strategy) -> None:
        """Make an iterator for input provided via an input function.

    Currently implements PER_WORKER mode, in which the `input_fn` is called
    once on each worker.

    TODO(priyag): Add other replication modes.

    Args:
      input_fn: Input function that returns a `tf.data.Dataset` object.
      input_workers: an `InputWorkers` object.
      input_contexts: A list of `InputContext` instances to be passed to call(s)
        to `input_fn`. Length and order should match worker order in
        `worker_device_pairs`.
      strategy: a `tf.distribute.Strategy` object, used to run all-reduce to
        handle last partial batch.
    """

class _SingleWorkerDatasetIterator(input_lib._SingleWorkerDatasetIteratorBase):
    """Iterator for a single DistributedDatasetV1 instance."""
    def initialize(self):
        """Initialize underlying iterator.

    In eager execution, this simply recreates the underlying iterator.
    In graph execution, it returns the initializer ops for the underlying
    iterator.

    Returns:
      A list of any initializer ops that should be run.
    """
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...

class _SingleWorkerCallableIterator:
    """Iterator for a single tensor-returning callable."""
    def __init__(self, fn, worker, devices) -> None: ...
    def get_next(self, device, name: Incomplete | None = None):
        """Get next element for the given device from the callable."""
    def get_next_as_list(self, name: Incomplete | None = None):
        """Get next element from the callable."""
    def get_next_as_optional_list(self): ...
    def initialize(self): ...
