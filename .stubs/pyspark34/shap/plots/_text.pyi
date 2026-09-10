from . import colors as colors
from _typeshed import Incomplete

have_ipython: bool

def text(shap_values, num_starting_labels: int = 0, grouping_threshold: float = 0.01, separator: str = '', xmin: Incomplete | None = None, xmax: Incomplete | None = None, cmax: Incomplete | None = None, display: bool = True):
    '''Plots an explanation of a string of text using coloring and interactive labels.

    The output is interactive HTML and you can click on any token to toggle the display of the
    SHAP value assigned to that token.

    Parameters
    ----------
    shap_values : [numpy.array]
        List of arrays of SHAP values. Each array has the shap values for a string (#input_tokens x output_tokens).

    num_starting_labels : int
        Number of tokens (sorted in descending order by corresponding SHAP values)
        that are uncovered in the initial view.
        When set to 0, all tokens are covered.

    grouping_threshold : float
        If the component substring effects are less than a ``grouping_threshold``
        fraction of an unlowered interaction effect, then we visualize the entire group
        as a single chunk. This is primarily used for explanations that were computed
        with fixed_context set to 1 or 0 when using the :class:`.explainers.Partition`
        explainer, since this causes interaction effects to be left on internal nodes
        rather than lowered.

    separator : string
        The string separator that joins tokens grouped by interaction effects and
        unbroken string spans. Defaults to the empty string ``""``.

    xmin : float
        Minimum shap value bound.

    xmax : float
        Maximum shap value bound.

    cmax : float
        Maximum absolute shap value for sample. Used for scaling colors for input tokens.

    display: bool
        Whether to display or return html to further manipulate or embed. Default: ``True``

    Examples
    --------

    See `text plot examples <https://shap.readthedocs.io/en/latest/example_notebooks/api_examples/plots/text.html>`_.

    '''
def process_shap_values(tokens, values, grouping_threshold, separator, clustering: Incomplete | None = None, return_meta_data: bool = False): ...
def svg_force_plot(values, base_values, fx, tokens, uuid, xmin, xmax, output_name): ...
def text_old(shap_values, tokens, partition_tree: Incomplete | None = None, num_starting_labels: int = 0, grouping_threshold: int = 1, separator: str = ''):
    """ Plots an explanation of a string of text using coloring and interactive labels.

    The output is interactive HTML and you can click on any token to toggle the display of the
    SHAP value assigned to that token.
    """
def text_to_text(shap_values) -> None: ...
def saliency_plot(shap_values): ...
def heatmap(shap_values): ...
def unpack_shap_explanation_contents(shap_values): ...
