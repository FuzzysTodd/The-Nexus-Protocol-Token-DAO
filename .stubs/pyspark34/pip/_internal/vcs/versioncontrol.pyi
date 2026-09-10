from _typeshed import Incomplete
from pip._internal.cli.spinners import SpinnerInterface
from pip._internal.utils.misc import HiddenText
from pip._internal.utils.subprocess import CommandArgs
from typing import Any, Iterable, Iterator, List, Literal, Mapping, Tuple, Type

__all__ = ['vcs']

AuthInfo = Tuple[str | None, str | None]

class RemoteNotFoundError(Exception): ...

class RemoteNotValidError(Exception):
    url: Incomplete
    def __init__(self, url: str) -> None: ...

class RevOptions:
    """
    Encapsulates a VCS-specific revision to install, along with any VCS
    install options.

    Instances of this class should be treated as if immutable.
    """
    extra_args: Incomplete
    rev: Incomplete
    vc_class: Incomplete
    branch_name: Incomplete
    def __init__(self, vc_class: Type['VersionControl'], rev: str | None = None, extra_args: CommandArgs | None = None) -> None:
        """
        Args:
          vc_class: a VersionControl subclass.
          rev: the name of the revision to install.
          extra_args: a list of extra options.
        """
    @property
    def arg_rev(self) -> str | None: ...
    def to_args(self) -> CommandArgs:
        """
        Return the VCS-specific command arguments.
        """
    def to_display(self) -> str: ...
    def make_new(self, rev: str) -> RevOptions:
        """
        Make a copy of the current instance, but with a new rev.

        Args:
          rev: the name of the revision for the new object.
        """

class VcsSupport:
    schemes: Incomplete
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    @property
    def backends(self) -> List['VersionControl']: ...
    @property
    def dirnames(self) -> List[str]: ...
    @property
    def all_schemes(self) -> List[str]: ...
    def register(self, cls: Type['VersionControl']) -> None: ...
    def unregister(self, name: str) -> None: ...
    def get_backend_for_dir(self, location: str) -> VersionControl | None:
        """
        Return a VersionControl object if a repository of that type is found
        at the given directory.
        """
    def get_backend_for_scheme(self, scheme: str) -> VersionControl | None:
        """
        Return a VersionControl object or None.
        """
    def get_backend(self, name: str) -> VersionControl | None:
        """
        Return a VersionControl object or None.
        """

vcs: Incomplete

