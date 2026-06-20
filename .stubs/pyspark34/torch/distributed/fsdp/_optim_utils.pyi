import torch
import torch.distributed as dist
from dataclasses import dataclass
from torch.distributed._shard.sharded_tensor import ShardedTensor as ShardedTensor
from torch.distributed.fsdp._common_utils import _FSDPState, clean_tensor_name as clean_tensor_name
from torch.distributed.fsdp.api import ShardingStrategy as ShardingStrategy
from torch.distributed.fsdp.flat_param import FlatParamHandle as FlatParamHandle, FlatParameter as FlatParameter
from typing import Any, Dict, Iterator, List, NamedTuple, Tuple

@dataclass
class FSDPParamInfo:
    state: _FSDPState
    flat_param: FlatParameter
    param_indices: Dict[str, int]
    def __init__(self, state, flat_param, param_indices) -> None: ...

def sorted_items(dictionary: Dict[str, Any]) -> Iterator[Tuple[str, Any]]: ...

class _ConsolidatedOptimState:
    """
    This holds the consolidated optimizer state on the target rank. Positive-
    dimension tensor state is communicated across ranks, while zero-dimension
    tensor state and non-tensor state is taken directly from the target rank.

    PyTorch version 1.12 moved to using zero-dimension tensors for scalar
    values, but user implemented optimizers may still use float (i.e. a
    non-tensor). Thus, we support both and handle them identically.

    Attributes:
        tensor_state (Dict[str, torch.Tensor]): Mapping from positive-dimension
            tensor state name to the unsharded flattened tensor representing
            the state.
        zero_dim_tensor_state (Dict[str, torch.Tensor]): Mapping from zero-
            dimension tensor state name to its value.
        non_tensor_state (Dict[str, Any]): Mapping from non-tensor state
            name to its value.
    """
    tensor_state: Dict[str, torch.Tensor]
    zero_dim_tensor_state: Dict[str, torch.Tensor]
    non_tensor_state: Dict[str, Any]

class _PosDimTensorInfo(NamedTuple):
    """
    Meatadata for positive-dimension tensors used internally for
    :meth:`scatter_full_optim_state_dict`.

    Attributes:
        shape (torch.Size): Sharded tensor shape (which is equal to the
            unsharded tensor shape if the tensor is optimizer state for a
            non-FSDP parameter and is hence not sharded).
        dtype (torch.dtype): Data type of the tensor.
    """
    shape: torch.Size
    dtype: torch.dtype

class _OptimStateKey(NamedTuple):
    """
    This represents an optimizer state key that may be used commonly across
    ranks. It is based on the unflattened parameter names rather than parameter
    IDs to make it indepenendent of each rank's own optimizer construction.
    """
    unflat_param_names: Tuple[str, ...]
    is_fsdp_managed: bool

@dataclass
class StateInfo:
    tensors: Dict[str, _PosDimTensorInfo]
    scalar_tensors: Dict[str, torch.Tensor]
    non_tensors: Dict[str, Any]
    def __init__(self, tensors, scalar_tensors, non_tensors) -> None: ...

@dataclass
class AllGatherInfo:
    tensors: List[torch.Tensor]
    numels: List[int]
    work: dist.Work | None
    def __init__(self, tensors, numels, work) -> None: ...
