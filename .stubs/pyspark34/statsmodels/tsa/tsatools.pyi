from _typeshed import Incomplete
from pandas import DataFrame
from pandas.tseries import offsets
from statsmodels.compat.python import Literal
from statsmodels.tools.typing import NDArray

__all__ = ['lagmat', 'lagmat2ds', 'add_trend', 'duplication_matrix', 'elimination_matrix', 'commutation_matrix', 'vec', 'vech', 'unvec', 'unvech', 'freq_to_period']

def add_trend(x, trend: str = 'c', prepend: bool = False, has_constant: str = 'skip'):
    """
    Add a trend and/or constant to an array.

    Parameters
    ----------
    x : array_like
        Original array of data.
    trend : str {'n', 'c', 't', 'ct', 'ctt'}
        The trend to add.

        * 'n' add no trend.
        * 'c' add constant only.
        * 't' add trend only.
        * 'ct' add constant and linear trend.
        * 'ctt' add constant and linear and quadratic trend.
    prepend : bool
        If True, prepends the new data to the columns of X.
    has_constant : str {'raise', 'add', 'skip'}
        Controls what happens when trend is 'c' and a constant column already
        exists in x. 'raise' will raise an error. 'add' will add a column of
        1s. 'skip' will return the data without change. 'skip' is the default.

    Returns
    -------
    array_like
        The original data with the additional trend columns.  If x is a
        pandas Series or DataFrame, then the trend column names are 'const',
        'trend' and 'trend_squared'.

    See Also
    --------
    statsmodels.tools.tools.add_constant
        Add a constant column to an array.

    Notes
    -----
    Returns columns as ['ctt','ct','c'] whenever applicable. There is currently
    no checking for an existing trend.
    """
def lagmat(x, maxlag: int, trim: Literal['forward', 'backward', 'both', 'none'] = 'forward', original: Literal['ex', 'sep', 'in'] = 'ex', use_pandas: bool = False) -> NDArray | DataFrame | tuple[NDArray, NDArray] | tuple[DataFrame, DataFrame]:
    '''
    Create 2d array of lags.

    Parameters
    ----------
    x : array_like
        Data; if 2d, observation in rows and variables in columns.
    maxlag : int
        All lags from zero to maxlag are included.
    trim : {\'forward\', \'backward\', \'both\', \'none\', None}
        The trimming method to use.

        * \'forward\' : trim invalid observations in front.
        * \'backward\' : trim invalid initial observations.
        * \'both\' : trim invalid observations on both sides.
        * \'none\', None : no trimming of observations.
    original : {\'ex\',\'sep\',\'in\'}
        How the original is treated.

        * \'ex\' : drops the original array returning only the lagged values.
        * \'in\' : returns the original array and the lagged values as a single
          array.
        * \'sep\' : returns a tuple (original array, lagged values). The original
                  array is truncated to have the same number of rows as
                  the returned lagmat.
    use_pandas : bool
        If true, returns a DataFrame when the input is a pandas
        Series or DataFrame.  If false, return numpy ndarrays.

    Returns
    -------
    lagmat : ndarray
        The array with lagged observations.
    y : ndarray, optional
        Only returned if original == \'sep\'.

    Notes
    -----
    When using a pandas DataFrame or Series with use_pandas=True, trim can only
    be \'forward\' or \'both\' since it is not possible to consistently extend
    index values.

    Examples
    --------
    >>> from statsmodels.tsa.tsatools import lagmat
    >>> import numpy as np
    >>> X = np.arange(1,7).reshape(-1,2)
    >>> lagmat(X, maxlag=2, trim="forward", original=\'in\')
    array([[ 1.,  2.,  0.,  0.,  0.,  0.],
       [ 3.,  4.,  1.,  2.,  0.,  0.],
       [ 5.,  6.,  3.,  4.,  1.,  2.]])

    >>> lagmat(X, maxlag=2, trim="backward", original=\'in\')
    array([[ 5.,  6.,  3.,  4.,  1.,  2.],
       [ 0.,  0.,  5.,  6.,  3.,  4.],
       [ 0.,  0.,  0.,  0.,  5.,  6.]])

    >>> lagmat(X, maxlag=2, trim="both", original=\'in\')
    array([[ 5.,  6.,  3.,  4.,  1.,  2.]])

    >>> lagmat(X, maxlag=2, trim="none", original=\'in\')
    array([[ 1.,  2.,  0.,  0.,  0.,  0.],
       [ 3.,  4.,  1.,  2.,  0.,  0.],
       [ 5.,  6.,  3.,  4.,  1.,  2.],
       [ 0.,  0.,  5.,  6.,  3.,  4.],
       [ 0.,  0.,  0.,  0.,  5.,  6.]])
    '''
def lagmat2ds(x, maxlag0, maxlagex: Incomplete | None = None, dropex: int = 0, trim: str = 'forward', use_pandas: bool = False):
    """
    Generate lagmatrix for 2d array, columns arranged by variables.

    Parameters
    ----------
    x : array_like
        Data, 2d. Observations in rows and variables in columns.
    maxlag0 : int
        The first variable all lags from zero to maxlag are included.
    maxlagex : {None, int}
        The max lag for all other variables all lags from zero to maxlag are
        included.
    dropex : int
        Exclude first dropex lags from other variables. For all variables,
        except the first, lags from dropex to maxlagex are included.
    trim : str
        The trimming method to use.

        * 'forward' : trim invalid observations in front.
        * 'backward' : trim invalid initial observations.
        * 'both' : trim invalid observations on both sides.
        * 'none' : no trimming of observations.
    use_pandas : bool
        If true, returns a DataFrame when the input is a pandas
        Series or DataFrame.  If false, return numpy ndarrays.

    Returns
    -------
    ndarray
        The array with lagged observations, columns ordered by variable.

    Notes
    -----
    Inefficient implementation for unequal lags, implemented for convenience.
    """
def vec(mat): ...
def vech(mat): ...
def unvec(v): ...
def unvech(v): ...
def duplication_matrix(n):
    """
    Create duplication matrix D_n which satisfies vec(S) = D_n vech(S) for
    symmetric matrix S

    Returns
    -------
    D_n : ndarray
    """
def elimination_matrix(n):
    """
    Create the elimination matrix L_n which satisfies vech(M) = L_n vec(M) for
    any matrix M

    Parameters
    ----------

    Returns
    -------
    """
def commutation_matrix(p, q):
    """
    Create the commutation matrix K_{p,q} satisfying vec(A') = K_{p,q} vec(A)

    Parameters
    ----------
    p : int
    q : int

    Returns
    -------
    K : ndarray (pq x pq)
    """
def freq_to_period(freq: str | offsets.DateOffset) -> int:
    """
    Convert a pandas frequency to a periodicity

    Parameters
    ----------
    freq : str or offset
        Frequency to convert

    Returns
    -------
    int
        Periodicity of freq

    Notes
    -----
    Annual maps to 1, quarterly maps to 4, monthly to 12, weekly to 52.
    """
