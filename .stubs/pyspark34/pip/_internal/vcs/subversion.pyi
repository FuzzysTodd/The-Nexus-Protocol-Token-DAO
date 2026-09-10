from _typeshed import Incomplete
from pip._internal.utils.misc import HiddenText as HiddenText, display_path as display_path, is_console_interactive as is_console_interactive, is_installable_dir as is_installable_dir, split_auth_from_netloc as split_auth_from_netloc
from pip._internal.utils.subprocess import CommandArgs as CommandArgs, make_command as make_command
from pip._internal.vcs.versioncontrol import AuthInfo as AuthInfo, RemoteNotFoundError as RemoteNotFoundError, RevOptions as RevOptions, VersionControl as VersionControl, vcs as vcs
from typing import List, Tuple

logger: Incomplete

class Subversion(VersionControl):
    name: str
    dirname: str
    repo_name: str
    schemes: Incomplete
    @classmethod
    def should_add_vcs_url_prefix(cls, remote_url: str) -> bool: ...
    @staticmethod
    def get_base_rev_args(rev: str) -> List[str]: ...
    @classmethod
    def get_revision(cls, location: str) -> str:
        """
        Return the maximum revision for all files under a given location
        """
    @classmethod
    def get_netloc_and_auth(cls, netloc: str, scheme: str) -> Tuple[str, Tuple[str | None, str | None]]:
        """
        This override allows the auth information to be passed to svn via the
        --username and --password options instead of via the URL.
        """
    @classmethod
    def get_url_rev_and_auth(cls, url: str) -> Tuple[str, str | None, AuthInfo]: ...
    @staticmethod
    def make_rev_args(username: str | None, password: HiddenText | None) -> CommandArgs: ...
    @classmethod
    def get_remote_url(cls, location: str) -> str: ...
    @classmethod
    def is_commit_id_equal(cls, dest: str, name: str | None) -> bool:
        """Always assume the versions don't match"""
    use_interactive: Incomplete
    def __init__(self, use_interactive: bool | None = None) -> None: ...
    def call_vcs_version(self) -> Tuple[int, ...]:
        """Query the version of the currently installed Subversion client.

        :return: A tuple containing the parts of the version information or
            ``()`` if the version returned from ``svn`` could not be parsed.
        :raises: BadCommand: If ``svn`` is not installed.
        """
    def get_vcs_version(self) -> Tuple[int, ...]:
        """Return the version of the currently installed Subversion client.

        If the version of the Subversion client has already been queried,
        a cached value will be used.

        :return: A tuple containing the parts of the version information or
            ``()`` if the version returned from ``svn`` could not be parsed.
        :raises: BadCommand: If ``svn`` is not installed.
        """
    def get_remote_call_options(self) -> CommandArgs:
        """Return options to be used on calls to Subversion that contact the server.

        These options are applicable for the following ``svn`` subcommands used
        in this class.

            - checkout
            - switch
            - update

        :return: A list of command line arguments to pass to ``svn``.
        """
    def fetch_new(self, dest: str, url: HiddenText, rev_options: RevOptions, verbosity: int) -> None: ...
    def switch(self, dest: str, url: HiddenText, rev_options: RevOptions) -> None: ...
    def update(self, dest: str, url: HiddenText, rev_options: RevOptions) -> None: ...
