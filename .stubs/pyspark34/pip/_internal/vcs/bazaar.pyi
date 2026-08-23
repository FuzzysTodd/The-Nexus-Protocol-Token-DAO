from _typeshed import Incomplete
from pip._internal.utils.misc import HiddenText as HiddenText, display_path as display_path
from pip._internal.utils.subprocess import make_command as make_command
from pip._internal.utils.urls import path_to_url as path_to_url
from pip._internal.vcs.versioncontrol import AuthInfo as AuthInfo, RemoteNotFoundError as RemoteNotFoundError, RevOptions as RevOptions, VersionControl as VersionControl, vcs as vcs
from typing import List, Tuple

logger: Incomplete

class Bazaar(VersionControl):
    name: str
    dirname: str
    repo_name: str
    schemes: Incomplete
    @staticmethod
    def get_base_rev_args(rev: str) -> List[str]: ...
    def fetch_new(self, dest: str, url: HiddenText, rev_options: RevOptions, verbosity: int) -> None: ...
    def switch(self, dest: str, url: HiddenText, rev_options: RevOptions) -> None: ...
    def update(self, dest: str, url: HiddenText, rev_options: RevOptions) -> None: ...
    @classmethod
    def get_url_rev_and_auth(cls, url: str) -> Tuple[str, str | None, AuthInfo]: ...
    @classmethod
    def get_remote_url(cls, location: str) -> str: ...
    @classmethod
    def get_revision(cls, location: str) -> str: ...
    @classmethod
    def is_commit_id_equal(cls, dest: str, name: str | None) -> bool:
        """Always assume the versions don't match"""
