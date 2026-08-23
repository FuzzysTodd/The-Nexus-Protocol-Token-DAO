import torch.nn as nn
from torch.distributed._tensor import DeviceMesh
from torch.distributed.tensor.parallel.style import ParallelStyle
from typing import Dict

__all__ = ['parallelize_module']

def parallelize_module(module: nn.Module, device_mesh: DeviceMesh, parallelize_plan: ParallelStyle | Dict[str, ParallelStyle], tp_mesh_dim: int = 0) -> nn.Module:
    '''
    The API to apply Tensor Parallelism (TP) in PyTorch. We parallelize module
    or sub_modules based on a parallelize_plan. The parallelize_plan contains
    :class:`ParallelStyle`, which indicates how user wants the module or sub_module
    to be parallelized.

    User can also specify different parallel style per module fully qualifed name (FQN).
    The API supports 2D parallelism natively by accepting an n-dimension device_mesh
    and users just need to specify the dimension where we perform tensor parallelism on.

    Args:
        module (:class:`nn.Module`):
            Module to be parallelized.
        device_mesh (:class:`DeviceMesh`):
            Object which describes the mesh topology
            of devices for the DTensor.
        parallelize_plan (Union[:class:`ParallelStyle`, Dict[str, :class:`ParallelStyle`]]):
            The plan used to parallelize the module. It can be either a
            :class:`ParallelStyle` object which contains how
            we prepare input/output for Tensor Parallelism or it can be a
            dict of module FQN and its corresponding :class:`ParallelStyle` object.
        tp_mesh_dim (int):
            The dimension of ``device_mesh`` where we perform
            Tensor Parallelism on.

    Return:
        A :class:`nn.Module` object parallelized.

    Example::
        >>> # xdoctest: +SKIP("distributed")
        >>> from torch.distributed._tensor.parallel import parallelize_module, PairwiseParallel
        >>>
        >>> # Define the module.
        >>> m = Model(...)
        >>> m = parallelize_module(m, PairwiseParallel())
        >>>

    .. warning::
        ``PairwiseParallel`` comes with constraints for now. If you need finer
        granularity, you need to pass in a dict of module FQN and parallel style instead.
    '''
