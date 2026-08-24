from ._bitset import set_raw_bitset_from_binned_bitset as set_raw_bitset_from_binned_bitset
from .common import MonotonicConstraint as MonotonicConstraint, PREDICTOR_RECORD_DTYPE as PREDICTOR_RECORD_DTYPE, X_BITSET_INNER_DTYPE as X_BITSET_INNER_DTYPE, Y_DTYPE as Y_DTYPE
from .histogram import HistogramBuilder as HistogramBuilder
from .predictor import TreePredictor as TreePredictor
from .splitting import Splitter as Splitter
from .utils import sum_parallel as sum_parallel
from _typeshed import Incomplete

EPS: Incomplete

class TreeNode:
    """Tree Node class used in TreeGrower.

    This isn't used for prediction purposes, only for training (see
    TreePredictor).

    Parameters
    ----------
    depth : int
        The depth of the node, i.e. its distance from the root.
    sample_indices : ndarray of shape (n_samples_at_node,), dtype=np.uint
        The indices of the samples at the node.
    sum_gradients : float
        The sum of the gradients of the samples at the node.
    sum_hessians : float
        The sum of the hessians of the samples at the node.

    Attributes
    ----------
    depth : int
        The depth of the node, i.e. its distance from the root.
    sample_indices : ndarray of shape (n_samples_at_node,), dtype=np.uint
        The indices of the samples at the node.
    sum_gradients : float
        The sum of the gradients of the samples at the node.
    sum_hessians : float
        The sum of the hessians of the samples at the node.
    split_info : SplitInfo or None
        The result of the split evaluation.
    is_leaf : bool
        True if node is a leaf
    left_child : TreeNode or None
        The left child of the node. None for leaves.
    right_child : TreeNode or None
        The right child of the node. None for leaves.
    value : float or None
        The value of the leaf, as computed in finalize_leaf(). None for
        non-leaf nodes.
    partition_start : int
        start position of the node's sample_indices in splitter.partition.
    partition_stop : int
        stop position of the node's sample_indices in splitter.partition.
    allowed_features : None or ndarray, dtype=int
        Indices of features allowed to split for children.
    interaction_cst_indices : None or list of ints
        Indices of the interaction sets that have to be applied on splits of
        child nodes. The fewer sets the stronger the constraint as fewer sets
        contain fewer features.
    children_lower_bound : float
    children_upper_bound : float
    """
    split_info: Incomplete
    left_child: Incomplete
    right_child: Incomplete
    histograms: Incomplete
    partition_start: int
    partition_stop: int
    depth: Incomplete
    sample_indices: Incomplete
    n_samples: Incomplete
    sum_gradients: Incomplete
    sum_hessians: Incomplete
    value: Incomplete
    is_leaf: bool
    allowed_features: Incomplete
    interaction_cst_indices: Incomplete
    def __init__(self, depth, sample_indices, sum_gradients, sum_hessians, value: Incomplete | None = None) -> None: ...
    children_lower_bound: Incomplete
    children_upper_bound: Incomplete
    def set_children_bounds(self, lower, upper) -> None:
        """Set children values bounds to respect monotonic constraints."""
    def __lt__(self, other_node):
        """Comparison for priority queue.

        Nodes with high gain are higher priority than nodes with low gain.

        heapq.heappush only need the '<' operator.
        heapq.heappop take the smallest item first (smaller is higher
        priority).

        Parameters
        ----------
        other_node : TreeNode
            The node to compare with.
        """

