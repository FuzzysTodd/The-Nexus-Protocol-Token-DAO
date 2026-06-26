from _typeshed import Incomplete
from tensorflow.compiler.xla import xla_data_pb2 as xla_data_pb2
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2

class Sharding:
    """A class to support adding sharding attributes to Ops.

  Use the factory constructors and then call apply_to_tensor:
    Sharding.replicate().apply_to_tensor(tensor)
  """
    def __init__(self, proto: Incomplete | None = None) -> None:
        """Do not use this constructor; use the factory functions below."""
    @classmethod
    def replicate(cls):
        """Returns a replicated sharding attribute.

    This causes an op to be computed in its entirety independently on all
    cores in the XLA device.
    """
    @classmethod
    def manual(cls):
        """Returns a manuall sharding attribute.

    This means the op is manually partitioned by the user and XLA will not
    change the shapes.
    """
    @classmethod
    def assign_device(cls, core):
        """Returns an AssignDevice sharding attribute.

    This causes an op to be computed in its entirety only on one core in
    the XLA device.
    Args:
      core: The core to assign this Op to.
    """
    @classmethod
    def tile(cls, tile_assignment):
        """Returns a Tiled sharding attribute.

    This causes an op to be partially computed on multiple cores in the
    XLA device.

    Args:
      tile_assignment: An np.ndarray describing the topology of the tiling and
        which device will compute which part of the topology.

    Raises:
      TypeError: tile_assignment was not of np.array type.

    TODO(jmolloy): This concept is nefarious and is not
    something we really want to expose to users (especially as the
    contract for tile_assignment is very strict).
    """
    @classmethod
    def subgroup_tile(cls, tile_assignment, subgroup_modes):
        """Returns a subgroup manual sharding attribute.

    This is similar to tile(), but tile_assignment has one or more dimension
    than the tensor, and subgroup_modes define the sharding types in the last
    dimensions of tile_assignment.

    Args:
      tile_assignment: An np.ndarray describing the topology of the tiling and
        which device will compute which part of the topology.
      subgroup_modes: sharding types for the dimension more than the tensor
        shape rank.

    Raises:
      TypeError: tile_assignment was not of np.array type or subgroup_modes
        has unsupported sharding type.
    """
    @classmethod
    def partial_tile(cls, tile_assignment):
        """Returns a partially tiled sharding attribute.

    This is similar to tile(), but tile_assignment has one more dimension than
    the tensor, and tiles in the last dimension of tile_assignment are
    replicated.

    Args:
      tile_assignment: An np.ndarray describing the topology of the tiling and
        which device will compute which part of the topology.

    Raises:
      TypeError: tile_assignment was not of np.array type.
    """
    @classmethod
    def split(cls, tensor, split_dimension, num_devices, input_shape: Incomplete | None = None):
        """Returns a Sharding that splits a tensor across a dimension.

    This creates a Tiled attribute, similar to tile(), but easier to use for the
    common case of tiling a tensor N ways in one dimension.

    Args:
      tensor: A tf.Tensor to split.
      split_dimension: The dimension number to split.
      num_devices: The number of cores to split `tensor` over.
      input_shape: The shape of the original tensor.

    Raises:
      ValueError: The tensor to split was smaller in the split dimension than
        the number of devices to split over.
    """
    def apply_to_tensor(self, tensor, assign_tuple_sharding: bool = False, use_sharding_op: bool = False, unspecified_dims: Incomplete | None = None):
        """Applies this Sharding attribute to `tensor`.

    Args:
      tensor: A tf.Tensor to split.
      assign_tuple_sharding: If the sharding type should be a tuple.
      use_sharding_op: Whether to create a sharding op on `tensor`.
      unspecified_dims: An optional list of dimensions unspecified.

    Returns:
      The tensor with Sharding attribute.
    """
    def apply_to_operation(self, operation) -> None:
        """Applies this Sharding attribute to `operation`.

    Args:
      operation: A tf.Operation to add sharding annotation.
    """
    @property
    def proto(self):
        """Return the sharding protobuf of type xla_data_pb2.OpSharding."""

def copy_sharding(from_tensor, to_tensor, use_sharding_op: bool = False):
    """Copies the a tensor's sharding to another.

  Args:
    from_tensor: Source tensor. Must be the sole output of an op.
    to_tensor: the tensor the annotate with the copy.
    use_sharding_op: whether to create a sharding op on `to_tensor`.

  Returns:
    A tensor with sharding annotation copied from `from_tensor`.
  """
def replicate(tensor, assign_tuple_sharding: bool = False, use_sharding_op: bool = False): ...
def assign_device(tensor, device, assign_tuple_sharding: bool = False, use_sharding_op: bool = False):
    """Returns a tensor that has AssignDevice sharding attribute."""
def tile(tensor, tile_assignment, assign_tuple_sharding: bool = False, use_sharding_op: bool = False, unspecified_dims: Incomplete | None = None):
    """Returns a tensor that has tiled sharding.

  Args:
    tensor: A tf.Tensor to shard.
    tile_assignment: An np.ndarray describing the topology of the tiling and
      which device will compute which part of the topology.
    assign_tuple_sharding: If the sharding type should be a tuple.
    use_sharding_op: If true, adds a sharding op to set the sharding.
    unspecified_dims: An optional list of dimensions unspecified.
  """
