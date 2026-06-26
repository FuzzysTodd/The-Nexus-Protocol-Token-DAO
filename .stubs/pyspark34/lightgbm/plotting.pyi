import numpy as np
from .basic import Booster
from .compat import pd_DataFrame
from .sklearn import LGBMModel
from _typeshed import Incomplete
from typing import Any, Dict, List, Tuple

__all__ = ['create_tree_digraph', 'plot_importance', 'plot_metric', 'plot_split_value_histogram', 'plot_tree']

def plot_importance(booster: Booster | LGBMModel, ax: Incomplete | None = None, height: float = 0.2, xlim: Tuple[float, float] | None = None, ylim: Tuple[float, float] | None = None, title: str | None = 'Feature importance', xlabel: str | None = 'Feature importance', ylabel: str | None = 'Features', importance_type: str = 'auto', max_num_features: int | None = None, ignore_zero: bool = True, figsize: Tuple[float, float] | None = None, dpi: int | None = None, grid: bool = True, precision: int | None = 3, **kwargs: Any) -> Any:
    '''Plot model\'s feature importances.

    Parameters
    ----------
    booster : Booster or LGBMModel
        Booster or LGBMModel instance which feature importance should be plotted.
    ax : matplotlib.axes.Axes or None, optional (default=None)
        Target axes instance.
        If None, new figure and axes will be created.
    height : float, optional (default=0.2)
        Bar height, passed to ``ax.barh()``.
    xlim : tuple of 2 elements or None, optional (default=None)
        Tuple passed to ``ax.xlim()``.
    ylim : tuple of 2 elements or None, optional (default=None)
        Tuple passed to ``ax.ylim()``.
    title : str or None, optional (default="Feature importance")
        Axes title.
        If None, title is disabled.
    xlabel : str or None, optional (default="Feature importance")
        X-axis title label.
        If None, title is disabled.
        @importance_type@ placeholder can be used, and it will be replaced with the value of ``importance_type`` parameter.
    ylabel : str or None, optional (default="Features")
        Y-axis title label.
        If None, title is disabled.
    importance_type : str, optional (default="auto")
        How the importance is calculated.
        If "auto", if ``booster`` parameter is LGBMModel, ``booster.importance_type`` attribute is used; "split" otherwise.
        If "split", result contains numbers of times the feature is used in a model.
        If "gain", result contains total gains of splits which use the feature.
    max_num_features : int or None, optional (default=None)
        Max number of top features displayed on plot.
        If None or <1, all features will be displayed.
    ignore_zero : bool, optional (default=True)
        Whether to ignore features with zero importance.
    figsize : tuple of 2 elements or None, optional (default=None)
        Figure size.
    dpi : int or None, optional (default=None)
        Resolution of the figure.
    grid : bool, optional (default=True)
        Whether to add a grid for axes.
    precision : int or None, optional (default=3)
        Used to restrict the display of floating point values to a certain precision.
    **kwargs
        Other parameters passed to ``ax.barh()``.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The plot with model\'s feature importances.
    '''
def plot_split_value_histogram(booster: Booster | LGBMModel, feature: int | str, bins: int | str | None = None, ax: Incomplete | None = None, width_coef: float = 0.8, xlim: Tuple[float, float] | None = None, ylim: Tuple[float, float] | None = None, title: str | None = 'Split value histogram for feature with @index/name@ @feature@', xlabel: str | None = 'Feature split value', ylabel: str | None = 'Count', figsize: Tuple[float, float] | None = None, dpi: int | None = None, grid: bool = True, **kwargs: Any) -> Any:
    '''Plot split value histogram for the specified feature of the model.

    Parameters
    ----------
    booster : Booster or LGBMModel
        Booster or LGBMModel instance of which feature split value histogram should be plotted.
    feature : int or str
        The feature name or index the histogram is plotted for.
        If int, interpreted as index.
        If str, interpreted as name.
    bins : int, str or None, optional (default=None)
        The maximum number of bins.
        If None, the number of bins equals number of unique split values.
        If str, it should be one from the list of the supported values by ``numpy.histogram()`` function.
    ax : matplotlib.axes.Axes or None, optional (default=None)
        Target axes instance.
        If None, new figure and axes will be created.
    width_coef : float, optional (default=0.8)
        Coefficient for histogram bar width.
    xlim : tuple of 2 elements or None, optional (default=None)
        Tuple passed to ``ax.xlim()``.
    ylim : tuple of 2 elements or None, optional (default=None)
        Tuple passed to ``ax.ylim()``.
    title : str or None, optional (default="Split value histogram for feature with @index/name@ @feature@")
        Axes title.
        If None, title is disabled.
        @feature@ placeholder can be used, and it will be replaced with the value of ``feature`` parameter.
        @index/name@ placeholder can be used,
        and it will be replaced with ``index`` word in case of ``int`` type ``feature`` parameter
        or ``name`` word in case of ``str`` type ``feature`` parameter.
    xlabel : str or None, optional (default="Feature split value")
        X-axis title label.
        If None, title is disabled.
    ylabel : str or None, optional (default="Count")
        Y-axis title label.
        If None, title is disabled.
    figsize : tuple of 2 elements or None, optional (default=None)
        Figure size.
    dpi : int or None, optional (default=None)
        Resolution of the figure.
    grid : bool, optional (default=True)
        Whether to add a grid for axes.
    **kwargs
        Other parameters passed to ``ax.bar()``.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The plot with specified model\'s feature split value histogram.
    '''
