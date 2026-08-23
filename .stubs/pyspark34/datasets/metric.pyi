from . import config as config
from .arrow_dataset import Dataset as Dataset
from .arrow_reader import ArrowReader as ArrowReader
from .arrow_writer import ArrowWriter as ArrowWriter
from .download.download_config import DownloadConfig as DownloadConfig
from .download.download_manager import DownloadManager as DownloadManager
from .features import Features as Features
from .info import DatasetInfo as DatasetInfo, MetricInfo as MetricInfo
from .naming import camelcase_to_snakecase as camelcase_to_snakecase
from .utils.deprecation_utils import deprecated as deprecated
from .utils.filelock import BaseFileLock as BaseFileLock, FileLock as FileLock, Timeout as Timeout
from .utils.logging import get_logger as get_logger
from .utils.py_utils import copyfunc as copyfunc, temp_seed as temp_seed
from _typeshed import Incomplete
from typing import List

logger: Incomplete

class FileFreeLock(BaseFileLock):
    """Thread lock until a file **cannot** be locked"""
    filelock: Incomplete
    def __init__(self, lock_file, *args, **kwargs) -> None: ...

def summarize_if_long_list(obj): ...

class MetricInfoMixin:
    '''This base class exposes some attributes of MetricInfo
    at the base level of the Metric for easy access.

    <Deprecated version="2.5.0">

    Use the new library 🤗 Evaluate instead: https://huggingface.co/docs/evaluate

    </Deprecated>

    '''
    def __init__(self, info: MetricInfo) -> None: ...
    @property
    def info(self):
        """:class:`datasets.MetricInfo` object containing all the metadata in the metric."""
    @property
    def name(self) -> str: ...
    @property
    def experiment_id(self) -> str | None: ...
    @property
    def description(self) -> str: ...
    @property
    def citation(self) -> str: ...
    @property
    def features(self) -> Features: ...
    @property
    def inputs_description(self) -> str: ...
    @property
    def homepage(self) -> str | None: ...
    @property
    def license(self) -> str: ...
    @property
    def codebase_urls(self) -> List[str] | None: ...
    @property
    def reference_urls(self) -> List[str] | None: ...
    @property
    def streamable(self) -> bool: ...
    @property
    def format(self) -> str | None: ...

class Metric(MetricInfoMixin):
    '''A Metric is the base class and common API for all metrics.

    <Deprecated version="2.5.0">

    Use the new library 🤗 Evaluate instead: https://huggingface.co/docs/evaluate

    </Deprecated>

    Args:
        config_name (``str``): This is used to define a hash specific to a metrics computation script and prevents the metric\'s data
            to be overridden when the metric loading script is modified.
        keep_in_memory (:obj:`bool`): keep all predictions and references in memory. Not possible in distributed settings.
        cache_dir (``str``): Path to a directory in which temporary prediction/references data will be stored.
            The data directory should be located on a shared file-system in distributed setups.
        num_process (``int``): specify the total number of nodes in a distributed settings.
            This is useful to compute metrics in distributed setups (in particular non-additive metrics like F1).
        process_id (``int``): specify the id of the current process in a distributed setup (between 0 and num_process-1)
            This is useful to compute metrics in distributed setups (in particular non-additive metrics like F1).
        seed (:obj:`int`, optional): If specified, this will temporarily set numpy\'s random seed when :func:`datasets.Metric.compute` is run.
        experiment_id (``str``): A specific experiment id. This is used if several distributed evaluations share the same file system.
            This is useful to compute metrics in distributed setups (in particular non-additive metrics like F1).
        max_concurrent_cache_files (``int``): Max number of concurrent metrics cache files (default 10000).
        timeout (``Union[int, float]``): Timeout in second for distributed setting synchronization.
    '''
    config_name: Incomplete
    num_process: Incomplete
    process_id: Incomplete
    max_concurrent_cache_files: Incomplete
    keep_in_memory: Incomplete
    data_dir: Incomplete
    seed: Incomplete
    timeout: Incomplete
    buf_writer: Incomplete
    writer: Incomplete
    writer_batch_size: Incomplete
    data: Incomplete
    cache_file_name: Incomplete
    filelock: Incomplete
    rendez_vous_lock: Incomplete
    file_paths: Incomplete
    filelocks: Incomplete
    def __init__(self, config_name: str | None = None, keep_in_memory: bool = False, cache_dir: str | None = None, num_process: int = 1, process_id: int = 0, seed: int | None = None, experiment_id: str | None = None, max_concurrent_cache_files: int = 10000, timeout: int | float = 100, **kwargs) -> None: ...
    def __len__(self) -> int:
        """Return the number of examples (predictions or predictions/references pair)
        currently stored in the metric's cache.
        """
    def compute(self, *, predictions: Incomplete | None = None, references: Incomplete | None = None, **kwargs) -> dict | None:
        '''Compute the metrics.

        Usage of positional arguments is not allowed to prevent mistakes.

        Args:
            predictions (list/array/tensor, optional): Predictions.
            references (list/array/tensor, optional): References.
            **kwargs (optional): Keyword arguments that will be forwarded to the metrics :meth:`_compute`
                method (see details in the docstring).

        Return:
            dict or None

            - Dictionary with the metrics if this metric is run on the main process (``process_id == 0``).
            - None if the metric is not run on the main process (``process_id != 0``).

        Example:

        ```py
        >>> from datasets import load_metric
        >>> metric = load_metric("accuracy")
        >>> accuracy = metric.compute(predictions=model_prediction, references=labels)
        ```
        '''
    def add_batch(self, *, predictions: Incomplete | None = None, references: Incomplete | None = None, **kwargs) -> None:
        '''Add a batch of predictions and references for the metric\'s stack.

        Args:
            predictions (list/array/tensor, optional): Predictions.
            references (list/array/tensor, optional): References.

        Example:

        ```py
        >>> from datasets import load_metric
        >>> metric = load_metric("accuracy")
        >>> metric.add_batch(predictions=model_prediction, references=labels)
        ```
        '''
    def add(self, *, prediction: Incomplete | None = None, reference: Incomplete | None = None, **kwargs) -> None:
        '''Add one prediction and reference for the metric\'s stack.

        Args:
            prediction (list/array/tensor, optional): Predictions.
            reference (list/array/tensor, optional): References.

        Example:

        ```py
        >>> from datasets import load_metric
        >>> metric = load_metric("accuracy")
        >>> metric.add(predictions=model_predictions, references=labels)
        ```
        '''
    def download_and_prepare(self, download_config: DownloadConfig | None = None, dl_manager: DownloadManager | None = None):
        """Downloads and prepares dataset for reading.

        Args:
            download_config (:class:`DownloadConfig`, optional): Specific download configuration parameters.
            dl_manager (:class:`DownloadManager`, optional): Specific download manager to use.
        """
    def __del__(self) -> None: ...
