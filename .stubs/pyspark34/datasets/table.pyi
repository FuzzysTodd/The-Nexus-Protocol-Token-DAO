import numpy as np
import pyarrow as pa
from . import config as config
from .features.features import FeatureType as FeatureType, Features as Features
from .utils.logging import get_logger as get_logger
from _typeshed import Incomplete
from typing import Callable, Iterator, List, Tuple, TypeVar

logger: Incomplete

def inject_arrow_table_documentation(arrow_table_method): ...
def read_schema_from_file(filename: str) -> pa.Schema:
    """
    Infer arrow table schema from file without loading whole file into memory.
    Usefull especially while having very big files.
    """

class IndexedTableMixin:
    def __init__(self, table: pa.Table) -> None: ...
    def fast_gather(self, indices: List[int] | np.ndarray) -> pa.Table:
        """
        Create a pa.Table by gathering the records at the records at the specified indices. Should be faster
        than pa.concat_tables(table.fast_slice(int(i) % table.num_rows, 1) for i in indices) since NumPy can compute
        the binary searches in parallel, highly optimized C
        """
    def fast_slice(self, offset: int = 0, length: Incomplete | None = None) -> pa.Table:
        """
        Slice the Table using interpolation search.
        The behavior is the same as `pyarrow.Table.slice` but it's significantly faster.

        Interpolation search is used to find the start and end indexes of the batches we want to keep.
        The batches to keep are then concatenated to form the sliced Table.
        """

