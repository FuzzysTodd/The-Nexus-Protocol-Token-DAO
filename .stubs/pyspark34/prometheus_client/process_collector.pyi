from .metrics_core import CounterMetricFamily as CounterMetricFamily, GaugeMetricFamily as GaugeMetricFamily, Metric as Metric
from .registry import Collector as Collector, CollectorRegistry as CollectorRegistry, REGISTRY as REGISTRY
from _typeshed import Incomplete
from typing import Callable, Iterable

class ProcessCollector(Collector):
    """Collector for Standard Exports such as cpu and memory."""
    def __init__(self, namespace: str = '', pid: Callable[[], int | str] = ..., proc: str = '/proc', registry: CollectorRegistry = ...) -> None: ...
    def collect(self) -> Iterable[Metric]: ...

PROCESS_COLLECTOR: Incomplete
