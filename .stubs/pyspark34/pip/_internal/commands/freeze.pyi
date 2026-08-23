from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli import cmdoptions as cmdoptions
from pip._internal.cli.base_command import Command as Command
from pip._internal.cli.status_codes import SUCCESS as SUCCESS
from pip._internal.operations.freeze import freeze as freeze
from pip._internal.utils.compat import stdlib_pkgs as stdlib_pkgs
from typing import List

class FreezeCommand(Command):
    """
    Output installed packages in requirements format.

    packages are listed in a case-insensitive sorted order.
    """
    usage: str
    log_streams: Incomplete
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...
