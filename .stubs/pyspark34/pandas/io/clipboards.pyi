from pandas import get_option as get_option, option_context as option_context
from pandas._libs import lib as lib
from pandas._typing import DtypeBackend as DtypeBackend
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import check_dtype_backend as check_dtype_backend

def read_clipboard(sep: str = '\\s+', dtype_backend: DtypeBackend | lib.NoDefault = ..., **kwargs):
    '''
    Read text from clipboard and pass to read_csv.

    Parameters
    ----------
    sep : str, default \'\\s+\'
        A string or regex delimiter. The default of \'\\s+\' denotes
        one or more whitespace characters.

    dtype_backend : {"numpy_nullable", "pyarrow"}, defaults to NumPy backed DataFrames
        Which dtype_backend to use, e.g. whether a DataFrame should have NumPy
        arrays, nullable dtypes are used for all dtypes that have a nullable
        implementation when "numpy_nullable" is set, pyarrow is used for all
        dtypes if "pyarrow" is set.

        The dtype_backends are still experimential.

        .. versionadded:: 2.0

    **kwargs
        See read_csv for the full argument list.

    Returns
    -------
    DataFrame
        A parsed DataFrame object.
    '''
def to_clipboard(obj, excel: bool | None = True, sep: str | None = None, **kwargs) -> None:
    """
    Attempt to write text representation of object to the system clipboard
    The clipboard can be then pasted into Excel for example.

    Parameters
    ----------
    obj : the object to write to the clipboard
    excel : bool, defaults to True
            if True, use the provided separator, writing in a csv
            format for allowing easy pasting into excel.
            if False, write a string representation of the object
            to the clipboard
    sep : optional, defaults to tab
    other keywords are passed to to_csv

    Notes
    -----
    Requirements for your platform
      - Linux: xclip, or xsel (with PyQt4 modules)
      - Windows:
      - OS X:
    """