class Table(IndexedTableMixin):
    """
    Wraps a pyarrow Table by using composition.
    This is the base class for `InMemoryTable`, `MemoryMappedTable` and `ConcatenationTable`.

    It implements all the basic attributes/methods of the pyarrow Table class except
    the Table transforms: `slice, filter, flatten, combine_chunks, cast, add_column,
    append_column, remove_column, set_column, rename_columns` and `drop`.

    The implementation of these methods differs for the subclasses.
    """
    table: Incomplete
    def __init__(self, table: pa.Table) -> None: ...
    def __deepcopy__(self, memo: dict): ...
    def validate(self, *args, **kwargs):
        """
        Perform validation checks.  An exception is raised if validation fails.

        By default only cheap validation checks are run.  Pass `full=True`
        for thorough validation checks (potentially `O(n)`).

        Args:
            full (`bool`, defaults to `False`):
                If `True`, run expensive checks, otherwise cheap checks only.

        Raises:
            `pa.lib.ArrowInvalid`: if validation fails
        """
    def equals(self, *args, **kwargs):
        """
        Check if contents of two tables are equal.

        Args:
            other ([`~datasets.table.Table`]):
                Table to compare against.
            check_metadata `bool`, defaults to `False`):
                Whether schema metadata equality should be checked as well.

        Returns:
            `bool`
        """
    def to_batches(self, *args, **kwargs):
        """
        Convert Table to list of (contiguous) `RecordBatch` objects.

        Args:
            max_chunksize (`int`, defaults to `None`):
                Maximum size for `RecordBatch` chunks. Individual chunks may be
                smaller depending on the chunk layout of individual columns.

        Returns:
            `List[pyarrow.RecordBatch]`
        """
    def to_pydict(self, *args, **kwargs):
        """
        Convert the Table to a `dict` or `OrderedDict`.

        Returns:
            `dict`
        """
    def to_pylist(self, *args, **kwargs):
        """
        Convert the Table to a list

        Returns:
            `list`
        """
    def to_pandas(self, *args, **kwargs):
        '''
        Convert to a pandas-compatible NumPy array or DataFrame, as appropriate.

        Args:
            memory_pool (`MemoryPool`, defaults to `None`):
                Arrow MemoryPool to use for allocations. Uses the default memory
                pool is not passed.
            strings_to_categorical (`bool`, defaults to `False`):
                Encode string (UTF8) and binary types to `pandas.Categorical`.
            categories (`list`, defaults to `empty`):
                List of fields that should be returned as `pandas.Categorical`. Only
                applies to table-like data structures.
            zero_copy_only (`bool`, defaults to `False`):
                Raise an `ArrowException` if this function call would require copying
                the underlying data.
            integer_object_nulls (`bool`, defaults to `False`):
                Cast integers with nulls to objects.
            date_as_object (`bool`, defaults to `True`):
                Cast dates to objects. If `False`, convert to `datetime64[ns]` dtype.
            timestamp_as_object (`bool`, defaults to `False`):
                Cast non-nanosecond timestamps (`np.datetime64`) to objects. This is
                useful if you have timestamps that don\'t fit in the normal date
                range of nanosecond timestamps (1678 CE-2262 CE).
                If `False`, all timestamps are converted to `datetime64[ns]` dtype.
            use_threads (`bool`, defaults to `True`):
                Whether to parallelize the conversion using multiple threads.
            deduplicate_objects (`bool`, defaults to `False`):
                Do not create multiple copies Python objects when created, to save
                on memory use. Conversion will be slower.
            ignore_metadata (`bool`, defaults to `False`):
                If `True`, do not use the \'pandas\' metadata to reconstruct the
                DataFrame index, if present.
            safe (`bool`, defaults to `True`):
                For certain data types, a cast is needed in order to store the
                data in a pandas DataFrame or Series (e.g. timestamps are always
                stored as nanoseconds in pandas). This option controls whether it
                is a safe cast or not.
            split_blocks (`bool`, defaults to `False`):
                If `True`, generate one internal "block" for each column when
                creating a pandas.DataFrame from a `RecordBatch` or `Table`. While this
                can temporarily reduce memory note that various pandas operations
                can trigger "consolidation" which may balloon memory use.
            self_destruct (`bool`, defaults to `False`):
                EXPERIMENTAL: If `True`, attempt to deallocate the originating Arrow
                memory while converting the Arrow object to pandas. If you use the
                object after calling `to_pandas` with this option it will crash your
                program.
            types_mapper (`function`, defaults to `None`):
                A function mapping a pyarrow DataType to a pandas `ExtensionDtype`.
                This can be used to override the default pandas type for conversion
                of built-in pyarrow types or in absence of `pandas_metadata` in the
                Table schema. The function receives a pyarrow DataType and is
                expected to return a pandas `ExtensionDtype` or `None` if the
                default conversion should be used for that type. If you have
                a dictionary mapping, you can pass `dict.get` as function.

        Returns:
            `pandas.Series` or `pandas.DataFrame`: `pandas.Series` or `pandas.DataFrame` depending on type of object
        '''
    def to_string(self, *args, **kwargs): ...
    def to_reader(self, max_chunksize: int | None = None):
        """
        Convert the Table to a RecordBatchReader.

        Note that this method is zero-copy, it merely exposes the same data under a different API.

        Args:
            max_chunksize (`int`, defaults to `None`)
                Maximum size for RecordBatch chunks. Individual chunks may be smaller depending
                on the chunk layout of individual columns.

        Returns:
            `pyarrow.RecordBatchReader`
        """
    def field(self, *args, **kwargs):
        """
        Select a schema field by its column name or numeric index.

        Args:
            i (`Union[int, str]`):
                The index or name of the field to retrieve.

        Returns:
            `pyarrow.Field`
        """
    def column(self, *args, **kwargs):
        """
        Select a column by its column name, or numeric index.

        Args:
            i (`Union[int, str]`):
                The index or name of the column to retrieve.

        Returns:
            `pyarrow.ChunkedArray`
        """
    def itercolumns(self, *args, **kwargs):
        """
        Iterator over all columns in their numerical order.

        Yields:
            `pyarrow.ChunkedArray`
        """
    @property
    def schema(self):
        """
        Schema of the table and its columns.

        Returns:
            `pyarrow.Schema`
        """
    @property
    def columns(self):
        """
        List of all columns in numerical order.

        Returns:
            `List[pa.ChunkedArray]`
        """
    @property
    def num_columns(self):
        """
        Number of columns in this table.

        Returns:
            int
        """
    @property
    def num_rows(self):
        """
        Number of rows in this table.

        Due to the definition of a table, all columns have the same number of
        rows.

        Returns:
            int
        """
    @property
    def shape(self):
        """
        Dimensions of the table: (#rows, #columns).

        Returns:
            `(int, int)`: Number of rows and number of columns.
        """
    @property
    def nbytes(self):
        """
        Total number of bytes consumed by the elements of the table.
        """
    @property
    def column_names(self):
        """
        Names of the table's columns.
        """
    def __eq__(self, other): ...
    def __getitem__(self, i): ...
    def __len__(self) -> int: ...
    def slice(self, *args, **kwargs) -> None:
        """
        Compute zero-copy slice of this Table.

        Args:
            offset (`int`, defaults to `0`):
                Offset from start of table to slice.
            length (`int`, defaults to `None`):
                Length of slice (default is until end of table starting from
                offset).

        Returns:
            `datasets.table.Table`
        """
    def filter(self, *args, **kwargs) -> None:
        """
        Select records from a Table. See `pyarrow.compute.filter` for full usage.
        """
    def flatten(self, *args, **kwargs) -> None:
        """
        Flatten this Table.  Each column with a struct type is flattened
        into one column per struct field.  Other columns are left unchanged.

        Args:
            memory_pool (`MemoryPool`, defaults to `None`):
                For memory allocations, if required, otherwise use default pool.

        Returns:
            `datasets.table.Table`
        """
    def combine_chunks(self, *args, **kwargs) -> None:
        """
        Make a new table by combining the chunks this table has.

        All the underlying chunks in the `ChunkedArray` of each column are
        concatenated into zero or one chunk.

        Args:
            memory_pool (`MemoryPool`, defaults to `None`):
                For memory allocations, if required, otherwise use default pool.

        Returns:
            `datasets.table.Table`
        """
    def cast(self, *args, **kwargs) -> None:
        """
        Cast table values to another schema.

        Args:
            target_schema (`Schema`):
                Schema to cast to, the names and order of fields must match.
            safe (`bool`, defaults to `True`):
                Check for overflows or other unsafe conversions.

        Returns:
            `datasets.table.Table`
        """
    def replace_schema_metadata(self, *args, **kwargs) -> None:
        """
        EXPERIMENTAL: Create shallow copy of table by replacing schema
        key-value metadata with the indicated new metadata (which may be None,
        which deletes any existing metadata

        Args:
            metadata (`dict`, defaults to `None`):

        Returns:
            `datasets.table.Table`: shallow_copy
        """
    def add_column(self, *args, **kwargs) -> None:
        """
        Add column to Table at position.

        A new table is returned with the column added, the original table
        object is left unchanged.

        Args:
            i (`int`):
                Index to place the column at.
            field_ (`Union[str, pyarrow.Field]`):
                If a string is passed then the type is deduced from the column
                data.
            column (`Union[pyarrow.Array, List[pyarrow.Array]]`):
                Column data.

        Returns:
            `datasets.table.Table`: New table with the passed column added.
        """
    def append_column(self, *args, **kwargs) -> None:
        """
        Append column at end of columns.

        Args:
            field_ (`Union[str, pyarrow.Field]`):
                If a string is passed then the type is deduced from the column
                data.
            column (`Union[pyarrow.Array, List[pyarrow.Array]]`):
                Column data.

        Returns:
            `datasets.table.Table`:  New table with the passed column added.
        """
    def remove_column(self, *args, **kwargs) -> None:
        """
        Create new Table with the indicated column removed.

        Args:
            i (`int`):
                Index of column to remove.

        Returns:
            `datasets.table.Table`: New table without the column.
        """
    def set_column(self, *args, **kwargs) -> None:
        """
        Replace column in Table at position.

        Args:
            i (`int`):
                Index to place the column at.
            field_ (`Union[str, pyarrow.Field]`):
                If a string is passed then the type is deduced from the column
                data.
            column (`Union[pyarrow.Array, List[pyarrow.Array]]`):
                Column data.

        Returns:
            `datasets.table.Table`: New table with the passed column set.
        """
    def rename_columns(self, *args, **kwargs) -> None:
        """
        Create new table with columns renamed to provided names.
        """
    def drop(self, *args, **kwargs) -> None:
        """
        Drop one or more columns and return a new table.

        Args:
            columns (`List[str]`):
                List of field names referencing existing columns.

        Raises:
            `KeyError` : if any of the passed columns name are not existing.

        Returns:
            `datasets.table.Table`: New table without the columns.
        """
    def select(self, *args, **kwargs) -> None:
        """
        Select columns of the table.

        Returns a new table with the specified columns, and metadata preserved.

        Args:
            columns (:obj:`Union[List[str], List[int]]`):
                The column names or integer indices to select.

        Returns:
            `datasets.table.Table`: table with only a subset of the columns
        """

