from _typeshed import Incomplete
from tensorflow.core.protobuf import rewriter_config_pb2 as rewriter_config_pb2, tensorflow_server_pb2 as tensorflow_server_pb2
from tensorflow.python.distribute import collective_util as collective_util, cross_device_utils as cross_device_utils, device_util as device_util, distribute_lib as distribute_lib, distribute_utils as distribute_utils, input_lib as input_lib, input_util as input_util, mirrored_strategy as mirrored_strategy, multi_worker_util as multi_worker_util, numpy_dataset as numpy_dataset, reduce_util as reduce_util, values as values
from tensorflow.python.distribute.cluster_resolver import ClusterResolver as ClusterResolver, SimpleClusterResolver as SimpleClusterResolver, TFConfigClusterResolver as TFConfigClusterResolver
from tensorflow.python.eager import context as context
from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.ops import array_ops as array_ops, collective_ops as collective_ops, control_flow_util as control_flow_util
from tensorflow.python.tpu import tpu_strategy_util as tpu_strategy_util
from tensorflow.python.trackable import base as base
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tsl.protobuf import coordination_config_pb2 as coordination_config_pb2

class CollectiveAllReduceStrategy(distribute_lib.Strategy):
    '''A distribution strategy for synchronous training on multiple workers.

  This strategy implements synchronous distributed training across multiple
  workers, each with potentially multiple GPUs. Similar to
  `tf.distribute.MirroredStrategy`, it replicates all variables and computations
  to each local device. The difference is that it uses a distributed collective
  implementation (e.g. all-reduce), so that multiple workers can work together.

  You need to launch your program on each worker and configure
  `cluster_resolver` correctly. For example, if you are using
  `tf.distribute.cluster_resolver.TFConfigClusterResolver`, each worker needs to
  have its corresponding `task_type` and `task_id` set in the `TF_CONFIG`
  environment variable. An example TF_CONFIG on worker-0 of a two worker cluster
  is:

  ```
  TF_CONFIG = \'{"cluster": {"worker": ["localhost:12345", "localhost:23456"]}, "task": {"type": "worker", "index": 0} }\'
  ```

  Your program runs on each worker as-is. Note that collectives require each
  worker to participate. All `tf.distribute` and non `tf.distribute` API may use
  collectives internally, e.g. checkpointing and saving since reading a
  `tf.Variable` with `tf.VariableSynchronization.ON_READ` all-reduces the value.
  Therefore it\'s recommended to run exactly the same program on each worker.
  Dispatching based on `task_type` or `task_id` of the worker is error-prone.

  `cluster_resolver.num_accelerators()` determines the number of GPUs the
  strategy uses. If it\'s zero, the strategy uses the CPU. All workers need to
  use the same number of devices, otherwise the behavior is undefined.

  This strategy is not intended for TPU. Use `tf.distribute.TPUStrategy`
  instead.

  After setting up TF_CONFIG, using this strategy is similar to using
  `tf.distribute.MirroredStrategy` and `tf.distribute.TPUStrategy`.

  ```
  strategy = tf.distribute.MultiWorkerMirroredStrategy()

  with strategy.scope():
    model = tf.keras.Sequential([
      tf.keras.layers.Dense(2, input_shape=(5,)),
    ])
    optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

  def dataset_fn(ctx):
    x = np.random.random((2, 5)).astype(np.float32)
    y = np.random.randint(2, size=(2, 1))
    dataset = tf.data.Dataset.from_tensor_slices((x, y))
    return dataset.repeat().batch(1, drop_remainder=True)
  dist_dataset = strategy.distribute_datasets_from_function(dataset_fn)

  model.compile()
  model.fit(dist_dataset)
  ```

  You can also write your own training loop:

  ```
  @tf.function
  def train_step(iterator):

    def step_fn(inputs):
      features, labels = inputs
      with tf.GradientTape() as tape:
        logits = model(features, training=True)
        loss = tf.keras.losses.sparse_categorical_crossentropy(
            labels, logits)

      grads = tape.gradient(loss, model.trainable_variables)
      optimizer.apply_gradients(zip(grads, model.trainable_variables))

    strategy.run(step_fn, args=(next(iterator),))

  for _ in range(NUM_STEP):
    train_step(iterator)
  ```

  See
  [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)
  for a detailed tutorial.

  __Saving__

  You need to save and checkpoint on all workers instead of just one. This is
  because variables whose synchronization=ON_READ triggers aggregation during
  saving. It\'s recommended to save to a different path on each worker to avoid
  race conditions. Each worker saves the same thing. See
  [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras#model_saving_and_loading)
  tutorial for examples.

  __Known Issues__

  * `tf.distribute.cluster_resolver.TFConfigClusterResolver` does not return the
  correct number of accelerators. The strategy uses all available GPUs if
  `cluster_resolver` is `tf.distribute.cluster_resolver.TFConfigClusterResolver`
  or `None`.
  * In eager mode, the strategy needs to be created before calling any other
  Tensorflow API.

  '''
    def __init__(self, cluster_resolver: Incomplete | None = None, communication_options: Incomplete | None = None) -> None:
        """Creates the strategy.

    Args:
      cluster_resolver: optional
        `tf.distribute.cluster_resolver.ClusterResolver`. If `None`,
        `tf.distribute.cluster_resolver.TFConfigClusterResolver` is used.
      communication_options: optional
        `tf.distribute.experimental.CommunicationOptions`. This configures the
        default options for cross device communications. It can be overridden by
        options provided to the communication APIs like
        `tf.distribute.ReplicaContext.all_reduce`. See
        `tf.distribute.experimental.CommunicationOptions` for details.
    """
    @property
    def cluster_resolver(self):
        """Returns the cluster resolver associated with this strategy.

    As a multi-worker strategy, `tf.distribute.MultiWorkerMirroredStrategy`
    provides the associated `tf.distribute.cluster_resolver.ClusterResolver`. If
    the user provides one in `__init__`, that instance is returned; if the user
    does not, a default `TFConfigClusterResolver` is provided.
    """

