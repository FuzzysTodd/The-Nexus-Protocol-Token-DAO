import abc
from .metrics_core import Metric as Metric
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import Dict, Iterable

class Collector(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def collect(self) -> Iterable[Metric]: ...

class _EmptyCollector(Collector):
    def collect(self) -> Iterable[Metric]: ...

class CollectorRegistry(Collector):
    """Metric collector registry.

    Collectors must have a no-argument method 'collect' that returns a list of
    Metric objects. The returned metrics should be consistent with the Prometheus
    exposition formats.
    """
    def __init__(self, auto_describe: bool = False, target_info: Dict[str, str] | None = None) -> None: ...
    def register(self, collector: Collector) -> None:
        """Add a collector to the registry."""
    def unregister(self, collector: Collector) -> None:
        """Remove a collector from the registry."""
    def collect(self) -> Iterable[Metric]:
        """Yields metrics from the collectors in the registry."""
    def restricted_registry(self, names: Iterable[str]) -> RestrictedRegistry:
        """Returns object that only collects some metrics.

        Returns an object which upon collect() will return
        only samples with the given names.

        Intended usage is:
            generate_latest(REGISTRY.restricted_registry(['a_timeseries']))

        Experimental."""
    def set_target_info(self, labels: Dict[str, str] | None) -> None: ...
    def get_target_info(self) -> Dict[str, str] | None: ...
    def get_sample_value(self, name: str, labels: Dict[str, str] | None = None) -> float | None:
        """Returns the sample value, or None if not found.

        This is inefficient, and intended only for use in unittests.
        """

class RestrictedRegistry:
    def __init__(self, names: Iterable[str], registry: CollectorRegistry) -> None: ...
    def collect(self) -> Iterable[Metric]: ...

REGISTRY: Incomplete
