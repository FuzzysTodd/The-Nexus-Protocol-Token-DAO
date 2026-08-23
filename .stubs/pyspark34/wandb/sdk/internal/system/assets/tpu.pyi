import threading
from .aggregators import aggregate_mean as aggregate_mean
from .asset_registry import asset_registry as asset_registry
from .interfaces import Interface as Interface, Metric as Metric, MetricsMonitor as MetricsMonitor
from _typeshed import Incomplete
from typing import Deque
from wandb.sdk.internal.settings_static import SettingsStatic as SettingsStatic

logger: Incomplete

class TPUUtilization:
    """Google Cloud TPU utilization in percent."""
    name: str
    samples: Deque[float]
    duration_ms: Incomplete
    service_addr: Incomplete
    def __init__(self, service_addr: str, duration_ms: int = 100) -> None: ...
    def sample(self) -> None: ...
    def clear(self) -> None: ...
    def aggregate(self) -> dict: ...

class TPU:
    name: Incomplete
    service_addr: Incomplete
    metrics: Incomplete
    metrics_monitor: Incomplete
    def __init__(self, interface: Interface, settings: SettingsStatic, shutdown_event: threading.Event) -> None: ...
    @staticmethod
    def get_service_addr(service_addr: str | None = None, tpu_name: str | None = None, compute_zone: str | None = None, core_project: str | None = None) -> str: ...
    def start(self) -> None: ...
    def finish(self) -> None: ...
    @classmethod
    def is_available(cls) -> bool: ...
    def probe(self) -> dict: ...
