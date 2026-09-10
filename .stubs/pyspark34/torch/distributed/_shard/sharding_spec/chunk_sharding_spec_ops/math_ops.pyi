from _typeshed import Incomplete
from torch import Tensor as Tensor
from torch.distributed._shard.sharded_tensor import ShardedTensor as ShardedTensor
from torch.distributed._shard.sharded_tensor._ops.math_ops import binary_math_op_impl as binary_math_op_impl
from torch.distributed._shard.sharding_spec import ChunkShardingSpec as ChunkShardingSpec
from torch.distributed._shard.sharding_spec.api import custom_sharding_spec_op as custom_sharding_spec_op

def register_math_op(op): ...

binary_ops: Incomplete
