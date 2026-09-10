from _typeshed import Incomplete
from optparse import Values
from pip import __version__ as __version__
from pip._internal.cli import cmdoptions as cmdoptions
from pip._internal.cli.req_command import Command as Command
from pip._internal.cli.status_codes import SUCCESS as SUCCESS
from pip._internal.metadata import BaseDistribution as BaseDistribution, get_environment as get_environment
from pip._internal.utils.compat import stdlib_pkgs as stdlib_pkgs
from pip._internal.utils.urls import path_to_url as path_to_url
from pip._vendor.packaging.markers import default_environment as default_environment
from pip._vendor.rich import print_json as print_json
from typing import List

logger: Incomplete

class InspectCommand(Command):
    """
    Inspect the content of a Python environment and produce a report in JSON format.
    """
    ignore_require_venv: bool
    usage: str
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...
