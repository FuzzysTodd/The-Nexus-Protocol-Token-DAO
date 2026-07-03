from _typeshed import Incomplete
from tensorflow.dtensor.python import config as config, dtensor_device as dtensor_device, gen_dtensor_ops as gen_dtensor_ops, layout as layout_lib
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import constant_op as constant_op, errors as errors, ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.tpu import topology as topology
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Dict, List, Optional

class _CoreLocation:
    """Represents a TPU core's location in the mesh."""
    x: Incomplete
    y: Incomplete
    z: Incomplete
    core: Incomplete
    def __init__(self, x: int = 0, y: int = 0, z: int = 0, core: int = 0) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    def to_list(self): ...

def shutdown_tpu_system():
    """Shuts down the TPU system."""
def tpu_system_init_helper(task_id, num_tasks, num_devices, use_tfrt_host_runtime: bool = True):
    """A helper function to initialize multi-client tpu system."""
def initialize_tpu_system() -> None:
    """Initializes the TPU system."""
def create_tpu_mesh(mesh_dim_names: List[str], mesh_shape: List[int], mesh_name: str, ring_dims: Optional[int] = None, ring_axes: Optional[List[str]] = None, ring_bounds: Optional[List[int]] = None, can_split_host_across_rings: bool = True, build_ring_across_rings: bool = False, rotate_ring_across_rings: bool = False, use_xla_spmd: bool = ...) -> layout_lib.Mesh:
    '''Returns a distributed TPU mesh optimized for AllReduce ring reductions.

  Only as many as leading axes specified by `ring_axes` as necessary will be
  used to build rings, as long as the subslice formed by these axes have enough
  cores to contain a ring of the required size. The leftover axes in `ring_axes`
  won\'t affect results.

  This function always uses all TPU devices, and offers more customization than
  `tf.experimental.dtensor.create_distributed_mesh`.

  Args:
    mesh_dim_names: List of mesh dimension names.
    mesh_shape: Shape of the mesh.
    mesh_name: A unique name for the mesh. If empty, internally generate one.
    ring_dims: Optional; The number of leading (ring_dims > 0) or trailing
      (ring_dims < 0) mesh dimensions to build rings for. If unspecified, build
      rings for all but the first dimension.
    ring_axes: Optional; A permutation of ["x", "y", "z", "core"], specifying
      the order of TPU topology axes to build rings in. If unspecified, default
      to ["core", "x", "y", "z"].
    ring_bounds: Optional; The maximum number of devices on each axis, in the x,
      y, z, core order. If unspecified, default to physical topology limits.
    can_split_host_across_rings: Optional; If true, devices attached to the same
      host (i.e., DTensor client) may get assigned to different rings. Setting
      it to false may cause some combinations of arguments to be infeasible; see
      DeviceAssignmentTest.testCreateMesh[No]SplittingHosts* for examples.
    build_ring_across_rings: Optional; If true, also build a data-parallel ring
      across model-parallel rings. This ring could be strided.
    rotate_ring_across_rings: Optional; If true, build the data-parallel ring in
      column-major instead of row-major order.
    use_xla_spmd: Boolean when True, will use XLA SPMD instead of
      DTensor SPMD.
  '''
def get_device_ids(mesh: layout_lib.Mesh, client_id: Optional[int] = None) -> List[int]:
    """Returns the device IDs of all TPU cores local to the given client.

  A device ID is a non-negative integer that uniquely identifies a device in the
  mesh. For example, for a 2x2 mesh ('x', 'y'), this function returns a
  permutation of [0, 1, 2, 3].

  Note that device IDs and device locations are equivalent. The former is a
  linearization of the latter along mesh dimensions.

  Args:
    mesh: A TPU mesh.
    client_id: Optional; A DTensor client ID. If empty, query this client.
  """
def get_device_locations(mesh: layout_lib.Mesh, client_id: Optional[int] = None) -> List[Dict[str, int]]:
    """Returns the device locations of all TPU cores local to the given client.

  A device location is a dictionary from dimension names to indices on those
  dimensions. For example, for a 2x2 mesh ('x', 'y'), this function returns a
  permutation of this list:

    [{'x': 0, 'y': 0},
     {'x': 0, 'y': 1},
     {'x': 1, 'y': 0},
     {'x': 1, 'y': 1}].

  Note that device IDs and device locations are equivalent. The former is a
  linearization of the latter along mesh dimensions.

  Args:
    mesh: A TPU mesh.
    client_id: Optional; A DTensor client ID. If empty, query this client.
  """
def dtensor_initialize_tpu_system(enable_coordination_service: bool = False) -> None:
    """Deprecated way to initialize the TPU system."""
def dtensor_shutdown_tpu_system() -> None:
    """Deprecated way to shutodwn the TPU system."""
