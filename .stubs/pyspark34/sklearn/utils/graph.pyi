from ..metrics.pairwise import pairwise_distances as pairwise_distances
from _typeshed import Incomplete

def single_source_shortest_path_length(graph, source, *, cutoff: Incomplete | None = None):
    """Return the length of the shortest path from source to all reachable nodes.

    Parameters
    ----------
    graph : {sparse matrix, ndarray} of shape (n_nodes, n_nodes)
        Adjacency matrix of the graph. Sparse matrix of format LIL is
        preferred.

    source : int
       Start node for path.

    cutoff : int, default=None
        Depth to stop the search - only paths of length <= cutoff are returned.

    Returns
    -------
    paths : dict
        Reachable end nodes mapped to length of path from source,
        i.e. `{end: path_length}`.

    Examples
    --------
    >>> from sklearn.utils.graph import single_source_shortest_path_length
    >>> import numpy as np
    >>> graph = np.array([[ 0, 1, 0, 0],
    ...                   [ 1, 0, 1, 0],
    ...                   [ 0, 1, 0, 0],
    ...                   [ 0, 0, 0, 0]])
    >>> single_source_shortest_path_length(graph, 0)
    {0: 0, 1: 1, 2: 2}
    >>> graph = np.ones((6, 6))
    >>> sorted(single_source_shortest_path_length(graph, 2).items())
    [(0, 1), (1, 1), (2, 0), (3, 1), (4, 1), (5, 1)]
    """
