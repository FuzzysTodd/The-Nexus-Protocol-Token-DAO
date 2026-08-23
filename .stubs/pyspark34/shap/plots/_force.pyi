from ..plots._force_matplotlib import draw_additive_plot as draw_additive_plot
from ..utils import hclust_ordering as hclust_ordering
from ..utils._legacy import Data as Data, DenseData as DenseData, Instance as Instance, Link as Link, Model as Model, convert_to_link as convert_to_link
from ._labels import labels as labels
from _typeshed import Incomplete

have_ipython: bool

def force(base_value, shap_values: Incomplete | None = None, features: Incomplete | None = None, feature_names: Incomplete | None = None, out_names: Incomplete | None = None, link: str = 'identity', plot_cmap: str = 'RdBu', matplotlib: bool = False, show: bool = True, figsize=(20, 3), ordering_keys: Incomplete | None = None, ordering_keys_time_format: Incomplete | None = None, text_rotation: int = 0, contribution_threshold: float = 0.05):
    '''Visualize the given SHAP values with an additive force layout.

    Parameters
    ----------
    base_value : float
        This is the reference value that the feature contributions start from.
        For SHAP values, it should be the value of ``explainer.expected_value``.

    shap_values : numpy.array
        Matrix of SHAP values (# features) or (# samples x # features). If this is a
        1D array, then a single force plot will be drawn. If it is a 2D array, then a
        stacked force plot will be drawn.

    features : numpy.array
        Matrix of feature values (# features) or (# samples x # features). This provides the values of all the
        features, and should be the same shape as the ``shap_values`` argument.

    feature_names : list
        List of feature names (# features).

    out_names : str
        The name of the output of the model (plural to support multi-output plotting in the future).

    link : "identity" or "logit"
        The transformation used when drawing the tick mark labels. Using "logit" will change log-odds numbers
        into probabilities.

    matplotlib : bool
        Whether to use the default Javascript output, or the (less developed) matplotlib output.
        Using matplotlib can be helpful in scenarios where rendering Javascript/HTML
        is inconvenient.

    contribution_threshold : float
        Controls the feature names/values that are displayed on force plot.
        Only features that the magnitude of their shap value is larger than min_perc * (sum of all abs shap values)
        will be displayed.
    '''

class Explanation:
    def __init__(self) -> None: ...

class AdditiveExplanation(Explanation):
    base_value: Incomplete
    out_value: Incomplete
    effects: Incomplete
    effects_var: Incomplete
    instance: Incomplete
    link: Incomplete
    model: Incomplete
    data: Incomplete
    def __init__(self, base_value, out_value, effects, effects_var, instance, link, model, data) -> None: ...

err_msg: str

def getjs(): ...
def initjs() -> None: ...
def save_html(out_file, plot, full_html: bool = True) -> None:
    """ Save html plots to an output file.

    Parameters
    ----------
    out_file : str or file
        Location or file to be written to.

    plot : BaseVisualizer
        Visualizer returned by :func:`shap.plots.force()`.

    full_html : boolean (default: True)
        If ``True``, writes a complete HTML document starting
        with an ``<html>`` tag. If ``False``, only script and div
        tags are included.
    """
def id_generator(size: int = 20, chars=...): ...
def ensure_not_numpy(x): ...
def verify_valid_cmap(cmap): ...
def visualize(e, plot_cmap: str = 'RdBu', matplotlib: bool = False, figsize=(20, 3), show: bool = True, ordering_keys: Incomplete | None = None, ordering_keys_time_format: Incomplete | None = None, text_rotation: int = 0, min_perc: float = 0.05): ...

class BaseVisualizer: ...

class SimpleListVisualizer(BaseVisualizer):
    data: Incomplete
    def __init__(self, e) -> None: ...
    def html(self): ...

class AdditiveForceVisualizer(BaseVisualizer):
    data: Incomplete
    def __init__(self, e, plot_cmap: str = 'RdBu') -> None: ...
    def html(self, label_margin: int = 20): ...
    def matplotlib(self, figsize, show, text_rotation, min_perc: float = 0.05): ...

class AdditiveForceArrayVisualizer(BaseVisualizer):
    data: Incomplete
    def __init__(self, arr, plot_cmap: str = 'RdBu', ordering_keys: Incomplete | None = None, ordering_keys_time_format: Incomplete | None = None) -> None: ...
    def html(self): ...
