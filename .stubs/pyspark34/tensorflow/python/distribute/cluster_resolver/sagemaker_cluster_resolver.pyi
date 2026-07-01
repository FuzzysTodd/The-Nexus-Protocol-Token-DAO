from _typeshed import Incomplete
from tensorflow.python.distribute.cluster_resolver.cluster_resolver import ClusterResolver as ClusterResolver
from tensorflow.python.training.server_lib import ClusterSpec as ClusterSpec
from tensorflow.python.util.tf_export import tf_export as tf_export

def format_master_url(master, rpc_layer: Incomplete | None = None): ...

class SageMakerClusterResolver(ClusterResolver):
    """Implementation of a ClusterResolver which reads the Sagemaker EnvVars. This is an implementation of cluster resolvers when running in a SageMaker environment to set information about the cluster.

  The cluster spec returned will be initialized from the SageMaker
  environment variables.
  Currently this Cluster Resolver only supports Multi-Worker Mirrored Strategy.
  It assumes all nodes in a SageMaker Cluster are workers.
  """
    def __init__(self, port: int = 2223, task_type: Incomplete | None = None, task_id: Incomplete | None = None, rpc_layer: Incomplete | None = None, environment: Incomplete | None = None) -> None:
        """Creates a new SageMakerClusterResolver.

    Args:
      port: (integer, optional) Override default port usage of 2223
      task_type: (String, optional) Overrides the task type.
      task_id: (Integer, optional) Overrides the task index.
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
        """Returns a ClusterSpec based on the SageMaker environment variables.

    Returns:
      A ClusterSpec with information from the SageMaker environment variables.
    """
    def master(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, rpc_layer: Incomplete | None = None):
        """Returns the master address to use when creating a TensorFlow session.

    Note: this is only useful for TensorFlow 1.x.

    Args:
      task_type: (String, optional) Overrides and sets the task_type of the
        master.
      task_id: (Integer, optional) Overrides and sets the task id of the master.
      rpc_layer: (String, optional) Overrides and sets the protocol over which
        TensorFlow nodes communicate with each other.

    Returns:
      The address of the master.

    Raises:
      RuntimeError: If the task_type or task_id is not specified and the
        SageMaker environment variables does not contain a task section.
    """
