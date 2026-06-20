from .download.download_config import DownloadConfig as DownloadConfig
from .download.download_manager import DownloadMode as DownloadMode
from .download.streaming_download_manager import StreamingDownloadManager as StreamingDownloadManager
from .info import DatasetInfo as DatasetInfo
from .load import dataset_module_factory as dataset_module_factory, get_dataset_builder_class as get_dataset_builder_class, import_main_class as import_main_class, load_dataset_builder as load_dataset_builder, metric_module_factory as metric_module_factory
from .utils.deprecation_utils import deprecated as deprecated
from .utils.file_utils import relative_to_absolute_path as relative_to_absolute_path
from .utils.logging import get_logger as get_logger
from .utils.version import Version as Version
from _typeshed import Incomplete
from typing import Dict, List, Mapping, Sequence

logger: Incomplete

class SplitsNotFoundError(ValueError): ...

def list_datasets(with_community_datasets: bool = True, with_details: bool = False):
    """List all the datasets scripts available on the Hugging Face Hub.

    Args:
        with_community_datasets (`bool`, *optional*, defaults to `True`):
            Include the community provided datasets.
        with_details (`bool`, *optional*, defaults to `False`):
            Return the full details on the datasets instead of only the short name.

    Example:

    ```py
    >>> from datasets import list_datasets
    >>> list_datasets()
    ['acronym_identification',
     'ade_corpus_v2',
     'adversarial_qa',
     'aeslc',
     'afrikaans_ner_corpus',
     'ag_news',
     ...
    ]
    ```
    """
def list_metrics(with_community_metrics: bool = True, with_details: bool = False):
    '''List all the metrics script available on the Hugging Face Hub.

    <Deprecated version="2.5.0">

    Use `evaluate.list_evaluation_modules` instead, from the new library 🤗 Evaluate: https://huggingface.co/docs/evaluate

    </Deprecated>

    Args:
        with_community_metrics (:obj:`bool`, optional, default ``True``): Include the community provided metrics.
        with_details (:obj:`bool`, optional, default ``False``): Return the full details on the metrics instead of only the short name.

    Example:

    ```py
    >>> from datasets import list_metrics
    >>> list_metrics()
    [\'accuracy\',
     \'bertscore\',
     \'bleu\',
     \'bleurt\',
     \'cer\',
     \'chrf\',
     ...
    ]
    ```
    '''
def inspect_dataset(path: str, local_path: str, download_config: DownloadConfig | None = None, **download_kwargs):
    """
    Allow inspection/modification of a dataset script by copying on local drive at local_path.

    Args:
        path (`str`): Path to the dataset processing script with the dataset builder. Can be either:

            - a local path to processing script or the directory containing the script (if the script has the same name
                as the directory),
                e.g. `'./dataset/squad'` or `'./dataset/squad/squad.py'`.
            - a dataset identifier on the Hugging Face Hub (list all available datasets and ids with [`list_datasets`])
                e.g. `'squad'`, `'glue'` or `'openai/webtext'`.
        local_path (`str`):
            Path to the local folder to copy the dataset script to.
        download_config ([`DownloadConfig`], *optional*):
            Specific download configuration parameters.
        **download_kwargs (additional keyword arguments):
            Optional arguments for [`DownloadConfig`] which will override
            the attributes of `download_config` if supplied.
    """
def inspect_metric(path: str, local_path: str, download_config: DownloadConfig | None = None, **download_kwargs):
    '''
    Allow inspection/modification of a metric script by copying it on local drive at local_path.

    <Deprecated version="2.5.0">

    Use `evaluate.inspect_evaluation_module` instead, from the new library 🤗 Evaluate instead: https://huggingface.co/docs/evaluate

    </Deprecated>

    Args:
        path (``str``): path to the dataset processing script with the dataset builder. Can be either:

            - a local path to processing script or the directory containing the script (if the script has the same name as the directory),
                e.g. ``\'./dataset/squad\'`` or ``\'./dataset/squad/squad.py\'``
            - a dataset identifier on the Hugging Face Hub (list all available datasets and ids with ``datasets.list_datasets()``)
                e.g. ``\'squad\'``, ``\'glue\'`` or ``\'openai/webtext\'``
        local_path (``str``): path to the local folder to copy the datset script to.
        download_config (Optional ``datasets.DownloadConfig``): specific download configuration parameters.
        **download_kwargs (additional keyword arguments): optional attributes for DownloadConfig() which will override the attributes in download_config if supplied.
    '''
