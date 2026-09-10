import abc
from _typeshed import Incomplete
from tensorflow.python.autograph.operators import py_builtins as py_builtins
from tensorflow.python.data.experimental.ops import batching as batching, distribute as distribute
from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops, multi_device_iterator_ops as multi_device_iterator_ops, optional_ops as optional_ops
from tensorflow.python.distribute import device_util as device_util, distribute_lib as distribute_lib, distribute_utils as distribute_utils, distribution_strategy_context as distribution_strategy_context, input_ops as input_ops, reduce_util as reduce_util, values as values
from tensorflow.python.distribute.distribute_lib import InputReplicationMode as InputReplicationMode
from tensorflow.python.eager import context as context, monitoring as monitoring
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, errors as errors, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.types import distribute as distribute_types
from tensorflow.python.util import nest as nest
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls

def get_iterator_spec_from_dataset(strategy, dataset):
    """Returns an iterator spec from dataset function.

  This function constructs type spec for iterator obtained from
  iter(dataset).

  Args:
    strategy: a `tf.distribute.Strategy` object, used to run all-reduce to
        handle last partial batch.
    dataset: A tf.data.Dataset instance. If using a function that returns a
      tf.data.Dataset instance, pass dataset_fn.structured_outputs.

  Returns:
    A type_spec for iterator for dataset instance.

  """

class DistributedIteratorInterface(collections_abc.Iterator, distribute_types.Iterator, metaclass=abc.ABCMeta):
    """An iterator over `tf.distribute.DistributedDataset`.

  `tf.distribute.DistributedIterator` is the primary mechanism for enumerating
  elements of a `tf.distribute.DistributedDataset`. It supports the Python
  Iterator protocol, which means it can be iterated over using a for-loop or by
  fetching individual elements explicitly via `get_next()`.

  You can create a `tf.distribute.DistributedIterator` by calling `iter` on
  a `tf.distribute.DistributedDataset` or creating a python loop over a
  `tf.distribute.DistributedDataset`.

  Visit the [tutorial](https://www.tensorflow.org/tutorials/distribute/input)
  on distributed input for more examples and caveats.
  """
    def get_next(self) -> None:
        '''Returns the next input from the iterator for all replicas.

    Example use:

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> dataset = tf.data.Dataset.range(100).batch(2)
    >>> dist_dataset = strategy.experimental_distribute_dataset(dataset)
    >>> dist_dataset_iterator = iter(dist_dataset)
    >>> @tf.function
    ... def one_step(input):
    ...   return input
    >>> step_num = 5
    >>> for _ in range(step_num):
    ...   strategy.run(one_step, args=(dist_dataset_iterator.get_next(),))
    >>> strategy.experimental_local_results(dist_dataset_iterator.get_next())
    (<tf.Tensor: shape=(1,), dtype=int64, numpy=array([10])>,
     <tf.Tensor: shape=(1,), dtype=int64, numpy=array([11])>)

    Returns:
      A single `tf.Tensor` or a `tf.distribute.DistributedValues` which contains
      the next input for all replicas.

    Raises:
      `tf.errors.OutOfRangeError`: If the end of the iterator has been reached.
    '''
    @property
    def element_spec(self) -> None:
        '''The type specification of an element of `tf.distribute.DistributedIterator`.

    Example usage:

    >>> global_batch_size = 16
    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> dataset = tf.data.Dataset.from_tensors(([1.],[2])).repeat(100).batch(global_batch_size)
    >>> distributed_iterator = iter(strategy.experimental_distribute_dataset(dataset))
    >>> distributed_iterator.element_spec
    (PerReplicaSpec(TensorSpec(shape=(None, 1), dtype=tf.float32, name=None),
                    TensorSpec(shape=(None, 1), dtype=tf.float32, name=None)),
     PerReplicaSpec(TensorSpec(shape=(None, 1), dtype=tf.int32, name=None),
                    TensorSpec(shape=(None, 1), dtype=tf.int32, name=None)))

    Returns:
      A nested structure of `tf.TypeSpec` objects matching the structure of an
      element of this `tf.distribute.DistributedIterator`. This returned value
      is typically a `tf.distribute.DistributedValues` object and specifies the
      `tf.TensorSpec` of individual components.
    '''
    def get_next_as_optional(self) -> None:
        '''Returns a `tf.experimental.Optional` that contains the next value for all replicas.

    If the `tf.distribute.DistributedIterator` has reached the end of the
    sequence, the returned `tf.experimental.Optional` will have no value.

    Example usage:

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> global_batch_size = 2
    >>> steps_per_loop = 2
    >>> dataset = tf.data.Dataset.range(10).batch(global_batch_size)
    >>> distributed_iterator = iter(
    ...     strategy.experimental_distribute_dataset(dataset))
    >>> def step_fn(x):
    ...   # train the model with inputs
    ...   return x
    >>> @tf.function
    ... def train_fn(distributed_iterator):
    ...   for _ in tf.range(steps_per_loop):
    ...     optional_data = distributed_iterator.get_next_as_optional()
    ...     if not optional_data.has_value():
    ...       break
    ...     per_replica_results = strategy.run(step_fn, args=(optional_data.get_value(),))
    ...     tf.print(strategy.experimental_local_results(per_replica_results))
    >>> train_fn(distributed_iterator)
    ... # ([0 1], [2 3])
    ... # ([4], [])

    Returns:
      An `tf.experimental.Optional` object representing the next value from the
      `tf.distribute.DistributedIterator` (if it has one) or no value.
    '''

