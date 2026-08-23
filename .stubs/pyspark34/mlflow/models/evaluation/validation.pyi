from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import BAD_REQUEST as BAD_REQUEST, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.utils.annotations import deprecated as deprecated

class MetricThreshold:
    """
    This class allows you to define metric thresholds for model validation.
    Allowed thresholds are: threshold, min_absolute_change, min_relative_change.

    :param threshold: (Optional) A number representing the value threshold for the metric.

                      - If higher is better for the metric, the metric value has to be
                        >= threshold to pass validation.
                      - Otherwise, the metric value has to be <= threshold to pass the validation.

    :param min_absolute_change: (Optional) A positive number representing the minimum absolute
                                change required for candidate model to pass validation with
                                the baseline model.

                                - If higher is better for the metric, metric value has to be
                                  >= baseline model metric value + min_absolute_change
                                  to pass the validation.
                                - Otherwise, metric value has to be
                                  <= baseline model metric value - min_absolute_change
                                  to pass the validation.

    :param min_relative_change: (Optional) A floating point number between 0 and 1 representing
                                the minimum relative change (in percentage of
                                baseline model metric value) for candidate model
                                to pass the comparison with the baseline model.

                                - If higher is better for the metric, metric value has to be
                                  >= baseline model metric value * (1 + min_relative_change)
                                - Otherwise, metric value has to be
                                  <= baseline model metric value * (1 - min_relative_change)
                                - Note that if the baseline model metric value is equal to 0, the
                                  threshold falls back performing a simple verification that the
                                  candidate metric value is better than the baseline metric value,
                                  i.e. metric value >= baseline model metric value + 1e-10 if higher
                                  is better; metric value <= baseline model metric value - 1e-10 if
                                  lower is better.

    :param greater_is_better: A required boolean representing whether higher value is
                              better for the metric.

    :param higher_is_better:
        .. deprecated:: 2.3.0
            Use ``greater_is_better`` instead.

        A required boolean representing whether higher value is better for the metric.
    """
    def __init__(self, threshold: Incomplete | None = None, min_absolute_change: Incomplete | None = None, min_relative_change: Incomplete | None = None, greater_is_better: Incomplete | None = None, higher_is_better: Incomplete | None = None) -> None: ...
    @property
    def threshold(self):
        """
        Value of the threshold.
        """
    @property
    def min_absolute_change(self):
        """
        Value of the minimum absolute change required to pass model comparison with baseline model.
        """
    @property
    def min_relative_change(self):
        """
        Float value of the minimum relative change required to pass model comparison with
        baseline model.
        """
    @property
    def higher_is_better(self):
        """
        Boolean value representing whether higher value is better for the metric.
        """
    @property
    def greater_is_better(self):
        """
        Boolean value representing whether higher value is better for the metric.
        """

class MetricThresholdClassException(MlflowException):
    def __init__(self, _message, **kwargs) -> None: ...

class _MetricValidationResult:
    """
    Internal class for representing validation result per metric.
    Not user facing, used for organizing metric failures and generating failure message
    more conveniently.
    :param metric_name: String representing the metric name
    :param candidate_metric_value: value of metric for candidate model
    :param metric_threshold: :py:class: `MetricThreshold<mlflow.models.validation.MetricThreshold>`
                             The MetricThreshold for the metric.
    :param baseline_metric_value: value of metric for baseline model
    """
    missing_candidate: bool
    missing_baseline: bool
    threshold_failed: bool
    min_absolute_change_failed: bool
    min_relative_change_failed: bool
    metric_name: Incomplete
    candidate_metric_value: Incomplete
    baseline_metric_value: Incomplete
    metric_threshold: Incomplete
    def __init__(self, metric_name, candidate_metric_value, metric_threshold, baseline_metric_value: Incomplete | None = None) -> None: ...
    def is_success(self): ...

class ModelValidationFailedException(MlflowException):
    def __init__(self, message, **kwargs) -> None: ...
