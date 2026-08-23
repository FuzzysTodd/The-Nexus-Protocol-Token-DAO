from ._general import safe_isinstance as safe_isinstance
from ._show_progress import show_progress as show_progress
from _typeshed import Incomplete

def partition_tree(X, metric: str = 'correlation'): ...
def partition_tree_shuffle(indexes, index_mask, partition_tree) -> None:
    """ Randomly shuffle the indexes in a way that is consistent with the given partition tree.

    Parameters
    ----------
    indexes: np.array
        The output location of the indexes we want shuffled. Note that len(indexes) should equal index_mask.sum().

    index_mask: np.array
        A bool mask of which indexes we want to include in the shuffled list.

    partition_tree: np.array
        The partition tree we should follow.
    """
def delta_minimization_order(all_masks, max_swap_size: int = 100, num_passes: int = 2): ...
def hclust_ordering(X, metric: str = 'sqeuclidean', anchor_first: bool = False):
    """ A leaf ordering is under-defined, this picks the ordering that keeps nearby samples similar.
    """
def xgboost_distances_r2(X, y, learning_rate: float = 0.6, early_stopping_rounds: int = 2, subsample: int = 1, max_estimators: int = 10000, random_state: int = 0):
    """ Compute reducancy distances scaled from 0-1 amoung all the feature in X relative to the label y.

    Distances are measured by training univariate XGBoost models of y for all the features, and then
    predicting the output of these models using univariate XGBoost models of other features. If one
    feature can effectively predict the output of another feature's univariate XGBoost model of y,
    then the second feature is redundant with the first with respect to y. A distance of 1 corresponds
    to no redundancy while a distance of 0 corresponds to perfect redundancy (measured using the
    proportion of variance explained). Note these distances are not symmetric.
    """
def hclust(X, y: Incomplete | None = None, linkage: str = 'single', metric: str = 'auto', random_state: int = 0): ...
