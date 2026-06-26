from typing import Any, Dict, List, Tuple
from wandb.errors import Error

__all__ = ['shell', 'build', 'run', 'image_id', 'image_id_from_registry', 'is_docker_installed', 'auth_token', 'parse', 'parse_repository_tag', 'default_image', 'get_image_uid', 'push', 'login', 'tag']

class DockerError(Error):
    """Raised when attempting to execute a docker command."""
    def __init__(self, command_launched: List[str], return_code: int, stdout: bytes | None = None, stderr: bytes | None = None) -> None: ...

def shell(cmd: List[str]) -> str | None:
    """Simple wrapper for calling docker,.

    returning None on error and the output on success
    """
def is_docker_installed() -> bool:
    """Return `True` if docker is installed and working, else `False`."""
def build(tags: List[str], file: str, context_path: str, platform: str | None = None) -> str: ...
def run(args: List[Any], capture_stdout: bool = True, capture_stderr: bool = True, input: bytes | None = None, return_stderr: bool = False, env: Dict[str, str] | None = None) -> str | Tuple[str, str]: ...
def default_image(gpu: bool = False) -> str: ...
def parse_repository_tag(repo_name: str) -> Tuple[str, str | None]: ...
def parse(image_name: str) -> Tuple[str, str, str]: ...
def auth_token(registry: str, repo: str) -> Dict[str, str]:
    """Make a request to the root of a v2 docker registry to get the auth url.

    Always returns a dictionary, if there's no token key we couldn't authenticate
    """
def image_id_from_registry(image_name: str) -> str | None:
    """Get the docker id from a public or private registry."""
def image_id(image_name: str) -> str | None:
    """Retreve the image id from the local docker daemon or remote registry."""
def get_image_uid(image_name: str) -> int:
    """Retrieve the image default uid through brute force."""
def push(image: str, tag: str) -> str | None:
    """Push an image to a remote registry."""
def login(username: str, password: str, registry: str) -> str | None:
    """Login to a registry."""
def tag(image_name: str, tag: str) -> str | None:
    """Tag an image."""
