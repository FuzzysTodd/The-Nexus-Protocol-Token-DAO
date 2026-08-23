from . import shared as shared
from _typeshed import Incomplete
from wandb.sklearn import calculate as calculate, utils as utils

def regressor(model, X_train, X_test, y_train, y_test, model_name: str = 'Regressor') -> None:
    '''Generates all sklearn regressor plots supported by W&B.

    The following plots are generated:
        learning curve, summary metrics, residuals plot, outlier candidates.

    Should only be called with a fitted regressor (otherwise an error is thrown).

    Arguments:
        model: (regressor) Takes in a fitted regressor.
        X_train: (arr) Training set features.
        y_train: (arr) Training set labels.
        X_test: (arr) Test set features.
        y_test: (arr) Test set labels.
        model_name: (str) Model name. Defaults to \'Regressor\'

    Returns:
        None: To see plots, go to your W&B run page then expand the \'media\' tab
            under \'auto visualizations\'.

    Example:
    ```python
    wandb.sklearn.plot_regressor(reg, X_train, X_test, y_train, y_test, "Ridge")
    ```
    '''
def outlier_candidates(regressor: Incomplete | None = None, X: Incomplete | None = None, y: Incomplete | None = None) -> None:
    """Measures a datapoint's influence on regression model via cook's distance.

    Instances with high influences could potentially be outliers.

    Should only be called with a fitted regressor (otherwise an error is thrown).

    Please note this function fits the model on the training set when called.

    Arguments:
        model: (regressor) Takes in a fitted regressor.
        X: (arr) Training set features.
        y: (arr) Training set labels.

    Returns:
        None: To see plots, go to your W&B run page then expand the 'media' tab
              under 'auto visualizations'.

    Example:
    ```python
    wandb.sklearn.plot_outlier_candidates(model, X, y)
    ```
    """
def residuals(regressor: Incomplete | None = None, X: Incomplete | None = None, y: Incomplete | None = None) -> None:
    """Measures and plots the regressor's predicted value against the residual.

    The marginal distribution of residuals is also calculated and plotted.

    Should only be called with a fitted regressor (otherwise an error is thrown).

    Please note this function fits variations of the model on the training set when called.

    Arguments:
        regressor: (regressor) Takes in a fitted regressor.
        X: (arr) Training set features.
        y: (arr) Training set labels.

    Returns:
        None: To see plots, go to your W&B run page then expand the 'media' tab
              under 'auto visualizations'.

    Example:
    ```python
    wandb.sklearn.plot_residuals(model, X, y)
    ```
    """
