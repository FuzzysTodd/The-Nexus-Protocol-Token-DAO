from . import colors as colors
from .. import Cohorts as Cohorts, Explanation as Explanation
from ..utils import format_value as format_value, ordinal_str as ordinal_str
from ..utils._exceptions import DimensionError as DimensionError
from ._labels import labels as labels
from ._utils import convert_ordering as convert_ordering, dendrogram_coords as dendrogram_coords, get_sort_order as get_sort_order, merge_nodes as merge_nodes, sort_inds as sort_inds
from _typeshed import Incomplete

def bar(shap_values, max_display: int = 10, order=..., clustering: Incomplete | None = None, clustering_cutoff: float = 0.5, merge_cohorts: bool = False, show_data: str = 'auto', show: bool = True) -> None:
    """Create a bar plot of a set of SHAP values.

    If a single sample is passed, then we plot the SHAP values as a bar chart. If an
    :class:`.Explanation` with many samples is passed, then we plot the mean absolute
    value for each feature column as a bar chart.


    Parameters
    ----------
    shap_values : shap.Explanation or shap.Cohorts or dictionary of shap.Explanation objects
        A single row of a SHAP :class:`.Explanation` object (i.e. ``shap_values[0]``) or
        a multi-row Explanation object that we want to summarize.

    max_display : int
        How many top features to include in the bar plot (default is 10).

    show : bool
        Whether ``matplotlib.pyplot.show()`` is called before returning.
        Setting this to ``False`` allows the plot
        to be customized further after it has been created.

    Examples
    --------

    See `bar plot examples <https://shap.readthedocs.io/en/latest/example_notebooks/api_examples/plots/bar.html>`_.

    """
def bar_legacy(shap_values, features: Incomplete | None = None, feature_names: Incomplete | None = None, max_display: Incomplete | None = None, show: bool = True) -> None: ...
