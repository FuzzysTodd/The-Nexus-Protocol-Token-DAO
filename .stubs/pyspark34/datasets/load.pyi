from . import config as config
from .arrow_dataset import Dataset as Dataset
from .builder import BuilderConfig as BuilderConfig, DatasetBuilder as DatasetBuilder
from .data_files import DEFAULT_PATTERNS_ALL as DEFAULT_PATTERNS_ALL, DataFilesDict as DataFilesDict, DataFilesList as DataFilesList, EmptyDatasetError as EmptyDatasetError, get_data_patterns as get_data_patterns, get_metadata_patterns as get_metadata_patterns, sanitize_patterns as sanitize_patterns
from .dataset_dict import DatasetDict as DatasetDict, IterableDatasetDict as IterableDatasetDict
from .download.download_config import DownloadConfig as DownloadConfig
from .download.download_manager import DownloadMode as DownloadMode
from .download.streaming_download_manager import StreamingDownloadManager as StreamingDownloadManager, xbasename as xbasename, xglob as xglob, xjoin as xjoin
from .features import Features as Features
from .filesystems import extract_path_from_uri as extract_path_from_uri, is_remote_filesystem as is_remote_filesystem
from .fingerprint import Hasher as Hasher
from .info import DatasetInfo as DatasetInfo, DatasetInfosDict as DatasetInfosDict
from .iterable_dataset import IterableDataset as IterableDataset
from .metric import Metric as Metric
from .naming import camelcase_to_snakecase as camelcase_to_snakecase, snakecase_to_camelcase as snakecase_to_camelcase
from .splits import Split as Split
from .utils.deprecation_utils import deprecated as deprecated
from .utils.file_utils import OfflineModeIsEnabled as OfflineModeIsEnabled, cached_path as cached_path, head_hf_s3 as head_hf_s3, hf_github_url as hf_github_url, init_hf_modules as init_hf_modules, is_relative_path as is_relative_path, relative_to_absolute_path as relative_to_absolute_path, url_or_path_join as url_or_path_join
from .utils.filelock import FileLock as FileLock
from .utils.hub import hf_hub_url as hf_hub_url
from .utils.info_utils import VerificationMode as VerificationMode, is_small_dataset as is_small_dataset
from .utils.logging import get_logger as get_logger
from .utils.metadata import MetadataConfigs as MetadataConfigs
from .utils.py_utils import get_imports as get_imports
from .utils.version import Version as Version
from _typeshed import Incomplete
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence, Tuple, Type

logger: Incomplete
ALL_ALLOWED_EXTENSIONS: Incomplete

def init_dynamic_modules(name: str = ..., hf_modules_cache: Path | str | None = None):
    """
    Create a module with name `name` in which you can add dynamic modules
    such as metrics or datasets. The module can be imported using its name.
    The module is created in the HF_MODULE_CACHE directory by default (~/.cache/huggingface/modules) but it can
    be overridden by specifying a path to another directory in `hf_modules_cache`.
    """
def import_main_class(module_path, dataset: bool = True) -> Type[DatasetBuilder] | Type[Metric] | None:
    """Import a module at module_path and return its main class:
    - a DatasetBuilder if dataset is True
    - a Metric if dataset is False
    """

class _InitializeConfiguredDatasetBuilder:
    """
    From https://stackoverflow.com/questions/4647566/pickle-a-dynamically-parameterized-sub-class
    See also ConfiguredDatasetBuilder.__reduce__
    When called with the param value as the only argument, returns an
    un-initialized instance of the parameterized class. Subsequent __setstate__
    will be called by pickle.
    """
    def __call__(self, builder_cls, metadata_configs, default_config_name, name): ...

def configure_builder_class(builder_cls: Type[DatasetBuilder], builder_configs: List[BuilderConfig], default_config_name: str | None, dataset_name: str) -> Type[DatasetBuilder]:
    """
    Dynamically create a builder class with custom builder configs parsed from README.md file,
    i.e. set BUILDER_CONFIGS class variable of a builder class to custom configs list.
    """
def get_dataset_builder_class(dataset_module: DatasetModule, dataset_name: str | None = None) -> Type[DatasetBuilder]: ...
def files_to_hash(file_paths: List[str]) -> str:
    """
    Convert a list of scripts or text files provided in file_paths into a hashed filename in a repeatable way.
    """
def increase_load_count(name: str, resource_type: str):
    """Update the download count of a dataset or metric."""
