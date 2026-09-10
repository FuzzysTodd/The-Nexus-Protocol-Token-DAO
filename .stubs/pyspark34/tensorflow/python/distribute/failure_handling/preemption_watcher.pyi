from tensorflow.python.distribute.failure_handling.failure_handling_util import PlatformDevice as PlatformDevice, detect_platform as detect_platform
from tensorflow.python.eager import context as context, monitoring as monitoring
from tensorflow.python.util.tf_export import tf_export as tf_export

class PreemptionWatcher:
    """Watch preemption signal and store it.

  Notice: Currently only support Borg TPU environment with TPUClusterResolver.

  This class provides a way to monitor the preemption signal during training on
  TPU. It will start a background thread to watch the training process, trying
  to fetch preemption message from the coordination service. When preemption
  happens, the preempted worker will write the preemption message to the
  coordination service. Thus getting a non-empty preemption message means there
  is a preemption happened.

  User can use the preemption message as a reliable preemption indicator, and
  then set the coordinator to reconnect to the TPU worker instead of a fully
  restart triggered by Borg. For example, a training process with
  preemption recovery will be like:

  ```python
  keep_running = True
  preemption_watcher = None
  while keep_running:
    try:
      # Initialize TPU cluster and stratygy.
      resolver = tf.distribute.cluster_resolver.TPUClusterResolver()
      tf.config.experimental_connect_to_cluster(resolver)
      tf.tpu.experimental.initialize_tpu_system(resolver)
      strategy = tf.distribute.TPUStrategy(resolver)

      # PreemptionWatcher must be created after connected to cluster.
      preemption_watcher = tf.distribute.experimental.PreemptionWatcher()
      train_model(strategy)
      keep_running = False
    except Exception as e:
      if preemption_watcher and preemption_watcher.preemption_message:
        keep_running = True
      else:
        raise e
  ```

  Attributes:
    preemption_message: A variable to store the preemption message fetched from
      the coordination service. If it is not None, then there is a preemption
      happened.
  """
    def __init__(self) -> None: ...
    @property
    def preemption_message(self):
        """Returns the preemption message."""
