import datasets
from dataclasses import dataclass
from datasets.table import table_cast as table_cast

@dataclass
class PandasConfig(datasets.BuilderConfig):
    """BuilderConfig for Pandas."""
    features: datasets.Features | None = ...
    def __init__(self, name, version, data_dir, data_files, description, features) -> None: ...

class Pandas(datasets.ArrowBasedBuilder):
    BUILDER_CONFIG_CLASS = PandasConfig
