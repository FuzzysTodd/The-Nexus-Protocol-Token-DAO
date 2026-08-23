from .metrics_core import CounterMetricFamily as CounterMetricFamily, Metric as Metric
from .registry import Collector as Collector, CollectorRegistry as CollectorRegistry, REGISTRY as REGISTRY
from _typeshed import Incomplete
from typing import Iterable

class GCCollector(Collector):
    """Collector for Garbage collection statistics."""
    def __init__(self, registry: CollectorRegistry = ...) -> None: ...
    def collect(self) -> Iterable[Metric]: ...

GC_COLLECTOR: Incomplete
