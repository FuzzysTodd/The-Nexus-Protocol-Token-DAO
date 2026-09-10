from _typeshed import Incomplete
from pyarrow._feather import FeatherError as FeatherError
from pyarrow.lib import Codec as Codec, Table as Table, concat_tables as concat_tables, schema as schema

class FeatherDataset:
    """
    Encapsulates details of reading a list of Feather files.

    Parameters
    ----------
    path_or_paths : List[str]
        A list of file names
    validate_schema : bool, default True
        Check that individual file schemas are all the same / compatible
    """
    paths: Incomplete
    validate_schema: Incomplete
    def __init__(self, path_or_paths, validate_schema: bool = True) -> None: ...
    schema: Incomplete
    def read_table(self, columns: Incomplete | None = None):
        """
        Read multiple feather files as a single pyarrow.Table

        Parameters
        ----------
        columns : List[str]
            Names of columns to read from the file

        Returns
        -------
        pyarrow.Table
            Content of the file as a table (of columns)
        """
    def validate_schemas(self, piece, table) -> None: ...
    def read_pandas(self, columns: Incomplete | None = None, use_threads: bool = True):
        """
        Read multiple Parquet files as a single pandas DataFrame

        Parameters
        ----------
        columns : List[str]
            Names of columns to read from the file
        use_threads : bool, default True
            Use multiple threads when converting to pandas

        Returns
        -------
        pandas.DataFrame
            Content of the file as a pandas DataFrame (of columns)
        """

def check_chunked_overflow(name, col) -> None: ...
def write_feather(df, dest, compression: Incomplete | None = None, compression_level: Incomplete | None = None, chunksize: Incomplete | None = None, version: int = 2) -> None:
    '''
    Write a pandas.DataFrame to Feather format.

    Parameters
    ----------
    df : pandas.DataFrame or pyarrow.Table
        Data to write out as Feather format.
    dest : str
        Local destination path.
    compression : string, default None
        Can be one of {"zstd", "lz4", "uncompressed"}. The default of None uses
        LZ4 for V2 files if it is available, otherwise uncompressed.
    compression_level : int, default None
        Use a compression level particular to the chosen compressor. If None
        use the default compression level
    chunksize : int, default None
        For V2 files, the internal maximum size of Arrow RecordBatch chunks
        when writing the Arrow IPC file format. None means use the default,
        which is currently 64K
    version : int, default 2
        Feather file version. Version 2 is the current. Version 1 is the more
        limited legacy format
    '''
def read_feather(source, columns: Incomplete | None = None, use_threads: bool = True, memory_map: bool = False, **kwargs):
    """
    Read a pandas.DataFrame from Feather format. To read as pyarrow.Table use
    feather.read_table.

    Parameters
    ----------
    source : str file path, or file-like object
        You can use MemoryMappedFile as source, for explicitly use memory map.
    columns : sequence, optional
        Only read a specific set of columns. If not provided, all columns are
        read.
    use_threads : bool, default True
        Whether to parallelize reading using multiple threads. If false the
        restriction is used in the conversion to Pandas as well as in the
        reading from Feather format.
    memory_map : boolean, default False
        Use memory mapping when opening file on disk, when source is a str.
    **kwargs
        Additional keyword arguments passed on to `pyarrow.Table.to_pandas`.

    Returns
    -------
    df : pandas.DataFrame
        The contents of the Feather file as a pandas.DataFrame
    """
def read_table(source, columns: Incomplete | None = None, memory_map: bool = False, use_threads: bool = True):
    """
    Read a pyarrow.Table from Feather format

    Parameters
    ----------
    source : str file path, or file-like object
        You can use MemoryMappedFile as source, for explicitly use memory map.
    columns : sequence, optional
        Only read a specific set of columns. If not provided, all columns are
        read.
    memory_map : boolean, default False
        Use memory mapping when opening file on disk, when source is a str
    use_threads : bool, default True
        Whether to parallelize reading using multiple threads.

    Returns
    -------
    table : pyarrow.Table
        The contents of the Feather file as a pyarrow.Table
    """