class TableBlock(Table):
    """
    `TableBlock` is the allowed class inside a `ConcanetationTable`.
    Only `MemoryMappedTable` and `InMemoryTable` are `TableBlock`.
    This is because we don't want a `ConcanetationTable` made out of other `ConcanetationTables`.
    """

class InMemoryTable(TableBlock):
    """
    The table is said in-memory when it is loaded into the user's RAM.

    Pickling it does copy all the data using memory.
    Its implementation is simple and uses the underlying pyarrow Table methods directly.

    This is different from the `MemoryMapped` table, for which pickling doesn't copy all the
    data in memory. For a `MemoryMapped`, unpickling instead reloads the table from the disk.

    `InMemoryTable` must be used when data fit in memory, while `MemoryMapped` are reserved for
    data bigger than memory or when you want the memory footprint of your application to
    stay low.
    """
    @classmethod
    def from_file(cls, filename: str): ...
    @classmethod
    def from_buffer(cls, buffer: pa.Buffer): ...
    @classmethod
    def from_pandas(cls, *args, **kwargs):
        """
        Convert pandas.DataFrame to an Arrow Table.

        The column types in the resulting Arrow Table are inferred from the
        dtypes of the pandas.Series in the DataFrame. In the case of non-object
        Series, the NumPy dtype is translated to its Arrow equivalent. In the
        case of `object`, we need to guess the datatype by looking at the
        Python objects in this Series.

        Be aware that Series of the `object` dtype don't carry enough
        information to always lead to a meaningful Arrow type. In the case that
        we cannot infer a type, e.g. because the DataFrame is of length 0 or
        the Series only contains `None/nan` objects, the type is set to
        null. This behavior can be avoided by constructing an explicit schema
        and passing it to this function.

        Args:
            df (`pandas.DataFrame`):
            schema (`pyarrow.Schema`, *optional*):
                The expected schema of the Arrow Table. This can be used to
                indicate the type of columns if we cannot infer it automatically.
                If passed, the output will have exactly this schema. Columns
                specified in the schema that are not found in the DataFrame columns
                or its index will raise an error. Additional columns or index
                levels in the DataFrame which are not specified in the schema will
                be ignored.
            preserve_index (`bool`, *optional*):
                Whether to store the index as an additional column in the resulting
                `Table`. The default of None will store the index as a column,
                except for RangeIndex which is stored as metadata only. Use
                `preserve_index=True` to force it to be stored as a column.
            nthreads (`int`, defaults to `None` (may use up to system CPU count threads))
                If greater than 1, convert columns to Arrow in parallel using
                indicated number of threads.
            columns (`List[str]`, *optional*):
               List of column to be converted. If `None`, use all columns.
            safe (`bool`, defaults to `True`):
               Check for overflows or other unsafe conversions,

        Returns:
            `datasets.table.Table`:

        Examples:
        ```python
        >>> import pandas as pd
        >>> import pyarrow as pa
        >>> df = pd.DataFrame({
            ...     'int': [1, 2],
            ...     'str': ['a', 'b']
            ... })
        >>> pa.Table.from_pandas(df)
        <pyarrow.lib.Table object at 0x7f05d1fb1b40>
        ```
        """
    @classmethod
    def from_arrays(cls, *args, **kwargs):
        """
        Construct a Table from Arrow arrays.

        Args:
            arrays (`List[Union[pyarrow.Array, pyarrow.ChunkedArray]]`):
                Equal-length arrays that should form the table.
            names (`List[str]`, *optional*):
                Names for the table columns. If not passed, schema must be passed.
            schema (`Schema`, defaults to `None`):
                Schema for the created table. If not passed, names must be passed.
            metadata (`Union[dict, Mapping]`, defaults to `None`):
                Optional metadata for the schema (if inferred).

        Returns:
            `datasets.table.Table`
        """
    @classmethod
    def from_pydict(cls, *args, **kwargs):
        """
        Construct a Table from Arrow arrays or columns.

        Args:
            mapping (`Union[dict, Mapping]`):
                A mapping of strings to Arrays or Python lists.
            schema (`Schema`, defaults to `None`):
                If not passed, will be inferred from the Mapping values
            metadata (`Union[dict, Mapping]`, defaults to `None`):
                Optional metadata for the schema (if inferred).

        Returns:
            `datasets.table.Table`
        """
    @classmethod
    def from_pylist(cls, mapping, *args, **kwargs):
        """
        Construct a Table from list of rows / dictionaries.

        Args:
            mapping (`List[dict]`):
                A mapping of strings to row values.
            schema (`Schema`, defaults to `None`):
                If not passed, will be inferred from the Mapping values
            metadata (`Union[dict, Mapping]`, defaults to `None`):
                Optional metadata for the schema (if inferred).

        Returns:
            `datasets.table.Table`
        """
    @classmethod
    def from_batches(cls, *args, **kwargs):
        """
        Construct a Table from a sequence or iterator of Arrow `RecordBatches`.

        Args:
            batches (`Union[Sequence[pyarrow.RecordBatch], Iterator[pyarrow.RecordBatch]]`):
                Sequence of `RecordBatch` to be converted, all schemas must be equal.
            schema (`Schema`, defaults to `None`):
                If not passed, will be inferred from the first `RecordBatch`.

        Returns:
            `datasets.table.Table`:
        """
    def slice(self, offset: int = 0, length: Incomplete | None = None):
        """
        Compute zero-copy slice of this Table.

        Args:
            offset (`int`, defaults to `0`):
                Offset from start of table to slice.
            length (`int`, defaults to `None`):
                Length of slice (default is until end of table starting from
                offset).

        Returns:
            `datasets.table.Table`
        """
    def filter(self, *args, **kwargs):
        """
        Select records from a Table. See `pyarrow.compute.filter` for full usage.
        """
    def flatten(self, *args, **kwargs):
        """
        Flatten this Table.  Each column with a struct type is flattened
        into one column per struct field.  Other columns are left unchanged.

        Args:
            memory_pool (`MemoryPool`, defaults to `None`):
                For memory allocations, if required, otherwise use default pool.

        Returns:
            `datasets.table.Table`
        """
    def combine_chunks(self, *args, **kwargs):
        """
        Make a new table by combining the chunks this table has.

        All the underlying chunks in the `ChunkedArray` of each column are
        concatenated into zero or one chunk.

        Args:
            memory_pool (`MemoryPool`, defaults to `None`):
                For memory allocations, if required, otherwise use default pool.

        Returns:
            `datasets.table.Table`
        """
    def cast(self, *args, **kwargs):
        """
        Cast table values to another schema.

        Args:
            target_schema (`Schema`):
                Schema to cast to, the names and order of fields must match.
            safe (`bool`, defaults to `True`):
                Check for overflows or other unsafe conversions.

        Returns:
            `datasets.table.Table`
        """
    def replace_schema_metadata(self, *args, **kwargs):
        """
        EXPERIMENTAL: Create shallow copy of table by replacing schema
        key-value metadata with the indicated new metadata (which may be `None`,
        which deletes any existing metadata).

        Args:
            metadata (`dict`, defaults to `None`):

        Returns:
            `datasets.table.Table`: shallow_copy
        """
    def add_column(self, *args, **kwargs):
        """
        Add column to Table at position.

        A new table is returned with the column added, the original table
        object is left unchanged.

        Args:
            i (`int`):
                Index to place the column at.
            field_ (`Union[str, pyarrow.Field]`):
                If a string is passed then the type is deduced from the column
                data.
            column (`Union[pyarrow.Array, List[pyarrow.Array]]`):
                Column data.

        Returns:
            `datasets.table.Table`: New table with the passed column added.
        """
    def append_column(self, *args, **kwargs):
        """
        Append column at end of columns.

        Args:
            field_ (`Union[str, pyarrow.Field]`):
                If a string is passed then the type is deduced from the column
                data.
            column (`Union[pyarrow.Array, List[pyarrow.Array]]`):
                Column data.

        Returns:
            `datasets.table.Table`:
                New table with the passed column added.
        """
    def remove_column(self, *args, **kwargs):
        """
        Create new Table with the indicated column removed.

        Args:
            i (`int`):
                Index of column to remove.

        Returns:
            `datasets.table.Table`:
                New table without the column.
        """
    def set_column(self, *args, **kwargs):
        """
        Replace column in Table at position.

        Args:
            i (`int`):
                Index to place the column at.
            field_ (`Union[str, pyarrow.Field]`):
                If a string is passed then the type is deduced from the column
                data.
            column (`Union[pyarrow.Array, List[pyarrow.Array]]`):
                Column data.

        Returns:
            `datasets.table.Table`:
                New table with the passed column set.
        """
    def rename_columns(self, *args, **kwargs):
        """
        Create new table with columns renamed to provided names.
        """
    def drop(self, *args, **kwargs):
        """
        Drop one or more columns and return a new table.

        Args:
            columns (`List[str]`):
                List of field names referencing existing columns.

        Raises:
            `KeyError` : if any of the passed columns name are not existing.

        Returns:
            `datasets.table.Table`:
                New table without the columns.
        """
    def select(self, *args, **kwargs):
        """
        Select columns of the table.

        Returns a new table with the specified columns, and metadata preserved.

        Args:
            columns (:obj:`Union[List[str], List[int]]`):
                The column names or integer indices to select.

        Returns:
            :class:`datasets.table.Table`: New table with the specified columns, and metadata preserved.
        """
