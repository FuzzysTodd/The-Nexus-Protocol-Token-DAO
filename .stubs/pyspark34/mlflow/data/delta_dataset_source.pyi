from _typeshed import Incomplete
from mlflow.data.dataset_source import DatasetSource as DatasetSource
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.databricks_utils import is_in_databricks_runtime as is_in_databricks_runtime

DATABRICKS_HIVE_METASTORE_NAME: str
DATABRICKS_LOCAL_METASTORE_NAMES: Incomplete
DATABRICKS_SAMPLES_CATALOG_NAME: str

class DeltaDatasetSource(DatasetSource):
    """
    Represents the source of a dataset stored at in a delta table.
    """
    def __init__(self, path: str | None = None, delta_table_name: str | None = None, delta_table_version: int | None = None) -> None: ...
    def load(self, **kwargs):
        """
        Loads the dataset source as a Delta Dataset Source.
        :return: An instance of ``pyspark.sql.DataFrame``.
        """
    @property
    def path(self) -> str | None: ...
    @property
    def delta_table_name(self) -> str | None: ...
    @property
    def delta_table_version(self) -> int | None: ...
