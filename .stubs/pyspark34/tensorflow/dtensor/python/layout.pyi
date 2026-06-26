import numpy as np
from _typeshed import Incomplete
from tensorflow.dtensor.proto import layout_pb2 as layout_pb2
from tensorflow.dtensor.python import config as config
from tensorflow.python import _pywrap_dtensor_device
from tensorflow.python.framework import device as tf_device, ops as ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Dict, List, NamedTuple, Optional

UNSHARDED: str
MATCH: str
USE_XLA_SPMD: bool

class MeshDimension(NamedTuple):
    name: Incomplete
    size: Incomplete

class Mesh(_pywrap_dtensor_device.Mesh):
    """Represents a Mesh configuration over a certain list of Mesh Dimensions.

  A mesh consists of named dimensions with sizes, which describe how a set of
  devices are arranged. Defining tensor layouts in terms of mesh dimensions
  allows us to efficiently determine the communication required when computing
  an operation with tensors of different layouts.

  A mesh provides information not only about the placement of the tensors but
  also the topology of the underlying devices. For example, we can group 8 TPUs
  as a 1-D array for data parallelism or a `2x4` grid for (2-way) data
  parallelism and (4-way) model parallelism.

  Note: the utilities `dtensor.create_mesh` and
  `dtensor.create_distributed_mesh` provide a simpler API to create meshes for
  single- or multi-client use cases.
  """
    def __init__(self, dim_names: List[str], global_device_ids: np.ndarray, local_device_ids: List[int], local_devices: List[tf_device.DeviceSpec], mesh_name: str = '', global_devices: Optional[List[tf_device.DeviceSpec]] = None, use_xla_spmd: bool = ...) -> None:
        """Builds a Mesh.

    The `dim_names` and `global_device_ids` arguments describe the dimension
    names and shape for the mesh.

    For example,

    ```python
      dim_names = ('x', 'y'),
      global_device_ids = [[0, 1],
                           [2, 3],
                           [4, 5]]
    ```

    defines a 2D mesh of shape 3x2. A reduction over the 'x' dimension will
    reduce across columns (0, 2, 4) and (1, 3, 5), and a reduction over the 'y'
    dimension reduces across rows.

    Note: the utilities `dtensor.create_mesh` and
    `dtensor.create_distributed_mesh` provide a simpler API to create meshes for
    single- or multi-client use cases.

    Args:
      dim_names: A list of strings indicating dimension names.
      global_device_ids: An ndarray of global device IDs is used to compose
        DeviceSpecs describing the mesh. The shape of this array determines the
        size of each mesh dimension. Values in this array should increment
        sequentially from 0. This argument is the same for every DTensor client.
      local_device_ids: A list of local device IDs equal to a subset of values
        in global_device_ids. They indicate the position of local devices in the
        global mesh. Different DTensor clients must contain distinct
        local_device_ids contents. All local_device_ids from all DTensor clients
        must cover every element in global_device_ids.
      local_devices: The list of devices hosted locally. The elements correspond
        1:1 to those of local_device_ids.
      mesh_name: The name of the mesh. Currently, this is rarely used, and is
        mostly used to indicate whether it is a CPU, GPU, or TPU-based mesh.
      global_devices (optional): The list of global devices. Set when multiple
        device meshes are in use.
      use_xla_spmd (optional): Boolean when True, will use XLA SPMD instead of
        DTensor SPMD.
    """
    def __eq__(self, other): ...
    def __getitem__(self, dim_name: str) -> MeshDimension: ...
    def __hash__(self): ...
    def __reduce__(self): ...
    def as_proto(self) -> layout_pb2.MeshProto:
        """Returns mesh protobuffer."""
    def coords(self, device_idx: int) -> ops.Tensor:
        """Converts the device index into a tensor of mesh coordinates."""
    def dim_size(self, dim_name: str) -> int:
        """Returns the size of a dimension."""
    @staticmethod
    def from_proto(proto: layout_pb2.MeshProto) -> Mesh:
        """Construct a mesh instance from input `proto`."""
    @staticmethod
    def from_string(mesh_str: str) -> Mesh:
        """Construct a mesh instance from input `proto`."""
    def host_mesh(self):
        """Returns the 1-1 mapped host mesh."""
    def is_remote(self) -> bool:
        """Returns True if a Mesh contains only remote devices."""
    def local_device_ids(self) -> List[int]:
        """Returns a list of local device IDs."""
    def local_device_locations(self) -> List[Dict[str, int]]:
        """Returns a list of local device locations.

    A device location is a dictionary from dimension names to indices on those
    dimensions.
    """
    def local_devices(self) -> List[str]:
        """Returns a list of local device specs represented as strings."""
    def min_global_device_id(self) -> int:
        """Returns the minimum global device ID."""
    def num_local_devices(self) -> int:
        """Returns the number of local devices."""
    def shape(self) -> List[int]:
        """Returns the shape of the mesh."""
    @property
    def size(self) -> int: ...
    @property
    def strides(self) -> List[int]:
        """Returns the strides tensor array for this mesh.

    If the mesh shape is `[a, b, c, d]`, then the strides array can be computed
    as `[b*c*d, c*d, d, 1]`. This array can be useful in computing local device
    offsets given a device ID. Using the same example, the device coordinates of
    the mesh can be computed as:

    ```
    [(device_id / (b*c*d)) % a,
     (device_id / (c*d))   % b,
     (device_id / (d))     % c,
     (device_id)           % d]
    ```

    This is the same as `(device_id // mesh.strides) % mesh.shape`.

    Returns:
      The mesh strides as an integer tensor.
    """
    def unravel_index(self):
        """Returns a dictionary from device ID to {dim_name: dim_index}.

    For example, for a 3x2 mesh, return this:

    ```
      { 0: {'x': 0, 'y', 0},
        1: {'x': 0, 'y', 1},
        2: {'x': 1, 'y', 0},
        3: {'x': 1, 'y', 1},
        4: {'x': 2, 'y', 0},
        5: {'x': 2, 'y', 1} }
    ```
    """

