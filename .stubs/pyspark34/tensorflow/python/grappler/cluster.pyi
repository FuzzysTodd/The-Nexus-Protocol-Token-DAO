from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.core.framework import step_stats_pb2 as step_stats_pb2
from tensorflow.core.grappler.costs import op_performance_data_pb2 as op_performance_data_pb2
from tensorflow.core.protobuf import device_properties_pb2 as device_properties_pb2

class Cluster:
    """Grappler Clusters."""
    def __init__(self, allow_soft_placement: bool = True, disable_detailed_stats: bool = True, disable_timeline: bool = True, devices: Incomplete | None = None) -> None:
        """Creates a Cluster.

    Args:
      allow_soft_placement: If True, TF will automatically fix illegal
        placements instead of erroring out if the placement isn't legal.
      disable_detailed_stats: If True, detailed statistics will not be
        available.
      disable_timeline: If True, the timeline information will not be reported.
      devices: A list of devices of type device_properties_pb2.NamedDevice.
        If None, a device list will be created based on the spec of
        the local machine.
    """
    def Shutdown(self) -> None: ...
    def __del__(self) -> None: ...
    @property
    def tf_cluster(self): ...
    def ListDevices(self):
        """Returns a list of available hardware devices."""
    def ListAvailableOps(self):
        """Returns a list of all available operations (sorted alphabetically)."""
    def GetSupportedDevices(self, item): ...
    def EstimatePerformance(self, device): ...
    def MeasureCosts(self, item):
        """Returns the cost of running the specified item.

    Args:
      item: The item for which to measure the costs.
    Returns: The triplet op_perfs, runtime, step_stats.
    """
    def DeterminePeakMemoryUsage(self, item):
        """Returns a snapshot of the peak memory usage.

    Args:
      item: The item for which to measure the costs.
    Returns: A hashtable indexed by device name.
    """

def Provision(allow_soft_placement: bool = True, disable_detailed_stats: bool = True, disable_timeline: bool = True, devices: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
