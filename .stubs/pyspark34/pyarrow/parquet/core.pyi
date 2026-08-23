from _typeshed import Incomplete
from pyarrow._parquet import ColumnChunkMetaData as ColumnChunkMetaData, ColumnSchema as ColumnSchema, FileDecryptionProperties as FileDecryptionProperties, FileEncryptionProperties as FileEncryptionProperties, FileMetaData as FileMetaData, ParquetLogicalType as ParquetLogicalType, ParquetReader as ParquetReader, ParquetSchema as ParquetSchema, RowGroupMetaData as RowGroupMetaData, Statistics as Statistics

__all__ = ['ColumnChunkMetaData', 'ColumnSchema', 'FileDecryptionProperties', 'FileEncryptionProperties', 'FileMetaData', 'ParquetDataset', 'ParquetDatasetPiece', 'ParquetFile', 'ParquetLogicalType', 'ParquetManifest', 'ParquetPartitions', 'ParquetReader', 'ParquetSchema', 'ParquetWriter', 'PartitionSet', 'RowGroupMetaData', 'Statistics', 'read_metadata', 'read_pandas', 'read_schema', 'read_table', 'write_metadata', 'write_table', 'write_to_dataset', '_filters_to_expression', 'filters_to_expression']

def filters_to_expression(filters):
    '''
    Check if filters are well-formed and convert to an ``Expression``.

    Parameters
    ----------
    filters : List[Tuple] or List[List[Tuple]]

    Notes
    -----
    See internal ``pyarrow._DNF_filter_doc`` attribute for more details.

    Examples
    --------

    >>> filters_to_expression([(\'foo\', \'==\', \'bar\')])
    <pyarrow.compute.Expression (foo == "bar")>

    Returns
    -------
    pyarrow.compute.Expression
        An Expression representing the filters
    '''

_filters_to_expression: Incomplete

