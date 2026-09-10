import datasets
from _typeshed import Incomplete
from dataclasses import dataclass
from datasets.table import table_cast as table_cast
from typing import List

logger: Incomplete

@dataclass
class ParquetConfig(datasets.BuilderConfig):
    """BuilderConfig for Parquet."""
    batch_size: int = ...
    columns: List[str] | None = ...
    features: datasets.Features | None = ...
    def __init__(self, name, version, data_dir, data_files, description, batch_size, columns, features) -> None: ...

class Parquet(datasets.ArrowBasedBuilder):
    BUILDER_CONFIG_CLASS = ParquetConfig
