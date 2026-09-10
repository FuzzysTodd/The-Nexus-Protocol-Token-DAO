from _typeshed import Incomplete
from tensorflow.python.distribute.cluster_resolver.cluster_resolver import ClusterResolver as ClusterResolver
from tensorflow.python.training.server_lib import ClusterSpec as ClusterSpec
from tensorflow.python.util.tf_export import tf_export as tf_export

def format_master_url(master, rpc_layer: Incomplete | None = None): ...

class TFConfigClusterResolver(ClusterResolver):
    '''Implementation of a ClusterResolver which reads the TF_CONFIG EnvVar.

  This is an implementation of cluster resolvers when using TF_CONFIG to set
  information about the cluster. The cluster spec returned will be
  initialized from the TF_CONFIG environment variable.

  An example to set TF_CONFIG is:

    ```Python
    os.environ[\'TF_CONFIG\'] = json.dumps({
      \'cluster\': {
          \'worker\': ["localhost:12345", "localhost:23456"]
      },
      \'task\': {\'type\': \'worker\', \'index\': 0}
    })
    ```

  However, sometimes the container orchestration framework will set TF_CONFIG
  for you. In this case, you can just create an instance without passing in any
  arguments. You can find an example here to let Kuburnetes set TF_CONFIG for
  you: https://github.com/tensorflow/ecosystem/tree/master/kubernetes. Then you
  can use it with `tf.distribute.Strategy` as:

    ```Python
    # `TFConfigClusterResolver` is already the default one in the following
    # strategy.
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
        cluster_resolver=TFConfigClusterResolver())
    ```
  '''
    def __init__(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, rpc_layer: Incomplete | None = None, environment: Incomplete | None = None) -> None:
        """Creates a new TFConfigClusterResolver.

    Args:
      task_type: (String, optional) Overrides the task type specified in the
        TF_CONFIG environment variable.
      task_id: (Integer, optional) Overrides the task index specified in the
        TF_CONFIG environment variable.
      rpc_layer: (String, optional) Overrides the rpc layer TensorFlow uses.
      environment: (String, optional) Overrides the environment TensorFlow
        operates in.
    """
    @property
    def task_type(self): ...
    @property
    def task_id(self): ...
    @task_type.setter
    def task_type(self, task_type) -> None: ...
    @task_id.setter
    def task_id(self, task_id) -> None: ...
    @property
    def environment(self): ...
    @property
    def rpc_layer(self): ...
    @rpc_layer.setter
    def rpc_layer(self, rpc_layer) -> None: ...
    def num_accelerators(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, config_proto: Incomplete | None = None): ...
    def cluster_spec(self):
        """Returns a ClusterSpec based on the TF_CONFIG environment variable.

    Returns:
      A ClusterSpec with information from the TF_CONFIG environment variable.
    """
    def master(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, rpc_layer: Incomplete | None = None):
        """Returns the master address to use when creating a TensorFlow session.

    Note: this is only useful for TensorFlow 1.x.

    Args:
      task_type: (String, optional) Overrides and sets the task_type of the
        master.
      task_id: (Integer, optional) Overrides and sets the task id of the
        master.
      rpc_layer: (String, optional) Overrides and sets the protocol over which
        TensorFlow nodes communicate with each other.

    Returns:
      The address of the master.

    Raises:
      RuntimeError: If the task_type or task_id is not specified and the
        `TF_CONFIG` environment variable does not contain a task section.
    """