class ParquetFile:
    '''
    Reader interface for a single Parquet file.

    Parameters
    ----------
    source : str, pathlib.Path, pyarrow.NativeFile, or file-like object
        Readable source. For passing bytes or buffer-like file containing a
        Parquet file, use pyarrow.BufferReader.
    metadata : FileMetaData, default None
        Use existing metadata object, rather than reading from file.
    common_metadata : FileMetaData, default None
        Will be used in reads for pandas schema metadata if not found in the
        main file\'s metadata, no other uses at the moment.
    read_dictionary : list
        List of column names to read directly as DictionaryArray.
    memory_map : bool, default False
        If the source is a file path, use a memory map to read file, which can
        improve performance in some environments.
    buffer_size : int, default 0
        If positive, perform read buffering when deserializing individual
        column chunks. Otherwise IO calls are unbuffered.
    pre_buffer : bool, default False
        Coalesce and issue file reads in parallel to improve performance on
        high-latency filesystems (e.g. S3). If True, Arrow will use a
        background I/O thread pool.
    coerce_int96_timestamp_unit : str, default None
        Cast timestamps that are stored in INT96 format to a particular
        resolution (e.g. \'ms\'). Setting to None is equivalent to \'ns\'
        and therefore INT96 timestamps will be inferred as timestamps
        in nanoseconds.
    decryption_properties : FileDecryptionProperties, default None
        File decryption properties for Parquet Modular Encryption.
    thrift_string_size_limit : int, default None
        If not None, override the maximum total string size allocated
        when decoding Thrift structures. The default limit should be
        sufficient for most Parquet files.
    thrift_container_size_limit : int, default None
        If not None, override the maximum total size of containers allocated
        when decoding Thrift structures. The default limit should be
        sufficient for most Parquet files.
    filesystem : FileSystem, default None
        If nothing passed, will be inferred based on path.
        Path will try to be found in the local on-disk filesystem otherwise
        it will be parsed as an URI to determine the filesystem.

    Examples
    --------

    Generate an example PyArrow Table and write it to Parquet file:

    >>> import pyarrow as pa
    >>> table = pa.table({\'n_legs\': [2, 2, 4, 4, 5, 100],
    ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
    ...                              "Brittle stars", "Centipede"]})

    >>> import pyarrow.parquet as pq
    >>> pq.write_table(table, \'example.parquet\')

    Create a ``ParquetFile`` object from the Parquet file:

    >>> parquet_file = pq.ParquetFile(\'example.parquet\')

    Read the data:

    >>> parquet_file.read()
    pyarrow.Table
    n_legs: int64
    animal: string
    ----
    n_legs: [[2,2,4,4,5,100]]
    animal: [["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]]

    Create a ParquetFile object with "animal" column as DictionaryArray:

    >>> parquet_file = pq.ParquetFile(\'example.parquet\',
    ...                               read_dictionary=["animal"])
    >>> parquet_file.read()
    pyarrow.Table
    n_legs: int64
    animal: dictionary<values=string, indices=int32, ordered=0>
    ----
    n_legs: [[2,2,4,4,5,100]]
    animal: [  -- dictionary:
    ["Flamingo","Parrot",...,"Brittle stars","Centipede"]  -- indices:
    [0,1,2,3,4,5]]
    '''
    reader: Incomplete
    common_metadata: Incomplete
    def __init__(self, source, *, metadata: Incomplete | None = None, common_metadata: Incomplete | None = None, read_dictionary: Incomplete | None = None, memory_map: bool = False, buffer_size: int = 0, pre_buffer: bool = False, coerce_int96_timestamp_unit: Incomplete | None = None, decryption_properties: Incomplete | None = None, thrift_string_size_limit: Incomplete | None = None, thrift_container_size_limit: Incomplete | None = None, filesystem: Incomplete | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args, **kwargs) -> None: ...
    @property
    def metadata(self):
        """
        Return the Parquet metadata.
        """
    @property
    def schema(self):
        """
        Return the Parquet schema, unconverted to Arrow types
        """
    @property
    def schema_arrow(self):
        '''
        Return the inferred Arrow schema, converted from the whole Parquet
        file\'s schema

        Examples
        --------
        Generate an example Parquet file:

        >>> import pyarrow as pa
        >>> table = pa.table({\'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_table(table, \'example.parquet\')
        >>> parquet_file = pq.ParquetFile(\'example.parquet\')

        Read the Arrow schema:

        >>> parquet_file.schema_arrow
        n_legs: int64
        animal: string
        '''
    @property
    def num_row_groups(self):
        '''
        Return the number of row groups of the Parquet file.

        Examples
        --------
        >>> import pyarrow as pa
        >>> table = pa.table({\'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_table(table, \'example.parquet\')
        >>> parquet_file = pq.ParquetFile(\'example.parquet\')

        >>> parquet_file.num_row_groups
        1
        '''
    def close(self, force: bool = False): ...
    @property
    def closed(self) -> bool: ...
    def read_row_group(self, i, columns: Incomplete | None = None, use_threads: bool = True, use_pandas_metadata: bool = False):
        '''
        Read a single row group from a Parquet file.

        Parameters
        ----------
        i : int
            Index of the individual row group that we want to read.
        columns : list
            If not None, only these columns will be read from the row group. A
            column name may be a prefix of a nested field, e.g. \'a\' will select
            \'a.b\', \'a.c\', and \'a.d.e\'.
        use_threads : bool, default True
            Perform multi-threaded column reads.
        use_pandas_metadata : bool, default False
            If True and file has custom pandas schema metadata, ensure that
            index columns are also loaded.

        Returns
        -------
        pyarrow.table.Table
            Content of the row group as a table (of columns)

        Examples
        --------
        >>> import pyarrow as pa
        >>> table = pa.table({\'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_table(table, \'example.parquet\')
        >>> parquet_file = pq.ParquetFile(\'example.parquet\')

        >>> parquet_file.read_row_group(0)
        pyarrow.Table
        n_legs: int64
        animal: string
        ----
        n_legs: [[2,2,4,4,5,100]]
        animal: [["Flamingo","Parrot",...,"Brittle stars","Centipede"]]
        '''
    def read_row_groups(self, row_groups, columns: Incomplete | None = None, use_threads: bool = True, use_pandas_metadata: bool = False):
        '''
        Read a multiple row groups from a Parquet file.

        Parameters
        ----------
        row_groups : list
            Only these row groups will be read from the file.
        columns : list
            If not None, only these columns will be read from the row group. A
            column name may be a prefix of a nested field, e.g. \'a\' will select
            \'a.b\', \'a.c\', and \'a.d.e\'.
        use_threads : bool, default True
            Perform multi-threaded column reads.
        use_pandas_metadata : bool, default False
            If True and file has custom pandas schema metadata, ensure that
            index columns are also loaded.

        Returns
        -------
        pyarrow.table.Table
            Content of the row groups as a table (of columns).

        Examples
        --------
        >>> import pyarrow as pa
        >>> table = pa.table({\'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_table(table, \'example.parquet\')
        >>> parquet_file = pq.ParquetFile(\'example.parquet\')

        >>> parquet_file.read_row_groups([0,0])
        pyarrow.Table
        n_legs: int64
        animal: string
        ----
        n_legs: [[2,2,4,4,5,...,2,4,4,5,100]]
        animal: [["Flamingo","Parrot","Dog",...,"Brittle stars","Centipede"]]
        '''
    def iter_batches(self, batch_size: int = 65536, row_groups: Incomplete | None = None, columns: Incomplete | None = None, use_threads: bool = True, use_pandas_metadata: bool = False):
        '''
        Read streaming batches from a Parquet file.

        Parameters
        ----------
        batch_size : int, default 64K
            Maximum number of records to yield per batch. Batches may be
            smaller if there aren\'t enough rows in the file.
        row_groups : list
            Only these row groups will be read from the file.
        columns : list
            If not None, only these columns will be read from the file. A
            column name may be a prefix of a nested field, e.g. \'a\' will select
            \'a.b\', \'a.c\', and \'a.d.e\'.
        use_threads : boolean, default True
            Perform multi-threaded column reads.
        use_pandas_metadata : boolean, default False
            If True and file has custom pandas schema metadata, ensure that
            index columns are also loaded.

        Yields
        ------
        pyarrow.RecordBatch
            Contents of each batch as a record batch

        Examples
        --------
        Generate an example Parquet file:

        >>> import pyarrow as pa
        >>> table = pa.table({\'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_table(table, \'example.parquet\')
        >>> parquet_file = pq.ParquetFile(\'example.parquet\')
        >>> for i in parquet_file.iter_batches():
        ...     print("RecordBatch")
        ...     print(i.to_pandas())
        ...
        RecordBatch
           n_legs         animal
        0       2       Flamingo
        1       2         Parrot
        2       4            Dog
        3       4          Horse
        4       5  Brittle stars
        5     100      Centipede
        '''
    def read(self, columns: Incomplete | None = None, use_threads: bool = True, use_pandas_metadata: bool = False):
        '''
        Read a Table from Parquet format.

        Parameters
        ----------
        columns : list
            If not None, only these columns will be read from the file. A
            column name may be a prefix of a nested field, e.g. \'a\' will select
            \'a.b\', \'a.c\', and \'a.d.e\'.
        use_threads : bool, default True
            Perform multi-threaded column reads.
        use_pandas_metadata : bool, default False
            If True and file has custom pandas schema metadata, ensure that
            index columns are also loaded.

        Returns
        -------
        pyarrow.table.Table
            Content of the file as a table (of columns).

        Examples
        --------
        Generate an example Parquet file:

        >>> import pyarrow as pa
        >>> table = pa.table({\'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_table(table, \'example.parquet\')
        >>> parquet_file = pq.ParquetFile(\'example.parquet\')

        Read a Table:

        >>> parquet_file.read(columns=["animal"])
        pyarrow.Table
        animal: string
        ----
        animal: [["Flamingo","Parrot",...,"Brittle stars","Centipede"]]
        '''
    def scan_contents(self, columns: Incomplete | None = None, batch_size: int = 65536):
        '''
        Read contents of file for the given columns and batch size.

        Notes
        -----
        This function\'s primary purpose is benchmarking.
        The scan is executed on a single thread.

        Parameters
        ----------
        columns : list of integers, default None
            Select columns to read, if None scan all columns.
        batch_size : int, default 64K
            Number of rows to read at a time internally.

        Returns
        -------
        num_rows : int
            Number of rows in file

        Examples
        --------
        >>> import pyarrow as pa
        >>> table = pa.table({\'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_table(table, \'example.parquet\')
        >>> parquet_file = pq.ParquetFile(\'example.parquet\')

        >>> parquet_file.scan_contents()
        6
        '''

