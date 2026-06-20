import torch
import torch.nn as nn
from _typeshed import Incomplete
from torch.distributed._tensor.device_mesh import DeviceMesh
from torch.distributed._tensor.placement_types import Placement
from typing import Callable, Sequence

__all__ = ['DTensor', 'distribute_tensor', 'distribute_module']

class _ToTorchTensor(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input: DTensor): ...
    @staticmethod
    def backward(ctx, grad_output: torch.Tensor): ...

class _FromTorchTensor(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input: torch.Tensor, device_mesh: DeviceMesh, placements: Sequence[Placement], run_check: bool) -> DTensor: ...
    @staticmethod
    def backward(ctx, grad_output: DTensor): ...

class DTensor(torch.Tensor):
    @staticmethod
    def __new__(cls, local_tensor: torch.Tensor, device_mesh: DeviceMesh, placements: Sequence[Placement], *, size: torch.Size, requires_grad: bool = False) -> DTensor:
        '''
        Construct a DTensor from a local tensor, device mesh, and placement and
        other tensor properties (i.e. shape, requires_grad, strides, etc).
        Note: This is not a public API and it\'s only supposed to be used by the
            operator implementations and internals. If you want to construct a
            DTensor from a local tensor, consider using `DTensor.from_local`, if
            you want to construct a DTensor from a "global" tensor (where you
            already have tensor initialized and want to shard this tensor),
            consider using `distribute_tensor`.
        '''
    @classmethod
    def __torch_dispatch__(cls, func, types, args=(), kwargs: Incomplete | None = None): ...
    @classmethod
    def from_local(cls, local_tensor: torch.Tensor, device_mesh: DeviceMesh | None = None, placements: Sequence[Placement] | None = None, run_check: bool = True) -> DTensor:
        """
        Create a :class:`DTensor` from a local torch.Tensor on each rank
        according to the `device_mesh` and `placements` specified.

        Args:
            local_tensor (torch.Tensor): local torch.Tensor on each rank.
            device_mesh (:class:`DeviceMesh`, optional): DeviceMesh to place the
                tensor, if not specified, must be called under a DeviceMesh
                context manager, default: None
            placements (List[:class:`Placement`], optional): the placements that
                describes how to place the local torch.Tensor on DeviceMesh, must
                have the same number of elements as `device_mesh.ndim`. If not
                specified, we will by default replicate the tensor across the
                `device_mesh` from the first rank of each dimension of the `device_mesh`.
            run_check (bool, optional): indicate whether to run check across ranks
                to check meta information and data. if have :class:`Replicate` in
                `placements`, the data on first rank of the device mesh dimension
                will be broadcasted to other ranks.

        Returns:
            A :class:`DTensor` object

        .. note:: `from_local` is differentiable, the `requires_grad` of the created
            `DTensor` object will depend on if `local_tensor` requires_grad or not.
        """
    def to_local(self) -> torch.Tensor:
        """
        Get the local tensor of this DTensor on its current rank. For sharding it returns
        a local shard of the logical tensor view, for replication it returns the replica on
        its current rank.

        Returns:
            A :class:`torch.Tensor` object that represents the local tensor of its current rank.

        .. note:: `to_local` is differentiable, the `requires_grad` of the local tensor returned
            will depend on if the `DTensor` requires_grad or not.
        """
    def redistribute(self, device_mesh: DeviceMesh | None = None, placements: Sequence[Placement] | None = None) -> DTensor:
        """
        `redistribute` performs necessary collective operations that redistribute the current
        DTensor from its current placements to a new placements, or from is current DeviceMesh
        to a new DeviceMesh. i.e. we can turn a Sharded DTensor to a Replicated DTensor by
        specifying a Replicate placement for each dimension of the DeviceMesh.

        Args:
            device_mesh (:class:`DeviceMesh`, optional): DeviceMesh to place the
                DTensor, if not specified, must be called under a DeviceMesh
                context manager, default: None
            placements (List[:class:`Placement`], optional): the new placements that
                describes how to place the DTensor into the DeviceMesh, must
                have the same number of elements as `device_mesh.ndim`.

        Returns:
            A :class:`DTensor` object

        .. note:: `redistribute` is differentiable.
        """
    @property
    def device_mesh(self) -> DeviceMesh:
        """
        The :class:`DeviceMesh` attribute that associates with this DTensor object.

        .. note:: device_mesh is a read-only property, it can not be set.
        """
    @property
    def placements(self) -> Sequence[Placement]:
        """
        The placements attribute of this DTensor that describes the layout of this
        DTensor on the its DeviceMesh.

        .. note:: placements is a read-only property, it can not be set.
        """

def distribute_tensor(tensor: torch.Tensor, device_mesh: DeviceMesh | None = None, placements: Sequence[Placement] | None = None) -> DTensor:
    """
    Distribute a torch.Tensor to the `device_mesh` according to the `placements`
    specified. The rank of `device_mesh` and `placements` must be the same.

    Args:
        tensor (torch.Tensor): torch.Tensor to be distributed. Note that if you
            want to shard a tensor on a dimension that is not evenly divisible by
            the number of devices in that mesh dimension, we use `torch.tensor_split`
            semantic to shard the tensor and scatter the shards.
        device_mesh (:class:`DeviceMesh`, optional): DeviceMesh to distribute the
            tensor, if not specified, must be called under a DeviceMesh context
            manager, default: None
        placements (List[:class:`Placement`], optional): the placements that
            describes how to place the tensor on DeviceMesh, must have the same
            number of elements as `device_mesh.ndim`. If not specified, we will
            by default replicate the tensor across the `device_mesh` from the
            first rank of each dimension of the `device_mesh`.

    Returns:
        A :class:`DTensor` object
    """
def distribute_module(module: nn.Module, device_mesh: DeviceMesh | None = None, partition_fn: Callable[[str, nn.Module, DeviceMesh], None] | None = None, input_fn: Callable[..., None] | None = None, output_fn: Callable[..., None] | None = None) -> nn.Module:
    """
    This function converts all module parameters to :class:`DTensor` parameters
    according to the `partition_fn` specified. It could also control the input or
    output of the module by specifying the `input_fn` and `output_fn`. (i.e. convert
    the input to :class:`DTensor`, convert the output back to torch.Tensor)
    Args:
        module (:class:`nn.Module`): user module to be partitioned.
        device_mesh (:class:`DeviceMesh`): the device mesh to place the module.
        partition_fn (Callable): the function to partition parameters (i.e. shard certain
            parameters across the `device_mesh`). If `partition_fn` is not specified,
            by default we replicate all module parameters of `module` across the mesh.
        input_fn (Callable): specify the input distribution, i.e. could control how the
            input of the module is sharded. `input_fn` will be installed as a module
            `forward_pre_hook` (pre forward hook).
        output_fn (Callable): specify the output distribution, i.e. could control how the
            output is sharded, or convert it back to torch.Tensor. output_fn will be
            installed as a module `forward_hook` (post forward hook).

    Returns:
        A module that contains parameters/buffers that are all `DTensor`s.
    """
