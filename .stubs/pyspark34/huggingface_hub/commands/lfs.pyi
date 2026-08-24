import abc
from ..utils import get_session as get_session, hf_raise_for_status as hf_raise_for_status, logging as logging
from _typeshed import Incomplete
from argparse import _SubParsersAction
from huggingface_hub.commands import BaseHuggingfaceCLICommand as BaseHuggingfaceCLICommand
from huggingface_hub.lfs import LFS_MULTIPART_UPLOAD_COMMAND as LFS_MULTIPART_UPLOAD_COMMAND, SliceFileObj as SliceFileObj
from typing import Dict

logger: Incomplete

class LfsCommands(BaseHuggingfaceCLICommand, metaclass=abc.ABCMeta):
    '''
    Implementation of a custom transfer agent for the transfer type "multipart"
    for git-lfs. This lets users upload large files >5GB 🔥. Spec for LFS custom
    transfer agent is:
    https://github.com/git-lfs/git-lfs/blob/master/docs/custom-transfers.md

    This introduces two commands to the CLI:

    1. $ huggingface-cli lfs-enable-largefiles

    This should be executed once for each model repo that contains a model file
    >5GB. It\'s documented in the error message you get if you just try to git
    push a 5GB file without having enabled it before.

    2. $ huggingface-cli lfs-multipart-upload

    This command is called by lfs directly and is not meant to be called by the
    user.
    '''
    @staticmethod
    def register_subcommand(parser: _SubParsersAction): ...

class LfsEnableCommand:
    args: Incomplete
    def __init__(self, args) -> None: ...
    def run(self) -> None: ...

def write_msg(msg: Dict):
    """Write out the message in Line delimited JSON."""
def read_msg() -> Dict | None:
    """Read Line delimited JSON from stdin."""

class LfsUploadCommand:
    args: Incomplete
    def __init__(self, args) -> None: ...
    def run(self) -> None: ...
