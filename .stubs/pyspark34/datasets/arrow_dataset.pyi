import numpy as np
import pandas as pd
import pyarrow as pa
import pyspark
import sqlalchemy
import sqlite3
from . import config as config
from .arrow_reader import ArrowReader as ArrowReader
from .arrow_writer import ArrowWriter as ArrowWriter, OptimizedTypedSequence as OptimizedTypedSequence
from .data_files import sanitize_patterns as sanitize_patterns
from .dataset_dict import DatasetDict as DatasetDict
from .download.download_config import DownloadConfig as DownloadConfig
from .download.streaming_download_manager import xgetsize as xgetsize
from .features import Audio as Audio, ClassLabel as ClassLabel, Features as Features, Image as Image, Sequence as Sequence, Value as Value
from .features.features import FeatureType as FeatureType, generate_from_arrow_type as generate_from_arrow_type, pandas_types_mapper as pandas_types_mapper, require_decoding as require_decoding
from .filesystems import extract_path_from_uri as extract_path_from_uri, is_remote_filesystem as is_remote_filesystem
from .fingerprint import fingerprint_transform as fingerprint_transform, format_kwargs_for_fingerprint as format_kwargs_for_fingerprint, format_transform_for_fingerprint as format_transform_for_fingerprint, generate_fingerprint as generate_fingerprint, generate_random_fingerprint as generate_random_fingerprint, get_temporary_cache_files_directory as get_temporary_cache_files_directory, is_caching_enabled as is_caching_enabled, maybe_register_dataset_for_temp_dir_deletion as maybe_register_dataset_for_temp_dir_deletion, update_fingerprint as update_fingerprint, validate_fingerprint as validate_fingerprint
from .formatting import format_table as format_table, get_format_type_from_alias as get_format_type_from_alias, get_formatter as get_formatter, query_table as query_table
from .formatting.formatting import LazyDict as LazyDict
from .info import DatasetInfo as DatasetInfo, DatasetInfosDict as DatasetInfosDict
from .iterable_dataset import IterableDataset as IterableDataset
from .search import IndexableMixin as IndexableMixin
from .splits import NamedSplit as NamedSplit, Split as Split, SplitDict as SplitDict, SplitInfo as SplitInfo
from .table import InMemoryTable as InMemoryTable, MemoryMappedTable as MemoryMappedTable, Table as Table, cast_array_to_feature as cast_array_to_feature, concat_tables as concat_tables, embed_table_storage as embed_table_storage, list_table_cache_files as list_table_cache_files, table_cast as table_cast, table_iter as table_iter, table_visitor as table_visitor
from .tasks import TaskTemplate as TaskTemplate
from .utils import logging as logging
from .utils.deprecation_utils import deprecated as deprecated
from .utils.file_utils import cached_path as cached_path, estimate_dataset_size as estimate_dataset_size
from .utils.hub import hf_hub_url as hf_hub_url
from .utils.info_utils import is_small_dataset as is_small_dataset
from .utils.metadata import MetadataConfigs as MetadataConfigs
from .utils.py_utils import Literal as Literal, asdict as asdict, convert_file_size_to_int as convert_file_size_to_int, glob_pattern_to_regex as glob_pattern_to_regex, iflatmap_unordered as iflatmap_unordered, string_to_dict as string_to_dict, unique_values as unique_values
from .utils.stratify import stratified_shuffle_split_generate_indices as stratified_shuffle_split_generate_indices
from .utils.tf_utils import dataset_to_tf as dataset_to_tf, minimal_tf_collate_fn as minimal_tf_collate_fn, multiprocess_dataset_to_tf as multiprocess_dataset_to_tf
from .utils.typing import ListLike as ListLike, PathLike as PathLike
from _typeshed import Incomplete
from typing import Any, BinaryIO, Callable, Dict, Iterable, Iterator, List, Sequence as Sequence_, Tuple, overload

logger: Incomplete
PUSH_TO_HUB_WITHOUT_METADATA_CONFIGS_SPLIT_PATTERN_SHARDED: str

class DatasetInfoMixin:
    """This base class exposes some attributes of DatasetInfo
    at the base level of the Dataset for easy access.
    """
    def __init__(self, info: DatasetInfo, split: NamedSplit | None) -> None: ...
    @property
    def info(self):
        """[`~datasets.DatasetInfo`] object containing all the metadata in the dataset."""
    @property
    def split(self):
        """[`~datasets.NamedSplit`] object corresponding to a named dataset split."""
    @property
    def builder_name(self) -> str: ...
    @property
    def citation(self) -> str: ...
    @property
    def config_name(self) -> str: ...
    @property
    def dataset_size(self) -> int | None: ...
    @property
    def description(self) -> str: ...
    @property
    def download_checksums(self) -> dict | None: ...
    @property
    def download_size(self) -> int | None: ...
    @property
    def features(self) -> Features | None: ...
    @property
    def homepage(self) -> str | None: ...
    @property
    def license(self) -> str | None: ...
    @property
    def size_in_bytes(self) -> int | None: ...
    @property
    def supervised_keys(self): ...
    @property
    def task_templates(self): ...
    @property
    def version(self): ...

class TensorflowDatasetMixin:
    def to_tf_dataset(self, batch_size: int | None = None, columns: str | List[str] | None = None, shuffle: bool = False, collate_fn: Callable | None = None, drop_remainder: bool = False, collate_fn_args: Dict[str, Any] | None = None, label_cols: str | List[str] | None = None, prefetch: bool = True, num_workers: int = 0, num_test_batches: int = 20):
        '''Create a `tf.data.Dataset` from the underlying Dataset. This `tf.data.Dataset` will load and collate batches from
        the Dataset, and is suitable for passing to methods like `model.fit()` or `model.predict()`. The dataset will yield
        `dicts` for both inputs and labels unless the `dict` would contain only a single key, in which case a raw
        `tf.Tensor` is yielded instead.

        Args:
            batch_size (`int`, *optional*):
                Size of batches to load from the dataset. Defaults to `None`, which implies that the dataset won\'t be
                batched, but the returned dataset can be batched later with `tf_dataset.batch(batch_size)`.
            columns (`List[str]` or `str`, *optional*):
                Dataset column(s) to load in the `tf.data.Dataset`.
                Column names that are created by the `collate_fn` and that do not exist in the original dataset can be used.
            shuffle(`bool`, defaults to `False`):
                Shuffle the dataset order when loading. Recommended `True` for training, `False` for
                validation/evaluation.
            drop_remainder(`bool`, defaults to `False`):
                Drop the last incomplete batch when loading. Ensures
                that all batches yielded by the dataset will have the same length on the batch dimension.
            collate_fn(`Callable`, *optional*):
                A function or callable object (such as a `DataCollator`) that will collate
                lists of samples into a batch.
            collate_fn_args (`Dict`, *optional*):
                An optional `dict` of keyword arguments to be passed to the
                `collate_fn`.
            label_cols (`List[str]` or `str`, defaults to `None`):
                Dataset column(s) to load as labels.
                Note that many models compute loss internally rather than letting Keras do it, in which case
                passing the labels here is optional, as long as they\'re in the input `columns`.
            prefetch (`bool`, defaults to `True`):
                Whether to run the dataloader in a separate thread and maintain
                a small buffer of batches for training. Improves performance by allowing data to be loaded in the
                background while the model is training.
            num_workers (`int`, defaults to `0`):
                Number of workers to use for loading the dataset. Only supported on Python versions >= 3.8.
            num_test_batches (`int`, defaults to `20`):
                Number of batches to use to infer the output signature of the dataset.
                The higher this number, the more accurate the signature will be, but the longer it will take to
                create the dataset.

        Returns:
            `tf.data.Dataset`

        Example:

        ```py
        >>> ds_train = ds["train"].to_tf_dataset(
        ...    columns=[\'input_ids\', \'token_type_ids\', \'attention_mask\', \'label\'],
        ...    shuffle=True,
        ...    batch_size=16,
        ...    collate_fn=data_collator,
        ... )
        ```
        '''

class DatasetTransformationNotAllowedError(Exception): ...

def transmit_format(func):
    """Wrapper for dataset transforms that recreate a new Dataset to transmit the format of the original dataset to the new dataset"""
def transmit_tasks(func):
    """Wrapper for dataset transforms that recreate a new Dataset to transmit the task templates of the original dataset to the new dataset"""
def update_metadata_with_features(table: Table, features: Features):
    """To be used in dataset transforms that modify the features of the dataset, in order to update the features stored in the metadata of its schema."""

class NonExistentDatasetError(Exception):
    """Used when we expect the existence of a dataset"""

