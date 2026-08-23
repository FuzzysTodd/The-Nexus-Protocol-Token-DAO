from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli.base_command import Command as Command
from pip._internal.cli.status_codes import ERROR as ERROR, SUCCESS as SUCCESS
from pip._internal.operations.check import check_package_set as check_package_set, create_package_set_from_installed as create_package_set_from_installed, warn_legacy_versions_and_specifiers as warn_legacy_versions_and_specifiers
from pip._internal.utils.misc import write_output as write_output
from typing import List

logger: Incomplete

class CheckCommand(Command):
    """Verify installed packages have compatible dependencies."""
    usage: str
    def run(self, options: Values, args: List[str]) -> int: ...
