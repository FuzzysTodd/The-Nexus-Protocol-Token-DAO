import enum
import numpy as np
from _typeshed import Incomplete
from tensorflow.python.tpu.topology import Topology as Topology
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import List, Optional, Text, Tuple

SINGLE_CORE_ASSIGNMENT: Incomplete

class DeviceAssignment:
    """Mapping from logical cores in a computation to the physical TPU topology.

  Prefer to use the `DeviceAssignment.build()` helper to construct a
  `DeviceAssignment`; it is easier if less flexible than constructing a
  `DeviceAssignment` directly.
  """
    def __init__(self, topology: Topology, core_assignment: np.ndarray) -> None:
        """Constructs a `DeviceAssignment` object.

    Args:
      topology: A `Topology` object that describes the physical TPU topology.
      core_assignment: A logical to physical core mapping, represented as a
        rank 3 numpy array. See the description of the `core_assignment`
        property for more details.

    Raises:
      ValueError: If `topology` is not `Topology` object.
      ValueError: If `core_assignment` is not a rank 3 numpy array.
    """
    @property
    def topology(self) -> Topology:
        """A `Topology` that describes the TPU topology."""
    @property
    def num_cores_per_replica(self) -> int:
        """The number of cores per replica."""
    @property
    def num_replicas(self) -> int:
        """The number of replicas of the computation."""
    @property
    def core_assignment(self) -> np.ndarray:
        """The logical to physical core mapping.

    Returns:
      An integer numpy array of rank 3, with shape
      `[num_replicas, num_cores_per_replica, topology_rank]`. Maps
      (replica, logical core) pairs to physical topology coordinates.
    """
    def coordinates(self, replica: int, logical_core: int) -> Tuple:
        """Returns the physical topology coordinates of a logical core."""
    def lookup_replicas(self, task_id: int, logical_core: int) -> List[int]:
        """Lookup replica ids by task number and logical core.

    Args:
      task_id: TensorFlow task number.
      logical_core: An integer, identifying a logical core.
    Returns:
      A sorted list of the replicas that are attached to that task and
      logical_core.
    Raises:
      ValueError: If no replica exists in the task which contains the logical
      core.
    """
    def tpu_ordinal(self, replica: int = 0, logical_core: int = 0) -> int:
        """Returns the ordinal of the TPU device assigned to a logical core."""
    def host_device(self, replica: int = 0, logical_core: int = 0, job: Optional[Text] = None) -> Text:
        """Returns the CPU device attached to a logical core."""
    def tpu_device(self, replica: int = 0, logical_core: int = 0, job: Optional[Text] = None) -> Text:
        """Returns the name of the TPU device assigned to a logical core."""
    @staticmethod
    def build(topology: Topology, computation_shape: Optional[np.ndarray] = None, computation_stride: Optional[np.ndarray] = None, num_replicas: int = 1) -> DeviceAssignment: ...

class DeviceOrderMode(enum.IntEnum):
    """The way of determining device orders when computing device assignment."""
    AUTO: int
    RING: int
    MESH: int

def device_assignment(topology: Topology, computation_shape: Optional[np.ndarray] = None, computation_stride: Optional[np.ndarray] = None, num_replicas: int = 1, device_order_mode: DeviceOrderMode = ...) -> DeviceAssignment:
    """Computes a device_assignment of a computation across a TPU topology.

  Attempts to choose a compact grid of cores for locality.

  Returns a `DeviceAssignment` that describes the cores in the topology assigned
  to each core of each replica.

  `computation_shape` and `computation_stride` values should be powers of 2 for
  optimal packing.

  Args:
    topology: A `Topology` object that describes the TPU cluster topology. To
      obtain a TPU topology, evaluate the `Tensor` returned by
      `initialize_system` using `Session.run`. Either a serialized
      `TopologyProto` or a `Topology` object may be passed. Note: you must
        evaluate the `Tensor` first; you cannot pass an unevaluated `Tensor`
        here.
    computation_shape: A rank 1 int32 numpy array with size equal to the
      topology rank, describing the shape of the computation's block of cores.
      If None, the `computation_shape` is `[1] * topology_rank`.
    computation_stride: A rank 1 int32 numpy array of size `topology_rank`,
      describing the inter-core spacing of the `computation_shape` cores in the
      TPU topology. If None, the `computation_stride` is `[1] * topology_rank`.
    num_replicas: The number of computation replicas to run. The replicas will
      be packed into the free spaces of the topology.
    device_order_mode: An enum of `DeviceOrderMode` class which indicates
      whether to assign devices to form rings or meshes, or let the library to
      choose.

  Returns:
    A DeviceAssignment object, which describes the mapping between the logical
    cores in each computation replica and the physical cores in the TPU
    topology.

  Raises:
    ValueError: If `topology` is not a valid `Topology` object.
    ValueError: If `computation_shape` or `computation_stride` are not 1D int32
      numpy arrays with shape [3] where all values are positive.
    ValueError: If computation's replicas cannot fit into the TPU topology.
  """
