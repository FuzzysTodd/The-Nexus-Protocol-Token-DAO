from _typeshed import Incomplete
from tensorflow.python.client import device_lib as device_lib
from tensorflow.python.distribute import collective_util as collective_util, cross_device_utils as cross_device_utils, device_util as device_util, distribute_utils as distribute_utils, ps_values as ps_values, reduce_util as reduce_util, tpu_values as tpu_values, values_util as values_util
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import indexed_slices as indexed_slices, kernels as kernels, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import NamedTuple

def check_destinations(destinations):
    """Checks whether `destinations` is not empty.

  Args:
    destinations: a `DistributedValues`, variable, or string object.

  Returns:
    Boolean which is True if `destinations` is not empty.
  """
def validate_destinations(destinations) -> None:
    """Validates the `destination` is one of expected types."""
def reduce_non_distributed_value(reduce_op, value, destinations, num_replicas_in_graph, canonicalize_devices: bool = True):
    """Reduce a non-DistributedValue `value` to `destinations`."""
def get_devices_from(destinations, canonicalize_devices: bool = True): ...
def simple_broadcast(value, destinations, always_mirrored: bool = False, canonicalize_devices: bool = True):
    """Broadcast `value` to `destinations` using simple copies."""

class CrossDeviceOps:
    """Base class for cross-device reduction and broadcasting algorithms.

  The main purpose of this class is to be passed to
  `tf.distribute.MirroredStrategy` in order to choose among different cross
  device communication implementations. Prefer using the methods of
  `tf.distribute.Strategy` instead of the ones of this class.

  Implementations:
  * `tf.distribute.ReductionToOneDevice`
  * `tf.distribute.NcclAllReduce`
  * `tf.distribute.HierarchicalCopyAllReduce`
  """
    def __init__(self) -> None: ...
    def reduce(self, reduce_op, per_replica_value, destinations, options: Incomplete | None = None):
        """Reduce `per_replica_value` to `destinations`.

    See `tf.distribute.StrategyExtended.reduce_to`. This can only be called in
    the cross-replica context.

    Args:
      reduce_op: a `tf.distribute.ReduceOp` specifying how values should be
        combined.
      per_replica_value: a `tf.distribute.DistributedValues`, or a `tf.Tensor`
        like object.
      destinations: a `tf.distribute.DistributedValues`, a `tf.Variable`, a
        `tf.Tensor` alike object, or a device string. It specifies the devices
        to reduce to. To perform an all-reduce, pass the same to `value` and
        `destinations`. Note that if it's a `tf.Variable`, the value is reduced
        to the devices of that variable, and this method doesn't update the
        variable.
      options: a `tf.distribute.experimental.CommunicationOptions`. See
        `tf.distribute.experimental.CommunicationOptions` for details.

    Returns:
      A `tf.Tensor` or `tf.distribute.DistributedValues`.

    Raises:
      ValueError: if per_replica_value can't be converted to a
        `tf.distribute.DistributedValues` or if destinations is not a string,
        `tf.Variable` or `tf.distribute.DistributedValues`.
    """
    def batch_reduce(self, reduce_op, value_destination_pairs, options: Incomplete | None = None):
        """Reduce values to destinations in batches.

    See `tf.distribute.StrategyExtended.batch_reduce_to`. This can only be
    called in the cross-replica context.

    Args:
      reduce_op: a `tf.distribute.ReduceOp` specifying how values should be
        combined.
      value_destination_pairs: a sequence of (value, destinations) pairs. See
        `tf.distribute.CrossDeviceOps.reduce` for descriptions.
      options: a `tf.distribute.experimental.CommunicationOptions`. See
        `tf.distribute.experimental.CommunicationOptions` for details.

    Returns:
      A list of `tf.Tensor` or `tf.distribute.DistributedValues`, one per pair
      in `value_destination_pairs`.

    Raises:
      ValueError: if `value_destination_pairs` is not an iterable of
        tuples of `tf.distribute.DistributedValues` and destinations.
    """
    def broadcast(self, tensor, destinations):
        """Broadcast `tensor` to `destinations`.

    This can only be called in the cross-replica context.

    Args:
      tensor: a `tf.Tensor` like object. The value to broadcast.
      destinations: a `tf.distribute.DistributedValues`, a `tf.Variable`, a
        `tf.Tensor` alike object, or a device string. It specifies the devices
        to broadcast to. Note that if it's a `tf.Variable`, the value is
        broadcasted to the devices of that variable, this method doesn't update
        the variable.

    Returns:
      A `tf.Tensor` or `tf.distribute.DistributedValues`.
    """
    def reduce_implementation(self, reduce_op, per_replica_value, destinations, options) -> None:
        """Implementation of `reduce`.

    Overriding this method is useful for subclass implementers.

    Args:
      reduce_op: a `tf.distribute.ReduceOp` specifying how values should be
        combined.
      per_replica_value: a `tf.distribute.DistributedValues`, or a `tf.Tensor`
        like object.
      destinations: a `tf.distribute.DistributedValues`, a `tf.Variable`, a
        `tf.Tensor` alike object, or a device string. It specifies the devices
        to reduce to. To perform an all-reduce, pass the same to `value` and
        `destinations`. Note that if it's a `tf.Variable`, the value is reduced
        to the devices of that variable, this method doesn't update the
        variable.
      options: a `tf.distribute.experimental.CommunicationOptions`. See
        `tf.distribute.experimental.CommunicationOptions` for details.

    Returns:
      A `tf.Tensor` or `tf.distribute.DistributedValues`.

    Raises:
      ValueError: if per_replica_value can't be converted to a
        `tf.distribute.DistributedValues` or if destinations is not a string,
        `tf.Variable` or `tf.distribute.DistributedValues`.
    """
    def batch_reduce_implementation(self, reduce_op, value_destination_pairs, options) -> None:
        """Implementation of `batch_reduce`.

    Overriding this method is useful for subclass implementers.

    Args:
      reduce_op: a `tf.distribute.ReduceOp` specifying how values should be
        combined.
      value_destination_pairs: a sequence of (value, destinations) pairs. See
        `reduce` for descriptions.
      options: a `tf.distribute.experimental.CommunicationOptions`. See
        `tf.distribute.experimental.CommunicationOptions` for details.

    Returns:
      A list of `tf.Tensor` or `tf.distribute.DistributedValues`, one per pair
      in `value_destination_pairs`.

    Raises:
      ValueError: if `value_destination_pairs` is not an iterable of
        tuples of `tf.distribute.DistributedValues` and destinations.
    """
    def broadcast_implementation(self, tensor, destinations):
        """Implementation of `broadcast`.

    Args:
      tensor: a `tf.Tensor` like object. The value to broadcast.
      destinations: a `tf.distribute.DistributedValues`, a `tf.Variable`, a
        `tf.Tensor` alike object, or a device string. It specifies the devices
        to broadcast to.
        `destinations`. Note that if it's a `tf.Variable`, the value is
        broadcasted to the devices of that variable, this method doesn't update
        the variable.

    Returns:
      A `tf.Tensor` or `tf.distribute.DistributedValues`.
    """

