import yaml
from ..config import METADATA_CONFIGS_FIELD as METADATA_CONFIGS_FIELD
from ..utils.logging import get_logger as get_logger
from .deprecation_utils import deprecated as deprecated
from _typeshed import Incomplete
from huggingface_hub import DatasetCardData as DatasetCardData
from pathlib import Path
from typing import Any, ClassVar, Dict

logger: Incomplete

class _NoDuplicateSafeLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep: bool = False): ...

class DatasetMetadata(dict):
    @classmethod
    def from_readme(cls, path: Path | str) -> DatasetMetadata:
        """Loads and validates the dataset metadata from its dataset card (README.md)

        Args:
            path (:obj:`Path`): Path to the dataset card (its README.md file)

        Returns:
            :class:`DatasetMetadata`: The dataset's metadata

        Raises:
            :obj:`TypeError`: If the dataset's metadata is invalid
        """
    def to_readme(self, path: Path): ...
    @classmethod
    def from_yaml_string(cls, string: str) -> DatasetMetadata:
        """Loads and validates the dataset metadata from a YAML string

        Args:
            string (:obj:`str`): The YAML string

        Returns:
            :class:`DatasetMetadata`: The dataset's metadata

        Raises:
            :obj:`TypeError`: If the dataset's metadata is invalid
        """
    def to_yaml_string(self) -> str: ...

class MetadataConfigs(Dict[str, Dict[str, Any]]):
    """Should be in format {config_name: {**config_params}}."""
    FIELD_NAME: ClassVar[str]
    @classmethod
    def from_dataset_card_data(cls, dataset_card_data: DatasetCardData) -> MetadataConfigs: ...
    def to_dataset_card_data(self, dataset_card_data: DatasetCardData) -> None: ...
    def get_default_config_name(self) -> str | None: ...

known_task_ids: Incomplete
