import torch
import torch.distributed.distributed_c10d as c10d
from _typeshed import Incomplete
from dataclasses import dataclass
from torch.distributed._spmd.comm_tensor import CommTensor as CommTensor
from torch.distributed._tensor.device_mesh import DeviceMesh as DeviceMesh
from typing import List, Sequence, Tuple

class Placement:
    def is_shard(self, dim: int | None = None) -> bool: ...
    def is_replicate(self) -> bool: ...
    def is_partial(self) -> bool: ...

class Shard(Placement):
    dim: Incomplete
    def __init__(self, dim) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class Replicate(Placement):
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class _Partial(Placement):
    reduce_op: Incomplete
    def __init__(self, reduce_op: c10d.ReduceOp = ...) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

@dataclass
class DTensorSpec:
    mesh: DeviceMesh
    placements: Sequence[Placement]
    shape: torch.Size
    ndim: int = ...
    def __post_init__(self) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, __o: object) -> bool: ...
    @property
    def dim_map(self) -> List[int]:
        """
        dim_map is a property we derive from `placements` of
        the distributed tensor. It simply return a list of ints
        where dim_map[i] denotes the sharding mapping to the mesh
        dimension, and len(dim_map) == dist_tensor.ndim
        dim_map[i] = -1: means tensor dim i replicate on mesh
        dim_map[i] = j: means tensor dim i shard on mesh dim j

        For example, we have a dist tensor that have the shape of
        [18, 20, 30], and device_mesh([0, 1, 2, 3]), placements:
        [Shard(1)], the dim_map of this placement would be:
        [-1, 0, -1]. This representation is pretty helpful during
        sharding propagation where we could know exactly each
        tensor dimension is sharded or not.

        Note that if placements contains `_Partial`, we have to
        explicitly deal with it, so that when we create a DTensorSpec
        with dim_map, we could properly record the pending sums.
        """
    @property
    def sums(self) -> List[int]:
        """
        sums is a property we derive from `placements` of the
        distributed tensor. It simply return a list of ints where
        sums[i] denotes the pending sum (partial) on mesh dim i
        """
    @property
    def local_shape(self) -> Tuple[int, ...]:
        """
        Compute the shape of a local shard of the given DTensor on its current
        coordinate of the mesh.
        """
    @property
    def local_offsets(self) -> Tuple[int, ...]:
        """
        Compute the offsets of a local shard of the given DTensor on its current
        global rank. This is mostly used by distributed checkpointing to know the
        exact offsets of the local shard.
        """
    @classmethod
    def from_dim_map(cls, mesh: DeviceMesh, dim_map: List[int], sums: List[int], shape: torch.Size) -> DTensorSpec:
        """
        Construct a DTensorSpec from dim_map list and pending sum.

        Args:
            mesh (class:`DeviceMesh`): device mesh to be used in the DTensorSpec
            dim_map (List[int]): a list of integer that represents sharding on each
                tensor dimension, see `dim_map` property doc for details
            sums (List[int]): a list of integer that represents the dist tensor have
                pending sum on which device mesh dimension.
            shape (torch.Size): shape of the DTensor associated with this spec.

        Return:
            a class:`DTensorSpec` object
        """
    def __init__(self, mesh, placements, shape, ndim) -> None: ...
