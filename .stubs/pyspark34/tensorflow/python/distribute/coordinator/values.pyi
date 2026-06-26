import enum
from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.ops.options import ExternalStatePolicy as ExternalStatePolicy
from tensorflow.python.distribute import input_lib as input_lib
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import composite_tensor as composite_tensor, errors as errors, ops as ops, type_spec as type_spec_lib
from tensorflow.python.ops import array_ops as array_ops, gen_dataset_ops as gen_dataset_ops, variable_scope as variable_scope
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

class RemoteValueStatus(enum.Enum):
    '''The status of a `RemoteValue` object.

  A `RemoteValue` object can have three states:
    1) not ready: no value, no non-retryable error and not aborted;
    2) aborted: i.e. the execution of function was aborted because of task
       failure, but can be retried;
    3) ready: i.e. has value or has non-tryable error;

  The initial state of a `RemoteValue` is "not ready". When its corresponding
  closure has
  been executed at least once, it will become aborted or ready. The state
  transitions are:
    1) not ready -> 2) aborted:
      when the corresponding closure is aborted due to worker failure, and the
      worker failure is not immediately handled.
    1) not ready -> 3) ready:
      when the corresponding closure has been executed successfully.
    2) aborted -> 3) ready:
      when the `RemoteValue` is rebuilt by rerunning the corresponding closure
      and the closure has been executed successfully.
    3) ready -> 2) aborted:
      when the corresponding closure had been executed successfully but later
      the corresponding remote worker failed. This is currently only implemented
      for resource `RemoteValue` like iterators.
  '''
    NOT_READY: str
    ABORTED: str
    READY: str

class RemoteValue:
    """An asynchronously available value of a scheduled function.

  This class is used as the return value of
  `tf.distribute.experimental.coordinator.ClusterCoordinator.schedule` where
  the underlying value becomes available at a later time once the function has
  been executed.

  Using `tf.distribute.experimental.coordinator.RemoteValue` as an input to
  a subsequent function scheduled with
  `tf.distribute.experimental.coordinator.ClusterCoordinator.schedule` is
  currently not supported.

  Example:

  ```python
  strategy = tf.distribute.experimental.ParameterServerStrategy(
      cluster_resolver=...)
  coordinator = (
      tf.distribute.experimental.coordinator.ClusterCoordinator(strategy))

  with strategy.scope():
    v1 = tf.Variable(initial_value=0.0)
    v2 = tf.Variable(initial_value=1.0)

  @tf.function
  def worker_fn():
    v1.assign_add(0.1)
    v2.assign_sub(0.2)
    return v1.read_value() / v2.read_value()

  result = coordinator.schedule(worker_fn)
  # Note that `fetch()` gives the actual result instead of a `tf.Tensor`.
  assert result.fetch() == 0.125

  for _ in range(10):
    # `worker_fn` will be run on arbitrary workers that are available. The
    # `result` value will be available later.
    result = coordinator.schedule(worker_fn)
  ```
  """
    def fetch(self) -> None:
        """Wait for the result of `RemoteValue` and return the numpy result.

    This makes the value concrete by copying the remote value to local.

    Returns:
      The numpy array structure of the actual output of the `tf.function`
      associated with this `RemoteValue`, previously returned by a
      `tf.distribute.experimental.coordinator.ClusterCoordinator.schedule` call.
      This can be a single value, or a structure of values, depending on the
      output of the `tf.function`.

    Raises:
      tf.errors.CancelledError: If the function that produces this `RemoteValue`
        is aborted or cancelled due to failure.
    """
    def get(self) -> None:
        """Wait for the result of `RemoteValue` and return the tensor result.

    This makes the value concrete by copying the remote tensor to local.

    Returns:
      The actual output (in the form of `tf.Tensor`s) of the `tf.function`
      associated with this `RemoteValue`, previously returned by a
      `tf.distribute.experimental.coordinator.ClusterCoordinator.schedule` call.
      This can be a single Tensor, or a structure of Tensors, depending on the
      output of the `tf.function`.

    Raises:
      tf.errors.CancelledError: If the function that produces this `RemoteValue`
        is aborted or cancelled due to failure.
    """

class RemoteValueImpl(RemoteValue):
    """Implementation of `RemoteValue`."""
    def __init__(self, closure, type_spec) -> None:
        """Initializes a `RemoteValueImpl`.

    Args:
      closure: The closure from which the `RemoteValue` is created.
      type_spec: The type spec for this `RemoteValue` which is used to trace
        functions that take this `RemoteValue` as input.
    """
    def fetch(self): ...
    def get(self): ...

class PerWorkerValues(composite_tensor.CompositeTensor):
    """A container that holds a list of values, one value per worker.

  `tf.distribute.experimental.coordinator.PerWorkerValues` contains a collection
  of values, where each of the values is located on its corresponding worker,
  and upon being used as one of the `args` or `kwargs` of
  `tf.distribute.experimental.coordinator.ClusterCoordinator.schedule()`, the
  value specific to a worker will be passed into the function being executed at
  that corresponding worker.

  Currently, the only supported path to create an object of
  `tf.distribute.experimental.coordinator.PerWorkerValues` is through calling
  `iter` on a `ClusterCoordinator.create_per_worker_dataset`-returned
  distributed dataset instance. The mechanism to create a custom
  `tf.distribute.experimental.coordinator.PerWorkerValues` is not yet supported.
  """
    def __init__(self, values) -> None: ...

class PerWorkerValuesTypeSpec(type_spec_lib.TypeSpec):
    """TypeSpec for PerWorkerValues.

  It only support tracing a function using a PerWorkerValues.
  """
    def __init__(self, value_spec, descendant_type) -> None: ...
    @property
    def value_type(self): ...
    def most_specific_common_supertype(self, others) -> None: ...

class PerWorkerDatasetFromDatasetFunction:
    """Represents worker-distributed datasets created from dataset function."""
    def __init__(self, dataset_fn, coordinator) -> None:
        """Makes an iterable from datasets created by the given function.

    Args:
      dataset_fn: A function that returns a `Dataset`.
      coordinator: a `ClusterCoordinator` object, used to create dataset
        resources.
    """
    def __iter__(self): ...
    @property
    def element_spec(self):
        """The type specification of an element of this dataset.

    This property is subject to change without notice.
    """

def serialize_dataset_to_graph(dataset): ...

class _RemoteDataset(dataset_ops.DatasetSource):
    """Creates a dataset given a graph def."""
    def __init__(self, graph_def, element_spec) -> None: ...
    @property
    def element_spec(self): ...

def deserialize_dataset_from_graph(graph_def, element_spec): ...

class PerWorkerDatasetFromDataset(PerWorkerDatasetFromDatasetFunction):
    """Represents worker-distributed datasets created from a dataset."""
    def __init__(self, dataset, coordinator) -> None:
        """Makes an iterable from datasets created by the given dataset.

    It creates a dataset_fn which deserializes a dataset from a graph under the
    hood.

    Args:
      dataset: A tf.data.Dataset, a DistributedDataset or a
        DistributedDatasetsFromFunction
      coordinator: a `ClusterCoordinator` object, used to create dataset
        resources.
    """

def get_per_worker_dataset(dataset_or_dataset_fn, coordinator):
    """Returns a per-worker dataset from a dataset or a dataset function."""

class PerWorkerDistributedIterator(PerWorkerValues):
    """Distributed iterator for `ClusterCoordinator`."""
    def __next__(self): ...
    def get_next(self, name: Incomplete | None = None) -> None:
        """Returns the next input from the iterator for all replicas."""
