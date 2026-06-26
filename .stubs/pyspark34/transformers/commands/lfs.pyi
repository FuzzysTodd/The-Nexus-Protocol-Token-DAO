import abc
from . import BaseTransformersCLICommand as BaseTransformersCLICommand
from ..utils import logging as logging
from _typeshed import Incomplete
from argparse import ArgumentParser
from contextlib import AbstractContextManager
from typing import Dict, Optional

logger: Incomplete
LFS_MULTIPART_UPLOAD_COMMAND: str

class LfsCommands(BaseTransformersCLICommand, metaclass=abc.ABCMeta):
    '''
    Implementation of a custom transfer agent for the transfer type "multipart" for git-lfs. This lets users upload
    large files >5GB 🔥. Spec for LFS custom transfer agent is:
    https://github.com/git-lfs/git-lfs/blob/master/docs/custom-transfers.md

    This introduces two commands to the CLI:

    1. $ transformers-cli lfs-enable-largefiles

    This should be executed once for each model repo that contains a model file >5GB. It\'s documented in the error
    message you get if you just try to git push a 5GB file without having enabled it before.

    2. $ transformers-cli lfs-multipart-upload

    This command is called by lfs directly and is not meant to be called by the user.
    '''
    @staticmethod
    def register_subcommand(parser: ArgumentParser): ...

class LfsEnableCommand:
    args: Incomplete
    def __init__(self, args) -> None: ...
    def run(self) -> None: ...

def write_msg(msg: Dict):
    """Write out the message in Line delimited JSON."""
def read_msg() -> Optional[Dict]:
    """Read Line delimited JSON from stdin."""

class FileSlice(AbstractContextManager):
    """
    File-like object that only reads a slice of a file

    Inspired by stackoverflow.com/a/29838711/593036
    """
    filepath: Incomplete
    seek_from: Incomplete
    read_limit: Incomplete
    n_seen: int
    def __init__(self, filepath: str, seek_from: int, read_limit: int) -> None: ...
    f: Incomplete
    def __enter__(self): ...
    def __len__(self) -> int: ...
    def read(self, n: int = -1): ...
    def __iter__(self): ...
    def __exit__(self, *args) -> None: ...

class LfsUploadCommand:
    args: Incomplete
    def __init__(self, args) -> None: ...
    def run(self) -> None: ...
