import pyarrow.lib as lib
from _typeshed import Incomplete
from pyarrow.lib import IpcReadOptions as IpcReadOptions, IpcWriteOptions as IpcWriteOptions, Message as Message, MessageReader as MessageReader, MetadataVersion as MetadataVersion, ReadStats as ReadStats, RecordBatchReader as RecordBatchReader, WriteStats as WriteStats, get_record_batch_size as get_record_batch_size, get_tensor_size as get_tensor_size, read_message as read_message, read_record_batch as read_record_batch, read_schema as read_schema, read_tensor as read_tensor, write_tensor as write_tensor

class RecordBatchStreamReader(lib._RecordBatchStreamReader):
    """
    Reader for the Arrow streaming binary format.

    Parameters
    ----------
    source : bytes/buffer-like, pyarrow.NativeFile, or file-like Python object
        Either an in-memory buffer, or a readable file object.
        If you want to use memory map use MemoryMappedFile as source.
    options : pyarrow.ipc.IpcReadOptions
        Options for IPC deserialization.
        If None, default values will be used.
    memory_pool : MemoryPool, default None
        If None, default memory pool is used.
    """
    def __init__(self, source, *, options: Incomplete | None = None, memory_pool: Incomplete | None = None) -> None: ...

class RecordBatchStreamWriter(lib._RecordBatchStreamWriter):
    __doc__: Incomplete
    def __init__(self, sink, schema, *, use_legacy_format: Incomplete | None = None, options: Incomplete | None = None) -> None: ...

class RecordBatchFileReader(lib._RecordBatchFileReader):
    """
    Class for reading Arrow record batch data from the Arrow binary file format

    Parameters
    ----------
    source : bytes/buffer-like, pyarrow.NativeFile, or file-like Python object
        Either an in-memory buffer, or a readable file object.
        If you want to use memory map use MemoryMappedFile as source.
    footer_offset : int, default None
        If the file is embedded in some larger file, this is the byte offset to
        the very end of the file data
    options : pyarrow.ipc.IpcReadOptions
        Options for IPC serialization.
        If None, default values will be used.
    memory_pool : MemoryPool, default None
        If None, default memory pool is used.
    """
    def __init__(self, source, footer_offset: Incomplete | None = None, *, options: Incomplete | None = None, memory_pool: Incomplete | None = None) -> None: ...

class RecordBatchFileWriter(lib._RecordBatchFileWriter):
    __doc__: Incomplete
    def __init__(self, sink, schema, *, use_legacy_format: Incomplete | None = None, options: Incomplete | None = None) -> None: ...

def new_stream(sink, schema, *, use_legacy_format: Incomplete | None = None, options: Incomplete | None = None): ...
def open_stream(source, *, options: Incomplete | None = None, memory_pool: Incomplete | None = None):
    """
    Create reader for Arrow streaming format.

    Parameters
    ----------
    source : bytes/buffer-like, pyarrow.NativeFile, or file-like Python object
        Either an in-memory buffer, or a readable file object.
    options : pyarrow.ipc.IpcReadOptions
        Options for IPC serialization.
        If None, default values will be used.
    memory_pool : MemoryPool, default None
        If None, default memory pool is used.

    Returns
    -------
    reader : RecordBatchStreamReader
        A reader for the given source
    """
def new_file(sink, schema, *, use_legacy_format: Incomplete | None = None, options: Incomplete | None = None): ...
def open_file(source, footer_offset: Incomplete | None = None, *, options: Incomplete | None = None, memory_pool: Incomplete | None = None):
    """
    Create reader for Arrow file format.

    Parameters
    ----------
    source : bytes/buffer-like, pyarrow.NativeFile, or file-like Python object
        Either an in-memory buffer, or a readable file object.
    footer_offset : int, default None
        If the file is embedded in some larger file, this is the byte offset to
        the very end of the file data.
    options : pyarrow.ipc.IpcReadOptions
        Options for IPC serialization.
        If None, default values will be used.
    memory_pool : MemoryPool, default None
        If None, default memory pool is used.

    Returns
    -------
    reader : RecordBatchFileReader
        A reader for the given source
    """
def serialize_pandas(df, *, nthreads: Incomplete | None = None, preserve_index: Incomplete | None = None):
    """
    Serialize a pandas DataFrame into a buffer protocol compatible object.

    Parameters
    ----------
    df : pandas.DataFrame
    nthreads : int, default None
        Number of threads to use for conversion to Arrow, default all CPUs.
    preserve_index : bool, default None
        The default of None will store the index as a column, except for
        RangeIndex which is stored as metadata only. If True, always
        preserve the pandas index data as a column. If False, no index
        information is saved and the result will have a default RangeIndex.

    Returns
    -------
    buf : buffer
        An object compatible with the buffer protocol.
    """
def deserialize_pandas(buf, *, use_threads: bool = True):
    """Deserialize a buffer protocol compatible object into a pandas DataFrame.

    Parameters
    ----------
    buf : buffer
        An object compatible with the buffer protocol.
    use_threads : bool, default True
        Whether to parallelize the conversion using multiple threads.

    Returns
    -------
    df : pandas.DataFrame
        The buffer deserialized as pandas DataFrame
    """
