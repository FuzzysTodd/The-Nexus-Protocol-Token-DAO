from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli.base_command import Command as Command
from pip._internal.cli.status_codes import SUCCESS as SUCCESS
from pip._internal.utils.misc import get_prog as get_prog
from typing import List

BASE_COMPLETION: str
COMPLETION_SCRIPTS: Incomplete

class CompletionCommand(Command):
    """A helper command to be used for command completion."""
    ignore_require_venv: bool
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int:
        """Prints the completion code of the given shell"""
