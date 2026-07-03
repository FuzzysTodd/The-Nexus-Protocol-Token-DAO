from mlflow.data.dataset_source import DatasetSource as DatasetSource
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.utils.annotations import experimental as experimental

class SparkDatasetSource(DatasetSource):
    """
    Represents the source of a dataset stored in a spark table.
    """
    def __init__(self, path: str | None = None, table_name: str | None = None, sql: str | None = None) -> None: ...
    def load(self, **kwargs):
        """
        Loads the dataset source as a Spark Dataset Source.
        :return: An instance of ``pyspark.sql.DataFrame``.
        """
