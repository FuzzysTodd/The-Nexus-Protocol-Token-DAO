from . import config as config
from .features import Features as Features, Value as Value
from .filesystems import is_remote_filesystem as is_remote_filesystem
from .splits import SplitDict as SplitDict
from .tasks import TaskTemplate as TaskTemplate, task_template_from_dict as task_template_from_dict
from .utils import Version as Version
from .utils.logging import get_logger as get_logger
from .utils.py_utils import asdict as asdict, unique_values as unique_values
from _typeshed import Incomplete
from dataclasses import dataclass
from huggingface_hub import DatasetCardData
from typing import Dict, List

logger: Incomplete

@dataclass
class SupervisedKeysData:
    input: str = ...
    output: str = ...
    def __init__(self, input, output) -> None: ...

@dataclass
class DownloadChecksumsEntryData:
    key: str = ...
    value: str = ...
    def __init__(self, key, value) -> None: ...

class MissingCachedSizesConfigError(Exception):
    """The expected cached sizes of the download file are missing."""
class NonMatchingCachedSizesError(Exception):
    """The prepared split doesn't have expected sizes."""

@dataclass
class PostProcessedInfo:
    features: Features | None = ...
    resources_checksums: dict | None = ...
    def __post_init__(self) -> None: ...
    @classmethod
    def from_dict(cls, post_processed_info_dict: dict) -> PostProcessedInfo: ...
    def __init__(self, features, resources_checksums) -> None: ...

@dataclass
class DatasetInfo:
    """Information about a dataset.

    `DatasetInfo` documents datasets, including its name, version, and features.
    See the constructor arguments and properties for a full list.

    Not all fields are known on construction and may be updated later.

    Attributes:
        description (`str`):
            A description of the dataset.
        citation (`str`):
            A BibTeX citation of the dataset.
        homepage (`str`):
            A URL to the official homepage for the dataset.
        license (`str`):
            The dataset's license. It can be the name of the license or a paragraph containing the terms of the license.
        features ([`Features`], *optional*):
            The features used to specify the dataset's column types.
        post_processed (`PostProcessedInfo`, *optional*):
            Information regarding the resources of a possible post-processing of a dataset. For example, it can contain the information of an index.
        supervised_keys (`SupervisedKeysData`, *optional*):
            Specifies the input feature and the label for supervised learning if applicable for the dataset (legacy from TFDS).
        builder_name (`str`, *optional*):
            The name of the `GeneratorBasedBuilder` subclass used to create the dataset. Usually matched to the corresponding script name. It is also the snake_case version of the dataset builder class name.
        config_name (`str`, *optional*):
            The name of the configuration derived from [`BuilderConfig`].
        version (`str` or [`Version`], *optional*):
            The version of the dataset.
        splits (`dict`, *optional*):
            The mapping between split name and metadata.
        download_checksums (`dict`, *optional*):
            The mapping between the URL to download the dataset's checksums and corresponding metadata.
        download_size (`int`, *optional*):
            The size of the files to download to generate the dataset, in bytes.
        post_processing_size (`int`, *optional*):
            Size of the dataset in bytes after post-processing, if any.
        dataset_size (`int`, *optional*):
            The combined size in bytes of the Arrow tables for all splits.
        size_in_bytes (`int`, *optional*):
            The combined size in bytes of all files associated with the dataset (downloaded files + Arrow files).
        task_templates (`List[TaskTemplate]`, *optional*):
            The task templates to prepare the dataset for during training and evaluation. Each template casts the dataset's [`Features`] to standardized column names and types as detailed in `datasets.tasks`.
        **config_kwargs (additional keyword arguments):
            Keyword arguments to be passed to the [`BuilderConfig`] and used in the [`DatasetBuilder`].
    """
    description: str = ...
    citation: str = ...
    homepage: str = ...
    license: str = ...
    features: Features | None = ...
    post_processed: PostProcessedInfo | None = ...
    supervised_keys: SupervisedKeysData | None = ...
    task_templates: List[TaskTemplate] | None = ...
    builder_name: str | None = ...
    dataset_name: str | None = ...
    config_name: str | None = ...
    version: str | Version | None = ...
    splits: dict | None = ...
    download_checksums: dict | None = ...
    download_size: int | None = ...
    post_processing_size: int | None = ...
    dataset_size: int | None = ...
    size_in_bytes: int | None = ...
    def __post_init__(self) -> None: ...
    def write_to_directory(self, dataset_info_dir, pretty_print: bool = False, fs: str = 'deprecated', storage_options: dict | None = None):
        '''Write `DatasetInfo` and license (if present) as JSON files to `dataset_info_dir`.

        Args:
            dataset_info_dir (`str`):
                Destination directory.
            pretty_print (`bool`, defaults to `False`):
                If `True`, the JSON will be pretty-printed with the indent level of 4.
            fs (`fsspec.spec.AbstractFileSystem`, *optional*):
                Instance of the remote filesystem used to download the files from.

                <Deprecated version="2.9.0">

                `fs` was deprecated in version 2.9.0 and will be removed in 3.0.0.
                Please use `storage_options` instead, e.g. `storage_options=fs.storage_options`.

                </Deprecated>

            storage_options (`dict`, *optional*):
                Key/value pairs to be passed on to the file-system backend, if any.

                <Added version="2.9.0"/>

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="validation")
        >>> ds.info.write_to_directory("/path/to/directory/")
        ```
        '''
    @classmethod
    def from_merge(cls, dataset_infos: List['DatasetInfo']): ...
    @classmethod
    def from_directory(cls, dataset_info_dir: str, fs: str = 'deprecated', storage_options: dict | None = None) -> DatasetInfo:
        '''Create [`DatasetInfo`] from the JSON file in `dataset_info_dir`.

        This function updates all the dynamically generated fields (num_examples,
        hash, time of creation,...) of the [`DatasetInfo`].

        This will overwrite all previous metadata.

        Args:
            dataset_info_dir (`str`):
                The directory containing the metadata file. This
                should be the root directory of a specific dataset version.
            fs (`fsspec.spec.AbstractFileSystem`, *optional*):
                Instance of the remote filesystem used to download the files from.

                <Deprecated version="2.9.0">

                `fs` was deprecated in version 2.9.0 and will be removed in 3.0.0.
                Please use `storage_options` instead, e.g. `storage_options=fs.storage_options`.

                </Deprecated>

            storage_options (`dict`, *optional*):
                Key/value pairs to be passed on to the file-system backend, if any.

                <Added version="2.9.0"/>

        Example:

        ```py
        >>> from datasets import DatasetInfo
        >>> ds_info = DatasetInfo.from_directory("/path/to/directory/")
        ```
        '''
    @classmethod
    def from_dict(cls, dataset_info_dict: dict) -> DatasetInfo: ...
    def update(self, other_dataset_info: DatasetInfo, ignore_none: bool = True): ...
    def copy(self) -> DatasetInfo: ...
    def __init__(self, description, citation, homepage, license, features, post_processed, supervised_keys, task_templates, builder_name, dataset_name, config_name, version, splits, download_checksums, download_size, post_processing_size, dataset_size, size_in_bytes) -> None: ...