class DistributedDatasetInterface(collections_abc.Iterable, distribute_types.Iterable):
    '''Represents a dataset distributed among devices and machines.

  A `tf.distribute.DistributedDataset` could be thought of as a "distributed"
  dataset. When you use `tf.distribute` API to scale training to multiple
  devices or machines, you also need to distribute the input data, which leads
  to a `tf.distribute.DistributedDataset` instance, instead of a
  `tf.data.Dataset` instance in the non-distributed case. In TF 2.x,
  `tf.distribute.DistributedDataset` objects are Python iterables.

  Note: `tf.distribute.DistributedDataset` instances are *not* of type
  `tf.data.Dataset`. It only supports two usages we will mention below:
  iteration and `element_spec`. We don\'t support any other APIs to transform or
  inspect the dataset.

  There are two APIs to create a `tf.distribute.DistributedDataset` object:
  `tf.distribute.Strategy.experimental_distribute_dataset(dataset)`and
  `tf.distribute.Strategy.distribute_datasets_from_function(dataset_fn)`.
  *When to use which?* When you have a `tf.data.Dataset` instance, and the
  regular batch splitting (i.e. re-batch the input `tf.data.Dataset` instance
  with a new batch size that is equal to the global batch size divided by the
  number of replicas in sync) and autosharding (i.e. the
  `tf.data.experimental.AutoShardPolicy` options) work for you, use the former
  API. Otherwise, if you are *not* using a canonical `tf.data.Dataset` instance,
  or you would like to customize the batch splitting or sharding, you can wrap
  these logic in a `dataset_fn` and use the latter API. Both API handles
  prefetch to device for the user. For more details and examples, follow the
  links to the APIs.


  There are two main usages of a `DistributedDataset` object:

  1. Iterate over it to generate the input for a single device or multiple
  devices, which is a `tf.distribute.DistributedValues` instance. To do this,
  you can:

    * use a pythonic for-loop construct:

      >>> global_batch_size = 4
      >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
      >>> dataset = tf.data.Dataset.from_tensors(([1.],[1.])).repeat(4).batch(global_batch_size)
      >>> dist_dataset = strategy.experimental_distribute_dataset(dataset)
      >>> @tf.function
      ... def train_step(input):
      ...   features, labels = input
      ...   return labels - 0.3 * features
      >>> for x in dist_dataset:
      ...   # train_step trains the model using the dataset elements
      ...   loss = strategy.run(train_step, args=(x,))
      ...   print("Loss is", loss)
      Loss is PerReplica:{
        0: tf.Tensor(
      [[0.7]
       [0.7]], shape=(2, 1), dtype=float32),
        1: tf.Tensor(
      [[0.7]
       [0.7]], shape=(2, 1), dtype=float32)
      }

      Placing the loop inside a `tf.function` will give a performance boost.
      However `break` and `return` are currently not supported if the loop is
      placed inside a `tf.function`. We also don\'t support placing the loop
      inside a `tf.function` when using
      `tf.distribute.experimental.MultiWorkerMirroredStrategy` or
      `tf.distribute.experimental.TPUStrategy` with multiple workers.

    * use `__iter__` to create an explicit iterator, which is of type
      `tf.distribute.DistributedIterator`

      >>> global_batch_size = 4
      >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
      >>> train_dataset = tf.data.Dataset.from_tensors(([1.],[1.])).repeat(50).batch(global_batch_size)
      >>> train_dist_dataset = strategy.experimental_distribute_dataset(train_dataset)
      >>> @tf.function
      ... def distributed_train_step(dataset_inputs):
      ...   def train_step(input):
      ...     loss = tf.constant(0.1)
      ...     return loss
      ...   per_replica_losses = strategy.run(train_step, args=(dataset_inputs,))
      ...   return strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses,axis=None)
      >>> EPOCHS = 2
      >>> STEPS = 3
      >>> for epoch in range(EPOCHS):
      ...   total_loss = 0.0
      ...   num_batches = 0
      ...   dist_dataset_iterator = iter(train_dist_dataset)
      ...   for _ in range(STEPS):
      ...     total_loss += distributed_train_step(next(dist_dataset_iterator))
      ...     num_batches += 1
      ...   average_train_loss = total_loss / num_batches
      ...   template = ("Epoch {}, Loss: {:.4f}")
      ...   print (template.format(epoch+1, average_train_loss))
      Epoch 1, Loss: 0.2000
      Epoch 2, Loss: 0.2000


    To achieve a performance improvement, you can also wrap the `strategy.run`
    call with a `tf.range` inside a `tf.function`. This runs multiple steps in a
    `tf.function`. Autograph will convert it to a `tf.while_loop` on the worker.
    However, it is less flexible comparing with running a single step inside
    `tf.function`. For example, you cannot run things eagerly or arbitrary
    python code within the steps.


  2. Inspect the `tf.TypeSpec` of the data generated by `DistributedDataset`.

    `tf.distribute.DistributedDataset` generates
    `tf.distribute.DistributedValues` as input to the devices. If you pass the
    input to a `tf.function` and would like to specify the shape and type of
    each Tensor argument to the function, you can pass a `tf.TypeSpec` object to
    the `input_signature` argument of the `tf.function`. To get the
    `tf.TypeSpec` of the input, you can use the `element_spec` property of the
    `tf.distribute.DistributedDataset` or `tf.distribute.DistributedIterator`
    object.

    For example:

    >>> global_batch_size = 4
    >>> epochs = 1
    >>> steps_per_epoch = 1
    >>> mirrored_strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> dataset = tf.data.Dataset.from_tensors(([2.])).repeat(100).batch(global_batch_size)
    >>> dist_dataset = mirrored_strategy.experimental_distribute_dataset(dataset)
    >>> @tf.function(input_signature=[dist_dataset.element_spec])
    ... def train_step(per_replica_inputs):
    ...   def step_fn(inputs):
    ...     return tf.square(inputs)
    ...   return mirrored_strategy.run(step_fn, args=(per_replica_inputs,))
    >>> for _ in range(epochs):
    ...   iterator = iter(dist_dataset)
    ...   for _ in range(steps_per_epoch):
    ...     output = train_step(next(iterator))
    ...     print(output)
    PerReplica:{
      0: tf.Tensor(
    [[4.]
     [4.]], shape=(2, 1), dtype=float32),
      1: tf.Tensor(
    [[4.]
     [4.]], shape=(2, 1), dtype=float32)
    }


  Visit the [tutorial](https://www.tensorflow.org/tutorials/distribute/input)
  on distributed input for more examples and caveats.
  '''
    def __iter__(self):
        '''Creates an iterator for the `tf.distribute.DistributedDataset`.

    The returned iterator implements the Python Iterator protocol.

    Example usage:

    >>> global_batch_size = 4
    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4]).repeat().batch(global_batch_size)
    >>> distributed_iterator = iter(strategy.experimental_distribute_dataset(dataset))
    >>> print(next(distributed_iterator))
    PerReplica:{
      0: tf.Tensor([1 2], shape=(2,), dtype=int32),
      1: tf.Tensor([3 4], shape=(2,), dtype=int32)
    }

    Returns:
      An `tf.distribute.DistributedIterator` instance for the given
      `tf.distribute.DistributedDataset` object to enumerate over the
      distributed data.
    '''
    @property
    def element_spec(self) -> None:
        '''The type specification of an element of this `tf.distribute.DistributedDataset`.

    Example usage:

    >>> global_batch_size = 16
    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> dataset = tf.data.Dataset.from_tensors(([1.],[2])).repeat(100).batch(global_batch_size)
    >>> dist_dataset = strategy.experimental_distribute_dataset(dataset)
    >>> dist_dataset.element_spec
    (PerReplicaSpec(TensorSpec(shape=(None, 1), dtype=tf.float32, name=None),
                    TensorSpec(shape=(None, 1), dtype=tf.float32, name=None)),
     PerReplicaSpec(TensorSpec(shape=(None, 1), dtype=tf.int32, name=None),
                    TensorSpec(shape=(None, 1), dtype=tf.int32, name=None)))

    Returns:
      A nested structure of `tf.TypeSpec` objects matching the structure of an
      element of this `tf.distribute.DistributedDataset`. This returned value is
      typically a `tf.distribute.DistributedValues` object and specifies the
      `tf.TensorSpec` of individual components.
    '''
    def reduce(self, initial_state, reduce_func) -> None: ...

