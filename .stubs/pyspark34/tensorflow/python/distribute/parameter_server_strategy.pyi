from _typeshed import Incomplete
from tensorflow.python.distribute import device_util as device_util, distribute_lib as distribute_lib, distribute_utils as distribute_utils, input_lib as input_lib, input_util as input_util, mirrored_run as mirrored_run, multi_worker_util as multi_worker_util, numpy_dataset as numpy_dataset, ps_values as ps_values, values as values
from tensorflow.python.distribute.cluster_resolver import SimpleClusterResolver as SimpleClusterResolver, TFConfigClusterResolver as TFConfigClusterResolver
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.training import device_setter as device_setter
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

class ParameterServerStrategyV1(distribute_lib.StrategyV1):
    """An asynchronous multi-worker parameter server tf.distribute strategy.

  This strategy requires two roles: workers and parameter servers. Variables and
  updates to those variables will be assigned to parameter servers and other
  operations are assigned to workers.

  When each worker has more than one GPU, operations will be replicated on all
  GPUs. Even though operations may be replicated, variables are not and each
  worker shares a common view for which parameter server a variable is assigned
  to.

  By default it uses `TFConfigClusterResolver` to detect configurations for
  multi-worker training. This requires a 'TF_CONFIG' environment variable and
  the 'TF_CONFIG' must have a cluster spec.

  This class assumes each worker is running the same code independently, but
  parameter servers are running a standard server. This means that while each
  worker will synchronously compute a single gradient update across all GPUs,
  updates between workers proceed asynchronously. Operations that occur only on
  the first replica (such as incrementing the global step), will occur on the
  first replica *of every worker*.

  It is expected to call `call_for_each_replica(fn, ...)` for any
  operations which potentially can be replicated across replicas (i.e. multiple
  GPUs) even if there is only CPU or one GPU. When defining the `fn`, extra
  caution needs to be taken:

  1) It is generally not recommended to open a device scope under the strategy's
  scope. A device scope (i.e. calling `tf.device`) will be merged with or
  override the device for operations but will not change the device for
  variables.

  2) It is also not recommended to open a colocation scope (i.e. calling
  `tf.compat.v1.colocate_with`) under the strategy's scope. For colocating
  variables, use `strategy.extended.colocate_vars_with` instead. Colocation of
  ops will possibly create device assignment conflicts.

  Note: This strategy only works with the Estimator API. Pass an instance of
  this strategy to the `experimental_distribute` argument when you create the
  `RunConfig`. This instance of `RunConfig` should then be passed to the
  `Estimator` instance on which `train_and_evaluate` is called.

  For Example:
  ```
  strategy = tf.distribute.experimental.ParameterServerStrategy()
  run_config = tf.estimator.RunConfig(
      experimental_distribute.train_distribute=strategy)
  estimator = tf.estimator.Estimator(config=run_config)
  tf.estimator.train_and_evaluate(estimator,...)
  ```
  """
    def __init__(self, cluster_resolver: Incomplete | None = None) -> None:
        """Initializes this strategy with an optional `cluster_resolver`.

    Args:
      cluster_resolver: Optional
        `tf.distribute.cluster_resolver.ClusterResolver` object. Defaults to a
        `tf.distribute.cluster_resolver.TFConfigClusterResolver`.
    """
    def experimental_distribute_dataset(self, dataset, options: Incomplete | None = None) -> None: ...
    def distribute_datasets_from_function(self, dataset_fn, options: Incomplete | None = None) -> None: ...
    def run(self, fn, args=(), kwargs: Incomplete | None = None, options: Incomplete | None = None) -> None: ...
    def scope(self): ...

class ParameterServerStrategyExtended(distribute_lib.StrategyExtendedV1):
    """Implementation of ParameterServerStrategy and CentralStorageStrategy."""
    def __init__(self, container_strategy, cluster_resolver: Incomplete | None = None, compute_devices: Incomplete | None = None, parameter_device: Incomplete | None = None) -> None: ...
    def value_container(self, val): ...
    def read_var(self, var): ...
    @property
    def worker_devices(self): ...
    @property
    def worker_devices_by_replica(self): ...
    @property
    def parameter_devices(self): ...
    def non_slot_devices(self, var_list): ...
    @property
    def experimental_between_graph(self): ...
    @property
    def experimental_should_init(self): ...
    @property
    def should_checkpoint(self): ...
    @property
    def should_save_summary(self): ...