class VersionControl:
    name: str
    dirname: str
    repo_name: str
    schemes: Tuple[str, ...]
    unset_environ: Tuple[str, ...]
    default_arg_rev: str | None
    @classmethod
    def should_add_vcs_url_prefix(cls, remote_url: str) -> bool:
        '''
        Return whether the vcs prefix (e.g. "git+") should be added to a
        repository\'s remote url when used in a requirement.
        '''
    @classmethod
    def get_subdirectory(cls, location: str) -> str | None:
        """
        Return the path to Python project root, relative to the repo root.
        Return None if the project root is in the repo root.
        """
    @classmethod
    def get_requirement_revision(cls, repo_dir: str) -> str:
        """
        Return the revision string that should be used in a requirement.
        """
    @classmethod
    def get_src_requirement(cls, repo_dir: str, project_name: str) -> str:
        """
        Return the requirement string to use to redownload the files
        currently at the given repository directory.

        Args:
          project_name: the (unescaped) project name.

        The return value has a form similar to the following:

            {repository_url}@{revision}#egg={project_name}
        """
    @staticmethod
    def get_base_rev_args(rev: str) -> List[str]:
        """
        Return the base revision arguments for a vcs command.

        Args:
          rev: the name of a revision to install.  Cannot be None.
        """
    def is_immutable_rev_checkout(self, url: str, dest: str) -> bool:
        """
        Return true if the commit hash checked out at dest matches
        the revision in url.

        Always return False, if the VCS does not support immutable commit
        hashes.

        This method does not check if there are local uncommitted changes
        in dest after checkout, as pip currently has no use case for that.
        """
    @classmethod
    def make_rev_options(cls, rev: str | None = None, extra_args: CommandArgs | None = None) -> RevOptions:
        """
        Return a RevOptions object.

        Args:
          rev: the name of a revision to install.
          extra_args: a list of extra options.
        """
    @classmethod
    def get_netloc_and_auth(cls, netloc: str, scheme: str) -> Tuple[str, Tuple[str | None, str | None]]:
        """
        Parse the repository URL's netloc, and return the new netloc to use
        along with auth information.

        Args:
          netloc: the original repository URL netloc.
          scheme: the repository URL's scheme without the vcs prefix.

        This is mainly for the Subversion class to override, so that auth
        information can be provided via the --username and --password options
        instead of through the URL.  For other subclasses like Git without
        such an option, auth information must stay in the URL.

        Returns: (netloc, (username, password)).
        """
    @classmethod
    def get_url_rev_and_auth(cls, url: str) -> Tuple[str, str | None, AuthInfo]:
        """
        Parse the repository URL to use, and return the URL, revision,
        and auth info to use.

        Returns: (url, rev, (username, password)).
        """
    @staticmethod
    def make_rev_args(username: str | None, password: HiddenText | None) -> CommandArgs:
        '''
        Return the RevOptions "extra arguments" to use in obtain().
        '''
    def get_url_rev_options(self, url: HiddenText) -> Tuple[HiddenText, RevOptions]:
        """
        Return the URL and RevOptions object to use in obtain(),
        as a tuple (url, rev_options).
        """
    @staticmethod
    def normalize_url(url: str) -> str:
        """
        Normalize a URL for comparison by unquoting it and removing any
        trailing slash.
        """
    @classmethod
    def compare_urls(cls, url1: str, url2: str) -> bool:
        """
        Compare two repo URLs for identity, ignoring incidental differences.
        """
    def fetch_new(self, dest: str, url: HiddenText, rev_options: RevOptions, verbosity: int) -> None:
        """
        Fetch a revision from a repository, in the case that this is the
        first fetch from the repository.

        Args:
          dest: the directory to fetch the repository to.
          rev_options: a RevOptions object.
          verbosity: verbosity level.
        """
    def switch(self, dest: str, url: HiddenText, rev_options: RevOptions) -> None:
        """
        Switch the repo at ``dest`` to point to ``URL``.

        Args:
          rev_options: a RevOptions object.
        """
    def update(self, dest: str, url: HiddenText, rev_options: RevOptions) -> None:
        """
        Update an already-existing repo to the given ``rev_options``.

        Args:
          rev_options: a RevOptions object.
        """
    @classmethod
    def is_commit_id_equal(cls, dest: str, name: str | None) -> bool:
        """
        Return whether the id of the current commit equals the given name.

        Args:
          dest: the repository directory.
          name: a string name.
        """
    def obtain(self, dest: str, url: HiddenText, verbosity: int) -> None:
        """
        Install or update in editable mode the package represented by this
        VersionControl object.

        :param dest: the repository directory in which to install or update.
        :param url: the repository URL starting with a vcs prefix.
        :param verbosity: verbosity level.
        """
    def unpack(self, location: str, url: HiddenText, verbosity: int) -> None:
        """
        Clean up current location and download the url repository
        (and vcs infos) into location

        :param url: the repository URL starting with a vcs prefix.
        :param verbosity: verbosity level.
        """
    @classmethod
    def get_remote_url(cls, location: str) -> str:
        """
        Return the url used at location

        Raises RemoteNotFoundError if the repository does not have a remote
        url configured.
        """
    @classmethod
    def get_revision(cls, location: str) -> str:
        """
        Return the current commit id of the files at the given location.
        """
    @classmethod
    def run_command(cls, cmd: List[str] | CommandArgs, show_stdout: bool = True, cwd: str | None = None, on_returncode: Literal['raise', 'warn', 'ignore'] = 'raise', extra_ok_returncodes: Iterable[int] | None = None, command_desc: str | None = None, extra_environ: Mapping[str, Any] | None = None, spinner: SpinnerInterface | None = None, log_failed_cmd: bool = True, stdout_only: bool = False) -> str:
        """
        Run a VCS subcommand
        This is simply a wrapper around call_subprocess that adds the VCS
        command name, and checks that the VCS is available
        """
    @classmethod
    def is_repository_directory(cls, path: str) -> bool:
        """
        Return whether a directory path is a repository directory.
        """
    @classmethod
    def get_repository_root(cls, location: str) -> str | None:
        '''
        Return the "root" (top-level) directory controlled by the vcs,
        or `None` if the directory is not in any.

        It is meant to be overridden to implement smarter detection
        mechanisms for specific vcs.

        This can do more than is_repository_directory() alone. For
        example, the Git override checks that Git is actually available.
        '''
