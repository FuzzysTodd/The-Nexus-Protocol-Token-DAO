from . import colors as colors
from ..utils import hclust_ordering as hclust_ordering
from ..utils._legacy import LogitLink as LogitLink, convert_to_link as convert_to_link
from ._labels import labels as labels
from _typeshed import Incomplete

class DecisionPlotResult:
    """The optional return value of decision_plot.

    The class attributes can be used to apply the same scale and feature ordering to other decision plots.
    """
    base_value: Incomplete
    shap_values: Incomplete
    feature_names: Incomplete
    feature_idx: Incomplete
    xlim: Incomplete
    def __init__(self, base_value, shap_values, feature_names, feature_idx, xlim) -> None:
        """
        Example
        -------
        Plot two decision plots using the same feature order and x-axis.
        >>> range1, range2 = range(20), range(20, 40)
        >>> r = decision_plot(base, shap_values[range1], features[range1], return_objects=True)
        >>> decision_plot(base, shap_values[range2], features[range2], feature_order=r.feature_idx, xlim=r.xlim)

        Parameters
        ----------
        base_value : float
            The base value used in the plot. For multioutput models,
            this will be the mean of the base values. This will inherit `new_base_value` if specified.

        shap_values : numpy.ndarray
            The `shap_values` passed to decision_plot re-ordered based on `feature_order`. If SHAP interaction values
            are passed to decision_plot, `shap_values` is a 2D (matrix) representation of the interactions. See
            `feature_names` to locate the feature positions. If `new_base_value` is specified, the SHAP values are
            relative to the new base value.

        feature_names : list of str
            The feature names used in the plot in the order specified in the decision_plot parameter `feature_order`.

        feature_idx : numpy.ndarray
            The index used to order `shap_values` based on `feature_order`. This attribute can be used to specify
            identical feature ordering in multiple decision plots.

        xlim : tuple[float, float]
            The x-axis limits. This attributed can be used to specify the same x-axis in multiple decision plots.

        """

