import datetime
import threading
from _typeshed import Incomplete
from typing import Any, Deque, List, Protocol, TypeVar
from wandb.proto.wandb_telemetry_pb2 import TelemetryRecord as TelemetryRecord
from wandb.sdk.interface.interface import FilesDict as FilesDict
from wandb.sdk.internal.settings_static import SettingsStatic as SettingsStatic

TimeStamp = TypeVar('TimeStamp', bound=datetime.datetime)
logger: Incomplete

class Metric(Protocol):
    """Base protocol for individual metrics."""
    name: str
    samples: Deque[Any]
    def sample(self) -> None:
        """Sample the metric."""
    def clear(self) -> None:
        """Clear the samples."""
    def aggregate(self) -> dict:
        """Aggregate the samples."""

class SetupTeardown(Protocol):
    """Protocol for classes that require setup and teardown."""
    def setup(self) -> None:
        """Extra setup required for the metric beyond __init__."""
    def teardown(self) -> None:
        """Extra teardown required for the metric."""

class Asset(Protocol):
    '''Base protocol encapsulate everything relating to an "Asset".

    An asset can be CPU, GPU, TPU, Network, I/O etc.
    '''
    name: str
    metrics: List[Metric]
    metrics_monitor: MetricsMonitor
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def is_available(cls) -> bool:
        """Check if the resource is available."""
    def start(self) -> None:
        """Start monitoring the resource."""
    def finish(self) -> None:
        """Finish monitoring the resource."""
    def probe(self) -> dict:
        """Get static information about the resource."""

class Interface(Protocol):
    def publish_stats(self, stats: dict) -> None: ...
    def publish_files(self, files_dict: FilesDict) -> None: ...

class MetricsMonitor:
    """Takes care of collecting, sampling, serializing, and publishing a set of metrics."""
    metrics: Incomplete
    asset_name: Incomplete
    sampling_interval: Incomplete
    samples_to_aggregate: Incomplete
    def __init__(self, asset_name: str, metrics: List[Metric], interface: Interface, settings: SettingsStatic, shutdown_event: threading.Event) -> None: ...
    def monitor(self) -> None:
        """Poll the Asset metrics."""
    def aggregate(self) -> dict:
        """Return a dict of metrics."""
    def publish(self) -> None:
        """Publish the Asset metrics."""
    def start(self) -> None: ...
    def finish(self) -> None: ...
