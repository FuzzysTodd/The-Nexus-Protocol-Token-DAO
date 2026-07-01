import datasets
from _typeshed import Incomplete
from dataclasses import dataclass
from datasets.features.features import FeatureType as FeatureType
from datasets.tasks.base import TaskTemplate as TaskTemplate
from typing import List, Type

logger: Incomplete

def count_path_segments(path): ...

@dataclass
class FolderBasedBuilderConfig(datasets.BuilderConfig):
    """BuilderConfig for AutoFolder."""
    features: datasets.Features | None = ...
    drop_labels: bool = ...
    drop_metadata: bool = ...
    def __init__(self, name, version, data_dir, data_files, description, features, drop_labels, drop_metadata) -> None: ...

class FolderBasedBuilder(datasets.GeneratorBasedBuilder):
    '''
    Base class for generic data loaders for vision and image data.


    Abstract class attributes to be overridden by a child class:
        BASE_FEATURE: feature object to decode data (i.e. datasets.Image, datasets.Audio, ...)
        BASE_COLUMN_NAME: string key name of a base feature (i.e. "image", "audio", ...)
        BUILDER_CONFIG_CLASS: builder config inherited from `folder_based_builder.FolderBasedBuilderConfig`
        EXTENSIONS: list of allowed extensions (only files with these extensions and METADATA_FILENAME files
            will be included in a dataset)
        CLASSIFICATION_TASK: classification task to use if labels are obtained from the folder structure
    '''
    BASE_FEATURE: Type[FeatureType]
    BASE_COLUMN_NAME: str
    BUILDER_CONFIG_CLASS: FolderBasedBuilderConfig
    EXTENSIONS: List[str]
    CLASSIFICATION_TASK: TaskTemplate
    METADATA_FILENAMES: List[str]
