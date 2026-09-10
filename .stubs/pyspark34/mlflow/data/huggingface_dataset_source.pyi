import datasets
from mlflow.data.dataset_source import DatasetSource as DatasetSource
from mlflow.utils.annotations import experimental as experimental
from typing import Mapping, Sequence

class HuggingFaceDatasetSource(DatasetSource):
    """
    Represents the source of a Hugging Face dataset used in MLflow Tracking.
    """
    def __init__(self, path: str, config_name: str | None = None, data_dir: str | None = None, data_files: str | Sequence[str] | Mapping[str, str | Sequence[str]] | None = None, split: str | datasets.Split | None = None, revision: str | datasets.Version | None = None, task: str | datasets.TaskTemplate | None = None) -> None:
        """
        :param path: The path of the Hugging Face dataset.
        :param config_name: The name of of the Hugging Face dataset configuration.
        :param data_dir: The `data_dir` of the Hugging Face dataset configuration.
        :param data_files: Paths to source data file(s) for the Hugging Face dataset configuration.
        :param revision: Version of the dataset script to load.
        :param task: The task to prepare the Hugging Face dataset for during training and
                     evaluation.
        """
    def load(self, **kwargs):
        """
        Loads the dataset source as a Hugging Face Dataset.

        :param kwargs: Additional keyword arguments used for loading the dataset with
                       the Hugging Face ``datasets.load_dataset()`` method. The following keyword
                       arguments are used automatically from the dataset source but may be
                       overridden by values passed in ``**kwargs``: ``path``, ``name``,
                       ``data_dir``, ``data_files``, ``split``, ``revision``, ``task``.
        :return: An instance of ``datasets.Dataset``.
        """
