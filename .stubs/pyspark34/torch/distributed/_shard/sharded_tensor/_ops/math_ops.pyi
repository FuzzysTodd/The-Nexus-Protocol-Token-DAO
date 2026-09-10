from _typeshed import Incomplete
from torch import Tensor as Tensor
from torch.distributed._shard._utils import narrow_tensor as narrow_tensor
from torch.distributed._shard.replicated_tensor import ReplicatedTensor as ReplicatedTensor
from torch.distributed._shard.sharded_tensor import ShardedTensor as ShardedTensor

def binary_math_op_impl(op, types, args=(), kwargs: Incomplete | None = None, pg: Incomplete | None = None):
    """
    Handles ``__torch_function__`` dispatch for the binary math ops
    such as `torch.add`, `torch.mul`, `torch.div`, etc.
    This method computes on ShardedTensor, or ShardedTensor op ReplicatedTensor
    """
def register_math_op(op): ...

binary_ops: Incomplete