class InputWorkers:
    """A 1-to-many mapping from input worker devices to compute devices."""
    def __init__(self, worker_device_pairs, canonicalize_devices: bool = True) -> None:
        """Initialize an `InputWorkers` object.

    Args:
      worker_device_pairs: A sequence of pairs: `(input device, a tuple of
        compute devices fed by that input device)`.
      canonicalize_devices: Whether to canonicalize devices for workers fully or
        partially. If False, it will partially canonicalize devices by removing
        job and task.
    """
    @property
    def num_workers(self): ...
    @property
    def worker_devices(self): ...
    def compute_devices_for_worker(self, worker_index): ...
    def serialize(self): ...
    def deserialize(self, serialized): ...

class DistributedIteratorBase(DistributedIteratorInterface):
    """Common implementation for all input iterators."""
    def __init__(self, input_workers, iterators, strategy, cardinality, enable_get_next_as_optional) -> None: ...
    def next(self): ...
    def __next__(self): ...
    def __iter__(self): ...
    def get_next_as_optional(self): ...
    def get_next(self, name: Incomplete | None = None):
        """Returns the next input from the iterator for all replicas."""

class DistributedDatasetAndIteratorSpec(type_spec.TypeSpec, metaclass=abc.ABCMeta):
    """Common Type specification for `DistributedDataset and DistributedDatasetsFromFunction."""
    def __init__(self, input_workers, element_spec, strategy, options, cardinality=..., enable_get_next_as_optional: Incomplete | None = None) -> None: ...
    def sanity_check_type(self, other) -> None:
        """Returns the most specific TypeSpec compatible with `self` and `other`.

    Args:
      other: A `TypeSpec`.

    Raises:
      ValueError: If there is no TypeSpec that is compatible with both `self`
        and `other`.
    """
    def is_subtype_of(self, other):
        """Returns True if `self` is subtype of `other`.

    Args:
      other: A `TypeSpec`.
    """
    def most_specific_common_supertype(self, others):
        """Returns the most specific supertype of `self` and `others`.

    Args:
      others: A Sequence of `TypeSpec`.

    Returns `None` if a supertype does not exist.
    """

