from _typeshed import Incomplete
from pip._internal.exceptions import BadCommand as BadCommand, InstallationError as InstallationError
from pip._internal.utils.misc import HiddenText as HiddenText, display_path as display_path, hide_url as hide_url
from pip._internal.utils.subprocess import make_command as make_command
from pip._internal.vcs.versioncontrol import AuthInfo as AuthInfo, RemoteNotFoundError as RemoteNotFoundError, RemoteNotValidError as RemoteNotValidError, RevOptions as RevOptions, VersionControl as VersionControl, find_path_to_project_root_from_repo_root as find_path_to_project_root_from_repo_root, vcs as vcs
from typing import List, Tuple

urlsplit: Incomplete
urlunsplit: Incomplete
logger: Incomplete
GIT_VERSION_REGEX: Incomplete
HASH_REGEX: Incomplete
SCP_REGEX: Incomplete

def looks_like_hash(sha: str) -> bool: ...

class Git(VersionControl):
    name: str
    dirname: str
    repo_name: str
    schemes: Incomplete
    unset_environ: Incomplete
    default_arg_rev: str
    @staticmethod
    def get_base_rev_args(rev: str) -> List[str]: ...
    def is_immutable_rev_checkout(self, url: str, dest: str) -> bool: ...
    def get_git_version(self) -> Tuple[int, ...]: ...
    @classmethod
    def get_current_branch(cls, location: str) -> str | None:
        """
        Return the current branch, or None if HEAD isn't at a branch
        (e.g. detached HEAD).
        """
    @classmethod
    def get_revision_sha(cls, dest: str, rev: str) -> Tuple[str | None, bool]:
        """
        Return (sha_or_none, is_branch), where sha_or_none is a commit hash
        if the revision names a remote branch or tag, otherwise None.

        Args:
          dest: the repository directory.
          rev: the revision name.
        """
    @classmethod
    def resolve_revision(cls, dest: str, url: HiddenText, rev_options: RevOptions) -> RevOptions:
        """
        Resolve a revision to a new RevOptions object with the SHA1 of the
        branch, tag, or ref if found.

        Args:
          rev_options: a RevOptions object.
        """
    @classmethod
    def is_commit_id_equal(cls, dest: str, name: str | None) -> bool:
        """
        Return whether the current commit hash equals the given name.

        Args:
          dest: the repository directory.
          name: a string name.
        """
    def fetch_new(self, dest: str, url: HiddenText, rev_options: RevOptions, verbosity: int) -> None: ...
    def switch(self, dest: str, url: HiddenText, rev_options: RevOptions) -> None: ...
    def update(self, dest: str, url: HiddenText, rev_options: RevOptions) -> None: ...
    @classmethod
    def get_remote_url(cls, location: str) -> str:
        """
        Return URL of the first remote encountered.

        Raises RemoteNotFoundError if the repository does not have a remote
        url configured.
        """
    @classmethod
    def has_commit(cls, location: str, rev: str) -> bool:
        """
        Check if rev is a commit that is available in the local repository.
        """
    @classmethod
    def get_revision(cls, location: str, rev: str | None = None) -> str: ...
    @classmethod
    def get_subdirectory(cls, location: str) -> str | None:
        """
        Return the path to Python project root, relative to the repo root.
        Return None if the project root is in the repo root.
        """
    @classmethod
    def get_url_rev_and_auth(cls, url: str) -> Tuple[str, str | None, AuthInfo]:
        """
        Prefixes stub URLs like 'user@hostname:user/repo.git' with 'ssh://'.
        That's required because although they use SSH they sometimes don't
        work with a ssh:// scheme (e.g. GitHub). But we need a scheme for
        parsing. Hence we remove it again afterwards and return it as a stub.
        """
    @classmethod
    def update_submodules(cls, location: str) -> None: ...
    @classmethod
    def get_repository_root(cls, location: str) -> str | None: ...
    @staticmethod
    def should_add_vcs_url_prefix(repo_url: str) -> bool:
        """In either https or ssh form, requirements must be prefixed with git+."""
