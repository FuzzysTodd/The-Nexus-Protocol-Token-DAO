from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_boosted_trees_ops as gen_boosted_trees_ops, resources as resources
from tensorflow.python.ops.gen_boosted_trees_ops import boosted_trees_aggregate_stats as boosted_trees_aggregate_stats, boosted_trees_bucketize as boosted_trees_bucketize, boosted_trees_sparse_aggregate_stats as boosted_trees_sparse_aggregate_stats
from tensorflow.python.training import saver as saver

class PruningMode:
    """Class for working with Pruning modes."""
    NO_PRUNING: Incomplete
    PRE_PRUNING: Incomplete
    POST_PRUNING: Incomplete
    @classmethod
    def from_str(cls, mode): ...

class QuantileAccumulatorSaveable(saver.BaseSaverBuilder.SaveableObject):
    """SaveableObject implementation for QuantileAccumulator."""
    resource_handle: Incomplete
    def __init__(self, resource_handle, create_op, num_streams, name) -> None: ...
    def restore(self, restored_tensors, unused_tensor_shapes): ...

class QuantileAccumulator:
    """SaveableObject implementation for QuantileAccumulator.

     The bucket boundaries are serialized and deserialized from checkpointing.
  """
    resource_handle: Incomplete
    def __init__(self, epsilon, num_streams, num_quantiles, name: Incomplete | None = None, max_elements: Incomplete | None = None) -> None: ...
    @property
    def initializer(self): ...
    def is_initialized(self): ...
    def add_summaries(self, float_columns, example_weights): ...
    def flush(self): ...
    def get_bucket_boundaries(self): ...

class _TreeEnsembleSavable(saver.BaseSaverBuilder.SaveableObject):
    """SaveableObject implementation for TreeEnsemble."""
    resource_handle: Incomplete
    def __init__(self, resource_handle, create_op, name) -> None:
        """Creates a _TreeEnsembleSavable object.

    Args:
      resource_handle: handle to the decision tree ensemble variable.
      create_op: the op to initialize the variable.
      name: the name to save the tree ensemble variable under.
    """
    def restore(self, restored_tensors, unused_restored_shapes):
        """Restores the associated tree ensemble from 'restored_tensors'.

    Args:
      restored_tensors: the tensors that were loaded from a checkpoint.
      unused_restored_shapes: the shapes this object should conform to after
        restore. Not meaningful for trees.

    Returns:
      The operation that restores the state of the tree ensemble variable.
    """

class TreeEnsemble:
    """Creates TreeEnsemble resource."""
    resource_handle: Incomplete
    def __init__(self, name, stamp_token: int = 0, is_local: bool = False, serialized_proto: str = '') -> None: ...
    @property
    def initializer(self): ...
    def is_initialized(self): ...
    def get_stamp_token(self):
        """Returns the current stamp token of the resource."""
    def get_states(self):
        """Returns states of the tree ensemble.

    Returns:
      stamp_token, num_trees, num_finalized_trees, num_attempted_layers and
      range of the nodes in the latest layer.
    """
    def serialize(self):
        """Serializes the ensemble into proto and returns the serialized proto.

    Returns:
      stamp_token: int64 scalar Tensor to denote the stamp of the resource.
      serialized_proto: string scalar Tensor of the serialized proto.
    """
    def deserialize(self, stamp_token, serialized_proto):
        """Deserialize the input proto and resets the ensemble from it.

    Args:
      stamp_token: int64 scalar Tensor to denote the stamp of the resource.
      serialized_proto: string scalar Tensor of the serialized proto.

    Returns:
      Operation (for dependencies).
    """
