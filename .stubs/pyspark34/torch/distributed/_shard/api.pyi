import torch
import torch.nn as nn
from .replicated_tensor import ReplicatedTensor as ReplicatedTensor
from .sharder import Sharder as Sharder
from .sharding_plan import ShardingPlan as ShardingPlan
from .sharding_spec import ChunkShardingSpec as ChunkShardingSpec, ShardingSpec as ShardingSpec
from _typeshed import Incomplete
from collections.abc import Generator
from torch.distributed import distributed_c10d as distributed_c10d
from torch.distributed._shard.sharded_tensor import ShardedTensor as ShardedTensor

def shard_parameter(module: torch.nn.Module, param_name: str, sharding_spec: ShardingSpec, src_rank: int = 0, process_group: Incomplete | None = None):
    """
    Given a :class:`torch.nn.Module`, a ``param_name`` for a parameter in that
    module, it shards that parameter according to the provided
    ``sharding_spec``. ``src_rank`` denotes the source rank which would be
    used as the ground truth of the data which would be scattered as shards
    across the rest of the ranks.

    This method replaces ``module.param_name`` with a
    :class:`torch.distributed._sharded_tensor.ShardedTensor`

    Args:
        module (:class:`torch.nn.Module`): Module whose parameter needs to be sharded.
        param_name (str): Name of the parameter of ``module`` that needs to be sharded.
        sharding_spec (:class:`torch.distributed._shard.sharding_spec.ShardingSpec`): The specification
            describing how to shard the Tensor.

    Keyword args:
        src_rank (int, optional): The source rank which is used as the ground truth of
            the data for the parameter that would be sharded and scattered
            across the rest of the ranks.
            Default: 0.
        process_group (ProcessGroup, optional): The process group to work on. If None,
            the default process group will be used.

    .. warning::
        Only :class:`torch.distributed._shard.sharding_spec.ChunkShardingSpec` is
        currently supported as the ``sharding_spec``.
    """
def load_with_process_group(process_group) -> Generator[Incomplete, None, None]:
    """
    Context manager to set the process group with which to load a ShardedTensor/ReplicatedTensor.
    """
def shard_module(module: nn.Module, plan: ShardingPlan, src_rank: int = 0, process_group: Incomplete | None = None):
    """
    Shards a given module according to the provided sharding `plan`. This method
    first shards all the parameters according to the given sharding `plan`. Then if
    `output_plan` and `return_local_tensor` are specified in the sharding `plan`, it
    will tag the output of modules according `output_plan`, convert the module's
    output back to data parallel according to `return_local_tensor`.

    Needs to be called on all ranks in an SPMD fashion.

    Args:
        module (:class:`torch.nn.Module`): The module to apply sharding to
        plan (:class:`torch.distributed._shard.sharding_plan.ShardingPlan`):
            The ShardingPlan which specified param name to ShardingSpec to apply to
            each parameter.

    Keyword args:
         src_rank (int, optional): The source rank which is used as the ground truth of
            the data for the module that would be sharded and scattered across the rest
            of the ranks.
            Default: 0.
        process_group (ProcessGroup, optional): The process group to work on. If None,
            the default process group will be used.
    """
