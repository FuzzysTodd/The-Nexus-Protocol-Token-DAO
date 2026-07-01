from _typeshed import Incomplete
from tensorflow.python.distribute.cluster_resolver.cluster_resolver import ClusterResolver as ClusterResolver
from tensorflow.python.training.server_lib import ClusterSpec as ClusterSpec
from tensorflow.python.util.tf_export import tf_export as tf_export

class GCEClusterResolver(ClusterResolver):
    '''ClusterResolver for Google Compute Engine.

  This is an implementation of cluster resolvers for the Google Compute Engine
  instance group platform. By specifying a project, zone, and instance group,
  this will retrieve the IP address of all the instances within the instance
  group and return a ClusterResolver object suitable for use for distributed
  TensorFlow.

  Note: this cluster resolver cannot retrieve `task_type`, `task_id` or
  `rpc_layer`. To use it with some distribution strategies like
  `tf.distribute.experimental.MultiWorkerMirroredStrategy`, you will need to
  specify `task_type` and `task_id` in the constructor.

  Usage example with tf.distribute.Strategy:

    ```Python
    # On worker 0
    cluster_resolver = GCEClusterResolver("my-project", "us-west1",
                                          "my-instance-group",
                                          task_type="worker", task_id=0)
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
        cluster_resolver=cluster_resolver)

    # On worker 1
    cluster_resolver = GCEClusterResolver("my-project", "us-west1",
                                          "my-instance-group",
                                          task_type="worker", task_id=1)
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
        cluster_resolver=cluster_resolver)
    ```
  '''
    def __init__(self, project, zone, instance_group, port, task_type: str = 'worker', task_id: int = 0, rpc_layer: str = 'grpc', credentials: str = 'default', service: Incomplete | None = None) -> None:
        """Creates a new GCEClusterResolver object.

    This takes in a few parameters and creates a GCEClusterResolver project. It
    will then use these parameters to query the GCE API for the IP addresses of
    each instance in the instance group.

    Args:
      project: Name of the GCE project.
      zone: Zone of the GCE instance group.
      instance_group: Name of the GCE instance group.
      port: Port of the listening TensorFlow server (default: 8470)
      task_type: Name of the TensorFlow job this GCE instance group of VM
        instances belong to.
      task_id: The task index for this particular VM, within the GCE
        instance group. In particular, every single instance should be assigned
        a unique ordinal index within an instance group manually so that they
        can be distinguished from each other.
      rpc_layer: The RPC layer TensorFlow should use to communicate across
        instances.
      credentials: GCE Credentials. If nothing is specified, this defaults to
        GoogleCredentials.get_application_default().
      service: The GCE API object returned by the googleapiclient.discovery
        function. (Default: discovery.build('compute', 'v1')). If you specify a
        custom service object, then the credentials parameter will be ignored.

    Raises:
      ImportError: If the googleapiclient is not installed.
    """
    def cluster_spec(self):
        """Returns a ClusterSpec object based on the latest instance group info.

    This returns a ClusterSpec object for use based on information from the
    specified instance group. We will retrieve the information from the GCE APIs
    every time this method is called.

    Returns:
      A ClusterSpec containing host information retrieved from GCE.
    """
    def master(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, rpc_layer: Incomplete | None = None): ...
    @property
    def task_type(self): ...
    @property
    def task_id(self): ...
    @task_type.setter
    def task_type(self, task_type) -> None: ...
    @task_id.setter
    def task_id(self, task_id) -> None: ...
    @property
    def rpc_layer(self): ...
    @rpc_layer.setter
    def rpc_layer(self, rpc_layer) -> None: ...
