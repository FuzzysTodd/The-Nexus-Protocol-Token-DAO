import datasets
from ..folder_based_builder import folder_based_builder as folder_based_builder
from _typeshed import Incomplete
from datasets.tasks import AudioClassification as AudioClassification
from typing import List

logger: Incomplete

class AudioFolderConfig(folder_based_builder.FolderBasedBuilderConfig):
    """Builder Config for AudioFolder."""
    drop_labels: bool
    drop_metadata: bool

class AudioFolder(folder_based_builder.FolderBasedBuilder):
    BASE_FEATURE = datasets.Audio
    BASE_COLUMN_NAME: str
    BUILDER_CONFIG_CLASS = AudioFolderConfig
    EXTENSIONS: List[str]
    CLASSIFICATION_TASK: Incomplete

AUDIO_EXTENSIONS: Incomplete
