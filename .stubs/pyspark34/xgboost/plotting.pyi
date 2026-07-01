from ._typing import PathLike as PathLike
from .core import Booster as Booster
from .sklearn import XGBModel as XGBModel
from typing import Any

Axes = Any
GraphvizSource = Any

def plot_importance(booster: Booster, ax: Axes | None = None, height: float = 0.2, xlim: tuple | None = None, ylim: tuple | None = None, title: str = 'Feature importance', xlabel: str = 'F score', ylabel: str = 'Features', fmap: PathLike = '', importance_type: str = 'weight', max_num_features: int | None = None, grid: bool = True, show_values: bool = True, **kwargs: Any) -> Axes:
    '''Plot importance based on fitted trees.

    Parameters
    ----------
    booster : Booster, XGBModel or dict
        Booster or XGBModel instance, or dict taken by Booster.get_fscore()
    ax : matplotlib Axes, default None
        Target axes instance. If None, new figure and axes will be created.
    grid : bool, Turn the axes grids on or off.  Default is True (On).
    importance_type : str, default "weight"
        How the importance is calculated: either "weight", "gain", or "cover"

        * "weight" is the number of times a feature appears in a tree
        * "gain" is the average gain of splits which use the feature
        * "cover" is the average coverage of splits which use the feature
          where coverage is defined as the number of samples affected by the split
    max_num_features : int, default None
        Maximum number of top features displayed on plot. If None, all features will be displayed.
    height : float, default 0.2
        Bar height, passed to ax.barh()
    xlim : tuple, default None
        Tuple passed to axes.xlim()
    ylim : tuple, default None
        Tuple passed to axes.ylim()
    title : str, default "Feature importance"
        Axes title. To disable, pass None.
    xlabel : str, default "F score"
        X axis title label. To disable, pass None.
    ylabel : str, default "Features"
        Y axis title label. To disable, pass None.
    fmap: str or os.PathLike (optional)
        The name of feature map file.
    show_values : bool, default True
        Show values on plot. To disable, pass False.
    kwargs :
        Other keywords passed to ax.barh()

    Returns
    -------
    ax : matplotlib Axes
    '''
def to_graphviz(booster: Booster, fmap: PathLike = '', num_trees: int = 0, rankdir: str | None = None, yes_color: str | None = None, no_color: str | None = None, condition_node_params: dict | None = None, leaf_node_params: dict | None = None, **kwargs: Any) -> GraphvizSource:
    '''Convert specified tree to graphviz instance. IPython can automatically plot
    the returned graphviz instance. Otherwise, you should call .render() method
    of the returned graphviz instance.

    Parameters
    ----------
    booster : Booster, XGBModel
        Booster or XGBModel instance
    fmap: str (optional)
       The name of feature map file
    num_trees : int, default 0
        Specify the ordinal number of target tree
    rankdir : str, default "UT"
        Passed to graphviz via graph_attr
    yes_color : str, default \'#0000FF\'
        Edge color when meets the node condition.
    no_color : str, default \'#FF0000\'
        Edge color when doesn\'t meet the node condition.
    condition_node_params : dict, optional
        Condition node configuration for for graphviz.  Example:

        .. code-block:: python

            {\'shape\': \'box\',
             \'style\': \'filled,rounded\',
             \'fillcolor\': \'#78bceb\'}

    leaf_node_params : dict, optional
        Leaf node configuration for graphviz. Example:

        .. code-block:: python

            {\'shape\': \'box\',
             \'style\': \'filled\',
             \'fillcolor\': \'#e48038\'}

    \\*\\*kwargs: dict, optional
        Other keywords passed to graphviz graph_attr, e.g. ``graph [ {key} = {value} ]``

    Returns
    -------
    graph: graphviz.Source

    '''
def plot_tree(booster: Booster, fmap: PathLike = '', num_trees: int = 0, rankdir: str | None = None, ax: Axes | None = None, **kwargs: Any) -> Axes:
    '''Plot specified tree.

    Parameters
    ----------
    booster : Booster, XGBModel
        Booster or XGBModel instance
    fmap: str (optional)
       The name of feature map file
    num_trees : int, default 0
        Specify the ordinal number of target tree
    rankdir : str, default "TB"
        Passed to graphviz via graph_attr
    ax : matplotlib Axes, default None
        Target axes instance. If None, new figure and axes will be created.
    kwargs :
        Other keywords passed to to_graphviz

    Returns
    -------
    ax : matplotlib Axes

    '''
