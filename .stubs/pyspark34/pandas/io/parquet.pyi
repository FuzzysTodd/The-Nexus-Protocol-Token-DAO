from _typeshed import Incomplete
from pandas import DataFrame as DataFrame, get_option as get_option
from pandas._libs import lib as lib
from pandas._typing import DtypeBackend as DtypeBackend, FilePath as FilePath, ReadBuffer as ReadBuffer, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.io.common import IOHandles as IOHandles, get_handle as get_handle, is_fsspec_url as is_fsspec_url, is_url as is_url, stringify_path as stringify_path
from pandas.util._decorators import doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import check_dtype_backend as check_dtype_backend
from pandas.util.version import Version as Version
from typing import Literal

def get_engine(engine: str) -> BaseImpl:
    """return our implementation"""

class BaseImpl:
    @staticmethod
    def validate_dataframe(df: DataFrame) -> None: ...
    def write(self, df: DataFrame, path, compression, **kwargs): ...
    def read(self, path, columns: Incomplete | None = None, **kwargs) -> DataFrame: ...

class PyArrowImpl(BaseImpl):
    api: Incomplete
    def __init__(self) -> None: ...
    def write(self, df: DataFrame, path: FilePath | WriteBuffer[bytes], compression: str | None = 'snappy', index: bool | None = None, storage_options: StorageOptions = None, partition_cols: list[str] | None = None, **kwargs) -> None: ...
    def read(self, path, columns: Incomplete | None = None, use_nullable_dtypes: bool = False, dtype_backend: DtypeBackend | lib.NoDefault = ..., storage_options: StorageOptions = None, **kwargs) -> DataFrame: ...

class FastParquetImpl(BaseImpl):
    api: Incomplete
    def __init__(self) -> None: ...
    def write(self, df: DataFrame, path, compression: Literal['snappy', 'gzip', 'brotli'] | None = 'snappy', index: Incomplete | None = None, partition_cols: Incomplete | None = None, storage_options: StorageOptions = None, **kwargs) -> None: ...
    def read(self, path, columns: Incomplete | None = None, storage_options: StorageOptions = None, **kwargs) -> DataFrame: ...

def to_parquet(df: DataFrame, path: FilePath | WriteBuffer[bytes] | None = None, engine: str = 'auto', compression: str | None = 'snappy', index: bool | None = None, storage_options: StorageOptions = None, partition_cols: list[str] | None = None, **kwargs) -> bytes | None:
    """
    Write a DataFrame to the parquet format.

    Parameters
    ----------
    df : DataFrame
    path : str, path object, file-like object, or None, default None
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a binary ``write()`` function. If None, the result is
        returned as bytes. If a string, it will be used as Root Directory path
        when writing a partitioned dataset. The engine fastparquet does not
        accept file-like objects.

        .. versionchanged:: 1.2.0

    engine : {{'auto', 'pyarrow', 'fastparquet'}}, default 'auto'
        Parquet library to use. If 'auto', then the option
        ``io.parquet.engine`` is used. The default ``io.parquet.engine``
        behavior is to try 'pyarrow', falling back to 'fastparquet' if
        'pyarrow' is unavailable.
    compression : {{'snappy', 'gzip', 'brotli', 'lz4', 'zstd', None}},
        default 'snappy'. Name of the compression to use. Use ``None``
        for no compression. The supported compression methods actually
        depend on which engine is used. For 'pyarrow', 'snappy', 'gzip',
        'brotli', 'lz4', 'zstd' are all supported. For 'fastparquet',
        only 'gzip' and 'snappy' are supported.
    index : bool, default None
        If ``True``, include the dataframe's index(es) in the file output. If
        ``False``, they will not be written to the file.
        If ``None``, similar to ``True`` the dataframe's index(es)
        will be saved. However, instead of being saved as values,
        the RangeIndex will be stored as a range in the metadata so it
        doesn't require much space and is faster. Other indexes will
        be included as columns in the file output.
    partition_cols : str or list, optional, default None
        Column names by which to partition the dataset.
        Columns are partitioned in the order they are given.
        Must be None if path is not a string.
    {storage_options}

        .. versionadded:: 1.2.0

    kwargs
        Additional keyword arguments passed to the engine

    Returns
    -------
    bytes if no path argument is provided else None
    """
def read_parquet(path: FilePath | ReadBuffer[bytes], engine: str = 'auto', columns: list[str] | None = None, storage_options: StorageOptions = None, use_nullable_dtypes: bool | lib.NoDefault = ..., dtype_backend: DtypeBackend | lib.NoDefault = ..., **kwargs) -> DataFrame:
    '''
    Load a parquet object from the file path, returning a DataFrame.

    Parameters
    ----------
    path : str, path object or file-like object
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a binary ``read()`` function.
        The string could be a URL. Valid URL schemes include http, ftp, s3,
        gs, and file. For file URLs, a host is expected. A local file could be:
        ``file://localhost/path/to/table.parquet``.
        A file URL can also be a path to a directory that contains multiple
        partitioned parquet files. Both pyarrow and fastparquet support
        paths to directories as well as file URLs. A directory path could be:
        ``file://localhost/path/to/tables`` or ``s3://bucket/partition_dir``.
    engine : {{\'auto\', \'pyarrow\', \'fastparquet\'}}, default \'auto\'
        Parquet library to use. If \'auto\', then the option
        ``io.parquet.engine`` is used. The default ``io.parquet.engine``
        behavior is to try \'pyarrow\', falling back to \'fastparquet\' if
        \'pyarrow\' is unavailable.
    columns : list, default=None
        If not None, only these columns will be read from the file.

    {storage_options}

        .. versionadded:: 1.3.0

    use_nullable_dtypes : bool, default False
        If True, use dtypes that use ``pd.NA`` as missing value indicator
        for the resulting DataFrame. (only applicable for the ``pyarrow``
        engine)
        As new dtypes are added that support ``pd.NA`` in the future, the
        output with this option will change to use those dtypes.
        Note: this is an experimental option, and behaviour (e.g. additional
        support dtypes) may change without notice.

        .. deprecated:: 2.0

    dtype_backend : {{"numpy_nullable", "pyarrow"}}, defaults to NumPy backed DataFrames
        Which dtype_backend to use, e.g. whether a DataFrame should have NumPy
        arrays, nullable dtypes are used for all dtypes that have a nullable
        implementation when "numpy_nullable" is set, pyarrow is used for all
        dtypes if "pyarrow" is set.

        The dtype_backends are still experimential.

        .. versionadded:: 2.0

    **kwargs
        Any additional kwargs are passed to the engine.

    Returns
    -------
    DataFrame
    '''
