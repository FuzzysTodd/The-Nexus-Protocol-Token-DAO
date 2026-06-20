from . import colors as colors
from .. import Explanation as Explanation
from ..utils import format_value as format_value, safe_isinstance as safe_isinstance
from ._labels import labels as labels
from _typeshed import Incomplete

def waterfall(shap_values, max_display: int = 10, show: bool = True):
    """Plots an explanation of a single prediction as a waterfall plot.

    The SHAP value of a feature represents the impact of the evidence provided by that feature on the model's
    output. The waterfall plot is designed to visually display how the SHAP values (evidence) of each feature
    move the model output from our prior expectation under the background data distribution, to the final model
    prediction given the evidence of all the features.

    Features are sorted by the magnitude of their SHAP values with the smallest
    magnitude features grouped together at the bottom of the plot when the number of
    features in the models exceeds the ``max_display`` parameter.

    Parameters
    ----------
    shap_values : Explanation
        A one-dimensional :class:`.Explanation` object that contains the feature values and SHAP values to plot.

    max_display : str
        The maximum number of features to plot (default is 10).

    show : bool
        Whether ``matplotlib.pyplot.show()`` is called before returning.
        Setting this to ``False`` allows the plot to be customized further after it
        has been created.

    Examples
    --------

    See `waterfall plot examples <https://shap.readthedocs.io/en/latest/example_notebooks/api_examples/plots/waterfall.html>`_.

    """
def waterfall_legacy(expected_value, shap_values: Incomplete | None = None, features: Incomplete | None = None, feature_names: Incomplete | None = None, max_display: int = 10, show: bool = True):
    """ Plots an explanation of a single prediction as a waterfall plot.

    The SHAP value of a feature represents the impact of the evidence provided by that feature on the model's
    output. The waterfall plot is designed to visually display how the SHAP values (evidence) of each feature
    move the model output from our prior expectation under the background data distribution, to the final model
    prediction given the evidence of all the features. Features are sorted by the magnitude of their SHAP values
    with the smallest magnitude features grouped together at the bottom of the plot when the number of features
    in the models exceeds the max_display parameter.

    Parameters
    ----------
    expected_value : float
        This is the reference value that the feature contributions start from. For SHAP values it should
        be the value of explainer.expected_value.

    shap_values : numpy.array
        One dimensional array of SHAP values.

    features : numpy.array
        One dimensional array of feature values. This provides the values of all the
        features, and should be the same shape as the shap_values argument.

    feature_names : list
        List of feature names (# features).

    max_display : str
        The maximum number of features to plot.

    show : bool
        Whether matplotlib.pyplot.show() is called before returning. Setting this to False allows the plot
        to be customized further after it has been created.
    """
