from . import DecisionTreeClassifier as DecisionTreeClassifier, DecisionTreeRegressor as DecisionTreeRegressor
from ..base import is_classifier as is_classifier
from ..utils._param_validation import HasMethods as HasMethods, Interval as Interval, StrOptions as StrOptions, validate_params as validate_params
from ..utils.validation import check_array as check_array, check_is_fitted as check_is_fitted
from ._reingold_tilford import Tree as Tree, buchheim as buchheim
from _typeshed import Incomplete

class Sentinel: ...

SENTINEL: Incomplete

def plot_tree(decision_tree, *, max_depth: Incomplete | None = None, feature_names: Incomplete | None = None, class_names: Incomplete | None = None, label: str = 'all', filled: bool = False, impurity: bool = True, node_ids: bool = False, proportion: bool = False, rounded: bool = False, precision: int = 3, ax: Incomplete | None = None, fontsize: Incomplete | None = None):
    '''Plot a decision tree.

    The sample counts that are shown are weighted with any sample_weights that
    might be present.

    The visualization is fit automatically to the size of the axis.
    Use the ``figsize`` or ``dpi`` arguments of ``plt.figure``  to control
    the size of the rendering.

    Read more in the :ref:`User Guide <tree>`.

    .. versionadded:: 0.21

    Parameters
    ----------
    decision_tree : decision tree regressor or classifier
        The decision tree to be plotted.

    max_depth : int, default=None
        The maximum depth of the representation. If None, the tree is fully
        generated.

    feature_names : list of str, default=None
        Names of each of the features.
        If None, generic names will be used ("x[0]", "x[1]", ...).

    class_names : list of str or bool, default=None
        Names of each of the target classes in ascending numerical order.
        Only relevant for classification and not supported for multi-output.
        If ``True``, shows a symbolic representation of the class name.

    label : {\'all\', \'root\', \'none\'}, default=\'all\'
        Whether to show informative labels for impurity, etc.
        Options include \'all\' to show at every node, \'root\' to show only at
        the top root node, or \'none\' to not show at any node.

    filled : bool, default=False
        When set to ``True``, paint nodes to indicate majority class for
        classification, extremity of values for regression, or purity of node
        for multi-output.

    impurity : bool, default=True
        When set to ``True``, show the impurity at each node.

    node_ids : bool, default=False
        When set to ``True``, show the ID number on each node.

    proportion : bool, default=False
        When set to ``True``, change the display of \'values\' and/or \'samples\'
        to be proportions and percentages respectively.

    rounded : bool, default=False
        When set to ``True``, draw node boxes with rounded corners and use
        Helvetica fonts instead of Times-Roman.

    precision : int, default=3
        Number of digits of precision for floating point in the values of
        impurity, threshold and value attributes of each node.

    ax : matplotlib axis, default=None
        Axes to plot to. If None, use current axis. Any previous content
        is cleared.

    fontsize : int, default=None
        Size of text font. If None, determined automatically to fit figure.

    Returns
    -------
    annotations : list of artists
        List containing the artists for the annotation boxes making up the
        tree.

    Examples
    --------
    >>> from sklearn.datasets import load_iris
    >>> from sklearn import tree

    >>> clf = tree.DecisionTreeClassifier(random_state=0)
    >>> iris = load_iris()

    >>> clf = clf.fit(iris.data, iris.target)
    >>> tree.plot_tree(clf)
    [...]
    '''

class _BaseTreeExporter:
    max_depth: Incomplete
    feature_names: Incomplete
    class_names: Incomplete
    label: Incomplete
    filled: Incomplete
    impurity: Incomplete
    node_ids: Incomplete
    proportion: Incomplete
    rounded: Incomplete
    precision: Incomplete
    fontsize: Incomplete
    def __init__(self, max_depth: Incomplete | None = None, feature_names: Incomplete | None = None, class_names: Incomplete | None = None, label: str = 'all', filled: bool = False, impurity: bool = True, node_ids: bool = False, proportion: bool = False, rounded: bool = False, precision: int = 3, fontsize: Incomplete | None = None) -> None: ...
    def get_color(self, value): ...
    def get_fill_color(self, tree, node_id): ...
    def node_to_str(self, tree, node_id, criterion): ...