def infer_module_for_data_files_list(data_files_list: DataFilesList, download_config: DownloadConfig | None = None) -> Tuple[str, str] | None:
    '''Infer module (and builder kwargs) from list of data files.

    It picks the module based on the most common file extension.
    In case of a draw ".parquet" is the favorite, and then alphabetical order.

    Args:
        data_files_list (DataFilesList): List of data files.
        download_config (bool or str, optional): mainly use use_auth_token or storage_options to support different platforms and auth types.

    Returns:
        tuple[str, dict[str, Any]]: Tuple with
            - inferred module name
            - dict of builder kwargs
    '''
def infer_module_for_data_files_list_in_archives(data_files_list: DataFilesList, download_config: DownloadConfig | None = None) -> Tuple[str, str] | None:
    """Infer module (and builder kwargs) from list of archive data files.

    Args:
        data_files_list (DataFilesList): List of data files.
        download_config (bool or str, optional): mainly use use_auth_token or storage_options to support different platforms and auth types.

    Returns:
        tuple[str, dict[str, Any]]: Tuple with
            - inferred module name
            - dict of builder kwargs
    """
def infer_module_for_data_files(data_files: DataFilesDict, path: str | None = None, download_config: DownloadConfig | None = None) -> Tuple[str | None, Dict[str, Any]]:
    """Infer module (and builder kwargs) from data files. Raise if module names for different splits don't match.

    Args:
        data_files (DataFilesDict): List of data files.
        path (str, optional): Dataset name or path.
        DownloadConfig (bool or str, optional): for authenticate on the Hugging Face Hub for private remote files.

    Returns:
        tuple[str, dict[str, Any]]: Tuple with
            - inferred module name
            - builder kwargs
    """
def update_hash_with_config_parameters(hash: str, config_parameters: dict) -> str:
    """
    Used to update hash of packaged modules which is used for creating unique cache directories to reflect
    different config parameters which are passed in metadata from readme.
    """
def create_builder_configs_from_metadata_configs(module_path: str, metadata_configs: MetadataConfigs, supports_metadata: bool, base_path: str | None = None, default_builder_kwargs: Dict[str, Any] = None, download_config: DownloadConfig | None = None) -> Tuple[List[BuilderConfig], str]: ...

@dataclass
class BuilderConfigsParameters:
    """Dataclass containing objects related to creation of builder configurations from yaml's metadata content.

    Attributes:
        metadata_configs (`MetadataConfigs`, *optional*):
            Configs parsed from yaml's metadata.
        builder_configs (`list[BuilderConfig]`, *optional*):
            List of BuilderConfig objects created from metadata_configs above.
        default_config_name (`str`):
            Name of default config taken from yaml's metadata.
    """
    metadata_configs: MetadataConfigs | None = ...
    builder_configs: List[BuilderConfig] | None = ...
    default_config_name: str | None = ...
    def __init__(self, metadata_configs, builder_configs, default_config_name) -> None: ...

@dataclass
class DatasetModule:
    module_path: str
    hash: str
    builder_kwargs: dict
    builder_configs_parameters: BuilderConfigsParameters = ...
    dataset_infos: DatasetInfosDict | None = ...
    def __init__(self, module_path, hash, builder_kwargs, builder_configs_parameters, dataset_infos) -> None: ...

@dataclass
class MetricModule:
    module_path: str
    hash: str
    def __init__(self, module_path, hash) -> None: ...

class _DatasetModuleFactory:
    def get_module(self) -> DatasetModule: ...

class _MetricModuleFactory:
    def get_module(self) -> MetricModule: ...

class GithubMetricModuleFactory(_MetricModuleFactory):
    '''Get the module of a metric. The metric script is downloaded from GitHub.

    <Deprecated version="2.5.0">

    Use the new library 🤗 Evaluate instead: https://huggingface.co/docs/evaluate

    </Deprecated>
    '''
    name: Incomplete
    revision: Incomplete
    download_config: Incomplete
    download_mode: Incomplete
    dynamic_modules_path: Incomplete
    def __init__(self, name: str, revision: str | Version | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, dynamic_modules_path: str | None = None) -> None: ...
    def download_loading_script(self, revision: str | None) -> str: ...
    def get_module(self) -> MetricModule: ...

class LocalMetricModuleFactory(_MetricModuleFactory):
    '''Get the module of a local metric. The metric script is loaded from a local script.

    <Deprecated version="2.5.0">

    Use the new library 🤗 Evaluate instead: https://huggingface.co/docs/evaluate

    </Deprecated>
    '''
    path: Incomplete
    name: Incomplete
    download_config: Incomplete
    download_mode: Incomplete
    dynamic_modules_path: Incomplete
    def __init__(self, path: str, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, dynamic_modules_path: str | None = None) -> None: ...
    def get_module(self) -> MetricModule: ...

