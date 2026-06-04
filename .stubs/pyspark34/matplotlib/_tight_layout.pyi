from _typeshed import Incomplete
from matplotlib.font_manager import FontProperties as FontProperties
from matplotlib.transforms import Bbox as Bbox

def get_subplotspec_list(axes_list, grid_spec: Incomplete | None = None):
    """
    Return a list of subplotspec from the given list of axes.

    For an instance of axes that does not support subplotspec, None is inserted
    in the list.

    If grid_spec is given, None is inserted for those not from the given
    grid_spec.
    """
def get_tight_layout_figure(fig, axes_list, subplotspec_list, renderer, pad: float = 1.08, h_pad: Incomplete | None = None, w_pad: Incomplete | None = None, rect: Incomplete | None = None):
    """
    Return subplot parameters for tight-layouted-figure with specified padding.

    Parameters
    ----------
    fig : Figure
    axes_list : list of Axes
    subplotspec_list : list of `.SubplotSpec`
        The subplotspecs of each axes.
    renderer : renderer
    pad : float
        Padding between the figure edge and the edges of subplots, as a
        fraction of the font size.
    h_pad, w_pad : float
        Padding (height/width) between edges of adjacent subplots.  Defaults to
        *pad*.
    rect : tuple (left, bottom, right, top), default: None.
        rectangle in normalized figure coordinates
        that the whole subplots area (including labels) will fit into.
        Defaults to using the entire figure.

    Returns
    -------
    subplotspec or None
        subplotspec kwargs to be passed to `.Figure.subplots_adjust` or
        None if tight_layout could not be accomplished.
    """
