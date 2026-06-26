from _typeshed import Incomplete
from tensorflow.python.compiler.xla.experimental import xla_sharding as xla_sharding
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.tpu import tpu_name_util as tpu_name_util, tpu_sharding as tpu_sharding
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from tensorflow.python.util import nest as nest

def partition_or_replicate_on_host(tensor, dims):
    """Partitions or replicates the input tensor.

    The ops inside this function are placed on the host side.

  Args:
    tensor: The input tensor which will be partitioned or replicated.
    dims: A list of integer describes how to partition the input tensor.

  Returns:
    An iterator of `Tensor`s or a list of partitioned tensors.
  """
def tag_sharding_attribute_for_dequeued_tensors(dequeues, dims):
    """Tags appropriate XLA sharding attribute to the dequeued tensors.

  Args:
    dequeues: A list of dequeued tensors on TPU.
    dims: A list of integer describes how the tensor is partitioned.

  Returns:
    The same dequeues with appropriate xla_sharding attribute.
  """

class InfeedQueue:
    """A helper object to build a device infeed queue.

  The InfeedQueue builds the host-side and device-side Ops to enqueue and
  dequeue elements, respectively, and ensures that their types and
  shapes match.
  """
    def __init__(self, number_of_tuple_elements: Incomplete | None = None, tuple_types: Incomplete | None = None, tuple_shapes: Incomplete | None = None, shard_dimensions: Incomplete | None = None, number_of_partitions: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """Creates a new InfeedQueue with the given configuration.

    The configuration need not be fully specified at creation since it
    can be modified subsequently by methods that set the values
    explicitly or infer them from the shapes of inputs.

    Args:
      number_of_tuple_elements: the number of Tensors fed atomically through the
        queue, must be present unless it can be inferred from other arguments.
      tuple_types: if not None, a list of types of the elements of the queue.
      tuple_shapes: if not None, a list of shapes of the elements of the queue.
      shard_dimensions: if not None, a list of dimensions on which the
        elements of the queue should be sharded during automatic
        parallelization.
      number_of_partitions: if > 1, the infeed dequeue shape will contain
        the full shape that includes all partitions and add corresponding XLA
        annotation on the infeed dequeue op. In this case, the infeed is still
        data parallel that feeds per-core batch size to each core while the XLA
        computation may be partitioned. As XLA requires infeed dequeue shape to
        be per-replica shape, thus we need number_of_partitions here to
        calculate the per-replica unpartitioned shape.
      name: the name of the queue.

    Raises:
      ValueError: if number_of_tuple_elements <= 0; or
        number_of_tuple_arguments, tuple_types, tuple_shapes, and
        shard_dimensions are all None; or the length of tuple_types,
        tuple_shapes, or shard_dimensions is not equal to
        number_of_tuple_elements; or any element of shard_dimensions
        can't be converted to a Dimension.
      TypeError: if any element of tuple_types or tuple_shapes can't
        be converted to a dtype or TensorShape, respectively.
    """
    @property
    def number_of_tuple_elements(self):
        """Returns the number of InfeedQueue tuple elements."""
    @property
    def tuple_types(self):
        """Returns the types of the InfeedQueue tuple elements."""
    def set_tuple_types(self, tuple_types) -> None:
        """Sets the type of each element of the queue.

    tuple_types must be a list of length
    self.number_of_tuple_elements, and each element must be
    convertible to a dtype.

    Args:
      tuple_types: the types of each queue element.

    Raises:
      ValueError: if tuple_types is not of length
        self.number_of_tuple_elements.
      TypeError: if an element of tuple_types cannot be converted to a
        dtype.
    """
    @property
    def tuple_shapes(self):
        """Returns the shapes of the InfeedQueue tuple elements."""
    def set_tuple_shapes(self, tuple_shapes) -> None:
        """Sets the shape of each element of the queue.

    tuple_shapes must be a list of length
    self.number_of_tuple_elements, and each element must be
    convertible to a TensorShape.

    Args:
      tuple_shapes: the shapes of each queue element.

    Raises:
      ValueError: if tuple_shapes is not of length
        self.number_of_tuple_elements.
      TypeError: if an element of tuple_shapes cannot be converted to
        a TensorShape.
    """
    @property
    def sharding_policies(self):
        """Returns the sharding policies of the InfeedQueue tuple elements."""
    @property
    def shard_dimensions(self):
        """Gets the shard dimension of each tuple element.

    Returns:
      A list of length number_of_tuple_elements, where each list entry
      is the shard dimension of that tuple element or None if the
      shard dimension has not been set.
    """
    def set_shard_dimensions(self, shard_dimensions) -> None:
        """Sets the shard_dimension of each element of the queue.

    shard_dimensions must be a list of length
    self.number_of_tuple_elements, and each element must be
    convertible to a Dimension compatible with self.tuple_shapes.

    Args:
      shard_dimensions: the dimensions of each queue element.

    Raises:
      ValueError: if shard_dimensions is not of length
        self.number_of_tuple_elements; or an element of
        shard_dimensions cannot be converted to a Dimension; or an
        element of shard_dimensions is a Dimension that is out of
        range for the corresponding tuple element shape.
    """
    @property
    def number_of_shards(self):
        """Gets the number of shards to use for the InfeedQueue.

    Returns:
      Number of shards or None if the number of shards has not been set.
    """
    def set_number_of_shards(self, number_of_shards) -> None:
        """Sets the number of shards to use for the InfeedQueue.

    Args:
      number_of_shards: number of ways to shard the InfeedQueue.

    Raises:
      ValueError: if number_of_shards is not > 0; or the policies have
        been frozen and number_of_shards was already set to something
        else.
    """
    def set_configuration_from_input_tensors(self, input_tensors) -> None:
        """Sets the shapes and types of the queue tuple elements.

    input_tensors is a list of Tensors whose types and shapes are used
    to set the queue configuration.

    Args:
      input_tensors: list of Tensors of the same types and shapes as
        the desired queue Tuple.

    Raises:
      ValueError: if input_tensors is not a list of length
        self.number_of_tuple_elements
    """
    def set_configuration_from_sharded_input_tensors(self, input_tensors) -> None:
        """Sets the shapes and types of the queue tuple elements.

    input_tensors is a list of lists of Tensors whose types and shapes are used
    to set the queue configuration. The length of the outer list is the number
    of shards required, and each inner list is the tuple of Tensors to use to
    determine the types and shapes of the corresponding shard. This method
    depends on the shard dimension, and calling it freezes the shard policy.

    Args:
      input_tensors: list of lists of Tensors. The outer list length corresponds
        to the desired number of shards, and each inner list is the size
        and shape of the desired configuration of the corresponding shard.

    Raises:
      ValueError: if any inner list is not a list of length
        self.number_of_tuple_elements; or the inner lists do not combine to
        form a consistent unsharded shape.
      TypeError: if the types of the Tensors in the inner lists do not match.
    """
    def freeze(self) -> None:
        """Freezes the InfeedQueue so it can no longer be modified.

    The configuration is implicitly frozen before any host-side or
    device-side Ops are generated. The configuration cannot be frozen
    until the types and shapes of the tuple elements have been set.

    Raises:
      ValueError: if the types or shapes of the tuple elements have not been
      set.
    """
    def generate_dequeue_op(self, tpu_device: int = 0):
        """Generates the device-side Op to dequeue a tuple from the queue.

    Implicitly freezes the queue configuration if it is not already
    frozen, which will raise errors if the shapes and types have not
    been fully specified.

    Args:
      tpu_device: The TPU device ordinal where the infeed instruction should be
        placed. If None, no explicit placement will be performed, and it is up
        to the user to call this API from within a proper TPU device scope.
        The XLA code will fail if the TPU dequeue instruction is not bound to
        any device.

    Returns:
      A list of Outputs corresponding to a shard of infeed dequeued
      into XLA, suitable for use within a replicated block.

    Raises:
      ValueError: if the types or shapes of the tuple elements have not been
      set; or if a dequeue op has already been generated.
    """
    def generate_enqueue_ops(self, sharded_inputs, tpu_ordinal_function: Incomplete | None = None, placement_function: Incomplete | None = None):
        """Generates the host-side Ops to enqueue the shards of a tuple.

    sharded_inputs is a list, one for each shard, of lists of
    Tensors. sharded_inputs[i] is the tuple of Tensors to use to feed
    shard i of the queue. Returns the host-side Ops that must be run to
    enqueue the sharded tuple. The Op for shard i is colocated with the inputs
    for shard i.

    Implicitly freezes the queue configuration if it is not already
    frozen. If the configuration has already been frozen, and is not
    compatible with the types and shapes of sharded_inputs, an error
    will be raised.

    Args:
      sharded_inputs: a list of lists of Tensors. The length of the outer list
        determines the number of shards. Each inner list indicates the types
        and shapes of the tuples in the corresponding shard.
      tpu_ordinal_function: if not None, a function that takes the
        shard index as input and returns the ordinal of the TPU device
        the shard's infeed should be placed on. tpu_ordinal_function must be
        set if the inputs are placed on CPU devices.
      placement_function: if not None, a function that takes the shard index as
        input and returns the host device where the enqueue op should be placed
        on.

    Returns:
      A list of host-side Ops, one for each shard, that when executed together
      will enqueue a full-size element of infeed.

    Raises:
      ValueError: if the queue configuration has previously been frozen and the
        shapes of the elements of sharded_inputs are not compatible with the
        frozen configuration; or if the shapes of the elements of sharded_inputs
        don't form a consistent unsharded tuple; or if the elements of a tuple
        have different device constraints.
      TypeError: if the queue configuration has previously been frozen and the
        types of the elements of sharded_inputs are not compatible with the
        frozen configuration; or if the types of the elements of sharded_inputs
        don't form a consistent unsharded tuple.
    """
    def split_inputs_and_generate_enqueue_ops(self, inputs, device_assignment: Incomplete | None = None, placement_function: Incomplete | None = None, tpu_ordinal_function: Incomplete | None = None):
        """POORLY-PERFORMING ON MULTI-HOST SYSTEMS.

    Generates the host-side Ops to enqueue a tuple.

    This method performs poorly because it takes an entire input on a single
    host, splits it, and distributes it to all of the cores. It is present only
    to simplify tutorial examples.

    inputs is a list of Tensors to use to feed the queue. Each input is split
    into self.number_of_shards shards. Returns an Op for each shard to enqueue
    the shard. The Op for shard i is placed on device placement_function(i).

    Implicitly freezes the queue configuration if it is not already
    frozen. If the configuration has already been frozen, and is not
    compatible with the types and shapes of inputs, an error
    will be raised.

    Args:
      inputs: a list of Tensors which indicates the types and shapes of the
        queue tuple.
     device_assignment: if not `None`, a TPU `DeviceAssignment`. If
        device_assignment is not `None`, but `placement_function` and
        `ordinal_function` are None, then `device_assignment` will be used to
        place infeeds on the first k TPU shards, where k is the number of shards
        in the queue. If all three are `None`, then default placement and
        ordinal functions are used.
      placement_function: if not None, a function that takes the shard
        index as input and returns a device string indicating which
        device the shard's infeed should be placed on. If placement_function
        and tpu_ordinal_function are None, inputs are sharded round-robin
        across the devices in the system.
      tpu_ordinal_function: if not None, a function that takes the
        shard index as input and returns the ordinal of the TPU device
        the shard's infeed should be placed on. If placement_function
        and tpu_ordinal_function are None, inputs are sharded round-robin
        across the devices in the system.

    Returns:
      A list of host-side Ops, one for each shard, that when executed together
      will enqueue a full-size element of infeed.

    Raises:
      ValueError: if the queue configuration has previously been frozen and the
        shapes of the elements of inputs are not compatible with the frozen
        configuration.
      TypeError: if the queue configuration has previously been frozen and the
        types of the elements of inputs are not compatible with the frozen
        configuration.
    """

class _PartitionedInfeedQueue(InfeedQueue):
    """A helper object to build a device infeed queue with input partition.

  Args:
    number_of_tuple_elements: the number of Tensors fed atomically through the
      queue, must be present unless it can be inferred from other arguments.
    device_assignment: A TPU `DeviceAssignment` which is used to place all the
      partitions to different TPU infeed queues.
    host_id: The id of the host machine.
    input_partition_dims: A nested list/tuple of integers. Each inner
      list/tuple describes how to partition the corresponding input tensor.
    tuple_types: If not None, a list of types of the elements of the queue.
    tuple_shapes: If not None, a list of shapes of the elements of the queue.
    name: The name of the queue.
  """
    def __init__(self, number_of_tuple_elements, device_assignment, host_id, input_partition_dims: Incomplete | None = None, tuple_types: Incomplete | None = None, tuple_shapes: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    def generate_dequeue_op(self, tpu_device: int = 0):
        """Generate TPU dequeue ops.

    Args:
      tpu_device: The TPU device ordinal where the infeed instruction should be
        placed.

    Returns:
      A list of Outputs corresponding to a partition of infeed dequeued
      into XLA, suitable for use within a replicated block.

    Raises:
      ValueError: if the types or shapes of the tuple elements have not been
      set; or if a dequeue op has already been generated.
    """
    def generate_enqueue_ops(self, sharded_inputs):
        """Generates the host-side Ops to enqueue the partitioned inputs.

    sharded_inputs is a list, one for each replica, of lists of
    Tensors. sharded_inputs[i] is the tuple of Tensors to use to feed
    replica i.
    sharded_inputs[i][j] is partitioned by self._input_partition_dims[j].

    For example, if sharded_inputs[i][j] is a 2-D Tensor:
    [[A, B, C, D],
     [E ,F, G, H]]
    self._input_partition_dims[j] is [2, 4].

    sharded_inputs[i][j] will be partitioned and flattened into:
    [A, B, C, D, E, F, G, H] and fed into the logical core ids:
    [0, 1, 2, 3, 4, 5, 6, 7] respectively.

    Args:
      sharded_inputs: a list of lists of Tensors. The length of the
        outer list determines the number of shards. Each inner list indicates
        the types and shapes of the tuples in the corresponding shard.

    Returns:
      A list of host-side Ops, one for each shard, that when executed together
      will enqueue a full-size element of infeed.

    Raises:
      ValueError: if the queue configuration has previously been frozen and the
        shapes of the elements of sharded_inputs are not compatible with the
        frozen configuration; or if the shapes of the elements of sharded_inputs
        don't form a consistent unsharded tuple; or if the elements of a tuple
        have different device constraints; or if the partition dims are invalid.
      TypeError: if the queue configuration has previously been frozen and the
        types of the elements of sharded_inputs are not compatible with the
        frozen configuration; or if the types of the elements of sharded_inputs
        don't form a consistent unsharded tuple.
    """
