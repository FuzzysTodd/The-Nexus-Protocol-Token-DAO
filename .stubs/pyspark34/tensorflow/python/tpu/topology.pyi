from _typeshed import Incomplete
from tensorflow.core.protobuf.tpu import topology_pb2 as topology_pb2
from tensorflow.python.util.tf_export import tf_export as tf_export

class Topology:
    """Describes a set of TPU devices.

  Represents both the shape of the physical mesh, and the mapping between
  TensorFlow TPU devices to physical mesh coordinates.
  """
    def __init__(self, serialized: Incomplete | None = None, mesh_shape: Incomplete | None = None, device_coordinates: Incomplete | None = None) -> None:
        """Builds a Topology object.

    If `serialized` is not `None`, the topology is parsed from `serialized` and
    the other arguments are ignored. Otherwise, the topology is computed from
    `mesh_shape` and `device_coordinates`.

    Args:
      serialized: A serialized `TopologyProto`, or `None`. If not `None`, the
        serialized proto is parsed to discover the topology.
      mesh_shape: A sequence of 4 positive integers, or `None`. If not `None`,
        the shape of the TPU topology, in number of cores. Ignored if
        `serialized` is not `None`.
      device_coordinates: A rank 3 numpy array that describes the mapping from
        TensorFlow TPU devices to TPU fabric coordinates, or `None`. If
        specified, array is a rank 3 int32 array with shape
        `[tasks, devices, axis]`.  `tasks` is the number of tasks in the TPU
        cluster, `devices` is the number of TPU devices per task, and `axis` is
        the number of axes in the TPU cluster topology. Each entry gives the
        `axis`-th coordinate in the topology of a task/device pair. TPU
        topologies are 4-dimensional, with dimensions `(x, y, z, core number)`.
        This arg is ignored if `serialized is not `None`.

    Raises:
      ValueError: If `serialized` does not describe a well-formed topology.
      ValueError: If `serialized` is `None` and `mesh_shape` is not a sequence
        of 4 positive integers.
      ValueError: If `serialized` is `None` and `device_coordinates` is not a
        rank 3 numpy int32 array that describes a valid coordinate mapping.
    """
    @property
    def mesh_shape(self):
        """A rank 1 int32 array describing the shape of the TPU topology."""
    @property
    def mesh_rank(self):
        """Returns the number of dimensions in the mesh."""
    @property
    def device_coordinates(self):
        """Describes the mapping from TPU devices to topology coordinates.

    Returns:
      A rank 3 int32 array with shape `[tasks, devices, axis]`.
      `tasks` is the number of tasks in the TPU cluster, `devices` is the number
      of TPU devices per task, and `axis` is the number of axes in the TPU
      cluster topology. Each entry gives the `axis`-th coordinate in the
      topology of a task/device pair. TPU topologies are 4-dimensional, with
      dimensions `(x, y, z, core number)`.
    """
    @property
    def missing_devices(self):
        """Array of indices of missing devices."""
    def task_ordinal_at_coordinates(self, device_coordinates):
        """Returns the TensorFlow task number attached to `device_coordinates`.

    Args:
      device_coordinates: An integer sequence describing a device's physical
        coordinates in the TPU fabric.

    Returns:
      Returns the TensorFlow task number that contains the TPU device with those
      physical coordinates.
    """
    def tpu_device_ordinal_at_coordinates(self, device_coordinates):
        """Returns the TensorFlow device number at `device_coordinates`.

    Args:
      device_coordinates: An integer sequence describing a device's physical
        coordinates in the TPU fabric.

    Returns:
      Returns the TensorFlow device number within the task corresponding to
      attached to the device with those physical coordinates.
    """
    def cpu_device_name_at_coordinates(self, device_coordinates, job: Incomplete | None = None):
        """Returns the CPU device attached to a logical core."""
    def tpu_device_name_at_coordinates(self, device_coordinates, job: Incomplete | None = None):
        """Returns the name of the TPU device assigned to a logical core."""
    @property
    def num_tasks(self):
        """Returns the number of TensorFlow tasks in the TPU slice."""
    @property
    def num_tpus_per_task(self):
        """Returns the number of TPU devices per task in the TPU slice."""
    def serialized(self):
        """Returns the serialized form of the topology."""
