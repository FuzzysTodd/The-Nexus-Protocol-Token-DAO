from mlflow.data.dataset import Dataset
from mlflow.data.dataset_source import DatasetSource
from mlflow.entities import Dataset as DatasetEntity, DatasetInput

__all__ = ['get_source']

def get_source(dataset: DatasetEntity | DatasetInput | Dataset) -> DatasetSource:
    """
    Obtains the source of the specified dataset or dataset input.

    :param dataset: An instance of :py:class:`mlflow.data.dataset.Dataset
                    <mlflow.data.dataset.Dataset>`,
                    :py:class:`mlflow.entities.Dataset`, or
                    :py:class:`mlflow.entities.DatasetInput`.
    :return: An instance of :py:class:`DatasetSource <mlflow.data.dataset_source.DatasetSource>`.
    """