class DistributedIteratorSpec(DistributedDatasetAndIteratorSpec):
    """Type specification for `DistributedIterator`."""
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value): ...

class DistributedIterator(DistributedIteratorBase, composite_tensor.CompositeTensor):
    """Input Iterator for a distributed dataset."""
    def __init__(self, input_workers: Incomplete | None = None, iterators: Incomplete | None = None, strategy: Incomplete | None = None, components: Incomplete | None = None, element_spec: Incomplete | None = None, cardinality=..., enable_get_next_as_optional: bool = False, options: Incomplete | None = None) -> None: ...
    @property
    def element_spec(self): ...

class _IterableInput(DistributedDatasetInterface):
    """Base class for iterable inputs for distribution strategies."""
    def __init__(self, input_workers) -> None: ...
    def __iter__(self): ...
    def reduce(self, initial_state, reduce_fn):
        """Execute a `reduce_fn` over all the elements of the input."""

class DistributedDatasetSpec(DistributedDatasetAndIteratorSpec):
    """Type specification for `DistributedDataset."""
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value): ...

class DistributedDataset(_IterableInput, composite_tensor.CompositeTensor):
    """Distributed dataset that supports prefetching to multiple devices."""
    def __init__(self, input_workers, strategy, dataset: Incomplete | None = None, num_replicas_in_sync: Incomplete | None = None, input_context: Incomplete | None = None, components: Incomplete | None = None, element_spec: Incomplete | None = None, enable_get_next_as_optional: Incomplete | None = None, build: bool = True, options: Incomplete | None = None) -> None:
        """Distribute the dataset on all workers.

    If `num_replicas_in_sync` is not None, we split each batch of the dataset
    into `num_replicas_in_sync` smaller batches, to be distributed among that
    worker's replicas, so that the batch size for a global step (across all
    workers and replicas) is as expected.

    Args:
      input_workers: an `InputWorkers` object.
      strategy: a `tf.distribute.Strategy` object, used to run all-reduce to
        handle last partial batch.
      dataset: `tf.data.Dataset` that will be used as the input source. Either
        dataset or components field should be passed when constructing
        DistributedDataset. Use this when contructing DistributedDataset from a
        new `tf.data.Dataset`. Use components when constructing using
        DistributedDatasetSpec.
      num_replicas_in_sync: Optional integer. If this is not None, the value
        is used to decide how to rebatch datasets into smaller batches so that
        the total batch size for each step (across all workers and replicas)
        adds up to `dataset`'s batch size.
      input_context: `InputContext` for sharding. Only pass this in for between
        graph multi-worker cases where there is only one `input_worker`. In
        these cases, we will shard based on the `input_pipeline_id` and
        `num_input_pipelines` in the `InputContext`.
      components: datasets when DistributedDataset is constructed from
        DistributedDatasetSpec. Either field dataset or components should be
        passed.
      element_spec: element spec for DistributedDataset when constructing from
        DistributedDatasetSpec. This will be used to set the element_spec for
        DistributedDataset and verified against element_spec from components.
      enable_get_next_as_optional: this is required when components is passed
        instead of dataset.
      build: whether to build underlying datasets when this object is created.
        This is only useful for `ParameterServerStrategy` now.
      options: `tf.distribute.InputOptions` used to control options on how this
        dataset is distributed.
    """
    def build(self, dataset_to_replace: Incomplete | None = None) -> None: ...
    @property
    def cardinality(self): ...
    def __iter__(self): ...
    @property
    def element_spec(self):
        """The type specification of an element of this dataset."""

