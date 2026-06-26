from _typeshed import Incomplete
from tensorflow.python.framework import tensor_shape as tensor_shape

class ShardingPolicy:
    """An object use to hold the sharding policy for a Tensor."""
    def __init__(self) -> None: ...
    def freeze(self) -> None:
        """Prevents further modification to the sharding policy.

    Any values that have not been set when freeze is called are set to
    defaults. If the ShardingPolicy is already frozen, this is a NoOp.
    """
    @property
    def number_of_shards(self):
        """Returns the number of shards in the policy or None if unspecified."""
    def set_number_of_shards(self, number_of_shards) -> None:
        """Sets the number of shards for the current policy.

    If the policy has been frozen then number_of_shards must match the
    existing setting.

    Args:
      number_of_shards: The number of shards to use in the policy.

    Raises:
      ValueError: If the policy has been frozen and number_of_shards
        differs from the frozen value; or number_of_shards <= 0.
    """
    @property
    def number_of_partitions(self):
        """Returns the number of partitions of the policy or None if unspecified."""
    def set_number_of_partitions(self, number_of_partitions) -> None:
        """Sets the number of partitions for the current policy.

    If the policy has been frozen then shard_dimension must match the
    existing setting.

    Args:
      number_of_partitions: The number of partitions to use in the policy.

    Raises:
      ValueError: If the policy has been frozen and shard_dimension
        differs from the frozen value.
    """
    @property
    def shard_dimension(self):
        """Returns the shard dimension of the policy or None if unspecified."""
    def set_shard_dimension(self, shard_dimension) -> None:
        """Sets the shard dimension for the current policy.

    If the policy has been frozen then shard_dimension must match the
    existing setting.

    Args:
      shard_dimension: The shard dimension to use in the policy.

    Raises:
      ValueError: If the policy has been frozen and shard_dimension
        differs from the frozen value, or shard_dimension can't be
        interpreted as a Dimension.
    """
    def merge(self, other) -> None:
        """Merges the policy of another policy into the current policy.

    Args:
      other: The policy to merge into this one.

    Raises:
      ValueError: If this policy has been frozen and the merge conflicts with
      the frozen policy.
    """
    def get_unpartitioned_shape(self, shape):
        """Returns the shape of an unpartitioned Tensor.

    When given the shape of a 'sharded-size' Tensor, returns the shape
    of the full shape of its unpartitioned Tensor.

    Args:
      shape: The shape of the sharded Tensor.

    Returns:
      The shape of the unpartitioned version of the Tensor.

    Raises:
      ValueError: if shape has unknown sharded dimension
    """
    def get_sharded_shape(self, shape, shard_index: Incomplete | None = None):
        """Returns the shape of a shard of a full Tensor.

    When given the shape of a 'full-size' Tensor, returns the shape of
    the sub-Tensor after it has been sharded. Freezes the policy if it
    has not yet been frozen.

    Args:
      shape: The shape of the full-size Tensor to be sharded.
      shard_index: The index of the shard whose shape should be returned.
        shard_index can be None for sharding policies that use the same shape
        for every shard.

    Returns:
      The shape of the sharded version of the Tensor.

    Raises:
      ValueError: If shard_index is None when shards are of different
        shapes; or shard_index is not None and
        !(0<=shard_index<number_of_shards); or shape does not have at
        least self.shard_dimension+1 dimensions; or the value of
        shape's shard dimension is not a multiple of
        self.number_of_shards
    """
    def get_unsharded_shape(self, shapes):
        """Returns the shape of an unsharded Tensor given a list of shards.

    When given a list of shapes of shards, returns the shape of the
    unsharded Tensor that would generate the shards. Sets defaults for the
    policy if number_of_shards or shard_dimension is None.

    Args:
      shapes: The shapes of the Tensor shards to be combined.

    Returns:
      The shape of the unsharded version of the Tensor.

    Raises:
      ValueError: if shapes is not a list of length
        self.number_of_shards; or any element of shapes is not a valid
        shape consistent with the sharding policy; or the list of
        shapes is not a valid sharding of a full shape.
      TypeError: if an element of shapes is not convertible to a
        TensorShape
    """
