from _typeshed import Incomplete
from tensorflow.python.distribute import device_util as device_util, distribute_lib as distribute_lib, parameter_server_strategy as parameter_server_strategy
from tensorflow.python.util.tf_export import tf_export as tf_export

class CentralStorageStrategy(distribute_lib.Strategy):
    """A one-machine strategy that puts all variables on a single device.

  Variables are assigned to local CPU or the only GPU. If there is more
  than one GPU, compute operations (other than variable update operations)
  will be replicated across all GPUs.

  For Example:
  ```
  strategy = tf.distribute.experimental.CentralStorageStrategy()
  # Create a dataset
  ds = tf.data.Dataset.range(5).batch(2)
  # Distribute that dataset
  dist_dataset = strategy.experimental_distribute_dataset(ds)

  with strategy.scope():
    @tf.function
    def train_step(val):
      return val + 1

    # Iterate over the distributed dataset
    for x in dist_dataset:
      # process dataset elements
      strategy.run(train_step, args=(x,))
  ```
  """
    def __init__(self, compute_devices: Incomplete | None = None, parameter_device: Incomplete | None = None) -> None: ...
    def experimental_distribute_dataset(self, dataset, options: Incomplete | None = None):
        '''Distributes a tf.data.Dataset instance provided via dataset.

    The returned dataset is a wrapped strategy dataset which creates a
    multidevice iterator under the hood. It prefetches the input data to the
    specified devices on the worker. The returned distributed dataset can be
    iterated over similar to how regular datasets can.

    NOTE: Currently, the user cannot add any more transformations to a
    distributed dataset.

    For Example:
    ```
    strategy = tf.distribute.CentralStorageStrategy()  # with 1 CPU and 1 GPU
    dataset = tf.data.Dataset.range(10).batch(2)
    dist_dataset = strategy.experimental_distribute_dataset(dataset)
    for x in dist_dataset:
      print(x)  # Prints PerReplica values [0, 1], [2, 3],...

    ```
    Args:
      dataset: `tf.data.Dataset` to be prefetched to device.
      options: `tf.distribute.InputOptions` used to control options on how this
        dataset is distributed.

    Returns:
      A "distributed `Dataset`" that the caller can iterate over.
    '''
    def experimental_local_results(self, value):
        """Returns the list of all local per-replica values contained in `value`.

    In `CentralStorageStrategy` there is a single worker so the value returned
    will be all the values on that worker.

    Args:
      value: A value returned by `run()`, `extended.call_for_each_replica()`,
      or a variable created in `scope`.

    Returns:
      A tuple of values contained in `value`. If `value` represents a single
      value, this returns `(value,).`
    """
    def run(self, fn, args=(), kwargs: Incomplete | None = None, options: Incomplete | None = None):
        '''Run `fn` on each replica, with the given arguments.

    In `CentralStorageStrategy`, `fn` is  called on each of the compute
    replicas, with the provided "per replica" arguments specific to that device.

    Args:
      fn: The function to run. The output must be a `tf.nest` of `Tensor`s.
      args: (Optional) Positional arguments to `fn`.
      kwargs: (Optional) Keyword arguments to `fn`.
      options: (Optional) An instance of `tf.distribute.RunOptions` specifying
        the options to run `fn`.

    Returns:
      Return value from running `fn`.
    '''
    def reduce(self, reduce_op, value, axis):
        '''Reduce `value` across replicas.

    Given a per-replica value returned by `run`, say a
    per-example loss, the batch will be divided across all the replicas. This
    function allows you to aggregate across replicas and optionally also across
    batch elements.  For example, if you have a global batch size of 8 and 2
    replicas, values for examples `[0, 1, 2, 3]` will be on replica 0 and
    `[4, 5, 6, 7]` will be on replica 1. By default, `reduce` will just
    aggregate across replicas, returning `[0+4, 1+5, 2+6, 3+7]`. This is useful
    when each replica is computing a scalar or some other value that doesn\'t
    have a "batch" dimension (like a gradient). More often you will want to
    aggregate across the global batch, which you can get by specifying the batch
    dimension as the `axis`, typically `axis=0`. In this case it would return a
    scalar `0+1+2+3+4+5+6+7`.

    If there is a last partial batch, you will need to specify an axis so
    that the resulting shape is consistent across replicas. So if the last
    batch has size 6 and it is divided into [0, 1, 2, 3] and [4, 5], you
    would get a shape mismatch unless you specify `axis=0`. If you specify
    `tf.distribute.ReduceOp.MEAN`, using `axis=0` will use the correct
    denominator of 6. Contrast this with computing `reduce_mean` to get a
    scalar value on each replica and this function to average those means,
    which will weigh some values `1/8` and others `1/4`.

    For Example:
    ```
    strategy = tf.distribute.experimental.CentralStorageStrategy(
        compute_devices=[\'CPU:0\', \'GPU:0\'], parameter_device=\'CPU:0\')
    ds = tf.data.Dataset.range(10)
    # Distribute that dataset
    dist_dataset = strategy.experimental_distribute_dataset(ds)

    with strategy.scope():
      @tf.function
      def train_step(val):
        # pass through
        return val

      # Iterate over the distributed dataset
      for x in dist_dataset:
        result = strategy.run(train_step, args=(x,))

    result = strategy.reduce(tf.distribute.ReduceOp.SUM, result,
                             axis=None).numpy()
    # result: array([ 4,  6,  8, 10])

    result = strategy.reduce(tf.distribute.ReduceOp.SUM, result, axis=0).numpy()
    # result: 28
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

class CentralStorageStrategyV1(distribute_lib.StrategyV1):
    __doc__: Incomplete
    def __init__(self, compute_devices: Incomplete | None = None, parameter_device: Incomplete | None = None) -> None: ...