class _DOTTreeExporter(_BaseTreeExporter):
    leaves_parallel: Incomplete
    out_file: Incomplete
    special_characters: Incomplete
    fontname: Incomplete
    rotate: Incomplete
    characters: Incomplete
    ranks: Incomplete
    colors: Incomplete
    def __init__(self, out_file=..., max_depth: Incomplete | None = None, feature_names: Incomplete | None = None, class_names: Incomplete | None = None, label: str = 'all', filled: bool = False, leaves_parallel: bool = False, impurity: bool = True, node_ids: bool = False, proportion: bool = False, rotate: bool = False, rounded: bool = False, special_characters: bool = False, precision: int = 3, fontname: str = 'helvetica') -> None: ...
    def export(self, decision_tree) -> None: ...
    def tail(self) -> None: ...
    def head(self) -> None: ...
    def recurse(self, tree, node_id, criterion, parent: Incomplete | None = None, depth: int = 0) -> None: ...

class _MPLTreeExporter(_BaseTreeExporter):
    fontsize: Incomplete
    ranks: Incomplete
    colors: Incomplete
    characters: Incomplete
    bbox_args: Incomplete
    arrow_args: Incomplete
    def __init__(self, max_depth: Incomplete | None = None, feature_names: Incomplete | None = None, class_names: Incomplete | None = None, label: str = 'all', filled: bool = False, impurity: bool = True, node_ids: bool = False, proportion: bool = False, rounded: bool = False, precision: int = 3, fontsize: Incomplete | None = None) -> None: ...
    def export(self, decision_tree, ax: Incomplete | None = None): ...
    def recurse(self, node, tree, ax, max_x, max_y, depth: int = 0) -> None: ...

def export_graphviz(decision_tree, out_file: Incomplete | None = None, *, max_depth: Incomplete | None = None, feature_names: Incomplete | None = None, class_names: Incomplete | None = None, label: str = 'all', filled: bool = False, leaves_parallel: bool = False, impurity: bool = True, node_ids: bool = False, proportion: bool = False, rotate: bool = False, rounded: bool = False, special_characters: bool = False, precision: int = 3, fontname: str = 'helvetica'):
    '''Export a decision tree in DOT format.

    This function generates a GraphViz representation of the decision tree,
    which is then written into `out_file`. Once exported, graphical renderings
    can be generated using, for example::

        $ dot -Tps tree.dot -o tree.ps      (PostScript format)
        $ dot -Tpng tree.dot -o tree.png    (PNG format)

    The sample counts that are shown are weighted with any sample_weights that
    might be present.

    Read more in the :ref:`User Guide <tree>`.

    Parameters
    ----------
    decision_tree : object
        The decision tree estimator to be exported to GraphViz.

    out_file : object or str, default=None
        Handle or name of the output file. If ``None``, the result is
        returned as a string.

        .. versionchanged:: 0.20
            Default of out_file changed from "tree.dot" to None.

    max_depth : int, default=None
        The maximum depth of the representation. If None, the tree is fully
        generated.

    feature_names : array-like of shape (n_features,), default=None
        An array containing the feature names.
        If None, generic names will be used ("x[0]", "x[1]", ...).

    class_names : array-like of shape (n_classes,) or bool, default=None
        Names of each of the target classes in ascending numerical order.
        Only relevant for classification and not supported for multi-output.
        If ``True``, shows a symbolic representation of the class name.

    label : {\'all\', \'root\', \'none\'}, default=\'all\'
        Whether to show informative labels for impurity, etc.
        Options include \'all\' to show at every node, \'root\' to show only at
        the top root node, or \'none\' to not show at any node.

    filled : bool, default=False
        When set to ``True``, paint nodes to indicate majority class for
        classification, extremity of values for regression, or purity of node
        for multi-output.

    leaves_parallel : bool, default=False
        When set to ``True``, draw all leaf nodes at the bottom of the tree.

    impurity : bool, default=True
        When set to ``True``, show the impurity at each node.

    node_ids : bool, default=False
        When set to ``True``, show the ID number on each node.

    proportion : bool, default=False
        When set to ``True``, change the display of \'values\' and/or \'samples\'
        to be proportions and percentages respectively.

    rotate : bool, default=False
        When set to ``True``, orient tree left to right rather than top-down.

    rounded : bool, default=False
        When set to ``True``, draw node boxes with rounded corners.

    special_characters : bool, default=False
        When set to ``False``, ignore special characters for PostScript
        compatibility.

    precision : int, default=3
        Number of digits of precision for floating point in the values of
        impurity, threshold and value attributes of each node.

    fontname : str, default=\'helvetica\'
        Name of font used to render text.

    Returns
    -------
    dot_data : str
        String representation of the input tree in GraphViz dot format.
        Only returned if ``out_file`` is None.

        .. versionadded:: 0.18

    Examples
    --------
    >>> from sklearn.datasets import load_iris
    >>> from sklearn import tree

    >>> clf = tree.DecisionTreeClassifier()
    >>> iris = load_iris()

    >>> clf = clf.fit(iris.data, iris.target)
    >>> tree.export_graphviz(clf)
    \'digraph Tree {...
    '''