class ReductionToOneDevice(CrossDeviceOps):
    """A CrossDeviceOps implementation that copies values to one device to reduce.

  This implementation always copies values to one device to reduce them, then
  broadcast reduced values to the destinations. It doesn't support efficient
  batching.

  Here is how you can use `ReductionToOneDevice` in
  `tf.distribute.MirroredStrategy`:

  ```
    strategy = tf.distribute.MirroredStrategy(
      cross_device_ops=tf.distribute.ReductionToOneDevice())
  ```
  """
    reduce_to_device: Incomplete
    accumulation_fn: Incomplete
    def __init__(self, reduce_to_device: Incomplete | None = None, accumulation_fn: Incomplete | None = None) -> None:
        """Initializes with a device to reduce to and a way to accumulate.

    Args:
      reduce_to_device: the intermediate device to reduce to. If None, reduce
        to the first device in `destinations` of the `reduce` method.
      accumulation_fn: a function that does accumulation.  If None,
        `tf.math.add_n` is used.
    """
    def reduce_implementation(self, reduce_op, per_replica_value, destinations, options): ...
    def batch_reduce_implementation(self, reduce_op, value_destination_pairs, options): ...

class _ConcatAndSplitPacker:
    """Concatenate and split tensors for reduction."""
    num_packs: Incomplete
    def __init__(self, num_packs: int = 1) -> None:
        """Initialize the _ConcatAndSplitPacker object.

    Args:
      num_packs: specifies the number of split packs that will be
        formed.

    Raises:
      ValueError: if num_packs is not greater than 0.
    """
    grouped_grads_and_vars: Incomplete
    all_device_shapes: Incomplete
    all_device_sizes: Incomplete
    def pack(self, grouped_grads_and_vars):
        """Pack tensors."""
    def unpack(self, summed_device_grad_packs):
        """Reverse the pack."""