class LocalDatasetModuleFactoryWithScript(_DatasetModuleFactory):
    """Get the module of a local dataset. The dataset script is loaded from a local script."""
    path: Incomplete
    name: Incomplete
    download_config: Incomplete
    download_mode: Incomplete
    dynamic_modules_path: Incomplete
    def __init__(self, path: str, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, dynamic_modules_path: str | None = None) -> None: ...
    def get_module(self) -> DatasetModule: ...

class LocalDatasetModuleFactoryWithoutScript(_DatasetModuleFactory):
    """Get the module of a dataset loaded from the user's data files. The dataset builder module to use is inferred
    from the data files extensions."""
    path: Incomplete
    name: Incomplete
    data_files: Incomplete
    data_dir: Incomplete
    download_mode: Incomplete
    def __init__(self, path: str, data_dir: str | None = None, data_files: str | List | Dict | None = None, download_mode: DownloadMode | str | None = None) -> None: ...
    def get_module(self) -> DatasetModule: ...

class PackagedDatasetModuleFactory(_DatasetModuleFactory):
    """Get the dataset builder module from the ones that are packaged with the library: csv, json, etc."""
    name: Incomplete
    data_files: Incomplete
    data_dir: Incomplete
    download_config: Incomplete
    download_mode: Incomplete
    def __init__(self, name: str, data_dir: str | None = None, data_files: str | List | Dict | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None) -> None: ...
    def get_module(self) -> DatasetModule: ...

class HubDatasetModuleFactoryWithoutScript(_DatasetModuleFactory):
    """
    Get the module of a dataset loaded from data files of a dataset repository.
    The dataset builder module to use is inferred from the data files extensions.
    """
    name: Incomplete
    revision: Incomplete
    data_files: Incomplete
    data_dir: Incomplete
    download_config: Incomplete
    download_mode: Incomplete
    def __init__(self, name: str, revision: str | Version | None = None, data_dir: str | None = None, data_files: str | List | Dict | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None) -> None: ...
    def get_module(self) -> DatasetModule: ...

class HubDatasetModuleFactoryWithScript(_DatasetModuleFactory):
    """
    Get the module of a dataset from a dataset repository.
    The dataset script comes from the script inside the dataset repository.
    """
    name: Incomplete
    revision: Incomplete
    download_config: Incomplete
    download_mode: Incomplete
    dynamic_modules_path: Incomplete
    def __init__(self, name: str, revision: str | Version | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, dynamic_modules_path: str | None = None) -> None: ...
    def download_loading_script(self) -> str: ...
    def download_dataset_infos_file(self) -> str: ...
    def download_dataset_readme_file(self) -> str: ...
    def get_module(self) -> DatasetModule: ...

class CachedDatasetModuleFactory(_DatasetModuleFactory):
    """
    Get the module of a dataset that has been loaded once already and cached.
    The script that is loaded from the cache is the most recent one with a matching name.
    """
    name: Incomplete
    dynamic_modules_path: Incomplete
    def __init__(self, name: str, dynamic_modules_path: str | None = None) -> None: ...
    def get_module(self) -> DatasetModule: ...

class CachedMetricModuleFactory(_MetricModuleFactory):
    '''
    Get the module of a metric that has been loaded once already and cached.
    The script that is loaded from the cache is the most recent one with a matching name.

    <Deprecated version="2.5.0">

    Use the new library 🤗 Evaluate instead: https://huggingface.co/docs/evaluate

    </Deprecated>
    '''
    name: Incomplete
    dynamic_modules_path: Incomplete
    def __init__(self, name: str, dynamic_modules_path: str | None = None) -> None: ...
    def get_module(self) -> MetricModule: ...

