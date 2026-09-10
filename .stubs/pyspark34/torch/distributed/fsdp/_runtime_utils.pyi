from _typeshed import Incomplete
from torch.autograd import Variable as Variable
from torch.distributed.algorithms._comm_hooks import LOW_PRECISION_HOOKS as LOW_PRECISION_HOOKS, default_hooks as default_hooks
from torch.distributed.fsdp._common_utils import TrainingState as TrainingState
from torch.distributed.fsdp._init_utils import HYBRID_SHARDING_STRATEGIES as HYBRID_SHARDING_STRATEGIES
from torch.distributed.fsdp._utils import p_assert as p_assert
from torch.distributed.fsdp.api import BackwardPrefetch as BackwardPrefetch
from torch.distributed.fsdp.flat_param import FlatParamHandle as FlatParamHandle, FlatParameter as FlatParameter, HandleShardingStrategy as HandleShardingStrategy, HandleTrainingState as HandleTrainingState

RESHARD_AFTER_FORWARD_STRATEGIES: Incomplete
HOMOGENEOUS_ATTR_NAMES: Incomplete
