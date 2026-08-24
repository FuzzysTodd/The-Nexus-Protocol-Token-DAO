from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli.base_command import Command as Command
from pip._internal.cli.status_codes import ERROR as ERROR, SUCCESS as SUCCESS
from pip._internal.utils.hashes import FAVORITE_HASH as FAVORITE_HASH, STRONG_HASHES as STRONG_HASHES
from pip._internal.utils.misc import read_chunks as read_chunks, write_output as write_output
from typing import List

logger: Incomplete

class HashCommand(Command):
    """
    Compute a hash of a local package archive.

    These can be used with --hash in a requirements file to do repeatable
    installs.
    """
    usage: str
    ignore_require_venv: bool
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...
