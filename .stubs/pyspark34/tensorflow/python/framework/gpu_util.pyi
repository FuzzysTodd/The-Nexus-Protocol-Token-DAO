from _typeshed import Incomplete
from typing import NamedTuple

class GpuInfo(NamedTuple):
    name: Incomplete
    compute_capability: Incomplete

def compute_capability_from_device_desc(device_attrs):
    """Returns the GpuInfo given a DeviceAttributes proto.

  Args:
    device_attrs: A DeviceAttributes proto.

  Returns
    A gpu_info tuple. Both fields are None if `device_attrs` does not have a
    valid physical_device_desc field.
  """
