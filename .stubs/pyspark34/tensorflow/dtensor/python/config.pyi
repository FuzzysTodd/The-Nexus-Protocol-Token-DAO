from tensorflow.python.eager import context as context
from tensorflow.python.framework import device as tf_device
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import List, Optional

def local_devices(device_type: str, for_client_id: Optional[int] = None) -> List[tf_device.DeviceSpec]:
    """Returns a list of device specs configured on this client."""
def num_local_devices(device_type: str) -> int:
    """Returns the number of devices of device_type configured on this client."""
def num_global_devices(device_type: str) -> int:
    """Returns the number of devices of device_type in this DTensor cluster."""
def client_id() -> int:
    """Returns this client's ID."""
def num_clients() -> int:
    """Returns the number of clients in this DTensor cluster."""
def job_name() -> str:
    """Returns the job name used by all clients in this DTensor cluster."""
def full_job_name(task_id: Optional[int] = None) -> str:
    """Returns the fully qualified TF job name for this or another task."""
def jobs() -> List[str]:
    """Returns a list of job names of all clients in this DTensor cluster."""
def heartbeat_enabled() -> bool:
    """Returns true if DTensor heartbeat service is enabled."""
def is_local_mode() -> bool:
    """Returns true if DTensor shall run in local mode."""
def is_tpu_present() -> bool:
    """Returns true if TPU devices are present."""
def is_gpu_present() -> bool:
    """Returns true if TPU devices are present."""
def preferred_device_type() -> str:
    """Returns the preferred device type for the accelerators.

  The returned device type is determined by checking the first present device
  type from all supported device types in the order of 'TPU', 'GPU', 'CPU'.
  """
def gpu_use_nccl_communication() -> bool:
    """Return True if environment indicates NCCL shall be used for GPU."""
def backend_is_pw() -> bool:
    """Return True if environment indicates the backend is Pathways."""