class ParquetWriter:
    __doc__: Incomplete
    flavor: Incomplete
    schema_changed: bool
    schema: Incomplete
    where: Incomplete
    file_handle: Incomplete
    writer: Incomplete
    is_open: bool
    def __init__(self, where, schema, filesystem: Incomplete | None = None, flavor: Incomplete | None = None, version: str = '2.4', use_dictionary: bool = True, compression: str = 'snappy', write_statistics: bool = True, use_deprecated_int96_timestamps: Incomplete | None = None, compression_level: Incomplete | None = None, use_byte_stream_split: bool = False, column_encoding: Incomplete | None = None, writer_engine_version: Incomplete | None = None, data_page_version: str = '1.0', use_compliant_nested_type: bool = False, encryption_properties: Incomplete | None = None, write_batch_size: Incomplete | None = None, dictionary_pagesize_limit: Incomplete | None = None, store_schema: bool = True, **options) -> None: ...
    def __del__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args, **kwargs): ...
    def write(self, table_or_batch, row_group_size: Incomplete | None = None) -> None:
        """
        Write RecordBatch or Table to the Parquet file.

        Parameters
        ----------
        table_or_batch : {RecordBatch, Table}
        row_group_size : int, default None
            Maximum number of rows in each written row group. If None,
            the row group size will be the minimum of the input
            table or batch length and 1024 * 1024.
        """
    def write_batch(self, batch, row_group_size: Incomplete | None = None) -> None:
        """
        Write RecordBatch to the Parquet file.

        Parameters
        ----------
        batch : RecordBatch
        row_group_size : int, default None
            Maximum number of rows in written row group. If None, the
            row group size will be the minimum of the RecordBatch
            size and 1024 * 1024.  If set larger than 64Mi then 64Mi
            will be used instead.
        """
    def write_table(self, table, row_group_size: Incomplete | None = None) -> None:
        """
        Write Table to the Parquet file.

        Parameters
        ----------
        table : Table
        row_group_size : int, default None
            Maximum number of rows in each written row group. If None,
            the row group size will be the minimum of the Table size
            and 1024 * 1024.  If set larger than 64Mi then 64Mi will
            be used instead.

        """
    def close(self) -> None:
        """
        Close the connection to the Parquet file.
        """

