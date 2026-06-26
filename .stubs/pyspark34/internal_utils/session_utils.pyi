from .constants import SYNAPSE_CLUSTER_IDENTIFIER as SYNAPSE_CLUSTER_IDENTIFIER, SYNAPSE_CLUSTER_TYPE as SYNAPSE_CLUSTER_TYPE, SYNAPSE_TOKEN_SERVICE_ENDPOINT as SYNAPSE_TOKEN_SERVICE_ENDPOINT
from _typeshed import Incomplete
from pyspark import SparkContext as SparkContext
from typing import Dict

logger: Incomplete
CONTEXT_FILE_PATH: str
TOKEN_SERVICE_FILE_PATH: str
SPARK_CONF_PATH: str
trident_context: Dict[str, str]

class TokenServiceConfig:
    sessionToken: Incomplete
    tokenServiceEndpoint: Incomplete
    clusterName: Incomplete
    clusterType: Incomplete
    def __init__(self, sessionToken: str, tokenServiceEndpoint: str, clusterName: str, clusterType: str) -> None: ...

def get_spark_conf() -> Dict[str, str]: ...
def get_fabric_context() -> Dict[str, str]: ...
def safe_get_spark_context() -> SparkContext: ...
def reset_cached_context() -> None: ...
