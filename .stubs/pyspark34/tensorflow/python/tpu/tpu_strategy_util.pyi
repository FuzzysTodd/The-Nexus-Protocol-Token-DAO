from _typeshed import Incomplete
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.distribute.cluster_resolver.tpu_cluster_resolver import TPUClusterResolver as TPUClusterResolver
from tensorflow.python.eager import context as context, monitoring as monitoring
from tensorflow.python.eager.def_function import function as function, functions_run_eagerly as functions_run_eagerly, run_functions_eagerly as run_functions_eagerly
from tensorflow.python.framework import device as device, errors as errors, ops as ops
from tensorflow.python.tpu import topology as topology, tpu as tpu
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import tf_export as tf_export

def initialize_tpu_system(cluster_resolver: Incomplete | None = None):
    """Initialize the TPU devices.

  Args:
    cluster_resolver: A tf.distribute.cluster_resolver.TPUClusterResolver,
        which provides information about the TPU cluster.
  Returns:
    The tf.tpu.Topology object for the topology of the TPU cluster. If called
    inside tf.function, it returns the serialized topology object instead.

  Raises:
    RuntimeError: If running inside a tf.function.
    NotFoundError: If no TPU devices found in eager mode.
  """
def get_initialized_tpu_systems():
    """Returns all currently initialized tpu systems.

  Returns:
     A dictionary, with tpu name as the key and the tpu topology as the value.
  """
def shutdown_tpu_system(cluster_resolver: Incomplete | None = None) -> None:
    """Shuts down the TPU devices.

  This will clear all caches, even those that are maintained through sequential
  calls to tf.tpu.experimental.initialize_tpu_system, such as the compilation
  cache.

  Args:
    cluster_resolver: A tf.distribute.cluster_resolver.TPUClusterResolver,
        which provides information about the TPU cluster.

  Raises:
    RuntimeError: If no TPU devices found for eager execution or if run in a
        tf.function.
  """
