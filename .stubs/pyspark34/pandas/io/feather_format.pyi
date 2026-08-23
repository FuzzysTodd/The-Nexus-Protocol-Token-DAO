from pandas._libs import lib as lib
from pandas._typing import DtypeBackend as DtypeBackend, FilePath as FilePath, ReadBuffer as ReadBuffer, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.api import DataFrame as DataFrame, RangeIndex as RangeIndex
from pandas.io.common import get_handle as get_handle
from pandas.util._decorators import doc as doc
from pandas.util._validators import check_dtype_backend as check_dtype_backend
from typing import Hashable, Sequence

def to_feather(df: DataFrame, path: FilePath | WriteBuffer[bytes], storage_options: StorageOptions = None, **kwargs) -> None:
    """
    Write a DataFrame to the binary Feather format.

    Parameters
    ----------
    df : DataFrame
    path : str, path object, or file-like object
    {storage_options}

        .. versionadded:: 1.2.0

    **kwargs :
        Additional keywords passed to `pyarrow.feather.write_feather`.

        .. versionadded:: 1.1.0
    """
def read_feather(path: FilePath | ReadBuffer[bytes], columns: Sequence[Hashable] | None = None, use_threads: bool = True, storage_options: StorageOptions = None, dtype_backend: DtypeBackend | lib.NoDefault = ...):
    '''
    Load a feather-format object from the file path.

    Parameters
    ----------
    path : str, path object, or file-like object
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a binary ``read()`` function. The string could be a URL.
        Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is
        expected. A local file could be: ``file://localhost/path/to/table.feather``.
    columns : sequence, default None
        If not provided, all columns are read.
    use_threads : bool, default True
        Whether to parallelize reading using multiple threads.
    {storage_options}

        .. versionadded:: 1.2.0

    dtype_backend : {{"numpy_nullable", "pyarrow"}}, defaults to NumPy backed DataFrames
        Which dtype_backend to use, e.g. whether a DataFrame should have NumPy
        arrays, nullable dtypes are used for all dtypes that have a nullable
        implementation when "numpy_nullable" is set, pyarrow is used for all
        dtypes if "pyarrow" is set.

        The dtype_backends are still experimential.

        .. versionadded:: 2.0

    Returns
    -------
    type of object stored in file
    '''