def get_dataset_infos(path: str, data_files: Dict | List | str | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, revision: str | Version | None = None, token: bool | str | None = None, use_auth_token: str = 'deprecated', **config_kwargs):
    '''Get the meta information about a dataset, returned as a dict mapping config name to DatasetInfoDict.

    Args:
        path (`str`): path to the dataset processing script with the dataset builder. Can be either:

            - a local path to processing script or the directory containing the script (if the script has the same name as the directory),
                e.g. `\'./dataset/squad\'` or `\'./dataset/squad/squad.py\'`
            - a dataset identifier on the Hugging Face Hub (list all available datasets and ids with [`datasets.list_datasets`])
                e.g. `\'squad\'`, `\'glue\'` or``\'openai/webtext\'`
        revision (`Union[str, datasets.Version]`, *optional*):
            If specified, the dataset module will be loaded from the datasets repository at this version.
            By default:
            - it is set to the local version of the lib.
            - it will also try to load it from the main branch if it\'s not available at the local version of the lib.
            Specifying a version that is different from your local version of the lib might cause compatibility issues.
        download_config ([`DownloadConfig`], *optional*):
            Specific download configuration parameters.
        download_mode ([`DownloadMode`] or `str`, defaults to `REUSE_DATASET_IF_EXISTS`):
            Download/generate mode.
        data_files (`Union[Dict, List, str]`, *optional*):
            Defining the data_files of the dataset configuration.
        token (`str` or `bool`, *optional*):
            Optional string or boolean to use as Bearer token for remote files on the Datasets Hub.
            If `True`, or not specified, will get token from `"~/.huggingface"`.
        use_auth_token (`str` or `bool`, *optional*):
            Optional string or boolean to use as Bearer token for remote files on the Datasets Hub.
            If `True`, or not specified, will get token from `"~/.huggingface"`.

            <Deprecated version="2.14.0">

            `use_auth_token` was deprecated in favor of `token` in version 2.14.0 and will be removed in 3.0.0.

            </Deprecated>

        **config_kwargs (additional keyword arguments):
            Optional attributes for builder class which will override the attributes if supplied.

    Example:

    ```py
    >>> from datasets import get_dataset_infos
    >>> get_dataset_infos(\'rotten_tomatoes\')
    {\'default\': DatasetInfo(description="Movie Review Dataset.
This is a dataset of containing 5,331 positive and 5,331 negative processed
sentences from Rotten Tomatoes movie reviews...), ...}
    ```
    '''
def get_dataset_config_names(path: str, revision: str | Version | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, dynamic_modules_path: str | None = None, data_files: Dict | List | str | None = None, **download_kwargs):
    '''Get the list of available config names for a particular dataset.

    Args:
        path (`str`): path to the dataset processing script with the dataset builder. Can be either:

            - a local path to processing script or the directory containing the script (if the script has the same name as the directory),
                e.g. `\'./dataset/squad\'` or `\'./dataset/squad/squad.py\'`
            - a dataset identifier on the Hugging Face Hub (list all available datasets and ids with [`datasets.list_datasets`])
                e.g. `\'squad\'`, `\'glue\'` or `\'openai/webtext\'`
        revision (`Union[str, datasets.Version]`, *optional*):
            If specified, the dataset module will be loaded from the datasets repository at this version.
            By default:
            - it is set to the local version of the lib.
            - it will also try to load it from the main branch if it\'s not available at the local version of the lib.
            Specifying a version that is different from your local version of the lib might cause compatibility issues.
        download_config ([`DownloadConfig`], *optional*):
            Specific download configuration parameters.
        download_mode ([`DownloadMode`] or `str`, defaults to `REUSE_DATASET_IF_EXISTS`):
            Download/generate mode.
        dynamic_modules_path (`str`, defaults to `~/.cache/huggingface/modules/datasets_modules`):
            Optional path to the directory in which the dynamic modules are saved. It must have been initialized with `init_dynamic_modules`.
            By default the datasets and metrics are stored inside the `datasets_modules` module.
        data_files (`Union[Dict, List, str]`, *optional*):
            Defining the data_files of the dataset configuration.
        **download_kwargs (additional keyword arguments):
            Optional attributes for [`DownloadConfig`] which will override the attributes in `download_config` if supplied,
            for example `token`.

    Example:

    ```py
    >>> from datasets import get_dataset_config_names
    >>> get_dataset_config_names("glue")
    [\'cola\',
     \'sst2\',
     \'mrpc\',
     \'qqp\',
     \'stsb\',
     \'mnli\',
     \'mnli_mismatched\',
     \'mnli_matched\',
     \'qnli\',
     \'rte\',
     \'wnli\',
     \'ax\']
    ```
    '''
