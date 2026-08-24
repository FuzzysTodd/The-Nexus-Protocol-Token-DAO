import torch
from torch.distributed._tensor.op_schema import ArgsType as ArgsType, KwargsType as KwargsType, OutputSpecType as OutputSpecType
from torch.distributed._tensor.placement_types import DTensorSpec as DTensorSpec
from torch.distributed._tensor.redistribute import redistribute_dtensor as redistribute_dtensor
from torch.distributed._tensor.sharding_prop import ShardingPropagator as ShardingPropagator
from torch.utils._pytree import tree_flatten as tree_flatten, tree_unflatten as tree_unflatten
from typing import Callable, Dict, Tuple

def wrap(res: object, spec: OutputSpecType) -> object: ...
def pack_args_kwargs_with_local_tensor(args: ArgsType | KwargsType, args_schema: ArgsType | KwargsType, redistribute_with_schema: bool = False) -> ArgsType | KwargsType: ...
def operator_dispatch(op_call: torch._ops.OpOverload, args: Tuple[object, ...], kwargs: Dict[str, object], sharding_propagator: ShardingPropagator, custom_dispatch_ops: Dict[str, Callable[..., object]] | None = None) -> object: ...
