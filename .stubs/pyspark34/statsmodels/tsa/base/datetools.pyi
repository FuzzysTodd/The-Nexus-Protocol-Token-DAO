from _typeshed import Incomplete
from statsmodels.compat.python import asstr as asstr, lmap as lmap, lrange as lrange, lzip as lzip

def date_parser(timestr, parserinfo: Incomplete | None = None, **kwargs):
    """
    Uses dateutil.parser.parse, but also handles monthly dates of the form
    1999m4, 1999:m4, 1999:mIV, 1999mIV and the same for quarterly data
    with q instead of m. It is not case sensitive. The default for annual
    data is the end of the year, which also differs from dateutil.
    """
def date_range_str(start, end: Incomplete | None = None, length: Incomplete | None = None):
    """
    Returns a list of abbreviated date strings.

    Parameters
    ----------
    start : str
        The first abbreviated date, for instance, '1965q1' or '1965m1'
    end : str, optional
        The last abbreviated date if length is None.
    length : int, optional
        The length of the returned array of end is None.

    Returns
    -------
    date_range : list
        List of strings
    """
def dates_from_str(dates):
    """
    Turns a sequence of date strings and returns a list of datetime.

    Parameters
    ----------
    dates : array_like
        A sequence of abbreviated dates as string. For instance,
        '1996m1' or '1996Q1'. The datetime dates are at the end of the
        period.

    Returns
    -------
    date_list : ndarray
        A list of datetime types.
    """
def dates_from_range(start, end: Incomplete | None = None, length: Incomplete | None = None):
    """
    Turns a sequence of date strings and returns a list of datetime.

    Parameters
    ----------
    start : str
        The first abbreviated date, for instance, '1965q1' or '1965m1'
    end : str, optional
        The last abbreviated date if length is None.
    length : int, optional
        The length of the returned array of end is None.

    Examples
    --------
    >>> import statsmodels.api as sm
    >>> import pandas as pd
    >>> nobs = 50
    >>> dates = pd.date_range('1960m1', length=nobs)


    Returns
    -------
    date_list : ndarray
        A list of datetime types.
    """