Replay = Tuple[str, tuple, dict]

class MemoryMappedTable(TableBlock):
    '''
    The table is said memory mapped when it doesn\'t use the user\'s RAM but loads the data
    from the disk instead.

    Pickling it doesn\'t copy the data into memory.
    Instead, only the path to the memory mapped arrow file is pickled, as well as the list
    of transforms to "replay" when reloading the table from the disk.

    Its implementation requires to store an history of all the transforms that were applied
    to the underlying pyarrow Table, so that they can be "replayed" when reloading the Table
    from the disk.

    This is different from the `InMemoryTable` table, for which pickling does copy all the
    data in memory.

    `InMemoryTable` must be used when data fit in memory, while `MemoryMapped` are reserved for
    data bigger than memory or when you want the memory footprint of your application to
    stay low.
    '''
    path: Incomplete
    replays: Incomplete
    def __init__(self, table: pa.Table, path: str, replays: List[Replay] | None = None) -> None: ...
    @classmethod
    def from_file(cls, filename: str, replays: Incomplete | None = None): ...
    def slice(self, offset: int = 0, length: Incomplete | None = None):
        """
        Compute zero-copy slice of this Table.

        Args:
            offset (`int`, defaults to `0`):
                Offset from start of table to slice.
            length (`int`, defaults to `None`):
                Length of slice (default is until end of table starting from
                offset).

        Returns:
            `datasets.table.Table`
        """
    def filter(self, *args, **kwargs):
        """
        Select records from a Table. See `pyarrow.compute.filter` for full usage.
        """
    def flatten(self, *args, **kwargs):
        """
        Flatten this Table.  Each column with a struct type is flattened
        into one column per struct field.  Other columns are left unchanged.

        Args:
            memory_pool (`MemoryPool`, defaults to `None`):
                For memory allocations, if required, otherwise use default pool.

        Returns:
            `datasets.table.Table`
        """
    def combine_chunks(self, *args, **kwargs):
        """
        Make a new table by combining the chunks this table has.

        All the underlying chunks in the ChunkedArray of each column are
        concatenated into zero or one chunk.

        Args:
            memory_pool (`MemoryPool`, defaults to `None`):
                For memory allocations, if required, otherwise use default pool.

        Returns:
            `datasets.table.Table`
        """
    def cast(self, *args, **kwargs):
        """
        Cast table values to another schema

        Args:
            target_schema (`Schema`):
                Schema to cast to, the names and order of fields must match.
            safe (`bool`, defaults to `True`):
                Check for overflows or other unsafe conversions.

        Returns:
            `datasets.table.Table`
        """
    def replace_schema_metadata(self, *args, **kwargs):
        """
        EXPERIMENTAL: Create shallow copy of table by replacing schema
        key-value metadata with the indicated new metadata (which may be None,
        which deletes any existing metadata.

        Args:
            metadata (`dict`, defaults to `None`):

        Returns:
            `datasets.table.Table`: shallow_copy
        """
    def add_column(self, *args, **kwargs):
        """
        Add column to Table at position.

        A new table is returned with the column added, the original table
        object is left unchanged.

        Args:
            i (`int`):
                Index to place the column at.
            field_ (`Union[str, pyarrow.Field]`):
                If a string is passed then the type is deduced from the column
                data.
            column (`Union[pyarrow.Array, List[pyarrow.Array]]`):
                Column data.

        Returns:
            `datasets.table.Table`: New table with the passed column added.
        """
    def append_column(self, *args, **kwargs):
        """
        Append column at end of columns.

        Args:
            field_ (`Union[str, pyarrow.Field]`):
                If a string is passed then the type is deduced from the column
                data.
            column (`Union[pyarrow.Array, List[pyarrow.Array]]`):
                Column data.

        Returns:
            `datasets.table.Table`:
                New table with the passed column added.
        """
    def remove_column(self, *args, **kwargs):
        """
        Create new Table with the indicated column removed.

        Args:
            i (`int`):
                Index of column to remove.

        Returns:
            `datasets.table.Table`:
                New table without the column.
        """
    def set_column(self, *args, **kwargs):
        """
        Replace column in Table at position.

        Args:
            i (`int`):
                Index to place the column at.
            field_ (`Union[str, pyarrow.Field]`):
                If a string is passed then the type is deduced from the column
                data.
            column (`Union[pyarrow.Array, List[pyarrow.Array]]`):
                Column data.

        Returns:
            `datasets.table.Table`:
                New table with the passed column set.
        """
    def rename_columns(self, *args, **kwargs):
        """
        Create new table with columns renamed to provided names.
        """
    def drop(self, *args, **kwargs):
        """
        Drop one or more columns and return a new table.

        Args:
            columns (`List[str]`):
                List of field names referencing existing columns.

        Raises:
            `KeyError` : if any of the passed columns name are not existing.

        Returns:
            `datasets.table.Table`:
                New table without the columns.
        """
    def select(self, *args, **kwargs):
        """
        Select columns of the table.

        Returns a new table with the specified columns, and metadata preserved.

        Args:
            columns (:obj:`Union[List[str], List[int]]`):
                The column names or integer indices to select.

        Returns:
            :class:`datasets.table.Table`: New table with the specified columns, and metadata preserved.
        """