class Dataset(DatasetInfoMixin, IndexableMixin, TensorflowDatasetMixin):
    """A Dataset backed by an Arrow table."""
    def __init__(self, arrow_table: Table, info: DatasetInfo | None = None, split: NamedSplit | None = None, indices_table: Table | None = None, fingerprint: str | None = None) -> None: ...
    @property
    def features(self) -> Features: ...
    @classmethod
    def from_file(cls, filename: str, info: DatasetInfo | None = None, split: NamedSplit | None = None, indices_filename: str | None = None, in_memory: bool = False) -> Dataset:
        """Instantiate a Dataset backed by an Arrow table at filename.

        Args:
            filename (`str`):
                File name of the dataset.
            info (`DatasetInfo`, *optional*):
                Dataset information, like description, citation, etc.
            split (`NamedSplit`, *optional*):
                Name of the dataset split.
            indices_filename (`str`, *optional*):
                File names of the indices.
            in_memory (`bool`, defaults to `False`):
                Whether to copy the data in-memory.

        Returns:
            [`Dataset`]
        """
    @classmethod
    def from_buffer(cls, buffer: pa.Buffer, info: DatasetInfo | None = None, split: NamedSplit | None = None, indices_buffer: pa.Buffer | None = None) -> Dataset:
        """Instantiate a Dataset backed by an Arrow buffer.

        Args:
            buffer (`pyarrow.Buffer`):
                Arrow buffer.
            info (`DatasetInfo`, *optional*):
                Dataset information, like description, citation, etc.
            split (`NamedSplit`, *optional*):
                Name of the dataset split.
            indices_buffer (`pyarrow.Buffer`, *optional*):
                Indices Arrow buffer.

        Returns:
            [`Dataset`]
        """
    @classmethod
    def from_pandas(cls, df: pd.DataFrame, features: Features | None = None, info: DatasetInfo | None = None, split: NamedSplit | None = None, preserve_index: bool | None = None) -> Dataset:
        """
        Convert `pandas.DataFrame` to a `pyarrow.Table` to create a [`Dataset`].

        The column types in the resulting Arrow Table are inferred from the dtypes of the `pandas.Series` in the
        DataFrame. In the case of non-object Series, the NumPy dtype is translated to its Arrow equivalent. In the
        case of `object`, we need to guess the datatype by looking at the Python objects in this Series.

        Be aware that Series of the `object` dtype don't carry enough information to always lead to a meaningful Arrow
        type. In the case that we cannot infer a type, e.g. because the DataFrame is of length 0 or the Series only
        contains `None/nan` objects, the type is set to `null`. This behavior can be avoided by constructing explicit
        features and passing it to this function.

        Args:
            df (`pandas.DataFrame`):
                Dataframe that contains the dataset.
            features ([`Features`], *optional*):
                Dataset features.
            info (`DatasetInfo`, *optional*):
                Dataset information, like description, citation, etc.
            split (`NamedSplit`, *optional*):
                Name of the dataset split.
            preserve_index (`bool`, *optional*):
                Whether to store the index as an additional column in the resulting Dataset.
                The default of `None` will store the index as a column, except for `RangeIndex` which is stored as metadata only.
                Use `preserve_index=True` to force it to be stored as a column.

        Returns:
            [`Dataset`]

        Example:

        ```py
        >>> ds = Dataset.from_pandas(df)
        ```
        """
    @classmethod
    def from_dict(cls, mapping: dict, features: Features | None = None, info: DatasetInfo | None = None, split: NamedSplit | None = None) -> Dataset:
        """
        Convert `dict` to a `pyarrow.Table` to create a [`Dataset`].

        Args:
            mapping (`Mapping`):
                Mapping of strings to Arrays or Python lists.
            features ([`Features`], *optional*):
                Dataset features.
            info (`DatasetInfo`, *optional*):
                Dataset information, like description, citation, etc.
            split (`NamedSplit`, *optional*):
                Name of the dataset split.

        Returns:
            [`Dataset`]
        """
    @classmethod
    def from_list(cls, mapping: List[dict], features: Features | None = None, info: DatasetInfo | None = None, split: NamedSplit | None = None) -> Dataset:
        """
        Convert a list of dicts to a `pyarrow.Table` to create a [`Dataset`]`.

        Note that the keys of the first entry will be used to determine the dataset columns,
        regardless of what is passed to features.

        Args:
            mapping (`List[dict]`): A list of mappings of strings to row values.
            features (`Features`, optional): Dataset features.
            info (`DatasetInfo`, optional): Dataset information, like description, citation, etc.
            split (`NamedSplit`, optional): Name of the dataset split.

        Returns:
            [`Dataset`]
        """
    @staticmethod
    def from_csv(path_or_paths: PathLike | List[PathLike], split: NamedSplit | None = None, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, num_proc: int | None = None, **kwargs):
        '''Create Dataset from CSV file(s).

        Args:
            path_or_paths (`path-like` or list of `path-like`):
                Path(s) of the CSV file(s).
            split ([`NamedSplit`], *optional*):
                Split name to be assigned to the dataset.
            features ([`Features`], *optional*):
                Dataset features.
            cache_dir (`str`, *optional*, defaults to `"~/.cache/huggingface/datasets"`):
                Directory to cache data.
            keep_in_memory (`bool`, defaults to `False`):
                Whether to copy the data in-memory.
            num_proc (`int`, *optional*, defaults to `None`):
                Number of processes when downloading and generating the dataset locally.
                This is helpful if the dataset is made of multiple files. Multiprocessing is disabled by default.

                <Added version="2.8.0"/>
            **kwargs (additional keyword arguments):
                Keyword arguments to be passed to [`pandas.read_csv`].

        Returns:
            [`Dataset`]

        Example:

        ```py
        >>> ds = Dataset.from_csv(\'path/to/dataset.csv\')
        ```
        '''
    @staticmethod
    def from_generator(generator: Callable, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, gen_kwargs: dict | None = None, num_proc: int | None = None, **kwargs):
        '''Create a Dataset from a generator.

        Args:
            generator (:`Callable`):
                A generator function that `yields` examples.
            features ([`Features`], *optional*):
                Dataset features.
            cache_dir (`str`, *optional*, defaults to `"~/.cache/huggingface/datasets"`):
                Directory to cache data.
            keep_in_memory (`bool`, defaults to `False`):
                Whether to copy the data in-memory.
            gen_kwargs(`dict`, *optional*):
                Keyword arguments to be passed to the `generator` callable.
                You can define a sharded dataset by passing the list of shards in `gen_kwargs`.
            num_proc (`int`, *optional*, defaults to `None`):
                Number of processes when downloading and generating the dataset locally.
                This is helpful if the dataset is made of multiple files. Multiprocessing is disabled by default.

                <Added version="2.7.0"/>
            **kwargs (additional keyword arguments):
                Keyword arguments to be passed to :[`GeneratorConfig`].

        Returns:
            [`Dataset`]

        Example:

        ```py
        >>> def gen():
        ...     yield {"text": "Good", "label": 0}
        ...     yield {"text": "Bad", "label": 1}
        ...
        >>> ds = Dataset.from_generator(gen)
        ```

        ```py
        >>> def gen(shards):
        ...     for shard in shards:
        ...         with open(shard) as f:
        ...             for line in f:
        ...                 yield {"line": line}
        ...
        >>> shards = [f"data{i}.txt" for i in range(32)]
        >>> ds = Dataset.from_generator(gen, gen_kwargs={"shards": shards})
        ```
        '''
    @staticmethod
    def from_json(path_or_paths: PathLike | List[PathLike], split: NamedSplit | None = None, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, field: str | None = None, num_proc: int | None = None, **kwargs):
        '''Create Dataset from JSON or JSON Lines file(s).

        Args:
            path_or_paths (`path-like` or list of `path-like`):
                Path(s) of the JSON or JSON Lines file(s).
            split ([`NamedSplit`], *optional*):
                Split name to be assigned to the dataset.
            features ([`Features`], *optional*):
                 Dataset features.
            cache_dir (`str`, *optional*, defaults to `"~/.cache/huggingface/datasets"`):
                Directory to cache data.
            keep_in_memory (`bool`, defaults to `False`):
                Whether to copy the data in-memory.
            field (`str`, *optional*):
                Field name of the JSON file where the dataset is contained in.
            num_proc (`int`, *optional* defaults to `None`):
                Number of processes when downloading and generating the dataset locally.
                This is helpful if the dataset is made of multiple files. Multiprocessing is disabled by default.

                <Added version="2.8.0"/>
            **kwargs (additional keyword arguments):
                Keyword arguments to be passed to [`JsonConfig`].

        Returns:
            [`Dataset`]

        Example:

        ```py
        >>> ds = Dataset.from_json(\'path/to/dataset.json\')
        ```
        '''
    @staticmethod
    def from_parquet(path_or_paths: PathLike | List[PathLike], split: NamedSplit | None = None, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, columns: List[str] | None = None, num_proc: int | None = None, **kwargs):
        '''Create Dataset from Parquet file(s).

        Args:
            path_or_paths (`path-like` or list of `path-like`):
                Path(s) of the Parquet file(s).
            split (`NamedSplit`, *optional*):
                Split name to be assigned to the dataset.
            features (`Features`, *optional*):
                Dataset features.
            cache_dir (`str`, *optional*, defaults to `"~/.cache/huggingface/datasets"`):
                Directory to cache data.
            keep_in_memory (`bool`, defaults to `False`):
                Whether to copy the data in-memory.
            columns (`List[str]`, *optional*):
                If not `None`, only these columns will be read from the file.
                A column name may be a prefix of a nested field, e.g. \'a\' will select
                \'a.b\', \'a.c\', and \'a.d.e\'.
            num_proc (`int`, *optional*, defaults to `None`):
                Number of processes when downloading and generating the dataset locally.
                This is helpful if the dataset is made of multiple files. Multiprocessing is disabled by default.

                <Added version="2.8.0"/>
            **kwargs (additional keyword arguments):
                Keyword arguments to be passed to [`ParquetConfig`].

        Returns:
            [`Dataset`]

        Example:

        ```py
        >>> ds = Dataset.from_parquet(\'path/to/dataset.parquet\')
        ```
        '''
    @staticmethod
    def from_text(path_or_paths: PathLike | List[PathLike], split: NamedSplit | None = None, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, num_proc: int | None = None, **kwargs):
        '''Create Dataset from text file(s).

        Args:
            path_or_paths (`path-like` or list of `path-like`):
                Path(s) of the text file(s).
            split (`NamedSplit`, *optional*):
                Split name to be assigned to the dataset.
            features (`Features`, *optional*):
                Dataset features.
            cache_dir (`str`, *optional*, defaults to `"~/.cache/huggingface/datasets"`):
                Directory to cache data.
            keep_in_memory (`bool`, defaults to `False`):
                Whether to copy the data in-memory.
            num_proc (`int`, *optional*, defaults to `None`):
                Number of processes when downloading and generating the dataset locally.
                This is helpful if the dataset is made of multiple files. Multiprocessing is disabled by default.

                <Added version="2.8.0"/>
            **kwargs (additional keyword arguments):
                Keyword arguments to be passed to [`TextConfig`].

        Returns:
            [`Dataset`]

        Example:

        ```py
        >>> ds = Dataset.from_text(\'path/to/dataset.txt\')
        ```
        '''
    @staticmethod
    def from_spark(df: pyspark.sql.DataFrame, split: NamedSplit | None = None, features: Features | None = None, keep_in_memory: bool = False, cache_dir: str = None, working_dir: str = None, load_from_cache_file: bool = True, **kwargs):
        '''Create a Dataset from Spark DataFrame. Dataset downloading is distributed over Spark workers.

        Args:
            df (`pyspark.sql.DataFrame`):
                The DataFrame containing the desired data.
            split (`NamedSplit`, *optional*):
                Split name to be assigned to the dataset.
            features (`Features`, *optional*):
                Dataset features.
            cache_dir (`str`, *optional*, defaults to `"~/.cache/huggingface/datasets"`):
                Directory to cache data. When using a multi-node Spark cluster, the cache_dir must be accessible to both
                workers and the driver.
            keep_in_memory (`bool`):
                Whether to copy the data in-memory.
            working_dir (`str`, *optional*)
                Intermediate directory for each Spark worker to write data to before moving it to `cache_dir`. Setting
                a non-NFS intermediate directory may improve performance.
            load_from_cache_file (`bool`):
                Whether to load the dataset from the cache if possible.

        Returns:
            [`Dataset`]

        Example:

        ```py
        >>> df = spark.createDataFrame(
        >>>     data=[[1, "Elia"], [2, "Teo"], [3, "Fang"]],
        >>>     columns=["id", "name"],
        >>> )
        >>> ds = Dataset.from_spark(df)
        ```
        '''
    @staticmethod
    def from_sql(sql: str | sqlalchemy.sql.Selectable, con: str | sqlalchemy.engine.Connection | sqlalchemy.engine.Engine | sqlite3.Connection, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, **kwargs):
        '''Create Dataset from SQL query or database table.

        Args:
            sql (`str` or `sqlalchemy.sql.Selectable`):
                SQL query to be executed or a table name.
            con (`str` or `sqlite3.Connection` or `sqlalchemy.engine.Connection` or `sqlalchemy.engine.Connection`):
                A [URI string](https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls) used to instantiate a database connection or a SQLite3/SQLAlchemy connection object.
            features ([`Features`], *optional*):
                Dataset features.
            cache_dir (`str`, *optional*, defaults to `"~/.cache/huggingface/datasets"`):
                Directory to cache data.
            keep_in_memory (`bool`, defaults to `False`):
                Whether to copy the data in-memory.
            **kwargs (additional keyword arguments):
                Keyword arguments to be passed to [`SqlConfig`].

        Returns:
            [`Dataset`]

        Example:

        ```py
        >>> # Fetch a database table
        >>> ds = Dataset.from_sql("test_data", "postgres:///db_name")
        >>> # Execute a SQL query on the table
        >>> ds = Dataset.from_sql("SELECT sentence FROM test_data", "postgres:///db_name")
        >>> # Use a Selectable object to specify the query
        >>> from sqlalchemy import select, text
        >>> stmt = select([text("sentence")]).select_from(text("test_data"))
        >>> ds = Dataset.from_sql(stmt, "postgres:///db_name")
        ```

        <Tip>

        The returned dataset can only be cached if `con` is specified as URI string.

        </Tip>
        '''
    def __del__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def save_to_disk(self, dataset_path: PathLike, fs: str = 'deprecated', max_shard_size: str | int | None = None, num_shards: int | None = None, num_proc: int | None = None, storage_options: dict | None = None):
        '''
        Saves a dataset to a dataset directory, or in a filesystem using any implementation of `fsspec.spec.AbstractFileSystem`.

        For [`Image`] and [`Audio`] data:

        All the Image() and Audio() data are stored in the arrow files.
        If you want to store paths or urls, please use the Value("string") type.

        Args:
            dataset_path (`str`):
                Path (e.g. `dataset/train`) or remote URI (e.g. `s3://my-bucket/dataset/train`)
                of the dataset directory where the dataset will be saved to.
            fs (`fsspec.spec.AbstractFileSystem`, *optional*):
                Instance of the remote filesystem where the dataset will be saved to.

                <Deprecated version="2.8.0">

                `fs` was deprecated in version 2.8.0 and will be removed in 3.0.0.
                Please use `storage_options` instead, e.g. `storage_options=fs.storage_options`

                </Deprecated>

            max_shard_size (`int` or `str`, *optional*, defaults to `"500MB"`):
                The maximum size of the dataset shards to be uploaded to the hub. If expressed as a string, needs to be digits followed by a unit
                (like `"50MB"`).
            num_shards (`int`, *optional*):
                Number of shards to write. By default the number of shards depends on `max_shard_size` and `num_proc`.

                <Added version="2.8.0"/>
            num_proc (`int`, *optional*):
                Number of processes when downloading and generating the dataset locally.
                Multiprocessing is disabled by default.

                <Added version="2.8.0"/>
            storage_options (`dict`, *optional*):
                Key/value pairs to be passed on to the file-system backend, if any.

                <Added version="2.8.0"/>

        Example:

        ```py
        >>> ds.save_to_disk("path/to/dataset/directory")
        >>> ds.save_to_disk("path/to/dataset/directory", max_shard_size="1GB")
        >>> ds.save_to_disk("path/to/dataset/directory", num_shards=1024)
        ```
        '''
    @staticmethod
    def load_from_disk(dataset_path: str, fs: str = 'deprecated', keep_in_memory: bool | None = None, storage_options: dict | None = None) -> Dataset:
        '''
        Loads a dataset that was previously saved using [`save_to_disk`] from a dataset directory, or from a
        filesystem using any implementation of `fsspec.spec.AbstractFileSystem`.

        Args:
            dataset_path (`str`):
                Path (e.g. `"dataset/train"`) or remote URI (e.g. `"s3//my-bucket/dataset/train"`)
                of the dataset directory where the dataset will be loaded from.
            fs (`fsspec.spec.AbstractFileSystem`, *optional*):
                Instance of the remote filesystem where the dataset will be saved to.

                <Deprecated version="2.8.0">

                `fs` was deprecated in version 2.8.0 and will be removed in 3.0.0.
                Please use `storage_options` instead, e.g. `storage_options=fs.storage_options`

                </Deprecated>

            keep_in_memory (`bool`, defaults to `None`):
                Whether to copy the dataset in-memory. If `None`, the
                dataset will not be copied in-memory unless explicitly enabled by setting
                `datasets.config.IN_MEMORY_MAX_SIZE` to nonzero. See more details in the
                [improve performance](../cache#improve-performance) section.
            storage_options (`dict`, *optional*):
                Key/value pairs to be passed on to the file-system backend, if any.

                <Added version="2.8.0"/>

        Returns:
            [`Dataset`] or [`DatasetDict`]:
            - If `dataset_path` is a path of a dataset directory, the dataset requested.
            - If `dataset_path` is a path of a dataset dict directory, a `datasets.DatasetDict` with each split.

        Example:

        ```py
        >>> ds = load_from_disk("path/to/dataset/directory")
        ```
        '''
    @property
    def data(self) -> Table:
        '''The Apache Arrow table backing the dataset.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.data
        MemoryMappedTable
        text: string
        label: int64
        ----
        text: [["compassionately explores the seemingly irreconcilable situation between conservative christian parents and their estranged gay and lesbian children .","the soundtrack alone is worth the price of admission .","rodriguez does a splendid job of racial profiling hollywood style--casting excellent latin actors of all ages--a trend long overdue .","beneath the film\'s obvious determination to shock at any cost lies considerable skill and determination , backed by sheer nerve .","bielinsky is a filmmaker of impressive talent .","so beautifully acted and directed , it\'s clear that washington most certainly has a new career ahead of him if he so chooses .","a visual spectacle full of stunning images and effects .","a gentle and engrossing character study .","it\'s enough to watch huppert scheming , with her small , intelligent eyes as steady as any noir villain , and to enjoy the perfectly pitched web of tension that chabrol spins .","an engrossing portrait of uncompromising artists trying to create something original against the backdrop of a corporate music industry that only seems to care about the bottom line .",...,"ultimately , jane learns her place as a girl , softens up and loses some of the intensity that made her an interesting character to begin with .","ah-nuld\'s action hero days might be over .","it\'s clear why deuces wild , which was shot two years ago , has been gathering dust on mgm\'s shelf .","feels like nothing quite so much as a middle-aged moviemaker\'s attempt to surround himself with beautiful , half-naked women .","when the precise nature of matthew\'s predicament finally comes into sharp focus , the revelation fails to justify the build-up .","this picture is murder by numbers , and as easy to be bored by as your abc\'s , despite a few whopping shootouts .","hilarious musical comedy though stymied by accents thick as mud .","if you are into splatter movies , then you will probably have a reasonably good time with the salton sea .","a dull , simple-minded and stereotypical tale of drugs , death and mind-numbing indifference on the inner-city streets .","the feature-length stretch . . . strains the show\'s concept ."]]
        label: [[1,1,1,1,1,1,1,1,1,1,...,0,0,0,0,0,0,0,0,0,0]]
        ```
        '''
    @property
    def cache_files(self) -> List[dict]:
        '''The cache files containing the Apache Arrow table backing the dataset.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.cache_files
        [{\'filename\': \'/root/.cache/huggingface/datasets/rotten_tomatoes_movie_review/default/1.0.0/40d411e45a6ce3484deed7cc15b82a53dad9a72aafd9f86f8f227134bec5ca46/rotten_tomatoes_movie_review-validation.arrow\'}]
        ```
        '''
    @property
    def num_columns(self) -> int:
        '''Number of columns in the dataset.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.num_columns
        2
        ```
        '''
    @property
    def num_rows(self) -> int:
        '''Number of rows in the dataset (same as [`Dataset.__len__`]).

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.num_rows
        1066
        ```
        '''
    @property
    def column_names(self) -> List[str]:
        '''Names of the columns in the dataset.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.column_names
        [\'text\', \'label\']
        ```
        '''
    @property
    def shape(self) -> Tuple[int, int]:
        '''Shape of the dataset (number of columns, number of rows).

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.shape
        (1066, 2)
        ```
        '''
    def unique(self, column: str) -> List:
        '''Return a list of the unique elements in a column.

        This is implemented in the low-level backend and as such, very fast.

        Args:
            column (`str`):
                Column name (list all the column names with [`~datasets.Dataset.column_names`]).

        Returns:
            `list`: List of unique elements in the given column.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.unique(\'label\')
        [1, 0]
        ```
        '''
    def class_encode_column(self, column: str, include_nulls: bool = False) -> Dataset:
        '''Casts the given column as [`~datasets.features.ClassLabel`] and updates the table.

        Args:
            column (`str`):
                The name of the column to cast (list all the column names with [`~datasets.Dataset.column_names`])
            include_nulls (`bool`, defaults to `False`):
                Whether to include null values in the class labels. If `True`, the null values will be encoded as the `"None"` class label.

                <Added version="1.14.2"/>

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("boolq", split="validation")
        >>> ds.features
        {\'answer\': Value(dtype=\'bool\', id=None),
         \'passage\': Value(dtype=\'string\', id=None),
         \'question\': Value(dtype=\'string\', id=None)}
        >>> ds = ds.class_encode_column(\'answer\')
        >>> ds.features
        {\'answer\': ClassLabel(num_classes=2, names=[\'False\', \'True\'], id=None),
         \'passage\': Value(dtype=\'string\', id=None),
         \'question\': Value(dtype=\'string\', id=None)}
        ```
        '''
    def flatten(self, new_fingerprint: str | None = None, max_depth: int = 16) -> Dataset:
        '''Flatten the table.
        Each column with a struct type is flattened into one column per struct field.
        Other columns are left unchanged.

        Args:
            new_fingerprint (`str`, *optional*):
                The new fingerprint of the dataset after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments.

        Returns:
            [`Dataset`]: A copy of the dataset with flattened columns.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("squad", split="train")
        >>> ds.features
        {\'answers\': Sequence(feature={\'text\': Value(dtype=\'string\', id=None), \'answer_start\': Value(dtype=\'int32\', id=None)}, length=-1, id=None),
         \'context\': Value(dtype=\'string\', id=None),
         \'id\': Value(dtype=\'string\', id=None),
         \'question\': Value(dtype=\'string\', id=None),
         \'title\': Value(dtype=\'string\', id=None)}
        >>> ds.flatten()
        Dataset({
            features: [\'id\', \'title\', \'context\', \'question\', \'answers.text\', \'answers.answer_start\'],
            num_rows: 87599
        })
        ```
        '''
    def cast(self, features: Features, batch_size: int | None = 1000, keep_in_memory: bool = False, load_from_cache_file: bool | None = None, cache_file_name: str | None = None, writer_batch_size: int | None = 1000, num_proc: int | None = None) -> Dataset:
        '''
        Cast the dataset to a new set of features.

        Args:
            features ([`Features`]):
                New features to cast the dataset to.
                The name of the fields in the features must match the current column names.
                The type of the data must also be convertible from one type to the other.
                For non-trivial conversion, e.g. `str` <-> `ClassLabel` you should use [`~datasets.Dataset.map`] to update the Dataset.
            batch_size (`int`, defaults to `1000`):
                Number of examples per batch provided to cast.
                If `batch_size <= 0` or `batch_size == None` then provide the full dataset as a single batch to cast.
            keep_in_memory (`bool`, defaults to `False`):
                Whether to copy the data in-memory.
            load_from_cache_file (`bool`, defaults to `True` if caching is enabled):
                If a cache file storing the current computation from `function`
                can be identified, use it instead of recomputing.
            cache_file_name (`str`, *optional*, defaults to `None`):
                Provide the name of a path for the cache file. It is used to store the
                results of the computation instead of the automatically generated cache file name.
            writer_batch_size (`int`, defaults to `1000`):
                Number of rows per write operation for the cache file writer.
                This value is a good trade-off between memory usage during the processing, and processing speed.
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running [`~datasets.Dataset.map`].
            num_proc (`int`, *optional*, defaults to `None`):
                Number of processes for multiprocessing. By default it doesn\'t
                use multiprocessing.

        Returns:
            [`Dataset`]: A copy of the dataset with casted features.

        Example:

        ```py
        >>> from datasets import load_dataset, ClassLabel, Value
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.features
        {\'label\': ClassLabel(num_classes=2, names=[\'neg\', \'pos\'], id=None),
         \'text\': Value(dtype=\'string\', id=None)}
        >>> new_features = ds.features.copy()
        >>> new_features[\'label\'] = ClassLabel(names=[\'bad\', \'good\'])
        >>> new_features[\'text\'] = Value(\'large_string\')
        >>> ds = ds.cast(new_features)
        >>> ds.features
        {\'label\': ClassLabel(num_classes=2, names=[\'bad\', \'good\'], id=None),
         \'text\': Value(dtype=\'large_string\', id=None)}
        ```
        '''
    def cast_column(self, column: str, feature: FeatureType, new_fingerprint: str | None = None) -> Dataset:
        '''Cast column to feature for decoding.

        Args:
            column (`str`):
                Column name.
            feature (`FeatureType`):
                Target feature.
            new_fingerprint (`str`, *optional*):
                The new fingerprint of the dataset after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments.

        Returns:
            [`Dataset`]

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.features
        {\'label\': ClassLabel(num_classes=2, names=[\'neg\', \'pos\'], id=None),
         \'text\': Value(dtype=\'string\', id=None)}
        >>> ds = ds.cast_column(\'label\', ClassLabel(names=[\'bad\', \'good\']))
        >>> ds.features
        {\'label\': ClassLabel(num_classes=2, names=[\'bad\', \'good\'], id=None),
         \'text\': Value(dtype=\'string\', id=None)}
        ```
        '''
    def remove_columns(self, column_names: str | List[str], new_fingerprint: str | None = None) -> Dataset:
        '''
        Remove one or several column(s) in the dataset and the features associated to them.

        You can also remove a column using [`~datasets.Dataset.map`] with `remove_columns` but the present method
        is in-place (doesn\'t copy the data to a new dataset) and is thus faster.

        Args:
            column_names (`Union[str, List[str]]`):
                Name of the column(s) to remove.
            new_fingerprint (`str`, *optional*):
                The new fingerprint of the dataset after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments.

        Returns:
            [`Dataset`]: A copy of the dataset object without the columns to remove.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.remove_columns(\'label\')
        Dataset({
            features: [\'text\'],
            num_rows: 1066
        })
        >>> ds.remove_columns(column_names=ds.column_names) # Removing all the columns returns an empty dataset with the `num_rows` property set to 0
        Dataset({
            features: [],
            num_rows: 0
        })
        ```
        '''
    def rename_column(self, original_column_name: str, new_column_name: str, new_fingerprint: str | None = None) -> Dataset:
        '''
        Rename a column in the dataset, and move the features associated to the original column under the new column
        name.

        Args:
            original_column_name (`str`):
                Name of the column to rename.
            new_column_name (`str`):
                New name for the column.
            new_fingerprint (`str`, *optional*):
                The new fingerprint of the dataset after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments.

        Returns:
            [`Dataset`]: A copy of the dataset with a renamed column.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.rename_column(\'label\', \'label_new\')
        Dataset({
            features: [\'text\', \'label_new\'],
            num_rows: 1066
        })
        ```
        '''
    def rename_columns(self, column_mapping: Dict[str, str], new_fingerprint: str | None = None) -> Dataset:
        '''
        Rename several columns in the dataset, and move the features associated to the original columns under
        the new column names.

        Args:
            column_mapping (`Dict[str, str]`):
                A mapping of columns to rename to their new names
            new_fingerprint (`str`, *optional*):
                The new fingerprint of the dataset after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments.

        Returns:
            [`Dataset`]: A copy of the dataset with renamed columns

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.rename_columns({\'text\': \'text_new\', \'label\': \'label_new\'})
        Dataset({
            features: [\'text_new\', \'label_new\'],
            num_rows: 1066
        })
        ```
        '''
    def select_columns(self, column_names: str | List[str], new_fingerprint: str | None = None) -> Dataset:
        '''Select one or several column(s) in the dataset and the features
        associated to them.

        Args:
            column_names (`Union[str, List[str]]`):
                Name of the column(s) to keep.
            new_fingerprint (`str`, *optional*):
                The new fingerprint of the dataset after transform. If `None`,
                the new fingerprint is computed using a hash of the previous
                fingerprint, and the transform arguments.

        Returns:
            [`Dataset`]: A copy of the dataset object which only consists of
            selected columns.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.select_columns([\'text\'])
        Dataset({
            features: [\'text\'],
            num_rows: 1066
        })
        ```
        '''
    def __len__(self) -> int:
        '''Number of rows in the dataset.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.__len__
        <bound method Dataset.__len__ of Dataset({
            features: [\'text\', \'label\'],
            num_rows: 1066
        })>
        ```
        '''
    def __iter__(self):
        """Iterate through the examples.

        If a formatting is set with :meth:`Dataset.set_format` rows will be returned with the
        selected format.
        """
    def iter(self, batch_size: int, drop_last_batch: bool = False):
        """Iterate through the batches of size `batch_size`.

        If a formatting is set with [`~datasets.Dataset.set_format`] rows will be returned with the
        selected format.

        Args:
            batch_size (:obj:`int`): size of each batch to yield.
            drop_last_batch (:obj:`bool`, default `False`): Whether a last batch smaller than the batch_size should be
                dropped
        """
    @property
    def format(self): ...
    def formatted_as(self, type: str | None = None, columns: List | None = None, output_all_columns: bool = False, **format_kwargs):
        """To be used in a `with` statement. Set `__getitem__` return format (type and columns).

        Args:
            type (`str`, *optional*):
                Output type selected in `[None, 'numpy', 'torch', 'tensorflow', 'pandas', 'arrow', 'jax']`.
                `None` means `__getitem__`` returns python objects (default).
            columns (`List[str]`, *optional*):
                Columns to format in the output.
                `None` means `__getitem__` returns all columns (default).
            output_all_columns (`bool`, defaults to `False`):
                Keep un-formatted columns as well in the output (as python objects).
            **format_kwargs (additional keyword arguments):
                Keywords arguments passed to the convert function like `np.array`, `torch.tensor` or `tensorflow.ragged.constant`.
        """
    def set_format(self, type: str | None = None, columns: List | None = None, output_all_columns: bool = False, **format_kwargs):
        '''Set `__getitem__` return format (type and columns). The data formatting is applied on-the-fly.
        The format `type` (for example "numpy") is used to format batches when using `__getitem__`.
        It\'s also possible to use custom transforms for formatting using [`~datasets.Dataset.set_transform`].

        Args:
            type (`str`, *optional*):
                Either output type selected in `[None, \'numpy\', \'torch\', \'tensorflow\', \'pandas\', \'arrow\', \'jax\']`.
                `None` means `__getitem__` returns python objects (default).
            columns (`List[str]`, *optional*):
                Columns to format in the output.
                `None` means `__getitem__` returns all columns (default).
            output_all_columns (`bool`, defaults to `False`):
                Keep un-formatted columns as well in the output (as python objects).
            **format_kwargs (additional keyword arguments):
                Keywords arguments passed to the convert function like `np.array`, `torch.tensor` or `tensorflow.ragged.constant`.

        It is possible to call [`~datasets.Dataset.map`] after calling `set_format`. Since `map` may add new columns, then the list of formatted columns
        gets updated. In this case, if you apply `map` on a dataset to add a new column, then this column will be formatted as:

            ```
            new formatted columns = (all columns - previously unformatted columns)
            ```

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> from transformers import AutoTokenizer
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
        >>> ds = ds.map(lambda x: tokenizer(x[\'text\'], truncation=True, padding=True), batched=True)
        >>> ds.set_format(type=\'numpy\', columns=[\'text\', \'label\'])
        >>> ds.format
        {\'type\': \'numpy\',
        \'format_kwargs\': {},
        \'columns\': [\'text\', \'label\'],
        \'output_all_columns\': False}
        ```
        '''
    def reset_format(self) -> None:
        '''Reset `__getitem__` return format to python objects and all columns.

        Same as `self.set_format()`

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> from transformers import AutoTokenizer
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
        >>> ds = ds.map(lambda x: tokenizer(x[\'text\'], truncation=True, padding=True), batched=True)
        >>> ds.set_format(type=\'numpy\', columns=[\'input_ids\', \'token_type_ids\', \'attention_mask\', \'label\'])
        >>> ds.format
        {\'columns\': [\'input_ids\', \'token_type_ids\', \'attention_mask\', \'label\'],
         \'format_kwargs\': {},
         \'output_all_columns\': False,
         \'type\': \'numpy\'}
        >>> ds.reset_format()
        >>> ds.format
        {\'columns\': [\'text\', \'label\', \'input_ids\', \'token_type_ids\', \'attention_mask\'],
         \'format_kwargs\': {},
         \'output_all_columns\': False,
         \'type\': None}
        ```
        '''
    def set_transform(self, transform: Callable | None, columns: List | None = None, output_all_columns: bool = False):
        '''Set `__getitem__` return format using this transform. The transform is applied on-the-fly on batches when `__getitem__` is called.
        As [`~datasets.Dataset.set_format`], this can be reset using [`~datasets.Dataset.reset_format`].

        Args:
            transform (`Callable`, *optional*):
                User-defined formatting transform, replaces the format defined by [`~datasets.Dataset.set_format`].
                A formatting function is a callable that takes a batch (as a `dict`) as input and returns a batch.
                This function is applied right before returning the objects in `__getitem__`.
            columns (`List[str]`, *optional*):
                Columns to format in the output.
                If specified, then the input batch of the transform only contains those columns.
            output_all_columns (`bool`, defaults to `False`):
                Keep un-formatted columns as well in the output (as python objects).
                If set to True, then the other un-formatted columns are kept with the output of the transform.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> from transformers import AutoTokenizer
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> tokenizer = AutoTokenizer.from_pretrained(\'bert-base-uncased\')
        >>> def encode(batch):
        ...     return tokenizer(batch[\'text\'], padding=True, truncation=True, return_tensors=\'pt\')
        >>> ds.set_transform(encode)
        >>> ds[0]
        {\'attention_mask\': tensor([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1]),
         \'input_ids\': tensor([  101, 29353,  2135, 15102,  1996,  9428, 20868,  2890,  8663,  6895,
                 20470,  2571,  3663,  2090,  4603,  3017,  3008,  1998,  2037, 24211,
                 5637,  1998, 11690,  2336,  1012,   102]),
         \'token_type_ids\': tensor([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0])}
        ```
        '''
    def with_format(self, type: str | None = None, columns: List | None = None, output_all_columns: bool = False, **format_kwargs):
        '''Set `__getitem__` return format (type and columns). The data formatting is applied on-the-fly.
        The format `type` (for example "numpy") is used to format batches when using `__getitem__`.

        It\'s also possible to use custom transforms for formatting using [`~datasets.Dataset.with_transform`].

        Contrary to [`~datasets.Dataset.set_format`], `with_format` returns a new [`Dataset`] object.

        Args:
            type (`str`, *optional*):
                Either output type selected in `[None, \'numpy\', \'torch\', \'tensorflow\', \'pandas\', \'arrow\', \'jax\']`.
                `None` means `__getitem__` returns python objects (default).
            columns (`List[str]`, *optional*):
                Columns to format in the output.
                `None` means `__getitem__` returns all columns (default).
            output_all_columns (`bool`, defaults to `False`):
                Keep un-formatted columns as well in the output (as python objects).
            **format_kwargs (additional keyword arguments):
                Keywords arguments passed to the convert function like `np.array`, `torch.tensor` or `tensorflow.ragged.constant`.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> from transformers import AutoTokenizer
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
        >>> ds = ds.map(lambda x: tokenizer(x[\'text\'], truncation=True, padding=True), batched=True)
        >>> ds.format
        {\'columns\': [\'text\', \'label\', \'input_ids\', \'token_type_ids\', \'attention_mask\'],
         \'format_kwargs\': {},
         \'output_all_columns\': False,
         \'type\': None}
        >>> ds = ds.with_format(type=\'tensorflow\', columns=[\'input_ids\', \'token_type_ids\', \'attention_mask\', \'label\'])
        >>> ds.format
        {\'columns\': [\'input_ids\', \'token_type_ids\', \'attention_mask\', \'label\'],
         \'format_kwargs\': {},
         \'output_all_columns\': False,
         \'type\': \'tensorflow\'}
        ```
        '''
    def with_transform(self, transform: Callable | None, columns: List | None = None, output_all_columns: bool = False):
        '''Set `__getitem__` return format using this transform. The transform is applied on-the-fly on batches when `__getitem__` is called.

        As [`~datasets.Dataset.set_format`], this can be reset using [`~datasets.Dataset.reset_format`].

        Contrary to [`~datasets.Dataset.set_transform`], `with_transform` returns a new [`Dataset`] object.

        Args:
            transform (`Callable`, `optional`):
                User-defined formatting transform, replaces the format defined by [`~datasets.Dataset.set_format`].
                A formatting function is a callable that takes a batch (as a `dict`) as input and returns a batch.
                This function is applied right before returning the objects in `__getitem__`.
            columns (`List[str]`, `optional`):
                Columns to format in the output.
                If specified, then the input batch of the transform only contains those columns.
            output_all_columns (`bool`, defaults to `False`):
                Keep un-formatted columns as well in the output (as python objects).
                If set to `True`, then the other un-formatted columns are kept with the output of the transform.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> from transformers import AutoTokenizer
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
        >>> def encode(example):
        ...     return tokenizer(example["text"], padding=True, truncation=True, return_tensors=\'pt\')
        >>> ds = ds.with_transform(encode)
        >>> ds[0]
        {\'attention_mask\': tensor([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1]),
         \'input_ids\': tensor([  101, 18027, 16310, 16001,  1103,  9321,   178, 11604,  7235,  6617,
                 1742,  2165,  2820,  1206,  6588, 22572, 12937,  1811,  2153,  1105,
                 1147, 12890, 19587,  6463,  1105, 15026,  1482,   119,   102]),
         \'token_type_ids\': tensor([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0])}
        ```
        '''
    def prepare_for_task(self, task: str | TaskTemplate, id: int = 0) -> Dataset:
        '''
        Prepare a dataset for the given task by casting the dataset\'s [`Features`] to standardized column names and types as detailed in [`datasets.tasks`](./task_templates).

        Casts [`datasets.DatasetInfo.features`] according to a task-specific schema. Intended for single-use only, so all task templates are removed from [`datasets.DatasetInfo.task_templates`] after casting.

        Args:
            task (`Union[str, TaskTemplate]`):
                The task to prepare the dataset for during training and evaluation. If `str`, supported tasks include:

                - `"text-classification"`
                - `"question-answering"`

                If [`TaskTemplate`], must be one of the task templates in [`datasets.tasks`](./task_templates).
            id (`int`, defaults to `0`):
                The id required to unambiguously identify the task template when multiple task templates of the same type are supported.
        '''
    @overload
    def __getitem__(self, key: int | slice | Iterable[int]) -> Dict: ...
    @overload
    def __getitem__(self, key: str) -> List: ...
    def __getitems__(self, keys: List) -> List:
        """Can be used to get a batch using a list of integers indices."""
    def cleanup_cache_files(self) -> int:
        '''Clean up all cache files in the dataset cache directory, excepted the currently used cache file if there is
        one.

        Be careful when running this command that no other process is currently using other cache files.

        Returns:
            `int`: Number of removed files.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.cleanup_cache_files()
        10
        ```
        '''
    def map(self, function: Callable | None = None, with_indices: bool = False, with_rank: bool = False, input_columns: str | List[str] | None = None, batched: bool = False, batch_size: int | None = 1000, drop_last_batch: bool = False, remove_columns: str | List[str] | None = None, keep_in_memory: bool = False, load_from_cache_file: bool | None = None, cache_file_name: str | None = None, writer_batch_size: int | None = 1000, features: Features | None = None, disable_nullable: bool = False, fn_kwargs: dict | None = None, num_proc: int | None = None, suffix_template: str = '_{rank:05d}_of_{num_proc:05d}', new_fingerprint: str | None = None, desc: str | None = None) -> Dataset:
        '''
        Apply a function to all the examples in the table (individually or in batches) and update the table.
        If your function returns a column that already exists, then it overwrites it.

        You can specify whether the function should be batched or not with the `batched` parameter:

        - If batched is `False`, then the function takes 1 example in and should return 1 example.
          An example is a dictionary, e.g. `{"text": "Hello there !"}`.
        - If batched is `True` and `batch_size` is 1, then the function takes a batch of 1 example as input and can return a batch with 1 or more examples.
          A batch is a dictionary, e.g. a batch of 1 example is `{"text": ["Hello there !"]}`.
        - If batched is `True` and `batch_size` is `n > 1`, then the function takes a batch of `n` examples as input and can return a batch with `n` examples, or with an arbitrary number of examples.
          Note that the last batch may have less than `n` examples.
          A batch is a dictionary, e.g. a batch of `n` examples is `{"text": ["Hello there !"] * n}`.

        Args:
            function (`Callable`): Function with one of the following signatures:

                - `function(example: Dict[str, Any]) -> Dict[str, Any]` if `batched=False` and `with_indices=False` and `with_rank=False`
                - `function(example: Dict[str, Any], *extra_args) -> Dict[str, Any]` if `batched=False` and `with_indices=True` and/or `with_rank=True` (one extra arg for each)
                - `function(batch: Dict[str, List]) -> Dict[str, List]` if `batched=True` and `with_indices=False` and `with_rank=False`
                - `function(batch: Dict[str, List], *extra_args) -> Dict[str, List]` if `batched=True` and `with_indices=True` and/or `with_rank=True` (one extra arg for each)

                For advanced usage, the function can also return a `pyarrow.Table`.
                Moreover if your function returns nothing (`None`), then `map` will run your function and return the dataset unchanged.
                If no function is provided, default to identity function: `lambda x: x`.
            with_indices (`bool`, defaults to `False`):
                Provide example indices to `function`. Note that in this case the
                signature of `function` should be `def function(example, idx[, rank]): ...`.
            with_rank (`bool`, defaults to `False`):
                Provide process rank to `function`. Note that in this case the
                signature of `function` should be `def function(example[, idx], rank): ...`.
            input_columns (`Optional[Union[str, List[str]]]`, defaults to `None`):
                The columns to be passed into `function`
                as positional arguments. If `None`, a `dict` mapping to all formatted columns is passed as one argument.
            batched (`bool`, defaults to `False`):
                Provide batch of examples to `function`.
            batch_size (`int`, *optional*, defaults to `1000`):
                Number of examples per batch provided to `function` if `batched=True`.
                If `batch_size <= 0` or `batch_size == None`, provide the full dataset as a single batch to `function`.
            drop_last_batch (`bool`, defaults to `False`):
                Whether a last batch smaller than the batch_size should be
                dropped instead of being processed by the function.
            remove_columns (`Optional[Union[str, List[str]]]`, defaults to `None`):
                Remove a selection of columns while doing the mapping.
                Columns will be removed before updating the examples with the output of `function`, i.e. if `function` is adding
                columns with names in `remove_columns`, these columns will be kept.
            keep_in_memory (`bool`, defaults to `False`):
                Keep the dataset in memory instead of writing it to a cache file.
            load_from_cache_file (`Optioanl[bool]`, defaults to `True` if caching is enabled):
                If a cache file storing the current computation from `function`
                can be identified, use it instead of recomputing.
            cache_file_name (`str`, *optional*, defaults to `None`):
                Provide the name of a path for the cache file. It is used to store the
                results of the computation instead of the automatically generated cache file name.
            writer_batch_size (`int`, defaults to `1000`):
                Number of rows per write operation for the cache file writer.
                This value is a good trade-off between memory usage during the processing, and processing speed.
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `map`.
            features (`Optional[datasets.Features]`, defaults to `None`):
                Use a specific Features to store the cache file
                instead of the automatically generated one.
            disable_nullable (`bool`, defaults to `False`):
                Disallow null values in the table.
            fn_kwargs (`Dict`, *optional*, defaults to `None`):
                Keyword arguments to be passed to `function`.
            num_proc (`int`, *optional*, defaults to `None`):
                Max number of processes when generating cache. Already cached shards are loaded sequentially.
            suffix_template (`str`):
                If `cache_file_name` is specified, then this suffix
                will be added at the end of the base name of each. Defaults to `"_{rank:05d}_of_{num_proc:05d}"`. For example, if `cache_file_name` is "processed.arrow", then for
                `rank=1` and `num_proc=4`, the resulting file would be `"processed_00001_of_00004.arrow"` for the default suffix.
            new_fingerprint (`str`, *optional*, defaults to `None`):
                The new fingerprint of the dataset after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments.
            desc (`str`, *optional*, defaults to `None`):
                Meaningful description to be displayed alongside with the progress bar while mapping examples.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> def add_prefix(example):
        ...     example["text"] = "Review: " + example["text"]
        ...     return example
        >>> ds = ds.map(add_prefix)
        >>> ds[0:3]["text"]
        [\'Review: compassionately explores the seemingly irreconcilable situation between conservative christian parents and their estranged gay and lesbian children .\',
         \'Review: the soundtrack alone is worth the price of admission .\',
         \'Review: rodriguez does a splendid job of racial profiling hollywood style--casting excellent latin actors of all ages--a trend long overdue .\']

        # process a batch of examples
        >>> ds = ds.map(lambda example: tokenizer(example["text"]), batched=True)
        # set number of processors
        >>> ds = ds.map(add_prefix, num_proc=4)
        ```
        '''
    def filter(self, function: Callable | None = None, with_indices: bool = False, input_columns: str | List[str] | None = None, batched: bool = False, batch_size: int | None = 1000, keep_in_memory: bool = False, load_from_cache_file: bool | None = None, cache_file_name: str | None = None, writer_batch_size: int | None = 1000, fn_kwargs: dict | None = None, num_proc: int | None = None, suffix_template: str = '_{rank:05d}_of_{num_proc:05d}', new_fingerprint: str | None = None, desc: str | None = None) -> Dataset:
        '''Apply a filter function to all the elements in the table in batches
        and update the table so that the dataset only includes examples according to the filter function.

        Args:
            function (`Callable`): Callable with one of the following signatures:

                - `function(example: Dict[str, Any]) -> bool` if `with_indices=False, batched=False`
                - `function(example: Dict[str, Any], indices: int) -> bool` if `with_indices=True, batched=False`
                - `function(example: Dict[str, List]) -> List[bool]` if `with_indices=False, batched=True`
                - `function(example: Dict[str, List], indices: List[int]) -> List[bool]` if `with_indices=True, batched=True`

                If no function is provided, defaults to an always `True` function: `lambda x: True`.
            with_indices (`bool`, defaults to `False`):
                Provide example indices to `function`. Note that in this case the signature of `function` should be `def function(example, idx): ...`.
            input_columns (`str` or `List[str]`, *optional*):
                The columns to be passed into `function` as
                positional arguments. If `None`, a `dict` mapping to all formatted columns is passed as one argument.
            batched (`bool`, defaults to `False`):
                Provide batch of examples to `function`.
            batch_size (`int`, *optional*, defaults to `1000`):
                Number of examples per batch provided to `function` if
                `batched = True`. If `batched = False`, one example per batch is passed to `function`.
                If `batch_size <= 0` or `batch_size == None`, provide the full dataset as a single batch to `function`.
            keep_in_memory (`bool`, defaults to `False`):
                Keep the dataset in memory instead of writing it to a cache file.
            load_from_cache_file (`Optional[bool]`, defaults to `True` if caching is enabled):
                If a cache file storing the current computation from `function`
                can be identified, use it instead of recomputing.
            cache_file_name (`str`, *optional*):
                Provide the name of a path for the cache file. It is used to store the
                results of the computation instead of the automatically generated cache file name.
            writer_batch_size (`int`, defaults to `1000`):
                Number of rows per write operation for the cache file writer.
                This value is a good trade-off between memory usage during the processing, and processing speed.
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `map`.
            fn_kwargs (`dict`, *optional*):
                Keyword arguments to be passed to `function`.
            num_proc (`int`, *optional*):
                Number of processes for multiprocessing. By default it doesn\'t
                use multiprocessing.
            suffix_template (`str`):
                If `cache_file_name` is specified, then this suffix will be added at the end of the base name of each.
                For example, if `cache_file_name` is `"processed.arrow"`, then for `rank = 1` and `num_proc = 4`,
                the resulting file would be `"processed_00001_of_00004.arrow"` for the default suffix (default
                `_{rank:05d}_of_{num_proc:05d}`).
            new_fingerprint (`str`, *optional*):
                The new fingerprint of the dataset after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments.
            desc (`str`, *optional*, defaults to `None`):
                Meaningful description to be displayed alongside with the progress bar while filtering examples.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.filter(lambda x: x["label"] == 1)
        Dataset({
            features: [\'text\', \'label\'],
            num_rows: 533
        })
        ```
        '''
    def flatten_indices(self, keep_in_memory: bool = False, cache_file_name: str | None = None, writer_batch_size: int | None = 1000, features: Features | None = None, disable_nullable: bool = False, num_proc: int | None = None, new_fingerprint: str | None = None) -> Dataset:
        """Create and cache a new Dataset by flattening the indices mapping.

        Args:
            keep_in_memory (`bool`, defaults to `False`):
                Keep the dataset in memory instead of writing it to a cache file.
            cache_file_name (`str`, *optional*, default `None`):
                Provide the name of a path for the cache file. It is used to store the
                results of the computation instead of the automatically generated cache file name.
            writer_batch_size (`int`, defaults to `1000`):
                Number of rows per write operation for the cache file writer.
                This value is a good trade-off between memory usage during the processing, and processing speed.
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `map`.
            features (`Optional[datasets.Features]`, defaults to `None`):
                Use a specific [`Features`] to store the cache file
                instead of the automatically generated one.
            disable_nullable (`bool`, defaults to `False`):
                Allow null values in the table.
            num_proc (`int`, optional, default `None`):
                Max number of processes when generating cache. Already cached shards are loaded sequentially
            new_fingerprint (`str`, *optional*, defaults to `None`):
                The new fingerprint of the dataset after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments
        """
    def select(self, indices: Iterable, keep_in_memory: bool = False, indices_cache_file_name: str | None = None, writer_batch_size: int | None = 1000, new_fingerprint: str | None = None) -> Dataset:
        '''Create a new dataset with rows selected following the list/array of indices.

        Args:
            indices (`range`, `list`, `iterable`, `ndarray` or `Series`):
                Range, list or 1D-array of integer indices for indexing.
                If the indices correspond to a contiguous range, the Arrow table is simply sliced.
                However passing a list of indices that are not contiguous creates indices mapping, which is much less efficient,
                but still faster than recreating an Arrow table made of the requested rows.
            keep_in_memory (`bool`, defaults to `False`):
                Keep the indices mapping in memory instead of writing it to a cache file.
            indices_cache_file_name (`str`, *optional*, defaults to `None`):
                Provide the name of a path for the cache file. It is used to store the
                indices mapping instead of the automatically generated cache file name.
            writer_batch_size (`int`, defaults to `1000`):
                Number of rows per write operation for the cache file writer.
                This value is a good trade-off between memory usage during the processing, and processing speed.
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `map`.
            new_fingerprint (`str`, *optional*, defaults to `None`):
                The new fingerprint of the dataset after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.select(range(4))
        Dataset({
            features: [\'text\', \'label\'],
            num_rows: 4
        })
        ```
        '''
    def sort(self, column_names: str | Sequence_[str], reverse: bool | Sequence_[bool] = False, kind: str = 'deprecated', null_placement: str = 'at_end', keep_in_memory: bool = False, load_from_cache_file: bool | None = None, indices_cache_file_name: str | None = None, writer_batch_size: int | None = 1000, new_fingerprint: str | None = None) -> Dataset:
        '''Create a new dataset sorted according to a single or multiple columns.

        Args:
            column_names (`Union[str, Sequence[str]]`):
                Column name(s) to sort by.
            reverse (`Union[bool, Sequence[bool]]`, defaults to `False`):
                If `True`, sort by descending order rather than ascending. If a single bool is provided,
                the value is applied to the sorting of all column names. Otherwise a list of bools with the
                same length and order as column_names must be provided.
            kind (`str`, *optional*):
                Pandas algorithm for sorting selected in `{quicksort, mergesort, heapsort, stable}`,
                The default is `quicksort`. Note that both `stable` and `mergesort` use `timsort` under the covers and, in general,
                the actual implementation will vary with data type. The `mergesort` option is retained for backwards compatibility.
                <Deprecated version="2.8.0">

                `kind` was deprecated in version 2.10.0 and will be removed in 3.0.0.

                </Deprecated>
            null_placement (`str`, defaults to `at_end`):
                Put `None` values at the beginning if `at_start` or `first` or at the end if `at_end` or `last`

                <Added version="1.14.2"/>
            keep_in_memory (`bool`, defaults to `False`):
                Keep the sorted indices in memory instead of writing it to a cache file.
            load_from_cache_file (`Optional[bool]`, defaults to `True` if caching is enabled):
                If a cache file storing the sorted indices
                can be identified, use it instead of recomputing.
            indices_cache_file_name (`str`, *optional*, defaults to `None`):
                Provide the name of a path for the cache file. It is used to store the
                sorted indices instead of the automatically generated cache file name.
            writer_batch_size (`int`, defaults to `1000`):
                Number of rows per write operation for the cache file writer.
                Higher value gives smaller cache files, lower value consume less temporary memory.
            new_fingerprint (`str`, *optional*, defaults to `None`):
                The new fingerprint of the dataset after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset(\'rotten_tomatoes\', split=\'validation\')
        >>> ds[\'label\'][:10]
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        >>> sorted_ds = ds.sort(\'label\')
        >>> sorted_ds[\'label\'][:10]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        >>> another_sorted_ds = ds.sort([\'label\', \'text\'], reverse=[True, False])
        >>> another_sorted_ds[\'label\'][:10]
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ```
        '''
    def shuffle(self, seed: int | None = None, generator: np.random.Generator | None = None, keep_in_memory: bool = False, load_from_cache_file: bool | None = None, indices_cache_file_name: str | None = None, writer_batch_size: int | None = 1000, new_fingerprint: str | None = None) -> Dataset:
        '''Create a new Dataset where the rows are shuffled.

        Currently shuffling uses numpy random generators.
        You can either supply a NumPy BitGenerator to use, or a seed to initiate NumPy\'s default random generator (PCG64).

        Shuffling takes the list of indices `[0:len(my_dataset)]` and shuffles it to create an indices mapping.
        However as soon as your [`Dataset`] has an indices mapping, the speed can become 10x slower.
        This is because there is an extra step to get the row index to read using the indices mapping, and most importantly, you aren\'t reading contiguous chunks of data anymore.
        To restore the speed, you\'d need to rewrite the entire dataset on your disk again using [`Dataset.flatten_indices`], which removes the indices mapping.
        This may take a lot of time depending of the size of your dataset though:

        ```python
        my_dataset[0]  # fast
        my_dataset = my_dataset.shuffle(seed=42)
        my_dataset[0]  # up to 10x slower
        my_dataset = my_dataset.flatten_indices()  # rewrite the shuffled dataset on disk as contiguous chunks of data
        my_dataset[0]  # fast again
        ```

        In this case, we recommend switching to an [`IterableDataset`] and leveraging its fast approximate shuffling method [`IterableDataset.shuffle`].
        It only shuffles the shards order and adds a shuffle buffer to your dataset, which keeps the speed of your dataset optimal:

        ```python
        my_iterable_dataset = my_dataset.to_iterable_dataset(num_shards=128)
        for example in enumerate(my_iterable_dataset):  # fast
            pass

        shuffled_iterable_dataset = my_iterable_dataset.shuffle(seed=42, buffer_size=100)

        for example in enumerate(shuffled_iterable_dataset):  # as fast as before
            pass
        ```

        Args:
            seed (`int`, *optional*):
                A seed to initialize the default BitGenerator if `generator=None`.
                If `None`, then fresh, unpredictable entropy will be pulled from the OS.
                If an `int` or `array_like[ints]` is passed, then it will be passed to SeedSequence to derive the initial BitGenerator state.
            generator (`numpy.random.Generator`, *optional*):
                Numpy random Generator to use to compute the permutation of the dataset rows.
                If `generator=None` (default), uses `np.random.default_rng` (the default BitGenerator (PCG64) of NumPy).
            keep_in_memory (`bool`, default `False`):
                Keep the shuffled indices in memory instead of writing it to a cache file.
            load_from_cache_file (`Optional[bool]`, defaults to `True` if caching is enabled):
                If a cache file storing the shuffled indices
                can be identified, use it instead of recomputing.
            indices_cache_file_name (`str`, *optional*):
                Provide the name of a path for the cache file. It is used to store the
                shuffled indices instead of the automatically generated cache file name.
            writer_batch_size (`int`, defaults to `1000`):
                Number of rows per write operation for the cache file writer.
                This value is a good trade-off between memory usage during the processing, and processing speed.
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `map`.
            new_fingerprint (`str`, *optional*, defaults to `None`):
                The new fingerprint of the dataset after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds[\'label\'][:10]
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        # set a seed
        >>> shuffled_ds = ds.shuffle(seed=42)
        >>> shuffled_ds[\'label\'][:10]
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0]
        ```
        '''
    def train_test_split(self, test_size: float | int | None = None, train_size: float | int | None = None, shuffle: bool = True, stratify_by_column: str | None = None, seed: int | None = None, generator: np.random.Generator | None = None, keep_in_memory: bool = False, load_from_cache_file: bool | None = None, train_indices_cache_file_name: str | None = None, test_indices_cache_file_name: str | None = None, writer_batch_size: int | None = 1000, train_new_fingerprint: str | None = None, test_new_fingerprint: str | None = None) -> DatasetDict:
        '''Return a dictionary ([`datasets.DatasetDict`]) with two random train and test subsets (`train` and `test` `Dataset` splits).
        Splits are created from the dataset according to `test_size`, `train_size` and `shuffle`.

        This method is similar to scikit-learn `train_test_split`.

        Args:
            test_size (`numpy.random.Generator`, *optional*):
                Size of the test split
                If `float`, should be between `0.0` and `1.0` and represent the proportion of the dataset to include in the test split.
                If `int`, represents the absolute number of test samples.
                If `None`, the value is set to the complement of the train size.
                If `train_size` is also `None`, it will be set to `0.25`.
            train_size (`numpy.random.Generator`, *optional*):
                Size of the train split
                If `float`, should be between `0.0` and `1.0` and represent the proportion of the dataset to include in the train split.
                If `int`, represents the absolute number of train samples.
                If `None`, the value is automatically set to the complement of the test size.
            shuffle (`bool`, *optional*, defaults to `True`):
                Whether or not to shuffle the data before splitting.
            stratify_by_column (`str`, *optional*, defaults to `None`):
                The column name of labels to be used to perform stratified split of data.
            seed (`int`, *optional*):
                A seed to initialize the default BitGenerator if `generator=None`.
                If `None`, then fresh, unpredictable entropy will be pulled from the OS.
                If an `int` or `array_like[ints]` is passed, then it will be passed to SeedSequence to derive the initial BitGenerator state.
            generator (`numpy.random.Generator`, *optional*):
                Numpy random Generator to use to compute the permutation of the dataset rows.
                If `generator=None` (default), uses `np.random.default_rng` (the default BitGenerator (PCG64) of NumPy).
            keep_in_memory (`bool`, defaults to `False`):
                Keep the splits indices in memory instead of writing it to a cache file.
            load_from_cache_file (`Optional[bool]`, defaults to `True` if caching is enabled):
                If a cache file storing the splits indices
                can be identified, use it instead of recomputing.
            train_cache_file_name (`str`, *optional*):
                Provide the name of a path for the cache file. It is used to store the
                train split indices instead of the automatically generated cache file name.
            test_cache_file_name (`str`, *optional*):
                Provide the name of a path for the cache file. It is used to store the
                test split indices instead of the automatically generated cache file name.
            writer_batch_size (`int`, defaults to `1000`):
                Number of rows per write operation for the cache file writer.
                This value is a good trade-off between memory usage during the processing, and processing speed.
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `map`.
            train_new_fingerprint (`str`, *optional*, defaults to `None`):
                The new fingerprint of the train set after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments
            test_new_fingerprint (`str`, *optional*, defaults to `None`):
                The new fingerprint of the test set after transform.
                If `None`, the new fingerprint is computed using a hash of the previous fingerprint, and the transform arguments

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds = ds.train_test_split(test_size=0.2, shuffle=True)
        DatasetDict({
            train: Dataset({
                features: [\'text\', \'label\'],
                num_rows: 852
            })
            test: Dataset({
                features: [\'text\', \'label\'],
                num_rows: 214
            })
        })

        # set a seed
        >>> ds = ds.train_test_split(test_size=0.2, seed=42)

        # stratified split
        >>> ds = load_dataset("imdb",split="train")
        Dataset({
            features: [\'text\', \'label\'],
            num_rows: 25000
        })
        >>> ds = ds.train_test_split(test_size=0.2, stratify_by_column="label")
        DatasetDict({
            train: Dataset({
                features: [\'text\', \'label\'],
                num_rows: 20000
            })
            test: Dataset({
                features: [\'text\', \'label\'],
                num_rows: 5000
            })
        })
        ```
        '''
    def shard(self, num_shards: int, index: int, contiguous: bool = False, keep_in_memory: bool = False, indices_cache_file_name: str | None = None, writer_batch_size: int | None = 1000) -> Dataset:
        '''Return the `index`-nth shard from dataset split into `num_shards` pieces.

        This shards deterministically. `dset.shard(n, i)` will contain all elements of dset whose
        index mod `n = i`.

        `dset.shard(n, i, contiguous=True)` will instead split dset into contiguous chunks,
        so it can be easily concatenated back together after processing. If `n % i == l`, then the
        first `l` shards will have length `(n // i) + 1`, and the remaining shards will have length `(n // i)`.
        `datasets.concatenate([dset.shard(n, i, contiguous=True) for i in range(n)])` will return
        a dataset with the same order as the original.

        Be sure to shard before using any randomizing operator (such as `shuffle`).
        It is best if the shard operator is used early in the dataset pipeline.


        Args:
            num_shards (`int`):
                How many shards to split the dataset into.
            index (`int`):
                Which shard to select and return.
            contiguous: (`bool`, defaults to `False`):
                Whether to select contiguous blocks of indices for shards.
            keep_in_memory (`bool`, defaults to `False`):
                Keep the dataset in memory instead of writing it to a cache file.
            indices_cache_file_name (`str`, *optional*):
                Provide the name of a path for the cache file. It is used to store the
                indices of each shard instead of the automatically generated cache file name.
            writer_batch_size (`int`, defaults to `1000`):
                Number of rows per write operation for the cache file writer.
                This value is a good trade-off between memory usage during the processing, and processing speed.
                Higher value makes the processing do fewer lookups, lower value consume less temporary memory while running `map`.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds
        Dataset({
            features: [\'text\', \'label\'],
            num_rows: 1066
        })
        >>> ds.shard(num_shards=2, index=0)
        Dataset({
            features: [\'text\', \'label\'],
            num_rows: 533
        })
        ```
        '''
    def export(self, filename: str, format: str = 'tfrecord'):
        '''Writes the Arrow dataset to a TFRecord file.

        The dataset must already be in tensorflow format. The records will be written with
        keys from `dataset._format_columns`.

        Args:
            filename (`str`): The filename, including the `.tfrecord` extension, to write to.
            format (`str`, optional, default `"tfrecord"`): The type of output file. Currently this is a no-op, as
                TFRecords are the only option. This enables a more flexible function signature later.
        '''
    def to_csv(self, path_or_buf: PathLike | BinaryIO, batch_size: int | None = None, num_proc: int | None = None, **to_csv_kwargs) -> int:
        '''Exports the dataset to csv

        Args:
            path_or_buf (`PathLike` or `FileOrBuffer`):
                Either a path to a file or a BinaryIO.
            batch_size (`int`, *optional*):
                Size of the batch to load in memory and write at once.
                Defaults to `datasets.config.DEFAULT_MAX_BATCH_SIZE`.
            num_proc (`int`, *optional*):
                Number of processes for multiprocessing. By default it doesn\'t
                use multiprocessing. `batch_size` in this case defaults to
                `datasets.config.DEFAULT_MAX_BATCH_SIZE` but feel free to make it 5x or 10x of the default
                value if you have sufficient compute power.
            **to_csv_kwargs (additional keyword arguments):
                Parameters to pass to pandas\'s [`pandas.DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html).

                <Changed version="2.10.0">

                Now, `index` defaults to `False` if not specified.

                If you would like to write the index, pass `index=True` and also set a name for the index column by
                passing `index_label`.

                </Changed>

        Returns:
            `int`: The number of characters or bytes written.

        Example:

        ```py
        >>> ds.to_csv("path/to/dataset/directory")
        ```
        '''
    def to_dict(self, batch_size: int | None = None, batched: str = 'deprecated') -> dict | Iterator[dict]:
        '''Returns the dataset as a Python dict. Can also return a generator for large datasets.

        Args:
            batched (`bool`):
                Set to `True` to return a generator that yields the dataset as batches
                of `batch_size` rows. Defaults to `False` (returns the whole datasets once).

                <Deprecated version="2.11.0">

                Use `.iter(batch_size=batch_size)` followed by `.to_dict()` on the individual batches instead.

                </Deprecated>

            batch_size (`int`, *optional*): The size (number of rows) of the batches if `batched` is `True`.
                Defaults to `datasets.config.DEFAULT_MAX_BATCH_SIZE`.

        Returns:
            `dict` or `Iterator[dict]`

        Example:

        ```py
        >>> ds.to_dict()
        ```
        '''
    def to_list(self) -> list:
        """Returns the dataset as a Python list.

        Returns:
            `list`

        Example:

        ```py
        >>> ds.to_list()
        ```
        """
    def to_json(self, path_or_buf: PathLike | BinaryIO, batch_size: int | None = None, num_proc: int | None = None, **to_json_kwargs) -> int:
        '''Export the dataset to JSON Lines or JSON.

        Args:
            path_or_buf (`PathLike` or `FileOrBuffer`):
                Either a path to a file or a BinaryIO.
            batch_size (`int`, *optional*):
                Size of the batch to load in memory and write at once.
                Defaults to `datasets.config.DEFAULT_MAX_BATCH_SIZE`.
            num_proc (`int`, *optional*):
                Number of processes for multiprocessing. By default it doesn\'t
                use multiprocessing. `batch_size` in this case defaults to
                `datasets.config.DEFAULT_MAX_BATCH_SIZE` but feel free to make it 5x or 10x of the default
                value if you have sufficient compute power.
            **to_json_kwargs (additional keyword arguments):
                Parameters to pass to pandas\'s [`pandas.DataFrame.to_json`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html).

                <Changed version="2.11.0">

                Now, `index` defaults to `False` if `orient` is `"split"` or `"table"`.

                If you would like to write the index, pass `index=True`.

                </Changed>

        Returns:
            `int`: The number of characters or bytes written.

        Example:

        ```py
        >>> ds.to_json("path/to/dataset/directory")
        ```
        '''
    def to_pandas(self, batch_size: int | None = None, batched: bool = False) -> pd.DataFrame | Iterator[pd.DataFrame]:
        """Returns the dataset as a `pandas.DataFrame`. Can also return a generator for large datasets.

        Args:
            batched (`bool`):
                Set to `True` to return a generator that yields the dataset as batches
                of `batch_size` rows. Defaults to `False` (returns the whole datasets once).
            batch_size (`int`, *optional*):
                The size (number of rows) of the batches if `batched` is `True`.
                Defaults to `datasets.config.DEFAULT_MAX_BATCH_SIZE`.

        Returns:
            `pandas.DataFrame` or `Iterator[pandas.DataFrame]`

        Example:

        ```py
        >>> ds.to_pandas()
        ```
        """
    def to_parquet(self, path_or_buf: PathLike | BinaryIO, batch_size: int | None = None, **parquet_writer_kwargs) -> int:
        '''Exports the dataset to parquet

        Args:
            path_or_buf (`PathLike` or `FileOrBuffer`):
                Either a path to a file or a BinaryIO.
            batch_size (`int`, *optional*):
                Size of the batch to load in memory and write at once.
                Defaults to `datasets.config.DEFAULT_MAX_BATCH_SIZE`.
            **parquet_writer_kwargs (additional keyword arguments):
                Parameters to pass to PyArrow\'s `pyarrow.parquet.ParquetWriter`.

        Returns:
            `int`: The number of characters or bytes written.

        Example:

        ```py
        >>> ds.to_parquet("path/to/dataset/directory")
        ```
        '''
    def to_sql(self, name: str, con: str | sqlalchemy.engine.Connection | sqlalchemy.engine.Engine | sqlite3.Connection, batch_size: int | None = None, **sql_writer_kwargs) -> int:
        '''Exports the dataset to a SQL database.

        Args:
            name (`str`):
                Name of SQL table.
            con (`str` or `sqlite3.Connection` or `sqlalchemy.engine.Connection` or `sqlalchemy.engine.Connection`):
                A [URI string](https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls) or a SQLite3/SQLAlchemy connection object used to write to a database.
            batch_size (`int`, *optional*):
                Size of the batch to load in memory and write at once.
                Defaults to `datasets.config.DEFAULT_MAX_BATCH_SIZE`.
            **sql_writer_kwargs (additional keyword arguments):
                Parameters to pass to pandas\'s [`pandas.DataFrame.to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html).

                <Changed version="2.11.0">

                Now, `index` defaults to `False` if not specified.

                If you would like to write the index, pass `index=True` and also set a name for the index column by
                passing `index_label`.

                </Changed>

        Returns:
            `int`: The number of records written.

        Example:

        ```py
        >>> # con provided as a connection URI string
        >>> ds.to_sql("data", "sqlite:///my_own_db.sql")
        >>> # con provided as a sqlite3 connection object
        >>> import sqlite3
        >>> con = sqlite3.connect("my_own_db.sql")
        >>> with con:
        ...     ds.to_sql("data", con)
        ```
        '''
    def to_iterable_dataset(self, num_shards: int | None = 1) -> IterableDataset:
        """Get an [`datasets.IterableDataset`] from a map-style [`datasets.Dataset`].
        This is equivalent to loading a dataset in streaming mode with [`datasets.load_dataset`], but much faster since the data is streamed from local files.

        Contrary to map-style datasets, iterable datasets are lazy and can only be iterated over (e.g. using a for loop).
        Since they are read sequentially in training loops, iterable datasets are much faster than map-style datasets.
        All the transformations applied to iterable datasets like filtering or processing are done on-the-fly when you start iterating over the dataset.

        Still, it is possible to shuffle an iterable dataset using [`datasets.IterableDataset.shuffle`].
        This is a fast approximate shuffling that works best if you have multiple shards and if you specify a buffer size that is big enough.

        To get the best speed performance, make sure your dataset doesn't have an indices mapping.
        If this is the case, the data are not read contiguously, which can be slow sometimes.
        You can use `ds = ds.flatten_indices()` to write your dataset in contiguous chunks of data and have optimal speed before switching to an iterable dataset.

        Args:
            num_shards (`int`, default to `1`):
                Number of shards to define when instantiating the iterable dataset. This is especially useful for big datasets to be able to shuffle properly,
                and also to enable fast parallel loading using a PyTorch DataLoader or in distributed setups for example.
                Shards are defined using [`datasets.Dataset.shard`]: it simply slices the data without writing anything on disk.

        Returns:
            [`datasets.IterableDataset`]

        Example:

        Basic usage:
        ```python
        >>> ids = ds.to_iterable_dataset()
        >>> for example in ids:
        ...     pass
        ```

        With lazy filtering and processing:
        ```python
        >>> ids = ds.to_iterable_dataset()
        >>> ids = ids.filter(filter_fn).map(process_fn)  # will filter and process on-the-fly when you start iterating over the iterable dataset
        >>> for example in ids:
        ...     pass
        ```

        With sharding to enable efficient shuffling:
        ```python
        >>> ids = ds.to_iterable_dataset(num_shards=64)  # the dataset is split into 64 shards to be iterated over
        >>> ids = ids.shuffle(buffer_size=10_000)  # will shuffle the shards order and use a shuffle buffer for fast approximate shuffling when you start iterating
        >>> for example in ids:
        ...     pass
        ```

        With a PyTorch DataLoader:
        ```python
        >>> import torch
        >>> ids = ds.to_iterable_dataset(num_shards=64)
        >>> ids = ids.filter(filter_fn).map(process_fn)
        >>> dataloader = torch.utils.data.DataLoader(ids, num_workers=4)  # will assign 64 / 4 = 16 shards to each worker to load, filter and process when you start iterating
        >>> for example in ids:
        ...     pass
        ```

        With a PyTorch DataLoader and shuffling:
        ```python
        >>> import torch
        >>> ids = ds.to_iterable_dataset(num_shards=64)
        >>> ids = ids.shuffle(buffer_size=10_000)  # will shuffle the shards order and use a shuffle buffer when you start iterating
        >>> dataloader = torch.utils.data.DataLoader(ids, num_workers=4)  # will assign 64 / 4 = 16 shards from the shuffled list of shards to each worker when you start iterating
        >>> for example in ids:
        ...     pass
        ```

        In a distributed setup like PyTorch DDP with a PyTorch DataLoader and shuffling
        ```python
        >>> from datasets.distributed import split_dataset_by_node
        >>> ids = ds.to_iterable_dataset(num_shards=512)
        >>> ids = ids.shuffle(buffer_size=10_000)  # will shuffle the shards order and use a shuffle buffer when you start iterating
        >>> ids = split_dataset_by_node(ds, world_size=8, rank=0)  # will keep only 512 / 8 = 64 shards from the shuffled lists of shards when you start iterating
        >>> dataloader = torch.utils.data.DataLoader(ids, num_workers=4)  # will assign 64 / 4 = 16 shards from this node's list of shards to each worker when you start iterating
        >>> for example in ids:
        ...     pass
        ```

        With shuffling and multiple epochs:
        ```python
        >>> ids = ds.to_iterable_dataset(num_shards=64)
        >>> ids = ids.shuffle(buffer_size=10_000, seed=42)  # will shuffle the shards order and use a shuffle buffer when you start iterating
        >>> for epoch in range(n_epochs):
        ...     ids.set_epoch(epoch)  # will use effective_seed = seed + epoch to shuffle the shards and for the shuffle buffer when you start iterating
        ...     for example in ids:
        ...         pass
        ```
        Feel free to also use [`IterableDataset.set_epoch`] when using a PyTorch DataLoader or in distributed setups.
        """
    def push_to_hub(self, repo_id: str, config_name: str = 'default', split: str | None = None, private: bool | None = False, token: str | None = None, branch: str | None = None, max_shard_size: int | str | None = None, num_shards: int | None = None, embed_external_files: bool = True):
        '''Pushes the dataset to the hub as a Parquet dataset.
        The dataset is pushed using HTTP requests and does not need to have neither git or git-lfs installed.

        The resulting Parquet files are self-contained by default. If your dataset contains [`Image`] or [`Audio`]
        data, the Parquet files will store the bytes of your images or audio files.
        You can disable this by setting `embed_external_files` to `False`.

        Args:
            repo_id (`str`):
                The ID of the repository to push to in the following format: `<user>/<dataset_name>` or
                `<org>/<dataset_name>`. Also accepts `<dataset_name>`, which will default to the namespace
                of the logged-in user.
            config_name (`str`, defaults to "default"):
                The configuration name of a dataset. Defaults to "default"
            split (`str`, *optional*):
                The name of the split that will be given to that dataset. Defaults to `self.split`.
            private (`bool`, *optional*, defaults to `False`):
                Whether the dataset repository should be set to private or not. Only affects repository creation:
                a repository that already exists will not be affected by that parameter.
            token (`str`, *optional*):
                An optional authentication token for the Hugging Face Hub. If no token is passed, will default
                to the token saved locally when logging in with `huggingface-cli login`. Will raise an error
                if no token is passed and the user is not logged-in.
            branch (`str`, *optional*):
                The git branch on which to push the dataset. This defaults to the default branch as specified
                in your repository, which defaults to `"main"`.
            max_shard_size (`int` or `str`, *optional*, defaults to `"500MB"`):
                The maximum size of the dataset shards to be uploaded to the hub. If expressed as a string, needs to be digits followed by
                a unit (like `"5MB"`).
            num_shards (`int`, *optional*): Number of shards to write. By default the number of shards depends on `max_shard_size`.

                <Added version="2.8.0"/>
            embed_external_files (`bool`, defaults to `True`):
                Whether to embed file bytes in the shards.
                In particular, this will do the following before the push for the fields of type:

                - [`Audio`] and [`Image`]: remove local path information and embed file content in the Parquet files.

        Example:

        ```python
        >>> dataset.push_to_hub("<organization>/<dataset_id>")
        >>> dataset.push_to_hub("<organization>/<dataset_id>", split="validation")
        >>> dataset.push_to_hub("<organization>/<dataset_id>", max_shard_size="1GB")
        >>> dataset.push_to_hub("<organization>/<dataset_id>", num_shards=1024)
        ```
        '''
    def add_column(self, name: str, column: list | np.array, new_fingerprint: str):
        '''Add column to Dataset.

        <Added version="1.7"/>

        Args:
            name (`str`):
                Column name.
            column (`list` or `np.array`):
                Column data to be added.

        Returns:
            [`Dataset`]

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> more_text = ds["text"]
        >>> ds.add_column(name="text_2", column=more_text)
        Dataset({
            features: [\'text\', \'label\', \'text_2\'],
            num_rows: 1066
        })
        ```
        '''
    def add_faiss_index(self, column: str, index_name: str | None = None, device: int | None = None, string_factory: str | None = None, metric_type: int | None = None, custom_index: faiss.Index | None = None, batch_size: int = 1000, train_size: int | None = None, faiss_verbose: bool = False, dtype=...):
        '''Add a dense index using Faiss for fast retrieval.
        By default the index is done over the vectors of the specified column.
        You can specify `device` if you want to run it on GPU (`device` must be the GPU index).
        You can find more information about Faiss here:

        - For [string factory](https://github.com/facebookresearch/faiss/wiki/The-index-factory)

        Args:
            column (`str`):
                The column of the vectors to add to the index.
            index_name (`str`, *optional*):
                The `index_name`/identifier of the index.
                This is the `index_name` that is used to call [`~datasets.Dataset.get_nearest_examples`] or [`~datasets.Dataset.search`].
                By default it corresponds to `column`.
            device (`Union[int, List[int]]`, *optional*):
                If positive integer, this is the index of the GPU to use. If negative integer, use all GPUs.
                If a list of positive integers is passed in, run only on those GPUs. By default it uses the CPU.
            string_factory (`str`, *optional*):
                This is passed to the index factory of Faiss to create the index.
                Default index class is `IndexFlat`.
            metric_type (`int`, *optional*):
                Type of metric. Ex: `faiss.METRIC_INNER_PRODUCT` or `faiss.METRIC_L2`.
            custom_index (`faiss.Index`, *optional*):
                Custom Faiss index that you already have instantiated and configured for your needs.
            batch_size (`int`):
                Size of the batch to use while adding vectors to the `FaissIndex`. Default value is `1000`.
                <Added version="2.4.0"/>
            train_size (`int`, *optional*):
                If the index needs a training step, specifies how many vectors will be used to train the index.
            faiss_verbose (`bool`, defaults to `False`):
                Enable the verbosity of the Faiss index.
            dtype (`data-type`):
                The dtype of the numpy arrays that are indexed.
                Default is `np.float32`.

        Example:

        ```python
        >>> ds = datasets.load_dataset(\'crime_and_punish\', split=\'train\')
        >>> ds_with_embeddings = ds.map(lambda example: {\'embeddings\': embed(example[\'line\']}))
        >>> ds_with_embeddings.add_faiss_index(column=\'embeddings\')
        >>> # query
        >>> scores, retrieved_examples = ds_with_embeddings.get_nearest_examples(\'embeddings\', embed(\'my new query\'), k=10)
        >>> # save index
        >>> ds_with_embeddings.save_faiss_index(\'embeddings\', \'my_index.faiss\')

        >>> ds = datasets.load_dataset(\'crime_and_punish\', split=\'train\')
        >>> # load index
        >>> ds.load_faiss_index(\'embeddings\', \'my_index.faiss\')
        >>> # query
        >>> scores, retrieved_examples = ds.get_nearest_examples(\'embeddings\', embed(\'my new query\'), k=10)
        ```
        '''
    def add_faiss_index_from_external_arrays(self, external_arrays: np.array, index_name: str, device: int | None = None, string_factory: str | None = None, metric_type: int | None = None, custom_index: faiss.Index | None = None, batch_size: int = 1000, train_size: int | None = None, faiss_verbose: bool = False, dtype=...):
        '''Add a dense index using Faiss for fast retrieval.
        The index is created using the vectors of `external_arrays`.
        You can specify `device` if you want to run it on GPU (`device` must be the GPU index).
        You can find more information about Faiss here:

        - For [string factory](https://github.com/facebookresearch/faiss/wiki/The-index-factory)

        Args:
            external_arrays (`np.array`):
                If you want to use arrays from outside the lib for the index, you can set `external_arrays`.
                It will use `external_arrays` to create the Faiss index instead of the arrays in the given `column`.
            index_name (`str`):
                The `index_name`/identifier of the index.
                This is the `index_name` that is used to call [`~datasets.Dataset.get_nearest_examples`] or [`~datasets.Dataset.search`].
            device (Optional `Union[int, List[int]]`, *optional*):
                If positive integer, this is the index of the GPU to use. If negative integer, use all GPUs.
                If a list of positive integers is passed in, run only on those GPUs. By default it uses the CPU.
            string_factory (`str`, *optional*):
                This is passed to the index factory of Faiss to create the index.
                Default index class is `IndexFlat`.
            metric_type (`int`, *optional*):
                Type of metric. Ex: `faiss.faiss.METRIC_INNER_PRODUCT` or `faiss.METRIC_L2`.
            custom_index (`faiss.Index`, *optional*):
                Custom Faiss index that you already have instantiated and configured for your needs.
            batch_size (`int`, *optional*):
                Size of the batch to use while adding vectors to the FaissIndex. Default value is 1000.
                <Added version="2.4.0"/>
            train_size (`int`, *optional*):
                If the index needs a training step, specifies how many vectors will be used to train the index.
            faiss_verbose (`bool`, defaults to False):
                Enable the verbosity of the Faiss index.
            dtype (`numpy.dtype`):
                The dtype of the numpy arrays that are indexed. Default is np.float32.
        '''
    def add_elasticsearch_index(self, column: str, index_name: str | None = None, host: str | None = None, port: int | None = None, es_client: elasticsearch.Elasticsearch | None = None, es_index_name: str | None = None, es_index_config: dict | None = None):
        '''Add a text index using ElasticSearch for fast retrieval. This is done in-place.

        Args:
            column (`str`):
                The column of the documents to add to the index.
            index_name (`str`, *optional*):
                The `index_name`/identifier of the index.
                This is the index name that is used to call [`~Dataset.get_nearest_examples`] or [`Dataset.search`].
                By default it corresponds to `column`.
            host (`str`, *optional*, defaults to `localhost`):
                Host of where ElasticSearch is running.
            port (`str`, *optional*, defaults to `9200`):
                Port of where ElasticSearch is running.
            es_client (`elasticsearch.Elasticsearch`, *optional*):
                The elasticsearch client used to create the index if host and port are `None`.
            es_index_name (`str`, *optional*):
                The elasticsearch index name used to create the index.
            es_index_config (`dict`, *optional*):
                The configuration of the elasticsearch index.
                Default config is:
                    ```
                    {
                        "settings": {
                            "number_of_shards": 1,
                            "analysis": {"analyzer": {"stop_standard": {"type": "standard", " stopwords": "_english_"}}},
                        },
                        "mappings": {
                            "properties": {
                                "text": {
                                    "type": "text",
                                    "analyzer": "standard",
                                    "similarity": "BM25"
                                },
                            }
                        },
                    }
                    ```
        Example:

        ```python
        >>> es_client = elasticsearch.Elasticsearch()
        >>> ds = datasets.load_dataset(\'crime_and_punish\', split=\'train\')
        >>> ds.add_elasticsearch_index(column=\'line\', es_client=es_client, es_index_name="my_es_index")
        >>> scores, retrieved_examples = ds.get_nearest_examples(\'line\', \'my new query\', k=10)
        ```
        '''
    def add_item(self, item: dict, new_fingerprint: str):
        '''Add item to Dataset.

        <Added version="1.7"/>

        Args:
            item (`dict`):
                Item data to be added.

        Returns:
            [`Dataset`]

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> new_review = {\'label\': 0, \'text\': \'this movie is the absolute worst thing I have ever seen\'}
        >>> ds = ds.add_item(new_review)
        >>> ds[-1]
        {\'label\': 0, \'text\': \'this movie is the absolute worst thing I have ever seen\'}
        ```
        '''
    def align_labels_with_mapping(self, label2id: Dict, label_column: str) -> Dataset:
        '''Align the dataset\'s label ID and label name mapping to match an input `label2id` mapping.
        This is useful when you want to ensure that a model\'s predicted labels are aligned with the dataset.
        The alignment in done using the lowercase label names.

        Args:
            label2id (`dict`):
                The label name to ID mapping to align the dataset with.
            label_column (`str`):
                The column name of labels to align on.

        Example:

        ```python
        >>> # dataset with mapping {\'entailment\': 0, \'neutral\': 1, \'contradiction\': 2}
        >>> ds = load_dataset("glue", "mnli", split="train")
        >>> # mapping to align with
        >>> label2id = {\'CONTRADICTION\': 0, \'NEUTRAL\': 1, \'ENTAILMENT\': 2}
        >>> ds_aligned = ds.align_labels_with_mapping(label2id, "label")
        ```

        '''

def get_indices_from_mask_function(function: Callable, batched: bool, with_indices: bool, input_columns: str | List[str] | None, indices_mapping: Table | None = None, *args, **fn_kwargs): ...
