from optparse import Values
from pip._internal.cli.base_command import Command as Command
from pip._internal.cli.status_codes import SUCCESS as SUCCESS
from pip._internal.exceptions import CommandError as CommandError
from typing import List

class HelpCommand(Command):
    """Show help for commands"""
    usage: str
    ignore_require_venv: bool
    def run(self, options: Values, args: List[str]) -> int: ...
