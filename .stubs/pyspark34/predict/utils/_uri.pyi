from _typeshed import Incomplete
from azureml.core import Workspace as Workspace
from enum import Enum
from pyspark.sql import SparkSession as SparkSession

class HadoopSchemas(Enum):
    WASB: str
    WASBS: str
    ABFS: str
    ABFSS: str
    HDFS: str

class UrlSchemas(Enum):
    HTTP: str
    HTTPS: str

class AzureMLSchemas(Enum):
    AML: str

SupportedSchemas: Incomplete