def decision(base_value, shap_values, features: Incomplete | None = None, feature_names: Incomplete | None = None, feature_order: str = 'importance', feature_display_range: Incomplete | None = None, highlight: Incomplete | None = None, link: str = 'identity', plot_color: Incomplete | None = None, axis_color: str = '#333333', y_demarc_color: str = '#333333', alpha: Incomplete | None = None, color_bar: bool = True, auto_size_plot: bool = True, title: Incomplete | None = None, xlim: Incomplete | None = None, show: bool = True, return_objects: bool = False, ignore_warnings: bool = False, new_base_value: Incomplete | None = None, legend_labels: Incomplete | None = None, legend_location: str = 'best') -> DecisionPlotResult | None:
    '''Visualize model decisions using cumulative SHAP values.

    Each plotted line explains a single model prediction. If a single prediction is plotted, feature values will be
    printed in the plot (if supplied). If multiple predictions are plotted together, feature values will not be printed.
    Plotting too many predictions together will make the plot unintelligible.

    Parameters
    ----------
    base_value : float or numpy.ndarray
        This is the reference value that the feature contributions start from. Usually, this is
        ``explainer.expected_value``.

    shap_values : numpy.ndarray
        Matrix of SHAP values (# features) or (# samples x # features) from
        ``explainer.shap_values()``. Or cube of SHAP interaction values (# samples x
        # features x # features) from ``explainer.shap_interaction_values()``.

    features : numpy.array or pandas.Series or pandas.DataFrame or numpy.ndarray or list
        Matrix of feature values (# features) or (# samples x # features). This provides the values of all the
        features and, optionally, the feature names.

    feature_names : list or numpy.ndarray
        List of feature names (# features). If ``None``, names may be derived from the
        ``features`` argument if a Pandas object is provided. Otherwise, numeric feature
        names will be generated.

    feature_order : str or None or list or numpy.ndarray
        Any of "importance" (the default), "hclust" (hierarchical clustering), ``None``,
        or a list/array of indices.

    feature_display_range: slice or range
        The slice or range of features to plot after ordering features by ``feature_order``. A step of 1 or ``None``
        will display the features in ascending order. A step of -1 will display the features in descending order. If
        ``feature_display_range=None``, ``slice(-1, -21, -1)`` is used (i.e. show the last 20 features in descending order).
        If ``shap_values`` contains interaction values, the number of features is automatically expanded to include all
        possible interactions: N(N + 1)/2 where N = ``shap_values.shape[1]``.

    highlight : Any
        Specify which observations to draw in a different line style. All numpy indexing methods are supported. For
        example, list of integer indices, or a bool array.

    link : str
        Use "identity" or "logit" to specify the transformation used for the x-axis. The "logit" link transforms
        log-odds into probabilities.

    plot_color : str or matplotlib.colors.ColorMap
        Color spectrum used to draw the plot lines. If ``str``, a registered matplotlib color name is assumed.

    axis_color : str or int
        Color used to draw plot axes.

    y_demarc_color : str or int
        Color used to draw feature demarcation lines on the y-axis.

    alpha : float
        Alpha blending value in [0, 1] used to draw plot lines.

    color_bar : bool
        Whether to draw the color bar (legend).

    auto_size_plot : bool
        Whether to automatically size the matplotlib plot to fit the number of features
        displayed. If ``False``, specify the plot size using matplotlib before calling
        this function.

    title : str
        Title of the plot.

    xlim: tuple[float, float]
        The extents of the x-axis (e.g. ``(-1.0, 1.0)``). If not specified, the limits
        are determined by the maximum/minimum predictions centered around base_value
        when ``link="identity"``. When ``link="logit"``, the x-axis extents are ``(0,
        1)`` centered at 0.5. ``xlim`` values are not transformed by the ``link``
        function. This argument is provided to simplify producing multiple plots on the
        same scale for comparison.

    show : bool
        Whether ``matplotlib.pyplot.show()`` is called before returning.
        Setting this to ``False`` allows the plot
        to be customized further after it has been created.

    return_objects : bool
        Whether to return a :obj:`DecisionPlotResult` object containing various plotting
        features. This can be used to generate multiple decision plots using the same
        feature ordering and scale.

    ignore_warnings : bool
        Plotting many data points or too many features at a time may be slow, or may create very large plots. Set
        this argument to ``True`` to override hard-coded limits that prevent plotting large amounts of data.

    new_base_value : float
        SHAP values are relative to a base value. By default, this base value is the
        expected value of the model\'s raw predictions. Use ``new_base_value`` to shift
        the base value to an arbitrary value (e.g. the cutoff point for a binary
        classification task).

    legend_labels : list of str
        List of legend labels. If ``None``, legend will not be shown.

    legend_location : str
        Legend location. Any of "best", "upper right", "upper left", "lower left", "lower right", "right",
        "center left", "center right", "lower center", "upper center", "center".

    Returns
    -------
    DecisionPlotResult or None
        Returns a :obj:`DecisionPlotResult` object if ``return_objects=True``. Returns ``None`` otherwise (the default).

    Examples
    --------

    Plot two decision plots using the same feature order and x-axis.

        >>> range1, range2 = range(20), range(20, 40)
        >>> r = decision_plot(base, shap_values[range1], features[range1], return_objects=True)
        >>> decision_plot(base, shap_values[range2], features[range2], feature_order=r.feature_idx, xlim=r.xlim)

    See more `decision plot examples here <https://shap.readthedocs.io/en/latest/example_notebooks/api_examples/plots/decision_plot.html>`_.

    '''
def multioutput_decision(base_values, shap_values, row_index, **kwargs) -> DecisionPlotResult | None:
    """Decision plot for multioutput models.

    Plots all outputs for a single observation. By default, the plotted base value will be the mean of base_values
    unless new_base_value is specified. Supports both SHAP values and SHAP interaction values.

    Parameters
    ----------
    base_values : list of float
        This is the reference value that the feature contributions start from. Use explainer.expected_value.

    shap_values : list of numpy.ndarray
        A multioutput list of SHAP matrices or SHAP cubes from explainer.shap_values() or
        explainer.shap_interaction_values(), respectively.

    row_index : int
        The integer index of the row to plot.

    **kwargs : Any
        Arguments to be passed on to decision_plot().

    Returns
    -------
    DecisionPlotResult or None
        Returns a DecisionPlotResult object if `return_objects=True`. Returns `None` otherwise (the default).
    """
