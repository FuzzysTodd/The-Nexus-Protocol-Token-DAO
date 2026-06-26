from _typeshed import Incomplete
from tensorflow.core.protobuf.tpu import topology_pb2 as topology_pb2
from tensorflow.python.distribute.cluster_resolver import cluster_resolver as cluster_resolver
from tensorflow.python.framework import errors as errors
from tensorflow.python.tpu.client import client as client
from tensorflow.python.training import server_lib as server_lib
from tensorflow.python.util import compat as compat
from typing import NamedTuple

def is_running_in_gce(): ...

class _LocalCloudTpuClient:
    """Dummy local Cloud TPU client."""
    def api_available(self): ...

class DeviceDetails(NamedTuple):
    device_map: Incomplete
    total_cores: Incomplete

class TPUClusterResolver(cluster_resolver.ClusterResolver):
    """Cluster Resolver for Google Cloud TPUs.

  This is an implementation of cluster resolvers for the Google Cloud TPU
  service.

  TPUClusterResolver supports the following distinct environments:
  Google Compute Engine
  Google Kubernetes Engine
  Google internal

  It can be passed into `tf.distribute.TPUStrategy` to support TF2 training on
  Cloud TPUs.
  """
    @staticmethod
    def connect(tpu: Incomplete | None = None, zone: Incomplete | None = None, project: Incomplete | None = None):
        """Initializes TPU and returns a TPUClusterResolver.

    This API will connect to remote TPU cluster and initialize the TPU
    hardwares. Example usage:

    >>> resolver = tf.distribute.cluster_resolver.TPUClusterResolver.connect(
    ...     tpu='')

    It can be viewed as convenient wrapper of the following code:

    >>> resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    >>> tf.config.experimental_connect_to_cluster(resolver)
    >>> tf.tpu.experimental.initialize_tpu_system(resolver)

    Args:
      tpu: A string corresponding to the TPU to use. It can be the TPU name or
        TPU worker gRPC address. If not set, it will try automatically resolve
        the TPU address on Cloud TPUs.
      zone: Zone where the TPUs are located. If omitted or empty, we will assume
        that the zone of the TPU is the same as the zone of the GCE VM, which we
        will try to discover from the GCE metadata service.
      project: Name of the GCP project containing Cloud TPUs. If omitted or
        empty, we will try to discover the project name of the GCE VM from the
        GCE metadata service.

    Returns:
      An instance of TPUClusterResolver object.

    Raises:
      NotFoundError: If no TPU devices found in eager mode.
    """
    task_type: Incomplete
    task_id: int
    def __init__(self, tpu: Incomplete | None = None, zone: Incomplete | None = None, project: Incomplete | None = None, job_name: str = 'worker', coordinator_name: Incomplete | None = None, coordinator_address: Incomplete | None = None, credentials: str = 'default', service: Incomplete | None = None, discovery_url: Incomplete | None = None) -> None:
        '''Creates a new TPUClusterResolver object.

    The ClusterResolver will then use the parameters to query the Cloud TPU APIs
    for the IP addresses and ports of each Cloud TPU listed.

    Args:
      tpu: A string corresponding to the TPU to use. It can be the TPU name or
        TPU worker gRPC address. If not set, it will try automatically resolve
        the TPU address on Cloud TPUs. If set to "local", it will assume that
        the TPU is directly connected to the VM instead of over the network.
      zone: Zone where the TPUs are located. If omitted or empty, we will assume
        that the zone of the TPU is the same as the zone of the GCE VM, which we
        will try to discover from the GCE metadata service.
      project: Name of the GCP project containing Cloud TPUs. If omitted or
        empty, we will try to discover the project name of the GCE VM from the
        GCE metadata service.
      job_name: Name of the TensorFlow job the TPUs belong to.
      coordinator_name: The name to use for the coordinator. Set to None if the
        coordinator should not be included in the computed ClusterSpec.
      coordinator_address: The address of the coordinator (typically an ip:port
        pair). If set to None, a TF server will be started. If coordinator_name
        is None, a TF server will not be started even if coordinator_address is
        None.
      credentials: GCE Credentials. If None, then we use default credentials
        from the oauth2client
      service: The GCE API object returned by the googleapiclient.discovery
        function. If you specify a custom service object, then the credentials
        parameter will be ignored.
      discovery_url: A URL template that points to the location of the discovery
        service. It should have two parameters {api} and {apiVersion} that when
        filled in produce an absolute URL to the discovery document for that
        service. The environment variable \'TPU_API_DISCOVERY_URL\' will override
        this.

    Raises:
      ImportError: If the googleapiclient is not installed.
      ValueError: If no TPUs are specified.
      RuntimeError: If an empty TPU name is specified and this is running in a
        Google Cloud environment.
    '''
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def master(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, rpc_layer: Incomplete | None = None):
        """Get the Master string to be used for the session.

    In the normal case, this returns the grpc path (grpc://1.2.3.4:8470) of
    first instance in the ClusterSpec returned by the cluster_spec function.

    If a non-TPU name is used when constructing a TPUClusterResolver, that will
    be returned instead (e.g. If the tpus argument's value when constructing
    this TPUClusterResolver was 'grpc://10.240.1.2:8470',
    'grpc://10.240.1.2:8470' will be returned).

    Args:
      task_type: (Optional, string) The type of the TensorFlow task of the
        master.
      task_id: (Optional, integer) The index of the TensorFlow task of the
        master.
      rpc_layer: (Optional, string) The RPC protocol TensorFlow should use to
        communicate with TPUs.

    Returns:
      string, the connection string to use when creating a session.

    Raises:
      ValueError: If none of the TPUs specified exists.
    """
    def get_master(self): ...
    def get_job_name(self): ...
    def get_coordination_service_leader(self):
        """Returns the location for coordination service.

    The coordination service should be located on TPU worker0.

    Returns:
      A string indicate the location path.
    """
    def get_tpu_system_metadata(self):
        """Returns the metadata of the TPU system.

    Users can call this method to get some facts of the TPU system, like
    total number of cores, number of TPU workers and the devices. E.g.
    ```python

    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tpu_system_metadata = resolver.get_tpu_system_metadata()
    num_hosts = tpu_system_metadata.num_hosts
    ```

    Returns:
      A `tf.tpu.experimental.TPUSystemMetadata` object.
    """
    def cluster_spec(self):
        """Returns a ClusterSpec object based on the latest TPU information.

    We retrieve the information from the GCE APIs every time this method is
    called.

    Returns:
      A ClusterSpec containing host information returned from Cloud TPUs,
      or None.

    Raises:
      RuntimeError: If the provided TPU is not healthy.
    """
    def num_accelerators(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, config_proto: Incomplete | None = None):
        """Returns the number of TPU cores per worker.

    Connects to the master and list all the devices present in the master,
    and counts them up. Also verifies that the device counts per host in the
    cluster is the same before returning the number of TPU cores per host.

    Args:
      task_type: Unused.
      task_id: Unused.
      config_proto: Used to create a connection to a TPU master in order to
        retrieve the system metadata.

    Raises:
      RuntimeError: If we cannot talk to a TPU worker after retrying or if the
        number of TPU devices per host is different.
    """
    def set_tpu_topology(self, serialized_tpu_topology) -> None:
        """Sets the tpu topology info stored in this resolver."""
    @property
    def tpu_hardware_feature(self):
        """Returns the tpu topology info stored."""
    @property
    def environment(self):
        """Returns the current environment which TensorFlow is running in."""
    def __deepcopy__(self, memo): ...
