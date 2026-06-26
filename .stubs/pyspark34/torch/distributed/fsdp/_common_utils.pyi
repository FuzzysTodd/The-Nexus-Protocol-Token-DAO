from .api import FullOptimStateDictConfig as FullOptimStateDictConfig, FullStateDictConfig as FullStateDictConfig, OptimStateDictConfig as OptimStateDictConfig, ShardingStrategy as ShardingStrategy, StateDictConfig as StateDictConfig, StateDictType as StateDictType
from _typeshed import Incomplete
from enum import Enum
from torch.distributed._composable_state import _State

FSDP_WRAPPED_MODULE: str
FSDP_PREFIX: Incomplete
FSDP_FLATTENED: str

class _FSDPState(_State):
    process_group: Incomplete
    rank: int
    world_size: int
    sharding_strategy: Incomplete
    training_state: Incomplete
    compute_device: Incomplete
    def __init__(self) -> None: ...

class TrainingState(Enum):
    """
    An enum that indicates the state of a ``FullyShardedDataParallel` instance.
    """
    IDLE: Incomplete
    FORWARD_BACKWARD: Incomplete
    SUMMON_FULL_PARAMS: Incomplete

class HandleTrainingState(Enum):
    """
    An enum that indicates the state of a ``FlatParamHandle`.
    """
    IDLE: Incomplete
    FORWARD: Incomplete
    BACKWARD_PRE: Incomplete
    BACKWARD_POST: Incomplete
    SUMMON_FULL_PARAMS: Incomplete

def clean_tensor_name(tensor_name: str) -> str:
    """
    Cleans the parameter or buffer name by removing any module wrapper
    prefixes.
    """