class Layout:
    '''Represents the layout information of a DTensor.

  A layout describes how a distributed tensor is partitioned across a mesh (and
  thus across devices). For each axis of the tensor, the corresponding
  sharding spec indicates which dimension of the mesh it is sharded over. A
  special sharding spec `UNSHARDED` indicates that axis is replicated on
  all the devices of that mesh.

  For example, let\'s consider a 1-D mesh:

  ```
  Mesh(["TPU:0", "TPU:1", "TPU:2", "TPU:3", "TPU:4", "TPU:5"], [("x", 6)])
  ```

  This mesh arranges 6 TPU devices into a 1-D array. `Layout([UNSHARDED], mesh)`
  is a layout for rank-1 tensor which is replicated on the 6 devices.

  For another example, let\'s consider a 2-D mesh:

  ```
  Mesh(["TPU:0", "TPU:1", "TPU:2", "TPU:3", "TPU:4", "TPU:5"],
       [("x", 3), ("y", 2)])
  ```

  This mesh arranges 6 TPU devices into a `3x2` 2-D array.
  `Layout(["x", UNSHARDED], mesh)` is a layout for rank-2 tensor whose first
  axis is sharded on mesh dimension "x" and the second axis is replicated. If we
  place `np.arange(6).reshape((3, 2))` using this layout, the individual
  components tensors would look like:

  ```
  Device  |  Component
   TPU:0     [[0, 1]]
   TPU:1     [[0, 1]]
   TPU:2     [[2, 3]]
   TPU:3     [[2, 3]]
   TPU:4     [[4, 5]]
   TPU:5     [[4, 5]]
  ```
  '''
    sharding_specs: Incomplete
    rank: Incomplete
    mesh: Incomplete
    shape: Incomplete
    def __init__(self, sharding_specs: List[str], mesh: Mesh) -> None:
        """Builds a Layout from a list of dimension names and a Mesh.

    Args:
      sharding_specs: List of sharding specifications, each corresponding to a
        tensor axis. Each specification (dim_sharding) can either be a mesh
        dimension or the special value UNSHARDED.
      mesh: A mesh configuration for the Tensor.

    Returns:
      A valid Layout built with given layout & mesh.
    """
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def as_proto(self) -> layout_pb2.LayoutProto:
        """Create a proto representation of a layout."""
    @staticmethod
    def batch_sharded(mesh: Mesh, batch_dim: str, rank: int) -> Layout:
        """Returns a layout sharded on batch dimension."""
    def delete(self, dims: List[int]) -> Layout:
        """Returns the layout with the give dimensions deleted."""
    @staticmethod
    def from_str(layout_str: bytes) -> Layout:
        """Creates an instance from a serialized Protobuf binary string."""
    @staticmethod
    def from_string(layout_str: str) -> Layout:
        """Creates an instance from a human-readable string."""
    @staticmethod
    def inner_sharded(mesh: Mesh, inner_dim: str, rank: int) -> Layout:
        """Returns a layout sharded on inner dimension."""
    def is_fully_replicated(self) -> bool:
        """Returns True if all tensor axes are replicated."""
    def mesh_proto(self) -> layout_pb2.MeshProto:
        """Returns the underlying mesh in Protobuf format."""
    def num_shards(self, idx: int) -> int:
        """Returns the number of shards for tensor dimension `idx`."""
    def offset_to_shard(self):
        """Mapping from offset in a flattened list to shard index."""
    def offset_tuple_to_global_index(self, offset_tuple):
        """Mapping from offset to index in global tensor."""
    @staticmethod
    def replicated(mesh: Mesh, rank: int) -> Layout:
        """Returns a replicated layout of rank `rank`."""
    def serialized_string(self) -> bytes:
        """Returns a serialized Protobuf binary string representation."""
    def to_string(self) -> str:
        """Returns a human-readable string representation."""
