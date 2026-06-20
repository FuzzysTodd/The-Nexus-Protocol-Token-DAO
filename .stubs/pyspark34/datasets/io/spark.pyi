import pyspark
from .. import Features as Features, NamedSplit as NamedSplit
from ..download import DownloadMode as DownloadMode
from ..packaged_modules.spark.spark import Spark as Spark
from .abc import AbstractDatasetReader as AbstractDatasetReader
from _typeshed import Incomplete

class SparkDatasetReader(AbstractDatasetReader):
    """A dataset reader that reads from a Spark DataFrame.

    When caching, cache materialization is parallelized over Spark; an NFS that is accessible to the driver must be
    provided. Streaming is not currently supported.
    """
    builder: Incomplete
    def __init__(self, df: pyspark.sql.DataFrame, split: NamedSplit | None = None, features: Features | None = None, streaming: bool = True, cache_dir: str = None, keep_in_memory: bool = False, working_dir: str = None, load_from_cache_file: bool = True, file_format: str = 'arrow', **kwargs) -> None: ...
    def read(self): ...