TableBlockContainer = TypeVar('TableBlockContainer', TableBlock, List[TableBlock], List[List[TableBlock]])

class ConcatenationTable(Table):
    '''
    The table comes from the concatenation of several tables called blocks.
    It enables concatenation on both axis 0 (append rows) and axis 1 (append columns).

    The underlying tables are called "blocks" and can be either `InMemoryTable`
    or `MemoryMappedTable` objects.
    This allows to combine tables that come from memory or that are memory mapped.
    When a `ConcatenationTable` is pickled, then each block is pickled:
    - the `InMemoryTable` objects are pickled by copying all the data in memory.
    - the MemoryMappedTable objects are pickled without copying the data into memory.
    Instead, only the path to the memory mapped arrow file is pickled, as well as the list
    of transforms to "replays" when reloading the table from the disk.

    Its implementation requires to store each block separately.
    The `blocks` attributes stores a list of list of blocks.
    The first axis concatenates the tables along the axis 0 (it appends rows),
    while the second axis concatenates tables along the axis 1 (it appends columns).

    If some columns are missing when concatenating on axis 0, they are filled with null values.
    This is done using `pyarrow.concat_tables(tables, promote=True)`.

    You can access the fully combined table by accessing the `ConcatenationTable.table` attribute,
    and the blocks by accessing the `ConcatenationTable.blocks` attribute.
    '''
    blocks: Incomplete
    def __init__(self, table: pa.Table, blocks: List[List[TableBlock]]) -> None: ...
    @classmethod
    def from_blocks(cls, blocks: TableBlockContainer) -> ConcatenationTable: ...
    @classmethod
    def from_tables(cls, tables: List[pa.Table | Table], axis: int = 0) -> ConcatenationTable:
        '''Create `ConcatenationTable` from list of tables.

        Args:
            tables (list of `Table` or list of `pyarrow.Table`):
                List of tables.
            axis (`{0, 1}`, defaults to `0`, meaning over rows):
                Axis to concatenate over, where `0` means over rows (vertically) and `1` means over columns
                (horizontally).

                <Added version="1.6.0"/>
        '''
    def slice(self, offset: int = 0, length: Incomplete | None = None):
        """
        Compute zero-copy slice of this Table.

        Args:
            offset (`int`, defaults to `0`):
                Offset from start of table to slice.
            length (`int`, defaults to `None`):
                Length of slice (default is until end of table starting from
                offset).

        Returns:
            `datasets.table.Table`
        """
    def filter(self, mask, *args, **kwargs):
        """
        Select records from a Table. See `pyarrow.compute.filter` for full usage.
        """
    def flatten(self, *args, **kwargs):
        """
        Flatten this Table.  Each column with a struct type is flattened
        into one column per struct field.  Other columns are left unchanged.

        Args:
            memory_pool (`MemoryPool`, defaults to `None`):
                For memory allocations, if required, otherwise use default pool.

        Returns:
            `datasets.table.Table`
        """
    def combine_chunks(self, *args, **kwargs):
        """
        Make a new table by combining the chunks this table has.

        All the underlying chunks in the `ChunkedArray` of each column are
        concatenated into zero or one chunk.

        Args:
            memory_pool (`MemoryPool`, defaults to `None`):
                For memory allocations, if required, otherwise use default pool.

        Returns:
            `datasets.table.Table`
        """
    def cast(self, target_schema, *args, **kwargs):
        """
        Cast table values to another schema.

        Args:
            target_schema (`Schema`):
                Schema to cast to, the names and order of fields must match.
            safe (`bool`, defaults to `True`):
                Check for overflows or other unsafe conversions.

        Returns:
            `datasets.table.Table`
        """
    def replace_schema_metadata(self, *args, **kwargs):
        """
        EXPERIMENTAL: Create shallow copy of table by replacing schema
        key-value metadata with the indicated new metadata (which may be `None`,
        which deletes any existing metadata).

        Args:
            metadata (`dict`, defaults to `None`):

        Returns:
            `datasets.table.Table`: shallow_copy
        """
    def add_column(self, *args, **kwargs) -> None:
        """
        Add column to Table at position.

        A new table is returned with the column added, the original table
        object is left unchanged.

        Args:
            i (`int`):
                Index to place the column at.
            field_ (`Union[str, pyarrow.Field]`):
                If a string is passed then the type is deduced from the column
                data.
            column (`Union[pyarrow.Array, List[pyarrow.Array]]`):
                Column data.

        Returns:
            `datasets.table.Table`: New table with the passed column added.
        """
    def append_column(self, *args, **kwargs) -> None:
        """
        Append column at end of columns.

        Args:
            field_ (`Union[str, pyarrow.Field]`):
                If a string is passed then the type is deduced from the column
                data.
            column (`Union[pyarrow.Array, List[pyarrow.Array]]`):
                Column data.

        Returns:
            `datasets.table.Table`:
                New table with the passed column added.
        """
    def remove_column(self, i, *args, **kwargs):
        """
        Create new Table with the indicated column removed.

        Args:
            i (`int`):
                Index of column to remove.

        Returns:
            `datasets.table.Table`:
                New table without the column.
        """
    def set_column(self, *args, **kwargs) -> None:
        """
        Replace column in Table at position.

        Args:
            i (`int`):
                Index to place the column at.
            field_ (`Union[str, pyarrow.Field]`):
                If a string is passed then the type is deduced from the column
                data.
            column (`Union[pyarrow.Array, List[pyarrow.Array]]`):
                Column data.

        Returns:
            `datasets.table.Table`:
                New table with the passed column set.
        """
    def rename_columns(self, names, *args, **kwargs):
        """
        Create new table with columns renamed to provided names.
        """
    def drop(self, columns, *args, **kwargs):
        """
        Drop one or more columns and return a new table.

        Args:
            columns (`List[str]`):
                List of field names referencing existing columns.

        Raises:
            `KeyError` : if any of the passed columns name are not existing.

        Returns:
            `datasets.table.Table`:
                New table without the columns.
        """
    def select(self, columns, *args, **kwargs):
        """
        Select columns of the table.

        Returns a new table with the specified columns, and metadata preserved.

        Args:
            columns (:obj:`Union[List[str], List[int]]`):
                The column names or integer indices to select.

        Returns:
            :class:`datasets.table.Table`: New table with the specified columns, and metadata preserved.
        """

