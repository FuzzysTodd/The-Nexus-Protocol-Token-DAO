from torch.distributed.checkpoint.planner import SavePlan
from typing import List

__all__ = ['dedup_tensors']

def dedup_tensors(all_plans: List[SavePlan]) -> List[SavePlan]: ...
