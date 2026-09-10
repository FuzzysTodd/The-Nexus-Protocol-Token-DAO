from _typeshed import Incomplete
from tensorflow.core.framework import summary_pb2 as summary_pb2
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.client import pywrap_tf_session as pywrap_tf_session
from tensorflow.python.framework import c_api_util as c_api_util
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class _MetricMethod(NamedTuple):
    create: Incomplete
    delete: Incomplete
    get_cell: Incomplete

class Metric:
    """The base class of metric."""
    def __init__(self, metric_name, metric_methods, label_length, *args) -> None:
        """Creates a new metric.

    Args:
      metric_name: name of the metric class.
      metric_methods: list of swig metric methods.
      label_length: length of label args.
      *args: the arguments to call create method.
    """
    def __del__(self) -> None: ...
    def get_cell(self, *labels):
        """Retrieves the cell."""

class CounterCell:
    """CounterCell stores each value of a Counter."""
    def __init__(self, cell) -> None:
        """Creates a new CounterCell.

    Args:
      cell: A c pointer of TFE_MonitoringCounterCell.
    """
    def increase_by(self, value) -> None:
        """Atomically increments the value.

    Args:
      value: non-negative value.
    """
    def value(self):
        """Retrieves the current value."""

class Counter(Metric):
    """A stateful class for updating a cumulative integer metric.

  This class encapsulates a set of values (or a single value for a label-less
  metric). Each value is identified by a tuple of labels. The class allows the
  user to increment each value.
  """
    def __init__(self, name, description, *labels) -> None:
        """Creates a new Counter.

    Args:
      name: name of the new metric.
      description: description of the new metric.
      *labels: The label list of the new metric.
    """
    def get_cell(self, *labels):
        """Retrieves the cell."""

class IntGaugeCell:
    """A single integer value stored in an `IntGauge`."""
    def __init__(self, cell) -> None:
        """Creates a new IntGaugeCell.

    Args:
      cell: A c pointer of TFE_MonitoringIntGaugeCell.
    """
    def set(self, value) -> None:
        """Atomically set the value.

    Args:
      value: integer value.
    """
    def value(self):
        """Retrieves the current value."""

class IntGauge(Metric):
    """A stateful class for updating a gauge-like integer metric.

  This class encapsulates a set of integer values (or a single value for a
  label-less metric). Each value is identified by a tuple of labels. The class
  allows the user to set each value.
  """
    def __init__(self, name, description, *labels) -> None:
        """Creates a new IntGauge.

    Args:
      name: name of the new metric.
      description: description of the new metric.
      *labels: The label list of the new metric.
    """
    def get_cell(self, *labels):
        """Retrieves the cell."""

class StringGaugeCell:
    """A single string value stored in an `StringGauge`."""
    def __init__(self, cell) -> None:
        """Creates a new StringGaugeCell.

    Args:
      cell: A c pointer of TFE_MonitoringStringGaugeCell.
    """
    def set(self, value) -> None:
        """Atomically set the value.

    Args:
      value: string value.
    """
    def value(self):
        """Retrieves the current value."""

class StringGauge(Metric):
    """A stateful class for updating a gauge-like string metric.

  This class encapsulates a set of string values (or a single value for a
  label-less metric). Each value is identified by a tuple of labels. The class
  allows the user to set each value.
  """
    def __init__(self, name, description, *labels) -> None:
        """Creates a new StringGauge.

    Args:
      name: name of the new metric.
      description: description of the new metric.
      *labels: The label list of the new metric.
    """
    def get_cell(self, *labels):
        """Retrieves the cell."""

class BoolGaugeCell:
    """A single boolean value stored in an `BoolGauge`."""
    def __init__(self, cell) -> None:
        """Creates a new BoolGaugeCell.

    Args:
      cell: A c pointer of TFE_MonitoringBoolGaugeCell.
    """
    def set(self, value) -> None:
        """Atomically set the value.

    Args:
      value: bool value.
    """
    def value(self):
        """Retrieves the current value."""

class BoolGauge(Metric):
    """A stateful class for updating a gauge-like bool metric.

  This class encapsulates a set of boolean values (or a single value for a
  label-less metric). Each value is identified by a tuple of labels. The class
  allows the user to set each value.
  """
    def __init__(self, name, description, *labels) -> None:
        """Creates a new BoolGauge.

    Args:
      name: name of the new metric.
      description: description of the new metric.
      *labels: The label list of the new metric.
    """
    def get_cell(self, *labels):
        """Retrieves the cell."""

class SamplerCell:
    """SamplerCell stores each value of a Sampler."""
    def __init__(self, cell) -> None:
        """Creates a new SamplerCell.

    Args:
      cell: A c pointer of TFE_MonitoringSamplerCell.
    """
    def add(self, value) -> None:
        """Atomically add a sample.

    Args:
      value: float value.
    """
    def value(self):
        """Retrieves the current distribution of samples.

    Returns:
      A HistogramProto describing the distribution of samples.
    """

class Buckets:
    """Bucketing strategies for the samplers."""
    buckets: Incomplete
    def __init__(self, buckets) -> None:
        """Creates a new Buckets.

    Args:
      buckets: A c pointer of TFE_MonitoringBuckets.
    """
    def __del__(self) -> None: ...

class ExponentialBuckets(Buckets):
    """Exponential bucketing strategy.

  Sets up buckets of the form:
      [-DBL_MAX, ..., scale * growth^i,
       scale * growth_factor^(i + 1), ..., DBL_MAX].
  """
    def __init__(self, scale, growth_factor, bucket_count) -> None:
        """Creates a new exponential Buckets.

    Args:
      scale: float
      growth_factor: float
      bucket_count: integer
    """

class Sampler(Metric):
    """A stateful class for updating a cumulative histogram metric.

  This class encapsulates a set of histograms (or a single histogram for a
  label-less metric) configured with a list of increasing bucket boundaries.
  Each histogram is identified by a tuple of labels. The class allows the
  user to add a sample to each histogram value.
  """
    def __init__(self, name, buckets, description, *labels) -> None:
        """Creates a new Sampler.

    Args:
      name: name of the new metric.
      buckets: bucketing strategy of the new metric.
      description: description of the new metric.
      *labels: The label list of the new metric.
    """
    def get_cell(self, *labels):
        """Retrieves the cell."""

class MonitoredTimer:
    """A context manager to measure the walltime and increment a Counter cell."""
    cell: Incomplete
    def __init__(self, cell) -> None:
        """Creates a new MonitoredTimer.

    Args:
      cell: the cell associated with the time metric that will be inremented.
    """
    t: Incomplete
    def __enter__(self): ...
    def __exit__(self, exception_type: type[BaseException] | None, exception_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def monitored_timer(cell):
    """A function decorator for adding MonitoredTimer support.

  Args:
    cell: the cell associated with the time metric that will be inremented.
  Returns:
    A decorator that measure the function runtime and increment the specified
    counter cell.
  """