class DatasetInfosDict(Dict[str, DatasetInfo]):
    def write_to_directory(self, dataset_infos_dir, overwrite: bool = False, pretty_print: bool = False) -> None: ...
    @classmethod
    def from_directory(cls, dataset_infos_dir) -> DatasetInfosDict: ...
    @classmethod
    def from_dataset_card_data(cls, dataset_card_data: DatasetCardData) -> DatasetInfosDict: ...
    def to_dataset_card_data(self, dataset_card_data: DatasetCardData) -> None: ...

@dataclass
class MetricInfo:
    """Information about a metric.

    `MetricInfo` documents a metric, including its name, version, and features.
    See the constructor arguments and properties for a full list.

    Note: Not all fields are known on construction and may be updated later.
    """
    description: str
    citation: str
    features: Features
    inputs_description: str = ...
    homepage: str = ...
    license: str = ...
    codebase_urls: List[str] = ...
    reference_urls: List[str] = ...
    streamable: bool = ...
    format: str | None = ...
    metric_name: str | None = ...
    config_name: str | None = ...
    experiment_id: str | None = ...
    def __post_init__(self) -> None: ...
    def write_to_directory(self, metric_info_dir, pretty_print: bool = False) -> None:
        '''Write `MetricInfo` as JSON to `metric_info_dir`.
        Also save the license separately in LICENCE.
        If `pretty_print` is True, the JSON will be pretty-printed with the indent level of 4.

        Example:

        ```py
        >>> from datasets import load_metric
        >>> metric = load_metric("accuracy")
        >>> metric.info.write_to_directory("/path/to/directory/")
        ```
        '''
    @classmethod
    def from_directory(cls, metric_info_dir) -> MetricInfo:
        '''Create MetricInfo from the JSON file in `metric_info_dir`.

        Args:
            metric_info_dir: `str` The directory containing the metadata file. This
                should be the root directory of a specific dataset version.

        Example:

        ```py
        >>> from datasets import MetricInfo
        >>> metric_info = MetricInfo.from_directory("/path/to/directory/")
        ```
        '''
    @classmethod
    def from_dict(cls, metric_info_dict: dict) -> MetricInfo: ...
    def __init__(self, description, citation, features, inputs_description, homepage, license, codebase_urls, reference_urls, streamable, format, metric_name, config_name, experiment_id) -> None: ...