def get_dataset_config_info(path: str, config_name: str | None = None, data_files: str | Sequence[str] | Mapping[str, str | Sequence[str]] | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, revision: str | Version | None = None, token: bool | str | None = None, use_auth_token: str = 'deprecated', **config_kwargs) -> DatasetInfo:
    '''Get the meta information (DatasetInfo) about a dataset for a particular config

    Args:
        path (``str``): path to the dataset processing script with the dataset builder. Can be either:

            - a local path to processing script or the directory containing the script (if the script has the same name as the directory),
                e.g. ``\'./dataset/squad\'`` or ``\'./dataset/squad/squad.py\'``
            - a dataset identifier on the Hugging Face Hub (list all available datasets and ids with ``datasets.list_datasets()``)
                e.g. ``\'squad\'``, ``\'glue\'`` or ``\'openai/webtext\'``
        config_name (:obj:`str`, optional): Defining the name of the dataset configuration.
        data_files (:obj:`str` or :obj:`Sequence` or :obj:`Mapping`, optional): Path(s) to source data file(s).
        download_config (:class:`~download.DownloadConfig`, optional): Specific download configuration parameters.
        download_mode (:class:`DownloadMode` or :obj:`str`, default ``REUSE_DATASET_IF_EXISTS``): Download/generate mode.
        revision (:class:`~utils.Version` or :obj:`str`, optional): Version of the dataset script to load.
            As datasets have their own git repository on the Datasets Hub, the default version "main" corresponds to their "main" branch.
            You can specify a different version than the default "main" by using a commit SHA or a git tag of the dataset repository.
        token (``str`` or :obj:`bool`, optional): Optional string or boolean to use as Bearer token for remote files on the Datasets Hub.
            If True, or not specified, will get token from `"~/.huggingface"`.
        use_auth_token (``str`` or :obj:`bool`, optional): Optional string or boolean to use as Bearer token for remote files on the Datasets Hub.
            If True, or not specified, will get token from `"~/.huggingface"`.

            <Deprecated version="2.14.0">

            `use_auth_token` was deprecated in favor of `token` in version 2.14.0 and will be removed in 3.0.0.

            </Deprecated>

        **config_kwargs (additional keyword arguments): optional attributes for builder class which will override the attributes if supplied.

    '''
def get_dataset_split_names(path: str, config_name: str | None = None, data_files: str | Sequence[str] | Mapping[str, str | Sequence[str]] | None = None, download_config: DownloadConfig | None = None, download_mode: DownloadMode | str | None = None, revision: str | Version | None = None, token: bool | str | None = None, use_auth_token: str = 'deprecated', **config_kwargs):
    '''Get the list of available splits for a particular config and dataset.

    Args:
        path (`str`): path to the dataset processing script with the dataset builder. Can be either:

            - a local path to processing script or the directory containing the script (if the script has the same name as the directory),
                e.g. `\'./dataset/squad\'` or `\'./dataset/squad/squad.py\'`
            - a dataset identifier on the Hugging Face Hub (list all available datasets and ids with [`datasets.list_datasets`])
                e.g. `\'squad\'`, `\'glue\'` or `\'openai/webtext\'`
        config_name (`str`, *optional*):
            Defining the name of the dataset configuration.
        data_files (`str` or `Sequence` or `Mapping`, *optional*):
            Path(s) to source data file(s).
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

        **config_kwargs (additional keyword arguments):
            Optional attributes for builder class which will override the attributes if supplied.

    Example:

    ```py
    >>> from datasets import get_dataset_split_names
    >>> get_dataset_split_names(\'rotten_tomatoes\')
    [\'train\', \'validation\', \'test\']
    ```
    '''
