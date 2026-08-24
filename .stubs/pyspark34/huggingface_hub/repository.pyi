import subprocess
from .hf_api import HfApi as HfApi, repo_type_and_id_from_hf_id as repo_type_and_id_from_hf_id
from .lfs import LFS_MULTIPART_UPLOAD_COMMAND as LFS_MULTIPART_UPLOAD_COMMAND
from .utils import HfFolder as HfFolder, SoftTemporaryDirectory as SoftTemporaryDirectory, logging as logging, run_subprocess as run_subprocess, tqdm as tqdm, validate_hf_hub_args as validate_hf_hub_args
from _typeshed import Incomplete
from huggingface_hub.constants import REPOCARD_NAME as REPOCARD_NAME, REPO_TYPES_URL_PREFIXES as REPO_TYPES_URL_PREFIXES
from huggingface_hub.repocard import metadata_load as metadata_load, metadata_save as metadata_save
from pathlib import Path
from typing import Callable, Dict, List, Tuple, TypedDict

logger: Incomplete

class CommandInProgress:
    """
    Utility to follow commands launched asynchronously.
    """
    title: Incomplete
    def __init__(self, title: str, is_done_method: Callable, status_method: Callable, process: subprocess.Popen, post_method: Callable | None = None) -> None: ...
    @property
    def is_done(self) -> bool:
        """
        Whether the process is done.
        """
    @property
    def status(self) -> int:
        """
        The exit code/status of the current action. Will return `0` if the
        command has completed successfully, and a number between 1 and 255 if
        the process errored-out.

        Will return -1 if the command is still ongoing.
        """
    @property
    def failed(self) -> bool:
        """
        Whether the process errored-out.
        """
    @property
    def stderr(self) -> str:
        """
        The current output message on the standard error.
        """
    @property
    def stdout(self) -> str:
        """
        The current output message on the standard output.
        """

def is_git_repo(folder: str | Path) -> bool:
    """
    Check if the folder is the root or part of a git repository

    Args:
        folder (`str`):
            The folder in which to run the command.

    Returns:
        `bool`: `True` if the repository is part of a repository, `False`
        otherwise.
    """
def is_local_clone(folder: str | Path, remote_url: str) -> bool:
    """
    Check if the folder is a local clone of the remote_url

    Args:
        folder (`str` or `Path`):
            The folder in which to run the command.
        remote_url (`str`):
            The url of a git repository.

    Returns:
        `bool`: `True` if the repository is a local clone of the remote
        repository specified, `False` otherwise.
    """
def is_tracked_with_lfs(filename: str | Path) -> bool:
    """
    Check if the file passed is tracked with git-lfs.

    Args:
        filename (`str` or `Path`):
            The filename to check.

    Returns:
        `bool`: `True` if the file passed is tracked with git-lfs, `False`
        otherwise.
    """
def is_git_ignored(filename: str | Path) -> bool:
    """
    Check if file is git-ignored. Supports nested .gitignore files.

    Args:
        filename (`str` or `Path`):
            The filename to check.

    Returns:
        `bool`: `True` if the file passed is ignored by `git`, `False`
        otherwise.
    """
def is_binary_file(filename: str | Path) -> bool:
    """
    Check if file is a binary file.

    Args:
        filename (`str` or `Path`):
            The filename to check.

    Returns:
        `bool`: `True` if the file passed is a binary file, `False` otherwise.
    """
def files_to_be_staged(pattern: str = '.', folder: str | Path | None = None) -> List[str]:
    """
    Returns a list of filenames that are to be staged.

    Args:
        pattern (`str` or `Path`):
            The pattern of filenames to check. Put `.` to get all files.
        folder (`str` or `Path`):
            The folder in which to run the command.

    Returns:
        `List[str]`: List of files that are to be staged.
    """
def is_tracked_upstream(folder: str | Path) -> bool:
    """
    Check if the current checked-out branch is tracked upstream.

    Args:
        folder (`str` or `Path`):
            The folder in which to run the command.

    Returns:
        `bool`: `True` if the current checked-out branch is tracked upstream,
        `False` otherwise.
    """
def commits_to_push(folder: str | Path, upstream: str | None = None) -> int:
    """
        Check the number of commits that would be pushed upstream

        Args:
            folder (`str` or `Path`):
                The folder in which to run the command.
            upstream (`str`, *optional*):
    The name of the upstream repository with which the comparison should be
    made.

        Returns:
            `int`: Number of commits that would be pushed upstream were a `git
            push` to proceed.
    """

class PbarT(TypedDict):
    bar: tqdm
    past_bytes: int

