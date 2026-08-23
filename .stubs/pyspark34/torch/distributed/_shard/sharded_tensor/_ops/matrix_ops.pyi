from torch.distributed._shard.sharded_tensor import Shard as Shard, ShardedTensor as ShardedTensor

def sharded_type_as_check(*args, **kwargs) -> None:
    """
    Perform extra checks for the sharded_type_as op such as the input needs to
    be either a Tensor or ShardedTensor.

    Args: same as ``torch.Tensor.type_as``.

    Return: None
    """
def same_dtype(*args, **kwargs):
    """
    When the dtype is the same, return the original ShardedTensor.

    Args: same as ``torch.Tensor.type_as``.

    Return (bool): Whether to return early or not.
    """
def sharded_type_as(args, kwargs, pg):
    """
    Handles ``__torch_function__`` dispatch for the ``torch.Tensor.type_as`` op.

    Args: same as ``torch.Tensor.type_as``.

    Return:
        new_local_shards (List[Shard]): Local shards for the new sharded tensor.
        st_meta (ShardedTensorMetadata): Metadata of the new sharded tensor.
    """
