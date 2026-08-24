import torch
from _typeshed import Incomplete
from torch.distributed.distributed_c10d import GroupMember as GroupMember, ProcessGroup as ProcessGroup, ReduceOp as ReduceOp, Work as Work, all_gather as all_gather, all_reduce as all_reduce, all_to_all as all_to_all, broadcast as broadcast, get_global_rank as get_global_rank, get_rank as get_rank, get_world_size as get_world_size, init_process_group as init_process_group, is_initialized as is_initialized, new_group as new_group, reduce_scatter as reduce_scatter, scatter as scatter
from typing import List, TypeVar

def get_global_device_mesh() -> DeviceMesh: ...
def set_global_device_mesh(mesh: DeviceMesh | None) -> None: ...
T = TypeVar('T')
NDIntList: Incomplete
MeshExprT: Incomplete

class DeviceMesh:
    '''
    DeviceMesh represents a mesh of devices, where layout of devices could be
    represented as a n-d dimension array, and each value of the n-d dimensional
    array is the global id of the default process group ranks.

    DeviceMesh could be used to describe the layout of devices across the cluster,
    and serves as a proxy for communication among the device lists within the cluster.

    We use the default ProcessGroup in this DeviceMesh class to implement proper
    communications. Note that we also add collective wrappers in this class. This is
    used to decouple detailed communication backend with the underlying
    DTensor implementation.

    DeviceMesh can be used as a context manager.
    Args:
        device_type (str): device type of the mesh. Currently supports: cpu, cuda.
        mesh (ndarray): could be a multi-dimension array or an integer tensor that
            describes the layout of devices, the ids are global ids of the
            default process group.
        dim_groups (List[ProcessGroup], optional): The ProcessGroup used per mesh
            dimension.

    Returns:
        A :class:`DeviceMesh` object

    Example (2 host with 4 GPUs each):
        ```
        # The following program runs on each process/rank in SPMD manner.
        # initialized default world
        torch.distributed.init_process_group(backend="nccl", world_size=8)
        # initialize device mesh as (2, 4) to represent the topology
        # of cross-host(dim 0), and within-host (dim 1)
        mesh = DeviceMesh(device_type="cuda",
                          mesh=[
                            [0, 1, 2, 3],
                            [4, 5, 6, 7]
                          ])
        ```
        A reduction over the first dimension of mesh will reduce across
        columns (0, 4), .. and (3, 7), a reduction over the second dimension
        of mesh reduces across rows (0, 1, 2, 3) and (4, 5, 6, 7)

    '''
    device_type: str
    mesh: torch.Tensor
    def __init__(self, device_type: str, mesh: MeshExprT, dim_groups: List[ProcessGroup] | None = None) -> None: ...
    def __enter__(self) -> DeviceMesh: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_traceback: types.TracebackType | None) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other: object) -> bool: ...
    def get_dim_groups(self) -> List[ProcessGroup]: ...
    def size(self, dim: int = 0): ...
    @property
    def ndim(self) -> int: ...
    def backend(self) -> str: ...
    def get_rank(self) -> int: ...
    def get_coordinate_on_dim(self, dim: int) -> int | None:
        """
        Return the relative index of this rank relative to a given
        dimension of the mesh. If this rank is not part of the mesh, return None.
        """
    def scatter(self, output: torch.Tensor, scatter_list: List[torch.Tensor], mesh_dim: int = 0, async_op: bool = False) -> Work | None:
        """
        scatter a list of tensors to a device mesh dimension. We by default
        use the first rank of the mesh dimension as the source of truth, i.e
        for a 2d mesh [[0, 1], [2, 3]], if we scatter on mesh_dim = 1, we will
        scatter the tensor list on rank 0 to rank 0/1, and tensor list on rank
        2 to rank 2/3.

        Args:
            output (torch.Tensor): the tensor to receive the scattered list.
            scatter_list (List[torch.Tensor]): the tensor list to be scattered.
            mesh_dim (int, optional): indicate which mesh dimension we want
                to scatter on, we by default choose the first rank on the
                mesh dimension as source of truth.

        Returns:
            A :class:`Work` object
        """
    def broadcast(self, tensor: torch.Tensor, mesh_dim: int = 0, async_op: bool = False) -> Work | None:
        """
        broadcast the tensor to a device mesh dimension. We by default
        use the first rank of the mesh dimension as the source of truth, i.e
        for a 2d mesh [[0, 1], [2, 3]], if we broadcast on mesh_dim = 1, we will
        broadcast the tensor on rank 0 to rank 0/1, and tensor on rank 2
        to rank 2/3.

        Args:
            tensor (torch.Tensor): tensor to broadcast.
            mesh_dim (int, optional): indicate which mesh dimension we want
                to scatter on, we by default choose the first rank on the
                mesh dimension as source of truth.

        Returns:
            A :class:`Work` object
        """
    def all_gather(self, tensor_list: List[torch.Tensor], tensor: torch.Tensor, mesh_dim: int = 0, async_op: bool = False) -> Work | None:
        """
        all_gather the tensor on each rank to the tensor_list on a
        device mesh dimension.

        Args:
            tensor_list (List[torch.Tensor]): The gathered tensor list.
            tensor (torch.Tensor): tensor to be gathered on each rank.
            mesh_dim (int, optional): indicate which mesh dimension we want
                to scatter on, we by default choose the first rank on the
                mesh dimension as source of truth.

        Returns:
            A :class:`Work` object
        """
    def all_reduce(self, tensor: torch.Tensor, op: ReduceOp = ..., mesh_dim: int = 0, async_op: bool = False) -> Work | None:
        """
        all_reduce the tensor on each rank on a device mesh dimension, and
        return an output tensor on each rank after all_reduce.

        Args:
            tensor (torch.Tensor): tensor to be all_reduced on each rank.
            op (:class:`torch.distributed.distributed_c10d.ReduceOp, optional):
                the reduction op of all_reduce (i.e. ReduceOp.SUM)
            mesh_dim (int, optional): indicate which mesh dimension we want
                to reduce on.

        Returns:
            A :class:`Work` object
        """
    def reduce_scatter(self, output: torch.Tensor, input_list: List[torch.Tensor], op: ReduceOp = ..., mesh_dim: int = 0, async_op: bool = False) -> Work | None:
        """
        reduce the input_list on each rank on a device mesh dimension, and scatter
        the results to the output tensor on each rank.

        Args:
            output (torch.Tensor): tensor to receive the scattered result.
            input_list (List[torch.Tensor]): tensor list to be reduced and scattered
                and scattered on each rank.
            op (:class:`torch.distributed.distributed_c10d.ReduceOp, optional):
                the reduction op of reduce_scatter (i.e. ReduceOp.SUM)
            mesh_dim (int, optional): indicate which mesh dimension we want
                to scatter on.

        Returns:
            A :class:`Work` object
        """
    def all_to_all(self, output_tensor_list: List[torch.Tensor], input_tensor_list: List[torch.Tensor], mesh_dim: int = 0, async_op: bool = False) -> Work | None: ...
