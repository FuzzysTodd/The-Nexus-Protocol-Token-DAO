from _typeshed import Incomplete
from torch._ops import OpOverload as OpOverload
from torch.distributed._tensor.op_schema import OpSchema as OpSchema, OutputSharding as OutputSharding
from torch.utils._pytree import tree_map as tree_map
from typing import Callable, Dict, Tuple

def unwrap_schema(e: object) -> object: ...

class ShardingPropagator:
    op_to_rules: Incomplete
    def __init__(self) -> None: ...
    def register_sharding_prop_rule(self, op_overload: OpOverload, rule_func: Callable[[OpSchema], OutputSharding]):
        """
        Register a sharding propagation rule for an operator.
        """
    def prepare_op_schema(self, op_call: OpOverload, args: Tuple[object, ...], kwargs: Dict[str, object]) -> OpSchema:
        """
        This unwrap the args/kwargs DTensor to DTensorSpec and pack them
        into an OpSchema for sharding propagation usage.
        """
    def propagate_op_sharding(self, op_overload: OpOverload, op_schema: OpSchema) -> OutputSharding:
        """
        Propagate the sharding for an operator given the op_schema.
        """

class _CachingPropagator(ShardingPropagator):
    """
    A sharding propagator that caches the propagation results.
    This is currently experimental for Tensor Parallel usage.
    """
    op_to_rules: Incomplete
    cached_prop_results: Incomplete
    def __init__(self, op_to_rules: Incomplete | None = None) -> None: ...
    def propagate_op_sharding(self, op_overload: OpOverload, op_schema: OpSchema) -> OutputSharding:
        """
        Propagate the sharding for an operator given the op_schema.
        Cache the propagation results to avoid running propagation again.
        """