def concat_tables(tables: List[Table], axis: int = 0) -> Table:
    '''
    Concatenate tables.

    Args:
        tables (list of `Table`):
            List of tables to be concatenated.
        axis (`{0, 1}`, defaults to `0`, meaning over rows):
            Axis to concatenate over, where `0` means over rows (vertically) and `1` means over columns
            (horizontally).

            <Added version="1.6.0"/>
    Returns:
        `datasets.table.Table`:
            If the number of input tables is > 1, then the returned table is a `datasets.table.ConcatenationTable`.
            Otherwise if there\'s only one table, it is returned as is.
    '''
def list_table_cache_files(table: Table) -> List[str]:
    """
    Get the cache files that are loaded by the table.
    Cache file are used when parts of the table come from the disk via memory mapping.

    Returns:
        `List[str]`:
            A list of paths to the cache files loaded by the table.
    """
def array_concat(arrays: List[pa.Array]):
    """Improved version of pa.concat_arrays

    It supports concatenating pa.ExtensionArray objects by concatenating the underlying storages.

    Args:
        arrays (List[pa.Array]): List of arrays to contatenate

    Raises:
        pa.ArrowInvalid: if the arrow array concatenation fails
        ValueError: if the list of arrays is empty
        TypeError: if the arrays to be concatenated have different types

    Returns:
        array (:obj:`pyarrow.Array`): the concatenated array
    """