def split(tensor, split_dimension, num_devices, assign_tuple_sharding: bool = False, use_sharding_op: bool = False, input_shape: Incomplete | None = None):
    """Returns a tensor that is split along the given dimension.

  Args:
    tensor: A tf.Tensor to split.
    split_dimension: The dimension to split.
    num_devices: The number of devices to partition the dimension.
    assign_tuple_sharding: If the sharding type should be a tuple.
    use_sharding_op: If true, adds a sharding op to set the sharding.
    input_shape: The full shape of the input tensor.
  """
def partial_tile(tensor, tile_assignment, use_sharding_op: bool = False, unspecified_dims: Incomplete | None = None):
    """Returns a tensor that has tiled sharding.

  Args:
    tensor: A tf.Tensor to shard.
    tile_assignment: An np.ndarray describing the topology of the tiling and
      which device will compute which part of the topology. It must have one
      more dimension than tensor, and the last dimension represents partially
      replicated tiles.
    use_sharding_op: If true, adds a sharding op to set the sharding.
    unspecified_dims: An optional list of dimensions unspecified.
  """
def get_op_sharding(op):
    """Returns sharding attribute of an op.

  Args:
    op: a TensorFlow op.

  Returns:
    The attribute representing XLA sharding on this op.
  """
def get_tensor_sharding(tensor):
    """Returns sharding attribute of a Tensor.

  Args:
    tensor: a Tensor.

  Returns:
    The attribute representing XLA sharding on tensor's op.
  """
def get_sharding_tile_shape(sharding):
    """Returns the tile assignment shape for a sharded Tensor.

  Args:
    sharding: a serialized OpSharding message describing the layout of a
      sharded Tensor.

  Returns:
    A list, for each dimension of the sharded Tensor, of the number of shards
      into which it has been split. Returns None if the input indicates no tile
      assignments.
  """
def auto_to_manual_spmd_partition(tensor, manual_sharding, single_dim: int = -1, unspecified_dims: Incomplete | None = None):
    """Switches from automatic SPMD partitioning to manual partitioning.

  Converts a full-shaped tensor (to be automatically partitioned by SPMD
  partitioner) to a shard-shaped tensor to be consumed by manually partitioned
  ops.

  Args:
    tensor: A tf.Tensor in full shape.
    manual_sharding: A serialized string of OpSharding to be used in manual
      partitioning.
    single_dim: If >= 0, the conversion will happen only on this dim in
      subgroups.
    unspecified_dims: An optional list of dimensions unspecified.

  Returns:
    A shard-shaped tensor to be consumed by manually partitioned ops.
  """
def manual_to_auto_spmd_partition(tensor, manual_sharding, full_shape, single_dim: int = -1, unspecified_dims: Incomplete | None = None):
    """Switches from manual partitioning to automatic SPMD partitioning.

  Converts a shard-shaped tensor (manually partitioned in SPMD-style) to a
  full-shaped tensor to be partitioned automatically by the SPMD partitioner.

  Args:
    tensor: A tf.Tensor in shard shape.
    manual_sharding: a serialized string of OpSharding to be used in manual
      partitioning.
    full_shape: the shape of tensor before partitioning.
    single_dim: If >= 0, the conversion will happen only on this dim in
      subgroups.
    unspecified_dims: An optional list of dimensions unspecified.

  Returns:
    A full-shaped tensor to be partitioned automatically by the SPMD
    partitioner.
  """
def mesh_split_sharding(device_mesh, tensor_split_dims_mapping, manual_mesh_dims: Incomplete | None = None):
    """Returns a Sharding object representing sharding along multiple dimensions.

  Args:
    device_mesh: An np.ndarray describing the topology of the device mesh and
      each element is the ID of the device in the topology.
    tensor_split_dims_mapping: A list of integers that map each tensor axis to
      the device mesh axis along which it is sharded. Its length is the tensor
      rank, and tensor_split_dims_mapping[i] is device mesh axis for tensor
      dimension i. Use -1 for tensor dimensions that are not sharded.
    manual_mesh_dims: An optional list of mesh dims for manual subgroups.

  Raises:
    ValueError: The number of tensor split dimensions is larger than device mesh
      rank.
  """
def mesh_split(tensor, device_mesh, tensor_split_dims_mapping, use_sharding_op: bool = False, manual_mesh_dims: Incomplete | None = None, unspecified_dims: Incomplete | None = None):
    """Returns a tensor that is split along multiple dimensions in a device mesh.

  Args:
    tensor: A tf.Tensor to split.
    device_mesh: An np.ndarray describing the topology of the device mesh and
      each element is the ID of the device in the topology.
    tensor_split_dims_mapping: A list of integers that map each tensor axis to
      the device mesh axis along which it is sharded. Its length is the tensor
      rank, and tensor_split_dims_mapping[i] is device mesh axis for tensor
      dimension i. Use -1 for tensor dimensions that are not sharded.
    use_sharding_op: If true, adds a sharding op to set the sharding.
    manual_mesh_dims: An optional list of mesh dims for manual subgroups.
    unspecified_dims: An optional list of dimensions unspecified.

  Raises:
    ValueError: The number of tensor split dimensions is larger than device mesh
      rank.
  """
