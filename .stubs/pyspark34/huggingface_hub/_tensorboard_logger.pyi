from .utils import experimental as experimental, is_tensorboard_available as is_tensorboard_available
from _typeshed import Incomplete
from huggingface_hub._commit_scheduler import CommitScheduler as CommitScheduler
from tensorboardX import SummaryWriter
from typing import List

SummaryWriter = object

class HFSummaryWriter(SummaryWriter):
    '''
    Wrapper around the tensorboard\'s `SummaryWriter` to push training logs to the Hub.

    Data is logged locally and then pushed to the Hub asynchronously. Pushing data to the Hub is done in a separate
    thread to avoid blocking the training script. In particular, if the upload fails for any reason (e.g. a connection
    issue), the main script will not be interrupted. Data is automatically pushed to the Hub every `commit_every`
    minutes (default to every 5 minutes).

    <Tip warning={true}>

    `HFSummaryWriter` is experimental. Its API is subject to change in the future without prior notice.

    </Tip>

    Args:
        repo_id (`str`):
            The id of the repo to which the logs will be pushed.
        logdir (`str`, *optional*):
            The directory where the logs will be written. If not specified, a local directory will be created by the
            underlying `SummaryWriter` object.
        commit_every (`int` or `float`, *optional*):
            The frequency (in minutes) at which the logs will be pushed to the Hub. Defaults to 5 minutes.
        squash_history (`bool`, *optional*):
            Whether to squash the history of the repo after each commit. Defaults to `False`. Squashing commits is
            useful to avoid degraded performances on the repo when it grows too large.
        repo_type (`str`, *optional*):
            The type of the repo to which the logs will be pushed. Defaults to "model".
        repo_revision (`str`, *optional*):
            The revision of the repo to which the logs will be pushed. Defaults to "main".
        repo_private (`bool`, *optional*):
            Whether to create a private repo or not. Defaults to False. This argument is ignored if the repo already
            exists.
        path_in_repo (`str`, *optional*):
            The path to the folder in the repo where the logs will be pushed. Defaults to "tensorboard/".
        repo_allow_patterns (`List[str]` or `str`, *optional*):
            A list of patterns to include in the upload. Defaults to `"*.tfevents.*"`. Check out the
            [upload guide](https://huggingface.co/docs/huggingface_hub/guides/upload#upload-a-folder) for more details.
        repo_ignore_patterns (`List[str]` or `str`, *optional*):
            A list of patterns to exclude in the upload. Check out the
            [upload guide](https://huggingface.co/docs/huggingface_hub/guides/upload#upload-a-folder) for more details.
        token (`str`, *optional*):
            Authentication token. Will default to the stored token. See https://huggingface.co/settings/token for more
            details
        kwargs:
            Additional keyword arguments passed to `SummaryWriter`.

    Examples:
    ```py
    >>> from huggingface_hub import HFSummaryWriter

    # Logs are automatically pushed every 15 minutes
    >>> logger = HFSummaryWriter(repo_id="test_hf_logger", commit_every=15)
    >>> logger.add_scalar("a", 1)
    >>> logger.add_scalar("b", 2)
    ...

    # You can also trigger a push manually
    >>> logger.scheduler.trigger()
    ```

    ```py
    >>> from huggingface_hub import HFSummaryWriter

    # Logs are automatically pushed every 5 minutes (default) + when exiting the context manager
    >>> with HFSummaryWriter(repo_id="test_hf_logger") as logger:
    ...     logger.add_scalar("a", 1)
    ...     logger.add_scalar("b", 2)
    ```
    '''
    def __new__(cls, *args, **kwargs) -> HFSummaryWriter: ...
    scheduler: Incomplete
    repo_id: Incomplete
    repo_type: Incomplete
    repo_revision: Incomplete
    def __init__(self, repo_id: str, *, logdir: str | None = None, commit_every: int | float = 5, squash_history: bool = False, repo_type: str | None = None, repo_revision: str | None = None, repo_private: bool = False, path_in_repo: str | None = 'tensorboard', repo_allow_patterns: List[str] | str | None = '*.tfevents.*', repo_ignore_patterns: List[str] | str | None = None, token: str | None = None, **kwargs) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None:
        """Push to hub in a non-blocking way when exiting the logger's context manager."""
