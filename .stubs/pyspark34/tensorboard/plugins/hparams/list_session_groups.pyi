import dataclasses
from tensorboard.data import provider as provider
from tensorboard.plugins.hparams import api_pb2 as api_pb2, error as error, metadata as metadata, metrics as metrics

class Handler:
    """Handles a ListSessionGroups request."""
    def __init__(self, request_context, backend_context, experiment_id, request) -> None:
        """Constructor.

        Args:
          request_context: A tensorboard.context.RequestContext.
          backend_context: A backend_context.Context instance.
          experiment_id: A string, as from `plugin_util.experiment_id`.
          request: A ListSessionGroupsRequest protobuf.
        """
    def run(self):
        """Handles the request specified on construction.

        Returns:
          A ListSessionGroupsResponse object.
        """

@dataclasses.dataclass(frozen=True)
class _MetricIdentifier:
    """An identifier for a metric.

    As protobuffers are mutable we can't use MetricName directly as a dict's key.
    Instead, we represent MetricName protocol buffer as an immutable dataclass.

    Attributes:
      group: Metric group corresponding to the dataset on which the model was
        evaluated.
      tag: String tag associated with the metric.
    """
    group: str
    tag: str
    def __init__(self, group, tag) -> None: ...

class _MetricStats:
    """A simple class to hold metric stats used in calculating metric averages.

    Used in _set_avg_session_metrics(). See the comments in that function
    for more details.

    Attributes:
      total: int. The sum of the metric measurements seen so far.
      count: int. The number of largest-step measuremens seen so far.
      total_step: int. The sum of the steps at which the measurements were taken
      total_wall_time_secs: float. The sum of the wall_time_secs at
          which the measurements were taken.
    """
    total: int
    count: int
    total_step: int
    total_wall_time_secs: float
    def __init__(self) -> None: ...

@dataclasses.dataclass(frozen=True)
class _Measurement:
    """Holds a session's metric value.

    Attributes:
      metric_value: Metric value of the session.
      session_index: Index of the session in its group.
    """
    metric_value: api_pb2.MetricValue | None
    session_index: int
    def __init__(self, metric_value, session_index) -> None: ...