class DistributedDatasetsFromFunctionSpec(DistributedDatasetAndIteratorSpec):
    """Type specification for `DistributedDatasetsFromFunction."""
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value): ...

class DistributedDatasetsFromFunction(_IterableInput, composite_tensor.CompositeTensor):
    """Inputs created from dataset function."""
    def __init__(self, input_workers, strategy, input_contexts: Incomplete | None = None, dataset_fn: Incomplete | None = None, options: Incomplete | None = None, components: Incomplete | None = None, element_spec: Incomplete | None = None, build: bool = True) -> None:
        """Makes an iterable from datasets created by the given function.

    Args:
      input_workers: an `InputWorkers` object.
      strategy: a `tf.distribute.Strategy` object, used to run all-reduce to
        handle last partial batch.
      input_contexts: A list of `InputContext` instances to be passed to call(s)
        to `dataset_fn`. Length and order should match worker order in
        `worker_device_pairs`.
      dataset_fn: A function that returns a `Dataset` given an `InputContext`.
        Either dataset_fn or components should be passed to construct
        DistributedDatasetsFromFunction. Use this when constructing
        DistributedDataset using a function. Use components when constructing
        using DistributedDatasetsFromFunctionSpec.
      options: `tf.distribute.InputOptions` used to control options on how this
        dataset is distributed.
      components: datasets when DistributedDatasetsFromFunction is constructed
        from DistributedDatasetsFromFunctionSpec. Only one of dataset or
        components should be passed.
      element_spec: element spec for DistributedDataset when constructing from
        DistributedDatasetSpec. This will be used to set the element_spec for
        DistributedDatasetsFromFunctionSpec and verified against element_spec
        from components.
      build: whether to build underlying datasets when this object is created.
        This is only useful for `ParameterServerStrategy` now.
    """
    def build(self) -> None: ...
    @property
    def cardinality(self): ...
    def __iter__(self): ...
    @property
    def element_spec(self):
        """The type specification of an element of this dataset."""

