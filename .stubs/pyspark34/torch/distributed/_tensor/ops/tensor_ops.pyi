from _typeshed import Incomplete
from torch.distributed._tensor.api import DTensorSpec as DTensorSpec, Placement as Placement, Replicate as Replicate, Shard as Shard
from torch.distributed._tensor.op_schema import OpSchema as OpSchema, OutputSharding as OutputSharding
from torch.distributed._tensor.ops.common_rules import einop_rule as einop_rule, pointwise_rule as pointwise_rule
from torch.distributed._tensor.ops.utils import normalize_dim as normalize_dim, register_prop_rule as register_prop_rule
from typing import Sequence

aten: Incomplete

def default_prop_rule(op_schema: OpSchema) -> OutputSharding: ...
def prop_create_like(op_schema: OpSchema) -> OutputSharding: ...
def no_shard_prop_rule(op_schema: OpSchema) -> OutputSharding: ...
def new_factory_rule(op_schema: OpSchema) -> OutputSharding: ...

default_prop_ops: Incomplete
create_like_ops: Incomplete
new_factory_ops: Incomplete

def prop_bucketize(op_schema: OpSchema) -> OutputSharding:
    """
    Point-wise on the first input (just propagate input sharding).
    Expect replicated for second input.
    """
def unshard_tensor_dim(placements: Sequence[Placement], dim: int) -> Sequence[Placement]:
    """Disallow the given tensor dimension to be sharded"""
def is_tensor_dim_sharded(spec: DTensorSpec, dim: int) -> bool:
    """Return True if tensor dim is sharded"""
def prop_slice(op_schema: OpSchema) -> OutputSharding:
    """NOTE: can be further optimized (right now it replicates before slicing on a sharded dimension)"""
def prop_slice_scatter(op_schema: OpSchema) -> OutputSharding: ...
def prop_index_select(op_schema: OpSchema) -> OutputSharding: ...
def prop_index(op_schema: OpSchema) -> OutputSharding:
    '''
    Expect replicated on the first input; _mostly_ pointwise on the second input.
    TODO: exception: when the dtype of second input is "bool", then a torch.nonzero needs to be triggered first.
    '''
def cat_rule(op_schema: OpSchema) -> OutputSharding: ...
def split_rule(op_schema: OpSchema) -> OutputSharding: ...
