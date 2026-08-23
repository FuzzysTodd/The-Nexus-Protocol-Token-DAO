import enum
from _typeshed import Incomplete
from tensorflow.python.eager import context as context

GCP_METADATA_HEADER: Incomplete
GRACE_PERIOD_GCE: int

def gce_exit_fn() -> None: ...
def default_tpu_exit_fn() -> None:
    """Default exit function to run after saving checkpoint for TPUStrategy.

  For TPUStrategy, we want the coordinator to exit after workers are down so
  that restarted coordinator would not connect to workers scheduled to be
  preempted. This function achieves so by attempting to get a key-value store
  from coordination service, which will block until workers are done and then
  returns with error. Then we have the coordinator sys.exit(42) to re-schedule
  the job.
  """
def request_compute_metadata(path):
    """Returns GCE VM compute metadata."""
def termination_watcher_function_gce(): ...
def on_gcp():
    """Detect whether the current running environment is on GCP."""

class PlatformDevice(enum.Enum):
    INTERNAL_CPU: str
    INTERNAL_GPU: str
    INTERNAL_TPU: str
    GCE_GPU: str
    GCE_TPU: str
    GCE_CPU: str
    UNSUPPORTED: str

def detect_platform():
    """Returns the platform and device information."""
