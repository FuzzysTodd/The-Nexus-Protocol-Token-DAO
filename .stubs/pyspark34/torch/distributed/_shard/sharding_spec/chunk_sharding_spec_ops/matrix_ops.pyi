from torch.distributed._shard.sharded_tensor import ShardedTensor as ShardedTensor
from torch.distributed._shard.sharding_spec._internals import get_chunk_sharding_params as get_chunk_sharding_params
from torch.distributed.nn.functional import all_reduce as all_reduce

def transpose_same_dim(*args, **kwargs):
    """
    When the dim0 and dim1 of transpose are the same, return the original ShardedTensor.

    Args: same as ``torch.Tensor.transpose``.

    Return (bool): Whether to return early or not.
    """
def sharded_transpose_check(*args, **kwargs) -> None:
    """
    Perform extra checks for the sharded_transpose op such as the input needs to
    be at least 2 and the sharding spec needs to be a ChunkShardingSpec.

    Args: same as ``torch.Tensor.type_as``.

    Return: None
    """
def sharded_transpose(args, kwargs, pg):
    """
    Handles ``__torch_function__`` dispatch for the ``torch.Tensor.transpose`` op.

    Returns a new sharded tensor with the given dimensions transposed.
    During the transpose, we keep the original shading dim, if the sharding
    dim is not neither dim0 nor dim1. Otherwise, we will swap the sharding
    dim with the other input of transpose.

    Args: (same as ``torch.Tensor.transpose``.)
        dim0 (Int): the first dimension to be transposed.
        dim1 (Int): the second dimension to be transposed.

    Returns:
        new_local_shards (List[Shard]): Local shards for the new sharded tensor.
        st_meta (ShardedTensorMetadata): Metadata of the new sharded tensor.
    """
def sharded_masked_fill_check(*args, **kwargs) -> None:
    """
    Perform extra checks for the ``torch.Tensor.masked_fill`` op.
    Ensure the mask size is broadcastable with the size of
    the sharded tensor.

    Args: same as ``torch.Tensor.masked_fill``.

    Return: None
    """
def sharded_masked_fill(args, kwargs, pg):
    """
    Handles ``__torch_function__`` dispatch for the ``torch.Tensor.masked_fill`` op.
    We first narrow down the mask to the size of local tensor if the mask
    contains the sharding dim and then apply the mask to the local tensor.

    Args: same as ``torch.Tensor.masked_fill``.

    Return:
        local_tensor (Tensor): New local tensor to build the sharded tensor.
        sharding_spec (:class:`torch.distributed._shard.sharding_spec.ShardingSpec`):
            sharding spec of the new sharded tensor.
        new_st_size (torch.Size): Size of the new sharded tensor.
    """
def sharded_view_check(*args, **kwargs) -> None:
    """
    Perform extra checks for the ``torch.Tensor.view`` op.

    Args: same as ``torch.Tensor.view``.

    Return: None
    """
def sharded_view(args, kwargs, pg):
    """
    Handles ``__torch_function__`` dispatch for the ``torch.Tensor.view`` op.
    For now we always keep the sharding dim after view. For example, if
    a sharded tensor with size [16, 5] and sharded by 0. If we now view
    it as [4, 2, 2, 5], it will still be sharded by dim 0.

    Args: same as ``torch.Tensor.view``.

    Return:
        local_tensor (Tensor): New local tensor to build the sharded tensor.
        sharding_spec (:class:`torch.distributed._shard.sharding_spec.ShardingSpec`):
            sharding spec of the new sharded tensor.
        new_st_size (torch.Size): Size of the new sharded tensor.
    """
def sharded_bmm_check(*args, **kwargs) -> None:
    """
    Perform extra checks for the sharded_bmm op, for example, st2 needs to
    be a sharded tensor and both tensors need to sharded by dim 0, etc.

    Args: same as ``torch.bmm``.

    Return: None
    """
def sharded_bmm(args, kwargs, pg):
    """
    Handles ``__torch_function__`` dispatch for the sharded_bmm op.

    Warning: For now we only supports the case when both tensors are sharded
             by dim 0 so that no local communication.

    Args: same as ``torch.bmm``.

    Return:
        local_tensor (Tensor): New local tensor to build the sharded tensor.
        sharding_spec (:class:`torch.distributed._shard.sharding_spec.ShardingSpec`):
            sharding spec of the new sharded tensor.
        new_st_size (torch.Size): Size of the new sharded tensor.
    """
def sharded_layer_norm_check(*args, **kwargs) -> None:
    """
    Perform extra checks for the ``nn.LayerNorm`` op.
    Ensure the normalized shape is compatible with
    the size of the sharded tensor.

    Args: same as ``torch.nn.LayerNorm``.

    Return: None
    """
def sharded_layer_norm(args, kwargs, pg):
    """
    Handles ``__torch_function__`` dispatch for the ``torch.nn.LayerNorm`` op.
    We gather all shards from local shards and perform a global normalization.
    We then scatter the result back to each rank.

    Args: same as ``torch.nn.LayerNorm``.

    Return:
        local_tensor (Tensor): New local tensor to build the sharded tensor.
        sharding_spec (:class:`torch.distributed._shard.sharding_spec.ShardingSpec`):
            sharding spec of the new sharded tensor.
        new_st_size (torch.Size): Size of the new sharded tensor.
    """