def dataset_module_factory(path: str, revision: str | Version | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, dynamic_modules_path: str | None = None, data_dir: str | None = None, data_files: Dict | List | str | DataFilesDict | None = None, **download_kwargs) -> DatasetModule:
    '''
    Download/extract/cache a dataset module.

    Dataset codes are cached inside the dynamic modules cache to allow easy import (avoid ugly sys.path tweaks).

    Args:

        path (str): Path or name of the dataset.
            Depending on ``path``, the dataset builder that is used comes from a generic dataset script (JSON, CSV, Parquet, text etc.) or from the dataset script (a python file) inside the dataset directory.

            For local datasets:

            - if ``path`` is a local directory (containing data files only)
              -> load a generic dataset builder (csv, json, text etc.) based on the content of the directory
              e.g. ``\'./path/to/directory/with/my/csv/data\'``.
            - if ``path`` is a local dataset script or a directory containing a local dataset script (if the script has the same name as the directory):
              -> load the dataset builder from the dataset script
              e.g. ``\'./dataset/squad\'`` or ``\'./dataset/squad/squad.py\'``.

            For datasets on the Hugging Face Hub (list all available datasets with ``huggingface_hub.list_datasets()``)

            - if ``path`` is a dataset repository on the HF hub (containing data files only)
              -> load a generic dataset builder (csv, text etc.) based on the content of the repository
              e.g. ``\'username/dataset_name\'``, a dataset repository on the HF hub containing your data files.
            - if ``path`` is a dataset repository on the HF hub with a dataset script (if the script has the same name as the directory)
              -> load the dataset builder from the dataset script in the dataset repository
              e.g. ``glue``, ``squad``, ``\'username/dataset_name\'``, a dataset repository on the HF hub containing a dataset script `\'dataset_name.py\'`.

        revision (:class:`~utils.Version` or :obj:`str`, optional): Version of the dataset script to load.
            As datasets have their own git repository on the Datasets Hub, the default version "main" corresponds to their "main" branch.
            You can specify a different version than the default "main" by using a commit SHA or a git tag of the dataset repository.
        download_config (:class:`DownloadConfig`, optional): Specific download configuration parameters.
        download_mode (:class:`DownloadMode` or :obj:`str`, default ``REUSE_DATASET_IF_EXISTS``): Download/generate mode.
        dynamic_modules_path (Optional str, defaults to HF_MODULES_CACHE / "datasets_modules", i.e. ~/.cache/huggingface/modules/datasets_modules):
            Optional path to the directory in which the dynamic modules are saved. It must have been initialized with :obj:`init_dynamic_modules`.
            By default, the datasets and metrics are stored inside the `datasets_modules` module.
        data_dir (:obj:`str`, optional): Directory with the data files. Used only if `data_files` is not specified,
            in which case it\'s equal to pass `os.path.join(data_dir, "**")` as `data_files`.
        data_files (:obj:`Union[Dict, List, str]`, optional): Defining the data_files of the dataset configuration.
        **download_kwargs (additional keyword arguments): optional attributes for DownloadConfig() which will override
            the attributes in download_config if supplied.

    Returns:
        DatasetModule
    '''
def metric_module_factory(path: str, revision: str | Version | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, dynamic_modules_path: str | None = None, **download_kwargs) -> MetricModule:
    '''
    Download/extract/cache a metric module.

    <Deprecated version="2.5.0">

    Use the new library 🤗 Evaluate instead: https://huggingface.co/docs/evaluate

    </Deprecated>

    Metrics codes are cached inside the dynamic modules cache to allow easy import (avoid ugly sys.path tweaks).

    Args:

        path (str): Path or name of the metric script.

            - if ``path`` is a local metric script or a directory containing a local metric script (if the script has the same name as the directory):
              -> load the module from the metric script
              e.g. ``\'./metrics/accuracy\'`` or ``\'./metrics/accuracy/accuracy.py\'``.
            - if ``path`` is a metric on the Hugging Face Hub (ex: `glue`, `squad`)
              -> load the module from the metric script in the GitHub repository at huggingface/datasets
              e.g. ``\'accuracy\'`` or ``\'rouge\'``.

        revision (Optional ``Union[str, datasets.Version]``):
            If specified, the module will be loaded from the datasets repository at this version.
            By default:
            - it is set to the local version of the lib.
            - it will also try to load it from the main branch if it\'s not available at the local version of the lib.
            Specifying a version that is different from your local version of the lib might cause compatibility issues.
        download_config (:class:`DownloadConfig`, optional): Specific download configuration parameters.
        download_mode (:class:`DownloadMode` or :obj:`str`, default ``REUSE_DATASET_IF_EXISTS``): Download/generate mode.
        dynamic_modules_path (Optional str, defaults to HF_MODULES_CACHE / "datasets_modules", i.e. ~/.cache/huggingface/modules/datasets_modules):
            Optional path to the directory in which the dynamic modules are saved. It must have been initialized with :obj:`init_dynamic_modules`.
            By default, the datasets and metrics are stored inside the `datasets_modules` module.
        **download_kwargs (additional keyword arguments): optional attributes for DownloadConfig() which will override
            the attributes in download_config if supplied.

    Returns:
        MetricModule
    '''