class AllReduceCrossDeviceOps(CrossDeviceOps):
    """All-reduce implementation of CrossDeviceOps.

  It performs all-reduce when applicable using NCCL or hierarchical copy. For
  the batch API, tensors will be repacked or aggregated for more efficient
  cross-device transportation.

  For reduces that are not all-reduce, it falls back to
  `tf.distribute.ReductionToOneDevice`.
  """
    def __init__(self, all_reduce_alg: str = 'nccl', num_packs: int = 1) -> None:
        '''Initializes the object.

    Args:
      all_reduce_alg: the all-reduce algorithm to use, currently only "nccl" or
        "hierarchical_copy" are supported.
      num_packs: a non-negative integer. The number of packs to split values
        into. If zero, no packing will be done.
    '''
    def reduce_implementation(self, reduce_op, per_replica_value, destinations, options): ...
    def batch_reduce_implementation(self, reduce_op, value_destination_pairs, options): ...
AllReduceCrossTowerOps = AllReduceCrossDeviceOps

class AllReduceSpecTuple(NamedTuple):
    alg: Incomplete
    shards: Incomplete
    limit: Incomplete

class NcclAllReduce(AllReduceCrossDeviceOps):
    """NCCL all-reduce implementation of CrossDeviceOps.

  It uses Nvidia NCCL for all-reduce. For the batch API, tensors will be
  repacked or aggregated for more efficient cross-device transportation.

  For reduces that are not all-reduce, it falls back to
  `tf.distribute.ReductionToOneDevice`.

  Here is how you can use `NcclAllReduce` in `tf.distribute.MirroredStrategy`:


  ```
    strategy = tf.distribute.MirroredStrategy(
      cross_device_ops=tf.distribute.NcclAllReduce())
  ```
  """
    def __init__(self, num_packs: int = 1) -> None:
        """Initializes the object.

    Args:
      num_packs: a non-negative integer. The number of packs to split values
        into. If zero, no packing will be done.

    Raises:
      ValueError: if `num_packs` is negative.
    """

class HierarchicalCopyAllReduce(AllReduceCrossDeviceOps):
    """Hierarchical copy all-reduce implementation of CrossDeviceOps.

  It reduces to one GPU along edges in some hierarchy and broadcasts back to
  each GPU along the same path. For the batch API, tensors will be repacked or
  aggregated for more efficient cross-device transportation.

  This is a reduction created for Nvidia DGX-1 which assumes GPUs connects like
  that on DGX-1 machine. If you have different GPU inter-connections, it is
  likely that it would be slower than `tf.distribute.ReductionToOneDevice`.

  For reduces that are not all-reduce, it falls back to
  `tf.distribute.ReductionToOneDevice`.

  Here is how you can use `HierarchicalCopyAllReduce` in
  `tf.distribute.MirroredStrategy`:

  ```
    strategy = tf.distribute.MirroredStrategy(
      cross_device_ops=tf.distribute.HierarchicalCopyAllReduce())
  ```
  """
    def __init__(self, num_packs: int = 1) -> None:
        """Initializes the object.

    Args:
      num_packs: a non-negative integer. The number of packs to split values
        into. If zero, no packing will be done.

    Raises:
      ValueError if `num_packs` is negative.
    """
CollectiveCommunication = collective_util.CommunicationImplementation
CommunicationImplementation = collective_util.CommunicationImplementation

class CollectiveAllReduce(CrossDeviceOps):
    """All-reduce cross device ops using collective ops.

  In the between-graph replicated training, it will still do all-reduces across
  all workers and then put results on the right destinations.
  """
    def __init__(self, devices, group_size, options, collective_keys: Incomplete | None = None, canonicalize_devices: bool = True) -> None:
        """Initializes the object.

    Args:
      devices: a list of device strings to run collectives on.
      group_size: the global group size. For between-graph replicated training
        it's the total number of devices across all workers.
      options: a `tf.distribute.experimental.CommunicationOptions`.
      collective_keys: an optional CollectiveKey object.
      canonicalize_devices: Whether to canonicalize devices for workers or not.
    """
    def reduce_implementation(self, reduce_op, per_replica_value, destinations, options): ...
    def batch_reduce_implementation(self, reduce_op, value_destination_pairs, options): ...
    def __deepcopy__(self, memo): ...

def select_cross_device_ops(devices, session_config: Incomplete | None = None):
    """Find the best `CrossDeviceOps` locally given a `tf.compat.v1.ConfigProto`.

  Args:
    devices: a list of devices passed to `tf.distribute.Strategy`.
    session_config: a `tf.compat.v1.ConfigProto` or `None`. If `None`, it will
      make decision based on all logical devices.

  Returns:
    A subclass of `CrossDeviceOps`.
  """
