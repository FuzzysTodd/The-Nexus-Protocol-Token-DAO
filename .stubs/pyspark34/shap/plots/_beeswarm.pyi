from . import colors as colors
from .. import Explanation as Explanation
from ..utils import safe_isinstance as safe_isinstance
from ..utils._exceptions import DimensionError as DimensionError
from ._labels import labels as labels
from ._utils import convert_color as convert_color, convert_ordering as convert_ordering, get_sort_order as get_sort_order, merge_nodes as merge_nodes, sort_inds as sort_inds
from _typeshed import Incomplete

def beeswarm(shap_values, max_display: int = 10, order=..., clustering: Incomplete | None = None, cluster_threshold: float = 0.5, color: Incomplete | None = None, axis_color: str = '#333333', alpha: int = 1, show: bool = True, log_scale: bool = False, color_bar: bool = True, plot_size: str = 'auto', color_bar_label=...) -> None:
    '''Create a SHAP beeswarm plot, colored by feature values when they are provided.

    Parameters
    ----------
    shap_values : Explanation
        This is an :class:`.Explanation` object containing a matrix of SHAP values
        (# samples x # features).

    max_display : int
        How many top features to include in the plot (default is 10, or 7 for
        interaction plots).

    show : bool
        Whether ``matplotlib.pyplot.show()`` is called before returning.
        Setting this to ``False`` allows the plot
        to be customized further after it has been created.

    color_bar : bool
        Whether to draw the color bar (legend).

    plot_size : "auto" (default), float, (float, float), or None
        What size to make the plot. By default, the size is auto-scaled based on the
        number of features that are being displayed. Passing a single float will cause
        each row to be that many inches high. Passing a pair of floats will scale the
        plot by that number of inches. If ``None`` is passed, then the size of the
        current figure will be left unchanged.

    Examples
    --------

    See `beeswarm plot examples <https://shap.readthedocs.io/en/latest/example_notebooks/api_examples/plots/beeswarm.html>`_.

    '''
def shorten_text(text, length_limit): ...
def is_color_map(color) -> None: ...
def summary_legacy(shap_values, features: Incomplete | None = None, feature_names: Incomplete | None = None, max_display: Incomplete | None = None, plot_type: Incomplete | None = None, color: Incomplete | None = None, axis_color: str = '#333333', title: Incomplete | None = None, alpha: int = 1, show: bool = True, sort: bool = True, color_bar: bool = True, plot_size: str = 'auto', layered_violin_max_num_bins: int = 20, class_names: Incomplete | None = None, class_inds: Incomplete | None = None, color_bar_label=..., cmap=..., auto_size_plot: Incomplete | None = None, use_log_scale: bool = False):
    '''Create a SHAP beeswarm plot, colored by feature values when they are provided.

    Parameters
    ----------
    shap_values : numpy.array
        For single output explanations this is a matrix of SHAP values (# samples x # features).
        For multi-output explanations this is a list of such matrices of SHAP values.

    features : numpy.array or pandas.DataFrame or list
        Matrix of feature values (# samples x # features) or a feature_names list as shorthand

    feature_names : list
        Names of the features (length # features)

    max_display : int
        How many top features to include in the plot (default is 20, or 7 for interaction plots)

    plot_type : "dot" (default for single output), "bar" (default for multi-output), "violin",
        or "compact_dot".
        What type of summary plot to produce. Note that "compact_dot" is only used for
        SHAP interaction values.

    plot_size : "auto" (default), float, (float, float), or None
        What size to make the plot. By default the size is auto-scaled based on the number of
        features that are being displayed. Passing a single float will cause each row to be that
        many inches high. Passing a pair of floats will scale the plot by that
        number of inches. If None is passed then the size of the current figure will be left
        unchanged.
    '''
