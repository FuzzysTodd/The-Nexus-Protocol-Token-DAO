from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['nonisomorphic_trees', 'number_of_nonisomorphic_trees']

def nonisomorphic_trees(order, create: str = 'graph') -> Generator[Incomplete, None, None]:
    '''Returns a list of nonisomorphic trees

    Parameters
    ----------
    order : int
      order of the desired tree(s)

    create : graph or matrix (default="Graph)
      If graph is selected a list of trees will be returned,
      if matrix is selected a list of adjacency matrix will
      be returned

    Returns
    -------
    G : List of NetworkX Graphs

    M : List of Adjacency matrices

    References
    ----------

    '''
def number_of_nonisomorphic_trees(order):
    """Returns the number of nonisomorphic trees

    Parameters
    ----------
    order : int
      order of the desired tree(s)

    Returns
    -------
    length : Number of nonisomorphic graphs for the given order

    References
    ----------

    """