class Repository:
    """
    Helper class to wrap the git and git-lfs commands.

    The aim is to facilitate interacting with huggingface.co hosted model or
    dataset repos, though not a lot here (if any) is actually specific to
    huggingface.co.
    """
    command_queue: List[CommandInProgress]
    local_dir: Incomplete
    skip_lfs_files: Incomplete
    client: Incomplete
    huggingface_token: Incomplete
    def __init__(self, local_dir: str | Path, clone_from: str | None = None, repo_type: str | None = None, token: bool | str = True, git_user: str | None = None, git_email: str | None = None, revision: str | None = None, skip_lfs_files: bool = False, client: HfApi | None = None) -> None:
        '''
        Instantiate a local clone of a git repo.

        If `clone_from` is set, the repo will be cloned from an existing remote repository.
        If the remote repo does not exist, a `EnvironmentError` exception will be thrown.
        Please create the remote repo first using [`create_repo`].

        `Repository` uses the local git credentials by default. If explicitly set, the `token`
        or the `git_user`/`git_email` pair will be used instead.

        Args:
            local_dir (`str` or `Path`):
                path (e.g. `\'my_trained_model/\'`) to the local directory, where
                the `Repository` will be initialized.
            clone_from (`str`, *optional*):
                Either a repository url or `repo_id`.
                Example:
                - `"https://huggingface.co/philschmid/playground-tests"`
                - `"philschmid/playground-tests"`
            repo_type (`str`, *optional*):
                To set when cloning a repo from a repo_id. Default is model.
            token (`bool` or `str`, *optional*):
                A valid authentication token (see https://huggingface.co/settings/token).
                If `None` or `True` and machine is logged in (through `huggingface-cli login`
                or [`~huggingface_hub.login`]), token will be retrieved from the cache.
                If `False`, token is not sent in the request header.
            git_user (`str`, *optional*):
                will override the `git config user.name` for committing and
                pushing files to the hub.
            git_email (`str`, *optional*):
                will override the `git config user.email` for committing and
                pushing files to the hub.
            revision (`str`, *optional*):
                Revision to checkout after initializing the repository. If the
                revision doesn\'t exist, a branch will be created with that
                revision name from the default branch\'s current HEAD.
            skip_lfs_files (`bool`, *optional*, defaults to `False`):
                whether to skip git-LFS files or not.
            client (`HfApi`, *optional*):
                Instance of [`HfApi`] to use when calling the HF Hub API. A new
                instance will be created if this is left to `None`.

        Raises:
            - [`EnvironmentError`](https://docs.python.org/3/library/exceptions.html#EnvironmentError)
              if the remote repository set in `clone_from` does not exist.
        '''
    @property
    def current_branch(self) -> str:
        """
        Returns the current checked out branch.

        Returns:
            `str`: Current checked out branch.
        """
    def check_git_versions(self) -> None:
        """
        Checks that `git` and `git-lfs` can be run.

        Raises:
            - [`EnvironmentError`](https://docs.python.org/3/library/exceptions.html#EnvironmentError)
              if `git` or `git-lfs` are not installed.
        """
    def clone_from(self, repo_url: str, token: bool | str | None = None):
        '''
        Clone from a remote. If the folder already exists, will try to clone the
        repository within it.

        If this folder is a git repository with linked history, will try to
        update the repository.

        Args:
            repo_url (`str`):
                The URL from which to clone the repository
            token (`Union[str, bool]`, *optional*):
                Whether to use the authentication token. It can be:
                 - a string which is the token itself
                 - `False`, which would not use the authentication token
                 - `True`, which would fetch the authentication token from the
                   local folder and use it (you should be logged in for this to
                   work).
                - `None`, which would retrieve the value of
                  `self.huggingface_token`.

        <Tip>

        Raises the following error:

            - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
              if an organization token (starts with "api_org") is passed. Use must use
              your own personal access token (see https://hf.co/settings/tokens).

            - [`EnvironmentError`](https://docs.python.org/3/library/exceptions.html#EnvironmentError)
              if you are trying to clone the repository in a non-empty folder, or if the
              `git` operations raise errors.

        </Tip>
        '''
    def git_config_username_and_email(self, git_user: str | None = None, git_email: str | None = None):
        """
        Sets git username and email (only in the current repo).

        Args:
            git_user (`str`, *optional*):
                The username to register through `git`.
            git_email (`str`, *optional*):
                The email to register through `git`.
        """
    def git_credential_helper_store(self) -> None:
        """
        Sets the git credential helper to `store`
        """
    def git_head_hash(self) -> str:
        """
        Get commit sha on top of HEAD.

        Returns:
            `str`: The current checked out commit SHA.
        """
    def git_remote_url(self) -> str:
        """
        Get URL to origin remote.

        Returns:
            `str`: The URL of the `origin` remote.
        """
    def git_head_commit_url(self) -> str:
        """
        Get URL to last commit on HEAD. We assume it's been pushed, and the url
        scheme is the same one as for GitHub or HuggingFace.

        Returns:
            `str`: The URL to the current checked-out commit.
        """
    def list_deleted_files(self) -> List[str]:
        """
        Returns a list of the files that are deleted in the working directory or
        index.

        Returns:
            `List[str]`: A list of files that have been deleted in the working
            directory or index.
        """
    def lfs_track(self, patterns: str | List[str], filename: bool = False):
        """
        Tell git-lfs to track files according to a pattern.

        Setting the `filename` argument to `True` will treat the arguments as
        literal filenames, not as patterns. Any special glob characters in the
        filename will be escaped when writing to the `.gitattributes` file.

        Args:
            patterns (`Union[str, List[str]]`):
                The pattern, or list of patterns, to track with git-lfs.
            filename (`bool`, *optional*, defaults to `False`):
                Whether to use the patterns as literal filenames.
        """
    def lfs_untrack(self, patterns: str | List[str]):
        """
        Tell git-lfs to untrack those files.

        Args:
            patterns (`Union[str, List[str]]`):
                The pattern, or list of patterns, to untrack with git-lfs.
        """
    def lfs_enable_largefiles(self) -> None:
        """
        HF-specific. This enables upload support of files >5GB.
        """
    def auto_track_binary_files(self, pattern: str = '.') -> List[str]:
        '''
        Automatically track binary files with git-lfs.

        Args:
            pattern (`str`, *optional*, defaults to "."):
                The pattern with which to track files that are binary.

        Returns:
            `List[str]`: List of filenames that are now tracked due to being
            binary files
        '''
    def auto_track_large_files(self, pattern: str = '.') -> List[str]:
        '''
        Automatically track large files (files that weigh more than 10MBs) with
        git-lfs.

        Args:
            pattern (`str`, *optional*, defaults to "."):
                The pattern with which to track files that are above 10MBs.

        Returns:
            `List[str]`: List of filenames that are now tracked due to their
            size.
        '''
    def lfs_prune(self, recent: bool = False) -> None:
        """
        git lfs prune

        Args:
            recent (`bool`, *optional*, defaults to `False`):
                Whether to prune files even if they were referenced by recent
                commits. See the following
                [link](https://github.com/git-lfs/git-lfs/blob/f3d43f0428a84fc4f1e5405b76b5a73ec2437e65/docs/man/git-lfs-prune.1.ronn#recent-files)
                for more information.
        """
    def git_pull(self, rebase: bool = False, lfs: bool = False):
        """
        git pull

        Args:
            rebase (`bool`, *optional*, defaults to `False`):
                Whether to rebase the current branch on top of the upstream
                branch after fetching.
            lfs (`bool`, *optional*, defaults to `False`):
                Whether to fetch the LFS files too. This option only changes the
                behavior when a repository was cloned without fetching the LFS
                files; calling `repo.git_pull(lfs=True)` will then fetch the LFS
                file from the remote repository.
        """
    def git_add(self, pattern: str = '.', auto_lfs_track: bool = False):
        '''
        git add

        Setting the `auto_lfs_track` parameter to `True` will automatically
        track files that are larger than 10MB with `git-lfs`.

        Args:
            pattern (`str`, *optional*, defaults to "."):
                The pattern with which to add files to staging.
            auto_lfs_track (`bool`, *optional*, defaults to `False`):
                Whether to automatically track large and binary files with
                git-lfs. Any file over 10MB in size, or in binary format, will
                be automatically tracked.
        '''
    def git_commit(self, commit_message: str = 'commit files to HF hub'):
        '''
        git commit

        Args:
            commit_message (`str`, *optional*, defaults to "commit files to HF hub"):
                The message attributed to the commit.
        '''
    def git_push(self, upstream: str | None = None, blocking: bool = True, auto_lfs_prune: bool = False) -> str | Tuple[str, CommandInProgress]:
        """
        git push

        If used without setting `blocking`, will return url to commit on remote
        repo. If used with `blocking=True`, will return a tuple containing the
        url to commit and the command object to follow for information about the
        process.

        Args:
            upstream (`str`, *optional*):
                Upstream to which this should push. If not specified, will push
                to the lastly defined upstream or to the default one (`origin
                main`).
            blocking (`bool`, *optional*, defaults to `True`):
                Whether the function should return only when the push has
                finished. Setting this to `False` will return an
                `CommandInProgress` object which has an `is_done` property. This
                property will be set to `True` when the push is finished.
            auto_lfs_prune (`bool`, *optional*, defaults to `False`):
                Whether to automatically prune files once they have been pushed
                to the remote.
        """
    def git_checkout(self, revision: str, create_branch_ok: bool = False):
        """
        git checkout a given revision

        Specifying `create_branch_ok` to `True` will create the branch to the
        given revision if that revision doesn't exist.

        Args:
            revision (`str`):
                The revision to checkout.
            create_branch_ok (`str`, *optional*, defaults to `False`):
                Whether creating a branch named with the `revision` passed at
                the current checked-out reference if `revision` isn't an
                existing revision is allowed.
        """
    def tag_exists(self, tag_name: str, remote: str | None = None) -> bool:
        """
        Check if a tag exists or not.

        Args:
            tag_name (`str`):
                The name of the tag to check.
            remote (`str`, *optional*):
                Whether to check if the tag exists on a remote. This parameter
                should be the identifier of the remote.

        Returns:
            `bool`: Whether the tag exists.
        """
    def delete_tag(self, tag_name: str, remote: str | None = None) -> bool:
        """
        Delete a tag, both local and remote, if it exists

        Args:
            tag_name (`str`):
                The tag name to delete.
            remote (`str`, *optional*):
                The remote on which to delete the tag.

        Returns:
             `bool`: `True` if deleted, `False` if the tag didn't exist.
                If remote is not passed, will just be updated locally
        """
    def add_tag(self, tag_name: str, message: str | None = None, remote: str | None = None):
        """
        Add a tag at the current head and push it

        If remote is None, will just be updated locally

        If no message is provided, the tag will be lightweight. if a message is
        provided, the tag will be annotated.

        Args:
            tag_name (`str`):
                The name of the tag to be added.
            message (`str`, *optional*):
                The message that accompanies the tag. The tag will turn into an
                annotated tag if a message is passed.
            remote (`str`, *optional*):
                The remote on which to add the tag.
        """
    def is_repo_clean(self) -> bool:
        """
        Return whether or not the git status is clean or not

        Returns:
            `bool`: `True` if the git status is clean, `False` otherwise.
        """
    def push_to_hub(self, commit_message: str = 'commit files to HF hub', blocking: bool = True, clean_ok: bool = True, auto_lfs_prune: bool = False) -> None | str | Tuple[str, CommandInProgress]:
        """
        Helper to add, commit, and push files to remote repository on the
        HuggingFace Hub. Will automatically track large files (>10MB).

        Args:
            commit_message (`str`):
                Message to use for the commit.
            blocking (`bool`, *optional*, defaults to `True`):
                Whether the function should return only when the `git push` has
                finished.
            clean_ok (`bool`, *optional*, defaults to `True`):
                If True, this function will return None if the repo is
                untouched. Default behavior is to fail because the git command
                fails.
            auto_lfs_prune (`bool`, *optional*, defaults to `False`):
                Whether to automatically prune files once they have been pushed
                to the remote.
        """
    def commit(self, commit_message: str, branch: str | None = None, track_large_files: bool = True, blocking: bool = True, auto_lfs_prune: bool = False):
        '''
        Context manager utility to handle committing to a repository. This
        automatically tracks large files (>10Mb) with git-lfs. Set the
        `track_large_files` argument to `False` if you wish to ignore that
        behavior.

        Args:
            commit_message (`str`):
                Message to use for the commit.
            branch (`str`, *optional*):
                The branch on which the commit will appear. This branch will be
                checked-out before any operation.
            track_large_files (`bool`, *optional*, defaults to `True`):
                Whether to automatically track large files or not. Will do so by
                default.
            blocking (`bool`, *optional*, defaults to `True`):
                Whether the function should return only when the `git push` has
                finished.
            auto_lfs_prune (`bool`, defaults to `True`):
                Whether to automatically prune files once they have been pushed
                to the remote.

        Examples:

        ```python
        >>> with Repository(
        ...     "text-files",
        ...     clone_from="<user>/text-files",
        ...     token=True,
        >>> ).commit("My first file :)"):
        ...     with open("file.txt", "w+") as f:
        ...         f.write(json.dumps({"hey": 8}))

        >>> import torch

        >>> model = torch.nn.Transformer()
        >>> with Repository(
        ...     "torch-model",
        ...     clone_from="<user>/torch-model",
        ...     token=True,
        >>> ).commit("My cool model :)"):
        ...     torch.save(model.state_dict(), "model.pt")
        ```

        '''
    def repocard_metadata_load(self) -> Dict | None: ...
    def repocard_metadata_save(self, data: Dict) -> None: ...
    @property
    def commands_failed(self):
        """
        Returns the asynchronous commands that failed.
        """
    @property
    def commands_in_progress(self):
        """
        Returns the asynchronous commands that are currently in progress.
        """
    def wait_for_commands(self) -> None:
        """
        Blocking method: blocks all subsequent execution until all commands have
        been processed.
        """
