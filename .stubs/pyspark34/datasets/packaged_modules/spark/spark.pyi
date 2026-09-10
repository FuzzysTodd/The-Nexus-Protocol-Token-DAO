import datasets
import numpy as np
import pyspark
from _typeshed import Incomplete
from dataclasses import dataclass
from datasets.arrow_writer import ArrowWriter as ArrowWriter, ParquetWriter as ParquetWriter
from datasets.config import MAX_SHARD_SIZE as MAX_SHARD_SIZE
from datasets.filesystems import is_remote_filesystem as is_remote_filesystem, rename as rename
from datasets.iterable_dataset import _BaseExamplesIterable
from datasets.utils.py_utils import convert_file_size_to_int as convert_file_size_to_int

logger: Incomplete

@dataclass
class SparkConfig(datasets.BuilderConfig):
    """BuilderConfig for Spark."""
    features: datasets.Features | None = ...
    def __init__(self, name, version, data_dir, data_files, description, features) -> None: ...

class SparkExamplesIterable(_BaseExamplesIterable):
    df: Incomplete
    partition_order: Incomplete
    generate_examples_fn: Incomplete
    def __init__(self, df: pyspark.sql.DataFrame, partition_order: Incomplete | None = None) -> None: ...
    def __iter__(self): ...
    def shuffle_data_sources(self, generator: np.random.Generator) -> SparkExamplesIterable: ...
    def shard_data_sources(self, worker_id: int, num_workers: int) -> SparkExamplesIterable: ...
    @property
    def n_shards(self) -> int: ...

class Spark(datasets.DatasetBuilder):
    BUILDER_CONFIG_CLASS = SparkConfig
    df: Incomplete
    def __init__(self, df: pyspark.sql.DataFrame, cache_dir: str = None, working_dir: str = None, **config_kwargs) -> None: ...
