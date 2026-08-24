import pyarrow as pa
from . import config as config
from .features import Features as Features, Image as Image, Value as Value
from .features.features import FeatureType as FeatureType, cast_to_python_objects as cast_to_python_objects, generate_from_arrow_type as generate_from_arrow_type, get_nested_type as get_nested_type, list_of_np_array_to_pyarrow_listarray as list_of_np_array_to_pyarrow_listarray, numpy_to_pyarrow_listarray as numpy_to_pyarrow_listarray, to_pyarrow_listarray as to_pyarrow_listarray
from .filesystems import is_remote_filesystem as is_remote_filesystem
from .info import DatasetInfo as DatasetInfo
from .keyhash import DuplicatedKeysError as DuplicatedKeysError, KeyHasher as KeyHasher
from .table import array_cast as array_cast, array_concat as array_concat, cast_array_to_feature as cast_array_to_feature, embed_table_storage as embed_table_storage, table_cast as table_cast
from .utils import logging as logging
from .utils.file_utils import hash_url_to_filename as hash_url_to_filename
from .utils.py_utils import asdict as asdict, first_non_null_value as first_non_null_value
from _typeshed import Incomplete
from typing import Any, Dict, Iterable, List

logger: Incomplete
type_ = type

class SchemaInferenceError(ValueError): ...

class TypedSequence:
    '''
    This data container generalizes the typing when instantiating pyarrow arrays, tables or batches.

    More specifically it adds several features:
    - Support extension types like ``datasets.features.Array2DExtensionType``:
        By default pyarrow arrays don\'t return extension arrays. One has to call
        ``pa.ExtensionArray.from_storage(type, pa.array(data, type.storage_type))``
        in order to get an extension array.
    - Support for ``try_type`` parameter that can be used instead of ``type``:
        When an array is transformed, we like to keep the same type as before if possible.
        For example when calling :func:`datasets.Dataset.map`, we don\'t want to change the type
        of each column by default.
    - Better error message when a pyarrow array overflows.

    Example::

        from datasets.features import Array2D, Array2DExtensionType, Value
        from datasets.arrow_writer import TypedSequence
        import pyarrow as pa

        arr = pa.array(TypedSequence([1, 2, 3], type=Value("int32")))
        assert arr.type == pa.int32()

        arr = pa.array(TypedSequence([1, 2, 3], try_type=Value("int32")))
        assert arr.type == pa.int32()

        arr = pa.array(TypedSequence(["foo", "bar"], try_type=Value("int32")))
        assert arr.type == pa.string()

        arr = pa.array(TypedSequence([[[1, 2, 3]]], type=Array2D((1, 3), "int64")))
        assert arr.type == Array2DExtensionType((1, 3), "int64")

        table = pa.Table.from_pydict({
            "image": TypedSequence([[[1, 2, 3]]], type=Array2D((1, 3), "int64"))
        })
        assert table["image"].type == Array2DExtensionType((1, 3), "int64")

    '''
    data: Incomplete
    type: Incomplete
    try_type: Incomplete
    optimized_int_type: Incomplete
    trying_type: Incomplete
    trying_int_optimization: Incomplete
    def __init__(self, data: Iterable, type: FeatureType | None = None, try_type: FeatureType | None = None, optimized_int_type: FeatureType | None = None) -> None: ...
    def get_inferred_type(self) -> FeatureType:
        """Return the inferred feature type.
        This is done by converting the sequence to an Arrow array, and getting the corresponding
        feature type.

        Since building the Arrow array can be expensive, the value of the inferred type is cached
        as soon as pa.array is called on the typed sequence.

        Returns:
            FeatureType: inferred feature type of the sequence.
        """
    def __arrow_array__(self, type: pa.DataType | None = None):
        """This function is called when calling pa.array(typed_sequence)"""

class OptimizedTypedSequence(TypedSequence):
    def __init__(self, data, type: FeatureType | None = None, try_type: FeatureType | None = None, col: str | None = None, optimized_int_type: FeatureType | None = None) -> None: ...

class ArrowWriter:
    """Shuffles and writes Examples to Arrow files."""
    stream: Incomplete
    fingerprint: Incomplete
    disable_nullable: Incomplete
    writer_batch_size: Incomplete
    update_features: Incomplete
    with_metadata: Incomplete
    unit: Incomplete
    embed_local_files: Incomplete
    current_examples: Incomplete
    current_rows: Incomplete
    pa_writer: Incomplete
    hkey_record: Incomplete
    def __init__(self, schema: pa.Schema | None = None, features: Features | None = None, path: str | None = None, stream: pa.NativeFile | None = None, fingerprint: str | None = None, writer_batch_size: int | None = None, hash_salt: str | None = None, check_duplicates: bool | None = False, disable_nullable: bool = False, update_features: bool = False, with_metadata: bool = True, unit: str = 'examples', embed_local_files: bool = False, storage_options: dict | None = None) -> None: ...
    def __len__(self) -> int:
        """Return the number of writed and staged examples"""
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def close(self) -> None: ...
    @property
    def schema(self): ...
    def write_examples_on_file(self) -> None:
        """Write stored examples from the write-pool of examples. It makes a table out of the examples and write it."""
    def write_rows_on_file(self) -> None:
        """Write stored rows from the write-pool of rows. It concatenates the single-row tables and it writes the resulting table."""
    def write(self, example: Dict[str, Any], key: str | int | bytes | None = None, writer_batch_size: int | None = None):
        """Add a given (Example,Key) pair to the write-pool of examples which is written to file.

        Args:
            example: the Example to add.
            key: Optional, a unique identifier(str, int or bytes) associated with each example
        """
    def check_duplicate_keys(self) -> None:
        """Raises error if duplicates found in a batch"""
    def write_row(self, row: pa.Table, writer_batch_size: int | None = None):
        """Add a given single-row Table to the write-pool of rows which is written to file.

        Args:
            row: the row to add.
        """
    def write_batch(self, batch_examples: Dict[str, List], writer_batch_size: int | None = None):
        """Write a batch of Example to file.
        Ignores the batch if it appears to be empty,
        preventing a potential schema update of unknown types.

        Args:
            batch_examples: the batch of examples to add.
        """
    def write_table(self, pa_table: pa.Table, writer_batch_size: int | None = None):
        """Write a Table to file.

        Args:
            example: the Table to add.
        """
    def finalize(self, close_stream: bool = True): ...

class ParquetWriter(ArrowWriter): ...

class BeamWriter:
    """
    Shuffles and writes Examples to Arrow files.
    The Arrow files are converted from Parquet files that are the output of Apache Beam pipelines.
    """
    def __init__(self, features: Features | None = None, schema: pa.Schema | None = None, path: str | None = None, namespace: str | None = None, cache_dir: str | None = None) -> None: ...
    def write_from_pcollection(self, pcoll_examples):
        """Add the final steps of the beam pipeline: write to parquet files."""
    def finalize(self, metrics_query_result: dict):
        """
        Run after the pipeline has finished.
        It converts the resulting parquet files to arrow and it completes the info from the pipeline metrics.

        Args:
            metrics_query_result: `dict` obtained from pipeline_results.metrics().query(m_filter). Make sure
                that the filter keeps only the metrics for the considered split, under the namespace `split_name`.
        """

def get_parquet_lengths(sources) -> List[int]: ...
def parquet_to_arrow(source, destination) -> List[int]:
    """Convert parquet file to arrow file. Inputs can be str paths or file-like objects"""
