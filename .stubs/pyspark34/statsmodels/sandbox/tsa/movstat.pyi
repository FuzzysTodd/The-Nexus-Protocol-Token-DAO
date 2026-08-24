__all__ = ['movorder', 'movmean', 'movvar', 'movmoment']

def movorder(x, order: str = 'med', windsize: int = 3, lag: str = 'lagged'):
    """moving order statistics

    Parameters
    ----------
    x : ndarray
       time series data
    order : float or 'med', 'min', 'max'
       which order statistic to calculate
    windsize : int
       window size
    lag : 'lagged', 'centered', or 'leading'
       location of window relative to current position

    Returns
    -------
    filtered array


    """
def movmean(x, windowsize: int = 3, lag: str = 'lagged'):
    """moving window mean


    Parameters
    ----------
    x : ndarray
       time series data
    windsize : int
       window size
    lag : 'lagged', 'centered', or 'leading'
       location of window relative to current position

    Returns
    -------
    mk : ndarray
        moving mean, with same shape as x


    Notes
    -----
    for leading and lagging the data array x is extended by the closest value of the array


    """
def movvar(x, windowsize: int = 3, lag: str = 'lagged'):
    """moving window variance


    Parameters
    ----------
    x : ndarray
       time series data
    windsize : int
       window size
    lag : 'lagged', 'centered', or 'leading'
       location of window relative to current position

    Returns
    -------
    mk : ndarray
        moving variance, with same shape as x


    """
def movmoment(x, k, windowsize: int = 3, lag: str = 'lagged'):
    """non-central moment


    Parameters
    ----------
    x : ndarray
       time series data
    windsize : int
       window size
    lag : 'lagged', 'centered', or 'leading'
       location of window relative to current position

    Returns
    -------
    mk : ndarray
        k-th moving non-central moment, with same shape as x


    Notes
    -----
    If data x is 2d, then moving moment is calculated for each
    column.

    """
