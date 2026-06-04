from . import colors as colors
from .._explanation import Explanation as Explanation
from ..utils import approximate_interactions as approximate_interactions, convert_name as convert_name
from ..utils._general import encode_array_if_needed as encode_array_if_needed
from ._labels import labels as labels
from _typeshed import Incomplete

def scatter(shap_values, color: str = '#1E88E5', hist: bool = True, axis_color: str = '#333333', cmap=..., dot_size: int = 16, x_jitter: str = 'auto', alpha: int = 1, title: Incomplete | None = None, xmin: Incomplete | None = None, xmax: Incomplete | None = None, ymin: Incomplete | None = None, ymax: Incomplete | None = None, overlay: Incomplete | None = None, ax: Incomplete | None = None, ylabel: str = 'SHAP value', show: bool = True) -> None:
    '''Create a SHAP dependence scatter plot, colored by an interaction feature.

    Plots the value of the feature on the x-axis and the SHAP value of the same feature
    on the y-axis. This shows how the model depends on the given feature, and is like a
    richer extension of classical parital dependence plots. Vertical dispersion of the
    data points represents interaction effects. Grey ticks along the y-axis are data
    points where the feature\'s value was NaN.

    Note that if you want to change the data being displayed, you can update the
    ``shap_values.display_features`` attribute and it will then be used for plotting instead of
    ``shap_values.data``.

    Parameters
    ----------
    shap_values : shap.Explanation
        A single column of an :class:`.Explanation` object (i.e.
        ``shap_values[:,"Feature A"]``).

    color : string or shap.Explanation
        How to color the scatter plot points. This can be a fixed color string, or an
        :class:`.Explanation` object. If it is an :class:`.Explanation` object, then the
        scatter plot points are colored by the feature that seems to have the strongest
        interaction effect with the feature given by the ``shap_values`` argument. This
        is calculated using :func:`shap.utils.approximate_interactions`. If only a
        single column of an :class:`.Explanation` object is passed, then that
        feature column will be used to color the data points.

    hist : bool
        Whether to show a light histogram along the x-axis to show the density of the
        data. Note that the histogram is normalized such that if all the points were in
        a single bin, then that bin would span the full height of the plot. Defaults to
        ``True``.

    x_jitter : \'auto\' or float
        Adds random jitter to feature values by specifying a float between 0 to 1. May
        increase plot readability when a feature is discrete. By default, ``x_jitter``
        is chosen based on auto-detection of categorical features.

    alpha : float
        The transparency of the data points (between 0 and 1). This can be useful to
        show the density of the data points when using a large dataset.

    xmin : float or string
        Represents the lower bound of the plot\'s x-axis. It can be a string of the format
        "percentile(float)" to denote that percentile of the feature\'s value used on the x-axis.

    xmax : float or string
        Represents the upper bound of the plot\'s x-axis. It can be a string of the format
        "percentile(float)" to denote that percentile of the feature\'s value used on the x-axis.

    ax : matplotlib Axes object
        Optionally specify an existing matplotlib ``Axes`` object, into which the plot will be placed.
        In this case, we do not create a ``Figure``, otherwise we do.

    show : bool
        Whether ``matplotlib.pyplot.show()`` is called before returning.
        Setting this to ``False`` allows the plot
        to be customized further after it has been created.

    Examples
    --------

    See `scatter plot examples <https://shap.readthedocs.io/en/latest/example_notebooks/api_examples/plots/scatter.html>`_.

    '''
def dependence_legacy(ind, shap_values: Incomplete | None = None, features: Incomplete | None = None, feature_names: Incomplete | None = None, display_features: Incomplete | None = None, interaction_index: str = 'auto', color: str = '#1E88E5', axis_color: str = '#333333', cmap: Incomplete | None = None, dot_size: int = 16, x_jitter: int = 0, alpha: int = 1, title: Incomplete | None = None, xmin: Incomplete | None = None, xmax: Incomplete | None = None, ax: Incomplete | None = None, show: bool = True, ymin: Incomplete | None = None, ymax: Incomplete | None = None) -> None:
    ''' Create a SHAP dependence plot, colored by an interaction feature.

    Plots the value of the feature on the x-axis and the SHAP value of the same feature
    on the y-axis. This shows how the model depends on the given feature, and is like a
    richer extenstion of the classical parital dependence plots. Vertical dispersion of the
    data points represents interaction effects. Grey ticks along the y-axis are data
    points where the feature\'s value was NaN.


    Parameters
    ----------
    ind : int or string
        If this is an int it is the index of the feature to plot. If this is a string it is
        either the name of the feature to plot, or it can have the form "rank(int)" to specify
        the feature with that rank (ordered by mean absolute SHAP value over all the samples).

    shap_values : numpy.array
        Matrix of SHAP values (# samples x # features).

    features : numpy.array or pandas.DataFrame
        Matrix of feature values (# samples x # features).

    feature_names : list
        Names of the features (length # features).

    display_features : numpy.array or pandas.DataFrame
        Matrix of feature values for visual display (such as strings instead of coded values).

    interaction_index : "auto", None, int, or string
        The index of the feature used to color the plot. The name of a feature can also be passed
        as a string. If "auto" then shap.common.approximate_interactions is used to pick what
        seems to be the strongest interaction (note that to find to true stongest interaction you
        need to compute the SHAP interaction values).

    x_jitter : float (0 - 1)
        Adds random jitter to feature values. May increase plot readability when feature
        is discrete.

    alpha : float
        The transparency of the data points (between 0 and 1). This can be useful to the
        show density of the data points when using a large dataset.

    xmin : float or string
        Represents the lower bound of the plot\'s x-axis. It can be a string of the format
        "percentile(float)" to denote that percentile of the feature\'s value used on the x-axis.

    xmax : float or string
        Represents the upper bound of the plot\'s x-axis. It can be a string of the format
        "percentile(float)" to denote that percentile of the feature\'s value used on the x-axis.

    ax : matplotlib Axes object
         Optionally specify an existing matplotlib Axes object, into which the plot will be placed.
         In this case we do not create a Figure, otherwise we do.

    ymin : float
        Represents the lower bound of the plot\'s y-axis.

    ymax : float
        Represents the upper bound of the plot\'s y-axis.

    '''
