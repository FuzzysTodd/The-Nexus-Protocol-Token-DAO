import threading
from .aggregators import aggregate_last as aggregate_last, aggregate_mean as aggregate_mean
from .interfaces import Interface as Interface, Metric as Metric, MetricsMonitor as MetricsMonitor
from _typeshed import Incomplete
from types import ModuleType
from typing import Dict, Mapping, Sequence
from wandb.sdk.internal.settings_static import SettingsStatic as SettingsStatic
from wandb.sdk.lib import hashutil as hashutil, telemetry as telemetry

logger: Incomplete
prometheus_client_parser: ModuleType | None

class OpenMetricsMetric:
    """Container for all the COUNTER and GAUGE metrics extracted from an OpenMetrics endpoint."""
    name: Incomplete
    url: Incomplete
    filters: Incomplete
    filters_tuple: Incomplete
    samples: Incomplete
    label_map: Incomplete
    label_hashes: Incomplete
    def __init__(self, name: str, url: str, filters: Mapping[str, Mapping[str, str]] | Sequence[str] | None) -> None: ...
    def setup(self) -> None: ...
    def teardown(self) -> None: ...
    def parse_open_metrics_endpoint(self) -> Dict[str, str | int | float]: ...
    def sample(self) -> None: ...
    def clear(self) -> None: ...
    def aggregate(self) -> dict: ...

class OpenMetrics:
    name: Incomplete
    url: Incomplete
    interface: Incomplete
    settings: Incomplete
    shutdown_event: Incomplete
    metrics: Incomplete
    metrics_monitor: Incomplete
    def __init__(self, interface: Interface, settings: SettingsStatic, shutdown_event: threading.Event, name: str, url: str) -> None: ...
    @classmethod
    def is_available(cls, url: str) -> bool: ...
    def start(self) -> None: ...
    def finish(self) -> None: ...
    def probe(self) -> dict: ...
