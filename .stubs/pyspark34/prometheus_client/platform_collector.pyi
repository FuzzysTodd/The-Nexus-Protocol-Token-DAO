from .metrics_core import GaugeMetricFamily as GaugeMetricFamily, Metric as Metric
from .registry import Collector as Collector, CollectorRegistry as CollectorRegistry, REGISTRY as REGISTRY
from _typeshed import Incomplete
from typing import Any, Iterable

class PlatformCollector(Collector):
    """Collector for python platform information"""
    def __init__(self, registry: CollectorRegistry = ..., platform: Any | None = None) -> None: ...
    def collect(self) -> Iterable[Metric]: ...

PLATFORM_COLLECTOR: Incomplete
