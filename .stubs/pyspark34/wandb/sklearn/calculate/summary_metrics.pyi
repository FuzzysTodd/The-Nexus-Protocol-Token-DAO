from _typeshed import Incomplete
from wandb.sklearn import utils as utils

def summary_metrics(model: Incomplete | None = None, X: Incomplete | None = None, y: Incomplete | None = None, X_test: Incomplete | None = None, y_test: Incomplete | None = None):
    """Calculate summary metrics for both regressors and classifiers.

    Called by plot_summary_metrics to visualize metrics. Please use the function
    plot_summary_metrics() if you wish to visualize your summary metrics.
    """
def make_table(metrics, model_name): ...
