import scipy.sparse
from pandas._libs import lib as lib
from pandas._typing import IndexLabel as IndexLabel, npt as npt
from pandas.core.algorithms import factorize as factorize
from pandas.core.dtypes.missing import notna as notna
from pandas.core.indexes.api import MultiIndex as MultiIndex
from pandas.core.series import Series as Series
from typing import Iterable

def sparse_series_to_coo(ss: Series, row_levels: Iterable[int] = (0,), column_levels: Iterable[int] = (1,), sort_labels: bool = False) -> tuple[scipy.sparse.coo_matrix, list[IndexLabel], list[IndexLabel]]:
    """
    Convert a sparse Series to a scipy.sparse.coo_matrix using index
    levels row_levels, column_levels as the row and column
    labels respectively. Returns the sparse_matrix, row and column labels.
    """
def coo_to_sparse_series(A: scipy.sparse.coo_matrix, dense_index: bool = False) -> Series:
    """
    Convert a scipy.sparse.coo_matrix to a Series with type sparse.

    Parameters
    ----------
    A : scipy.sparse.coo_matrix
    dense_index : bool, default False

    Returns
    -------
    Series

    Raises
    ------
    TypeError if A is not a coo_matrix
    """