class _SingleWorkerDatasetIteratorBase:
    """Iterator for a single `tf.data.Dataset`."""
    def __init__(self, dataset, worker, devices, options: Incomplete | None = None) -> None:
        """Create iterator for the `dataset` to fetch data to worker's `devices` .

    A `MultiDeviceIterator`  or `OwnedMultiDeviceIterator` is used to prefetch
    input to the devices on the given worker.

    Args:
      dataset: A `tf.data.Dataset` instance.
      worker: Worker on which ops should be created.
      devices: Distribute data from `dataset` to these devices.
      options: options.
    """
    def get_next(self, device, name: Incomplete | None = None):
        """Get next element for the given device."""
    def get_next_as_list(self, name: Incomplete | None = None):
        """Get next element from the underlying iterator.

    Runs the iterator get_next() within a device scope. Since this doesn't use
    get_next_as_optional(), it is considerably faster than get_next_as_list(),
    but it raises EOFError if any of the device doesn't get any data.

    Args:
      name: not used.

    Returns:
      A list consisting of the next data from each device.
    """
    def get_next_as_optional_list(self): ...

class _SingleWorkerDatasetIteratorSpec(type_spec.TypeSpec):
    """Type specification for `_SingleWorkerOwnedDatasetIterator`."""
    def __init__(self, worker, devices, element_spec, options, canonicalize_devices: bool = True) -> None: ...
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value): ...

