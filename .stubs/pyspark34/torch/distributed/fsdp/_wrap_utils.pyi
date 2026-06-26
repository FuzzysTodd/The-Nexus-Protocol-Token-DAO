import torch
import torch.nn as nn
from typing import List, NamedTuple

class FullyShardedModuleState(NamedTuple):
    """
    Module state for ``_get_fully_sharded_module_to_states()``, representing
    a logical grouping (e.g. parameters to be flattened together).
    """
    params: List[nn.Parameter]
    buffers: List[torch.Tensor]
