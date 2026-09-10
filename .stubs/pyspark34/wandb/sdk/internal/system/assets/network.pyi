import threading
from .aggregators import aggregate_mean as aggregate_mean
from .asset_registry import asset_registry as asset_registry
from .interfaces import Interface as Interface, Metric as Metric, MetricsMonitor as MetricsMonitor
from _typeshed import Incomplete
from typing import Deque
from wandb.sdk.internal.settings_static import SettingsStatic as SettingsStatic

class NetworkSent:
    """Network bytes sent."""
    name: str
    samples: Deque[float]
    sent_init: Incomplete
    def __init__(self) -> None: ...
    def sample(self) -> None: ...
    def clear(self) -> None: ...
    def aggregate(self) -> dict: ...

class NetworkRecv:
    """Network bytes received."""
    name: str
    samples: Deque[float]
    recv_init: Incomplete
    def __init__(self) -> None: ...
    def sample(self) -> None: ...
    def clear(self) -> None: ...
    def aggregate(self) -> dict: ...

class Network:
    name: Incomplete
    metrics: Incomplete
    metrics_monitor: Incomplete
    def __init__(self, interface: Interface, settings: SettingsStatic, shutdown_event: threading.Event) -> None: ...
    def start(self) -> None: ...
    def finish(self) -> None: ...
    @classmethod
    def is_available(cls) -> bool:
        """Return a new instance of the CPU metrics."""
    def probe(self) -> dict:
        """Return a dict of the hardware information."""