class _SingleWorkerOwnedDatasetIterator(_SingleWorkerDatasetIteratorBase, composite_tensor.CompositeTensor):
    """Iterator for a DistributedDataset instance."""
    def __init__(self, dataset: Incomplete | None = None, worker: Incomplete | None = None, devices: Incomplete | None = None, components: Incomplete | None = None, element_spec: Incomplete | None = None, options: Incomplete | None = None, canonicalize_devices: Incomplete | None = None) -> None:
        """Create iterator for the `dataset` to fetch data to worker's `devices` .

    `OwnedMultiDeviceIterator` is used to prefetch input to the devices on the
    given worker. The lifetime of this iterator is tied to the encompassing
    python object. Once we go out of scope of the python object or return from
    a tf.function the underlying iterator resource is deleted.

    Args:
      dataset: A `tf.data.Dataset` instance.
      worker: Worker on which ops should be created.
      devices: Distribute data from `dataset` to these devices.
      components: Tensor components to construct the
        _SingleWorkerOwnedDatasetIterator from.
      element_spec: A nested structure of `TypeSpec` objects that represents the
      type specification of elements of the iterator.
      options: `tf.distribute.InputOptions` used to control options on how this
      dataset is distributed.
      canonicalize_devices: Whether to canonicalize devices for workers fully or
      partially. If False, it will partially canonicalize devices by removing
      job and task.
    """
    @property
    def element_spec(self): ...
    @property
    def output_classes(self):
        """Returns the class of each component of an element of this iterator.

    The expected values are `tf.Tensor` and `tf.SparseTensor`.

    Returns:
      A nested structure of Python `type` objects corresponding to each
      component of an element of this dataset.
    """
    @property
    def output_shapes(self):
        """Returns the shape of each component of an element of this iterator.

    Returns:
      A nested structure of `tf.TensorShape` objects corresponding to each
      component of an element of this dataset.
    """
    @property
    def output_types(self):
        """Returns the type of each component of an element of this iterator.

    Returns:
      A nested structure of `tf.DType` objects corresponding to each component
      of an element of this dataset.
    """

class MultiStepContext:
    """A context object that can be used to capture things when running steps.

  This context object is useful when running multiple steps at a time using the
  `experimental_run_steps_on_iterator` API. For e.g. it allows the user's step
  function to specify which outputs to emit at what frequency. Currently it
  supports capturing output from the last step, as well as capturing non tensor
  outputs.  In the future it will be augmented to support other use cases such
  as output each N steps.
  """
    def __init__(self) -> None:
        """Initialize an output context.

    Returns:
      A context object.
    """
    @property
    def last_step_outputs(self):
        """A dictionary consisting of outputs to be captured on last step.

    Keys in the dictionary are names of tensors to be captured, as specified
    when `set_last_step_output` is called.
    Values in the dictionary are the tensors themselves. If
    `set_last_step_output` was called with a `reduce_op` for this output,
    then the value is the reduced value.

    Returns:
      A dictionary with last step outputs.
    """
    def set_last_step_output(self, name, output, reduce_op: Incomplete | None = None) -> None:
        """Set `output` with `name` to be outputted from the last step.

    Args:
      name: String, name to identify the output. Doesn't need to match tensor
        name.
      output: The tensors that should be outputted with `name`. See below for
        actual types supported.
      reduce_op: Reduction method to use to reduce outputs from multiple
        replicas. Required if `set_last_step_output` is called in a replica
        context. Optional in cross_replica_context.
        When present, the outputs from all the replicas are reduced using the
        current distribution strategy's `reduce` method. Hence, the type of
        `output` must be what's supported by the corresponding `reduce` method.
        For e.g. if using MirroredStrategy and reduction is set, output
        must be a `PerReplica` value.
        The reduce method is also recorded in a dictionary
        `_last_step_outputs_reduce_ops` for later interpreting of the
        outputs as already reduced or not.
    """
    @property
    def non_tensor_outputs(self):
        """A dictionary consisting of any non tensor outputs to be captured."""
    def set_non_tensor_output(self, name, output) -> None:
        """Set `output` with `name` to be captured as a non tensor output."""
