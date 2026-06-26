from . import colors as colors
from ..utils._exceptions import DimensionError as DimensionError
from ._labels import labels as labels
from _typeshed import Incomplete

def violin(shap_values, features: Incomplete | None = None, feature_names: Incomplete | None = None, max_display: Incomplete | None = None, plot_type: str = 'violin', color: Incomplete | None = None, axis_color: str = '#333333', title: Incomplete | None = None, alpha: int = 1, show: bool = True, sort: bool = True, color_bar: bool = True, plot_size: str = 'auto', layered_violin_max_num_bins: int = 20, class_names: Incomplete | None = None, class_inds: Incomplete | None = None, color_bar_label=..., cmap=..., auto_size_plot: Incomplete | None = None, use_log_scale: bool = False) -> None:
    '''Create a SHAP violin plot, colored by feature values when they are provided.

    Parameters
    ----------
    shap_values : Explanation, or numpy.array
        For single output explanations, this is a matrix of SHAP values (# samples x # features).

    features : numpy.array or pandas.DataFrame or list
        Matrix of feature values (# samples x # features) or a ``feature_names`` list as
        shorthand.

    feature_names : list
        Names of the features (length: # features).

    max_display : int
        How many top features to include in the plot (default is 20).

    plot_type : "violin", or "layered_violin".
        What type of summary plot to produce. A "layered_violin" plot shows the
        distribution of the SHAP values of each variable. A "violin" plot is the same,
        except with outliers drawn as scatter points.

    color_bar : bool
        Whether to draw the color bar (legend).

    show : bool
        Whether ``matplotlib.pyplot.show()`` is called before returning.
        Setting this to ``False`` allows the plot
        to be customized further after it has been created.

    plot_size : "auto" (default), float, (float, float), or None
        What size to make the plot. By default, the size is auto-scaled based on the number of
        features that are being displayed. Passing a single float will cause each row to be that
        many inches high. Passing a pair of floats will scale the plot by that
        number of inches. If ``None`` is passed, then the size of the current figure will be left
        unchanged.

    Examples
    --------

    See `violin plot examples <https://shap.readthedocs.io/en/latest/example_notebooks/api_examples/plots/violin.html>`_.

    '''
def shorten_text(text, length_limit): ...
