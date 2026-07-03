from .. import Audio as Audio, Dataset as Dataset, Features as Features, Image as Image, NamedSplit as NamedSplit, Value as Value, config as config
from ..features.features import FeatureType as FeatureType
from ..formatting import query_table as query_table
from ..packaged_modules.parquet.parquet import Parquet as Parquet
from ..utils import logging as logging
from ..utils.typing import NestedDataStructureLike as NestedDataStructureLike, PathLike as PathLike
from .abc import AbstractDatasetReader as AbstractDatasetReader
from _typeshed import Incomplete
from typing import BinaryIO

def get_writer_batch_size(features: Features) -> int | None:
    """
    Get the writer_batch_size that defines the maximum row group size in the parquet files.
    The default in `datasets` is 1,000 but we lower it to 100 for image datasets.
    This allows to optimize random access to parquet file, since accessing 1 row requires
    to read its entire row group.

    This can be improved to get optimized size for querying/iterating
    but at least it matches the dataset viewer expectations on HF.

    Args:
        ds_config_info (`datasets.info.DatasetInfo`):
            Dataset info from `datasets`.
    Returns:
        writer_batch_size (`Optional[int]`):
            Writer batch size to pass to a dataset builder.
            If `None`, then it will use the `datasets` default.
    """

class ParquetDatasetReader(AbstractDatasetReader):
    builder: Incomplete
    def __init__(self, path_or_paths: NestedDataStructureLike[PathLike], split: NamedSplit | None = None, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, streaming: bool = False, num_proc: int | None = None, **kwargs) -> None: ...
    def read(self): ...

class ParquetDatasetWriter:
    dataset: Incomplete
    path_or_buf: Incomplete
    batch_size: Incomplete
    parquet_writer_kwargs: Incomplete
    def __init__(self, dataset: Dataset, path_or_buf: PathLike | BinaryIO, batch_size: int | None = None, **parquet_writer_kwargs) -> None: ...
    def write(self) -> int: ...
