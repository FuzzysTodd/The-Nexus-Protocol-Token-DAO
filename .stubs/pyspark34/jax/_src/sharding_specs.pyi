from _typeshed import Incomplete
from collections.abc import Mapping, Sequence
from jax._src import op_shardings as op_shardings, util as util
from jax._src.lib import pmap_lib as pmap_lib, xla_client as xc
from typing import Any

unsafe_map: Incomplete
map: Incomplete
NoSharding: Incomplete
Chunked: Incomplete
Unstacked: Incomplete
ShardedAxis: Incomplete
Replicated: Incomplete
MeshDimAssignment = ShardedAxis | Replicated
ShardingSpec: Incomplete
OpShardingType = Any

def get_logical_mesh_ids(mesh_shape): ...
def sharding_spec_sharding_proto(self, special_axes: Mapping[int, OpShardingType] | None = None) -> xc.HloSharding:
    """Converts a ShardingSpec to an OpSharding proto.

  See
  https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/xla_data.proto#L601
  for details on the OpSharding proto.
  Unfortunately the semantics are not very well described in the proto spec, but
  the code here might help:
  https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/compiler/xla/experimental/xla_sharding/xla_sharding.py
  """
Index = int | slice | tuple[int | slice, ...]

def spec_to_indices(shape: Sequence[int], spec: ShardingSpec) -> tuple[Index, ...]:
    """Returns numpy-style indices corresponding to a sharding spec.

  Each index describes a shard of the array. The order of the indices is the
  same as the device_buffers of a Array sharded using PmapSharding (i.e. the
  data is laid out row-major).

  Args:
    shape: The shape of the logical array being sharded.
    spec: Describes how the array is sharded and how the shards are assigned to
      the logical mesh.

  Returns:
    A tuple of length equal to the size of the mesh (inferred as the product of
    sharded dimension sizes and all replication factors).  Each element is an
    int, a slice object with step=1, or a tuple thereof, to be treated as an
    index into the full logical array.
  """
def make_sharding_spec(axis_sizes, mesh_axis_pos, num_dimensions, aval_axes): ...
def new_mesh_sharding_specs(axis_sizes, axis_names): ...
def pmap_sharding_spec(nrep, axis_size, sharded_shape: Sequence[int], map_axis: int | None) -> ShardingSpec:
    """Sharding spec for arguments or results of a pmap.
  Args:
    nrep: number of local XLA replicas (product of local axis sizes)
    axis_size: local axis size for outer pmap
    sharded_aval: the aval of the value inside the outer pmap, an instance of
      a ShapedArray.
    map_axis: the axis along which the value is mapped in the outer pmap
  Returns:
    A ShardingSpec.
  """
def create_pmap_sharding_spec(shape: tuple[int, ...], sharded_dim: int = 0, sharded_dim_size: int | None = None): ...