def export_text(decision_tree, *, feature_names: Incomplete | None = None, class_names: Incomplete | None = None, max_depth: int = 10, spacing: int = 3, decimals: int = 2, show_weights: bool = False):
    '''Build a text report showing the rules of a decision tree.

    Note that backwards compatibility may not be supported.

    Parameters
    ----------
    decision_tree : object
        The decision tree estimator to be exported.
        It can be an instance of
        DecisionTreeClassifier or DecisionTreeRegressor.

    feature_names : array-like of shape (n_features,), default=None
        An array containing the feature names.
        If None generic names will be used ("feature_0", "feature_1", ...).

    class_names : array-like of shape (n_classes,), default=None
        Names of each of the target classes in ascending numerical order.
        Only relevant for classification and not supported for multi-output.

        - if `None`, the class names are delegated to `decision_tree.classes_`;
        - otherwise, `class_names` will be used as class names instead of
          `decision_tree.classes_`. The length of `class_names` must match
          the length of `decision_tree.classes_`.

        .. versionadded:: 1.3

    max_depth : int, default=10
        Only the first max_depth levels of the tree are exported.
        Truncated branches will be marked with "...".

    spacing : int, default=3
        Number of spaces between edges. The higher it is, the wider the result.

    decimals : int, default=2
        Number of decimal digits to display.

    show_weights : bool, default=False
        If true the classification weights will be exported on each leaf.
        The classification weights are the number of samples each class.

    Returns
    -------
    report : str
        Text summary of all the rules in the decision tree.

    Examples
    --------

    >>> from sklearn.datasets import load_iris
    >>> from sklearn.tree import DecisionTreeClassifier
    >>> from sklearn.tree import export_text
    >>> iris = load_iris()
    >>> X = iris[\'data\']
    >>> y = iris[\'target\']
    >>> decision_tree = DecisionTreeClassifier(random_state=0, max_depth=2)
    >>> decision_tree = decision_tree.fit(X, y)
    >>> r = export_text(decision_tree, feature_names=iris[\'feature_names\'])
    >>> print(r)
    |--- petal width (cm) <= 0.80
    |   |--- class: 0
    |--- petal width (cm) >  0.80
    |   |--- petal width (cm) <= 1.75
    |   |   |--- class: 1
    |   |--- petal width (cm) >  1.75
    |   |   |--- class: 2
    '''
