from _typeshed import Incomplete
from mlflow.entities import ViewType as ViewType
from mlflow.environment_variables import MLFLOW_EXPERIMENT_ID as MLFLOW_EXPERIMENT_ID
from mlflow.utils.time_utils import conv_longdate_to_str as conv_longdate_to_str

RUN_ID: Incomplete

def commands() -> None:
    """
    Manage runs. To manage runs of experiments associated with a tracking server, set the
    MLFLOW_TRACKING_URI environment variable to the URL of the desired server.
    """
def list_run(experiment_id, view) -> None:
    """
    List all runs of the specified experiment in the configured tracking server.
    """
def delete_run(run_id) -> None:
    """
    Mark a run for deletion. Return an error if the run does not exist or
    is already marked. You can restore a marked run with ``restore_run``,
    or permanently delete a run in the backend store.
    """
def restore_run(run_id) -> None:
    """
    Restore a deleted run.
    Returns an error if the run is active or has been permanently deleted.
    """
def describe_run(run_id) -> None:
    """
    All of run details will print to the stdout as JSON format.
    """
