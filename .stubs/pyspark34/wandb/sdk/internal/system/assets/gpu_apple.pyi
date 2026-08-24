import threading
from .aggregators import aggregate_mean as aggregate_mean
from .asset_registry import asset_registry as asset_registry
from .interfaces import Interface as Interface, Metric as Metric, MetricsMonitor as MetricsMonitor
from _typeshed import Incomplete
from typing import Deque, TypedDict
from wandb.sdk.internal.settings_static import SettingsStatic as SettingsStatic
from wandb.sdk.lib import telemetry as telemetry

logger: Incomplete

class _Stats(TypedDict):
    gpu: float
    memoryAllocated: float
    temp: float
    powerWatts: float
    powerPercent: float

class GPUAppleStats:
    """Apple GPU stats available on Arm Macs."""
    name: str
    samples: Deque[_Stats]
    MAX_POWER_WATTS: float
    binary_path: Incomplete
    def __init__(self) -> None: ...
    def sample(self) -> None: ...
    def clear(self) -> None: ...
    def aggregate(self) -> dict: ...

class GPUApple:
    name: Incomplete
    metrics: Incomplete
    metrics_monitor: Incomplete
    def __init__(self, interface: Interface, settings: SettingsStatic, shutdown_event: threading.Event) -> None: ...
    @classmethod
    def is_available(cls) -> bool: ...
    def start(self) -> None: ...
    def finish(self) -> None: ...
    def probe(self) -> dict: ...