def array_cast(array: pa.Array, pa_type: pa.DataType, allow_number_to_str: bool = True):
    """Improved version of `pa.Array.cast`

    It supports casting `pa.StructArray` objects to re-order the fields.
    It also let you control certain aspects of the casting, e.g. whether
    to disable numbers (`floats` or `ints`) to strings.

    Args:
        array (`pa.Array`):
            PyArrow array to cast
        pa_type (`pa.DataType`):
            Target PyArrow type
        allow_number_to_str (`bool`, defaults to `True`):
            Whether to allow casting numbers to strings.
            Defaults to `True`.

    Raises:
        `pa.ArrowInvalidError`: if the arrow data casting fails
        `TypeError`: if the target type is not supported according, e.g.

            - if a field is missing
            - if casting from numbers to strings and `allow_number_to_str` is `False`

    Returns:
        `List[pyarrow.Array]`: the casted array
    """
def cast_array_to_feature(array: pa.Array, feature: FeatureType, allow_number_to_str: bool = True):
    '''Cast an array to the arrow type that corresponds to the requested feature type.
    For custom features like [`Audio`] or [`Image`], it takes into account the "cast_storage" methods
    they defined to enable casting from other arrow types.

    Args:
        array (`pa.Array`):
            The PyArrow array to cast.
        feature (`datasets.features.FeatureType`):
            The target feature type.
        allow_number_to_str (`bool`, defaults to `True`):
            Whether to allow casting numbers to strings.
            Defaults to `True`.

    Raises:
        `pa.ArrowInvalidError`: if the arrow data casting fails
        `TypeError`: if the target type is not supported according, e.g.

            - if a field is missing
            - if casting from numbers to strings and `allow_number_to_str` is `False`

    Returns:
        array (`pyarrow.Array`): the casted array
    '''