class _CollectiveAllReduceStrategyExperimentalMeta(type):
    @classmethod
    def __instancecheck__(cls, instance): ...

class _CollectiveAllReduceStrategyExperimental(CollectiveAllReduceStrategy, metaclass=_CollectiveAllReduceStrategyExperimentalMeta):
    __doc__: Incomplete
    def __init__(self, communication=..., cluster_resolver: Incomplete | None = None) -> None:
        """Creates the strategy.

    Args:
      communication: optional
        `tf.distribute.experimental.CommunicationImplementation`. This is a hint
        on the preferred collective communication implementation. Possible
        values include `AUTO`, `RING`, and `NCCL`.
      cluster_resolver: optional
        `tf.distribute.cluster_resolver.ClusterResolver`. If `None`,
        `tf.distribute.cluster_resolver.TFConfigClusterResolver` is used.
    """

class CollectiveAllReduceStrategyV1(distribute_lib.StrategyV1):
    __doc__: Incomplete
    def __init__(self, communication=..., cluster_resolver: Incomplete | None = None) -> None:
        """Initializes the object."""

class CollectiveAllReduceExtended(mirrored_strategy.MirroredExtended):
    """Implementation of CollectiveAllReduceStrategy."""
    experimental_enable_get_next_as_optional: bool
    def __init__(self, container_strategy, cluster_resolver, communication_options, devices: Incomplete | None = None) -> None: ...
    def __del__(self) -> None: ...
    @property
    def experimental_between_graph(self): ...
    @property
    def experimental_should_init(self): ...
    @property
    def should_checkpoint(self): ...
    @property
    def should_save_summary(self): ...
    def __deepcopy__(self, memo): ...
