from tensorflow.dtensor.python import accelerator_util as accelerator_util, api as api, config as config, layout as layout, tpu_util as tpu_util
from tensorflow.python.eager import context as context
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import List, Optional, Tuple

def create_mesh(mesh_dims: Optional[List[Tuple[str, int]]] = None, mesh_name: str = '', devices: Optional[List[str]] = None, device_type: Optional[str] = None, use_xla_spmd: bool = ...) -> layout.Mesh:
    """Creates a single-client mesh.

  If both `mesh_dims` and `devices` are specified, they must match each otehr.
  As a special case, when all arguments are missing, this creates a 1D CPU mesh
  with an empty name, assigning all available devices to that dimension.

  Args:
    mesh_dims: A list of (dim_name, dim_size) tuples. Defaults to a single
      batch-parallel dimension called 'x' using all devices. As a special case,
      a single-element mesh_dims whose dim_size is -1 also uses all devices.
    mesh_name: Name of the created mesh. Defaults to ''.
    devices: String representations of devices to use. This is the device part
      of tf.DeviceSpec, e.g. 'CPU:0'. Defaults to all available logical devices.
    device_type: If `devices` is missing, the type of devices to use. Defaults
      to 'CPU'.
    use_xla_spmd: Boolean when True, will use XLA SPMD instead of
      DTensor SPMD.

  Returns:
    A single-client mesh created from specified or default arguments.
  """
def create_distributed_mesh(mesh_dims: List[Tuple[str, int]], mesh_name: str = '', local_devices: Optional[List[str]] = None, device_type: Optional[str] = None, use_xla_spmd: bool = ...) -> layout.Mesh:
    """Creates a distributed mesh.

  This is similar to `create_mesh`, but with a different set of arguments to
  create a mesh that spans evenly across a multi-client DTensor cluster.

  For CPU and GPU meshes, users can choose to use fewer local devices than what
  is available `local_devices`.

  For TPU, only meshes that uses all TPU cores is supported by the DTensor
  runtime.

  Args:
    mesh_dims: A list of (dim_name, dim_size) tuples.
    mesh_name: Name of the created mesh. Defaults to ''.
    local_devices: String representations of devices to use. This is the device
      part of tf.DeviceSpec, e.g. 'CPU:0'. Defaults to all available local
      logical devices.
    device_type: Type of device to build the mesh for. Defaults to 'CPU'.
      Supported values are 'CPU', 'GPU', 'TPU'.6
    use_xla_spmd: Boolean when True, will use XLA SPMD instead of
      DTensor SPMD.

  Returns:
    A mesh that spans evenly across all DTensor clients in the cluster.
  """
def barrier(mesh: layout.Mesh, barrier_name: Optional[str] = None, timeout_in_ms: Optional[int] = None):
    """Runs a barrier on the mesh.

  Upon returning from the barrier, all operations run before the barrier
  would have completed across all clients. Currently we allocate a fully
  sharded tensor with mesh shape and run an all_reduce on it.

  Example:

  A barrier can be used before application exit to ensure completion of pending
  ops.

  ```python

  x = [1, 2, 3]
  x = dtensor.relayout(x, dtensor.Layout.batch_sharded(mesh, 'batch', 1))
  dtensor.barrier(mesh)

  # At this point all devices on all clients in the mesh have completed
  # operations before the barrier. Therefore it is OK to tear down the clients.
  sys.exit()
  ```

  Args:
    mesh: The mesh to run the barrier on.
    barrier_name: The name of the barrier. Mainly used for logging purpose.
    timeout_in_ms: The timeout of the barrier in ms. If omitted, blocks
      indefinitely till the barrier is reached from all clients.
  """
