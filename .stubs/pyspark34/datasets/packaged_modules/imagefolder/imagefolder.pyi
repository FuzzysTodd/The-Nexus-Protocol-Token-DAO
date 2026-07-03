import datasets
from ..folder_based_builder import folder_based_builder as folder_based_builder
from _typeshed import Incomplete
from datasets.tasks import ImageClassification as ImageClassification
from typing import List

logger: Incomplete

class ImageFolderConfig(folder_based_builder.FolderBasedBuilderConfig):
    """BuilderConfig for ImageFolder."""
    drop_labels: bool
    drop_metadata: bool

class ImageFolder(folder_based_builder.FolderBasedBuilder):
    BASE_FEATURE = datasets.Image
    BASE_COLUMN_NAME: str
    BUILDER_CONFIG_CLASS = ImageFolderConfig
    EXTENSIONS: List[str]
    CLASSIFICATION_TASK: Incomplete

IMAGE_EXTENSIONS: Incomplete
