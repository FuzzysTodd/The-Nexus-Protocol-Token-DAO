from . import colors as colors
from _typeshed import Incomplete

def group_difference(shap_values, group_mask, feature_names: Incomplete | None = None, xlabel: Incomplete | None = None, xmin: Incomplete | None = None, xmax: Incomplete | None = None, max_display: Incomplete | None = None, sort: bool = True, show: bool = True) -> None:
    """ This plots the difference in mean SHAP values between two groups.

    It is useful to decompose many group level metrics about the model output among the
    input features. Quantitative fairness metrics for machine learning models are
    a common example of such group level metrics.

    Parameters
    ----------
    shap_values : numpy.array
        Matrix of SHAP values (# samples x # features) or a vector of model outputs (# samples).

    group_mask : numpy.array
        A boolean mask where True represents the first group of samples and False the second.

    feature_names : list
        A list of feature names.
    """
