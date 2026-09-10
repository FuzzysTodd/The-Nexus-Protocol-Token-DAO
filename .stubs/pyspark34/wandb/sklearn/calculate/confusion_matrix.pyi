from _typeshed import Incomplete
from wandb.sklearn import utils as utils

def validate_labels(*args, **kwargs) -> None: ...
def confusion_matrix(y_true: Incomplete | None = None, y_pred: Incomplete | None = None, labels: Incomplete | None = None, true_labels: Incomplete | None = None, pred_labels: Incomplete | None = None, normalize: bool = False):
    """Compute the confusion matrix to evaluate the performance of a classification.

    Called by plot_confusion_matrix to visualize roc curves. Please use the function
    plot_confusion_matrix() if you wish to visualize your confusion matrix.
    """
def make_table(cm, pred_classes, true_classes, labels): ...
