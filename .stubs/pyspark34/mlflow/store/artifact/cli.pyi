from mlflow.store.artifact.artifact_repository_registry import get_artifact_repository as get_artifact_repository
from mlflow.utils.proto_json_utils import message_to_json as message_to_json

def commands() -> None:
    """
    Upload, list, and download artifacts from an MLflow artifact repository.

    To manage artifacts for a run associated with a tracking server, set the MLFLOW_TRACKING_URI
    environment variable to the URL of the desired server.
    """
def log_artifact(local_file, run_id, artifact_path) -> None:
    """
    Log a local file as an artifact of a run, optionally within a run-specific
    artifact path. Run artifacts can be organized into directories, so you can
    place the artifact in a directory this way.
    """
def log_artifacts(local_dir, run_id, artifact_path) -> None:
    """
    Log the files within a local directory as an artifact of a run, optionally
    within a run-specific artifact path. Run artifacts can be organized into
    directories, so you can place the artifact in a directory this way.
    """
def list_artifacts(run_id, artifact_path) -> None:
    """
    Return all the artifacts directly under run's root artifact directory,
    or a sub-directory. The output is a JSON-formatted list.
    """
def download_artifacts(run_id, artifact_path, artifact_uri, dst_path) -> None:
    """
    Download an artifact file or directory to a local directory.
    The output is the name of the file or directory on the local filesystem.

    Either ``--artifact-uri`` or ``--run-id`` must be provided.
    """