def load_metric(path: str, config_name: str | None = None, process_id: int = 0, num_process: int = 1, cache_dir: str | None = None, experiment_id: str | None = None, keep_in_memory: bool = False, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, revision: str | Version | None = None, **metric_init_kwargs) -> Metric:
    '''Load a `datasets.Metric`.

    <Deprecated version="2.5.0">

    Use `evaluate.load` instead, from the new library 🤗 Evaluate: https://huggingface.co/docs/evaluate

    </Deprecated>

    Args:

        path (``str``):
            path to the metric processing script with the metric builder. Can be either:
                - a local path to processing script or the directory containing the script (if the script has the same name as the directory),
                    e.g. ``\'./metrics/rouge\'`` or ``\'./metrics/rogue/rouge.py\'``
                - a metric identifier on the HuggingFace datasets repo (list all available metrics with ``datasets.list_metrics()``)
                    e.g. ``\'rouge\'`` or ``\'bleu\'``
        config_name (:obj:`str`, optional): selecting a configuration for the metric (e.g. the GLUE metric has a configuration for each subset)
        process_id (:obj:`int`, optional): for distributed evaluation: id of the process
        num_process (:obj:`int`, optional): for distributed evaluation: total number of processes
        cache_dir (Optional str): path to store the temporary predictions and references (default to `~/.cache/huggingface/metrics/`)
        experiment_id (``str``): A specific experiment id. This is used if several distributed evaluations share the same file system.
            This is useful to compute metrics in distributed setups (in particular non-additive metrics like F1).
        keep_in_memory (bool): Whether to store the temporary results in memory (defaults to False)
        download_config (Optional ``datasets.DownloadConfig``: specific download configuration parameters.
        download_mode (:class:`DownloadMode` or :obj:`str`, default ``REUSE_DATASET_IF_EXISTS``): Download/generate mode.
        revision (Optional ``Union[str, datasets.Version]``): if specified, the module will be loaded from the datasets repository
            at this version. By default, it is set to the local version of the lib. Specifying a version that is different from
            your local version of the lib might cause compatibility issues.

    Returns:
        `datasets.Metric`

    Example:

    ```py
    >>> from datasets import load_metric
    >>> accuracy = load_metric(\'accuracy\')
    >>> accuracy.compute(references=[1, 0], predictions=[1, 1])
    {\'accuracy\': 0.5}
    ```
    '''
def load_dataset_builder(path: str, name: str | None = None, data_dir: str | None = None, data_files: str | Sequence[str] | Mapping[str, str | Sequence[str]] | None = None, cache_dir: str | None = None, features: Features | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, revision: str | Version | None = None, token: bool | str | None = None, use_auth_token: str = 'deprecated', storage_options: Dict | None = None, **config_kwargs) -> DatasetBuilder:
    '''Load a dataset builder from the Hugging Face Hub, or a local dataset. A dataset builder can be used to inspect general information that is required to build a dataset (cache directory, config, dataset info, etc.)
    without downloading the dataset itself.

    You can find the list of datasets on the [Hub](https://huggingface.co/datasets) or with [`huggingface_hub.list_datasets`].

    A dataset is a directory that contains:

    - some data files in generic formats (JSON, CSV, Parquet, text, etc.)
    - and optionally a dataset script, if it requires some code to read the data files. This is used to load any kind of formats or structures.

    Note that dataset scripts can also download and read data files from anywhere - in case your data files already exist online.

    Args:

        path (`str`):
            Path or name of the dataset.
            Depending on `path`, the dataset builder that is used comes from a generic dataset script (JSON, CSV, Parquet, text etc.) or from the dataset script (a python file) inside the dataset directory.

            For local datasets:

            - if `path` is a local directory (containing data files only)
              -> load a generic dataset builder (csv, json, text etc.) based on the content of the directory
              e.g. `\'./path/to/directory/with/my/csv/data\'`.
            - if `path` is a local dataset script or a directory containing a local dataset script (if the script has the same name as the directory)
              -> load the dataset builder from the dataset script
              e.g. `\'./dataset/squad\'` or `\'./dataset/squad/squad.py\'`.

            For datasets on the Hugging Face Hub (list all available datasets with [`huggingface_hub.list_datasets`])

            - if `path` is a dataset repository on the HF hub (containing data files only)
              -> load a generic dataset builder (csv, text etc.) based on the content of the repository
              e.g. `\'username/dataset_name\'`, a dataset repository on the HF hub containing your data files.
            - if `path` is a dataset repository on the HF hub with a dataset script (if the script has the same name as the directory)
              -> load the dataset builder from the dataset script in the dataset repository
              e.g. `glue`, `squad`, `\'username/dataset_name\'`, a dataset repository on the HF hub containing a dataset script `\'dataset_name.py\'`.

        name (`str`, *optional*):
            Defining the name of the dataset configuration.
        data_dir (`str`, *optional*):
            Defining the `data_dir` of the dataset configuration. If specified for the generic builders (csv, text etc.) or the Hub datasets and `data_files` is `None`,
            the behavior is equal to passing `os.path.join(data_dir, **)` as `data_files` to reference all the files in a directory.
        data_files (`str` or `Sequence` or `Mapping`, *optional*):
            Path(s) to source data file(s).
        cache_dir (`str`, *optional*):
            Directory to read/write data. Defaults to `"~/.cache/huggingface/datasets"`.
        features ([`Features`], *optional*):
            Set the features type to use for this dataset.
        download_config ([`DownloadConfig`], *optional*):
            Specific download configuration parameters.
        download_mode ([`DownloadMode`] or `str`, defaults to `REUSE_DATASET_IF_EXISTS`):
            Download/generate mode.
        revision ([`Version`] or `str`, *optional*):
            Version of the dataset script to load.
            As datasets have their own git repository on the Datasets Hub, the default version "main" corresponds to their "main" branch.
            You can specify a different version than the default "main" by using a commit SHA or a git tag of the dataset repository.
        token (`str` or `bool`, *optional*):
            Optional string or boolean to use as Bearer token for remote files on the Datasets Hub.
            If `True`, or not specified, will get token from `"~/.huggingface"`.
        use_auth_token (`str` or `bool`, *optional*):
            Optional string or boolean to use as Bearer token for remote files on the Datasets Hub.
            If `True`, or not specified, will get token from `"~/.huggingface"`.

            <Deprecated version="2.14.0">

            `use_auth_token` was deprecated in favor of `token` in version 2.14.0 and will be removed in 3.0.0.

            </Deprecated>
        storage_options (`dict`, *optional*, defaults to `None`):
            **Experimental**. Key/value pairs to be passed on to the dataset file-system backend, if any.

            <Added version="2.11.0"/>
        **config_kwargs (additional keyword arguments):
            Keyword arguments to be passed to the [`BuilderConfig`]
            and used in the [`DatasetBuilder`].

    Returns:
        [`DatasetBuilder`]

    Example:

    ```py
    >>> from datasets import load_dataset_builder
    >>> ds_builder = load_dataset_builder(\'rotten_tomatoes\')
    >>> ds_builder.info.features
    {\'label\': ClassLabel(num_classes=2, names=[\'neg\', \'pos\'], id=None),
     \'text\': Value(dtype=\'string\', id=None)}
    ```
    '''