def embed_array_storage(array: pa.Array, feature: FeatureType):
    '''Embed data into an arrays\'s storage.
    For custom features like Audio or Image, it takes into account the "embed_storage" methods
    they defined to enable embedding external data (e.g. an image file) into an other arrow types.

    <Added version="2.4.0"/>

    Args:
        array (`pa.Array`):
            The PyArrow array in which to embed data.
        feature (`datasets.features.FeatureType`):
            Array features.

    Raises:
        `TypeError`: if the target type is not supported according, e.g.

            - if a field is missing

    Returns:
         array (`pyarrow.Array`): the casted array
    '''
def cast_table_to_features(table: pa.Table, features: Features):
    """Cast a table to the arrow schema that corresponds to the requested features.

    Args:
        table (`pyarrow.Table`):
            PyArrow table to cast.
        features ([`Features`]):
            Target features.

    Returns:
        table (`pyarrow.Table`): the casted table
    """
def cast_table_to_schema(table: pa.Table, schema: pa.Schema):
    """Cast a table to the arrow schema. Different from `cast_table_to_features`, this method can preserve nullability.

    Args:
        table (`pa.Table`):
            PyArrow table to cast.
        features ([`Features`]):
            Target features.

    Returns:
        `pa.Table`: the casted table
    """
def embed_table_storage(table: pa.Table):
    '''Embed external data into a table\'s storage.

    <Added version="2.4.0"/>

    Args:
        table (`pyarrow.Table`):
            PyArrow table in which to embed data.

    Returns:
        table (`pyarrow.Table`): the table with embedded data
    '''
def table_cast(table: pa.Table, schema: pa.Schema):
    """Improved version of `pa.Table.cast`.

    It supports casting to feature types stored in the schema metadata.

    Args:
        table (`pyarrow.Table`):
            PyArrow table to cast.
        schema (`pyarrow.Schema`):
            Target PyArrow schema.

    Returns:
        table (`pyarrow.Table`): the casted table
    """
def table_flatten(table: pa.Table):
    """Improved version of `pa.Table.flatten`.

    It behaves as `pa.Table.flatten` in a sense it does 1-step flatten of the columns with a struct type into one column per struct field,
    but updates the metadata and skips decodable features unless the `decode` attribute of these features is set to False.

    Args:
        table (`pa.Table`):
            PyArrow table to flatten.

    Returns:
        `Table`: the flattened table
    """
def table_visitor(table: pa.Table, function: Callable[[pa.Array], None]):
    """Visit all arrays in a table and apply a function to them.

    Args:
        table (`pyarrow.Table`):
            PyArrow table to visit.
        function (`Callable[[pa.Array], None]`):
            Function to apply to each array.
    """
def table_iter(table: Table, batch_size: int, drop_last_batch: bool = False) -> Iterator[pa.Table]:
    """Iterate over sub-tables of size `batch_size`.

    Args:
        table (`pyarrow.Table`):
            PyArrow table to iterate over.
        batch_size (`int`):
            Size of each sub-table to yield.
        drop_last_batch (`bool`, defaults to `False`):
            Drop the last batch if it is smaller than `batch_size`.
    """
