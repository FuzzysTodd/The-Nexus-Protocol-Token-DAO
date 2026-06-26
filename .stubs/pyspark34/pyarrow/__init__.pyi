from pyarrow._hdfsio import HdfsFile as HdfsFile, have_libhdfs as have_libhdfs
from pyarrow.ipc import Message as Message, MessageReader as MessageReader, MetadataVersion as MetadataVersion, RecordBatchFileReader as RecordBatchFileReader, RecordBatchFileWriter as RecordBatchFileWriter, RecordBatchStreamReader as RecordBatchStreamReader, RecordBatchStreamWriter as RecordBatchStreamWriter, deserialize_pandas as deserialize_pandas, serialize_pandas as serialize_pandas
from pyarrow.lib import Array as Array, ArrowCancelled as ArrowCancelled, ArrowCapacityError as ArrowCapacityError, ArrowException as ArrowException, ArrowIOError as ArrowIOError, ArrowIndexError as ArrowIndexError, ArrowInvalid as ArrowInvalid, ArrowKeyError as ArrowKeyError, ArrowMemoryError as ArrowMemoryError, ArrowNotImplementedError as ArrowNotImplementedError, ArrowSerializationError as ArrowSerializationError, ArrowTypeError as ArrowTypeError, BaseExtensionType as BaseExtensionType, BinaryArray as BinaryArray, BinaryScalar as BinaryScalar, BooleanArray as BooleanArray, BooleanScalar as BooleanScalar, Buffer as Buffer, BufferOutputStream as BufferOutputStream, BufferReader as BufferReader, BufferedInputStream as BufferedInputStream, BufferedOutputStream as BufferedOutputStream, BuildInfo as BuildInfo, ChunkedArray as ChunkedArray, Codec as Codec, CompressedInputStream as CompressedInputStream, CompressedOutputStream as CompressedOutputStream, DataType as DataType, Date32Array as Date32Array, Date32Scalar as Date32Scalar, Date64Array as Date64Array, Date64Scalar as Date64Scalar, Decimal128Array as Decimal128Array, Decimal128Scalar as Decimal128Scalar, Decimal128Type as Decimal128Type, Decimal256Array as Decimal256Array, Decimal256Scalar as Decimal256Scalar, Decimal256Type as Decimal256Type, DenseUnionType as DenseUnionType, DictionaryArray as DictionaryArray, DictionaryMemo as DictionaryMemo, DictionaryScalar as DictionaryScalar, DictionaryType as DictionaryType, DoubleScalar as DoubleScalar, DurationArray as DurationArray, DurationScalar as DurationScalar, DurationType as DurationType, ExtensionArray as ExtensionArray, ExtensionScalar as ExtensionScalar, ExtensionType as ExtensionType, Field as Field, FixedShapeTensorArray as FixedShapeTensorArray, FixedShapeTensorType as FixedShapeTensorType, FixedSizeBinaryArray as FixedSizeBinaryArray, FixedSizeBinaryScalar as FixedSizeBinaryScalar, FixedSizeBinaryType as FixedSizeBinaryType, FixedSizeBufferWriter as FixedSizeBufferWriter, FixedSizeListArray as FixedSizeListArray, FixedSizeListScalar as FixedSizeListScalar, FixedSizeListType as FixedSizeListType, FloatScalar as FloatScalar, FloatingPointArray as FloatingPointArray, HalfFloatScalar as HalfFloatScalar, Int16Array as Int16Array, Int16Scalar as Int16Scalar, Int32Array as Int32Array, Int32Scalar as Int32Scalar, Int64Array as Int64Array, Int64Scalar as Int64Scalar, Int8Array as Int8Array, Int8Scalar as Int8Scalar, IntegerArray as IntegerArray, KeyValueMetadata as KeyValueMetadata, LargeBinaryArray as LargeBinaryArray, LargeBinaryScalar as LargeBinaryScalar, LargeListArray as LargeListArray, LargeListScalar as LargeListScalar, LargeListType as LargeListType, LargeStringArray as LargeStringArray, LargeStringScalar as LargeStringScalar, ListArray as ListArray, ListScalar as ListScalar, ListType as ListType, LoggingMemoryPool as LoggingMemoryPool, MapArray as MapArray, MapScalar as MapScalar, MapType as MapType, MemoryMappedFile as MemoryMappedFile, MemoryPool as MemoryPool, MockOutputStream as MockOutputStream, MonthDayNano as MonthDayNano, MonthDayNanoIntervalArray as MonthDayNanoIntervalArray, MonthDayNanoIntervalScalar as MonthDayNanoIntervalScalar, NA as NA, NativeFile as NativeFile, NullArray as NullArray, NullScalar as NullScalar, NumericArray as NumericArray, OSFile as OSFile, ProxyMemoryPool as ProxyMemoryPool, PyExtensionType as PyExtensionType, PythonFile as PythonFile, RecordBatch as RecordBatch, RecordBatchReader as RecordBatchReader, ResizableBuffer as ResizableBuffer, RunEndEncodedArray as RunEndEncodedArray, RunEndEncodedScalar as RunEndEncodedScalar, RunEndEncodedType as RunEndEncodedType, RuntimeInfo as RuntimeInfo, Scalar as Scalar, Schema as Schema, SparseCOOTensor as SparseCOOTensor, SparseCSCMatrix as SparseCSCMatrix, SparseCSFTensor as SparseCSFTensor, SparseCSRMatrix as SparseCSRMatrix, SparseUnionType as SparseUnionType, StringArray as StringArray, StringScalar as StringScalar, StructArray as StructArray, StructScalar as StructScalar, StructType as StructType, Table as Table, TableGroupBy as TableGroupBy, Tensor as Tensor, Time32Array as Time32Array, Time32Scalar as Time32Scalar, Time32Type as Time32Type, Time64Array as Time64Array, Time64Scalar as Time64Scalar, Time64Type as Time64Type, TimestampArray as TimestampArray, TimestampScalar as TimestampScalar, TimestampType as TimestampType, TransformInputStream as TransformInputStream, UInt16Array as UInt16Array, UInt16Scalar as UInt16Scalar, UInt32Array as UInt32Array, UInt32Scalar as UInt32Scalar, UInt64Array as UInt64Array, UInt64Scalar as UInt64Scalar, UInt8Array as UInt8Array, UInt8Scalar as UInt8Scalar, UnionArray as UnionArray, UnionScalar as UnionScalar, UnionType as UnionType, UnknownExtensionType as UnknownExtensionType, VersionInfo as VersionInfo, allocate_buffer as allocate_buffer, array as array, binary as binary, bool_ as bool_, chunked_array as chunked_array, compress as compress, concat_arrays as concat_arrays, concat_tables as concat_tables, cpp_build_info as cpp_build_info, cpp_version as cpp_version, cpp_version_info as cpp_version_info, cpu_count as cpu_count, create_memory_map as create_memory_map, date32 as date32, date64 as date64, decimal128 as decimal128, decimal256 as decimal256, decompress as decompress, default_memory_pool as default_memory_pool, dense_union as dense_union, dictionary as dictionary, duration as duration, enable_signal_handlers as enable_signal_handlers, field as field, fixed_shape_tensor as fixed_shape_tensor, float16 as float16, float32 as float32, float64 as float64, foreign_buffer as foreign_buffer, from_numpy_dtype as from_numpy_dtype, infer_type as infer_type, input_stream as input_stream, int16 as int16, int32 as int32, int64 as int64, int8 as int8, io_thread_count as io_thread_count, jemalloc_memory_pool as jemalloc_memory_pool, jemalloc_set_decay_ms as jemalloc_set_decay_ms, large_binary as large_binary, large_list as large_list, large_string as large_string, large_utf8 as large_utf8, list_ as list_, log_memory_allocations as log_memory_allocations, logging_memory_pool as logging_memory_pool, map_ as map_, memory_map as memory_map, mimalloc_memory_pool as mimalloc_memory_pool, month_day_nano_interval as month_day_nano_interval, null as null, nulls as nulls, output_stream as output_stream, proxy_memory_pool as proxy_memory_pool, py_buffer as py_buffer, record_batch as record_batch, register_extension_type as register_extension_type, repeat as repeat, run_end_encoded as run_end_encoded, runtime_info as runtime_info, scalar as scalar, schema as schema, set_cpu_count as set_cpu_count, set_io_thread_count as set_io_thread_count, set_memory_pool as set_memory_pool, sparse_union as sparse_union, string as string, struct as struct, supported_memory_backends as supported_memory_backends, system_memory_pool as system_memory_pool, table as table, time32 as time32, time64 as time64, timestamp as timestamp, total_allocated_bytes as total_allocated_bytes, transcoding_input_stream as transcoding_input_stream, type_for_alias as type_for_alias, uint16 as uint16, uint32 as uint32, uint64 as uint64, uint8 as uint8, unify_schemas as unify_schemas, union as union, unregister_extension_type as unregister_extension_type, utf8 as utf8

