from _typeshed import Incomplete
from wandb import util as util
from wandb.plots.utils import deprecation_notice as deprecation_notice, encode_labels as encode_labels, test_missing as test_missing, test_types as test_types

chart_limit: Incomplete

def precision_recall(y_true: Incomplete | None = None, y_probas: Incomplete | None = None, labels: Incomplete | None = None, plot_micro: bool = True, classes_to_plot: Incomplete | None = None):
    """
    Computes the tradeoff between precision and recall for different thresholds.
        A high area under the curve represents both high recall and high precision,
        where high precision relates to a low false positive rate, and high recall
        relates to a low false negative rate. High scores for both show that the
        classifier is returning accurate results (high precision), as well as
        returning a majority of all positive results (high recall).
        PR curve is useful when the classes are very imbalanced.

    Arguments:
    y_true (arr): Test set labels.
    y_probas (arr): Test set predicted probabilities.
    labels (list): Named labels for target varible (y). Makes plots easier to
      read by replacing target values with corresponding index.
      For example labels= ['dog', 'cat', 'owl'] all 0s are
      replaced by 'dog', 1s by 'cat'.

    Returns:
    Nothing. To see plots, go to your W&B run page then expand the 'media' tab
    under 'auto visualizations'.

    Example:
    wandb.log({'pr': wandb.plots.precision_recall(y_true, y_probas, labels)})
    """
