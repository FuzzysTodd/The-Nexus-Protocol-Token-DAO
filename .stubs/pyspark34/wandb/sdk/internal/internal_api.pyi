import datetime
import requests
import threading
import wandb
from . import context as context
from ..lib import retry as retry
from ..lib.filenames import DIFF_FNAME as DIFF_FNAME, METADATA_FNAME as METADATA_FNAME
from ..lib.gitlib import GitRepo as GitRepo
from .progress import AsyncProgress as AsyncProgress, Progress as Progress, ProgressFn as ProgressFn
from _typeshed import Incomplete
from typing import Any, Callable, Dict, IO, Iterable, List, Mapping, MutableMapping, Sequence, TextIO, Tuple, TypedDict
from wandb import env as env, util as util
from wandb.apis.normalize import normalize_exceptions as normalize_exceptions, parse_backend_error_messages as parse_backend_error_messages
from wandb.errors import CommError as CommError, UnsupportedError as UnsupportedError, UsageError as UsageError
from wandb.integration.sagemaker import parse_sm_secrets as parse_sm_secrets
from wandb.old.settings import Settings as Settings
from wandb.sdk.lib.gql_request import GraphQLSession as GraphQLSession
from wandb.sdk.lib.hashutil import B64MD5 as B64MD5, md5_file_b64 as md5_file_b64

logger: Incomplete

class CreateArtifactFileSpecInput(TypedDict, total=False):
    """Corresponds to `type CreateArtifactFileSpecInput` in schema.graphql."""
    artifactID: str
    name: str
    md5: str
    mimetype: str | None
    artifactManifestID: str | None
    uploadPartsInput: List[Dict[str, object]] | None

class CreateArtifactFilesResponseFile(TypedDict):
    id: str
    name: str
    displayName: str
    uploadUrl: str | None
    uploadHeaders: Sequence[str]
    uploadMultipartUrls: UploadPartsResponse
    storagePath: str
    artifact: CreateArtifactFilesResponseFileNode

class CreateArtifactFilesResponseFileNode(TypedDict):
    id: str

class UploadPartsResponse(TypedDict):
    uploadUrlParts: List['UploadUrlParts']
    uploadID: str

class UploadUrlParts(TypedDict):
    partNumber: int
    uploadUrl: str

class CompleteMultipartUploadArtifactInput(TypedDict):
    """Corresponds to `type CompleteMultipartUploadArtifactInput` in schema.graphql."""
    completeMultipartAction: str
    completedParts: Dict[int, str]
    artifactID: str
    storagePath: str
    uploadID: str
    md5: str

class CompleteMultipartUploadArtifactResponse(TypedDict):
    digest: str

class DefaultSettings(TypedDict):
    section: str
    git_remote: str
    ignore_globs: List[str] | None
    base_url: str | None
    root_dir: str | None
    api_key: str | None
    entity: str | None
    project: str | None

SweepState: Incomplete
Number = int | float
httpclient_logger: Incomplete

def check_httpclient_logger_handler() -> None: ...
def check_httpx_exc_retriable(exc: Exception) -> bool: ...

class _ThreadLocalData(threading.local):
    context: context.Context | None
    def __init__(self) -> None: ...

