from .hf_api import CommitInfo as CommitInfo, CommitOperationAdd as CommitOperationAdd, HfApi as HfApi, IGNORE_GIT_FOLDER_PATTERNS as IGNORE_GIT_FOLDER_PATTERNS
from .utils import filter_repo_objects as filter_repo_objects
from _typeshed import Incomplete
from concurrent.futures import Future
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import List

logger: Incomplete

@dataclass(frozen=True)
class _FileToUpload:
    """Temporary dataclass to store info about files to upload. Not meant to be used directly."""
    local_path: Path
    path_in_repo: str
    size_limit: int
    last_modified: float
    def __init__(self, local_path, path_in_repo, size_limit, last_modified) -> None: ...

class CommitScheduler:
    '''
    Scheduler to upload a local folder to the Hub at regular intervals (e.g. push to hub every 5 minutes).

    The scheduler is started when instantiated and run indefinitely. At the end of your script, a last commit is
    triggered. Checkout the [upload guide](https://huggingface.co/docs/huggingface_hub/guides/upload#scheduled-uploads)
    to learn more about how to use it.

    Args:
        repo_id (`str`):
            The id of the repo to commit to.
        folder_path (`str` or `Path`):
            Path to the local folder to upload regularly.
        every (`int` or `float`, *optional*):
            The number of minutes between each commit. Defaults to 5 minutes.
        path_in_repo (`str`, *optional*):
            Relative path of the directory in the repo, for example: `"checkpoints/"`. Defaults to the root folder
            of the repository.
        repo_type (`str`, *optional*):
            The type of the repo to commit to. Defaults to `model`.
        revision (`str`, *optional*):
            The revision of the repo to commit to. Defaults to `main`.
        private (`bool`, *optional*):
            Whether to make the repo private. Defaults to `False`. This value is ignored if the repo already exist.
        token (`str`, *optional*):
            The token to use to commit to the repo. Defaults to the token saved on the machine.
        allow_patterns (`List[str]` or `str`, *optional*):
            If provided, only files matching at least one pattern are uploaded.
        ignore_patterns (`List[str]` or `str`, *optional*):
            If provided, files matching any of the patterns are not uploaded.
        squash_history (`bool`, *optional*):
            Whether to squash the history of the repo after each commit. Defaults to `False`. Squashing commits is
            useful to avoid degraded performances on the repo when it grows too large.
        hf_api (`HfApi`, *optional*):
            The [`HfApi`] client to use to commit to the Hub. Can be set with custom settings (user agent, token,...).

    Example:
    ```py
    >>> from pathlib import Path
    >>> from huggingface_hub import CommitScheduler

    # Scheduler uploads every 10 minutes
    >>> csv_path = Path("watched_folder/data.csv")
    >>> CommitScheduler(repo_id="test_scheduler", repo_type="dataset", folder_path=csv_path.parent, every=10)

    >>> with csv_path.open("a") as f:
    ...     f.write("first line")

    # Some time later (...)
    >>> with csv_path.open("a") as f:
    ...     f.write("second line")
    ```
    '''
    api: Incomplete
    folder_path: Incomplete
    path_in_repo: Incomplete
    allow_patterns: Incomplete
    ignore_patterns: Incomplete
    repo_id: Incomplete
    repo_type: Incomplete
    revision: Incomplete
    token: Incomplete
    last_uploaded: Incomplete
    lock: Incomplete
    every: Incomplete
    squash_history: Incomplete
    def __init__(self, *, repo_id: str, folder_path: str | Path, every: int | float = 5, path_in_repo: str | None = None, repo_type: str | None = None, revision: str | None = None, private: bool = False, token: str | None = None, allow_patterns: List[str] | str | None = None, ignore_patterns: List[str] | str | None = None, squash_history: bool = False, hf_api: HfApi | None = None) -> None: ...
    def stop(self) -> None:
        """Stop the scheduler.

        A stopped scheduler cannot be restarted. Mostly for tests purposes.
        """
    def trigger(self) -> Future:
        """Trigger a `push_to_hub` and return a future.

        This method is automatically called every `every` minutes. You can also call it manually to trigger a commit
        immediately, without waiting for the next scheduled commit.
        """
    def push_to_hub(self) -> CommitInfo | None:
        """
        Push folder to the Hub and return the commit info.

        <Tip warning={true}>

        This method is not meant to be called directly. It is run in the background by the scheduler, respecting a
        queue mechanism to avoid concurrent commits. Making a direct call to the method might lead to concurrency
        issues.

        </Tip>

        The default behavior of `push_to_hub` is to assume an append-only folder. It lists all files in the folder and
        uploads only changed files. If no changes are found, the method returns without committing anything. If you want
        to change this behavior, you can inherit from [`CommitScheduler`] and override this method. This can be useful
        for example to compress data together in a single file before committing. For more details and examples, check
        out our [integration guide](https://huggingface.co/docs/huggingface_hub/main/en/guides/upload#scheduled-uploads).
        """

class PartialFileIO(BytesIO):
    """A file-like object that reads only the first part of a file.

    Useful to upload a file to the Hub when the user might still be appending data to it. Only the first part of the
    file is uploaded (i.e. the part that was available when the filesystem was first scanned).

    In practice, only used internally by the CommitScheduler to regularly push a folder to the Hub with minimal
    disturbance for the user. The object is passed to `CommitOperationAdd`.

    Only supports `read`, `tell` and `seek` methods.

    Args:
        file_path (`str` or `Path`):
            Path to the file to read.
        size_limit (`int`):
            The maximum number of bytes to read from the file. If the file is larger than this, only the first part
            will be read (and uploaded).
    """
    def __init__(self, file_path: str | Path, size_limit: int) -> None: ...
    def __del__(self) -> None: ...
    def __len__(self) -> int: ...
    def __getattribute__(self, name: str): ...
    def tell(self) -> int:
        """Return the current file position."""
    def seek(self, __offset: int, __whence: int = ...) -> int:
        """Change the stream position to the given offset.

        Behavior is the same as a regular file, except that the position is capped to the size limit.
        """
    def read(self, __size: int | None = -1) -> bytes:
        """Read at most `__size` bytes from the file.

        Behavior is the same as a regular file, except that it is capped to the size limit.
        """
