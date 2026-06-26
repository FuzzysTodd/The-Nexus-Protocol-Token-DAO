import fsspec
from ._commit_api import CommitOperationCopy as CommitOperationCopy, CommitOperationDelete as CommitOperationDelete
from .constants import DEFAULT_REVISION as DEFAULT_REVISION, ENDPOINT as ENDPOINT, REPO_TYPES_MAPPING as REPO_TYPES_MAPPING, REPO_TYPES_URL_PREFIXES as REPO_TYPES_URL_PREFIXES, REPO_TYPE_MODEL as REPO_TYPE_MODEL
from .hf_api import HfApi as HfApi
from .utils import EntryNotFoundError as EntryNotFoundError, HFValidationError as HFValidationError, RepositoryNotFoundError as RepositoryNotFoundError, RevisionNotFoundError as RevisionNotFoundError, hf_raise_for_status as hf_raise_for_status, http_backoff as http_backoff, paginate as paginate, parse_datetime as parse_datetime
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List

SPECIAL_REFS_REVISION_REGEX: Incomplete

@dataclass
class HfFileSystemResolvedPath:
    """Data structure containing information about a resolved Hugging Face file system path."""
    repo_type: str
    repo_id: str
    revision: str
    path_in_repo: str
    def unresolve(self) -> str: ...
    def __init__(self, repo_type, repo_id, revision, path_in_repo) -> None: ...

class HfFileSystem(fsspec.AbstractFileSystem):
    '''
    Access a remote Hugging Face Hub repository as if were a local file system.

    Args:
        endpoint (`str`, *optional*):
            The endpoint to use. If not provided, the default one (https://huggingface.co) is used.
        token (`str`, *optional*):
            Authentication token, obtained with [`HfApi.login`] method. Will default to the stored token.

    Usage:

    ```python
    >>> from huggingface_hub import HfFileSystem

    >>> fs = HfFileSystem()

    >>> # List files
    >>> fs.glob("my-username/my-model/*.bin")
    [\'my-username/my-model/pytorch_model.bin\']
    >>> fs.ls("datasets/my-username/my-dataset", detail=False)
    [\'datasets/my-username/my-dataset/.gitattributes\', \'datasets/my-username/my-dataset/README.md\', \'datasets/my-username/my-dataset/data.json\']

    >>> # Read/write files
    >>> with fs.open("my-username/my-model/pytorch_model.bin") as f:
    ...     data = f.read()
    >>> with fs.open("my-username/my-model/pytorch_model.bin", "wb") as f:
    ...     f.write(data)
    ```
    '''
    root_marker: str
    protocol: str
    endpoint: Incomplete
    token: Incomplete
    def __init__(self, *args, endpoint: str | None = None, token: str | None = None, **storage_options) -> None: ...
    def exists(self, path, **kwargs):
        """Is there a file at the given path

        Exact same implementation as in fsspec except that instead of catching all exceptions, we only catch when it's
        not a `NotImplementedError` (which we do want to raise). Catching a `NotImplementedError` can lead to undesired
        behavior.

        Adapted from https://github.com/fsspec/filesystem_spec/blob/f5d24b80a0768bf07a113647d7b4e74a3a2999e0/fsspec/spec.py#L649C1-L656C25
        """
    def resolve_path(self, path: str, revision: str | None = None) -> HfFileSystemResolvedPath: ...
    def invalidate_cache(self, path: str | None = None) -> None: ...
    def rm(self, path: str, recursive: bool = False, maxdepth: int | None = None, revision: str | None = None, **kwargs) -> None: ...
    def ls(self, path: str, detail: bool = True, refresh: bool = False, revision: str | None = None, **kwargs) -> List[str | Dict[str, Any]]:
        """List the contents of a directory."""
    def cp_file(self, path1: str, path2: str, revision: str | None = None, **kwargs) -> None: ...
    def modified(self, path: str, **kwargs) -> datetime: ...
    def info(self, path: str, **kwargs) -> Dict[str, Any]: ...

class HfFileSystemFile(fsspec.spec.AbstractBufferedFile):
    fs: Incomplete
    resolved_path: Incomplete
    def __init__(self, fs: HfFileSystem, path: str, revision: str | None = None, **kwargs) -> None: ...

def safe_revision(revision: str) -> str: ...
def safe_quote(s: str) -> str: ...