class Api:
    """W&B Internal Api wrapper.

    Note:
        Settings are automatically overridden by looking for
        a `wandb/settings` file in the current working directory or its parent
        directory. If none can be found, we look in the current user's home
        directory.

    Arguments:
        default_settings(dict, optional): If you aren't using a settings
        file, or you wish to override the section to use in the settings file
        Override the settings here.
    """
    HTTP_TIMEOUT: Incomplete
    FILE_PUSHER_TIMEOUT: Incomplete
    default_settings: Incomplete
    retry_timedelta: Incomplete
    retry_uploads: int
    git: Incomplete
    dynamic_settings: Incomplete
    client: Incomplete
    retry_callback: Incomplete
    upload_file_retry: Incomplete
    upload_multipart_file_chunk_retry: Incomplete
    query_types: Incomplete
    mutation_types: Incomplete
    server_info_types: Incomplete
    server_use_artifact_input_info: Incomplete
    server_create_artifact_input_info: Incomplete
    server_artifact_fields_info: Incomplete
    fail_run_queue_item_input_info: Incomplete
    create_launch_agent_input_info: Incomplete
    server_create_run_queue_supports_drc: Incomplete
    def __init__(self, default_settings: wandb.sdk.wandb_settings.Settings | wandb.sdk.internal.settings_static.SettingsStatic | Settings | dict | None = None, load_settings: bool = True, retry_timedelta: datetime.timedelta = ..., environ: MutableMapping = ..., retry_callback: Callable[[int, str], Any] | None = None) -> None: ...
    def gql(self, *args: Any, **kwargs: Any) -> Any: ...
    def set_local_context(self, api_context: context.Context | None) -> None: ...
    def clear_local_context(self) -> None: ...
    @property
    def context(self) -> context.Context: ...
    def reauth(self) -> None:
        """Ensure the current api key is set in the transport."""
    def relocate(self) -> None:
        """Ensure the current api points to the right server."""
    def execute(self, *args: Any, **kwargs: Any) -> _Response:
        """Wrapper around execute that logs in cases of failure."""
    def disabled(self) -> str | bool: ...
    def set_current_run_id(self, run_id: str) -> None: ...
    @property
    def current_run_id(self) -> str | None: ...
    @property
    def user_agent(self) -> str: ...
    @property
    def api_key(self) -> str | None: ...
    @property
    def api_url(self) -> str: ...
    @property
    def app_url(self) -> str: ...
    @property
    def default_entity(self) -> str: ...
    def settings(self, key: str | None = None, section: str | None = None) -> Any:
        '''The settings overridden from the wandb/settings file.

        Arguments:
            key (str, optional): If provided only this setting is returned
            section (str, optional): If provided this section of the setting file is
            used, defaults to "default"

        Returns:
            A dict with the current settings

                {
                    "entity": "models",
                    "base_url": "https://api.wandb.ai",
                    "project": None
                }
        '''
    def clear_setting(self, key: str, globally: bool = False, persist: bool = False) -> None: ...
    def set_setting(self, key: str, value: Any, globally: bool = False, persist: bool = False) -> None: ...
    def parse_slug(self, slug: str, project: str | None = None, run: str | None = None) -> Tuple[str, str]:
        """Parse a slug into a project and run.

        Arguments:
            slug (str): The slug to parse
            project (str, optional): The project to use, if not provided it will be
            inferred from the slug
            run (str, optional): The run to use, if not provided it will be inferred
            from the slug

        Returns:
            A dict with the project and run
        """
    def server_info_introspection(self) -> Tuple[List[str], List[str], List[str]]: ...
    def server_settings_introspection(self) -> None: ...
    def server_use_artifact_input_introspection(self) -> List: ...
    def launch_agent_introspection(self) -> str | None: ...
    def create_run_queue_introspection(self) -> Tuple[bool, bool]: ...
    def create_default_resource_config_introspection(self) -> bool: ...
    def fail_run_queue_item_introspection(self) -> bool: ...
    def fail_run_queue_item_fields_introspection(self) -> List: ...
    def fail_run_queue_item(self, run_queue_item_id: str, message: str, stage: str, file_paths: List[str] | None = None) -> bool: ...
    def update_run_queue_item_warning_introspection(self) -> bool: ...
    def update_run_queue_item_warning(self, run_queue_item_id: str, message: str, stage: str, file_paths: List[str] | None = None) -> bool: ...
    def viewer(self) -> Dict[str, Any]: ...
    def max_cli_version(self) -> str | None: ...
    def viewer_server_info(self) -> Tuple[Dict[str, Any], Dict[str, Any]]: ...
    def list_projects(self, entity: str | None = None) -> List[Dict[str, str]]:
        '''List projects in W&B scoped by entity.

        Arguments:
            entity (str, optional): The entity to scope this project to.

        Returns:
                [{"id","name","description"}]
        '''
    def project(self, project: str, entity: str | None = None) -> _Response:
        '''Retrieve project.

        Arguments:
            project (str): The project to get details for
            entity (str, optional): The entity to scope this project to.

        Returns:
                [{"id","name","repo","dockerImage","description"}]
        '''
    def sweep(self, sweep: str, specs: str, project: str | None = None, entity: str | None = None) -> Dict[str, Any]:
        '''Retrieve sweep.

        Arguments:
            sweep (str): The sweep to get details for
            specs (str): history specs
            project (str, optional): The project to scope this sweep to.
            entity (str, optional): The entity to scope this sweep to.

        Returns:
                [{"id","name","repo","dockerImage","description"}]
        '''
    def list_runs(self, project: str, entity: str | None = None) -> List[Dict[str, str]]:
        '''List runs in W&B scoped by project.

        Arguments:
            project (str): The project to scope the runs to
            entity (str, optional): The entity to scope this project to.  Defaults to public models

        Returns:
                [{"id","name","description"}]
        '''
    def run_config(self, project: str, run: str | None = None, entity: str | None = None) -> Tuple[str, Dict[str, Any], str | None, Dict[str, Any]]:
        """Get the relevant configs for a run.

        Arguments:
            project (str): The project to download, (can include bucket)
            run (str, optional): The run to download
            entity (str, optional): The entity to scope this project to.
        """
    def run_resume_status(self, entity: str, project_name: str, name: str) -> Dict[str, Any] | None:
        """Check if a run exists and get resume information.

        Arguments:
            entity (str): The entity to scope this project to.
            project_name (str): The project to download, (can include bucket)
            name (str): The run to download
        """
    def check_stop_requested(self, project_name: str, entity_name: str, run_id: str) -> bool: ...
    def format_project(self, project: str) -> str: ...
    def upsert_project(self, project: str, id: str | None = None, description: str | None = None, entity: str | None = None) -> Dict[str, Any]:
        """Create a new project.

        Arguments:
            project (str): The project to create
            description (str, optional): A description of this project
            entity (str, optional): The entity to scope this project to.
        """
    def entity_is_team(self, entity: str) -> bool: ...
    def get_project_run_queues(self, entity: str, project: str) -> List[Dict[str, str]]: ...
    def create_default_resource_config(self, entity: str, resource: str, config: str) -> Dict[str, Any] | None: ...
    def create_run_queue(self, entity: str, project: str, queue_name: str, access: str, config_id: str | None = None) -> Dict[str, Any] | None: ...
    def push_to_run_queue_by_name(self, entity: str, project: str, queue_name: str, run_spec: str) -> Dict[str, Any] | None:
        """Queryless mutation, should be used before legacy fallback method."""
    def push_to_run_queue(self, queue_name: str, launch_spec: Dict[str, str], project_queue: str) -> Dict[str, Any] | None: ...
    def pop_from_run_queue(self, queue_name: str, entity: str | None = None, project: str | None = None, agent_id: str | None = None) -> Dict[str, Any] | None: ...
    def ack_run_queue_item(self, item_id: str, run_id: str | None = None) -> bool: ...
    def create_launch_agent_fields_introspection(self) -> List: ...
    def create_launch_agent(self, entity: str, project: str, queues: List[str], agent_config: Dict[str, Any], version: str, gorilla_agent_support: bool) -> dict: ...
    def update_launch_agent_status(self, agent_id: str, status: str, gorilla_agent_support: bool) -> dict: ...
    def get_launch_agent(self, agent_id: str, gorilla_agent_support: bool) -> dict: ...
    def upsert_run(self, id: str | None = None, name: str | None = None, project: str | None = None, host: str | None = None, group: str | None = None, tags: List[str] | None = None, config: dict | None = None, description: str | None = None, entity: str | None = None, state: str | None = None, display_name: str | None = None, notes: str | None = None, repo: str | None = None, job_type: str | None = None, program_path: str | None = None, commit: str | None = None, sweep_name: str | None = None, summary_metrics: str | None = None, num_retries: int | None = None) -> Tuple[dict, bool, List | None]:
        """Update a run.

        Arguments:
            id (str, optional): The existing run to update
            name (str, optional): The name of the run to create
            group (str, optional): Name of the group this run is a part of
            project (str, optional): The name of the project
            host (str, optional): The name of the host
            tags (list, optional): A list of tags to apply to the run
            config (dict, optional): The latest config params
            description (str, optional): A description of this project
            entity (str, optional): The entity to scope this project to.
            display_name (str, optional): The display name of this project
            notes (str, optional): Notes about this run
            repo (str, optional): Url of the program's repository.
            state (str, optional): State of the program.
            job_type (str, optional): Type of job, e.g 'train'.
            program_path (str, optional): Path to the program.
            commit (str, optional): The Git SHA to associate the run with
            sweep_name (str, optional): The name of the sweep this run is a part of
            summary_metrics (str, optional): The JSON summary metrics
            num_retries (int, optional): Number of retries
        """
    def get_run_info(self, entity: str, project: str, name: str) -> dict: ...
    def get_run_state(self, entity: str, project: str, name: str) -> str: ...
    def create_run_files_introspection(self) -> bool: ...
    def upload_urls(self, project: str, files: List[str] | Dict[str, IO], run: str | None = None, entity: str | None = None, description: str | None = None) -> Tuple[str, List[str], Dict[str, Dict[str, Any]]]:
        '''Generate temporary resumable upload urls.

        Arguments:
            project (str): The project to download
            files (list or dict): The filenames to upload
            run (str, optional): The run to upload to
            entity (str, optional): The entity to scope this project to.
            description (str, optional): description

        Returns:
            (run_id, upload_headers, file_info)
            run_id: id of run we uploaded files to
            upload_headers: A list of headers to use when uploading files.
            file_info: A dict of filenames and urls.
                {
                    "run_id": "run_id",
                    "upload_headers": [""],
                    "file_info":  [
                        { "weights.h5": { "uploadUrl": "https://weights.url" } },
                        { "model.json": { "uploadUrl": "https://model.json" } }
                    ]
                }
        '''
    def legacy_upload_urls(self, project: str, files: List[str] | Dict[str, IO], run: str | None = None, entity: str | None = None, description: str | None = None) -> Tuple[str, List[str], Dict[str, Dict[str, Any]]]:
        """Generate temporary resumable upload urls.

        A new mutation createRunFiles was introduced after 0.15.4.
        This function is used to support older versions.
        """
    def download_urls(self, project: str, run: str | None = None, entity: str | None = None) -> Dict[str, Dict[str, str]]:
        '''Generate download urls.

        Arguments:
            project (str): The project to download
            run (str): The run to upload to
            entity (str, optional): The entity to scope this project to.  Defaults to wandb models

        Returns:
            A dict of extensions and urls

                {
                    \'weights.h5\': { "url": "https://weights.url", "updatedAt": \'2013-04-26T22:22:23.832Z\', \'md5\': \'mZFLkyvTelC5g8XnyQrpOw==\' },
                    \'model.json\': { "url": "https://model.url", "updatedAt": \'2013-04-26T22:22:23.832Z\', \'md5\': \'mZFLkyvTelC5g8XnyQrpOw==\' }
                }
        '''
    def download_url(self, project: str, file_name: str, run: str | None = None, entity: str | None = None) -> Dict[str, str] | None:
        '''Generate download urls.

        Arguments:
            project (str): The project to download
            file_name (str): The name of the file to download
            run (str): The run to upload to
            entity (str, optional): The entity to scope this project to.  Defaults to wandb models

        Returns:
            A dict of extensions and urls

                { "url": "https://weights.url", "updatedAt": \'2013-04-26T22:22:23.832Z\', \'md5\': \'mZFLkyvTelC5g8XnyQrpOw==\' }

        '''
    def download_file(self, url: str) -> Tuple[int, requests.Response]:
        """Initiate a streaming download.

        Arguments:
            url (str): The url to download

        Returns:
            A tuple of the content length and the streaming response
        """
    def download_write_file(self, metadata: Dict[str, str], out_dir: str | None = None) -> Tuple[str, requests.Response | None]:
        """Download a file from a run and write it to wandb/.

        Arguments:
            metadata (obj): The metadata object for the file to download. Comes from Api.download_urls().
            out_dir (str, optional): The directory to write the file to. Defaults to wandb/

        Returns:
            A tuple of the file's local path and the streaming response. The streaming response is None if the file
            already existed and was up-to-date.
        """
    def upload_file_azure(self, url: str, file: Any, extra_headers: Dict[str, str]) -> None:
        """Upload a file to azure."""
    def upload_multipart_file_chunk(self, url: str, upload_chunk: bytes, extra_headers: Dict[str, str] | None = None) -> requests.Response | None:
        """Upload a file chunk to S3 with failure resumption.

        Arguments:
            url: The url to download
            upload_chunk: The path to the file you want to upload
            extra_headers: A dictionary of extra headers to send with the request

        Returns:
            The `requests` library response object
        """
    def upload_file(self, url: str, file: IO[bytes], callback: ProgressFn | None = None, extra_headers: Dict[str, str] | None = None) -> requests.Response | None:
        """Upload a file to W&B with failure resumption.

        Arguments:
            url: The url to download
            file: The path to the file you want to upload
            callback: A callback which is passed the number of
            bytes uploaded since the last time it was called, used to report progress
            extra_headers: A dictionary of extra headers to send with the request

        Returns:
            The `requests` library response object
        """
    async def upload_file_async(self, url: str, file: IO[bytes], callback: ProgressFn | None = None, extra_headers: Dict[str, str] | None = None) -> None:
        """An async not-quite-equivalent version of `upload_file`.

        Differences from `upload_file`:
            - This method doesn't implement Azure uploads. (The Azure SDK supports
              async, but it's nontrivial to use it here.) If the upload looks like
              it's destined for Azure, this method will delegate to the sync impl.
            - Consequently, this method doesn't return the response object.
              (Because it might fall back to the sync impl, it would sometimes
               return a `requests.Response` and sometimes an `httpx.Response`.)
            - This method doesn't wrap retryable errors in `TransientError`.
              It leaves that determination to the caller.
        """
    async def upload_file_retry_async(self, url: str, file: IO[bytes], callback: ProgressFn | None = None, extra_headers: Dict[str, str] | None = None, num_retries: int = 100) -> None: ...
    def register_agent(self, host: str, sweep_id: str | None = None, project_name: str | None = None, entity: str | None = None) -> dict:
        """Register a new agent.

        Arguments:
            host (str): hostname
            sweep_id (str): sweep id
            project_name: (str): model that contains sweep
            entity: (str): entity that contains sweep
        """
    def agent_heartbeat(self, agent_id: str, metrics: dict, run_states: dict) -> List[Dict[str, Any]]:
        """Notify server about agent state, receive commands.

        Arguments:
            agent_id (str): agent_id
            metrics (dict): system metrics
            run_states (dict): run_id: state mapping
        Returns:
            List of commands to execute.
        """
    def upsert_sweep(self, config: dict, controller: str | None = None, launch_scheduler: str | None = None, scheduler: str | None = None, obj_id: str | None = None, project: str | None = None, entity: str | None = None, state: str | None = None) -> Tuple[str, List[str]]:
        """Upsert a sweep object.

        Arguments:
            config (dict): sweep config (will be converted to yaml)
            controller (str): controller to use
            launch_scheduler (str): launch scheduler to use
            scheduler (str): scheduler to use
            obj_id (str): object id
            project (str): project to use
            entity (str): entity to use
            state (str): state
        """
    def create_anonymous_api_key(self) -> str:
        """Create a new API key belonging to a new anonymous user."""
    @staticmethod
    def file_current(fname: str, md5: B64MD5) -> bool:
        """Checksum a file and compare the md5 with the known md5."""
    def pull(self, project: str, run: str | None = None, entity: str | None = None) -> List[requests.Response]:
        """Download files from W&B.

        Arguments:
            project (str): The project to download
            run (str, optional): The run to upload to
            entity (str, optional): The entity to scope this project to.  Defaults to wandb models

        Returns:
            The `requests` library response object
        """
    def get_project(self) -> str: ...
    def push(self, files: List[str] | Dict[str, IO], run: str | None = None, entity: str | None = None, project: str | None = None, description: str | None = None, force: bool = True, progress: TextIO | bool = False) -> List[requests.Response | None]:
        """Uploads multiple files to W&B.

        Arguments:
            files (list or dict): The filenames to upload, when dict the values are open files
            run (str, optional): The run to upload to
            entity (str, optional): The entity to scope this project to.  Defaults to wandb models
            project (str, optional): The name of the project to upload to. Defaults to the one in settings.
            description (str, optional): The description of the changes
            force (bool, optional): Whether to prevent push if git has uncommitted changes
            progress (callable, or stream): If callable, will be called with (chunk_bytes,
                total_bytes) as argument else if True, renders a progress bar to stream.

        Returns:
            A list of `requests.Response` objects
        """
    def link_artifact(self, client_id: str, server_id: str, portfolio_name: str, entity: str, project: str, aliases: Sequence[str]) -> Dict[str, Any]: ...
    def use_artifact(self, artifact_id: str, entity_name: str | None = None, project_name: str | None = None, run_name: str | None = None, use_as: str | None = None) -> Dict[str, Any] | None: ...
    def create_artifact_type(self, artifact_type_name: str, entity_name: str | None = None, project_name: str | None = None, description: str | None = None) -> str | None: ...
    def server_artifact_introspection(self) -> List: ...
    def server_create_artifact_introspection(self) -> List: ...
    def create_artifact(self, artifact_type_name: str, artifact_collection_name: str, digest: str, client_id: str | None = None, sequence_client_id: str | None = None, entity_name: str | None = None, project_name: str | None = None, run_name: str | None = None, description: str | None = None, metadata: Dict | None = None, ttl_duration_seconds: int | None = None, aliases: List[Dict[str, str]] | None = None, distributed_id: str | None = None, is_user_created: bool | None = False, history_step: int | None = None) -> Tuple[Dict, Dict]: ...
    def commit_artifact(self, artifact_id: str) -> _Response: ...
    def complete_multipart_upload_artifact(self, artifact_id: str, storage_path: str, completed_parts: List[Dict[str, Any]], upload_id: str, complete_multipart_action: str = 'Complete') -> str | None: ...
    def create_artifact_manifest(self, name: str, digest: str, artifact_id: str | None, base_artifact_id: str | None = None, entity: str | None = None, project: str | None = None, run: str | None = None, include_upload: bool = True, type: str = 'FULL') -> Tuple[str, Dict[str, Any]]: ...
    def update_artifact_manifest(self, artifact_manifest_id: str, base_artifact_id: str | None = None, digest: str | None = None, include_upload: bool | None = True) -> Tuple[str, Dict[str, Any]]: ...
    def server_create_artifact_file_spec_input_introspection(self) -> List: ...
    def create_artifact_files(self, artifact_files: Iterable['CreateArtifactFileSpecInput']) -> Mapping[str, 'CreateArtifactFilesResponseFile']: ...
    def notify_scriptable_run_alert(self, title: str, text: str, level: str | None = None, wait_duration: Number | None = None) -> bool: ...
    def get_sweep_state(self, sweep: str, entity: str | None = None, project: str | None = None) -> SweepState: ...
    def set_sweep_state(self, sweep: str, state: SweepState, entity: str | None = None, project: str | None = None) -> None: ...
    def stop_sweep(self, sweep: str, entity: str | None = None, project: str | None = None) -> None:
        """Finish the sweep to stop running new runs and let currently running runs finish."""
    def cancel_sweep(self, sweep: str, entity: str | None = None, project: str | None = None) -> None:
        """Cancel the sweep to kill all running runs and stop running new runs."""
    def pause_sweep(self, sweep: str, entity: str | None = None, project: str | None = None) -> None:
        """Pause the sweep to temporarily stop running new runs."""
    def resume_sweep(self, sweep: str, entity: str | None = None, project: str | None = None) -> None:
        """Resume the sweep to continue running new runs."""
    def stop_run(self, run_id: str) -> bool: ...