def plot_metric(booster: Dict | LGBMModel, metric: str | None = None, dataset_names: List[str] | None = None, ax: Incomplete | None = None, xlim: Tuple[float, float] | None = None, ylim: Tuple[float, float] | None = None, title: str | None = 'Metric during training', xlabel: str | None = 'Iterations', ylabel: str | None = '@metric@', figsize: Tuple[float, float] | None = None, dpi: int | None = None, grid: bool = True) -> Any:
    '''Plot one metric during training.

    Parameters
    ----------
    booster : dict or LGBMModel
        Dictionary returned from ``lightgbm.train()`` or LGBMModel instance.
    metric : str or None, optional (default=None)
        The metric name to plot.
        Only one metric supported because different metrics have various scales.
        If None, first metric picked from dictionary (according to hashcode).
    dataset_names : list of str, or None, optional (default=None)
        List of the dataset names which are used to calculate metric to plot.
        If None, all datasets are used.
    ax : matplotlib.axes.Axes or None, optional (default=None)
        Target axes instance.
        If None, new figure and axes will be created.
    xlim : tuple of 2 elements or None, optional (default=None)
        Tuple passed to ``ax.xlim()``.
    ylim : tuple of 2 elements or None, optional (default=None)
        Tuple passed to ``ax.ylim()``.
    title : str or None, optional (default="Metric during training")
        Axes title.
        If None, title is disabled.
    xlabel : str or None, optional (default="Iterations")
        X-axis title label.
        If None, title is disabled.
    ylabel : str or None, optional (default="@metric@")
        Y-axis title label.
        If \'auto\', metric name is used.
        If None, title is disabled.
        @metric@ placeholder can be used, and it will be replaced with metric name.
    figsize : tuple of 2 elements or None, optional (default=None)
        Figure size.
    dpi : int or None, optional (default=None)
        Resolution of the figure.
    grid : bool, optional (default=True)
        Whether to add a grid for axes.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The plot with metric\'s history over the training.
    '''