class TreeGrower:
    """Tree grower class used to build a tree.

    The tree is fitted to predict the values of a Newton-Raphson step. The
    splits are considered in a best-first fashion, and the quality of a
    split is defined in splitting._split_gain.

    Parameters
    ----------
    X_binned : ndarray of shape (n_samples, n_features), dtype=np.uint8
        The binned input samples. Must be Fortran-aligned.
    gradients : ndarray of shape (n_samples,)
        The gradients of each training sample. Those are the gradients of the
        loss w.r.t the predictions, evaluated at iteration ``i - 1``.
    hessians : ndarray of shape (n_samples,)
        The hessians of each training sample. Those are the hessians of the
        loss w.r.t the predictions, evaluated at iteration ``i - 1``.
    max_leaf_nodes : int, default=None
        The maximum number of leaves for each tree. If None, there is no
        maximum limit.
    max_depth : int, default=None
        The maximum depth of each tree. The depth of a tree is the number of
        edges to go from the root to the deepest leaf.
        Depth isn't constrained by default.
    min_samples_leaf : int, default=20
        The minimum number of samples per leaf.
    min_gain_to_split : float, default=0.
        The minimum gain needed to split a node. Splits with lower gain will
        be ignored.
    n_bins : int, default=256
        The total number of bins, including the bin for missing values. Used
        to define the shape of the histograms.
    n_bins_non_missing : ndarray, dtype=np.uint32, default=None
        For each feature, gives the number of bins actually used for
        non-missing values. For features with a lot of unique values, this
        is equal to ``n_bins - 1``. If it's an int, all features are
        considered to have the same number of bins. If None, all features
        are considered to have ``n_bins - 1`` bins.
    has_missing_values : bool or ndarray, dtype=bool, default=False
        Whether each feature contains missing values (in the training data).
        If it's a bool, the same value is used for all features.
    is_categorical : ndarray of bool of shape (n_features,), default=None
        Indicates categorical features.
    monotonic_cst : array-like of int of shape (n_features,), dtype=int, default=None
        Indicates the monotonic constraint to enforce on each feature.
          - 1: monotonic increase
          - 0: no constraint
          - -1: monotonic decrease

        Read more in the :ref:`User Guide <monotonic_cst_gbdt>`.
    interaction_cst : list of sets of integers, default=None
        List of interaction constraints.
    l2_regularization : float, default=0.
        The L2 regularization parameter.
    min_hessian_to_split : float, default=1e-3
        The minimum sum of hessians needed in each node. Splits that result in
        at least one child having a sum of hessians less than
        ``min_hessian_to_split`` are discarded.
    shrinkage : float, default=1.
        The shrinkage parameter to apply to the leaves values, also known as
        learning rate.
    n_threads : int, default=None
        Number of OpenMP threads to use. `_openmp_effective_n_threads` is called
        to determine the effective number of threads use, which takes cgroups CPU
        quotes into account. See the docstring of `_openmp_effective_n_threads`
        for details.

    Attributes
    ----------
    histogram_builder : HistogramBuilder
    splitter : Splitter
    root : TreeNode
    finalized_leaves : list of TreeNode
    splittable_nodes : list of TreeNode
    missing_values_bin_idx : int
        Equals n_bins - 1
    n_categorical_splits : int
    n_features : int
    n_nodes : int
    total_find_split_time : float
        Time spent finding the best splits
    total_compute_hist_time : float
        Time spent computing histograms
    total_apply_split_time : float
        Time spent splitting nodes
    with_monotonic_cst : bool
        Whether there are monotonic constraints that apply. False iff monotonic_cst is
        None.
    """
    with_monotonic_cst: Incomplete
    histogram_builder: Incomplete
    splitter: Incomplete
    n_bins_non_missing: Incomplete
    missing_values_bin_idx: Incomplete
    max_leaf_nodes: Incomplete
    has_missing_values: Incomplete
    monotonic_cst: Incomplete
    interaction_cst: Incomplete
    is_categorical: Incomplete
    l2_regularization: Incomplete
    n_features: Incomplete
    max_depth: Incomplete
    min_samples_leaf: Incomplete
    X_binned: Incomplete
    min_gain_to_split: Incomplete
    shrinkage: Incomplete
    n_threads: Incomplete
    splittable_nodes: Incomplete
    finalized_leaves: Incomplete
    total_find_split_time: float
    total_compute_hist_time: float
    total_apply_split_time: float
    n_categorical_splits: int
    n_nodes: int
    def __init__(self, X_binned, gradients, hessians, max_leaf_nodes: Incomplete | None = None, max_depth: Incomplete | None = None, min_samples_leaf: int = 20, min_gain_to_split: float = 0.0, n_bins: int = 256, n_bins_non_missing: Incomplete | None = None, has_missing_values: bool = False, is_categorical: Incomplete | None = None, monotonic_cst: Incomplete | None = None, interaction_cst: Incomplete | None = None, l2_regularization: float = 0.0, min_hessian_to_split: float = 0.001, shrinkage: float = 1.0, n_threads: Incomplete | None = None) -> None: ...
    def grow(self) -> None:
        """Grow the tree, from root to leaves."""
    def split_next(self):
        """Split the node with highest potential gain.

        Returns
        -------
        left : TreeNode
            The resulting left child.
        right : TreeNode
            The resulting right child.
        """
    def make_predictor(self, binning_thresholds):
        """Make a TreePredictor object out of the current tree.

        Parameters
        ----------
        binning_thresholds : array-like of floats
            Corresponds to the bin_thresholds_ attribute of the BinMapper.
            For each feature, this stores:

            - the bin frontiers for continuous features
            - the unique raw category values for categorical features

        Returns
        -------
        A TreePredictor object.
        """
