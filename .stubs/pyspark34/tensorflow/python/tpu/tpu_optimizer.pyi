from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops.losses import losses as losses
from tensorflow.python.tpu import tpu_function as tpu_function
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from tensorflow.python.training import optimizer as optimizer
from tensorflow.python.util.tf_export import tf_export as tf_export

class CrossShardOptimizer(optimizer.Optimizer):
    """An optimizer that averages gradients across TPU shards."""
    def __init__(self, opt, reduction=..., name: str = 'CrossShardOptimizer', group_assignment: Incomplete | None = None) -> None:
        '''Construct a new cross-shard optimizer.

    Args:
      opt: An existing `Optimizer` to encapsulate.
      reduction: The reduction to apply to the shard losses.
      name: Optional name prefix for the operations created when applying
        gradients. Defaults to "CrossShardOptimizer".
      group_assignment: Optional 2d int32 lists with shape
        [num_groups, num_replicas_per_group] which describles how to apply
        optimizer to subgroups.

    Raises:
      ValueError: If reduction is not a valid cross-shard reduction.
    '''
    def compute_gradients(self, loss, var_list: Incomplete | None = None, **kwargs):
        '''Compute gradients of "loss" for the variables in "var_list".

    This simply wraps `compute_gradients()` from the real optimizer. The
    gradients will be aggregated in `apply_gradients()` so that user can
    modify the gradients like clipping with per replica global norm if needed.
    The global norm with aggregated gradients can be bad as one replica\'s huge
    gradients can hurt the gradients from other replicas.

    When the CrossShardOptimizer is constructed with
    `reduction == losses.Reduction.MEAN` (default), this function scales the
    loss by `1.0 / num_shards` before computing the gradients. Assuming the
    optimizer uses the default implementation of `compute_gradients()`, the
    gradients of the scaled loss are scaled by `1.0 / num_shards` compared to
    the gradients of the original loss. This scaling factor is important because
    `apply_gradients()` sums gradients across shards, rather than averaging
    them. However, the scaling factor must be taken into account when clipping
    the norm of the gradients or performing other postprocessing.

    Args:
      loss: A Tensor containing the value to minimize.
      var_list: Optional list or tuple of `tf.Variable` to update to minimize
        `loss`.  Defaults to the list of variables collected in the graph
        under the key `GraphKey.TRAINABLE_VARIABLES`.
      **kwargs: Keyword arguments for compute_gradients().

    Returns:
      A list of (gradient, variable) pairs.

    Raises:
      ValueError: If not within a tpu_shard_context or group_assignment is
        invalid.
    '''
    def apply_gradients(self, grads_and_vars, global_step: Incomplete | None = None, name: Incomplete | None = None):
        """Apply gradients to variables.

    Calls tpu_ops.cross_replica_sum() to sum gradient contributions across
    replicas, and then applies the real optimizer.

    Args:
      grads_and_vars: List of (gradient, variable) pairs as returned by
        compute_gradients().
      global_step: Optional Variable to increment by one after the
        variables have been updated.
      name: Optional name for the returned operation.  Default to the
        name passed to the Optimizer constructor.

    Returns:
      An `Operation` that applies the gradients. If `global_step` was not None,
      that operation also increments `global_step`.

    Raises:
      ValueError: If the grads_and_vars is malformed.
    """
    def get_slot(self, *args, **kwargs):
        '''Return a slot named "name" created for "var" by the Optimizer.

    This simply wraps the get_slot() from the actual optimizer.

    Args:
      *args: Arguments for get_slot().
      **kwargs: Keyword arguments for get_slot().

    Returns:
      The `Variable` for the slot if it was created, `None` otherwise.
    '''
    def get_slot_names(self, *args, **kwargs):
        """Return a list of the names of slots created by the `Optimizer`.

    This simply wraps the get_slot_names() from the actual optimizer.

    Args:
      *args: Arguments for get_slot().
      **kwargs: Keyword arguments for get_slot().

    Returns:
      A list of strings.
    """
    def variables(self):
        """Forwarding the variables from the underlying optimizer."""
