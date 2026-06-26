from torch.distributed._tensor.op_schema import OpSchema as OpSchema, OutputSharding as OutputSharding
from torch.distributed._tensor.ops.utils import prod as prod
from torch.distributed._tensor.placement_types import DTensorSpec as DTensorSpec
from typing import Dict, Sequence

def einop_rule(equation: str, op_schema: OpSchema, *, linearity: bool = False, enforce_sharding: Dict[str, int] | None = None) -> OutputSharding:
    """
    Propagate the sharding of inputs to output for ops whose data
    moves according to einsum notation. This is mostly borrowed
    from @zdevito's sharding simulator. Examples:
        mk,kn->mn - einsum
        ij,ij->ij - addition
        ij,j->ij - broadcasted addition
        ij->i - reduction
    Other ops could use this propagation algorithm when applied, note
    that einsum propagation only deal with list of specs (DTensor specs)
    as it only works on list of tensors!

    linearity in einop_rule means that the calling op `f` follows this rule:
        f(a + b) = f(a) + f(b)

    In this case we can propagate the partial sum, note that linearity in einop
    only applies to partial sum, not other operations like min/max (which are
    associative but not linear).
    """
def pointwise_rule(op_schema: OpSchema, linearity: bool = False) -> OutputSharding:
    """
    Propagate the sharding for pointwise operations. Examples:
        ij,ij->ij - addition/mul
        ij,j->ij - broadcasted addition
    """
def linear_pointwise_rule(op_schema: OpSchema) -> OutputSharding:
    """
    Linear pointwise operators can propagate pending reductions.
    For example, c = add(a, b); if a is pending sum, then c will be
    pending sum as well without any communication overhead.
    """
def reduction_rule(op_schema: OpSchema, *, dims: Sequence[int] | None = None, keep_dim: bool = False, reduction_linear: bool = False) -> OutputSharding:
    """
    Propagate the sharding for reduction operations. Examples:
        ij->i - sum on dim

    reduction_linear means that the reduction `f` follows this rule:
        f([f(a), f(b)]) = f([a, b])

    reduction linear should be super set of linearity.
    """