def create_tree_digraph(booster: Booster | LGBMModel, tree_index: int = 0, show_info: List[str] | None = None, precision: int | None = 3, orientation: str = 'horizontal', example_case: np.ndarray | pd_DataFrame | None = None, max_category_values: int = 10, **kwargs: Any) -> Any:
    '''Create a digraph representation of specified tree.

    Each node in the graph represents a node in the tree.

    Non-leaf nodes have labels like ``Column_10 <= 875.9``, which means
    "this node splits on the feature named "Column_10", with threshold 875.9".

    Leaf nodes have labels like ``leaf 2: 0.422``, which means "this node is a
    leaf node, and the predicted value for records that fall into this node
    is 0.422". The number (``2``) is an internal unique identifier and doesn\'t
    have any special meaning.

    .. note::

        For more information please visit
        https://graphviz.readthedocs.io/en/stable/api.html#digraph.

    Parameters
    ----------
    booster : Booster or LGBMModel
        Booster or LGBMModel instance to be converted.
    tree_index : int, optional (default=0)
        The index of a target tree to convert.
    show_info : list of str, or None, optional (default=None)
        What information should be shown in nodes.

            - ``\'split_gain\'`` : gain from adding this split to the model
            - ``\'internal_value\'`` : raw predicted value that would be produced by this node if it was a leaf node
            - ``\'internal_count\'`` : number of records from the training data that fall into this non-leaf node
            - ``\'internal_weight\'`` : total weight of all nodes that fall into this non-leaf node
            - ``\'leaf_count\'`` : number of records from the training data that fall into this leaf node
            - ``\'leaf_weight\'`` : total weight (sum of Hessian) of all observations that fall into this leaf node
            - ``\'data_percentage\'`` : percentage of training data that fall into this node
    precision : int or None, optional (default=3)
        Used to restrict the display of floating point values to a certain precision.
    orientation : str, optional (default=\'horizontal\')
        Orientation of the tree.
        Can be \'horizontal\' or \'vertical\'.
    example_case : numpy 2-D array, pandas DataFrame or None, optional (default=None)
        Single row with the same structure as the training data.
        If not None, the plot will highlight the path that sample takes through the tree.

        .. versionadded:: 4.0.0

    max_category_values : int, optional (default=10)
        The maximum number of category values to display in tree nodes, if the number of thresholds is greater than this value, thresholds will be collapsed and displayed on the label tooltip instead.

        .. warning::

            Consider wrapping the SVG string of the tree graph with ``IPython.display.HTML`` when running on JupyterLab to get the `tooltip <https://graphviz.org/docs/attrs/tooltip>`_ working right.

            Example:

            .. code-block:: python

                from IPython.display import HTML

                graph = lgb.create_tree_digraph(clf, max_category_values=5)
                HTML(graph._repr_image_svg_xml())

        .. versionadded:: 4.0.0

    **kwargs
        Other parameters passed to ``Digraph`` constructor.
        Check https://graphviz.readthedocs.io/en/stable/api.html#digraph for the full list of supported parameters.

    Returns
    -------
    graph : graphviz.Digraph
        The digraph representation of specified tree.
    '''
def plot_tree(booster: Booster | LGBMModel, ax: Incomplete | None = None, tree_index: int = 0, figsize: Tuple[float, float] | None = None, dpi: int | None = None, show_info: List[str] | None = None, precision: int | None = 3, orientation: str = 'horizontal', example_case: np.ndarray | pd_DataFrame | None = None, **kwargs: Any) -> Any:
    '''Plot specified tree.

    Each node in the graph represents a node in the tree.

    Non-leaf nodes have labels like ``Column_10 <= 875.9``, which means
    "this node splits on the feature named "Column_10", with threshold 875.9".

    Leaf nodes have labels like ``leaf 2: 0.422``, which means "this node is a
    leaf node, and the predicted value for records that fall into this node
    is 0.422". The number (``2``) is an internal unique identifier and doesn\'t
    have any special meaning.

    .. note::

        It is preferable to use ``create_tree_digraph()`` because of its lossless quality
        and returned objects can be also rendered and displayed directly inside a Jupyter notebook.

    Parameters
    ----------
    booster : Booster or LGBMModel
        Booster or LGBMModel instance to be plotted.
    ax : matplotlib.axes.Axes or None, optional (default=None)
        Target axes instance.
        If None, new figure and axes will be created.
    tree_index : int, optional (default=0)
        The index of a target tree to plot.
    figsize : tuple of 2 elements or None, optional (default=None)
        Figure size.
    dpi : int or None, optional (default=None)
        Resolution of the figure.
    show_info : list of str, or None, optional (default=None)
        What information should be shown in nodes.

            - ``\'split_gain\'`` : gain from adding this split to the model
            - ``\'internal_value\'`` : raw predicted value that would be produced by this node if it was a leaf node
            - ``\'internal_count\'`` : number of records from the training data that fall into this non-leaf node
            - ``\'internal_weight\'`` : total weight of all nodes that fall into this non-leaf node
            - ``\'leaf_count\'`` : number of records from the training data that fall into this leaf node
            - ``\'leaf_weight\'`` : total weight (sum of Hessian) of all observations that fall into this leaf node
            - ``\'data_percentage\'`` : percentage of training data that fall into this node
    precision : int or None, optional (default=3)
        Used to restrict the display of floating point values to a certain precision.
    orientation : str, optional (default=\'horizontal\')
        Orientation of the tree.
        Can be \'horizontal\' or \'vertical\'.
    example_case : numpy 2-D array, pandas DataFrame or None, optional (default=None)
        Single row with the same structure as the training data.
        If not None, the plot will highlight the path that sample takes through the tree.

        .. versionadded:: 4.0.0

    **kwargs
        Other parameters passed to ``Digraph`` constructor.
        Check https://graphviz.readthedocs.io/en/stable/api.html#digraph for the full list of supported parameters.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The plot with single tree.
    '''
