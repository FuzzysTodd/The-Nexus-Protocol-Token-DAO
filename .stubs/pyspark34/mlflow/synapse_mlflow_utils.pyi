import re
from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException, RestException as RestException
from pyspark import SparkContext as SparkContext
from synapse.ml.pymds.scrubbers.scrubber import IScrub
from typing import Dict

logger: Incomplete

class ArtifactNameScrubber(IScrub):
    pattern: Incomplete
    mask: str
    def scrub(self, msg: str) -> str: ...

kusto_logger: Incomplete
CONTEXT_FILE_PATH: str
trident_context: Dict[str, str]

def get_trident_context() -> Dict[str, str]: ...

class MLflowEnvConfig:
    capacity_id: Incomplete
    workspace_id: Incomplete
    artifact_id: Incomplete
    onelake_endpoint: Incomplete
    workload_endpoint: Incomplete
    shared_host: Incomplete
    shared_endpoint: Incomplete
    tracking_uri: Incomplete
    region: Incomplete
    pbienv: Incomplete
    driver_aad_token: Incomplete
    driver_storage_token: Incomplete
    def __init__(self, capacity_id: str, workspace_id: str, artifact_id: str, onelake_endpoint: str, workload_endpoint: str, shared_host: str, shared_endpoint: str, tracking_uri: str, region: str, pbienv: str, driver_aad_token: str, driver_storage_token: str) -> None: ...

class MLConfig:
    sc: Incomplete
    env_configs: Incomplete
    def __init__(self, sc: Incomplete | None = None) -> None: ...
    def get_mlflow_configs(self): ...
    @classmethod
    def get_mlflow_workload_host(cls, pbienv: str, capacity_id: str, workspace_id: str, shared_host: str = ''): ...
    @classmethod
    def get_mlflow_workload_endpoint(cls, pbienv: str, capacity_id: str, workspace_id: str, shared_host: str = ''): ...
    @classmethod
    def get_mlflow_shared_host(cls, pbienv: str): ...

def set_mlflow_env_config(value: MLflowEnvConfig, overwrite_executor_hadoop_conf: bool = False): ...
def parse_and_write_hadoop_conf(overwrite: bool = False) -> str:
    """On executor, predict needs to create local spark session in order to
    load spark model. But read/write to onelake will fail since not all necessary
    hadoop config are export to core-site.xml. This function is supposed to used on
    executor which copies origin core-site.xml and fill necessary values in
    '/home/trusted-service-user/.trident-context'

    Args:
        overwrite (bool, optional): If True, regenerate hadoop config file.
        Defaults to False.

    Raises:
        Exception: When source hadoop config file not found

    Returns:
        str: new HADOOP_CONF_DIR value
    """
def get_mlflow_env_config(refresh_token: bool = True) -> MLflowEnvConfig: ...
def set_envs() -> None: ...
def safe_get_spark_context() -> SparkContext: ...
def get_sds_url(mlflow_workload_endpoint: str = None): ...
def parse_tridentml_uri(uri):
    """
    example uri: sds://{region}.pbidedicated.windows.net/webapi/capacities/{capacity-object-id}/workspaces/{trident-workspace-id}
    """
def protect_module(module_name: str, throwable: bool = True):
    """
    decorate a function so that it catch and record all exceptions
    """
def record_all_public_functions(cls): ...
def timed(function): ...
def check_experiment_name(input_string) -> re.Match[str] | None: ...
def check_model_name(input_string) -> re.Match[str] | None: ...
