from _typeshed import Incomplete
from statsmodels.compat.python import lrange as lrange

def webuse(data, baseurl: str = 'https://www.stata-press.com/data/r11/', as_df: bool = True):
    """
    Download and return an example dataset from Stata.

    Parameters
    ----------
    data : str
        Name of dataset to fetch.
    baseurl : str
        The base URL to the stata datasets.
    as_df : bool
        Deprecated. Always returns a DataFrame

    Returns
    -------
    dta : DataFrame
        A DataFrame containing the Stata dataset.

    Examples
    --------
    >>> dta = webuse('auto')

    Notes
    -----
    Make sure baseurl has trailing forward slash. Does not do any
    error checking in response URLs.
    """

class Dataset(dict):
    endog: Incomplete
    exog: Incomplete
    data: Incomplete
    names: Incomplete
    __dict__: Incomplete
    raw_data: Incomplete
    def __init__(self, **kw) -> None: ...

def process_pandas(data, endog_idx: int = 0, exog_idx: Incomplete | None = None, index_idx: Incomplete | None = None): ...
def get_rdataset(dataname, package: str = 'datasets', cache: bool = False):
    """download and return R dataset

    Parameters
    ----------
    dataname : str
        The name of the dataset you want to download
    package : str
        The package in which the dataset is found. The default is the core
        'datasets' package.
    cache : bool or str
        If True, will download this data into the STATSMODELS_DATA folder.
        The default location is a folder called statsmodels_data in the
        user home folder. Otherwise, you can specify a path to a folder to
        use for caching the data. If False, the data will not be cached.

    Returns
    -------
    dataset : Dataset
        A `statsmodels.data.utils.Dataset` instance. This objects has
        attributes:

        * data - A pandas DataFrame containing the data
        * title - The dataset title
        * package - The package from which the data came
        * from_cache - Whether not cached data was retrieved
        * __doc__ - The verbatim R documentation.

    Notes
    -----
    If the R dataset has an integer index. This is reset to be zero-based.
    Otherwise the index is preserved. The caching facilities are dumb. That
    is, no download dates, e-tags, or otherwise identifying information
    is checked to see if the data should be downloaded again or not. If the
    dataset is in the cache, it's used.
    """
def get_data_home(data_home: Incomplete | None = None):
    """Return the path of the statsmodels data dir.

    This folder is used by some large dataset loaders to avoid
    downloading the data several times.

    By default the data dir is set to a folder named 'statsmodels_data'
    in the user home folder.

    Alternatively, it can be set by the 'STATSMODELS_DATA' environment
    variable or programatically by giving an explicit folder path. The
    '~' symbol is expanded to the user home folder.

    If the folder does not already exist, it is automatically created.
    """
def clear_data_home(data_home: Incomplete | None = None) -> None:
    """Delete all the content of the data home cache."""
def check_internet(url: Incomplete | None = None):
    """Check if internet is available"""
def strip_column_names(df):
    """
    Remove leading and trailing single quotes

    Parameters
    ----------
    df : DataFrame
        DataFrame to process

    Returns
    -------
    df : DataFrame
        DataFrame with stripped column names

    Notes
    -----
    In-place modification
    """
def load_csv(base_file, csv_name, sep: str = ',', convert_float: bool = False):
    """Standard simple csv loader"""
