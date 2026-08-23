from .builder.templates._wandb_bootstrap import FAILED_PACKAGES_POSTFIX as FAILED_PACKAGES_POSTFIX, FAILED_PACKAGES_PREFIX as FAILED_PACKAGES_PREFIX
from _typeshed import Incomplete
from typing import Any, Dict, List, Tuple
from wandb import util as util
from wandb.apis.internal import Api as Api
from wandb.errors import CommError as CommError
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.launch.agent.job_status_tracker import JobAndRunStatusTracker as JobAndRunStatusTracker
from wandb.sdk.launch.errors import LaunchError as LaunchError
from wandb.sdk.launch.github_reference import GitHubReference as GitHubReference
from wandb.sdk.launch.wandb_reference import WandbReference as WandbReference

FAILED_PACKAGES_REGEX: Incomplete
API_KEY_REGEX: str
MACRO_REGEX: Incomplete
PROJECT_SYNCHRONOUS: str
LAUNCH_CONFIG_FILE: str
LAUNCH_DEFAULT_PROJECT: str
LOG_PREFIX: Incomplete
MAX_ENV_LENGTHS: Dict[str, int]

def sanitize_wandb_api_key(s: str) -> str: ...
def get_project_from_job(job: str) -> str | None: ...
def set_project_entity_defaults(uri: str | None, job: str | None, api: Api, project: str | None, entity: str | None, launch_config: Dict[str, Any] | None) -> Tuple[str | None, str]: ...
def construct_launch_spec(uri: str | None, job: str | None, api: Api, name: str | None, project: str | None, entity: str | None, docker_image: str | None, resource: str | None, entry_point: List[str] | None, version: str | None, resource_args: Dict[str, Any] | None, launch_config: Dict[str, Any] | None, run_id: str | None, repository: str | None, author: str | None, sweep_id: str | None = None) -> Dict[str, Any]:
    """Construct the launch specification from CLI arguments."""
def validate_launch_spec_source(launch_spec: Dict[str, Any]) -> None: ...
def parse_wandb_uri(uri: str) -> Tuple[str, str, str]:
    """Parse wandb uri to retrieve entity, project and run name."""
def is_bare_wandb_uri(uri: str) -> bool:
    """Check that a wandb uri is valid.

    URI must be in the format
    `/<entity>/<project>/runs/<run_name>[other stuff]`
    or
    `/<entity>/<project>/artifacts/job/<job_name>[other stuff]`.
    """
def fetch_wandb_project_run_info(entity: str, project: str, run_name: str, api: Api) -> Any: ...
def download_entry_point(entity: str, project: str, run_name: str, api: Api, entry_point: str, dir: str) -> bool: ...
def download_wandb_python_deps(entity: str, project: str, run_name: str, api: Api, dir: str) -> str | None: ...
def get_local_python_deps(dir: str, filename: str = 'requirements.local.txt') -> str | None: ...
def diff_pip_requirements(req_1: List[str], req_2: List[str]) -> Dict[str, str]:
    """Return a list of pip requirements that are not in req_1 but are in req_2."""
def validate_wandb_python_deps(requirements_file: str | None, dir: str) -> None:
    """Warn if local python dependencies differ from wandb requirements.txt."""
def fetch_project_diff(entity: str, project: str, run_name: str, api: Api) -> str | None:
    """Fetches project diff from wandb servers."""
def apply_patch(patch_string: str, dst_dir: str) -> None:
    """Applies a patch file to a directory."""
def merge_parameters(higher_priority_params: Dict[str, Any], lower_priority_params: Dict[str, Any]) -> Dict[str, Any]:
    """Merge the contents of two dicts, keeping values from higher_priority_params if there are conflicts."""
def convert_jupyter_notebook_to_script(fname: str, project_dir: str) -> str: ...
def check_and_download_code_artifacts(entity: str, project: str, run_name: str, internal_api: Api, project_dir: str) -> Artifact | None: ...
def to_camel_case(maybe_snake_str: str) -> str: ...
def run_shell(args: List[str]) -> Tuple[str, str]: ...
def validate_build_and_registry_configs(build_config: Dict[str, Any], registry_config: Dict[str, Any]) -> None: ...
def get_kube_context_and_api_client(kubernetes: Any, resource_args: Dict[str, Any]) -> Tuple[Any, Any]: ...
def resolve_build_and_registry_config(default_launch_config: Dict[str, Any] | None, build_config: Dict[str, Any] | None, registry_config: Dict[str, Any] | None) -> Tuple[Dict[str, Any], Dict[str, Any]]: ...
def check_logged_in(api: Api) -> bool:
    """Check if a user is logged in.

    Raises an error if the viewer doesn't load (likely a broken API key). Expected time
    cost is 0.1-0.2 seconds.
    """
def make_name_dns_safe(name: str) -> str: ...
def warn_failed_packages_from_build_logs(log: str, image_uri: str, api: Api, job_tracker: JobAndRunStatusTracker | None) -> None: ...
def docker_image_exists(docker_image: str, should_raise: bool = False) -> bool:
    """Check if a specific image is already available.

    Optionally raises an exception if the image is not found.
    """
def pull_docker_image(docker_image: str) -> None:
    """Pull the requested docker image."""
def macro_sub(original: str, sub_dict: Dict[str, str | None]) -> str:
    """Substitute macros in a string.

    Macros occur in the string in the ${macro} format. The macro names are
    substituted with their values from the given dictionary. If a macro
    is not found in the dictionary, it is left unchanged.

    Args:
        original: The string to substitute macros in.
        sub_dict: A dictionary mapping macro names to their values.

    Returns:
        The string with the macros substituted.
    """
def recursive_macro_sub(source: Any, sub_dict: Dict[str, str | None]) -> Any:
    """Recursively substitute macros in a parsed JSON or YAML blob.

    Macros occur in strings at leaves of the blob in the ${macro} format.
    The macro names are substituted with their values from the given dictionary.
    If a macro is not found in the dictionary, it is left unchanged.

    Arguments:
        source: The JSON or YAML blob to substitute macros in.
        sub_dict: A dictionary mapping macro names to their values.

    Returns:
        The blob with the macros substituted.
    """
