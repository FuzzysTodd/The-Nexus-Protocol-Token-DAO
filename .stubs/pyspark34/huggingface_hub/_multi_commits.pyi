from ._commit_api import CommitOperationAdd as CommitOperationAdd, CommitOperationDelete as CommitOperationDelete
from .community import DiscussionWithDetails as DiscussionWithDetails
from .hf_api import HfApi as HfApi
from .utils import experimental as experimental
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Iterable, List, Set, Tuple

class MultiCommitException(Exception):
    """Base exception for any exception happening while doing a multi-commit."""

MULTI_COMMIT_PR_DESCRIPTION_TEMPLATE: str
MULTI_COMMIT_PR_COMPLETION_COMMENT_TEMPLATE: str
MULTI_COMMIT_PR_CLOSING_COMMENT_TEMPLATE: str
MULTI_COMMIT_PR_CLOSE_COMMENT_FAILURE_NO_CHANGES_TEMPLATE: str
MULTI_COMMIT_PR_CLOSE_COMMENT_FAILURE_BAD_REQUEST_TEMPLATE: str
STEP_ID_REGEX: Incomplete

def plan_multi_commits(operations: Iterable[CommitOperationAdd | CommitOperationDelete], max_operations_per_commit: int = 50, max_upload_size_per_commit: int = ...) -> Tuple[List[List[CommitOperationAdd]], List[List[CommitOperationDelete]]]:
    '''Split a list of operations in a list of commits to perform.

    Implementation follows a sub-optimal (yet simple) algorithm:
    1. Delete operations are grouped together by commits of maximum `max_operations_per_commits` operations.
    2. All additions exceeding `max_upload_size_per_commit` are committed 1 by 1.
    3. All remaining additions are grouped together and split each time the `max_operations_per_commit` or the
       `max_upload_size_per_commit` limit is reached.

    We do not try to optimize the splitting to get the lowest number of commits as this is a NP-hard problem (see
    [bin packing problem](https://en.wikipedia.org/wiki/Bin_packing_problem)). For our use case, it is not problematic
    to use a sub-optimal solution so we favored an easy-to-explain implementation.

    Args:
        operations (`List` of [`~hf_api.CommitOperation`]):
            The list of operations to split into commits.
        max_operations_per_commit (`int`):
            Maximum number of operations in a single commit. Defaults to 50.
        max_upload_size_per_commit (`int`):
            Maximum size to upload (in bytes) in a single commit. Defaults to 2GB. Files bigger than this limit are
            uploaded, 1 per commit.

    Returns:
        `Tuple[List[List[CommitOperationAdd]], List[List[CommitOperationDelete]]]`: a tuple. First item is a list of
        lists of [`CommitOperationAdd`] representing the addition commits to push. The second item is a list of lists
        of [`CommitOperationDelete`] representing the deletion commits.

    <Tip warning={true}>

    `plan_multi_commits` is experimental. Its API and behavior is subject to change in the future without prior notice.

    </Tip>

    Example:
    ```python
    >>> from huggingface_hub import HfApi, plan_multi_commits
    >>> addition_commits, deletion_commits = plan_multi_commits(
    ...     operations=[
    ...          CommitOperationAdd(...),
    ...          CommitOperationAdd(...),
    ...          CommitOperationDelete(...),
    ...          CommitOperationDelete(...),
    ...          CommitOperationAdd(...),
    ...     ],
    ... )
    >>> HfApi().create_commits_on_pr(
    ...     repo_id="my-cool-model",
    ...     addition_commits=addition_commits,
    ...     deletion_commits=deletion_commits,
    ...     (...)
    ...     verbose=True,
    ... )
    ```

    <Tip warning={true}>

    The initial order of the operations is not guaranteed! All deletions will be performed before additions. If you are
    not updating multiple times the same file, you are fine.

    </Tip>
    '''

@dataclass
class MultiCommitStep:
    """Dataclass containing a list of CommitOperation to commit at once.

    A [`MultiCommitStep`] is one atomic part of a [`MultiCommitStrategy`]. Each step is identified by its own
    deterministic ID based on the list of commit operations (hexadecimal sha256). ID is persistent between re-runs if
    the list of commits is kept the same.
    """
    operations: List[CommitOperationAdd | CommitOperationDelete]
    id: str = ...
    completed: bool = ...
    def __post_init__(self) -> None: ...
    def __init__(self, operations, completed) -> None: ...

@dataclass
class MultiCommitStrategy:
    """Dataclass containing a list of [`MultiCommitStep`] to commit iteratively.

    A strategy is identified by its own deterministic ID based on the list of its steps (hexadecimal sha256). ID is
    persistent between re-runs if the list of commits is kept the same.
    """
    addition_commits: List[MultiCommitStep]
    deletion_commits: List[MultiCommitStep]
    id: str = ...
    all_steps: Set[str] = ...
    def __post_init__(self) -> None: ...
    def __init__(self, addition_commits, deletion_commits) -> None: ...

def multi_commit_create_pull_request(api: HfApi, repo_id: str, commit_message: str, commit_description: str | None, strategy: MultiCommitStrategy, token: str | None, repo_type: str | None) -> DiscussionWithDetails: ...
def multi_commit_generate_comment(commit_message: str, commit_description: str | None, strategy: MultiCommitStrategy) -> str: ...
def multi_commit_parse_pr_description(description: str) -> Set[str]: ...
