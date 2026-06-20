from _typeshed import Incomplete
from tensorflow.python.distribute import device_util as device_util, distribute_lib as distribute_lib, distribute_utils as distribute_utils, input_lib as input_lib, input_util as input_util, numpy_dataset as numpy_dataset
from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

class OneDeviceStrategy(distribute_lib.Strategy):
    '''A distribution strategy for running on a single device.

  Using this strategy will place any variables created in its scope on the
  specified device. Input distributed through this strategy will be
  prefetched to the specified device. Moreover, any functions called via
  `strategy.run` will also be placed on the specified device
  as well.

  Typical usage of this strategy could be testing your code with the
  tf.distribute.Strategy API before switching to other strategies which
  actually distribute to multiple devices/machines.

  For example:
  ```
  strategy = tf.distribute.OneDeviceStrategy(device="/gpu:0")

  with strategy.scope():
    v = tf.Variable(1.0)
    print(v.device)  # /job:localhost/replica:0/task:0/device:GPU:0

  def step_fn(x):
    return x * 2

  result = 0
  for i in range(10):
    result += strategy.run(step_fn, args=(i,))
  print(result)  # 90
  ```
  '''
    def __init__(self, device) -> None:
        '''Creates a `OneDeviceStrategy`.

    Args:
      device: Device string identifier for the device on which the variables
        should be placed. See class docs for more details on how the device is
        used. Examples: "/cpu:0", "/gpu:0", "/device:CPU:0", "/device:GPU:0"
    '''
    def experimental_distribute_dataset(self, dataset, options: Incomplete | None = None):
        '''Distributes a tf.data.Dataset instance provided via dataset.

    In this case, there is only one device, so this is only a thin wrapper
    around the input dataset. It will, however, prefetch the input data to the
    specified device. The returned distributed dataset can be iterated over
    similar to how regular datasets can.

    NOTE: Currently, the user cannot add any more transformations to a
    distributed dataset.

    Example:
    ```
    strategy = tf.distribute.OneDeviceStrategy()
    dataset = tf.data.Dataset.range(10).batch(2)
    dist_dataset = strategy.experimental_distribute_dataset(dataset)
    for x in dist_dataset:
      print(x)  # [0, 1], [2, 3],...
    ```
    Args:
      dataset: `tf.data.Dataset` to be prefetched to device.
      options: `tf.distribute.InputOptions` used to control options on how this
        dataset is distributed.
    Returns:
      A "distributed `Dataset`" that the caller can iterate over.
    '''
    def distribute_datasets_from_function(self, dataset_fn, options: Incomplete | None = None):
        '''Distributes `tf.data.Dataset` instances created by calls to `dataset_fn`.

    `dataset_fn` will be called once for each worker in the strategy. In this
    case, we only have one worker and one device so `dataset_fn` is called
    once.

    The `dataset_fn` should take an `tf.distribute.InputContext` instance where
    information about batching and input replication can be accessed:

    ```
    def dataset_fn(input_context):
      batch_size = input_context.get_per_replica_batch_size(global_batch_size)
      d = tf.data.Dataset.from_tensors([[1.]]).repeat().batch(batch_size)
      return d.shard(
          input_context.num_input_pipelines, input_context.input_pipeline_id)

    inputs = strategy.distribute_datasets_from_function(dataset_fn)

    for batch in inputs:
      replica_results = strategy.run(replica_fn, args=(batch,))
    ```

    IMPORTANT: The `tf.data.Dataset` returned by `dataset_fn` should have a
    per-replica batch size, unlike `experimental_distribute_dataset`, which uses
    the global batch size.  This may be computed using
    `input_context.get_per_replica_batch_size`.

    Args:
      dataset_fn: A function taking a `tf.distribute.InputContext` instance and
        returning a `tf.data.Dataset`.
      options: `tf.distribute.InputOptions` used to control options on how this
        dataset is distributed.

    Returns:
      A "distributed `Dataset`", which the caller can iterate over like regular
      datasets.
    '''
    def experimental_local_results(self, value):
        """Returns the list of all local per-replica values contained in `value`.

    In `OneDeviceStrategy`, the `value` is always expected to be a single
    value, so the result is just the value in a tuple.

    Args:
      value: A value returned by `experimental_run()`, `run()`,
        `extended.call_for_each_replica()`, or a variable created in `scope`.

    Returns:
      A tuple of values contained in `value`. If `value` represents a single
      value, this returns `(value,).`
    """
    def run(self, fn, args=(), kwargs: Incomplete | None = None, options: Incomplete | None = None):
        """Run `fn` on each replica, with the given arguments.

    In `OneDeviceStrategy`, `fn` is simply called within a device scope for the
    given device, with the provided arguments.

    Args:
      fn: The function to run. The output must be a `tf.nest` of `Tensor`s.
      args: (Optional) Positional arguments to `fn`.
      kwargs: (Optional) Keyword arguments to `fn`.
      options: (Optional) An instance of `tf.distribute.RunOptions` specifying
        the options to run `fn`.

    Returns:
      Return value from running `fn`.
    """
    def reduce(self, reduce_op, value, axis):
        '''Reduce `value` across replicas.

    In `OneDeviceStrategy`, there is only one replica, so if axis=None, value
    is simply returned. If axis is specified as something other than None,
    such as axis=0, value is reduced along that axis and returned.

    Example:
    ```
    t = tf.range(10)

    result = strategy.reduce(tf.distribute.ReduceOp.SUM, t, axis=None).numpy()
    # result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    result = strategy.reduce(tf.distribute.ReduceOp.SUM, t, axis=0).numpy()
    # result: 45
    ```

    Args:
      reduce_op: A `tf.distribute.ReduceOp` value specifying how values should
        be combined.
      value: A "per replica" value, e.g. returned by `run` to
        be combined into a single tensor.
      axis: Specifies the dimension to reduce along within each
        replica\'s tensor. Should typically be set to the batch dimension, or
        `None` to only reduce across replicas (e.g. if the tensor has no batch
        dimension).

    Returns:
      A `Tensor`.
    '''
    def scope(self):
        '''Returns a context manager selecting this Strategy as current.

    Inside a `with strategy.scope():` code block, this thread
    will use a variable creator set by `strategy`, and will
    enter its "cross-replica context".

    In `OneDeviceStrategy`, all variables created inside `strategy.scope()`
    will be on `device` specified at strategy construction time.
    See example in the docs for this class.

    Returns:
      A context manager to use for creating variables with this strategy.
    '''

class OneDeviceStrategyV1(distribute_lib.StrategyV1):
    __doc__: Incomplete
    def __init__(self, device) -> None: ...

class OneDeviceExtended(distribute_lib.StrategyExtendedV1):
    """Implementation of OneDeviceStrategy."""
    def __init__(self, container_strategy, device) -> None: ...
    def read_var(self, replica_local_var):
        """Read the aggregate value of a replica-local variable."""
    def value_container(self, value): ...
    @property
    def worker_devices(self): ...
    @property
    def parameter_devices(self): ...
    def non_slot_devices(self, var_list): ...
    @property
    def experimental_should_init(self): ...
    @property
    def experimental_between_graph(self): ...
    @property
    def should_checkpoint(self): ...
    @property
    def should_save_summary(self): ...

class _OneDeviceReplicaContext(distribute_lib.ReplicaContext):
    """ReplicaContext for OneDeviceStrategy."""
    def __init__(self, strategy) -> None: ...
    @property
    def devices(self): ...
