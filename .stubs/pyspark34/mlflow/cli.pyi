import click
from mlflow import projects as projects, version as version
from mlflow.entities import ViewType as ViewType
from mlflow.entities.lifecycle_stage import LifecycleStage as LifecycleStage
from mlflow.environment_variables import MLFLOW_EXPERIMENT_ID as MLFLOW_EXPERIMENT_ID, MLFLOW_EXPERIMENT_NAME as MLFLOW_EXPERIMENT_NAME
from mlflow.exceptions import InvalidUrlException as InvalidUrlException, MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.store.artifact.artifact_repository_registry import get_artifact_repository as get_artifact_repository
from mlflow.store.tracking import DEFAULT_ARTIFACTS_URI as DEFAULT_ARTIFACTS_URI, DEFAULT_LOCAL_FILE_AND_ARTIFACT_PATH as DEFAULT_LOCAL_FILE_AND_ARTIFACT_PATH
from mlflow.utils import cli_args as cli_args
from mlflow.utils.logging_utils import eprint as eprint
from mlflow.utils.os import is_windows as is_windows
from mlflow.utils.process import ShellCommandException as ShellCommandException
from mlflow.utils.server_cli_utils import artifacts_only_config_validation as artifacts_only_config_validation, resolve_default_artifact_root as resolve_default_artifact_root

class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name): ...

def cli() -> None: ...
def run(uri, entry_point, version, param_list, docker_args, experiment_name, experiment_id, backend, backend_config, env_manager, storage_dir, run_id, run_name, build_image) -> None:
    """
    Run an MLflow project from the given URI.

    For local runs, the run will block until it completes.
    Otherwise, the project will run asynchronously.

    If running locally (the default), the URI can be either a Git repository URI or a local path.
    If running on Databricks, the URI must be a Git repository.

    By default, Git projects run in a new working directory with the given parameters, while
    local projects run from the project's root directory.
    """
def server(backend_store_uri, registry_store_uri, default_artifact_root, serve_artifacts, artifacts_only, artifacts_destination, host, port, workers, static_prefix, gunicorn_opts, waitress_opts, expose_prometheus, app_name, dev) -> None:
    """
    Run the MLflow tracking server.

    The server listens on http://localhost:5000 by default and only accepts connections
    from the local machine. To let the server accept connections from other machines, you will need
    to pass ``--host 0.0.0.0`` to listen on all network interfaces
    (or a specific interface address).
    """
def gc(older_than, backend_store_uri, run_ids, experiment_ids):
    """
    Permanently delete runs in the `deleted` lifecycle stage from the specified backend store.
    This command deletes all artifacts and metadata associated with the specified runs.
    If the provided artifact URL is invalid, the artifact deletion will be bypassed,
    and the gc process will continue.
    """
def doctor(mask_envs) -> None: ...
