from _typeshed import Incomplete
from wandb.sklearn import calculate as calculate, utils as utils

def summary_metrics(model: Incomplete | None = None, X: Incomplete | None = None, y: Incomplete | None = None, X_test: Incomplete | None = None, y_test: Incomplete | None = None) -> None:
    """Logs a chart depicting summary metrics for a model.

    Should only be called with a fitted model (otherwise an error is thrown).

    Arguments:
        model: (clf or reg) Takes in a fitted regressor or classifier.
        X: (arr) Training set features.
        y: (arr) Training set labels.
        X_test: (arr) Test set features.
        y_test: (arr) Test set labels.

    Returns:
        None: To see plots, go to your W&B run page then expand the 'media' tab
              under 'auto visualizations'.

    Example:
    ```python
    wandb.sklearn.plot_summary_metrics(model, X_train, y_train, X_test, y_test)
    ```
    """
def learning_curve(model: Incomplete | None = None, X: Incomplete | None = None, y: Incomplete | None = None, cv: Incomplete | None = None, shuffle: bool = False, random_state: Incomplete | None = None, train_sizes: Incomplete | None = None, n_jobs: int = 1, scoring: Incomplete | None = None) -> None:
    """Logs a plot depicting model performance against dataset size.

    Please note this function fits the model to datasets of varying sizes when called.

    Arguments:
        model: (clf or reg) Takes in a fitted regressor or classifier.
        X: (arr) Dataset features.
        y: (arr) Dataset labels.

    For details on the other keyword arguments, see the documentation for
    `sklearn.model_selection.learning_curve`.

    Returns:
        None: To see plots, go to your W&B run page then expand the 'media' tab
              under 'auto visualizations'.

    Example:
    ```python
    wandb.sklearn.plot_learning_curve(model, X, y)
    ```
    """
