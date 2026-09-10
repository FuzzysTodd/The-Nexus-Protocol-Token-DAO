import numpy as np
from flaml.automl.spark import F as F, psSeries as psSeries

def ps_group_counts(groups: psSeries | np.ndarray) -> np.ndarray: ...
def spark_metric_loss_score(metric_name: str, y_predict: psSeries, y_true: psSeries, sample_weight: psSeries = None, groups: psSeries = None) -> float:
    """
    Compute the loss score of a metric for spark models.

    Args:
        metric_name: str | the name of the metric.
        y_predict: psSeries | the predicted values.
        y_true: psSeries | the true values.
        sample_weight: psSeries | the sample weights. Default: None.
        groups: psSeries | the group of each row. Default: None.

    Returns:
        float | the loss score. A lower value indicates a better model.
    """
