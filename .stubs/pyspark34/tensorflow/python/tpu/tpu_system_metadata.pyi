from _typeshed import Incomplete
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.distribute import device_util as device_util
from tensorflow.python.eager import context as context
from tensorflow.python.framework import config as config, errors as errors, ops as ops
from tensorflow.python.tpu import tpu as tpu
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class TPUSystemMetadata(NamedTuple('TPUSystemMetadata', [('num_cores', Incomplete), ('num_hosts', Incomplete), ('num_of_cores_per_host', Incomplete), ('topology', Incomplete), ('devices', Incomplete)])):
    """Describes some metadata about the TPU system.

  Attributes:
    num_cores: interger. Total number of TPU cores in the TPU system.
    num_hosts: interger. Total number of hosts (TPU workers) in the TPU system.
    num_of_cores_per_host: interger. Number of TPU cores per host (TPU worker).
    topology: an instance of `tf.tpu.experimental.Topology`, which describes the
      physical topology of TPU system.
    devices: a tuple of strings, which describes all the TPU devices in the
      system.
  """
    def __new__(cls, num_cores, num_hosts, num_of_cores_per_host, topology, devices): ...

def get_session_config_with_timeout(timeout_in_secs, cluster_def):
    """Returns a session given a timeout and a cluster configuration."""
def master_job(master, cluster_def):
    """Returns the canonical job name to use to place TPU computations on.

  Args:
    master: A `string` representing the TensorFlow master to use.
    cluster_def: A ClusterDef object describing the TPU cluster.

  Returns:
    A string containing the job name, or None if no job should be specified.

  Raises:
    ValueError: If the user needs to specify a tpu_job_name, because we are
      unable to infer the job name automatically, or if the user-specified job
      names are inappropriate.
  """
