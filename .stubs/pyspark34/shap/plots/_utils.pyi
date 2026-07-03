from . import colors as colors
from .. import Explanation as Explanation
from ..utils import OpChain as OpChain
from _typeshed import Incomplete

def convert_color(color): ...
def convert_ordering(ordering, shap_values): ...
def get_sort_order(dist, clust_order, cluster_threshold, feature_order):
    """ Returns a sorted order of the values where we respect the clustering order when dist[i,j] < cluster_threshold
    """
def merge_nodes(values, partition_tree):
    """ This merges the two clustered leaf nodes with the smallest total value.
    """
def dendrogram_coords(leaf_positions, partition_tree):
    """ Returns the x and y coords of the lines of a dendrogram where the leaf order is given.

    Note that scipy can compute these coords as well, but it does not allow you to easily specify
    a specific leaf order, hence this reimplementation.
    """
def fill_internal_max_values(partition_tree, leaf_values):
    """ This fills the forth column of the partition tree matrix with the max leaf value in that cluster.
    """
def fill_counts(partition_tree) -> None:
    """ This updates the
    """
def sort_inds(partition_tree, leaf_values, pos: Incomplete | None = None, inds: Incomplete | None = None): ...
