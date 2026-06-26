from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.distribute import collective_util as collective_util, cross_device_utils as cross_device_utils, device_util as device_util, distribute_lib as distribute_lib, distribute_utils as distribute_utils, distribution_strategy_context as distribution_strategy_context, input_lib as input_lib, input_util as input_util, mirrored_run as mirrored_run, multi_worker_util as multi_worker_util, numpy_dataset as numpy_dataset, reduce_util as reduce_util, values as values, values_util as values_util
from tensorflow.python.distribute.cluster_resolver import TFConfigClusterResolver as TFConfigClusterResolver
from tensorflow.python.eager import context as context, tape as tape
from tensorflow.python.framework import config as config, constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util as control_flow_util
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

def all_local_devices(num_gpus: Incomplete | None = None): ...
def all_devices(): ...

class MirroredStrategy(distribute_lib.Strategy):
    '''Synchronous training across multiple replicas on one machine.

  This strategy is typically used for training on one
  machine with multiple GPUs. For TPUs, use
  `tf.distribute.TPUStrategy`. To use `MirroredStrategy` with multiple workers,
  please refer to `tf.distribute.experimental.MultiWorkerMirroredStrategy`.

  For example, a variable created under a `MirroredStrategy` is a
  `MirroredVariable`. If no devices are specified in the constructor argument of
  the strategy then it will use all the available GPUs. If no GPUs are found, it
  will use the available CPUs. Note that TensorFlow treats all CPUs on a
  machine as a single device, and uses threads internally for parallelism.

  >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
  >>> with strategy.scope():
  ...   x = tf.Variable(1.)
  >>> x
  MirroredVariable:{
    0: <tf.Variable ... shape=() dtype=float32, numpy=1.0>,
    1: <tf.Variable ... shape=() dtype=float32, numpy=1.0>
  }

  While using distribution strategies, all the variable creation should be done
  within the strategy\'s scope. This will replicate the variables across all the
  replicas and keep them in sync using an all-reduce algorithm.

  Variables created inside a `MirroredStrategy` which is wrapped with a
  `tf.function` are still `MirroredVariables`.

  >>> x = []
  >>> @tf.function  # Wrap the function with tf.function.
  ... def create_variable():
  ...   if not x:
  ...     x.append(tf.Variable(1.))
  ...   return x[0]
  >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
  >>> with strategy.scope():
  ...   _ = create_variable()
  ...   print(x[0])
  MirroredVariable:{
    0: <tf.Variable ... shape=() dtype=float32, numpy=1.0>,
    1: <tf.Variable ... shape=() dtype=float32, numpy=1.0>
  }

  `experimental_distribute_dataset` can be used to distribute the dataset across
  the replicas when writing your own training loop. If you are using `.fit` and
  `.compile` methods available in `tf.keras`, then `tf.keras` will handle the
  distribution for you.

  For example:

  ```python
  my_strategy = tf.distribute.MirroredStrategy()
  with my_strategy.scope():
    @tf.function
    def distribute_train_epoch(dataset):
      def replica_fn(input):
        # process input and return result
        return result

      total_result = 0
      for x in dataset:
        per_replica_result = my_strategy.run(replica_fn, args=(x,))
        total_result += my_strategy.reduce(tf.distribute.ReduceOp.SUM,
                                           per_replica_result, axis=None)
      return total_result

    dist_dataset = my_strategy.experimental_distribute_dataset(dataset)
    for _ in range(EPOCHS):
      train_result = distribute_train_epoch(dist_dataset)
  ```

  Args:
    devices: a list of device strings such as `[\'/gpu:0\', \'/gpu:1\']`.  If
      `None`, all available GPUs are used. If no GPUs are found, CPU is used.
    cross_device_ops: optional, a descendant of `CrossDeviceOps`. If this is not
      set, `NcclAllReduce()` will be used by default.  One would customize this
      if NCCL isn\'t available or if a special implementation that exploits
      the particular hardware is available.
  '''
    def __init__(self, devices: Incomplete | None = None, cross_device_ops: Incomplete | None = None) -> None: ...

class MirroredStrategyV1(distribute_lib.StrategyV1):
    __doc__: Incomplete
    def __init__(self, devices: Incomplete | None = None, cross_device_ops: Incomplete | None = None) -> None: ...

class MirroredExtended(distribute_lib.StrategyExtendedV1):
    """Implementation of MirroredStrategy."""
    experimental_enable_get_next_as_optional: bool
    def __init__(self, container_strategy, devices: Incomplete | None = None, cross_device_ops: Incomplete | None = None) -> None: ...
    def read_var(self, replica_local_var):
        """Read the aggregate value of a replica-local variable."""
    def value_container(self, val): ...
    @property
    def worker_devices(self): ...
    @property
    def worker_devices_by_replica(self): ...
    @property
    def parameter_devices(self): ...
    @property
    def experimental_between_graph(self): ...
    @property
    def experimental_should_init(self): ...
    @property
    def should_checkpoint(self): ...
    @property
    def should_save_summary(self): ...
    def non_slot_devices(self, var_list): ...