def load_dataset(path: str, name: str | None = None, data_dir: str | None = None, data_files: str | Sequence[str] | Mapping[str, str | Sequence[str]] | None = None, split: str | Split | None = None, cache_dir: str | None = None, features: Features | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, verification_mode: VerificationMode | str | None = None, ignore_verifications: str = 'deprecated', keep_in_memory: bool | None = None, save_infos: bool = False, revision: str | Version | None = None, token: bool | str | None = None, use_auth_token: str = 'deprecated', task: str = 'deprecated', streaming: bool = False, num_proc: int | None = None, storage_options: Dict | None = None, **config_kwargs) -> DatasetDict | Dataset | IterableDatasetDict | IterableDataset:
    '''Load a dataset from the Hugging Face Hub, or a local dataset.

    You can find the list of datasets on the [Hub](https://huggingface.co/datasets) or with [`huggingface_hub.list_datasets`].

    A dataset is a directory that contains:

    - some data files in generic formats (JSON, CSV, Parquet, text, etc.).
    - and optionally a dataset script, if it requires some code to read the data files. This is used to load any kind of formats or structures.

    Note that dataset scripts can also download and read data files from anywhere - in case your data files already exist online.

    This function does the following under the hood:

        1. Download and import in the library the dataset script from `path` if it\'s not already cached inside the library.

            If the dataset has no dataset script, then a generic dataset script is imported instead (JSON, CSV, Parquet, text, etc.)

            Dataset scripts are small python scripts that define dataset builders. They define the citation, info and format of the dataset,
            contain the path or URL to the original data files and the code to load examples from the original data files.

            You can find the complete list of datasets in the Datasets [Hub](https://huggingface.co/datasets).

        2. Run the dataset script which will:

            * Download the dataset file from the original URL (see the script) if it\'s not already available locally or cached.
            * Process and cache the dataset in typed Arrow tables for caching.

                Arrow table are arbitrarily long, typed tables which can store nested objects and be mapped to numpy/pandas/python generic types.
                They can be directly accessed from disk, loaded in RAM or even streamed over the web.

        3. Return a dataset built from the requested splits in `split` (default: all).

    It also allows to load a dataset from a local directory or a dataset repository on the Hugging Face Hub without dataset script.
    In this case, it automatically loads all the data files from the directory or the dataset repository.

    Args:

        path (`str`):
            Path or name of the dataset.
            Depending on `path`, the dataset builder that is used comes from a generic dataset script (JSON, CSV, Parquet, text etc.) or from the dataset script (a python file) inside the dataset directory.

            For local datasets:

            - if `path` is a local directory (containing data files only)
              -> load a generic dataset builder (csv, json, text etc.) based on the content of the directory
              e.g. `\'./path/to/directory/with/my/csv/data\'`.
            - if `path` is a local dataset script or a directory containing a local dataset script (if the script has the same name as the directory)
              -> load the dataset builder from the dataset script
              e.g. `\'./dataset/squad\'` or `\'./dataset/squad/squad.py\'`.

            For datasets on the Hugging Face Hub (list all available datasets with [`huggingface_hub.list_datasets`])

            - if `path` is a dataset repository on the HF hub (containing data files only)
              -> load a generic dataset builder (csv, text etc.) based on the content of the repository
              e.g. `\'username/dataset_name\'`, a dataset repository on the HF hub containing your data files.
            - if `path` is a dataset repository on the HF hub with a dataset script (if the script has the same name as the directory)
              -> load the dataset builder from the dataset script in the dataset repository
              e.g. `glue`, `squad`, `\'username/dataset_name\'`, a dataset repository on the HF hub containing a dataset script `\'dataset_name.py\'`.

        name (`str`, *optional*):
            Defining the name of the dataset configuration.
        data_dir (`str`, *optional*):
            Defining the `data_dir` of the dataset configuration. If specified for the generic builders (csv, text etc.) or the Hub datasets and `data_files` is `None`,
            the behavior is equal to passing `os.path.join(data_dir, **)` as `data_files` to reference all the files in a directory.
        data_files (`str` or `Sequence` or `Mapping`, *optional*):
            Path(s) to source data file(s).
        split (`Split` or `str`):
            Which split of the data to load.
            If `None`, will return a `dict` with all splits (typically `datasets.Split.TRAIN` and `datasets.Split.TEST`).
            If given, will return a single Dataset.
            Splits can be combined and specified like in tensorflow-datasets.
        cache_dir (`str`, *optional*):
            Directory to read/write data. Defaults to `"~/.cache/huggingface/datasets"`.
        features (`Features`, *optional*):
            Set the features type to use for this dataset.
        download_config ([`DownloadConfig`], *optional*):
            Specific download configuration parameters.
        download_mode ([`DownloadMode`] or `str`, defaults to `REUSE_DATASET_IF_EXISTS`):
            Download/generate mode.
        verification_mode ([`VerificationMode`] or `str`, defaults to `BASIC_CHECKS`):
            Verification mode determining the checks to run on the downloaded/processed dataset information (checksums/size/splits/...).

            <Added version="2.9.1"/>
        ignore_verifications (`bool`, defaults to `False`):
            Ignore the verifications of the downloaded/processed dataset information (checksums/size/splits/...).

            <Deprecated version="2.9.1">

            `ignore_verifications` was deprecated in version 2.9.1 and will be removed in 3.0.0.
            Please use `verification_mode` instead.

            </Deprecated>
        keep_in_memory (`bool`, defaults to `None`):
            Whether to copy the dataset in-memory. If `None`, the dataset
            will not be copied in-memory unless explicitly enabled by setting `datasets.config.IN_MEMORY_MAX_SIZE` to
            nonzero. See more details in the [improve performance](../cache#improve-performance) section.
        save_infos (`bool`, defaults to `False`):
            Save the dataset information (checksums/size/splits/...).
        revision ([`Version`] or `str`, *optional*):
            Version of the dataset script to load.
            As datasets have their own git repository on the Datasets Hub, the default version "main" corresponds to their "main" branch.
            You can specify a different version than the default "main" by using a commit SHA or a git tag of the dataset repository.
        token (`str` or `bool`, *optional*):
            Optional string or boolean to use as Bearer token for remote files on the Datasets Hub.
            If `True`, or not specified, will get token from `"~/.huggingface"`.
        use_auth_token (`str` or `bool`, *optional*):
            Optional string or boolean to use as Bearer token for remote files on the Datasets Hub.
            If `True`, or not specified, will get token from `"~/.huggingface"`.

            <Deprecated version="2.14.0">

            `use_auth_token` was deprecated in favor of `token` in version 2.14.0 and will be removed in 3.0.0.

            </Deprecated>
        task (`str`):
            The task to prepare the dataset for during training and evaluation. Casts the dataset\'s [`Features`] to standardized column names and types as detailed in `datasets.tasks`.

            <Deprecated version="2.13.0">

            `task` was deprecated in version 2.13.0 and will be removed in 3.0.0.

            </Deprecated>
        streaming (`bool`, defaults to `False`):
            If set to `True`, don\'t download the data files. Instead, it streams the data progressively while
            iterating on the dataset. An [`IterableDataset`] or [`IterableDatasetDict`] is returned instead in this case.

            Note that streaming works for datasets that use data formats that support being iterated over like txt, csv, jsonl for example.
            Json files may be downloaded completely. Also streaming from remote zip or gzip files is supported but other compressed formats
            like rar and xz are not yet supported. The tgz format doesn\'t allow streaming.
        num_proc (`int`, *optional*, defaults to `None`):
            Number of processes when downloading and generating the dataset locally.
            Multiprocessing is disabled by default.

            <Added version="2.7.0"/>
        storage_options (`dict`, *optional*, defaults to `None`):
            **Experimental**. Key/value pairs to be passed on to the dataset file-system backend, if any.

            <Added version="2.11.0"/>
        **config_kwargs (additional keyword arguments):
            Keyword arguments to be passed to the `BuilderConfig`
            and used in the [`DatasetBuilder`].

    Returns:
        [`Dataset`] or [`DatasetDict`]:
        - if `split` is not `None`: the dataset requested,
        - if `split` is `None`, a [`~datasets.DatasetDict`] with each split.

        or [`IterableDataset`] or [`IterableDatasetDict`]: if `streaming=True`

        - if `split` is not `None`, the dataset is requested
        - if `split` is `None`, a [`~datasets.streaming.IterableDatasetDict`] with each split.

    Example:

    Load a dataset from the Hugging Face Hub:

    ```py
    >>> from datasets import load_dataset
    >>> ds = load_dataset(\'rotten_tomatoes\', split=\'train\')

    # Map data files to splits
    >>> data_files = {\'train\': \'train.csv\', \'test\': \'test.csv\'}
    >>> ds = load_dataset(\'namespace/your_dataset_name\', data_files=data_files)
    ```

    Load a local dataset:

    ```py
    # Load a CSV file
    >>> from datasets import load_dataset
    >>> ds = load_dataset(\'csv\', data_files=\'path/to/local/my_dataset.csv\')

    # Load a JSON file
    >>> from datasets import load_dataset
    >>> ds = load_dataset(\'json\', data_files=\'path/to/local/my_dataset.json\')

    # Load from a local loading script
    >>> from datasets import load_dataset
    >>> ds = load_dataset(\'path/to/local/loading_script/loading_script.py\', split=\'train\')
    ```

    Load an [`~datasets.IterableDataset`]:

    ```py
    >>> from datasets import load_dataset
    >>> ds = load_dataset(\'rotten_tomatoes\', split=\'train\', streaming=True)
    ```

    Load an image dataset with the `ImageFolder` dataset builder:

    ```py
    >>> from datasets import load_dataset
    >>> ds = load_dataset(\'imagefolder\', data_dir=\'/path/to/images\', split=\'train\')
    ```
    '''
