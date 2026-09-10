from .samples import Exemplar as Exemplar, Sample as Sample, Timestamp as Timestamp
from _typeshed import Incomplete
from typing import Dict, Sequence, Tuple

METRIC_TYPES: Incomplete
METRIC_NAME_RE: Incomplete
METRIC_LABEL_NAME_RE: Incomplete
RESERVED_METRIC_LABEL_NAME_RE: Incomplete

class Metric:
    """A single metric family and its samples.

    This is intended only for internal use by the instrumentation client.

    Custom collectors should use GaugeMetricFamily, CounterMetricFamily
    and SummaryMetricFamily instead.
    """
    name: Incomplete
    documentation: Incomplete
    unit: Incomplete
    type: Incomplete
    samples: Incomplete
    def __init__(self, name: str, documentation: str, typ: str, unit: str = '') -> None: ...
    def add_sample(self, name: str, labels: Dict[str, str], value: float, timestamp: Timestamp | float | None = None, exemplar: Exemplar | None = None) -> None:
        """Add a sample to the metric.

        Internal-only, do not use."""
    def __eq__(self, other: object) -> bool: ...

class UnknownMetricFamily(Metric):
    """A single unknown metric and its samples.
    For use by custom collectors.
    """
    def __init__(self, name: str, documentation: str, value: float | None = None, labels: Sequence[str] | None = None, unit: str = '') -> None: ...
    def add_metric(self, labels: Sequence[str], value: float, timestamp: Timestamp | float | None = None) -> None:
        """Add a metric to the metric family.
        Args:
        labels: A list of label values
        value: The value of the metric.
        """
UntypedMetricFamily = UnknownMetricFamily

class CounterMetricFamily(Metric):
    """A single counter and its samples.

    For use by custom collectors.
    """
    def __init__(self, name: str, documentation: str, value: float | None = None, labels: Sequence[str] | None = None, created: float | None = None, unit: str = '') -> None: ...
    def add_metric(self, labels: Sequence[str], value: float, created: float | None = None, timestamp: Timestamp | float | None = None) -> None:
        """Add a metric to the metric family.

        Args:
          labels: A list of label values
          value: The value of the metric
          created: Optional unix timestamp the child was created at.
        """

class GaugeMetricFamily(Metric):
    """A single gauge and its samples.

    For use by custom collectors.
    """
    def __init__(self, name: str, documentation: str, value: float | None = None, labels: Sequence[str] | None = None, unit: str = '') -> None: ...
    def add_metric(self, labels: Sequence[str], value: float, timestamp: Timestamp | float | None = None) -> None:
        """Add a metric to the metric family.

        Args:
          labels: A list of label values
          value: A float
        """

class SummaryMetricFamily(Metric):
    """A single summary and its samples.

    For use by custom collectors.
    """
    def __init__(self, name: str, documentation: str, count_value: int | None = None, sum_value: float | None = None, labels: Sequence[str] | None = None, unit: str = '') -> None: ...
    def add_metric(self, labels: Sequence[str], count_value: int, sum_value: float, timestamp: float | Timestamp | None = None) -> None:
        """Add a metric to the metric family.

        Args:
          labels: A list of label values
          count_value: The count value of the metric.
          sum_value: The sum value of the metric.
        """

class HistogramMetricFamily(Metric):
    """A single histogram and its samples.

    For use by custom collectors.
    """
    def __init__(self, name: str, documentation: str, buckets: Sequence[Tuple[str, float] | Tuple[str, float, Exemplar]] | None = None, sum_value: float | None = None, labels: Sequence[str] | None = None, unit: str = '') -> None: ...
    def add_metric(self, labels: Sequence[str], buckets: Sequence[Tuple[str, float] | Tuple[str, float, Exemplar]], sum_value: float | None, timestamp: Timestamp | float | None = None) -> None:
        """Add a metric to the metric family.

        Args:
          labels: A list of label values
          buckets: A list of lists.
              Each inner list can be a pair of bucket name and value,
              or a triple of bucket name, value, and exemplar.
              The buckets must be sorted, and +Inf present.
          sum_value: The sum value of the metric.
        """

class GaugeHistogramMetricFamily(Metric):
    """A single gauge histogram and its samples.

    For use by custom collectors.
    """
    def __init__(self, name: str, documentation: str, buckets: Sequence[Tuple[str, float]] | None = None, gsum_value: float | None = None, labels: Sequence[str] | None = None, unit: str = '') -> None: ...
    def add_metric(self, labels: Sequence[str], buckets: Sequence[Tuple[str, float]], gsum_value: float | None, timestamp: float | Timestamp | None = None) -> None:
        """Add a metric to the metric family.

        Args:
          labels: A list of label values
          buckets: A list of pairs of bucket names and values.
              The buckets must be sorted, and +Inf present.
          gsum_value: The sum value of the metric.
        """

class InfoMetricFamily(Metric):
    """A single info and its samples.

    For use by custom collectors.
    """
    def __init__(self, name: str, documentation: str, value: Dict[str, str] | None = None, labels: Sequence[str] | None = None) -> None: ...
    def add_metric(self, labels: Sequence[str], value: Dict[str, str], timestamp: Timestamp | float | None = None) -> None:
        """Add a metric to the metric family.

        Args:
          labels: A list of label values
          value: A dict of labels
        """

class StateSetMetricFamily(Metric):
    """A single stateset and its samples.

    For use by custom collectors.
    """
    def __init__(self, name: str, documentation: str, value: Dict[str, bool] | None = None, labels: Sequence[str] | None = None) -> None: ...
    def add_metric(self, labels: Sequence[str], value: Dict[str, bool], timestamp: Timestamp | float | None = None) -> None:
        """Add a metric to the metric family.

        Args:
          labels: A list of label values
          value: A dict of string state names to booleans
        """
