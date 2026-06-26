from _typeshed import Incomplete
from pip._internal.exceptions import BadCommand as BadCommand, InstallationError as InstallationError
from pip._internal.utils.misc import HiddenText as HiddenText, display_path as display_path
from pip._internal.utils.subprocess import make_command as make_command
from pip._internal.utils.urls import path_to_url as path_to_url
from pip._internal.vcs.versioncontrol import RevOptions as RevOptions, VersionControl as VersionControl, find_path_to_project_root_from_repo_root as find_path_to_project_root_from_repo_root, vcs as vcs
from typing import List

logger: Incomplete

class Mercurial(VersionControl):
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
    def get_remote_url(cls, location: str) -> str: ...
    @classmethod
    def get_revision(cls, location: str) -> str:
        """
        Return the repository-local changeset revision number, as an integer.
        """
    @classmethod
    def get_requirement_revision(cls, location: str) -> str:
        """
        Return the changeset identification hash, as a 40-character
        hexadecimal string
        """
    @classmethod
    def is_commit_id_equal(cls, dest: str, name: str | None) -> bool:
        """Always assume the versions don't match"""
    @classmethod
    def get_subdirectory(cls, location: str) -> str | None:
        """
        Return the path to Python project root, relative to the repo root.
        Return None if the project root is in the repo root.
        """
    @classmethod
    def get_repository_root(cls, location: str) -> str | None: ...
