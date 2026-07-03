from pandas import DataFrame as DataFrame
from pandas._libs import lib as lib
from pandas._typing import DtypeBackend as DtypeBackend
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.inference import is_list_like as is_list_like
from pandas.io.common import stringify_path as stringify_path
from pandas.util._validators import check_dtype_backend as check_dtype_backend
from pathlib import Path
from typing import Sequence

def read_spss(path: str | Path, usecols: Sequence[str] | None = None, convert_categoricals: bool = True, dtype_backend: DtypeBackend | lib.NoDefault = ...) -> DataFrame:
    '''
    Load an SPSS file from the file path, returning a DataFrame.

    Parameters
    ----------
    path : str or Path
        File path.
    usecols : list-like, optional
        Return a subset of the columns. If None, return all columns.
    convert_categoricals : bool, default is True
        Convert categorical columns into pd.Categorical.
    dtype_backend : {"numpy_nullable", "pyarrow"}, defaults to NumPy backed DataFrames
        Which dtype_backend to use, e.g. whether a DataFrame should have NumPy
        arrays, nullable dtypes are used for all dtypes that have a nullable
        implementation when "numpy_nullable" is set, pyarrow is used for all
        dtypes if "pyarrow" is set.

        The dtype_backends are still experimential.

        .. versionadded:: 2.0

    Returns
    -------
    DataFrame
    '''