def parse_git(root, **kwargs):
    """
            Parse function for setuptools_scm that ignores tags for non-C++
            subprojects, e.g. apache-arrow-js-XXX tags.
            """
def show_versions() -> None:
    """
    Print various version information, to help with error reporting.
    """
def show_info() -> None:
    """
    Print detailed version and platform information, for error reporting
    """
def __getattr__(name): ...
def get_include():
    """
    Return absolute path to directory containing Arrow C++ include
    headers. Similar to numpy.get_include
    """
def get_libraries():
    """
    Return list of library names to include in the `libraries` argument for C
    or Cython extensions using pyarrow
    """
def create_library_symlinks():
    """
    With Linux and macOS wheels, the bundled shared libraries have an embedded
    ABI version like libarrow.so.17 or libarrow.17.dylib and so linking to them
    with -larrow won't work unless we create symlinks at locations like
    site-packages/pyarrow/libarrow.so. This unfortunate workaround addresses
    prior problems we had with shipping two copies of the shared libraries to
    permit third party projects like turbodbc to build their C++ extensions
    against the pyarrow wheels.

    This function must only be invoked once and only when the shared libraries
    are bundled with the Python package, which should only apply to wheel-based
    installs. It requires write access to the site-packages/pyarrow directory
    and so depending on your system may need to be run with root.
    """
def get_library_dirs():
    """
    Return lists of directories likely to contain Arrow C++ libraries for
    linking C or Cython extensions using pyarrow
    """
