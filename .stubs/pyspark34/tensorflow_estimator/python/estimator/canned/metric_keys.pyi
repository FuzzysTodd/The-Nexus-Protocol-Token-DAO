from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import model_fn as model_fn

class MetricKeys:
    """Metric key strings."""
    LOSS: Incomplete
    LOSS_MEAN: Incomplete
    LOSS_REGULARIZATION: str
    ACCURACY: str
    PRECISION: str
    RECALL: str
    ACCURACY_BASELINE: str
    AUC: str
    AUC_PR: str
    LABEL_MEAN: str
    PREDICTION_MEAN: str
    ACCURACY_AT_THRESHOLD: str
    PRECISION_AT_THRESHOLD: str
    RECALL_AT_THRESHOLD: str
    PRECISION_AT_RECALL: str
    RECALL_AT_PRECISION: str
    SENSITIVITY_AT_SPECIFICITY: str
    SPECIFICITY_AT_SENSITIVITY: str
    PROBABILITY_MEAN_AT_CLASS: str
    AUC_AT_CLASS: str
    AUC_PR_AT_CLASS: str
    PROBABILITY_MEAN_AT_NAME: str
    AUC_AT_NAME: str
    AUC_PR_AT_NAME: str
