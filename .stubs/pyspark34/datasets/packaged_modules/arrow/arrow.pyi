import datasets
from _typeshed import Incomplete
from dataclasses import dataclass
from datasets.table import table_cast as table_cast

logger: Incomplete

@dataclass
class ArrowConfig(datasets.BuilderConfig):
    """BuilderConfig for Arrow."""
    features: datasets.Features | None = ...
    def __init__(self, name, version, data_dir, data_files, description, features) -> None: ...

class Arrow(datasets.ArrowBasedBuilder):
    BUILDER_CONFIG_CLASS = ArrowConfig