class ParquetDatasetPiece:
    """
    DEPRECATED: A single chunk of a potentially larger Parquet dataset to read.

    The arguments will indicate to read either a single row group or all row
    groups, and whether to add partition keys to the resulting pyarrow.Table.

    .. deprecated:: 5.0
        Directly constructing a ``ParquetDatasetPiece`` is deprecated, as well
        as accessing the pieces of a ``ParquetDataset`` object. Specify
        ``use_legacy_dataset=False`` when constructing the ``ParquetDataset``
        and use the ``ParquetDataset.fragments`` attribute instead.

    Parameters
    ----------
    path : str or pathlib.Path
        Path to file in the file system where this piece is located.
    open_file_func : callable
        Function to use for obtaining file handle to dataset piece.
    file_options : dict
        Options
    row_group : int, default None
        Row group to load. By default, reads all row groups.
    partition_keys : list of tuples
        Two-element tuples of ``(column name, ordinal index)``.
    """
    def __init__(self, path, open_file_func=..., file_options: Incomplete | None = None, row_group: Incomplete | None = None, partition_keys: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def get_metadata(self):
        """
        Return the file's metadata.

        Returns
        -------
        metadata : FileMetaData
            The file's metadata
        """
    def open(self):
        """
        Return instance of ParquetFile.
        """
    def read(self, columns: Incomplete | None = None, use_threads: bool = True, partitions: Incomplete | None = None, file: Incomplete | None = None, use_pandas_metadata: bool = False):
        """
        Read this piece as a pyarrow.Table.

        Parameters
        ----------
        columns : list of column names, default None
        use_threads : bool, default True
            Perform multi-threaded column reads.
        partitions : ParquetPartitions, default None
        file : file-like object
            Passed to ParquetFile.
        use_pandas_metadata : bool
            If pandas metadata should be used or not.

        Returns
        -------
        table : pyarrow.Table
            The piece as a pyarrow.Table.
        """

class PartitionSet:
    """
    A data structure for cataloguing the observed Parquet partitions at a
    particular level. So if we have

    /foo=a/bar=0
    /foo=a/bar=1
    /foo=a/bar=2
    /foo=b/bar=0
    /foo=b/bar=1
    /foo=b/bar=2

    Then we have two partition sets, one for foo, another for bar. As we visit
    levels of the partition hierarchy, a PartitionSet tracks the distinct
    values and assigns categorical codes to use when reading the pieces

    Parameters
    ----------
    name : str
        Name of the partition set. Under which key to collect all values.
    keys : list
        All possible values that have been collected for that partition set.
    """
    name: Incomplete
    keys: Incomplete
    key_indices: Incomplete
    def __init__(self, name, keys: Incomplete | None = None) -> None: ...
    def get_index(self, key):
        """
        Get the index of the partition value if it is known, otherwise assign
        one

        Parameters
        ----------
        key : str or int
            The value for which we want to known the index.
        """
    @property
    def dictionary(self): ...
    @property
    def is_sorted(self): ...

class ParquetPartitions:
    levels: Incomplete
    partition_names: Incomplete
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def equals(self, other): ...
    def __eq__(self, other): ...
    def get_index(self, level, name, key):
        """
        Record a partition value at a particular level, returning the distinct
        code for that value at that level.

        Examples
        --------

        partitions.get_index(1, 'foo', 'a') returns 0
        partitions.get_index(1, 'foo', 'b') returns 1
        partitions.get_index(1, 'foo', 'c') returns 2
        partitions.get_index(1, 'foo', 'a') returns 0

        Parameters
        ----------
        level : int
            The nesting level of the partition we are observing
        name : str
            The partition name
        key : str or int
            The partition value
        """
    def filter_accepts_partition(self, part_key, filter, level): ...

class ParquetManifest:
    filesystem: Incomplete
    open_file_func: Incomplete
    pathsep: Incomplete
    dirpath: Incomplete
    partition_scheme: Incomplete
    partitions: Incomplete
    pieces: Incomplete
    common_metadata_path: Incomplete
    metadata_path: Incomplete
    def __init__(self, dirpath, open_file_func: Incomplete | None = None, filesystem: Incomplete | None = None, pathsep: str = '/', partition_scheme: str = 'hive', metadata_nthreads: int = 1) -> None: ...

class _ParquetDatasetMetadata: ...

class ParquetDataset:
    __doc__: Incomplete
    def __new__(cls, path_or_paths: Incomplete | None = None, filesystem: Incomplete | None = None, schema: Incomplete | None = None, metadata: Incomplete | None = None, split_row_groups: bool = False, validate_schema: bool = True, filters: Incomplete | None = None, metadata_nthreads: Incomplete | None = None, read_dictionary: Incomplete | None = None, memory_map: bool = False, buffer_size: int = 0, partitioning: str = 'hive', use_legacy_dataset: Incomplete | None = None, pre_buffer: bool = True, coerce_int96_timestamp_unit: Incomplete | None = None, thrift_string_size_limit: Incomplete | None = None, thrift_container_size_limit: Incomplete | None = None): ...
    paths: Incomplete
    split_row_groups: Incomplete
    def __init__(self, path_or_paths, filesystem: Incomplete | None = None, schema: Incomplete | None = None, metadata: Incomplete | None = None, split_row_groups: bool = False, validate_schema: bool = True, filters: Incomplete | None = None, metadata_nthreads: Incomplete | None = None, read_dictionary: Incomplete | None = None, memory_map: bool = False, buffer_size: int = 0, partitioning: str = 'hive', use_legacy_dataset: Incomplete | None = None, pre_buffer: bool = True, coerce_int96_timestamp_unit: Incomplete | None = None, thrift_string_size_limit: Incomplete | None = None, thrift_container_size_limit: Incomplete | None = None) -> None: ...
    def __getnewargs_ex__(self): ...
    def equals(self, other): ...
    def __eq__(self, other): ...
    def validate_schemas(self) -> None: ...
    def read(self, columns: Incomplete | None = None, use_threads: bool = True, use_pandas_metadata: bool = False):
        '''
        Read multiple Parquet files as a single pyarrow.Table.

        Parameters
        ----------
        columns : List[str]
            Names of columns to read from the file.
        use_threads : bool, default True
            Perform multi-threaded column reads
        use_pandas_metadata : bool, default False
            Passed through to each dataset piece.

        Returns
        -------
        pyarrow.Table
            Content of the file as a table (of columns).

        Examples
        --------
        Generate an example dataset:

        >>> import pyarrow as pa
        >>> table = pa.table({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],
        ...                   \'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_to_dataset(table, root_path=\'dataset_name_read\',
        ...                     partition_cols=[\'year\'],
        ...                     use_legacy_dataset=False)
        >>> dataset = pq.ParquetDataset(\'dataset_name_read/\',
        ...                             use_legacy_dataset=False)

        Read multiple Parquet files as a single pyarrow.Table:

        >>> dataset.read(columns=["n_legs"])
        pyarrow.Table
        n_legs: int64
        ----
        n_legs: [[5],[2],[4,100],[2,4]]
        '''
    def read_pandas(self, **kwargs):
        '''
        Read dataset including pandas metadata, if any. Other arguments passed
        through to ParquetDataset.read, see docstring for further details.

        Parameters
        ----------
        **kwargs : optional
            All additional options to pass to the reader.

        Returns
        -------
        pyarrow.Table
            Content of the file as a table (of columns).

        Examples
        --------
        Generate an example PyArrow Table and write it to a partitioned
        dataset:

        >>> import pyarrow as pa
        >>> import pandas as pd
        >>> df = pd.DataFrame({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],
        ...                    \'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                    \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                    "Brittle stars", "Centipede"]})
        >>> table = pa.Table.from_pandas(df)
        >>> import pyarrow.parquet as pq
        >>> pq.write_table(table, \'table.parquet\')
        >>> dataset = pq.ParquetDataset(\'table.parquet\',
        ...                             use_legacy_dataset=False)

        Read dataset including pandas metadata:

        >>> dataset.read_pandas(columns=["n_legs"])
        pyarrow.Table
        n_legs: int64
        ----
        n_legs: [[2,2,4,4,5,100]]

        Select pandas metadata:

        >>> dataset.read_pandas(columns=["n_legs"]).schema.pandas_metadata
        {\'index_columns\': [{\'kind\': \'range\', \'name\': None, \'start\': 0, ...}
        '''
    @property
    def pieces(self):
        """
        DEPRECATED
        """
    @property
    def partitions(self):
        """
        DEPRECATED
        """
    @property
    def schema(self): ...
    @property
    def memory_map(self):
        """
        DEPRECATED
        """
    @property
    def read_dictionary(self):
        """
        DEPRECATED
        """
    @property
    def buffer_size(self):
        """
        DEPRECATED
        """
    @property
    def fs(self):
        """
        DEPRECATED
        """
    @property
    def metadata(self):
        """
        DEPRECATED
        """
    @property
    def metadata_path(self):
        """
        DEPRECATED
        """
    @property
    def common_metadata_path(self):
        """
        DEPRECATED
        """
    @property
    def common_metadata(self):
        """
        DEPRECATED
        """
    @property
    def fragments(self) -> None:
        '''
        A list of the Dataset source fragments or pieces with absolute
        file paths. To use this property set \'use_legacy_dataset=False\'
        while constructing ParquetDataset object.

        Examples
        --------
        Generate an example dataset:

        >>> import pyarrow as pa
        >>> table = pa.table({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],
        ...                   \'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_to_dataset(table, root_path=\'dataset_name_fragments\',
        ...                     partition_cols=[\'year\'],
        ...                     use_legacy_dataset=False)
        >>> dataset = pq.ParquetDataset(\'dataset_name_fragments/\',
        ...                             use_legacy_dataset=False)

        List the fragments:

        >>> dataset.fragments
        [<pyarrow.dataset.ParquetFileFragment path=dataset_name_fragments/...
        '''
    @property
    def files(self) -> None:
        '''
        A list of absolute Parquet file paths in the Dataset source.
        To use this property set \'use_legacy_dataset=False\'
        while constructing ParquetDataset object.

        Examples
        --------
        Generate an example dataset:

        >>> import pyarrow as pa
        >>> table = pa.table({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],
        ...                   \'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_to_dataset(table, root_path=\'dataset_name_files\',
        ...                     partition_cols=[\'year\'],
        ...                     use_legacy_dataset=False)
        >>> dataset = pq.ParquetDataset(\'dataset_name_files/\',
        ...                             use_legacy_dataset=False)

        List the files:

        >>> dataset.files
        [\'dataset_name_files/year=2019/...-0.parquet\', ...
        '''
    @property
    def filesystem(self) -> None:
        """
        The filesystem type of the Dataset source.
        To use this property set 'use_legacy_dataset=False'
        while constructing ParquetDataset object.
        """
    @property
    def partitioning(self) -> None:
        """
        The partitioning of the Dataset source, if discovered.
        To use this property set 'use_legacy_dataset=False'
        while constructing ParquetDataset object.
        """

class _ParquetDatasetV2:
    '''
    ParquetDataset shim using the Dataset API under the hood.

    Examples
    --------
    Generate an example PyArrow Table and write it to a partitioned dataset:

    >>> import pyarrow as pa
    >>> table = pa.table({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],
    ...                   \'n_legs\': [2, 2, 4, 4, 5, 100],
    ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
    ...                              "Brittle stars", "Centipede"]})
    >>> import pyarrow.parquet as pq
    >>> pq.write_to_dataset(table, root_path=\'dataset_v2\',
    ...                     partition_cols=[\'year\'],
    ...                     use_legacy_dataset=False)

    create a ParquetDataset object from the dataset source:

    >>> dataset = pq.ParquetDataset(\'dataset_v2/\', use_legacy_dataset=False)

    and read the data:

    >>> dataset.read().to_pandas()
       n_legs         animal  year
    0       5  Brittle stars  2019
    1       2       Flamingo  2020
    2       4            Dog  2021
    3     100      Centipede  2021
    4       2         Parrot  2022
    5       4          Horse  2022

    create a ParquetDataset object with filter:

    >>> dataset = pq.ParquetDataset(\'dataset_v2/\',
    ...                             filters=[(\'n_legs\',\'=\',4)],
    ...                             use_legacy_dataset=False)
    >>> dataset.read().to_pandas()
       n_legs animal  year
    0       4    Dog  2021
    1       4  Horse  2022
    '''
    def __init__(self, path_or_paths, filesystem: Incomplete | None = None, *, filters: Incomplete | None = None, partitioning: str = 'hive', read_dictionary: Incomplete | None = None, buffer_size: Incomplete | None = None, memory_map: bool = False, ignore_prefixes: Incomplete | None = None, pre_buffer: bool = True, coerce_int96_timestamp_unit: Incomplete | None = None, schema: Incomplete | None = None, decryption_properties: Incomplete | None = None, thrift_string_size_limit: Incomplete | None = None, thrift_container_size_limit: Incomplete | None = None, **kwargs) -> None: ...
    def equals(self, other): ...
    def __eq__(self, other): ...
    @property
    def schema(self):
        '''
        Schema of the Dataset.

        Examples
        --------
        Generate an example dataset:

        >>> import pyarrow as pa
        >>> table = pa.table({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],
        ...                   \'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_to_dataset(table, root_path=\'dataset_v2_schema\',
        ...                     partition_cols=[\'year\'],
        ...                     use_legacy_dataset=False)
        >>> dataset = pq.ParquetDataset(\'dataset_v2_schema/\',
        ...                             use_legacy_dataset=False)

        Read the schema:

        >>> dataset.schema
        n_legs: int64
        animal: string
        year: dictionary<values=int32, indices=int32, ordered=0>
        '''
    def read(self, columns: Incomplete | None = None, use_threads: bool = True, use_pandas_metadata: bool = False):
        '''
        Read (multiple) Parquet files as a single pyarrow.Table.

        Parameters
        ----------
        columns : List[str]
            Names of columns to read from the dataset. The partition fields
            are not automatically included (in contrast to when setting
            ``use_legacy_dataset=True``).
        use_threads : bool, default True
            Perform multi-threaded column reads.
        use_pandas_metadata : bool, default False
            If True and file has custom pandas schema metadata, ensure that
            index columns are also loaded.

        Returns
        -------
        pyarrow.Table
            Content of the file as a table (of columns).

        Examples
        --------
        Generate an example dataset:

        >>> import pyarrow as pa
        >>> table = pa.table({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],
        ...                   \'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_to_dataset(table, root_path=\'dataset_v2_read\',
        ...                     partition_cols=[\'year\'],
        ...                     use_legacy_dataset=False)
        >>> dataset = pq.ParquetDataset(\'dataset_v2_read/\',
        ...                             use_legacy_dataset=False)

        Read the dataset:

        >>> dataset.read(columns=["n_legs"])
        pyarrow.Table
        n_legs: int64
        ----
        n_legs: [[5],[2],[4,100],[2,4]]
        '''
    def read_pandas(self, **kwargs):
        '''
        Read dataset including pandas metadata, if any. Other arguments passed
        through to ParquetDataset.read, see docstring for further details.

        Examples
        --------
        Generate an example parquet file:

        >>> import pyarrow as pa
        >>> import pandas as pd
        >>> df = pd.DataFrame({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],
        ...                    \'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                    \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                    "Brittle stars", "Centipede"]})
        >>> table = pa.Table.from_pandas(df)
        >>> import pyarrow.parquet as pq
        >>> pq.write_table(table, \'table_V2.parquet\')
        >>> dataset = pq.ParquetDataset(\'table_V2.parquet\',
        ...                             use_legacy_dataset=False)

        Read the dataset with pandas metadata:

        >>> dataset.read_pandas(columns=["n_legs"])
        pyarrow.Table
        n_legs: int64
        ----
        n_legs: [[2,2,4,4,5,100]]

        >>> dataset.read_pandas(columns=["n_legs"]).schema.pandas_metadata
        {\'index_columns\': [{\'kind\': \'range\', \'name\': None, \'start\': 0, ...}
        '''
    @property
    def pieces(self): ...
    @property
    def fragments(self):
        '''
        A list of the Dataset source fragments or pieces with absolute
        file paths.

        Examples
        --------
        Generate an example dataset:

        >>> import pyarrow as pa
        >>> table = pa.table({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],
        ...                   \'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_to_dataset(table, root_path=\'dataset_v2_fragments\',
        ...                     partition_cols=[\'year\'],
        ...                     use_legacy_dataset=False)
        >>> dataset = pq.ParquetDataset(\'dataset_v2_fragments/\',
        ...                             use_legacy_dataset=False)

        List the fragments:

        >>> dataset.fragments
        [<pyarrow.dataset.ParquetFileFragment path=dataset_v2_fragments/...
        '''
    @property
    def files(self):
        '''
        A list of absolute Parquet file paths in the Dataset source.

        Examples
        --------
        Generate an example dataset:

        >>> import pyarrow as pa
        >>> table = pa.table({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],
        ...                   \'n_legs\': [2, 2, 4, 4, 5, 100],
        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
        ...                              "Brittle stars", "Centipede"]})
        >>> import pyarrow.parquet as pq
        >>> pq.write_to_dataset(table, root_path=\'dataset_v2_files\',
        ...                     partition_cols=[\'year\'],
        ...                     use_legacy_dataset=False)
        >>> dataset = pq.ParquetDataset(\'dataset_v2_files/\',
        ...                             use_legacy_dataset=False)

        List the files:

        >>> dataset.files
        [\'dataset_v2_files/year=2019/...-0.parquet\', ...
        '''
    @property
    def filesystem(self):
        """
        The filesystem type of the Dataset source.
        """
    @property
    def partitioning(self):
        """
        The partitioning of the Dataset source, if discovered.
        """

def read_table(source, *, columns: Incomplete | None = None, use_threads: bool = True, metadata: Incomplete | None = None, schema: Incomplete | None = None, use_pandas_metadata: bool = False, read_dictionary: Incomplete | None = None, memory_map: bool = False, buffer_size: int = 0, partitioning: str = 'hive', filesystem: Incomplete | None = None, filters: Incomplete | None = None, use_legacy_dataset: bool = False, ignore_prefixes: Incomplete | None = None, pre_buffer: bool = True, coerce_int96_timestamp_unit: Incomplete | None = None, decryption_properties: Incomplete | None = None, thrift_string_size_limit: Incomplete | None = None, thrift_container_size_limit: Incomplete | None = None): ...
def read_pandas(source, columns: Incomplete | None = None, **kwargs): ...
def write_table(table, where, row_group_size: Incomplete | None = None, version: str = '2.4', use_dictionary: bool = True, compression: str = 'snappy', write_statistics: bool = True, use_deprecated_int96_timestamps: Incomplete | None = None, coerce_timestamps: Incomplete | None = None, allow_truncated_timestamps: bool = False, data_page_size: Incomplete | None = None, flavor: Incomplete | None = None, filesystem: Incomplete | None = None, compression_level: Incomplete | None = None, use_byte_stream_split: bool = False, column_encoding: Incomplete | None = None, data_page_version: str = '1.0', use_compliant_nested_type: bool = False, encryption_properties: Incomplete | None = None, write_batch_size: Incomplete | None = None, dictionary_pagesize_limit: Incomplete | None = None, store_schema: bool = True, **kwargs) -> None: ...
def write_to_dataset(table, root_path, partition_cols: Incomplete | None = None, partition_filename_cb: Incomplete | None = None, filesystem: Incomplete | None = None, use_legacy_dataset: Incomplete | None = None, schema: Incomplete | None = None, partitioning: Incomplete | None = None, basename_template: Incomplete | None = None, use_threads: Incomplete | None = None, file_visitor: Incomplete | None = None, existing_data_behavior: Incomplete | None = None, **kwargs) -> None:
    '''Wrapper around dataset.write_dataset (when use_legacy_dataset=False) or
    parquet.write_table (when use_legacy_dataset=True) for writing a Table to
    Parquet format by partitions.
    For each combination of partition columns and values,
    a subdirectories are created in the following
    manner:

    root_dir/
      group1=value1
        group2=value1
          <uuid>.parquet
        group2=value2
          <uuid>.parquet
      group1=valueN
        group2=value1
          <uuid>.parquet
        group2=valueN
          <uuid>.parquet

    Parameters
    ----------
    table : pyarrow.Table
    root_path : str, pathlib.Path
        The root directory of the dataset
    partition_cols : list,
        Column names by which to partition the dataset.
        Columns are partitioned in the order they are given
    partition_filename_cb : callable,
        A callback function that takes the partition key(s) as an argument
        and allow you to override the partition filename. If nothing is
        passed, the filename will consist of a uuid.
        This option is only supported for use_legacy_dataset=True.
        When use_legacy_dataset=None and this option is specified,
        use_legacy_datase will be set to True.
    filesystem : FileSystem, default None
        If nothing passed, will be inferred based on path.
        Path will try to be found in the local on-disk filesystem otherwise
        it will be parsed as an URI to determine the filesystem.
    use_legacy_dataset : bool
        Default is False. Set to True to use the the legacy behaviour
        (this option is deprecated, and the legacy implementation will be
        removed in a future version). The legacy implementation still
        supports the `partition_filename_cb` keyword but is less efficient
        when using partition columns.
    schema : Schema, optional
        This option is only supported for use_legacy_dataset=False.
    partitioning : Partitioning or list[str], optional
        The partitioning scheme specified with the
        ``pyarrow.dataset.partitioning()`` function or a list of field names.
        When providing a list of field names, you can use
        ``partitioning_flavor`` to drive which partitioning type should be
        used.
        This option is only supported for use_legacy_dataset=False.
    basename_template : str, optional
        A template string used to generate basenames of written data files.
        The token \'{i}\' will be replaced with an automatically incremented
        integer. If not specified, it defaults to "guid-{i}.parquet".
        This option is only supported for use_legacy_dataset=False.
    use_threads : bool, default True
        Write files in parallel. If enabled, then maximum parallelism will be
        used determined by the number of available CPU cores.
        This option is only supported for use_legacy_dataset=False.
    file_visitor : function
        If set, this function will be called with a WrittenFile instance
        for each file created during the call.  This object will have both
        a path attribute and a metadata attribute.

        The path attribute will be a string containing the path to
        the created file.

        The metadata attribute will be the parquet metadata of the file.
        This metadata will have the file path attribute set and can be used
        to build a _metadata file.  The metadata attribute will be None if
        the format is not parquet.

        Example visitor which simple collects the filenames created::

            visited_paths = []

            def file_visitor(written_file):
                visited_paths.append(written_file.path)

        This option is only supported for use_legacy_dataset=False.
    existing_data_behavior : \'overwrite_or_ignore\' | \'error\' | \'delete_matching\'
        Controls how the dataset will handle data that already exists in
        the destination. The default behaviour is \'overwrite_or_ignore\'.

        \'overwrite_or_ignore\' will ignore any existing data and will
        overwrite files with the same name as an output file.  Other
        existing files will be ignored.  This behavior, in combination
        with a unique basename_template for each write, will allow for
        an append workflow.

        \'error\' will raise an error if any data exists in the destination.

        \'delete_matching\' is useful when you are writing a partitioned
        dataset.  The first time each partition directory is encountered
        the entire directory will be deleted.  This allows you to overwrite
        old partitions completely.
        This option is only supported for use_legacy_dataset=False.
    **kwargs : dict,
        When use_legacy_dataset=False, used as additional kwargs for
        `dataset.write_dataset` function for matching kwargs, and remainder to
        `ParquetFileFormat.make_write_options`. See the docstring
        of `write_table` and `dataset.write_dataset` for the available options.
        When use_legacy_dataset=True, used as additional kwargs for
        `parquet.write_table` function (See docstring for `write_table`
        or `ParquetWriter` for more information).
        Using `metadata_collector` in kwargs allows one to collect the
        file metadata instances of dataset pieces. The file paths in the
        ColumnChunkMetaData will be set relative to `root_path`.

    Examples
    --------
    Generate an example PyArrow Table:

    >>> import pyarrow as pa
    >>> table = pa.table({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],
    ...                   \'n_legs\': [2, 2, 4, 4, 5, 100],
    ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
    ...                              "Brittle stars", "Centipede"]})

    and write it to a partitioned dataset:

    >>> import pyarrow.parquet as pq
    >>> pq.write_to_dataset(table, root_path=\'dataset_name_3\',
    ...                     partition_cols=[\'year\'])
    >>> pq.ParquetDataset(\'dataset_name_3\', use_legacy_dataset=False).files
    [\'dataset_name_3/year=2019/...-0.parquet\', ...

    Write a single Parquet file into the root folder:

    >>> pq.write_to_dataset(table, root_path=\'dataset_name_4\')
    >>> pq.ParquetDataset(\'dataset_name_4/\', use_legacy_dataset=False).files
    [\'dataset_name_4/...-0.parquet\']
    '''
def write_metadata(schema, where, metadata_collector: Incomplete | None = None, filesystem: Incomplete | None = None, **kwargs) -> None:
    '''
    Write metadata-only Parquet file from schema. This can be used with
    `write_to_dataset` to generate `_common_metadata` and `_metadata` sidecar
    files.

    Parameters
    ----------
    schema : pyarrow.Schema
    where : string or pyarrow.NativeFile
    metadata_collector : list
        where to collect metadata information.
    filesystem : FileSystem, default None
        If nothing passed, will be inferred from `where` if path-like, else
        `where` is already a file-like object so no filesystem is needed.
    **kwargs : dict,
        Additional kwargs for ParquetWriter class. See docstring for
        `ParquetWriter` for more information.

    Examples
    --------
    Generate example data:

    >>> import pyarrow as pa
    >>> table = pa.table({\'n_legs\': [2, 2, 4, 4, 5, 100],
    ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",
    ...                              "Brittle stars", "Centipede"]})

    Write a dataset and collect metadata information.

    >>> metadata_collector = []
    >>> import pyarrow.parquet as pq
    >>> pq.write_to_dataset(
    ...     table, \'dataset_metadata\',
    ...      metadata_collector=metadata_collector)

    Write the `_common_metadata` parquet file without row groups statistics.

    >>> pq.write_metadata(
    ...     table.schema, \'dataset_metadata/_common_metadata\')

    Write the `_metadata` parquet file with row groups statistics.

    >>> pq.write_metadata(
    ...     table.schema, \'dataset_metadata/_metadata\',
    ...     metadata_collector=metadata_collector)
    '''
def read_metadata(where, memory_map: bool = False, decryption_properties: Incomplete | None = None, filesystem: Incomplete | None = None):
    '''
    Read FileMetaData from footer of a single Parquet file.

    Parameters
    ----------
    where : str (file path) or file-like object
    memory_map : bool, default False
        Create memory map when the source is a file path.
    decryption_properties : FileDecryptionProperties, default None
        Decryption properties for reading encrypted Parquet files.
    filesystem : FileSystem, default None
        If nothing passed, will be inferred based on path.
        Path will try to be found in the local on-disk filesystem otherwise
        it will be parsed as an URI to determine the filesystem.

    Returns
    -------
    metadata : FileMetaData
        The metadata of the Parquet file

    Examples
    --------
    >>> import pyarrow as pa
    >>> import pyarrow.parquet as pq
    >>> table = pa.table({\'n_legs\': [4, 5, 100],
    ...                   \'animal\': ["Dog", "Brittle stars", "Centipede"]})
    >>> pq.write_table(table, \'example.parquet\')

    >>> pq.read_metadata(\'example.parquet\')
    <pyarrow._parquet.FileMetaData object at ...>
      created_by: parquet-cpp-arrow version ...
      num_columns: 2
      num_rows: 3
      num_row_groups: 1
      format_version: 2.6
      serialized_size: ...
    '''
def read_schema(where, memory_map: bool = False, decryption_properties: Incomplete | None = None, filesystem: Incomplete | None = None):
    '''
    Read effective Arrow schema from Parquet file metadata.

    Parameters
    ----------
    where : str (file path) or file-like object
    memory_map : bool, default False
        Create memory map when the source is a file path.
    decryption_properties : FileDecryptionProperties, default None
        Decryption properties for reading encrypted Parquet files.
    filesystem : FileSystem, default None
        If nothing passed, will be inferred based on path.
        Path will try to be found in the local on-disk filesystem otherwise
        it will be parsed as an URI to determine the filesystem.

    Returns
    -------
    schema : pyarrow.Schema
        The schema of the Parquet file

    Examples
    --------
    >>> import pyarrow as pa
    >>> import pyarrow.parquet as pq
    >>> table = pa.table({\'n_legs\': [4, 5, 100],
    ...                   \'animal\': ["Dog", "Brittle stars", "Centipede"]})
    >>> pq.write_table(table, \'example.parquet\')

    >>> pq.read_schema(\'example.parquet\')
    n_legs: int64
    animal: string
    '''
