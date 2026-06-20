from _typeshed import Incomplete
from torch.distributed.algorithms._comm_hooks import default_hooks as default_hooks
from torch.distributed.fsdp._common_utils import TrainingState as TrainingState, clean_tensor_name as clean_tensor_name
from torch.distributed.fsdp.api import BackwardPrefetch as BackwardPrefetch, CPUOffload as CPUOffload, FullOptimStateDictConfig as FullOptimStateDictConfig, FullStateDictConfig as FullStateDictConfig, MixedPrecision as MixedPrecision, ShardingStrategy as ShardingStrategy, StateDictConfig as StateDictConfig, StateDictType as StateDictType
from torch.distributed.fsdp.flat_param import FlatParamHandle as FlatParamHandle, FlatParameter as FlatParameter, HandleShardingStrategy as HandleShardingStrategy
from torch.utils.hooks import RemovableHandle as RemovableHandle

PARAM_BROADCAST_BUCKET_SIZE: Incomplete
FSDP_SYNCED: str
HybridShardProcessGroupType: Incomplete
ProcessGroupType: Incomplete
SHARDING_STRATEGY_MAP: Incomplete
HYBRID_SHARDING_STRATEGIES: Incomplete
