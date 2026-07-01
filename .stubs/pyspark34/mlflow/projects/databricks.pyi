from _typeshed import Incomplete
from mlflow import tracking as tracking
from mlflow.entities import RunStatus as RunStatus
from mlflow.environment_variables import MLFLOW_EXPERIMENT_ID as MLFLOW_EXPERIMENT_ID, MLFLOW_TRACKING_URI as MLFLOW_TRACKING_URI
from mlflow.exceptions import ExecutionException as ExecutionException, MlflowException as MlflowException
from mlflow.projects.submitted_run import SubmittedRun as SubmittedRun
from mlflow.projects.utils import MLFLOW_LOCAL_BACKEND_RUN_ID_CONFIG as MLFLOW_LOCAL_BACKEND_RUN_ID_CONFIG
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.utils import databricks_utils as databricks_utils, file_utils as file_utils, rest_utils as rest_utils
from mlflow.utils.mlflow_tags import MLFLOW_DATABRICKS_RUN_URL as MLFLOW_DATABRICKS_RUN_URL, MLFLOW_DATABRICKS_SHELL_JOB_ID as MLFLOW_DATABRICKS_SHELL_JOB_ID, MLFLOW_DATABRICKS_SHELL_JOB_RUN_ID as MLFLOW_DATABRICKS_SHELL_JOB_RUN_ID, MLFLOW_DATABRICKS_WEBAPP_URL as MLFLOW_DATABRICKS_WEBAPP_URL
from mlflow.utils.string_utils import quote as quote
from mlflow.utils.uri import is_databricks_uri as is_databricks_uri, is_http_uri as is_http_uri
from mlflow.version import VERSION as VERSION, is_release_version as is_release_version

DB_CONTAINER_BASE: str
DB_TARFILE_BASE: Incomplete
DB_PROJECTS_BASE: Incomplete
DB_TARFILE_ARCHIVE_NAME: str
DBFS_EXPERIMENT_DIR_BASE: str

def before_run_validations(tracking_uri, backend_config) -> None:
    """Validations to perform before running a project on Databricks."""

class DatabricksJobRunner:
    """
    Helper class for running an MLflow project as a Databricks Job.
    :param databricks_profile: Optional Databricks CLI profile to use to fetch hostname &
           authentication information when making Databricks API requests.
    """
    databricks_profile_uri: Incomplete
    def __init__(self, databricks_profile_uri) -> None: ...
    def run_databricks(self, uri, entry_point, work_dir, parameters, experiment_id, cluster_spec, run_id, env_manager): ...
    def get_status(self, databricks_run_id): ...
    def get_run_result_state(self, databricks_run_id):
        """
        Get the run result state (string) of a Databricks job run.

        :param databricks_run_id: Integer Databricks job run ID.
        :returns `RunResultState
        <https://docs.databricks.com/api/latest/jobs.html#runresultstate>`_ or None if
        the run is still active.
        """
    def jobs_runs_cancel(self, databricks_run_id): ...
    def jobs_runs_get(self, databricks_run_id): ...

def run_databricks(remote_run, uri, entry_point, work_dir, parameters, experiment_id, cluster_spec, env_manager):
    """
    Run the project at the specified URI on Databricks, returning a ``SubmittedRun`` that can be
    used to query the run's status or wait for the resulting Databricks Job run to terminate.
    """

class DatabricksSubmittedRun(SubmittedRun):
    """
    Instance of SubmittedRun corresponding to a Databricks Job run launched to run an MLflow
    project. Note that run_id may be None, e.g. if we did not launch the run against a tracking
    server accessible to the local client.
    :param databricks_run_id: Run ID of the launched Databricks Job.
    :param mlflow_run_id: ID of the MLflow project run.
    :param databricks_job_runner: Instance of ``DatabricksJobRunner`` used to make Databricks API
                                  requests.
    """
    POLL_STATUS_INTERVAL: int
    def __init__(self, databricks_run_id, mlflow_run_id, databricks_job_runner) -> None: ...
    @property
    def run_id(self): ...
    def wait(self): ...
    def cancel(self) -> None: ...
    def get_status(self): ...
