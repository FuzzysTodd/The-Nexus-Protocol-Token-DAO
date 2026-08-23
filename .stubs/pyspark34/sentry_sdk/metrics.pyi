from _typeshed import Incomplete
from sentry_sdk._compat import text_type as text_type
from sentry_sdk._types import BucketKey as BucketKey, DurationUnit as DurationUnit, FlushedMetricValue as FlushedMetricValue, MeasurementUnit as MeasurementUnit, MetricTagValue as MetricTagValue, MetricTags as MetricTags, MetricTagsInternal as MetricTagsInternal, MetricType as MetricType, MetricValue as MetricValue, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.envelope import Envelope as Envelope, Item as Item
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.tracing import TRANSACTION_SOURCE_COMPONENT as TRANSACTION_SOURCE_COMPONENT, TRANSACTION_SOURCE_ROUTE as TRANSACTION_SOURCE_ROUTE, TRANSACTION_SOURCE_TASK as TRANSACTION_SOURCE_TASK, TRANSACTION_SOURCE_VIEW as TRANSACTION_SOURCE_VIEW
from sentry_sdk.utils import nanosecond_time as nanosecond_time, now as now
from typing import Any, Callable, Generator, Iterable

GOOD_TRANSACTION_SOURCES: Incomplete

def recursion_protection() -> Generator[bool, None, None]:
    """Enters recursion protection and returns the old flag."""
def metrics_noop(func: Any) -> Any:
    """Convenient decorator that uses `recursion_protection` to
    make a function a noop.
    """

class Metric:
    @property
    def weight(self) -> int: ...
    def add(self, value: MetricValue) -> None: ...
    def serialize_value(self) -> Iterable[FlushedMetricValue]: ...

class CounterMetric(Metric):
    value: Incomplete
    def __init__(self, first: MetricValue) -> None: ...
    @property
    def weight(self) -> int: ...
    def add(self, value: MetricValue) -> None: ...
    def serialize_value(self) -> Iterable[FlushedMetricValue]: ...

class GaugeMetric(Metric):
    last: Incomplete
    min: Incomplete
    max: Incomplete
    sum: Incomplete
    count: int
    def __init__(self, first: MetricValue) -> None: ...
    @property
    def weight(self) -> int: ...
    def add(self, value: MetricValue) -> None: ...
    def serialize_value(self) -> Iterable[FlushedMetricValue]: ...

class DistributionMetric(Metric):
    value: Incomplete
    def __init__(self, first: MetricValue) -> None: ...
    @property
    def weight(self) -> int: ...
    def add(self, value: MetricValue) -> None: ...
    def serialize_value(self) -> Iterable[FlushedMetricValue]: ...

class SetMetric(Metric):
    value: Incomplete
    def __init__(self, first: MetricValue) -> None: ...
    @property
    def weight(self) -> int: ...
    def add(self, value: MetricValue) -> None: ...
    def serialize_value(self) -> Iterable[FlushedMetricValue]: ...

METRIC_TYPES: Incomplete
TIMING_FUNCTIONS: Incomplete

class MetricsAggregator:
    ROLLUP_IN_SECONDS: float
    MAX_WEIGHT: int
    FLUSHER_SLEEP_TIME: float
    buckets: Incomplete
    def __init__(self, capture_func: Callable[[Envelope], None]) -> None: ...
    def add(self, ty: MetricType, key: str, value: MetricValue, unit: MeasurementUnit, tags: MetricTags | None, timestamp: float | None = None) -> None: ...
    def kill(self) -> None: ...
    def flush(self) -> None: ...

def incr(key: str, value: float = 1.0, unit: MeasurementUnit = 'none', tags: MetricTags | None = None, timestamp: float | None = None) -> None:
    """Increments a counter."""

class _Timing:
    key: Incomplete
    tags: Incomplete
    timestamp: Incomplete
    value: Incomplete
    unit: Incomplete
    entered: Incomplete
    def __init__(self, key: str, tags: MetricTags | None, timestamp: float | None, value: float | None, unit: DurationUnit) -> None: ...
    def __enter__(self) -> _Timing: ...
    def __exit__(self, exc_type: Any, exc_value: Any, tb: Any) -> None: ...
    def __call__(self, f: Any) -> Any: ...

def timing(key: str, value: float | None = None, unit: DurationUnit = 'second', tags: MetricTags | None = None, timestamp: float | None = None) -> _Timing:
    """Emits a distribution with the time it takes to run the given code block.

    This method supports three forms of invocation:

    - when a `value` is provided, it functions similar to `distribution` but with
    - it can be used as a context manager
    - it can be used as a decorator
    """
def distribution(key: str, value: float, unit: MeasurementUnit = 'none', tags: MetricTags | None = None, timestamp: float | None = None) -> None:
    """Emits a distribution."""
def set(key: str, value: MetricValue, unit: MeasurementUnit = 'none', tags: MetricTags | None = None, timestamp: float | None = None) -> None:
    """Emits a set."""
def gauge(key: str, value: float, unit: MetricValue = 'none', tags: MetricTags | None = None, timestamp: float | None = None) -> None:
    """Emits a gauge."""
