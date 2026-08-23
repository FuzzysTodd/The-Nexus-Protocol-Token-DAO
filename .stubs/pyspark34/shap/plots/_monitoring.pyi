from . import colors as colors
from ._labels import labels as labels
from _typeshed import Incomplete

def truncate_text(text, max_len): ...
def monitoring(ind, shap_values, features, feature_names: Incomplete | None = None, show: bool = True) -> None:
    """ Create a SHAP monitoring plot.

    (Note this function is preliminary and subject to change!!)
    A SHAP monitoring plot is meant to display the behavior of a model
    over time. Often the shap_values given to this plot explain the loss
    of a model, so changes in a feature's impact on the model's loss over
    time can help in monitoring the model's performance.

    Parameters
    ----------
    ind : int
        Index of the feature to plot.

    shap_values : numpy.array
        Matrix of SHAP values (# samples x # features)

    features : numpy.array or pandas.DataFrame
        Matrix of feature values (# samples x # features)

    feature_names : list
        Names of the features (length # features)
    """