def load_from_disk(dataset_path: str, fs: str = 'deprecated', keep_in_memory: bool | None = None, storage_options: dict | None = None) -> Dataset | DatasetDict:
    '''
    Loads a dataset that was previously saved using [`~Dataset.save_to_disk`] from a dataset directory, or
    from a filesystem using any implementation of `fsspec.spec.AbstractFileSystem`.

    Args:
        dataset_path (`str`):
            Path (e.g. `"dataset/train"`) or remote URI (e.g.
            `"s3://my-bucket/dataset/train"`) of the [`Dataset`] or [`DatasetDict`] directory where the dataset will be
            loaded from.
        fs (`~filesystems.S3FileSystem` or `fsspec.spec.AbstractFileSystem`, *optional*):
            Instance of the remote filesystem used to download the files from.

            <Deprecated version="2.9.0">

            `fs` was deprecated in version 2.9.0 and will be removed in 3.0.0.
            Please use `storage_options` instead, e.g. `storage_options=fs.storage_options`.

            </Deprecated>

        keep_in_memory (`bool`, defaults to `None`):
            Whether to copy the dataset in-memory. If `None`, the dataset
            will not be copied in-memory unless explicitly enabled by setting `datasets.config.IN_MEMORY_MAX_SIZE` to
            nonzero. See more details in the [improve performance](../cache#improve-performance) section.

        storage_options (`dict`, *optional*):
            Key/value pairs to be passed on to the file-system backend, if any.

            <Added version="2.9.0"/>

    Returns:
        [`Dataset`] or [`DatasetDict`]:
        - If `dataset_path` is a path of a dataset directory: the dataset requested.
        - If `dataset_path` is a path of a dataset dict directory, a [`DatasetDict`] with each split.

    Example:

    ```py
    >>> from datasets import load_from_disk
    >>> ds = load_from_disk(\'path/to/dataset/directory\')
    ```
    '''
